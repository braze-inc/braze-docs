---
nav_title: Ingestion de données cloud
article_title: Ingestion de données cloud de Braze
alias: /cloud_ingestion/
description: "Cet article de référence traite de l’ingestion de données cloud de Braze et de la manière de synchroniser les données utilisateurs pertinentes avec votre intégration Snowflake."
page_order: 6.1
page_type: reference

---

# Ingestion de données cloud de Braze : intégration Snowflake

{% alert important %}
L’ingestion de données cloud de Braze est actuellement disponible en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Qu’est-ce que l’ingestion de données cloud de Braze ?

L’ingestion de données cloud de Braze vous permet de mettre en place une connexion directe depuis votre instance Snowflake vers Braze pour synchroniser les données utilisateur pertinentes. Une fois synchronisés avec Braze, ces attributs peuvent être utilisés pour la personnalisation ou la segmentation.

### Fonctionnement

Grâce à l’ingestion de données cloud de Braze, vous pouvez mettre en place une intégration entre votre instance Snowflake et le groupe d’apps de Braze pour synchroniser des données de manière récurrente. Cette synchronisation se fait selon la planification que vous déterminez et chaque intégration peut disposer d’une planification différente. Les synchronisations peuvent avoir lieu d’une fois toutes les 15 minutes à une fois par mois. Les clients ayant besoin d’une synchronisation plus fréquente que toutes les 15 minutes peuvent contacter leur gestionnaire du succès des clients ou envisager d’utiliser les appels API REST pour une ingestion de données en temps réel.

Pendant qu’une synchronisation a lieu, Braze se connectera directement à votre instance Snowflake, récupérera toutes les nouvelles données d’un tableau donné et mettra à jour les profils utilisateurs correspondants sur votre tableau de bord de Braze. Chaque fois qu’une synchronisation a lieu, toutes les données mises à jour s’afficheront sur les profils utilisateurs.

### Qu’est-ce qui est synchronisé

Chaque fois qu’une synchronisation a lieu, Braze cherchera les lignes qui n’ont pas déjà été synchronisées. Nous le vérifions en utilisant la colonne `UPDATED_AT` dans votre table ou votre affichage. Chaque ligne dans laquelle `UPDATED_AT` est plus ancien que la dernière synchronisation, la ligne sera sélectionnée et transmise à Braze.

Dans Snowflake, vous ajoutez les utilisateurs et attributs suivants à votre table en réglant l’heure de `UPDATED_AT` sur le moment où vous ajoutez cette donnée :

| UPDATED_AT | EXTERNAL_ID | PAYLOAD |
| --- | --- | --- |
| '2022-07-19 09:07:23' | 'customer_1234' | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_2":42,<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| '2022-07-19 09:07:23' | 'customer_3456' | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_2":42,<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_3":"2019-07-16T19:20:30+1:00",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_5":"testing"<br>} |
| '2022-07-19 09:07:23' | 'customer_5678' | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_4":true,<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_5":"testing_123"<br>} |

Pendant la prochaine synchronisation planifiée, toutes les lignes possédant un horodatage `UPDATED_AT` plus ancien que l’horodatage le plus récent seront synchronisées aux profils utilisateurs de Braze. Les champs seront mis à jour ou ajoutés et vous n’aurez donc pas besoin de synchroniser le profil utilisateur tout entier à chaque fois. Après la synchronisation, les utilisateurs afficheront les nouvelles mises à jour :

```json
{
  "external_id":"customer_1234",
  "email":"jane@exaple.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2019-07-16T19:20:30+1:00",
  "attribute_4":false,
  "attribute_5":"testing"
}
```
```json
{
  "external_id":"customer_3456",
  "email":"michael@exaple.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2019-07-16T19:20:30+1:00",
  "attribute_4":true,
  "attribute_5":"testing"
}
```
```json
{
  "external_id":"customer_5678",
  "email":"bob@exaple.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2017-08-10T09:20:30+1:00",
  "attribute_4":true,
  "attribute_5":"testing_123"
}
```

### Utilisation de points de données

Chaque attribut envoyé pour un utilisateur utilisera un point de données. Il dépend de vous de n’envoyer que les données requises. Le suivi de points de données pour l’ingestion de données pour le cloud est équivalent au suivi à l’aide de l’endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track). Consultez les [points de données]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/) pour plus d’informations.

## Recommandations de paramétrage de données

#### N’écrivez que les attributs nouveaux ou mis à jour pour limiter l’utilisation

Nous synchroniserons tous les attributs dans une rangée donnée, qu’ils soient ou non les mêmes que ceux contenus actuellement dans le profil utilisateur. De ce fait, nous vous recommandons de ne synchroniser que les attributs que vous voulez ajouter ou mettre à jour.

#### Utilisez l’horodatage UTC pour la colonne UPDATED_AT

La colonne `UPDATED_AT` devrait être en UTC pour éviter les problèmes liés aux heures d’été.  Utilisez de préférence des fonctions uniquement en UTC, telles que `SYSDATE()` plutôt que `CURRENT_DATE()` dès que possible.

#### Enlever un attribut

Si vous désirez enlever entièrement un attribut d’un profil utilisateur, vous pouvez le définir sur `null`. Si vous désirez qu’un attribut reste inchangé, ne l’envoyez pas à Braze jusqu’à ce qu’il ait été mis à jour.

#### Créer une chaîne de caractères JSON depuis une autre table

Si vous préférez stocker de manière interne chaque attribut dans sa propre colonne, vous devez convertir ces colonnes en chaîne de caractères JSON pour remplir la synchronisation avec Braze. Pour ce faire, vous pouvez utiliser une requête du type :
```json
CREATE TABLE "PURCHASE_DATA"
    (purchase_date datetime,
     purchase_amount number,
     quantity number,
     address string);

SELECT TO_JSON(OBJECT_CONSTRUCT (*)) FROM "PURCHASE_DATA";
```

#### En utilisant l’horodatage UPDATED_AT

Nous utilisons l’horodatage `UPDATED_AT` pour suivre quelles données ont été synchronisées avec succès dans Braze. Si de nombreuses rangées sont écrites avec le même horodatage pendant qu’une synchronisation est en cours, ceci peut entraîner la synchronisation de données en double dans Braze. Voici quelques conseils pour éviter des données en double :
- Si vous mettez en place une synchronisation contre une `VIEW`, n’utilisez pas `CURRENT_TIMESTAMP` comme valeur de base. Ceci entraînera la synchronisation de toutes les données chaque fois qu’elle s’effectue, car le champ `UPDATED_AT` sera évalué à chaque fois que nos requêtes sont lancées. 
- Si vous avez des flux de données à très longue durée d’exécution ou des requêtes écrivant des données dans votre table source, évitez de les exécuter en même temps que la synchronisation ou évitez d’utiliser le même horodatage pour chaque ligne insérée.
- Utilisez une transaction pour écrire toutes les rangées qui ont le même horodatage.

#### Exemple de configuration de table

Nous disposons d’un [référentiel GitHub](https://github.com/braze-inc/braze-examples/tree/main/data-ingestion) public pour que les clients puissent partager leurs bonnes pratiques ou leurs extraits de code. Pour contribuer avec vos propres extraits de code, créez une requête d’extraction !

## Paramétrage du produit

Les nouvelles intégrations d’ingestion de données cloud nécessitent une configuration sur Braze ainsi que dans votre instance Snowflake. Suivez ces étapes pour mettre en place votre intégration :
1. Dans votre instance Snowflake, paramétrez les tables ou les vues que vous voulez synchroniser avec Braze.
2. Créez une nouvelle intégration dans le tableau de bord de Braze.
3. Obtenez la clé publique fournie dans le tableau de bord de Braze et [annexez-la à l’utilisateur Snowflake pour l’authentification](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. Testez l’intégration et débutez la synchronisation.

### Paramétrez les tables et les vues

#### Étape 1 : Paramétrez la table

```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     EXTERNAL_ID VARCHAR(16777216) NOT NULL,
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

Vous pouvez donner le nom que vous désirez à la base de données, au schéma et à la table, mais les noms de colonnes doivent correspondre à la définition précédente.

- `UPDATED_AT` : L’heure à laquelle la rangée a été mise à jour ou ajoutée à la table. Nous ne synchroniserons que les rangées qui ont été ajoutées ou mises à jour depuis la dernière synchronisation.
- `EXTERNAL_ID` : Ceci identifie l’utilisateur que vous désirez mettre à jour. Vous pouvez utiliser un des éléments parmi les suivants : `external_id`, `user_alias` ou `braze_id`.
- `PAYLOAD` : Il s’agit d’une chaîne de caractères JSON des champs que vous désirez synchroniser à l’utilisateur dans Braze.

#### Étape 2 : Définir le rôle et les autorisations de la base de données

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Changez les noms si nécessaire, mais les permissions doivent correspondre à l’exemple précédent.

#### Étape 3 : Définir l’entrepôt et donner accès au rôle de Braze

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
Cet entrepôt devra avoir la balise **relancement automatique** activée. Si ce n’est pas le cas, vous devrez nous donner des privilèges `OPERATE` supplémentaires sur l’entrepôt pour que nous puissions le mettre en route lorsque nous devons exécuter la requête.
{% endalert %}

#### Étape 4 : Définir l’utilisateur

```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Après cette étape, vous partagerez les informations de connexion avec Braze et vous recevrez une clé publique à annexer à l’utilisateur.

{% alert note %}
Lorsque vous connectez plusieurs groupes d’apps au même compte Snowflake, vous devez créer un utilisateur unique pour chaque groupe d’app Braze pour lequel vous créez une intégration. Au sein du groupe d’apps, vous pouvez réutiliser le même utilisateur entre les intégrations, mais la création d’intégration échouera si un utilisateur du même compte Snowflake est dupliqué entre les groupes d’apps.
{% endalert %}

#### Étape 5 : Autoriser les IP de Braze dans la politique réseau de Snowflake (optionnel)

Selon la configuration de votre compte Snowflake, vous pourrez avoir à autoriser les adresses IP suivantes au sein de votre politique réseau Snowflake. Pour plus de renseignements concernant la manière de l’activer, consultez la documentation Snowflake pertinente pour [modifier une politique réseau](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

| Pour les instances `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06` | Pour les instances `EU-01` et `EU-02` |
|---|---|
| `23.21.118.191`| `52.58.142.242`
| `34.206.23.173`| `52.29.193.121`
| `50.16.249.9`| `35.158.29.228`
| `52.4.160.214`| `18.157.135.97`
| `54.87.8.34`| `3.123.166.46`
| `54.156.35.251`| `3.64.27.36`
| `52.54.89.238`| `3.65.88.25`
| `18.205.178.15`| `3.68.144.188`
|   | `3.70.107.88`

### Créer une nouvelle intégration dans le tableau de bord de Braze

Rendez-vous sur la page Snowflake de Braze, dans **Technology Partners** et cliquez sur **Créer une nouvelle synchronisation d’importation**.

1. Ajouter les informations de connexion et la table source de Snowflake
Saisissez les informations de votre compte Snowflake and de la table source et passez à l’étape suivante.<br>![][1]<br><br>
2. Donnez un nom à la synchronisation et définissez la fréquence
Choisissez ensuite un nom pour votre synchronisation et saisissez les e-mails de contact. Nous utiliserons ces informations de contact pour vous signaler toute erreur d’intégration (par ex., l’accès à la table a été supprimé inopinément).<br>![][2]<br><br>Vous choisirez également la fréquence de synchronisation. La fréquence peut être définie d’une fois toutes les 15 minutes jusqu’à une fois par mois. Nous utiliserons le fuseau horaire configuré dans votre tableau de bord de Braze pour planifier la synchronisation récurrente.

### Ajouter une clé publique à un utilisateur Braze
À ce stade, vous devrez vous rendre sur Snowflake pour terminer la configuration. Ajoutez la clé publique affichée sur le tableau de bord à l’utilisateur que vous avez créé pour que Braze se connecte à Snowflake.

Pour plus de renseignements concernant la manière de le faire, consultez la [documentation Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Si vous désirez, à un moment donné, faire alterner les clés, nous pouvons générer une nouvelle paire de clés et vous fournir une nouvelle clé publique.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

### Tester la connexion

Une fois que l’utilisateur a été mis à jour avec la clé publique, retournez sur le tableau de bord de Braze et cliquez sur **Tester la connexion**. Si vous avez réussi, vous pourrez voir un aperçu des données. Si, pour une raison quelconque, nous ne pouvons pas nous connecter, nous afficherons un message d’erreur pour vous aider à résoudre les problèmes.

![][3]

{% alert note %}
Vous devez avoir testé une intégration avec succès avant qu’elle ne puisse passer de l’état d’ébauche à l’état actif. Si vous avez besoin de créer la page de création, votre intégration sera sauvegardée et vous pourrez revenir à la page de détails pour effectuer des changements et les tester.  
{% endalert %}

### Définir des intégrations ou des utilisateurs supplémentaires (optionnel)

Vous pouvez également définir plusieurs intégrations avec Braze, mais chaque intégration devrait être configurée pour se synchroniser à une table différente. Lorsque vous créez des synchronisations supplémentaires, vous pouvez réutiliser des identifiants existants si vous vous connectez au compte Snowflake.
![][4]

Si vous réutilisez le même utilisateur et rôle entre les intégrations, vous n’aurez **pas** besoin d’effectuer à nouveau l’étape d’ajout de la clé publique.

### Exécuter la synchronisation

Une fois qu’elle est activée, votre synchronisation s’exécutera selon la planification définie pendant la configuration. Si vous désirez exécuter la synchronisation en dehors des horaires de planification habituels pour tester ou récupérer les données les plus récentes, cliquez sur **Synchroniser maintenant**. Cette exécution n’aura pas d’impact sur les synchronisations futures et habituelles planifiées.  
![][5]

## Limites du produit

| Limitations | Description |
| --- | --- |
| Nombre d’intégrations | Le nombre d’intégrations que vous pouvez définir n’est pas limité. Cependant, vous ne pourrez définir qu’une seule intégration par table ou par affichage.
| Nombre de lignes | Le nombre de lignes que vous pouvez synchroniser n’est pas limité. Chaque ligne ne sera synchronisée qu’une fois selon la colonne `UPDATED`. |
| Attributs par rangée | Chaque rangée ne devrait contenir qu’un seul ID utilisateur et un seul objet JSON contenant jusqu’à 50 attributs. Chaque clé dans l’objet JSON compte comme un seul attribut (c.-à-d., un tableau compte comme un attribut). |
| Type de données | Vous pouvez synchroniser les attributs utilisateurs à l’aide de l’ingestion de données cloud. |
| Région Braze | Ce produit est disponible dans toutes les régions Braze. Toutes les régions Braze peuvent se connecter à toutes les régions Snowflake |
| Région Snowflake | Vous pouvez connecter votre instance Snowflake à Braze dans toutes les régions et tous les clouds en utilisant ce produit. |
{: .reset-td-br-1 .reset-td-br-2}

[1]: {% image_buster /assets/img/cloud_ingestion/ingestion_1.png %}
[2]: {% image_buster /assets/img/cloud_ingestion/ingestion_2.png %}
[3]: {% image_buster /assets/img/cloud_ingestion/ingestion_3.png %}
[4]: {% image_buster /assets/img/cloud_ingestion/ingestion_4.png %}
[5]: {% image_buster /assets/img/cloud_ingestion/ingestion_5.png %}
