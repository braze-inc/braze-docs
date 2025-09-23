---
nav_title: Eppo
article_title: Eppo
description: "Découvrez comment intégrer Eppo à Braze."
alias: /partners/eppo/
page_type: partner
search_tag: Partner
---

# Eppo

> [Eppo](https://www.geteppo.com/) est une plateforme d'expérimentation de nouvelle génération qui permet aux équipes d'effectuer des tests A/B, de gérer les fonctionnalités à l'échelle et d'exploiter les informations basées sur l'intelligence artificielle pour prendre des décisions fondées sur les données.

*Cette intégration est maintenue par Eppo.*

L'intégration de Braze et d'Eppo vous permet de mettre en place des tests A/B dans Braze et d'analyser les résultats dans Eppo pour découvrir des informations et lier la performance des messages à des indicateurs commerciaux à long terme tels que le chiffre d'affaires ou la fidélisation.

## Conditions préalables

| Condition                        | Description                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------|
| Compte Eppo                       | Un compte Eppo est nécessaire pour bénéficier de ce partenariat.                   |
| Partage des données sur les courants ou les Snowflakes | Le partage de données Currents ou Snowflake est nécessaire pour qu'Eppo puisse analyser les données des expériences. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Configurez le partage des données Currents ou Snowflake dans Braze

Eppo analyse les expériences directement dans votre entrepôt de données. Pour permettre l'intégration, les données d'envoi de messages de Braze doivent être disponibles dans l'entrepôt connecté à Eppo. Vous pouvez exporter les données de campagne de Braze à l'aide de Currents, ou accéder aux données de Braze dans votre instance de Snowflake à l'aide de [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake).

### Étape 2 : Implantez votre expérience dans une campagne Braze ou Canvas.

Vous pouvez utiliser les fonctionnalités natives de test A/B dans vos campagnes et Canvases. Pour en savoir plus, consultez la rubrique [Test multivarié et test A/B](https://www.braze.com/docs/user_guide/engagement_tools/testing/multivariant_testing#what-are-multivariate-and-ab-testing).

### Étape 3 : Mise en place d'Eppo pour mesurer les expériences de Braze

Pour réaliser des expériences à l'aide des données de Braze dans Eppo, créez dans votre entrepôt des [tables d'affectations](https://docs.geteppo.com/data-management/definitions/assignment-sql/) basées sur les données d'événements de messages au niveau de l'utilisateur exportées depuis Braze. Il est recommandé d'utiliser des tableaux distincts pour les expériences Canvas et les campagnes, car elles reposent sur des métadonnées différentes.

{% tabs local %}
{% tab expériences Canvas %}
Pour les expériences Canvas, les affectations peuvent être créées soit :

- Au niveau d'entrée de Canvas (`users.canvas.Entry`)
- Ou dans une étape de l'expérience Canvas (`users.canvas.experimentstep.SplitEntry`)

Dans ce cas, des champs tels que `canvas_name`, `experiment_step_id`, `canvas_variation_name`, et `experiment_split_id` sont utilisés pour définir le nom et la variation de l'expérience.

{% endtab %}

{% tab expériences de campagne %}
Pour les expériences de campagne, utilisez des événements d'envoi (tels que push, e-mail, SMS) pour déterminer quand un utilisateur est entré dans l'expérience. `campaign_name` Les données de la table d'assignation, `message_variation_name` et `time`, sont utilisées pour remplir la table d'assignation.

{% endtab %}
{% endtabs %}

Pour suivre les indicateurs spécifiques aux messages (comme les clics ou les ouvertures), incluez une **entité secondaire** en créant une adresse `combined_id` qui associe l'ID de l'utilisateur au nom de la campagne ou du Canvas. Ce site `combined_id` est également utilisé dans vos tables de faits pour aligner les indicateurs sur l'expérience et la variation correctes.

Eppo utilise ces affectations et ces tables de faits pour analyser les résultats. Il est recommandé de mettre en place un **protocole** dans Eppo afin de standardiser la configuration des expériences futures. Pour plus d'informations, reportez-vous à la [documentation d'Eppo](https://docs.geteppo.com/guides/marketing/integrating-with-braze/).

## Assistance

Pour toute question concernant la configuration de Braze Currents, le partage de données Snowflake ou la configuration de campagnes à plusieurs variables, contactez votre gestionnaire de satisfaction client Braze.

Pour obtenir de l'aide sur la configuration d'Eppo afin de mesurer les expériences de Braze, contactez l'équipe d'assistance d'Eppo.
