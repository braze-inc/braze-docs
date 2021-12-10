---
nav_title: Rapports de rétention
article_title: Rapports de rétention pour les campagnes et les toiles
page_order: 5
tool: Rapports
page_type: Référence
description: "Cet article de référence décrit comment mesurer la rétention des utilisateurs pour les utilisateurs qui ont effectué un événement de rétention sélectionné dans une campagne spécifique ou Canvas."
---

# Rapports de rétention pour les campagnes et toiles

> Cet article de référence décrit comment mesurer la rétention des utilisateurs pour les utilisateurs qui ont effectué un événement de rétention sélectionné dans une campagne spécifique ou Canvas. En sachant comment vos utilisateurs sont conservés après avoir envoyé un message, vous pouvez mesurer l'efficacité de vos trajets de messagerie.

La conservation des utilisateurs est l'une des mesures les plus importantes pour tout commercialiste. Maintenir le retour des utilisateurs motivés indique que les affaires sont en bonne santé. Braze vous permet de mesurer la rétention des utilisateurs directement sur la page **Analytiques** de votre campagne ou Canvas.

{% alert important %}
Les rapports de rétention ne sont pas disponibles pour les campagnes déclenchées par l'API.
{% endalert %}

## Exécuter un rapport de rétention

### Étape 1 : Sélectionnez une plage de dates

!\[Report Date\]\[8\]{: style="float:right;max-width:30%;margin-left:15px;"}

Commencez par visiter n'importe quelle campagne ou Canvas dans votre tableau de bord Braze et sélectionnez une plage de dates pour votre rapport. La sélection d'une plage de dates appropriée est cruciale en raison de la manière dont elle affecte les rapports de rétention.

Ce rapport inclura tous les utilisateurs qui sont initialement entrés dans la campagne ou Canvas pendant cette fenêtre, et de ces utilisateurs, les données de ceux qui ont effectué leur événement de rétention pendant la plage de dates apparaîtront dans le rapport.

Pour sélectionner une plage de dates, vous devez naviguer dans le coin supérieur droit de la page campagne ou Analytiques de Canvas ****. Ici, vous pouvez sélectionner différentes plages ou définir une plage personnalisée pour votre rapport.

### Étape 2 : Sélectionnez un événement de rétention

{% tabs %}
{% tab Campaign %}

Ensuite, faites défiler vers le bas jusqu'à la section **Rétention de la campagne**. La campagne de rétention vous montre le taux auquel tout utilisateur ayant reçu cette campagne spécifique a réalisé un événement de rétention (spécifié par vous sur le Rapport de rétention) au cours des 30 jours suivant la réception de la campagne.

{% endtab %}
{% tab Canvas %}

Ensuite, cliquez sur **Analyser les variantes** au bas de la page. À partir d'ici, vous pouvez analyser vos variantes, consulter votre rapport d'entonnoir et consulter votre rapport de rétention. La rétention de Canvas vous indique le taux auquel tout utilisateur ayant reçu ce Canvas a effectué un événement de rétention (précisé par vous sur le Rapport de rétention) au cours des 30 jours suivant la réception du Canevas.

{% endtab %}
{% endtabs %}

!\[Select a Retention event\]\[1\]{: style="max-width:80%"}

### Étape 3 : Générer le rapport

Une fois que vous avez sélectionné un événement de rétention, cliquez sur **Exécuter le rapport** pour démarrer la requête.

!\[Run Report\]\[2\]{: style="max-width:80%"}

Cette requête peut prendre quelques minutes, selon la quantité de données à récupérer pour générer les résultats. Si cela prend trop de temps, vous verrez une notification vous demandant de recommencer le chargement. Vous devrez peut-être attendre jusqu'à cinq minutes avant que le rapport ne soit chargé.

Une fois le rapport généré, il ne peut pas être relancé avec le même événement de rétention pendant 24 heures. Vous verrez toujours un horodatage de la date à laquelle le rapport a été généré pour la dernière fois, et une option à régénérer, s'il a été plus d'un jour. Vous pouvez toutefois modifier l'événement de rétention et refaire le rapport pour examiner l'impact de la campagne sur différents indicateurs de performance (KPI).

Le rapport ne répertorie que les jours où la campagne ou Canvas a envoyé des messages. Pour certaines campagnes et Canvases, cela peut signifier que le rapport ne montre qu'un jour s'il n'a été envoyé qu'une seule fois. S'il est récurrent ou déclenché, vous pouvez voir plusieurs jours dans le tableau.

{% tabs %}
{% tab Campaign %}

![Rapport complet]({% image_buster /assets/img/campaign_retention3.png %})

{% endtab %}
{% tab Canvas %}

![Rapport complet]({% image_buster /assets/img/canvas_retention_report.png %}){: style="largeur-max-70%"}

{% endtab %}
{% endtabs %}

## Explication du rapport

Le Rapport de rétention offre une formule de rétention et de rétention à distance. Pour voir votre campagne ou rapport Canvas avec l'un de ces types de rétention, sélectionnez soit **Rolling Retention** ou **Range Retention** pour votre **type de rétention**.

### Rouler la rétention

Rouler la rétention mesure le nombre d'utilisateurs qui reviennent et font l'événement de rétention le ou après l'un des jours énumérés en haut du rapport. Donc, si un utilisateur a commencé une session entre le 3 et le 7, l'utilisateur sera comptabilisé comme conservé sous les colonnes « 3 jours », « 1 jour » et « 0 jours ». N'importe quel utilisateur qui est retenu après la marque de 30 jours à partir de la date d'envoi de la campagne ou de Canvas sera compté sous la colonne « 30 jours » de cette ligne.

Un utilisateur qui complète l'événement plusieurs fois dans une fenêtre de plus de 30 jours sera compté dans le cadre de plusieurs intervalles de temps. Par exemple, un utilisateur qui termine une session après 1 jour sera incrémenté dans les colonnes pour >0 et >1. S'ils complètent alors l'événement après 3 jours, ils seront à nouveau incrémentés dans les colonnes précédentes (>0 et >1), qui pourraient entraîner un taux de rétention supérieur à 100 %.

#### Comment lire les rapports de fidélisation

La façon de lire le tableau des rapports de rétention pour une colonne de jour 3 serait Y% ou Y nombre d'utilisateurs (basés sur les unités choisis) a effectué l'événement 3 jours ou plus après avoir reçu la campagne le jour Z.

![Rapport de Lancement]({% image_buster /assets/img/campaign_retention3.png %})

Comme autre exemple, en se référant au tableau ci-dessus, le 25 mars, un total de 38 utilisateurs ont effectué l'événement de rétention. Le jour 0 de rétention était 68,42 %, ce qui signifie que 68. 2% des utilisateurs ont effectué l'événement de rétention de 0 ou plus (jour 0 ou plus) après avoir reçu la campagne. La rétention du jour 7 était de 57,89%, ce qui signifie que 57,89% des utilisateurs ont effectué l'événement 7 jours ou plus (au jour 7 ou plus) après avoir reçu la campagne.

Ces informations peuvent être utiles si vous voulez connaître le pourcentage d'utilisateurs qui ont et n'ont pas utilisé votre produit plus de 30 jours après la première utilisation. Une valeur de pourcentage/nombre dans le jour 30 vous indique le pourcentage d'utilisateurs qui ont retourné le jour 30 ou après.

### Intervalle de rétention

La fréquence de conservation mesure le nombre d'utilisateurs qui reviennent dans la fourchette de jours listée en haut du rapport. Donc, si un utilisateur a commencé une session entre les jours 3 et 7 puis à nouveau le jour 13, ils seraient comptabilisés dans les rangs « Jour 3-7 » et « Jour 7-14 ».

#### Comment lire les rapports de rétention des intervalles

Les rapports de gamme sont parmi les rapports les plus intuitifs à lire. Ils indiquent clairement, de tous les utilisateurs dans une cohorte, quel pourcentage de ces utilisateurs ont effectué l'événement de rétention dans une plage de dates donnée. Par exemple, dans l'image ci-dessous, référençant la Cohorte de tous les utilisateurs, sur la plage de dates "Jour 0 (0-24hrs)", 35. 1 % de la cohorte a effectué le rapport de rétention. Si un utilisateur exécute plusieurs événements de rétention dans des intervalles de dates multiples, ils seront comptabilisés comme conservés pour chaque plage.

!\[Rapport de rétention\]\[5\]

### Composants de rapport de rétention

- __Colonne Utilisateurs__: La valeur affichée est le nombre d'utilisateurs uniques qui ont effectué l'action de démarrage dans le laps de temps sélectionné ; le nombre d'utilisateurs pour le jour présent sera exclu car il est calculé.
- __Cohort Z Lignes__: Affiche les jours où la campagne ou Canvas envoyait des messages.
- __Day X Colonnes__: Jours compris entre 0 et 30 jours à différents incréments.
- __Toutes les lignes d'utilisateurs__: Aussi connu sous le nom de ligne de résumé du rapport, résume les données de rétention pour toute la période. Notez que si un utilisateur a reçu la campagne ou Canvas dans plusieurs cohortes, leurs résultats seront comptés deux fois ici.
- __Pourcentages/Nombres__: Affiche le pourcentage/nombre d'utilisateurs qui ont effectué l'événement X ou plus de jours après avoir reçu la campagne ou Canvas le jour Z. Ces pourcentages sont les pourcentages moyens pondérés. Les valeurs incomplètes seront indiquées par un astérisque.
- __Plage de dates__: Définir sur la campagne ou sur Canvas **Détails** page, la plage de dates comprend tous les utilisateurs qui ont reçu la campagne ou Canvas pendant cette fenêtre, et de ces utilisateurs, les données de ceux qui ont effectué leur événement de rétention pendant la plage de dates apparaîtront dans le rapport.
- __Unités__: Vous pouvez ajuster les unités entre le pourcentage d'utilisateurs et le nombre d'utilisateurs dans le coin supérieur droit du graphique, des unités spécifiques peuvent s'avérer plus importantes lorsque l'on évalue l'impact d'une campagne ou de Canvas.
- __Cartographie des couleurs__: Dans votre rapport de rétention, des pourcentages/nombre d'utilisateurs sont assignés des nuances plus sombres de bleu. Pourcentage/nombre plus bas d'utilisateurs sont assignés des nuances plus claires de bleu. Ceci est fait pour aider les utilisateurs à visualiser ces données.
- __Graphique du rapport de rétention__: Ce graphique résume les résultats de toutes les cohortes pour la plage de dates sélectionnée.

### Performance par variante

Afficher votre rapport de rétention par variante vous permet de comparer la rétention en cours pour chaque variante ou variation de message pour la période sélectionnée, ainsi que le groupe de contrôle. Ce rapport peut être consulté en activant **Afficher les performances de** à **par variante**.

Quelques cas d'utilisation pour afficher les performances par variante :

- Y a-t-il des variantes ou des expériences dans lesquelles les résultats semblent être un effort gaspillé ou n'ont aucune signification statistique? Jetez un autre coup d'œil et voyez si l'un ou l'autre a eu un impact plus long sur l'autre.
- Voyez à quoi ressemble la rétention si vous n'avez pas envoyé de message en fouillant dans les données de rétention du groupe de contrôle.

{% tabs %}
{% tab Campaign %}

![Voir par variante]({% image_buster /assets/img/variant_view.png %})

{% endtab %}
{% tab Canvas %}

![Voir par variante]({% image_buster /assets/img/variant_view_canvas.png %})

{% endtab %}
{% endtabs %}

#### Rapport de rétention par composants variants

- __Plage de dates__: Définir sur la campagne ou sur la toile **Détails** page, la plage de dates comprend tous les utilisateurs qui ont reçu la campagne ou Canvas pendant cette fenêtre, et de ces utilisateurs, les données de ceux qui ont effectué leur événement de rétention pendant la plage de dates apparaîtront dans le rapport. Chaque jour, le taux de rétention, le pourcentage de variation par rapport au groupe de contrôle et la confiance sont mesurés.
- __Taux de rétention__: affiche le taux de rétention par variante. Le taux de rétention est équivalent au nombre d'utilisateurs qui ont effectué l'événement de rétention divisé par le nombre total d'utilisateurs qui ont reçu la campagne ou Canvas.
- __Changement de recentage depuis le pilotage__: Quantifie le changement de pourcentage par variante du groupe de pilotage.
- __Confiance__: Braze compare le taux de conversion de chaque variante avec le taux de conversion du contrôle avec une procédure statistique appelée Z Test pour calculer un [pourcentage de confiance]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#understanding-confidence). Ce pourcentage indique à quel point cette variante fonctionne mieux que le groupe de contrôle.
- __Unités__: Vous pouvez ajuster les unités entre le pourcentage d'utilisateurs et le nombre d'utilisateurs dans le coin supérieur droit du graphique, des unités spécifiques peuvent s'avérer plus importantes lorsque l'on évalue l'impact d'une campagne ou de Canvas.
- __Graphique de variante__: Ce graphique résume les résultats par variante pour la plage de dates sélectionnée.

## Choses à rechercher dans vos rapports de rétention

Les rapports de fidélisation sont faciles à produire, mais difficiles à interpréter et à agir. Pour aider les marketeurs, nous avons rassemblé quelques sujets et questions à prendre en considération lors de l'examen de vos rapports de fidélisation.

- Considérons les tendances de la journée de la semaine pour les campagnes récurrentes (par exemple, les cohortes du lundi ont-elles un meilleur rendement que les cohortes du samedi ?).
- Où l'impact commence-t-il à baisser? Cela pourrait être un signal qu'une nouvelle campagne/Canvas qui cible les utilisateurs à ce moment-là est nécessaire pour donner un nouvel élan à la rétention.
- Voyez-vous la fatigue de la messagerie ?
- Est-ce qu'une optimisation spécifique que vous avez faite à une campagne/Canvas il y a X a eu un impact positif ?
[1]: {% image_buster /assets/img/retention_1.png %} [2]: {% image_buster /assets/img/retention_2. ng %} [5]: {% image_buster /assets/img/range_retention.png %} [8]: {% image_buster /assets/img/date_select_retention.png %}


