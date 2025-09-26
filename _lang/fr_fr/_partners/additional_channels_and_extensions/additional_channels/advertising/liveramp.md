---
nav_title: LiveRamp
article_title: LiveRamp
description: "Apprenez à connecter LiveRamp, Snowflake et Braze afin de créer des campagnes marketing pertinentes et hautement personnalisées."
alias: /partners/liveramp/
page_type: partner
search_tag: Partner
---

# Connecter LiveRamp, Snowflake et Braze

> Apprenez à connecter LiveRamp, Snowflake et Braze afin de créer des campagnes marketing pertinentes et hautement personnalisées en réduisant le temps nécessaire pour obtenir des informations, en éliminant les silos de données et en optimisant l'engagement client. Cette intégration améliore le marketing axé sur les données en fournissant des informations exploitables basées sur les personnes et en consolidant les points de contact avec les consommateurs pour une meilleure segmentation de l'audience et des campagnes opportunes. Il s'appuie également sur des benchmarks fournis par Snowflake pour vous aider à affiner vos stratégies marketing par rapport aux normes du secteur.

{% alert important %}
Les partages de [données sécurisés de Snowflake ne transfèrent pas de données](https://docs.snowflake.com/en/user-guide/data-sharing-intro) entre LiveRamp, Snowflake et Braze. Les données sont uniquement partagées via les services et le magasin de métadonnées de Snowflake, ce qui signifie qu'aucune donnée n'est copiée et qu'aucun frais de stockage supplémentaire n'est facturé. L'accès aux données partagées est contrôlé et régi à l'aide des contrôles d'accès de votre compte Snowflake.
{% endalert %}

## Cas d'utilisation

- **Minimisation des données :** L'application d'activation de LiveRamp utilise la fonctionnalité de partage de données sécurisé de Snowflake pour lire efficacement les tableaux directement depuis votre instance. Aucune donnée n'est transférée de Snowflake jusqu'au point de distribution au partenaire en aval.
- **Activation sécurisée des données first party :** En utilisant l'application Identity Resolution ci-dessus, l'application d'activation de LiveRamp utilisera uniquement les tables basées sur Rampid dans votre instance Snowflake, et les informations personnelles n'auront donc jamais à quitter vos murs.
- **Accélérez le délai de vie :** En résolvant les données RAMPID directement dans votre environnement, la distribution vers une destination finale peut s'effectuer en quelques heures, contre plusieurs jours avec l'approche plus traditionnelle basée sur les fichiers de LiveRamp. Cela augmente considérablement la capacité à optimiser les performances des campagnes au moment opportun.
- **Économies opérationnelles :** De même, grâce à la fonctionnalité Secure Data Share de Snowflake, les clients économisent du temps et de l'argent par rapport à la coordination du transfert des fichiers vers LiveRamp ou vers n'importe quelle destination finale.

## Conditions préalables

| Prérequis       | Description                                                                                                                                                                                     |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Compte Snowflake | Vous avez besoin d'un compte Snowflake avec des autorisations de niveau administrateur.                                                                                                                                      |
| Compte LiveRamp  | Contactez l'équipe de votre compte LiveRamp ou envoyez un e-mail à [snowflake@ liveramp.com](mailto:snowflake@liveramp.com) pour discuter des applications LiveRamp requises dans Snowflake.                              |
{: .reset-td-br-1 .reset-td-br-2 }

## Configuration de l'intégration

### Étape 1 : Demander un partage de données à Braze

Tout d'abord, contactez votre responsable de compte Braze ou votre responsable de la satisfaction client pour acheter un connecteur Snowflake Data Share pour votre compte Braze. Lorsque vous requêtez un partage de données, Braze fournira le partage depuis le ou les espaces de travail dans lesquels l'action a été achetée. Une fois le partage configuré, toutes les données sont immédiatement accessibles depuis votre instance Snowflake sous la forme d'un partage de données entrant. Une fois que le partage est visible dans votre instance, créez une base de données à partir du partage afin de pouvoir voir et interroger les tables.

Pour une procédure pas à pas complète, consultez le guide d'[intégration de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) avec Braze.

### Étape 2 : Configurer l'application LiveRamp dans Snowflake 

Les fonctionnalités de traduction et de résolution d'identité sont disponibles dans Snowflake via l'application native LiveRamp Identity Resolution and Translation, qui crée un partage sur votre compte, ouvrant une vue pour interroger l'ensemble de données de référence depuis votre propre environnement Snowflake.

Pour configurer l'application native, suivez ces étapes fournies dans la documentation LiveRamp : [Configurez l'application native LiveRamp dans Snowflake](https://docs.liveramp.com/identity/en/set-up-the-liveramp-native-app-in-snowflake.html). Lorsque vous avez terminé, passez à l'étape suivante.

### Étape 3 : Création d'une table de données

{% alert warning %}
Avant de préparer des tableaux basés sur des informations personnelles, assurez-vous de bien comprendre le [filtre de confidentialité de LiveRamp](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html) qui est exécuté pendant les tâches pour garantir que les colonnes d'attributs (non identificateurs) de vos tables de saisie ne contiennent pas de valeurs trop uniques. Cela est essentiel pour préserver la confidentialité des consommateurs et éviter toute nouvelle identification.
{% endalert %}

Ensuite, créez une table de données [au format requis](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html) qui sera appelée par le biais de l'application native LiveRamp. Reportez-vous aux catégories suivantes pour déterminer lesquels de vos identifiants peuvent faire l'objet d'une résolution :

| Type d'identifiant | Description  |
|-----------------|--------------|
| PII complet        | Les informations personnelles identifiables (PII) incluent le nom, l'adresse postale, l'e-mail et le numéro de téléphone de l'utilisateur. **Remarque:** Tous les identifiants ne sont pas requis pour chaque enregistrement. |
| E-mail uniquement      | Les adresses e-mail de l'utilisateur, telles que`alex-lee@email.com`. |
| Appareil          | Cela inclut les cookies tiers, les identifiants publicitaires mobiles (MAID), les identifiants de télévision connectée (identifiants CTV) et les RAMPID (résolus en RAMPID de foyers). |
| CID            | Il s'agit d'identifiants provenant d'un partenaire de plateforme ou d'une synchronisation d'identité avec LiveRamp, tels que votre identifiant client interne. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Identifiants de Braze

Les journaux d'événements de Braze contiennent des identifiants que vous pouvez utiliser dans l'application native LiveRamp. Pour obtenir la liste complète des identifiants disponibles pour chaque type d'événement, téléchargez les [schémas et identificateurs d'événements Braze]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt).

| Type d'identifiant | Description  |
|-----------------|--------------|
| `AD_ID` | Les identifiants publicitaires, tels que`ios_idfa`, `google_ad_id` et `roku_ad_id`, capturés dans le cadre de types d'événements particuliers, peuvent être utilisés conjointement avec les services de résolution des appareils de LiveRamp. Par défaut, les ID de publicité ne sont pas collectés. Toutefois, vous pouvez activer le suivi en suivant la [documentation de Braze]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#data-not-collected-by-default). |
| `EMAIL_ADDRESS`   | Adresse e-mail pouvant être utilisée conjointement avec les services de résolution par e-mail uniquement de LiveRamp |
| `TO_PHONE_NUMBER` | Numéro de téléphone, qui peut être utilisé conjointement avec les services de résolution PII de LiveRamp. |
| `EXTERNAL_USER_ID` | L'ID externe associé à un utilisateur, qui peut être utilisé conjointement avec les services de résolution des appareils (CID) de LiveRamp. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
[L'utilisation de tout identifiant personnalisé spécifique à un client ou à une marque dans l'application LiveRamp nécessite une synchronisation d'identité avec LiveRamp.](https://docs.liveramp.com/identity/en/getting-started-with-liveramp-identity.html)
{% endalert %}

### Étape 4 : Définissez vos variables

Ensuite, définissez vos variables pour la tâche dans la feuille de travail Étapes d'exécution fournie dans l'application. Cela inclut des détails tels que la base de données cible, les tables associées (données d'entrée, indicateurs, journalisation) et la définition du nom de la table de sortie. Pour une présentation complète, consultez [ LiveRamp : Spécifiez les variables](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#specify-the-variables-43-150727).

### Étape 5 : Création de la table de métadonnées pour la résolution des PII

Maintenant que vos variables sont définies, créez la table de métadonnées pour la résolution des PII. Cela donnera des détails sur le type de tâche spécifique à exécuter en fonction de la catégorie d'identifiants impliquée. Pour une présentation complète, consultez [ LiveRamp : Créez la table de métadonnées](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#create-the-metadata-table-43).

### Étape 6 : Réaliser l'opération de résolution d'identité

Enfin, effectuez l'opération de résolution d'identité. Pour une présentation complète, consultez [ LiveRamp : Effectuez l'opération de résolution d'identité](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#perform-the-identity-resolution-operation).

{% tabs local %}
{% tab exemple de saisie %}
```sql
call lr_resolution_and_transcoding(
$customer_input_table_name,
$customer_meta_table_name,
$output_table_name,
$customer_logging_table_name,
$customer_metrics_table_name
);
```
{% endtab %}

{% tab exemple de sortie %}
```sql
call check_for_output(
$output_table_name
);
```
{% endtab %}
{% endtabs %}

### Prochaines étapes

Vos données étant désormais pseudonymisées selon l’encodage dédié de RAMPID, vous pouvez partager les tables basées sur RAMPID avec l'application d'activation gérée de LiveRamp afin de les transmettre facilement à vos principaux partenaires de plateformes publicitaires. L'application d'activation comprend une interface conviviale pour les utilisateurs professionnels permettant une segmentation et une sélection/configuration supplémentaires des partenaires de destination en aval. Pour plus de détails sur l'application, veuillez contacter l'équipe responsable de votre compte LiveRamp ou envoyez un e-mail à [ snowflake@liveramp.com](mailto:snowflake@liveramp.com).

## Résolution des problèmes

{% alert note %}
Si vous avez des problèmes ou des questions plus spécifiques, envoyez un e-mail à l’adresse [martech@ liveramp.com](mailto:martech@liveramp.com).
{% endalert %}

### Régions Snowflake

Actuellement, cette application n'est disponible que pour les régions américaines suivantes :

  - aws-us-est-1 : POA18931
  - aws-us-ouest-2 : FAA28932
  - azure-east-us-2 : BL60425

### Confidentialité et valeurs des colonnes

Le processus évalue la combinaison de toutes les valeurs de colonne par ligne pour obtenir des valeurs uniques. Si une combinaison particulière de valeurs de colonne apparaît 3 fois ou moins, les lignes contenant ces valeurs de colonne ne pourront pas être mises en correspondance et ne seront pas renvoyées dans la table de sortie. De même, pour garantir la confidentialité, le service LiveRamp évalue le caractère unique des combinaisons de valeurs de colonnes, garantissant ainsi que si plus de 5 % des lignes du fichier deviennent incomparables en raison de combinaisons rares, le travail échouera.

### Données historiques

Les données historiques de Snowflake remontent à avril 2019, mais il peut y avoir de légères différences par rapport aux données antérieures à août 2019 en raison de changements de produits.

### Vitesse, performance, coût

La rapidité et le coût des requêtes dépendent de la taille de l'entrepôt utilisé. Tenez compte de vos besoins en matière d'accès aux données lors de la sélection de la taille de l’entrepôt.

### Références Braze

Les références vous permettent de comparer vos indicateurs aux normes du secteur, disponibles directement dans Snowflake Data Exchange.

### Changement disruptifs ou non disruptifs

Soyez conscient des changements qui peuvent affecter votre intégration. Les changements de dernière minute seront précédés d'une annonce et d'une période de migration.
