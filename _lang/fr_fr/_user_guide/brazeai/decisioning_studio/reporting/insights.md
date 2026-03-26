---
nav_title: Informations
article_title: Rapport d'informations
page_order: 2
description: "Découvrez comment utiliser le rapport d'informations pour comprendre comment les options de recommandation de votre banque d'actions sont générées dans BrazeAI Decisioning Studio."
---

# Rapport d'informations

> Les informations vous montrent comment les différentes options de recommandation de votre banque d'actions sont générées, comme la sélection de blocs. Il existe deux rapports d'informations : **Préférences de l'agent** et **SHAPs**.

{% tabs local %}
{% tab agent preferences %}
Le rapport **Préférences de l'agent** vous aide à identifier les tendances saisonnières et à évaluer la pertinence des choix dans la banque d'actions, pour orienter vos décisions de mise à jour.

![Rapport des préférences de l'agent affichant un graphique à barres comparant la fréquence de sélection des différentes options de recommandation sur une période donnée. Le graphique présente plusieurs barres colorées, chacune représentant une option de recommandation de la banque d'actions, avec l'axe des ordonnées indiquant le pourcentage de sélection et l'axe des abscisses listant les noms des options.]({% image_buster /assets/img/decisioning_studio/reporting_insights_agent_preferences.png %})

Consultez le tableau suivant pour plus de détails sur ce rapport :

| Champ | Description |
|-------|-------------|
| Dimension | L'attribut utilisé pour organiser les résultats, comme le canal, la campagne ou la plateforme. |
| Groupe de comparaison | Les groupes que vous souhaitez comparer dans votre rapport. Vous pouvez sélectionner plusieurs groupes de comparaison. |
| Paramètre | L'indicateur appliqué à cet attribut, comme les ouvertures, les clics ou le taux de conversion. |
| Segment | Le [segment d'audience]({{site.baseurl}}/user_guide/engagement_tools/segments/) que vous avez créé dans Braze. |
| Option             | L'option de recommandation spécifique sélectionnée dans la banque d'actions. |
| Description        | Une courte explication de ce que représente l'option.            |
| Nombre de sélections  | Le nombre total de fois où l'option a été sélectionnée.         |
| % de sélection   | Le pourcentage de sélections totales où cette option a été choisie. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab SHAPs %}
Le rapport **SHAPs** s'appuie sur le modèle Shapley Additive exPlanations (SHAP) pour vous aider à quantifier la contribution de chaque fonctionnalité ou variable à votre agent de recommandation. Chaque point du graphique représente une valeur SHAP, et la distribution des points donne une idée générale de l'impact directionnel d'une fonctionnalité.

![Graphique du rapport SHAPs affichant un diagramme à barres horizontales avec plusieurs barres colorées représentant différentes fonctionnalités ou variables. Chaque barre montre l'impact d'une fonctionnalité sur l'agent de recommandation, avec l'axe des abscisses indiquant la valeur SHAP et l'axe des ordonnées listant les noms des fonctionnalités telles que Récence, Fréquence et Canal. Le graphique illustre comment chaque fonctionnalité contribue positivement ou négativement aux prédictions de l'agent.]({% image_buster /assets/img/decisioning_studio/reporting_insights_shaps.png %})

{% endtab %}
{% endtabs %}