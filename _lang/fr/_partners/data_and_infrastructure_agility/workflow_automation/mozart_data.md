---
nav_title: Mozart Data
article_title: Mozart Data
description: "Ce document décrit les étapes de partenariat et d’intégration de Braze avec Mozart Data, une plateforme de données moderne et tout-en-un."
alias: /partners/mozartdata/
page_type: partner
search_tag: Partenaire

---

# Mozart Data

{% multi_lang_include video.html id="HU6dSOClcQ0" align="right" %}

> [Mozart Data](https://mozartdata.com/) est une plateforme de données moderne et tout-en-un optimisée par Fivetran, Portable et Snowflake.

L’intégration de Braze et Mozart Data vous permet de :
- Utilisez Fivetran pour importer des données Braze dans Snowflake
- Créer des transformations en combinant les données Braze avec d’autres données d’applications et analyser efficacement les comportements des utilisateurs
- Importer des données de Snowflake dans Braze pour créer de nouvelles opportunités d’engagement client
- Combinez les données Braze avec d’autres données d’applications pour obtenir une compréhension plus globale des comportements utilisateur
- Intégrez avec un outil d’aide à la décision pour explorer plus en détail les données stockées dans Snowflake

## Conditions préalables

<style>
table th:nth-child(1) {
    width: 25%;
}
table th:nth-child(2) {
    width: 75%;
}
table td {
    word-break: break-word;
}
</style>

| Condition | Description |
| ----------- | ----------- |
| Compte Mozart Data | Un compte Mozart Data est requis pour profiter de ce partenariat. [Inscrivez-vous ici.](https://app.mozartdata.com/signup)|
| Compte Snowflake<br>Option 1 : Nouveau compte | Sélectionnez **Create a New Snowflake Account (Créer un nouveau compte Snowflake)** pendant le processus de création de compte Mozart Data pour que Mozart Data vous fournisse un nouveau compte Snowflake. |
| Compte Snowflake<br>Option 2 : Compte existant | Si votre organisation possède déjà un compte Snowflake, vous pouvez utiliser l’option connectée Mozart Data.<br><br>Sélectionnez l’option **Already Have a Snowflake Account (J’ai déjà un compte Snowflake)** pour connecter un compte Snowflake existant. Pour continuer avec cette option, un utilisateur disposant d’autorisations au niveau du compte doit [suivre ces étapes](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount). |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

L’intégration est prise en charge pour synchroniser les données de [Braze à Mozart Data](#syncing-data-from-braze-to-mozart-data) et de [Mozart Data à Braze](#syncing-data-from-mozart-data-to-braze).

### Synchronisation des données de Braze à Mozart Data

#### Étape 1 : Configurer le connecteur Braze

1. Dans Mozart Data, allez dans **Connectors (Connecteurs)** et cliquez sur **Add Connector (Ajouter un connecteur)**.
2. Recherchez « Braze » et sélectionnez la carte de connecteur.
3. Saisissez un nom de schéma de destination où seront stockées toutes les données synchronisées de Braze. Nous vous recommandons d’utiliser le nom du schéma par défaut `braze`.
4. Cliquez sur **Add Connector (Ajouter un connecteur)**.

#### Étape 2 : Remplissez le formulaire de connecteur Fivetran

Vous serez redirigé vers la page du connecteur Fivetran. Sur cette page, remplissez les champs indiqués. Cliquez ensuite sur **Continue (Continuer)** > **Save & Test (Enregistrer et tester)** pour achever le connecteur Fivetran.

Fivetran commencera à synchroniser les données de votre compte Braze vers votre entrepôt de données Snowflake. Vous pouvez accéder aux données de requête à partir de Mozart Data une fois que le connecteur a terminé la synchronisation. 

### Synchroniser des données de Braze à Mozart Data

#### Étape 1 : Configurer un entrepôt de données Snowflake

Suivez les [instructions d’ingestion de données cloud](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/snowflake/) pour configurer une table, un utilisateur et une autorisation à partir de l’interface Snowflake. Notez que cette étape nécessite un accès au niveau administrateur Snowflake.

#### Étape 2 : Configurez votre intégration Snowflake dans Braze

Après avoir configuré votre entrepôt Snowflake, dans Mozart Data, accédez à la page **Integration (Intégration)** et sélectionnez **Braze**. Vous trouverez ici les identifiants dont vous aurez besoin de fournir à Braze.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

Ensuite, lorsque vous êtes connecté à Braze, allez dans **Integrations (Intégrations) > Technology Partners (Partenaires technologiques) > Snowflake** pour commencer le processus d’intégration. Copiez les informations d’identification de Mozart Data et ajoutez-les à la page d’importation de données Snowflake. Cliquez sur **Set up sync details (Configurer les détails de synchronisation)** et saisissez vos informations de compte Snowflake et de table source. 

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

Ensuite, choisissez un nom pour votre synchronisation, fournissez des e-mails de contact et sélectionnez un type de données et une fréquence de synchronisation. 

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-importsync.png %}){: style="max-width:80%;"}

#### Étape 3 : Ajouter une clé publique à l’utilisateur Braze
À ce stade, vous devrez vous rendre sur Snowflake pour terminer la configuration. Ajoutez la clé publique affichée sur le tableau de bord de Braze à l’utilisateur que vous avez créé pour que Braze se connecte à Snowflake.

Pour plus de renseignements concernant la manière de le faire, consultez la [documentation Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Si vous désirez, à un moment donné, faire alterner les clés, Mozart Data peut générer une nouvelle paire de clés et vous fournir une nouvelle clé publique.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### Étape 4 : Tester la connexion

Une fois que l’utilisateur a été mis à jour avec la clé publique, retournez sur le tableau de bord de Braze et cliquez sur **Test connection (Tester la connexion)**. Si vous avez réussi, vous pourrez voir un aperçu des données. Si, pour une raison quelconque, la connexion échoue, nous afficherons un message d’erreur pour vous aider à résoudre le problème.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
Vous devez avoir testé une intégration avec succès avant qu’elle ne puisse passer de l’état d’ébauche à l’état actif. Si vous avez besoin de fermer la page de création, votre intégration sera sauvegardée et vous pourrez revenir à la page Détails pour effectuer des changements et les tester.  
{% endalert %}

## Comment utiliser cette intégration

### Comment accéder aux données Braze en tant qu’utilisateur de Mozart Data
Après avoir créé un compte Mozart Data, vous pouvez accéder à vos données Braze synchronisées avec votre entrepôt de données Snowflake à partir de Mozart Data.

#### Transformations
Mozart Data propose une couche de transformation SQL pour permettre aux utilisateurs de créer une vue ou une table. Vous pouvez créer une table de dimensions au niveau de l’utilisateur (par ex., `dim_users`) pour résumer les données d’utilisation du produit, l’historique des transactions et les activités d’engagement de chaque utilisateur avec les messages Braze. 

#### Analyse
En utilisant les modèles de transformation ou les données brutes synchronisées à partir de Braze, vous pouvez analyser l’engagement des utilisateurs avec les messages de Braze. De plus, vous pouvez combiner les données Braze avec d’autres données d’application et analyser la manière dont les informations que vous avez obtenues de l’interaction des utilisateurs avec les messages Braze sont liées aux autres données que vous pouvez avoir sur les utilisateurs. Par exemple, leurs informations démographiques, leur historique d’achat, leur utilisation des produits et leur engagement envers le service client. 

Cela peut vous aider à prendre des décisions mieux renseignées sur les stratégies d’engagement afin d’améliorer la rétention des utilisateurs. Tout cela peut être réalisé dans l’interface de Mozart Data à l’aide de l’outil Requête, dans lequel vous pouvez exporter les résultats dans un Google Sheet ou un CSV pour préparer une présentation.

#### Aide à la décision (BI)
Prêt à visualiser et à partager vos idées avec d’autres membres de l’équipe ? Mozart Data s’intègre à presque tous les outils de BI. Si vous n’avez pas encore d’outil BI, contactez Mozart Data pour créer un compte Metabase gratuit. 