---
nav_title: Mozart Data
article_title: Mozart Data
description: "Cet article de référence présente le partenariat entre Braze et Mozart Data, une plateforme de données moderne tout-en-un, vous permettant d'utiliser Fivetran pour importer des données vers Snowflake, créer des transformations, combiner des données, et plus encore."
alias: /partners/mozartdata/
page_type: partner
search_tag: Partner

---

# Mozart Data

{% multi_lang_include video.html id="HU6dSOClcQ0" align="right" %}

> [Mozart Data](https://mozartdata.com/) est une plateforme de données moderne tout-en-un alimentée par Fivetran, Portable et Snowflake.

L'intégration de Braze et des données Mozart vous permet de :
- Utilisez Fivetran pour importer les données de Braze dans Snowflake.
- Créez des transformations en combinant les données Braze avec les données d'autres applications et analysez efficacement les comportements des utilisateurs.
- Importer les données de Snowflake dans Braze pour créer de nouvelles opportunités d'engagement client.
- Combinez les données Braze avec les données d'autres applications pour obtenir une compréhension plus holistique des comportements des utilisateurs.
- Intégration à un outil d'aide à la décision pour explorer davantage les données stockées dans Snowflake.

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
| Compte Mozart Data | Un compte Mozart Data est nécessaire pour profiter de ce partenariat. [Inscrivez-vous ici.](https://app.mozartdata.com/signup)|
| Compte Snowflake<br>Option 1 : Nouveau compte | Sélectionnez **Créer un nouveau compte Snowflake** pendant le processus de création du compte Mozart Data pour que Mozart Data crée un nouveau compte Snowflake pour vous. |
| Compte Snowflake<br>Option 2 : Compte existant | Si votre entreprise possède déjà un compte Snowflake, vous pouvez utiliser l'option Mozart Data connecté.<br><br>Sélectionnez l'option **Avoir déjà un compte Snowflake** pour connecter un compte Snowflake existant. Pour mettre en œuvre cette option, un utilisateur disposant d'autorisations au niveau du compte doit [suivre les étapes suivantes.](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

L'intégration est prise en charge à la fois pour la synchronisation des données de [Braze vers Mozart Data](#syncing-data-from-braze-to-mozart-data) et de [Mozart Data vers Braze](#syncing-data-from-mozart-data-to-braze).

### Synchronisation des données de Braze vers Mozart Data

#### Étape 1 : Configurez un connecteur Braze

1. Dans Mozart Data, allez dans **Connecteurs** et cliquez sur **Ajouter un connecteur**.
2. Recherchez "Braze" et sélectionnez la carte de connecteur.
3. Saisissez un nom de schéma de destination où seront stockées toutes les données synchronisées depuis Braze. Nous vous recommandons d'utiliser le nom de schéma par défaut `braze`.
4. Cliquez sur **Ajouter un connecteur**.

#### Étape 2 : Remplissez le formulaire du connecteur Fivetran

Vous serez redirigé vers la page du connecteur Fivetran. Sur cette page, remplissez les champs indiqués. Ensuite, cliquez sur **Continue** > **Save & Test** pour terminer le connecteur Fivetran.

Fivetran commencera à synchroniser les données de votre compte Braze vers votre entrepôt de données Snowflake. Vous pouvez accéder aux données de requête de Mozart Data une fois que le connecteur a terminé la synchronisation. 

### Synchronisation des données de Mozart Data vers Braze

#### Étape 1 : Configurez un entrepôt de données Snowflake

Suivez les instructions relatives à [l'ingestion de données dans le cloud]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake) pour configurer une table, un utilisateur et une permission à partir de l'interface Snowflake. Notez que cette étape nécessite un accès de niveau administrateur à Snowflake.

#### Étape 2 : Configurez votre intégration Snowflake dans Braze

Après avoir configuré votre entrepôt Snowflake, dans Mozart Data, allez sur la page d'**intégration** et sélectionnez **Braze**. Vous y trouverez les informations d'identification dont vous aurez besoin pour fournir Braze.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

Ensuite, tout en étant connecté à Braze, allez dans **Intégrations > Partenaires technologiques > Snowflake** pour commencer le processus d'intégration. Copiez les données d'identification de Mozart Data et ajoutez-les à la page d'importation de Snowflake Data. Cliquez sur **Configurer les détails de la synchronisation** et saisissez les informations relatives à votre compte Snowflake et à votre table source. 

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

Ensuite, choisissez un nom pour votre synchronisation, fournissez les e-mails de contact et sélectionnez un type de données et une fréquence de synchronisation. 

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-importsync.png %}){: style="max-width:80%;"}

#### Étape 3 : Ajouter une clé publique à l'utilisateur Braze
À ce stade, vous devrez retourner à Snowflake pour terminer la configuration. Ajoutez la clé publique affichée sur le tableau de bord de Braze à l'utilisateur que vous avez créé pour que Braze se connecte à Snowflake.

Pour plus d'informations sur la manière de procéder, consultez la [documentation de Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Si vous voulez changer les clés, Mozart Data peut générer une nouvelle paire de clés et vous fournir la nouvelle clé publique.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### Étape 4 : Testez la connexion

Une fois l'utilisateur mis à jour avec la clé publique, retournez dans le tableau de bord de Braze et cliquez sur **Tester la connexion**. Si l’opération réussie, un aperçu des données s’affiche. Si, pour une raison quelconque, la connexion échoue, un message d'erreur s'affiche pour vous aider à résoudre le problème.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
Vous devez avoir testé une intégration avec succès avant qu’elle ne puisse passer de l’état d’ébauche à l’état actif. Si vous avez besoin de fermer la page de création, votre intégration sera sauvegardée et vous pourrez revenir à la page Détails pour effectuer des changements et les tester.  
{% endalert %}

## Grâce à cette intégration

### Comment accéder aux données de Braze en tant qu'utilisateur de Mozart Data ?
Après avoir créé avec succès un compte Mozart Data, vous pouvez accéder à vos données Braze synchronisées avec votre entrepôt de données Snowflake à partir de Mozart Data.

#### Transformations
Mozart Data propose une couche de transformation SQL pour permettre aux utilisateurs de créer une vue ou une table. Vous pouvez créer une table de dimension au niveau de l'utilisateur (par exemple, `dim_users`) pour résumer les données d'utilisation du produit, l'historique des transactions et les activités d'engagement de chaque utilisateur avec les messages Braze. 

#### Analyse
À l'aide des modèles de transformation ou des données brutes synchronisées depuis Braze, vous pouvez analyser l'engagement des utilisateurs vis-à-vis des messages de Braze. En outre, vous pouvez combiner les données de Braze avec d'autres données d'application et analyser comment les informations que vous avez obtenues à partir de l'interaction des utilisateurs avec les messages de Braze sont liées à d'autres données que vous pourriez avoir sur les utilisateurs. Par exemple, leurs informations démographiques, l'historique de leurs achats, l'utilisation des produits et l'engagement du service client. 

Cela peut vous aider à prendre des décisions plus éclairées sur les stratégies d'engagement afin d'améliorer la rétention des utilisateurs. Tout cela peut être fait dans l'interface de Mozart Data à l'aide de l'outil de requête, où vous pouvez exporter les résultats dans une feuille Google ou CSV pour préparer une présentation.

#### Aide à la décision (BI)
Vous êtes prêt à visualiser et à partager vos informations avec les autres membres de l'équipe ? Mozart Data s'intègre à presque tous les outils d’aide à la décision. Si vous n'avez pas encore d'outil d’aide à la décision, contactez Mozart Data pour créer un compte Metabase gratuit. 