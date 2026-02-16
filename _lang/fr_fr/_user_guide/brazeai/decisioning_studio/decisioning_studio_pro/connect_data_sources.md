---
nav_title: Connecter les sources de données
article_title: Connecter les sources de données
page_order: 1
description: "Découvrez comment connecter des sources de données clients à BrazeAI Decisioning Studio Pro pour une prise de décision personnalisée en matière d'intelligence artificielle."
---

# Connecter les sources de données

> BrazeAI Decisioning Studio™ Les agents Pro doivent comprendre parfaitement le contexte du client pour prendre des décisions efficaces. Cet article explique comment connecter des sources de données clients à Decisioning Studio Pro.

{% alert tip %}
Votre équipe d'intelligence artificielle Decisioning Services vous aidera à configurer les connexions de données pour des performances optimales.
{% endalert %}

## Modèles d'intégration pris en charge

Decisioning Studio Pro prend en charge plusieurs modèles d'intégration pour connecter les données des clients :

| Modèle d'intégration | Meilleur pour | Complexité de la configuration |
|---------------------|----------|------------------|
| **Plateforme de données Braze** | Les clients qui utilisent déjà Braze | Faible |
| **Braze - Ingestion de données dans le nuage (CDI)** | Connexion d'entrepôts de données externes | Moyen |
| **Stockage en nuage (GCS, AWS, Azure)** | Exportation directe de données à partir d'autres plateformes | Moyen |
| **Intégrations CEP** | SFMC, extensions de données Klaviyo | Moyen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Types de données personnalisées

Les ressources de données personnalisées suivantes aident les agents à personnaliser plus efficacement :

| Type de données | Description | Exemples |
|-----------|-------------|----------|
| **Profil du client** | Attributs statiques et à évolution lente | Années comme client, géographie, canal d'acquisition, niveau de satisfaction, estimation de la valeur vie |
| **Le comportement des clients** | Modèles d'activité et d'engagement | Identifiants de compte, type d'appareil, interactions avec le service clientèle, utilisation des produits. |
| **Historique des transactions** | Données relatives aux achats et à la conversion | Produits achetés, montants des transactions, modes de paiement, canaux d'achat |
| **Engagement des marketeurs** | Réponses aux communications | Ouvertures/clics sur les e-mails, engagement par SMS, activité web et mobile, réponses aux enquêtes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert tip %}
Plus les agents disposent d'informations sur vos clients, plus ils seront performants. Pensez à inclure des données sur toutes les informations qui seraient particulièrement importantes pour votre entreprise (par exemple, voulez-vous voir comment l'intelligence artificielle traite différemment vos clients fidèles ? Assurez-vous que le statut de fidélité figure dans les données du client).
{% endalert %}

## Connecter les données par plateforme

{% tabs %}
{% tab Braze %}

### Envoyer les données des clients par l'intermédiaire de Braze

BrazeAI Decisioning Studio peut utiliser toutes les données que vous envoyez déjà à la plateforme de données de Braze.

S'il existe des données client que vous souhaitez utiliser pour Decisioning Studio et qui ne sont pas actuellement stockées dans le profil utilisateur ou les attributs personnalisés, l'approche recommandée consiste à utiliser Braze [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) pour ingérer des données à partir d'autres sources.

CDI prend en charge les intégrations directes avec :

- Snowflake
- Redshift
- BigQuery
- Databricks
- Microsoft Fabric
- AWS S3

Pour obtenir la liste complète des sources prises en charge, consultez la rubrique [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

Une fois que vous êtes satisfait des données que vous envoyez dans la plateforme de données de Braze, contactez votre équipe de services d'intelligence artificielle pour discuter des champs du profil utilisateur ou des attributs personnalisés à utiliser pour l'intelligence artificielle.

Pour rationaliser ce processus, créez une liste d'attributs de profil utilisateur Braze qui, selon vous, représentent le mieux les comportements de vos clients à utiliser dans Decisioning Studio (voir la [liste des champs disponibles]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/#fields-to-export)). Votre équipe de services peut également vous aider à mener des sessions de découverte pour décider quels champs sont les plus appropriés pour l'intelligence artificielle.

D'autres options pour l'envoi de données sont possibles :

- Envoi d'événements personnalisés Braze via le SDK
- L'envoi d'événements à l'aide de l'endpoint REST ([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track))

Ces modèles nécessitent un effort d'ingénierie plus important, mais sont parfois préférables en fonction de votre configuration Braze actuelle. Prenez contact avec l'équipe des services d'intelligence artificielle décisionnelle pour en savoir plus.

{% endtab %}
{% tab SFMC %}

### Envoyer les données des clients par l'intermédiaire du SFMC

Pour les intégrations de Salesforce Marketing Cloud :

1. Configurez les extensions de données SFMC pour vos données personnalisées.
2. Configurez SFMC Installed Package pour l'intégration API avec les autorisations appropriées requises par Decisioning Studio.
3. Veillez à ce que les extensions de données soient actualisées quotidiennement, car Decisioning Studio s'appuiera sur les dernières données incrémentielles disponibles.

Fournissez l'ID d'extension et la clé API à votre équipe de services décisionnels de l'intelligence artificielle. Ils vous assisteront dans les prochaines étapes de l'ingestion des données personnalisées.

{% endtab %}
{% tab Klaviyo %}

### Envoyez les données de vos clients par l'intermédiaire de Klaviyo.

Pour les intégrations Klaviyo :

1. Confirmez que les données du profil du client sont disponibles dans les profils Klaviyo.
2. Générer une clé API privée avec accès complet aux profils
3. Fournissez la clé API à votre équipe de services d'aide à la décision en matière d'intelligence artificielle.

Consultez la [documentation de Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908) pour plus d'informations sur la configuration de la clé API.

{% endtab %}
{% tab Cloud Storage %}

### Autres solutions en nuage (Google cloud storage, Azure, AWS)

Si les données des clients ne sont pas actuellement stockées dans Braze, SFMC ou Klaviyo, la meilleure étape suivante consiste à configurer une exportation automatisée directement vers un compartiment Google Cloud Storage contrôlé par Braze. Nous pouvons également prendre en charge l'exportation vers AWS ou Azure (bien que GCS soit préférable). Pour ces plateformes, l'exportation vers leur stockage interne en nuage dans ces plateformes en nuage et Braze peut alors extraire ces données.

Pour savoir si cela est possible, reportez-vous à la documentation de votre plateforme Martech. Par exemple :

- mParticle propose une [intégration native avec Google cloud storage.](https://www.mparticle.com/integration/google-cloud-storage/)
- [Segmentation de Twilio](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

Si cela est possible, nous pouvons vous fournir un compartiment GCS pour exporter les données personnalisées vers un compartiment isolé de Decisioning Studio.

{% endtab %}
{% endtabs %}

## Bonnes pratiques

- **Noms de colonnes descriptifs**: Les données clients doivent avoir des noms de colonnes clairs et descriptifs. Idéalement, un dictionnaire de données devrait être fourni.
- **Mises à jour incrémentales**: Les fichiers incrémentaux sont préférables aux instantanés de l'ensemble de l'historique du client chaque jour.
- **Des identifiants cohérents**: Chaque enregistrement doit contenir un identifiant de client unique et cohérent pour toutes les ressources de données.
- **Inclure les horodatages**: Les enregistrements doivent être horodatés pour permettre une attribution précise et la formation des agents.

## Intégrations personnalisées

D'autres options ou des pipelines de données entièrement personnalisés sont possibles. Celles-ci peuvent nécessiter un travail supplémentaire de la part des services ou de l'ingénierie de votre équipe. Pour déterminer ce qui est faisable et optimal, collaborez avec votre équipe de services d'intelligence artificielle.

{% alert important %}
Ce guide explique les modèles d'intégration les plus courants. La sécurité de l'information devra toujours vérifier tous les points de connexion et des consultants en solutions seront disponibles pour vous conseiller sur la mise en œuvre.
{% endalert %}

## Étapes suivantes

Après avoir connecté vos sources de données, passez à la configuration de l'orchestration :

- [Mettre en place l'orchestration]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

