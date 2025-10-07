---
nav_title: Afficher les rapports
article_title: Afficher les rapports de Decisioning Studio
page_order: 3
description: "Découvrez comment afficher les rapports BrazeAI Decisioning Studio™ dans Braze afin de comprendre l'impact des décisions basées sur l'IA sur vos campagnes."
---

# Afficher les rapports de Decisioning Studio

> Découvrez comment afficher les rapports BrazeAI Decisioning Studio™ dans Braze afin de comprendre l'impact des décisions basées sur l'IA sur vos campagnes. Des indicateurs de performances à la santé des données et aux modifications du système, ces rapports vous aident à comprendre les résultats, à résoudre les problèmes et à prendre des décisions avisées en toute confiance.

## Conditions préalables

Avant de pouvoir afficher les rapports de Decisioning Studio dans la Braze, vous devez :

- Disposer d'un contrat actif pour Braze et BrazeAI Decisioning Studio™. 
- Contacter votre CSM pour qu'il active BrazeAI Decisioning Studio™ en votre nom.
- Disposer d'un agent BrazeAI Decisioning Studio™ en ligne.

## Afficher les rapports {#view}

Pour afficher les indicateurs des agents de Decisioning Studio dans Braze, sélectionnez **AI Decisioning (Prise de décisions basées sur l’IA)** > **BrazeAI Decisioning Studio™**, puis sélectionnez un agent.

\![Écran d'accueil des rapports BrazeAI Decisioning Studio™ montrant un tableau de bord avec plusieurs fiches de rapport. Chaque fiche montre un type de rapport tel que les performances, les informations, les diagnostics et la chronologie, avec de brèves descriptions et les icônes correspondantes.]( {% image_buster /assets/img/decisioning_studio/reporting_home.png %} )

Ici, vous pouvez consulter des rapports tels que les performances, les informations, les diagnostics et les chronologies. Pour plus de détails, voir [Rapports disponibles](#reports).

## Modifier les dates des rapports

Après avoir [ouvert un rapport](#view), vous pouvez modifier la plage de dates en sélectionnant une nouvelle date de début et de fin dans le menu déroulant du calendrier.

\![Sélecteur de plage de dates de BrazeAI Decisioning Studio™ ouvert avec une liste déroulante de calendrier. Le calendrier affiche des dates de début et de fin sélectionnables pour personnaliser l'affichage du rapport.]({% image_buster /assets/img/decisioning_studio/reporting_change_date_range.png %}){: style="max-width:50%;"}

Vous pouvez également définir une date de début par défaut ou choisir des dates à exclure systématiquement. Les dates exclues seront supprimées de tous les rapports pour cet agent.

Pour définir ou exclure des dates, sélectionnez <i class="fa-solid fa-gear"></i> **Settings (Paramètres)**, puis modifiez votre date par défaut ou excluez des dates si nécessaire.

\![Panneau des paramètres ouvert dans BrazeAI Decisioning Studio™ affichant des options permettant de définir une date de début par défaut et d'exclure certaines dates spécifiques des rapports. Le panneau affiche deux sections intitulées Default start date (Date de début par défaut) et Exclude dates (Exclure des dates). Sous Exclude dates (Exclure des dates), plusieurs dates s’affichent avec des cases à cocher.]({% image_buster /assets/img/decisioning_studio/reporting_set_exclude_dates.png %})

## Rapports disponibles {#reports}

### Performances

Le rapport de performances propose des indicateurs généraux sur les agents. Ils permettent de comparer les groupes de traitement (de Braze) à un ou plusieurs groupes de contrôle (par exemple, le chiffre d'affaires). Il peut être affiché de deux façons différentes : **Trending (Tendances)** et**Driver Tree (Arborescence des facteurs)**.

Par défaut, le rapport utilise la vue **Trending (Tendances)**, qui compare les performances de BrazeAI™ dans le temps par rapport à vos groupes de contrôle, et suit l'évolution de l'augmentation.

\![Vue Tendances du rapport de performances montrant un graphique linéaire comparant les performances de BrazeAI™ et des groupes de contrôle au fil du temps. Le graphique affiche deux lignes intitulées BrazeAI™ et Control (Contrôle), l'axe des ordonnées étant intitulé Uplift (Augmentation) et l'axe des abscisses indiquant les dates. Une légende identifie chaque groupe par sa couleur.]({% image_buster /assets/img/decisioning_studio/reporting_agent_performance_trending.png %})

Vous pouvez également sélectionner **Driver Tree (Arborescence des facteurs)** pour visualiser et mieux comprendre les relations entre les principaux facteurs de valeur et les indicateurs cibles.

\![Vue Driver Tree (Arborescence des facteurs) du rapport de performances montrant un diagramme hiérarchique des correspondances entre les principaux facteurs de valeur et les indicateurs cibles. Le diagramme présente plusieurs nœuds connectés, chacun libellé avec un nom de facteur ou d'indicateur, illustrant la façon dont les différents facteurs contribuent aux performances globales.]({% image_buster /assets/img/decisioning_studio/reporting_performance_drivertree.png %})

Pour comparer les performances de deux groupes, utilisez les menus déroulants afin de sélectionner les critères de comparaison souhaités. Pour plus de détails, reportez-vous au tableau suivant :

| Champ | Description |
|-------|-------------|
| Groupes de comparaison | Groupes que vous souhaitez comparer dans votre rapport. |
| Agrégation | Façon dont le rapport regroupe les données, comme les totaux, les moyennes ou les pourcentages. |
| Segments | [Segments d'audience]({{site.baseurl}}/user_guide/engagement_tools/segments/) que vous avez créés dans Braze. |
| Événements de la chronologie | Événements spécifiques affichés au fil du temps, tels que les envois de messages, les ouvertures ou les conversions. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Insights (Informations)

Le rapport Insights (Informations) vous montre comment sont générées les différentes options de recommandations de votre banque d'actions, comme la sélection de blocs ou SL. Il existe deux rapports d'informations différents : **Agent preferences (Préférences des agents)** et **SHAPs (SHAP)**.

{% tabs local %}
{% tab agent preferences %}
Le rapport **Agent preferences** vous aide à identifier les tendances saisonnières et à évaluer la pertinence des choix de la banque d'actions, ce qui vous permet de prendre des décisions avisées pour les mises à jour.

\![Rapport Agent preferences (Préférences des agents) montrant un diagramme à barres comparant la fréquence de sélection des différentes options de recommandations au cours d'une période donnée. Le graphique affiche plusieurs barres colorées, chacune représentant une option de recommandation de la banque d'actions, l'axe des ordonnées représentant le pourcentage de fois où l'option a été choisie et l'axe des abscisses énumérant les noms des options.]({% image_buster /assets/img/decisioning_studio/reporting_insights_agent_preferences.png %})

Pour plus de détails sur ce rapport, reportez-vous au tableau suivant :

| Champ | Description |
|-------|-------------|
| Dimension | Attribut utilisé pour organiser les résultats, comme le canal, la campagne ou la plateforme. |
| Groupe de comparaison | Groupes que vous souhaitez comparer dans votre rapport. Vous pouvez sélectionner plusieurs groupes de comparaison, jusqu'à NUM. |
| Paramètre | Indicateur appliqué cet attribut, comme les ouvertures, les clics ou le taux de conversion. |
| Segment | [Segment d'audience]({{site.baseurl}}/user_guide/engagement_tools/segments/) que vous avez créé dans Braze. |
| Option             | Option de recommandation spécifique sélectionnée dans la banque d'actions. |
| Description        | Brève explication de ce que représente l'option.            |
| Nombre de fois choisie  | Nombre total de fois où l'option a été sélectionnée.         |
| % de fois choisie   | Pourcentage de sélections totales où cette option a été choisie. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab shaps %}
Le rapport **SHAPs (SHAP)** utilise le modèle SHapley Additive exPlanations (SHAP) pour vous aider à quantifier la contribution de chaque fonctionnalité ou variable à votre modèle de recommandation. Chaque point du graphique représente un SHAP et la distribution des points donne une idée générale de l'impact directionnel d'une fonctionnalité.

\![Tableau du rapport SHAPs (SHAP) montrant un diagramme à barres horizontales avec plusieurs barres colorées représentant différentes fonctionnalités ou variables. Chaque barre montre l'impact d'une fonctionnalité sur le modèle de recommandation, l'axe des x affichant la valeur SHAP et l'axe des y énumérant les noms des fonctionnalités telles que le caractère récent, la fréquence et le canal. Le graphique visualise la contribution positive ou négative de chaque fonctionnalité dans les prédictions du modèle.]({% image_buster /assets/img/decisioning_studio/reporting_insights_shaps.png %})

{% endtab %}
{% endtabs %}

### Diagnostics

Le rapport Diagnostics contient deux types de rapports différents : **Outbound (Entrants)** et **Inbound (Sortants)**.

{% tabs local %}
{% tab outbound %}
Le rapport de diagnostics sortants indique le volume quotidien de recommandations générées et activées sur l'ensemble de vos audiences. Vous pouvez l’utiliser pour repérer les problèmes de distribution, suivre les pics ou les baisses d'activations et vérifier que les messages atteignent les bons groupes comme prévu.

\![Rapport de diagnostics sortants montrant un graphique linéaire du volume quotidien de recommandations générées et activées pour différents groupes d'audience. Le graphique affiche deux lignes intitulées Generated (Générées) et Activated (Activées), l'axe des ordonnées représentant le nombre de recommandations et l'axe des abscisses les dates. Une légende identifie chaque ligne par sa couleur. L'interface comprend des filtres déroulants pour la plage de dates et la sélection de l'audience au-dessus du graphique.]({% image_buster /assets/img/decisioning_studio/reporting_diagnostics_outbound.png %})

{% endtab %}

{% tab inbound %}

Le rapport de diagnostics entrants permet de contrôler la santé de vos flux de données dans BrazeAI™. Il affiche des informations telles que le nombre de fichiers, leur taille et le volume des lignes pour chaque ressource, ce qui vous aide à vérifier que les données sont transmises comme prévu et à résoudre les problèmes avant qu'ils n'affectent vos modèles ou vos campagnes.

Vous pouvez utiliser le menu déroulant pour sélectionner différents indicateurs, comme la taille moyenne des fichiers ou le nombre de fichiers.

\![Rapport de diagnostics entrant montrant un graphique linéaire avec le nombre de fichiers quotidiens et la taille moyenne des fichiers pour les ressources de données distribuées à BrazeAI™. Le graphique affiche deux lignes intitulées File count (Nombre de fichiers) et Average file size (Taille moyenne des fichiers) en Mo, l'axe des ordonnées représentant les valeurs et l'axe des abscisses les dates. Au-dessus du graphique se trouvent des filtres déroulants pour la sélection de la plage de dates et des ressources de données.]( {% image_buster /assets/img/decisioning_studio/reporting_diagnostics_inbound.png %} )

Pour plus de détails sur chaque indicateur du rapport des diagnostics entrants, reportez-vous au tableau suivant :

| Champ | Description |
|-------|-------------|
| Ressources de données | Nom de l'ensemble de données ou du fichier distribué. |
| Date | Date à laquelle les données ont été reçues. |
| Dernière heure de distribution | Heure la plus récente à laquelle les données ont été distribuées. |
| Nombre de fichiers | Nombre total de fichiers reçus. |
| Taille maximale des fichiers (Mo) | Taille du plus gros fichier reçu, en méga-octets. |
| Taille moyenne des fichiers (Mo) | Taille moyenne de tous les fichiers reçus, en méga-octets. |
| Nombre de lignes des fichiers | Nombre total de lignes contenues dans les fichiers distribués. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}

### Timeline (Chronologie)

Le rapport Timeline (Chronologie) fournit un enregistrement visuel des événements clés ainsi que de vos indicateurs de performances. Ces événements incluent, entre autres, les exécutions de modèles, les changements de configuration, les mises à jour des protections de sécurité, etc. Les annotations apparaissent directement sur les graphiques d'évolution et dans un onglet chronologique dédié, ce qui vous permet de connaître instantanément le contexte de l'évolution des résultats sans avoir à retracer l'historique des changements.

\![Rapport chronologique présentant un graphique avec les indicateurs de performances au fil du temps. Les événements clés tels que les exécutions de modèles, les changements de configuration et les mises à jour de protections de sécurité sont marqués par des icônes le long de la ligne de temps. Sous le graphique, un tableau répertorie les événements avec des colonnes pour la date, le type, le libellé, les détails et la visibilité dans les graphiques.]({% image_buster /assets/img/decisioning_studio/reporting_timeline.png %})

Pour comparer les performances de deux groupes, utilisez les menus déroulants afin de sélectionner les critères de comparaison souhaités. Pour plus de détails, reportez-vous au tableau suivant :

| Champ | Description |
|-------|-------------|
| Date | Date à laquelle l'événement s'est produit. |
| Type | Catégorie d'événement, telle qu’une mise à jour du système, une exécution de modèle ou un changement de configuration. |
| Libellé | Nom ou identifiant donné à l'événement. |
| Détails | Informations supplémentaires décrivant l'événement. |
| Visible dans les graphiques | Indique si l'événement est affiché dans les graphiques connexes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
