---
nav_title: Sisu Data
article_title: Sisu Data
description: "Cet article de référence décrit le partenariat entre Braze et Sisu Data, un leader dans l’intelligence décisionnelle sur le cloud, qui vous permet de comprendre dans toutes les campagnes ou au niveau de la campagne pourquoi les indicateurs changent et ce qui génère les résultats les plus optimaux."
alias: /partners/sisudata
page_type: partner
search_tag: Partenaire
---

# Sisu Data

> [Sisu Data][2] est le leader de l’intelligence décisionnelle cloud qui utilise le machine learning pour décomposer automatiquement les indicateurs de performances et fournir des insights rapides, complets et exploitables.

L’intégration de Sisu Data et Braze vous permet de comprendre dans toutes les campagnes ou au niveau de la campagne pourquoi les indicateurs (par ex., taux d’ouverture, taux de clics, taux de conversion, etc.) changent et ce qui génère les résultats les plus optimaux. Une fois ces segments identifiés, les utilisateurs de Braze peuvent matérialiser les sorties dans leur entrepôt de données ou les envoyer directement de Sisu vers Braze pour recibler et réengager les utilisateurs.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Sisu | Un compte [Sisu][3] est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze | [URL de votre endpoint REST][1]. Votre endpoint dépendra de l’URL Braze pour votre instance. |
| Entrepôt cloud | Cette intégration suppose que vos données Braze sont stockées dans un entrepôt cloud (par ex. Snowflake, BigQuery). Pour rationaliser ce processus d’intégration, nous recommandons d’utiliser la fonctionnalité native de Braze à l’aide de [Currents][4]. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Préparer un jeu de données

Le jeu de données doit indiquer le KPI que vous souhaitez que Sisu analyse. Par exemple, si vous souhaitez mieux comprendre pourquoi les taux de conversion ont chuté d’une semaine à l’autre, l’enregistrement de la portée doit représenter une conversion hebdomadaire. Les colonnes du jeu de données doivent être constituées des raisons potentielles pour lesquelles le taux de conversion pourrait chuter.

### Étape 2 : Créer un indicateur  

Une fois le jeu de données préparé, vous devrez créer un indicateur qui fait référence à une colonne agrégée. Étant donné qu’un jeu de données peut alimenter plusieurs indicateurs, l’utilisateur peut également organiser un ensemble de dimensions qui devraient ou ne devraient pas faire partie de toutes les analyses par défaut. Notez que les utilisateurs peuvent toujours continuer à organiser au niveau de l’analyse.

![][6]

### Étape 3 : Créer une analyse  

Il existe différentes analyses pouvant être créées par les utilisateurs dans Sisu en fonction du cas d’utilisation. L’une des analyses les plus courantes est une analyse d’une période à l’autre pour comprendre quels segments ont le plus changé. Les utilisateurs peuvent décider d’analyser des périodes quotidiennes, hebdomadaires, mensuelles ou personnalisées en sélectionnant les périodes relatives.

Par exemple, l’utilisateur peut créer une analyse du taux de conversion mois par mois pour un groupe publicitaire et un canal d’engagement particuliers et comprendre les principaux facteurs de modification positifs et négatifs.

{% tabs %}
{% tab Top positive drivers %}

![]({% image_buster /assets/img/sisudata/kda_result_positive.png %})

{% endtab %}
{% tab Top negative drivers %}

![]({% image_buster /assets/img/sisudata/kda_result_negative.png %})

{% endtab %}
{% endtabs %}

À partir de là, vous pouvez affiner les cohortes dans lesquelles ils peuvent vouloir s’engager ou modifier des campagnes. Par exemple, Sisu a automatiquement identifié que les notifications push envoyées le mardi et les e-mails envoyés en gros volumes affectent gravement le taux de conversion.

![][9]

### Étape 4 : Réécrire les résultats dans l’entrepôt de données

Les utilisateurs peuvent extraire les résultats de Sisu à l’aide de l’[API de Sisu][10] et matérialiser les segments dans un entrepôt de données. Les clients de Snowflake peuvent activer ces segments dans Braze à l’aide de l’[ingestion de données cloud][5].

Pour les autres entrepôts de données, les utilisateurs peuvent tirer parti d’une solution d’activation existante ou contacter Sisu pour obtenir une aide supplémentaire.

## Assistance

Pour toute question concernant cette intégration, contactez Sisu à l’adresse e-mail partners@sisudata.com.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://sisudata.com/
[3]: https://sisudata.com/
[4]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/
[6]: {% image_buster /assets/img/sisudata/metric_creation.png %}
[9]: {% image_buster /assets/img/sisudata/segment.png %}
[10]: https://docs.sisudata.com/docs/api/#tag/AnalysesService/operation/AnalysesService_AnalysisRunResults