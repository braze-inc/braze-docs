---
nav_title: Ingestion de données Cloud
article_title: Ingestion de Données Cloud dans Braze
alias: /cloud_ingestion/
description: "Cet article de référence couvre l’Ingestion de Données Cloud dans Braze et comment synchroniser les données utilisateur pertinentes avec votre intégration Snowflake."
page_order: 4.1
page_type: reference

---

# Ingestion de données Cloud dans Braze -Intégration Snowflake

{% alert important %}
L’ingestion de données cloud Braze est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Qu’est-ce que l’Ingestion de données Cloud dans Braze ?

L’ingestion de données cloud dans Braze vous permet de configurer une connexion directe entre votre instance Snowflake et Braze pour synchroniser les attributs, les événements et les achats pertinents de l’utilisateur. Une fois synchronisées avec Braze, ces données peuvent être exploitées dans des cas d’utilisation tels que la personnalisation ou la segmentation.

### Fonctionnement

Avec l’Ingestion des Données Cloud dans Braze, vous configurez une intégration pour synchroniser les données de façon récurrente entre votre instance Snowflake et votre Groupe d’apps Braze. Cette synchronisation s’exécute selon un calendrier que vous définissez. Chaque intégration peut avoir un calendrier différent. Les synchronisations peuvent s’exécuter aussi fréquemment que toutes les 15 minutes ou aussi rarement qu’une fois par mois. Les clients qui ont besoin de synchroniser plus souvent que toutes les 15 minutes doivent contacter leur gestionnaire du succès des clients ou envisager d’utiliser des appels vers l’API REST pour l’ingestion des données en temps réel.

Lorsqu’une synchronisation s’exécute, Braze se connecte directement à votre instance Snowflake, récupère toutes les nouvelles données de la table spécifiée et met à jour les profils utilisateur correspondants sur votre tableau de bord de Braze. Chaque fois que la synchronisation s’exécute, les données mises à jour seront reflétées sur les profils des utilisateurs.

### Ce qui est synchronisé

Chaque fois qu’une synchronisation s’exécute, Braze recherche les lignes qui n’ont pas été synchronisées auparavant. Nous utilisons pour cela la colonne `UPDATED_AT` de votre table ou vue. Toute ligne où `UPDATED_AT` est ultérieur à la dernière ligne synchronisée sera sélectionnée et ajoutée dans Braze.

Dans Snowflake, vous ajoutez les utilisateurs et attributs suivants à votre table, en définissant la date `UPDATED_AT` sur la date à laquelle vous ajoutez ces données.

| UPDATED_AT | EXTERNAL_ID | PAYLOAD |
| --- | --- | --- |
| '2022-07-19 09:07:23' | 'customer_1234' | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_2":42,<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| '2022-07-19 09:07:23' | 'customer_3456' | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_2":42,<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_3":"2019-07-16T19:20:30+1:00",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_5":"testing"<br>} |
| '2022-07-19 09:07:23' | 'customer_5678' | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_1":"abcdefg",<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_4":true,<br>&nbsp;&nbsp;&nbsp;&nbsp;"attribute_5":"testing_123"<br>} |

Pendant la prochaine synchronisation planifiée, toutes les lignes possédant un timestamp `UPDATED_AT` plus ancien que le timestamp le plus récent seront synchronisées aux profils utilisateurs de Braze. Les champs seront mis à jour ou ajoutés et vous n’aurez donc pas besoin de synchroniser tout le profil utilisateur à chaque fois. Après la synchronisation, les utilisateurs auront les données mises à jour :

```json
{
  "external_id":"customer_1234",
  "email":"jane@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2019-07-16T19:20:30+1:00",
  "attribute_4":false,
  "attribute_5":"tester"
}
```
```json
{
  "external_id":"customer_3456",
  "email":"michael@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2019-07-16T19:20:30+1:00",
  "attribute_4":true,
  "attribute_5":"tester"
}
```
```json
{
  "external_id":"customer_5678",
  "email":"bob@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2017-08-10T09:20:30+1:00",
  "attribute_4":true,
  "attribute_5":"testing_123"
}
```

### Utilisation de points de données

Chaque attribut envoyé pour un utilisateur utilisera un point de données Il dépend de vous de n’envoyer que les données nécessaires. Le suivi de points de données pour l’ingestion de données pour le cloud est équivalent au suivi à l’aide de l’endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track) Consultez la rubrique [Points de données]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/) pour plus d’informations.

## Recommandations pour le paramétrage des données

#### N’écrivez que les attributs nouveaux ou mis à jour pour limiter la consommation

Nous synchroniserons tous les attributs dans une ligne donnée, qu’elles soient ou non les mêmes que celles contenues actuellement dans le profil utilisateur. Voilà pourquoi nous vous recommandons de ne synchroniser que les attributs que vous voulez ajouter ou mettre à jour.

#### Utilisez un timestamp UTC pour la colonne UPDATEDUPDATED_ATAT

La colonne `UPDATED_AT` doit être en UTC pour éviter les problèmes liés aux heures d’été.  Utilisez de préférence des fonctions uniquement en UTC, telles que `SYSDATE()` plutôt que `CURRENT_DATE()` lorsque c’est possible.

#### Séparer EXTERNAL_ID de la colonne PAYLOAD. 
L’objet PAYLOAD ne doit pas inclure d’identifiant externe ou d’autre type d’identifiant. 

#### Retirer un attribut

Si vous désirez retirer complètement un attribut d’un profil utilisateur, vous pouvez le définir sur `null`. Si vous désirez qu’un attribut reste inchangé, ne l’envoyez pas à Braze jusqu’à ce qu’il ait été mis à jour.

#### Créer un string JSON à partir d’une autre table

Si vous préférez stocker de manière interne chaque attribut dans sa propre colonne, vous devez convertir ces colonnes en strings JSON pour renseigner la synchronisation avec Braze. Pour ce faire, vous pouvez utiliser une requête du type :
```json
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    )as PAYLOAD FROM "EXAMPLE_DATA";
```

#### Utilisation de le timestamp UPDATED_AT

Nous utilisons le timestamp `UPDATED_AT` pour suivre quelles données ont été synchronisées avec succès dans Braze. Si de nombreuses lignes sont écrites avec le même timestamp pendant qu’une synchronisation est en cours, ceci peut entrainer la synchronisation de données en double dans Braze. Voici quelques conseils pour éviter des données en double :
- Si vous mettez en place une synchronisation pour une `VOIR`, n’utilisez pas `CURRENT_TIMESTAMP` comme valeur par défaut. Cela entrainera la synchronisation de toutes les données chaque fois qu’elle s’effectue, car le champ `UPDATED_AT` sera mis à jour à chaque exécution de nos requêtes. 
- Si vous avez des flux de données à très longue durée d’exécution ou des requêtes écrivant des données dans votre table source, évitez de les exécuter en même temps que la synchronisation ou évitez d’utiliser le même timestamp pour chaque ligne insérée.
- Utilisez une transaction pour écrire toutes les lignes qui ont le même timestamp.

#### Exemple de configuration de table

Nous avons un [dépôt GitHub](https://github.com/braze-inc/braze-examples/tree/main/data-ingestion) où les clients peuvent partager leurs bonnes pratiques ou leurs extraits de code. Créez une requête d’extraction pour contribuer avec vos propres extraits de code !

## Paramétrage du produit

Les nouvelles intégrations d’ingestion de données cloud nécessitent une configuration sur Braze ainsi que dans votre instance Snowflake. Suivez ces étapes pour configurer votre intégration :
1. Dans votre instance Snowflake, paramétrez la ou les tables ou vues que vous voulez synchroniser avec Braze.
2. Créez une nouvelle intégration dans le tableau de bord de Braze.
3. Récupérez la clé publique fournie dans le tableau de bord de Braze et [ajoutez-la à l’utilisateur Snowflake pour l’authentification](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. Testez l’intégration et démarrez la synchronisation.

### Paramétrez les tables et les vues

#### Étape 1 : Configurer la table

```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     EXTERNAL_ID VARCHAR(16777216) NOT NULL,
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

Vous pouvez donner le nom que vous désirez à la base de données, au schéma et à la table, mais les noms de colonnes doivent correspondre aux définitions ci-dessus.

- `UPDATED_AT` : L’heure à laquelle la ligne a été mise à jour ou ajoutée à la table. Nous ne synchroniserons que les lignes qui ont été ajoutées ou mises à jour depuis la dernière synchronisation.
- `EXTERNAL_ID` : Identifie l’utilisateur que vous désirez mettre à jour. Vous pouvez utiliser un des éléments parmi les suivants : `external_id`, `user_alias` ou `braze_id`.
- `CHARGE UTILE` : string JSON des champs que vous désirez synchroniser pour l’utilisateur dans Braze.

#### Étape 2 : Définir le rôle et les autorisations de la base de données

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Changez les noms si nécessaire, mais les permissions doivent correspondre à l’exemple ci-dessus.

#### Étape 3 : Définir l’entrepôt et donner accès au rôle Braze

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
Cet entrepôt devra avoir la balise **auto-resume (reprise automatique)** activée. Si ce n’est pas le cas, vous devrez nous donner des privilèges `OPÉRER` supplémentaires sur l’entrepôt pour que nous puissions l’utiliser e lorsque nous devons exécuter la requête.
{% endalert %}

#### Étape 4 : Configurer l’utilisateur

```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Après cette étape, vous partagerez les informations de connexion avec Braze et vous recevrez une clé publique à ajouter (append) à l’utilisateur.

{% alert note %}
Si vous connectez plusieurs groupes d’apps au même compte Snowflake, vous devez créer un utilisateur unique pour chaque groupe d’app Braze pour lequel vous créez une intégration. Dans le groupe d’apps, vous pouvez réutiliser le même utilisateur entre les intégrations, mais la création d’intégration échouera si un utilisateur du même compte Snowflake est dupliqué entre les groupes d’apps.
{% endalert %}

#### Étape 5 : Autoriser les IP de Braze dans la politique réseau de Snowflake (optionnel)

Selon la configuration de votre compte Snowflake, vous pourrez avoir à autoriser les adresses IP suivantes dans votre politique réseau Snowflake. Pour plus d’informations, consultez la documentation Snowflake pertinente pour [modifier une politique réseau](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies)..

| Pour les instances `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`[`Retrait en magasin`]| Pour les instances `EU-01` et `EU-02`[`Retrait en magasin`]|
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

Allez sur la page Snowflake de Braze, dans **Technology Partners** et cliquez sur **Create new import sync** (Créer une nouvelle synchronisation d’importation)..

1. **Ajoutez les informations de connexion et la table source de Snowflake**<br>
Saisissez les informations de votre compte Snowflake and de la table source et passez à l’étape suivante<br>![][1]<br><br>
2. **Configurer les détails de la synchronisation**<br>
Choisissez ensuite un nom pour votre synchronisation et entrez les e-mails de contact. Nous utiliserons ces informations de contact pour vous signaler toute erreur d’intégration (par ex., accès à la table supprimé inopinément).<br>![][2]<br><br> Vous choisirez également le type de données et la fréquence de synchronisation. La fréquence peut être définie une fois toutes les 15 minutes jusqu’à une fois par mois. Nous utiliserons le fuseau horaire configuré dans votre tableau de bord de Braze pour planifier la synchronisation récurrente. Les types de données supportés sont Attributs personnalisés, Événements personnalisés, et Événements d’Achat. Le type de données pour une synchronisation ne peut pas être modifié une fois créé. 

### Ajouter une clé publique à l’utilisateur Braze
À ce stade, vous devrez revenir sur Snowflake pour terminer la configuration. Ajoutez la clé publique (affichée sur le tableau de bord) à l’utilisateur que vous avez créé pour que Braze puisse se connecter à Snowflake.

Pour plus de renseignements concernant la manière de le faire, consultez la [documentation Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Si vous souhaitez alterner les clés, nous pouvons générer une nouvelle paire de clés et vous fournir une nouvelle clé publique.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

### Tester la connexion

Une fois que l’utilisateur a été mis à jour avec la clé publique, retournez sur le tableau de bord de Braze et cliquez sur **Test connection (Tester la connexion)**. Si la connexion fonctionne, vous pourrez voir un aperçu des données. Si, pour une raison quelconque, nous ne pouvons pas nous connecter, nous afficherons un message d’erreur pour vous aider à résoudre le problème.

![][3]

{% alert note %}
Vous devez avoir testé une intégration avec succès pour qu’elle puisse passer du mode Draft au mode Active. Si vous avez besoin de fermer la page de création, votre intégration sera sauvegardée et vous pourrez revenir à la page Détails pour effectuer des changements et les tester.  
{% endalert %}

### Définir des intégrations ou des utilisateurs supplémentaires (optionnel)

Vous pouvez également définir plusieurs intégrations avec Braze, mais chaque intégration devra être configurée pour se synchroniser à une table différente. Quand vous créez des synchronisations supplémentaires, vous pouvez réutiliser des identifiants existants si vous vous connectez au compte Snowflake.
![][4]

Si vous réutilisez le même utilisateur et rôle entre les intégrations, vous n’aurez **pas besoin** de refaire l’étape d’ajout de la clé publique.

### Exécution de la synchronisation

Une fois qu’elle est activée, votre synchronisation s’exécutera selon le calendrier défini pendant la configuration. Si vous désirez exécuter la synchronisation en dehors des horaires de planification habituels pour tester ou récupérer les données les plus récentes, cliquez sur **Sync Now (Synchroniser maintenant)**. Cette exécution n’aura pas d’impact sur les synchronisations futures et habituelles planifiées.  
![][5]

## Limites du produit

| Limitations | Description |
| --- | --- |
| Nombre d’intégrations | Le nombre d’intégrations que vous pouvez définir n’est pas limité. Cependant, vous ne pourrez définir qu’une seule intégration par table ou par vue.
| Nombre de lignes | Le nombre de lignes que vous pouvez synchroniser n’est pas limité. Chaque ligne ne sera synchronisée qu’une fois, en fonction de la colonne `MIS À JOUR`. |
| Attributs par ligne | Chaque ligne doit contenir un seul ID utilisateur et un seul objet JSON contenant jusqu’à 50 attributs. Chaque clé dans l’objet JSON compte comme un seul attribut (par exemple, un array compte comme un attribut). |
| Type de données | Vous pouvez synchroniser les attributs utilisateurs via l’ingestion de données cloud. |
| Région Braze | Ce produit est disponible dans toutes les régions Braze. Toutes les régions Braze peuvent se connecter à toutes les régions Snowflake |
| Région Snowflake | Vous pouvez connecter votre instance Snowflake à Braze dans toutes les régions et tous les clouds en utilisant ce produit. |
{: .reset-td-br-1 .reset-td-br-2}

[1]: {% image_buster /assets/img/cloud_ingestion/ingestion_1.png %}
[2]: {% image_buster /assets/img/cloud_ingestion/ingestion_2.png %}
[3]: {% image_buster /assets/img/cloud_ingestion/ingestion_3.png %}
[4]: {% image_buster /assets/img/cloud_ingestion/ingestion_4.png %}
[5]: {% image_buster /assets/img/cloud_ingestion/ingestion_5.png %}
