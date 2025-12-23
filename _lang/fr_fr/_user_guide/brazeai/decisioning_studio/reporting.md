---
nav_title: Rapports et Insights
article_title: Rapports et Insights
page_order: 3
description: "Découvrez comment afficher les rapports BrazeAI Decisioning Studio™ dans Braze, afin de comprendre l'impact des décisions basées sur l'intelligence artificielle sur vos campagnes."
---

# Rapports et Insights

> Découvrez comment afficher les rapports BrazeAI Decisioning Studio™ dans Braze, afin de comprendre l'impact des décisions basées sur l'intelligence artificielle sur vos campagnes. Des indicateurs de performance à la santé des données et aux modifications du système, ces rapports vous aident à comprendre les résultats, à résoudre les problèmes et à prendre des décisions éclairées en toute confiance.

## Conditions préalables

Avant de pouvoir consulter les rapports du studio décisionnel dans la Braze, vous devez :

- Disposer d'un contrat actif pour Braze et BrazeAI Decisioning Studio™. 
- Contactez votre CSM pour qu'il active BrazeAI Decisioning Studio™ en votre nom.
- Disposez d'un agent BrazeAI Decisioning Studio™ en ligne/en production/instantanée.

## Consultation des rapports {#view}

Pour afficher les indicateurs des agents d'un studio décisionnel dans Braze, accédez à **Intelligence artificielle** > **BrazeAI Decisioning Studio™**, puis sélectionnez un agent.

\![Écran d'accueil du rapport BrazeAI Decisioning Studio™ montrant un tableau de bord avec plusieurs fiches de rapport. Chaque carte affiche un type de rapport tel que Performance, Insights, Diagnostics et Timeline, avec de brèves descriptions et des icônes pour chacun d'entre eux.]( {% image_buster /assets/img/decisioning_studio/reporting_home.png %} )

Ici, vous pouvez consulter des rapports tels que les performances, les informations, les diagnostics et les calendriers. Pour plus de détails, voir [Rapports disponibles.](#reports)

## Modifier les dates des rapports

Après avoir [ouvert un rapport](#view), vous pouvez modifier la plage de dates en sélectionnant une nouvelle date de début et de fin dans le menu déroulant du calendrier.

\![Le sélecteur de plage de dates de BrazeAI Decisioning Studio™ s'ouvre avec un calendrier déroulant. Le calendrier affiche des dates de début et de fin sélectionnables pour personnaliser l'affichage du rapport.]({% image_buster /assets/img/decisioning_studio/reporting_change_date_range.png %}){: style="max-width:50%;"}

Vous pouvez également définir une date de début par défaut ou choisir des dates à exclure systématiquement. Les dates exclues seront filtrées de tous les rapports pour cet agent.

Pour définir ou exclure des dates, sélectionnez <i class="fa-solid fa-gear"></i> **Settings**, puis modifiez votre date par défaut ou excluez des dates si nécessaire.

\![Panneau des paramètres ouvert dans BrazeAI Decisioning Studio™ affichant des options permettant de définir une date de début par défaut et d'exclure des dates spécifiques des rapports. Le panneau affiche deux sections intitulées Date de début par défaut et Dates d'exclusion. Sous Exclure des dates, plusieurs dates sont répertoriées avec des cases à cocher à côté de chacune d'elles.]({% image_buster /assets/img/decisioning_studio/reporting_set_exclude_dates.png %})

## Rapports disponibles {#reports}

### Performance

Le rapport de performance propose des indicateurs de haut niveau sur les agents qui comparent les groupes de traitement (de Braze) à un ou plusieurs groupes de contrôle, (comme les chiffres affaires). Il soutient deux points de vue différents : **Arbre des****tendances** et des **conducteurs**.

Par défaut, le rapport utilise la vue **Tendance**, qui compare les performances de BrazeAI™ dans le temps par rapport à vos groupes de contrôle, et suit l'évolution de l'élévation.

Vue des tendances du rapport de performance montrant un graphique linéaire comparant les performances du BrazeAI™ et du groupe de contrôle au fil du temps. Le graphique affiche deux lignes intitulées BrazeAI™ et Control, l'axe des ordonnées étant intitulé Uplift et l'axe des abscisses indiquant les dates. Une légende identifie chaque groupe par sa couleur.]({% image_buster /assets/img/decisioning_studio/reporting_agent_performance_trending.png %})

Vous pouvez également sélectionner l'**arborescence des** moteurs pour voir comment les principaux moteurs de valeur sont liés aux indicateurs cibles, ce qui vous aidera à mieux comprendre la relation qui existe entre eux.

L'arborescence des inducteurs du rapport de performance présente un diagramme hiérarchique qui mappe les inducteurs de valeur clés aux indicateurs cibles. Le diagramme présente plusieurs nœuds connectés, chacun étiqueté avec un nom de pilote ou d'indicateur, illustrant la façon dont les différents facteurs contribuent à la performance globale.]({% image_buster /assets/img/decisioning_studio/reporting_performance_drivertree.png %})

Pour comparer les performances de deux groupes, utilisez les menus déroulants pour sélectionner les critères de comparaison souhaités. Reportez-vous au tableau suivant pour plus de détails :

| Champ d'application | Description |
|-------|-------------|
| Groupes de comparaison | Les groupes que vous souhaitez comparer dans votre rapport. |
| Agrégation | La façon dont le rapport regroupe les données, comme les totaux, les moyennes ou les pourcentages. |
| Segmentations | Les [segments d'audience]({{site.baseurl}}/user_guide/engagement_tools/segments/) que vous avez créés dans Braze. |
| Chronologie des événements | Les événements spécifiques affichés au fil du temps, tels que les envois de messages, les ouvertures ou les conversions. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Informations

Les informations exploitables vous montrent comment sont générées les différentes options de recommandation de votre banque d'actions, comme la sélection de SL ou de blocs. Il existe deux rapports d'informations différents : **Préférences des agents** et **SHAPs**.

{% tabs local %}
{% tab agent preferences %}
Le rapport sur **les préférences des agents** vous aide à identifier les tendances saisonnières et à évaluer la pertinence des choix de la banque d'actions, ce qui vous permet de prendre des décisions éclairées pour les mises à jour.

Le rapport sur les préférences de l'agent présente un diagramme à barres comparant la fréquence de sélection des différentes options de recommandation au cours d'une période donnée. Le graphique affiche plusieurs barres colorées, chacune conseillant une option de la banque d'actions, l'axe des ordonnées représentant le pourcentage de fois où l'option a été choisie et l'axe des abscisses énumérant les noms des options.]({% image_buster /assets/img/decisioning_studio/reporting_insights_agent_preferences.png %})

Pour plus de détails sur ce rapport, reportez-vous au tableau suivant :

| Champ d'application | Description |
|-------|-------------|
| Dimension | L'attribut utilisé pour organiser les résultats, comme le canal, la campagne ou la plateforme. |
| Groupe de comparaison | Les groupes que vous souhaitez comparer dans votre rapport. Vous pouvez sélectionner plusieurs groupes de comparaison, jusqu'à NUM. |
| Paramètres | La mesure appliquée à cet attribut, comme les ouvertures, les clics ou le taux de conversion. |
| Segmentation | Le [segment d'audience]({{site.baseurl}}/user_guide/engagement_tools/segments/) que vous avez créé dans Braze. |
| Option             | L'option de recommandation spécifique sélectionnée dans la banque d'actions. |
| Description        | Une brève explication de ce que représente l'option.            |
| \# Nombre de fois choisies  | Le nombre total de fois où l'option a été sélectionnée.         |
| % du temps choisi   | Le pourcentage de sélections totales où cette option a été choisie. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab shaps %}
Le rapport **SHAPs** utilise le modèle SHapley Additive exPlanations (SHAP) pour vous aider à quantifier la contribution de chaque fonctionnalité ou variable à votre modèle de recommandation. Chaque point du graphique représente un SHAP et la distribution des points donne une idée générale de l'impact directionnel d'une fonctionnalité.

Le graphique du rapport SHAPs est un diagramme à barres horizontales avec plusieurs barres colorées représentant différentes fonctionnalités ou variables. Chaque barre montre l'impact d'une fonctionnalité sur le modèle de recommandation, l'axe des x étant étiqueté valeur SHAP et l'axe des y énumérant les noms des fonctionnalités telles que Récence, Fréquence et Canal. Le graphique visualise la contribution positive ou négative de chaque fonctionnalité aux prédictions du modèle.]({% image_buster /assets/img/decisioning_studio/reporting_insights_shaps.png %})

{% endtab %}
{% endtabs %}

### Diagnostics

Le rapport de diagnostic contient deux types de rapports différents : Les services **sortants** et les services **entrants**.

{% tabs local %}
{% tab outbound %}
Le rapport de diagnostic sortant indique le volume quotidien de recommandations générées et activées sur l'ensemble de vos audiences. Utilisez-le pour repérer les problèmes de réception/distribution, suivre les pics ou les baisses d'activation et confirmer que les messages atteignent les bons groupes comme prévu.

Rapport de diagnostic sortant montrant un graphique linéaire du volume quotidien de recommandations générées et activées pour différents groupes d'audience. Le graphique affiche deux lignes intitulées Généré et Activé, l'axe des ordonnées représentant le nombre de recommandations et l'axe des abscisses les dates. Une légende identifie chaque ligne par sa couleur. L'interface comprend des filtres déroulants pour la plage de dates et la sélection de l'audience au-dessus du graphique.]({% image_buster /assets/img/decisioning_studio/reporting_diagnostics_outbound.png %})

{% endtab %}

{% tab inbound %}

Le rapport de diagnostics entrants surveille la santé de vos flux de données dans BrazeAI™. Il suit des détails tels que le nombre de fichiers, leur taille et le volume des lignes pour chaque ressource, ce qui vous aide à confirmer que les données sont transmises comme prévu et à résoudre les problèmes avant qu'ils n'affectent vos modèles ou vos campagnes.

Vous pouvez utiliser le menu déroulant pour sélectionner différents indicateurs, tels que la taille moyenne des fichiers ou le nombre de fichiers.

Rapport de diagnostic entrant présentant un graphique linéaire sur le nombre de fichiers quotidiens et la taille moyenne des fichiers pour les ressources de données livrées à BrazeAI™. Le graphique affiche deux lignes intitulées Nombre de fichiers et Taille moyenne des fichiers en Mo, l'axe des ordonnées représentant les valeurs et l'axe des abscisses les dates. Au-dessus du graphique se trouvent des filtres déroulants pour la sélection de la plage de dates et des ressources de données.]( {% image_buster /assets/img/decisioning_studio/reporting_diagnostics_inbound.png %} )

Reportez-vous au tableau suivant pour plus d'indicateurs sur chaque paramètre du rapport de réception :

| Champ d'application | Description |
|-------|-------------|
| Ressources en données | Le nom de l'ensemble de données ou du fichier livré. |
| Date | La date à laquelle les données ont été reçues. |
| Dernier délai de réception/distribution | L'heure la plus récente à laquelle les données ont été livrées. |
| Nombre de fichiers | Le nombre total de fichiers reçus. |
| Taille maximale du fichier (Mo) | Taille du plus gros fichier reçu, en mégaoctets. |
| Taille moyenne des fichiers (Mo) | Taille moyenne de tous les fichiers reçus, en mégaoctets. |
| Nombre de lignes du fichier | Le nombre total de lignes contenues dans les fichiers livrés. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}

### Chronologie

Le rapport chronologique fournit un enregistrement visuel des événements clés ainsi que de vos indicateurs de performance. Ces événements comprennent des exécutions de modèles, des changements de configuration, des mises à jour de garde-fous, etc. Les annotations apparaissent directement sur les graphiques d'évolution et dans un onglet chronologique dédié, ce qui vous permet de connaître instantanément le contexte de l'évolution des résultats sans avoir à retracer l'historique des changements.

Rapport chronologique présentant un graphique avec les indicateurs de performance au fil du temps. Les événements clés tels que les exécutions de modèles, les changements de configuration et les mises à jour de garde-corps sont marqués par des icônes le long de la ligne de temps. Sous le graphique, un tableau répertorie les événements avec des colonnes pour la date, le type, l'étiquette, les détails et la visibilité dans les graphiques.]({% image_buster /assets/img/decisioning_studio/reporting_timeline.png %})

Pour comparer les performances de deux groupes, utilisez les menus déroulants pour sélectionner les critères de comparaison souhaités. Reportez-vous au tableau suivant pour plus de détails :

| Champ d'application | Description |
|-------|-------------|
| Date | La date à laquelle l'événement s'est produit. |
| Type | La catégorie d'événement, telle que la mise à jour du système, l'exécution du modèle ou la modification de la configuration. |
| Étiquette | Nom ou identifiant donné à l'événement. |
| Détails | Informations supplémentaires décrivant l'événement. |
| Visible dans les graphiques | Indique si l'événement est affiché dans les graphiques connexes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
