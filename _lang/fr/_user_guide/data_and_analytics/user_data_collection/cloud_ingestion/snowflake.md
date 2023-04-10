---
nav_title: Snowflake
article_title: Ingestion de données Cloud dans Braze pour Snowflake
description: "Cet article de référence couvre l’Ingestion de Données Cloud dans Braze et comment synchroniser les données utilisateur pertinentes avec votre intégration Snowflake."
page_order: 1
page_type: reference

---

# Ingestion de données Cloud pour Snowflake

## Paramétrage du produit

Les nouvelles intégrations d’ingestion de données cloud nécessitent une configuration sur Braze ainsi que dans votre instance Snowflake. Suivez ces étapes pour configurer votre intégration :
1. Dans votre instance Snowflake, paramétrez la ou les tables ou vues que vous voulez synchroniser avec Braze
2. Créer une nouvelle intégration dans le tableau de bord de Braze
3. Récupérez la clé publique fournie dans le tableau de bord de Braze et [ajoutez-la à l’utilisateur Snowflake pour l’authentification](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)
4. Testez l’intégration et démarrez la synchronisation

### Paramétrez les tables et les vues

#### Étape 1 : Configurer le tableau

```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, or braze_id is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

Vous pouvez donner le nom que vous désirez à la base de données, au schéma et au tableau, mais les noms de colonnes doivent correspondre aux définitions ci-dessus.

- `UPDATED_AT` : L’heure à laquelle la rangée a été mise à jour ou ajoutée au tableau. Nous ne synchroniserons que les rangées qui ont été ajoutées ou mises à jour depuis la dernière synchronisation.
- Colonnes d’identifiant utilisateur. Votre tableau peut contenir une ou plusieurs colonnes d’identifiants utilisateur. Chaque ligne ne doit contenir qu’un seul identifiant (soit un `external_id`, la combinaison d’un `alias_name` et d’un `alias_label`, soit un `braze_id`. Une table source peut contenir des colonnes pour un, deux ou les trois types d’identifiants. 
    - `EXTERNAL_ID` : Ceci identifie l’utilisateur que vous désirez mettre à jour.  Cela doit correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` : Ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais seulement un `alias_name` par `alias_label`.
    - `BRAZE_ID` : L’identifiant d’utilisateur Braze. Il est généré par le SDK Braze et les nouveaux utilisateurs ne peuvent pas être créés à l’aide d’un ID Braze via l’ingestion de données cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias utilisateur. 
- `PAYLOAD` : Il s’agit d’une chaîne de caractères JSON des champs que vous désirez synchroniser à l’utilisateur dans Braze.

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
Cet entrepôt devra avoir la balise **auto-resume (reprise automatique)** activée. Si ce n’est pas le cas, vous devrez nous donner des privilèges `OPERATE` supplémentaires sur l’entrepôt pour que nous puissions le mettre en route lorsque nous devons exécuter la requête.
{% endalert %}

#### Étape 4 : Configurer l’utilisateur

```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Après cette étape, vous partagerez les informations de connexion avec Braze et vous recevrez une clé publique à ajouter (append) à l’utilisateur.

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

Rendez-vous sur la page Snowflake de Braze, dans **Technology Partners (partenaires technologiques)** et cliquez sur **Create new import sync (Créer une nouvelle synchronisation d’importation)**.

1. **Ajoutez les informations de connexion et le tableau source de Snowflake**<br>
Saisissez les informations de votre compte Snowflake et le tableau source, puis passez à l’étape suivante.<br>![][1]<br><br>
2. **Configurer les détails de la synchronisation**<br>
Choisissez ensuite un nom pour votre synchronisation et entrez les e-mails de contact. Nous utiliserons ces informations de contact pour vous signaler toute erreur d’intégration (par ex., l’accès au tableau a été supprimé inopinément).<br>![][2]<br><br> Vous choisirez également le type de données et la fréquence de synchronisation. La fréquence peut être définie une fois toutes les 15 minutes jusqu’à une fois par mois. Nous utiliserons le fuseau horaire configuré dans votre tableau de bord de Braze pour planifier la synchronisation récurrente. Les types de données supportés sont Attributs personnalisés, Événements personnalisés, et Événements d’Achat. Le type de données pour une synchronisation ne peut pas être modifié une fois créé. 

### Ajouter une clé publique à l’utilisateur Braze
À ce stade, vous devrez vous rendre sur Snowflake pour terminer la configuration. Ajoutez la clé publique affichée sur le tableau de bord à l’utilisateur que vous avez créé pour que Braze se connecte à Snowflake.

Pour plus de renseignements concernant la manière de le faire, consultez la [documentation Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Si vous désirez, à un moment donné, faire alterner les clés, nous pouvons générer une nouvelle paire de clés et vous fournir une nouvelle clé publique.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

### Tester la connexion

Une fois que l’utilisateur a été mis à jour avec la clé publique, retournez sur le tableau de bord de Braze et cliquez sur **Test connection (Tester la connexion)**. Si vous avez réussi, vous pourrez voir un aperçu des données. Si, pour une raison quelconque, nous ne pouvons pas nous connecter, nous afficherons un message d’erreur pour vous aider à résoudre le problème.

![][3]

{% alert note %}
Vous devez avoir testé une intégration avec succès pour qu’elle puisse passer du mode Draft au mode Active. Si vous avez besoin de fermer la page de création, votre intégration sera sauvegardée et vous pourrez revenir à la page Détails pour effectuer des changements et les tester.  
{% endalert %}

### Définir des intégrations ou des utilisateurs supplémentaires (optionnel)

Vous pouvez également définir plusieurs intégrations avec Braze, mais chaque intégration devra être configurée pour se synchroniser à un tableau différent. Lorsque vous créez des synchronisations supplémentaires, vous pouvez réutiliser des identifiants existants si vous vous connectez au compte Snowflake.
![][4]

Si vous réutilisez le même utilisateur et rôle entre les intégrations, vous n’aurez **pas** besoin d’effectuer à nouveau l’étape d’ajout de la clé publique.

### Exécuter la synchronisation

Une fois qu’elle est activée, votre synchronisation s’exécutera selon la planification définie pendant la configuration. Si vous désirez exécuter la synchronisation en dehors des horaires de planification habituels pour tester ou récupérer les données les plus récentes, cliquez sur **Sync Now (Synchroniser maintenant)**. Cette exécution n’aura pas d’impact sur les synchronisations futures et habituelles planifiées. 
![][5]

[1]: {% image_buster /assets/img/cloud_ingestion/ingestion_1.png %}
[2]: {% image_buster /assets/img/cloud_ingestion/ingestion_2.png %}
[3]: {% image_buster /assets/img/cloud_ingestion/ingestion_3.png %}
[4]: {% image_buster /assets/img/cloud_ingestion/ingestion_4.png %}
[5]: {% image_buster /assets/img/cloud_ingestion/ingestion_5.png %}
