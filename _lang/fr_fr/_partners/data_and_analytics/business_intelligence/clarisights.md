---
nav_title: Clarisights
article_title: Clarisights
description: "Cet article de référence présente le partenariat entre Braze et Clarisights, une plateforme de reporting des performances marketing en libre-service, vous permettant d'importer les données des campagnes Braze et Canvas pour créer une interface unifiée de reporting des performances et de marketing CRM/de rétention."
alias: /partners/clarisights/
page_type: partner
search_tag: Partner

---

# Clarisights

> [Clarisights](https://clarisights.com) est une plateforme de reporting marketing en libre-service pour les entreprises axées sur les données. Elle intègre, traite et visualise automatiquement toutes vos données provenant de sources marketing, analytiques et d'attribution.

_Cette intégration est maintenue par Clarisights._

## À propos de l'intégration

L'intégration de Braze et de Clarisights vous permet d'importer les données des campagnes Braze et Canvas afin d'obtenir une interface de reporting unifiée des performances et du marketing CRM/dde rétention.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Clarisights | Un espace de travail Clarisights est nécessaire pour profiter de ce partenariat. |
| Clé API REST de Braze | Une clé API REST de Braze avec les autorisations suivantes :  <br> - `campaigns.list` <br>  - `campaigns.details`<br> - `campaigns.data_series` <br> - `canvas.details`<br> - `canvas.list` <br>  - `canvas.data_series` <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Votre endpoint dépendra de l'URL de Braze pour votre instance. |
| Nom de l'espace de travail de Braze | Le nom de l'espace de travail associé à la clé API de Braze. Ce nom sera utilisé pour identifier l'intégration de l'espace de travail sur Clarisights. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

Grâce à l'intégration de Braze et de Clarisights, les utilisateurs peuvent créer différentes visualisations et tableaux pour obtenir des informations sur les campagnes qu'ils ont créées. Les cas d'utilisation les plus courants sont les suivants :

{% tabs %}
{% tab Une meilleure visibilité %}
Meilleure visibilité sur les performances globales des campagnes et des Canvases.

![Un graphique montrant un exemple de la meilleure visibilité des performances dans la plateforme Clarisights. Ce graphique comprend des statistiques sur les campagnes et les canvas ouverts, les clics, les envois, les conversions, etc.]({{site.baseurl}}/assets/img/clarisights/overall_view.png)
{% endtab %}
{% tab Rapports détaillés %}
Rapports granulaires pour les campagnes et les canevas.

![Un graphique montrant des rapports précis, comme le "total des envois par canal d'envoi" et le "taux de conversion".]({{site.baseurl}}/assets/img/clarisights/unified_dashboard.png)
{% endtab %}
{% tab Tableaux de bord unifiés %}
Tableaux de bord unifiés pour les CMO et les CXO.

![Un graphique montrant un exemple de tableaux de bord unifiés.]({{site.baseurl}}/assets/img/clarisights/granular_reporting.png)
{% endtab %}
{% endtabs %}

## Intégration

Pour synchroniser les données Braze avec Clarisights, vous devez créer un connecteur Braze et connecter les espaces de travail Braze.

1. Dans Clarisights, accédez à la page **Intégrations**, localisez le connecteur **Braze** et sélectionnez **\+ Connecter.**<br>![Une liste des connecteurs disponibles sur le marché des intégrations Clarisights.]({{site.baseurl}}/assets/img/clarisights/integrations.png)<br><br>
2. Ensuite, à l'aide du flux d'intégration, connectez votre compte Clarisights à Braze. Pour ce faire, vous devez fournir la clé API REST de Braze, le nom de l'espace de travail Braze et l'endpoint REST de Braze.<br>![Connecteur d'espace de travail Braze dans la plateforme Clarisights. Cette page contient des champs pour le nom de l'espace de travail de Braze, la clé API REST de Braze et le point d'extrémité REST de Braze.]({{site.baseurl}}/assets/img/clarisights/braze_flow.png)<br><br>Avant une intégration réussie, les utilisateurs verront les espaces de travail connectés sur la même page.<br>![Dans "Comptes Braze", vous trouverez une liste des espaces de travail connectés.]({{site.baseurl}}/assets/img/clarisights/connected.png)<br><br>

## Utilisation de cette intégration

Pour inclure Braze comme source de données dans vos rapports Clarisights, naviguez vers **Créer un nouveau rapport.** Nommez votre rapport et sélectionnez **Braze** comme source de données dans l'invite qui s'affiche. Vous pouvez également choisir les indicateurs et les dimensions à inclure dans le rapport. Lorsque vous avez terminé, sélectionnez **Créer un rapport**. 

Les données de Braze commenceront à circuler à partir de la prochaine importation de données planifiée. Contactez votre gestionnaire de satisfaction client Clarisights pour demander des remplissages historiques pour des durées plus longues. 

![Paramètres du rapport Clarisight affichant les champs pour le nom et la source de données. Dans cet exemple, "Braze" est sélectionné comme source de données.]({{site.baseurl}}/assets/img/clarisights/braze_report.png)

Visitez Clarisights pour plus d'informations sur les [indicateurs et dimensions](https://help.clarisights.com/en/articles/5670864-braze-metrics-and-dimensions) disponibles ou sur la [création de rapports](https://help.clarisights.com/en/articles/1421478-creating-a-report-using-clarisights).


