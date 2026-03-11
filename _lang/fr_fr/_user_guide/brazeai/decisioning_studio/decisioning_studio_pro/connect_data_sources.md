---
nav_title: Connecter les sources de données
article_title: Connecter les sources de données
page_order: 1
description: "Découvrez comment connecter les sources de données clients à BrazeAI Decisioning Studio Pro pour une prise de décision personnalisée basée sur l'intelligence artificielle."
---

# Connecter les sources de données

> Les agents de BrazeAI Decisioning Studio™ Pro doivent parfaitement comprendre le contexte du client afin de prendre des décisions efficaces. Cet article explique comment connecter des sources de données clients à Decisioning Studio Pro.

{% alert tip %}
Votre équipe de service AI Decisioning vous assistera dans la configuration des connexions de données afin d'optimiser les performances.
{% endalert %}

## Modèles d'intégration pris en charge

Decisioning Studio Pro prend en charge plusieurs modèles d'intégration pour connecter les données clients :

| Modèle d'intégration | Meilleur pour | Complexité de la configuration |
|---------------------|----------|------------------|
| **Plateforme de données Braze** | Les clients qui utilisent déjà Braze | Faible |
| **Ingestion de données dans le cloud Braze (CDI)** | Connexion d'entrepôts de données externes | Moyen |
| **Stockage dans le cloud (GCS, AWS, Azure)** | Exportation directe des données depuis d'autres plateformes | Moyen |
| **Intégrations CEP** | Extensions de données SFMC et Klaviyo | Moyen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Types de données clients

Les ressources clients suivantes permettent aux agents de réaliser une personnalisation plus efficace :

| Type de données | Description | Exemples |
|-----------|-------------|----------|
| **Profil client personnalisé** | Attributs statiques et à évolution lente | Années en tant que client, zone géographique, canal d'acquisition, niveau de satisfaction, estimation de la valeur vie client |
| **Comportement des clients** | Modèles d'activité et d'engagement | Identifiants, type d'appareil, interactions avec le service client, utilisation des produits |
| **Historique des transactions** | Données relatives aux achats et aux conversions | Produits achetés, montants des transactions, méthodes de paiement, canaux d'achat |
| **Engagement marketing** | Réponses aux communications | Ouvertures/clics d'e-mails, engagement SMS, activité Web et mobile, réponses aux enquêtes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert tip %}
Plus les agents disposent d'informations sur vos clients, plus ils seront performants. Envisagez d'inclure des données sur toutes les informations particulièrement importantes pour votre entreprise (par exemple, souhaitez-vous voir comment l'intelligence artificielle traite différemment vos clients fidèles ?). Veuillez vous assurer que le statut de fidélité est bien indiqué dans les données client.
{% endalert %}

## Connexion des données par plateforme

{% tabs %}
{% tab Braze %}

### Transmettre les données clients via Braze

BrazeAI Decisioning Studio peut exploiter toutes les données que vous transmettez déjà à la plateforme de données Braze.

Si vous souhaitez utiliser des données client pour Decisioning Studio qui ne sont actuellement pas stockées dans le profil utilisateur ou les attributs personnalisés, il est recommandé d'utiliser [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) pour importer des données provenant d'autres sources.

CDI prend en charge les intégrations directes avec :

- Snowflake
- Redshift
- BigQuery
- Databricks
- Microsoft Fabric
- AWS S3

Pour obtenir la liste complète des sources prises en charge, veuillez consulter [la section Ingestion de données dans le cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

Une fois que vous êtes satisfait des données que vous envoyez à la plateforme de données Braze, veuillez contacter votre équipe AI Decisioning Services afin de déterminer quels champs du profil utilisateur ou attributs personnalisés doivent être utilisés pour l'intelligence artificielle.

Afin de rationaliser ce processus, veuillez créer une liste des attributs du profil utilisateur Braze qui, selon vous, représentent le mieux les comportements des clients et qui devraient être utilisés dans Decisioning Studio (veuillez consulter la [liste des champs disponibles]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/#fields-to-export)). Votre équipe de service peut également vous aider à organiser des séances de découverte afin de déterminer les domaines les plus appropriés pour la prise de décision par l'intelligence artificielle.

D'autres options pour l'envoi de données sont disponibles, notamment :

- Envoi d'événements personnalisés Braze via le SDK
- Envoi d'événements à l'aide de l'endpoint REST ([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track))

Ces modèles nécessitent davantage d'efforts d'ingénierie, mais peuvent parfois être préférables en fonction de votre configuration Braze actuelle. Veuillez contacter l'équipe des services de prise de décision par intelligence artificielle pour obtenir de plus amples informations.

{% endtab %}
{% tab SFMC %}

### Veuillez transmettre les données clients via SFMC.

Pour les intégrations Salesforce Marketing Cloud :

1. Veuillez configurer les extensions de données SFMC pour vos données clients.
2. Veuillez configurer le package SFMC installé pour l'intégration API avec les autorisations appropriées requises par Decisioning Studio.
3. Veuillez vous assurer que les extensions de données sont actualisées quotidiennement, car Decisioning Studio extraira les dernières données incrémentielles disponibles.

Veuillez fournir l'ID d'extension et la clé API à votre équipe AI Decisioning Services. Ils vous assisteront dans les prochaines étapes de l'ingestion de données clients.

{% endtab %}
{% tab Klaviyo %}

### Veuillez transmettre les données clients via Klaviyo.

Pour les intégrations Klaviyo :

1. Veuillez vérifier que les données du profil client sont disponibles dans les profils Klaviyo.
2. Générer une clé API privée avec accès complet aux profils
3. Veuillez fournir la clé API à votre équipe AI Decisioning Services.

Veuillez consulter la [documentation Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908) pour plus d'informations sur la configuration de la clé API.

{% endtab %}
{% tab Cloud Storage %}

### Autres solutions cloud (Google cloud storage, Azure, AWS)

Si les données client ne sont actuellement pas stockées dans Braze, SFMC ou Klaviyo, la meilleure solution consiste à configurer une exportation automatisée directement vers un compartiment Google cloud storage contrôlé par Braze. Nous pouvons également prendre en charge l'exportation vers AWS ou Azure (bien que GCS soit préférable). Pour ces plateformes, veuillez exporter les données vers leur stockage cloud interne, et Braze pourra ensuite récupérer ces données.

Pour déterminer si cela est possible, veuillez consulter la documentation de votre plateforme Martech. Par exemple :

- mParticle propose une [intégration native avec Google cloud storage.](https://www.mparticle.com/integration/google-cloud-storage/)
- [Segment Twilio](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

Si cela est possible, nous pouvons fournir un compartiment GCS vers lequel exporter les données client, qui est isolé de Decisioning Studio.

{% endtab %}
{% endtabs %}

## Bonnes pratiques

- **Noms de colonnes descriptifs** : Les données clients doivent avoir des noms de colonnes clairs et descriptifs. Idéalement, un dictionnaire de données devrait être fourni.
- **Mises à jour incrémentielles** : Les fichiers incrémentiels sont préférables aux instantanés quotidiens de l'historique complet du client.
- **Identifiants cohérents** : Chaque enregistrement doit contenir un identifiant client unique qui est cohérent dans toutes les ressources de données.
- **Veuillez inclure les horodatages** : Les enregistrements doivent être associés à des horodatages afin de garantir une attribution précise et la formation des agents.

## Intégrations personnalisées

D'autres options ou des pipelines de données entièrement personnalisés sont également envisageables. Cela peut nécessiter des services supplémentaires ou des travaux d'ingénierie de la part de votre équipe. Afin de déterminer ce qui est réalisable et optimal, veuillez collaborer avec votre équipe des services de prise de décision par intelligence artificielle.

{% alert important %}
Ce guide présente les modèles d'intégration les plus courants. Le service de sécurité informatique devra toujours vérifier tous les points de connexion et des consultants en solutions seront disponibles pour vous conseiller sur la mise en œuvre.
{% endalert %}

## Étapes suivantes

Après avoir connecté vos sources de données, veuillez procéder à la configuration de l'orchestration :

- [Configurer l'orchestration]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

