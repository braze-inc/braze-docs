---
nav_title: Données Sisu
article_title: Données Sisu
description: "Cet article de référence décrit le partenariat entre Braze et Sisu Data, un leader de l'intelligence décisionnelle dans le cloud, qui vous permet de comprendre, dans toutes les campagnes ou au niveau de la campagne, pourquoi les indicateurs évoluent et ce qui permet d'obtenir les meilleurs résultats."
alias: /partners/sisudata
page_type: partner
search_tag: Partner
---

# Données Sisu

> [Sisu Data][2] est le leader de l'intelligence décisionnelle dans le cloud qui utilise le machine learning pour décomposer automatiquement les performances métriques et fournir des informations exploitables rapides et complètes.

L'intégration de Sisu Data et Braze vous permet de comprendre pourquoi les indicateurs (par exemple, le taux d'ouverture, le taux de clics, le taux de conversion, etc.) évoluent et comment obtenir les meilleurs résultats. Une fois ces segments identifiés, les utilisateurs de Braze peuvent matérialiser les résultats dans leur entrepôt de données ou les envoyer directement de Sisu à Braze pour recibler et réengager les utilisateurs.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Sisu | Un compte [Sisu][3] est nécessaire pour bénéficier de ce partenariat. |
| Entrepôt cloud | Cette intégration suppose que vos données Braze sont stockées dans un entrepôt cloud (par exemple, Snowflake, BigQuery). Pour rationaliser ce processus d'intégration, nous vous recommandons d'utiliser la fonctionnalité native de Braze via [Currents][4]. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Préparer un ensemble de données

L'ensemble de données doit indiquer l'indicateur clé de performance que Sisu doit analyser. Par exemple, si vous souhaitez mieux comprendre pourquoi les taux de conversion baissent d'une semaine à l'autre, l'enregistrement de la portée de la campagne doit représenter les conversions hebdomadaires. Les colonnes de l'ensemble de données devraient correspondre aux raisons potentielles de la baisse du taux de conversion.

### Étape 2 : Création d'une métrique  

Une fois le jeu de données préparé, vous devez créer une métrique qui fait référence à une colonne agrégée. Comme un jeu de données peut générer plusieurs indicateurs, l'utilisateur peut également sélectionner un ensemble de dimensions qui devraient ou ne devraient pas faire partie de toutes les analyses par défaut. Notez que les utilisateurs peuvent toujours continuer à effectuer des tâches de curation au niveau de l'analyse.

![][6]

### Étape 3 : Création d'une analyse  

Les utilisateurs peuvent créer différentes analyses dans Sisu en fonction du cas d'utilisation. L'une des analyses les plus courantes est l'analyse d'une période à l'autre afin de comprendre quels segments ont le plus évolué. Les utilisateurs peuvent décider d'analyser des périodes quotidiennes, hebdomadaires, mensuelles ou personnalisées en sélectionnant les périodes relatives.

Par exemple, l'utilisateur peut créer une analyse mensuelle du taux de conversion pour un groupe d'annonces et un canal d'engagement spécifiques et identifier les principaux facteurs positifs et négatifs.

{% tabs %}
{% tab Principaux facteurs positifs %}

![]({% image_buster /assets/img/sisudata/kda_result_positive.png %})

{% endtab %}
{% tab Principaux facteurs négatifs %}

![]({% image_buster /assets/img/sisudata/kda_result_negative.png %})

{% endtab %}
{% endtabs %}

À partir de là, vous pouvez vous concentrer sur les cohortes auxquelles ils souhaiteront participer ou modifier des campagnes. Par exemple, Sisu a automatiquement identifié que les notifications push envoyées le mardi et les e-mails envoyés en gros volumes affectaient gravement le taux de conversion.

![][9]

### Étape 4 : Réinscrire les résultats dans l'entrepôt de données

Les utilisateurs peuvent extraire les résultats de Sisu à l'aide de l'API de [Sisu] ][10] et matérialiser les segments dans un entrepôt de données. [Les clients de Snowflake peuvent activer ces segments dans Braze via Cloud Data Ingestion.][5]

Pour les autres entrepôts de données, les utilisateurs peuvent tirer parti d'une solution d'activation existante ou contacter Sisu pour obtenir de l'aide supplémentaire.

## Service d’assistance

Pour toute question concernant cette intégration, contactez Sisu à l'adressepartners@sisudata.com.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://sisudata.com/
[3]: https://sisudata.com/
[4]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/
[6]: {% image_buster /assets/img/sisudata/metric_creation.png %}
[9]: {% image_buster /assets/img/sisudata/segment.png %}
Il y a [10]: https://docs.sisudata.com/docs/api/#tag/AnalysesService/operation/AnalysesService_AnalysisRunResults
