---
nav_title: Clarisights
article_title: Clarisights
page_order: 1
description: "Cet article de référence décrit le partenariat entre Braze et Clarisights, une plateforme de reporting de performance marketing en libre-service, vous permettant d’importer des données à partir des campagnes et Canvas Braze pour aider à obtenir une interface unifiée de reporting de performance et de marketing CRM/retention."
alias: /partners/Clarisights/
page_type: partner
search_tag: Partenaire

---

# Clarisights

> [Clarisights][2] est une plateforme de reporting en libre-service pour la performance marketing destinée aux entreprises axées sur les données. Elle intègre, traite et visualise automatiquement toutes vos données provenant de sources marketing, analytiques et d’attribution.

L’intégration entre Braze et Clarisights vous permet d’importer des données issues des campagnes et Canvas de Braze pour aider à obtenir une interface unifiée de reporting de performance et de marketing CRM/retention.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Clarisights | Un espace de travail Clarisights est requis pour profiter de ce partenariat |
| Clé d’API REST Braze | Une clé API REST Braze avec les autorisations suivantes :  <br> - `campaigns.list` <br>  - `campaigns.details`<br> - `campaigns.data_series` <br> - `canvas.details`<br> - `canvas.list` <br>  - `canvas.data_series` <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze | [URL de votre endpoint REST][1]. Votre endpoint dépendra de l’URL Braze pour votre instance. |
| Nom du groupe d’apps Braze | Nom du groupe d’apps associé à la clé API Braze. Ce nom sera utilisé pour identifier l’intégration du groupe d’apps dans Clarisights. |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d’utilisation

Avec l’intégration de Braze et Clarisights, les utilisateurs peuvent créer différents tableaux et visualisations pour obtenir des informations sur les campagnes qu’ils ont créées. Les cas d’utilisation les plus répandus incluent :

{% tabs %}
{% tab Better visibility %}
Meilleure visibilité sur les campagnes globales et les performances des Canvas.

![Un graphique montrant un exemple de meilleure visibilité sur la plateforme Clarisights. Ce graphique comprend des statistiques sur les ouvertures, les clics, les envois et les conversions relatives aux campagnes et Canvas.]({{site.baseurl}}/assets/img/clarisights/overall_view.png)
{% endtab %}
{% tab Granular reporting %}
Rapports granulaires pour les campagnes et les Canvas.

![Graphique montrant des rapports granulaires, comme « total des envois par canal d’envoi » et « taux de conversion ».]({{site.baseurl}}/assets/img/clarisights/unified_dashboard.png)
{% endtab %}
{% tab Unified dashboards %}
Tableaux de bord unifiés pour les directeurs marketing et les directeurs de l’expérience client.

![Un graphique montrant un exemple de tableaux de bord unifiés.]({{site.baseurl}}/assets/img/clarisights/granular_reporting.png)
{% endtab %}
{% endtabs %}

## Intégration

Pour synchroniser les données de Braze avec Clarisights, vous devez créer un connecteur Braze et connecter des groupes d’apps Braze.

1. Dans Clarisights, accédez à la page **Integrations (Intégrations)**, recherchez le connecteur **Braze**, puis sélectionnez **+ Connect (+ Connexion)**.<br>![Liste des connecteurs disponibles sur le marketplace des intégrations de Clarisights.][6]<br><br>
2. Ensuite, en utilisant le flux d’intégration, connectez votre compte Clarisights à Braze. Pour ce faire, vous pouvez fournir votre clé API REST Braze, le nom du groupe d’apps Braze et l’endpoint REST de Braze.<br>![Connecteur de groupe d’apps Braze dans la plateforme Clarisights. Cette page comporte des champs pour le nom du groupe d’apps Braze, la clé API REST Braze et l’endpoint REST de Braze.][7]<br><br>Avant que l’intégration ne soit effectuée, les utilisateurs verront les groupes d’apps connectés sur la même page.<br>![Vous trouverez une liste des groupes d’apps connectés dans « Comptes Braze ».][9]<br><br>

## Comment utiliser cette intégration

Pour inclure Braze comme source de données dans vos rapports Clarisights, accédez à **Create New Report (Créer un nouveau rapport)**. Nommez votre rapport et sélectionnez **Braze** comme source de données dans l’invite qui apparaît. Vous pouvez également choisir les indicateurs et dimensions à inclure dans le rapport. Une fois terminé, sélectionnez **Create Report (Créer un rapport)**. 

Les données de Braze commenceront à affluer à partir de la prochaine importation de données que vous avez programmée. Contactez votre gestionnaire du succès des clients Clarisights afin de demander des renvois pour des durées supérieures. 

![Paramètres de rapport Clarisight affichant les champs relatifs au nom et à la source des données. Dans cet exemple, « Braze » est sélectionné comme source de données.][8]

Rendez-vous sur le site Web de Clarisights pour plus d’informations sur les [indicateurs et dimensions][10] disponibles ou la [création de rapports][11].

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://clarisights.com
[3]: {{site.baseurl}}/assets/img/clarisights/overall_view.png
[4]: {{site.baseurl}}/assets/img/clarisights/unified_dashboard.png
[5]: {{site.baseurl}}/assets/img/clarisights/granular_reporting.png
[6]: {{site.baseurl}}/assets/img/clarisights/integrations.png
[7]: {{site.baseurl}}/assets/img/clarisights/braze_flow.png
[8]: {{site.baseurl}}/assets/img/clarisights/braze_report.png
[9]: {{site.baseurl}}/assets/img/clarisights/connected.png
[10]: https://help.clarisights.com/en/articles/5670864-braze-metrics-and-dimensions
[11]: https://help.clarisights.com/en/articles/1421478-creating-a-report-using-clarisights
