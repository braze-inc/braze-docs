---
nav_title: Rapports de rétention
article_title: Rapports de rétention pour les campagnes et les Canvas
page_order: 5
tool: Reports
page_type: reference
description: "Cette page explique comment mesurer la fidélisation des utilisateurs qui ont effectué un événement de fidélisation sélectionné dans une campagne ou un canvas spécifique."
---

# Rapports de rétention

> La rétention d’utilisateur est l’un des indicateurs les plus importants pour un marketeur. Gagner la confiance des utilisateurs pour les fidéliser est un indicateur de la croissance de l’entreprise. Braze vous permet de mesurer la rétention des utilisateurs directement sur la page **Analytics** de votre campagne ou Canvas.

{% alert important %}
Les rapports de rétention ne sont pas disponibles pour les campagnes déclenchées via API.
{% endalert %}

## Exécuter un rapport de rétention

### Étape 1 : Sélectionner une plage de dates

![Date du rapport]({% image_buster /assets/img/date_select_retention.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Commencez par aller sur une campagne ou un Canvas dans votre tableau de bord de Braze, et sélectionnez une plage de dates pour votre rapport. La sélection d’une plage de dates appropriée est cruciale, elle affecte les rapports de rétention. 

Ce rapport inclura tous les utilisateurs qui sont initialement entrés dans la campagne ou le Canvas pendant cette fenêtre. Parmi ces utilisateurs, ceux qui ont effectué leur événement de rétention pendant la période auront leurs données dans le rapport.

Pour sélectionner une plage de dates, naviguez jusqu'à la page de la campagne ou de Canvas **Analytics** et sélectionnez diverses plages ou définissez une plage personnalisée pour votre rapport.

### Étape 2 : Sélectionner un événement de rétention

{% tabs %}
{% tab Campagne %}

Ensuite, allez dans la section **Rétention de la campagne.**  La rétention de la campagne vous indique le taux auquel tout utilisateur ayant reçu cette campagne spécifique a effectué un événement de rétention (spécifié par vous dans le rapport de rétention) au cours des 30 jours à partir du moment où il a reçu la campagne.

{% endtab %}
{% tab Canvas %}

Ensuite, sélectionnez **Analyser les variantes**. À partir de là, vous pouvez analyser vos variantes, consulter votre rapport d’entonnoir et afficher votre rapport de rétention. La rétention des canevas vous indique le taux de rétention (spécifié par vous dans le rapport de rétention) de tout utilisateur ayant reçu ce canevas spécifique au cours des 30 jours qui ont suivi la réception du canevas.

{% endtab %}
{% endtabs %}

![Sélectionnez un événement de rétention]({% image_buster /assets/img/retention_1.png %}){: style="max-width:80%"}

### Étape 3 : Générer le rapport

Après avoir sélectionné un événement de rétention, sélectionnez **Exécuter le rapport** pour lancer la requête.

![Exécuter le/un rapport]({% image_buster /assets/img/retention_2.png %}){: style="max-width:80%"}

Cette requête peut prendre quelques minutes pour exécuter, selon la quantité de données à récupérer pour générer les résultats. Si elle met trop de temps, vous verrez une notification vous demandant de réessayer de charger le rapport. Vous devrez peut-être attendre cinq minutes avant que le rapport ne soit chargé.

Une fois le rapport généré, il ne peut pas être exécuté à nouveau avec le même événement de rétention pendant 24 heures. Vous verrez toujours un horodatage du moment où le rapport a été généré pour la dernière fois, et une option pour le régénérer, si cela remonte à plus d’une journée. Vous pouvez toutefois modifier l’événement de rétention et relancer le rapport pour examiner l’impact de la campagne sur différents KPI.

Le rapport montre uniquement les jours où la campagne ou Canvas envoyait des messages. Pour certaines campagnes et Canvas, le rapport n’affichera donc qu’un seul jour si elles n’ont été envoyées qu’une seule fois. Si elles sont récurrentes ou déclenchées, vous pouvez voir plusieurs jours dans le tableau.

{% tabs %}
{% tab Campagne %}

![Rapport complet]({% image_buster /assets/img/campaign_retention3.png %})

{% endtab %}
{% tab Canvas %}

![Rapport complet]({% image_buster /assets/img/canvas_retention_report.png %}){: style="max-width:70%"}

{% endtab %}
{% endtabs %}

## Explication du rapport

Le rapport de rétention propose une formule de rétention glissante et une formule de rétention par plage. Pour afficher votre campagne ou votre rapport Canvas avec l'un de ces types de rétention, sélectionnez **Rétention glissante** ou **Rétention par plage** pour votre **Type de rétention**.

### Rétention glissante

La rétention glissante x mesure le nombre d’utilisateurs qui reviennent et font l’événement de rétention le ou les jours (ou après) indiqués en haut du rapport. Ainsi, si un utilisateur a commencé une session entre le troisième et le septième jour, il sera comptabilisé comme retenu dans les colonnes "3 jours", "1 jour" et "0 jour". Tout utilisateur qui est compté comme conservé au bout de 30 jours à partir de la date de l’envoi de la campagne ou du Canvas sera comptabilisé sous la colonne « 30 jours » de cette ligne.

Un utilisateur qui effectue l’événement plusieurs fois pendant une fenêtre de plus de 30 jours sera comptabilisé dans plusieurs plages de dates. Par exemple, un utilisateur qui termine une session après un jour sera incrémenté dans les colonnes >0 et >1. S'ils terminent ensuite l'événement après trois jours, ils seront à nouveau incrémentés dans les colonnes précédentes (>0 et >1), ce qui pourrait faire en sorte que le taux de rétention dépasse 100 %.

#### Comment lire les rapports de rétention

La lecture du tableau du rapport de rétention pour une colonne de trois jours serait la suivante : Y% ou Y nombre d'utilisateurs (sur la base des unités choisies) ont réalisé l'événement trois jours ou plus après avoir reçu la campagne le jour Z.

![Rapport glissant]({% image_buster /assets/img/campaign_retention3.png %})

Par exemple, en se référant au tableau de l’image précédente, le 25 mars, un total de 38 utilisateurs a effectué l’événement de rétention. La rétention au jour zéro était de 68,42 %, ce qui signifie que 68,42 % des utilisateurs ont effectué l'événement de rétention zéro jour ou plus (au jour zéro ou plus tard) après avoir reçu la campagne. Le taux de rétention au septième jour était de 57,89 %, ce qui signifie que 57,89 % des utilisateurs ont réalisé l'événement sept jours ou plus (au septième jour ou plus tard) après avoir reçu la campagne.

Ces informations peuvent être utiles si vous souhaitez connaître le pourcentage d’utilisateurs qui ont et n’ont pas utilisé votre produit 30 jours ou plus après la première utilisation. Un pourcentage ou un nombre dans la colonne du jour 30 vous indique le pourcentage d'utilisateurs qui sont revenus le jour 30 ou après.

### Rétention par plage

La rétention par plage mesure le nombre d’utilisateurs qui reviennent pendant la période figurant dans la partie supérieure du rapport. Ainsi, si un utilisateur a commencé une session entre le troisième et le septième jour, puis à nouveau le treizième jour, il sera compté comme retenu à la fois dans les plages "3-7 jours" et "7-14 jours".

#### Comment lire les rapports de rétention par plage

Les rapports par plage sont certains des rapports les plus intuitifs à lire. Ils indiquent clairement, parmi tous les utilisateurs d’une cohorte, le pourcentage de ceux qui ont eu l’événement de rétention dans une plage de dates donnée. Par exemple, dans l’image suivante, pour la cohorte Tous les utilisateurs et la période « Jour 0 (0-24 h) », 35,71 % de la cohorte a eu le rapport de rétention. Si un utilisateur effectue plusieurs événements de rétention dans plusieurs plages de dates, il sera comptabilisé comme conservé pour chaque plage.

![Rapport de rétention]({% image_buster /assets/img/range_retention.png %})

### Composants du rapport de rétention

- **Colonne des utilisateurs**: La valeur affichée est le nombre d’utilisateurs uniques qui ont effectué l’action de début dans le délai sélectionné ; le nombre d’utilisateurs pour le jour actuel sera exclu puisqu’il est en cours de calcul. 
- **Lignes de la cohorte Z** : Affiche les jours où la campagne ou Canvas envoyait des messages.
- **Jour X Colonnes**: Jours compris entre 0 et 30 jours à divers incréments.
- **Ligne « Tous les utilisateurs »** : Également appelée Ligne récapitulative du rapport, elle résume les données de rétention sur toute la période. Notez que si un utilisateur a reçu la campagne ou le Canvas dans plusieurs cohortes, ses résultats seront comptabilisés deux fois ici. 
- **Pourcentages/Nombres**: Indique le pourcentage ou le nombre d'utilisateurs qui ont réalisé l'événement X jours ou plus après avoir reçu la campagne ou le Canvas le jour Z. Ces pourcentages sont les pourcentages moyens pondérés. Les valeurs incomplètes seront indiquées par un astérisque.
- **Plage de dates** : Définie sur la page **Détails de la** campagne ou du Canvas, la plage de dates inclut tous les utilisateurs qui ont reçu la campagne ou le Canvas pendant cette fenêtre, et parmi ces utilisateurs, les données de ceux qui ont effectué leur événement de rétention pendant la plage de dates apparaîtront dans le rapport.
- **Unités**: Vous pouvez ajuster les unités pour le pourcentage d’utilisateurs et le nombre d’utilisateurs dans le coin supérieur droit du graphique, des unités spécifiques peuvent s’avérer plus significatives pour juger l’impact d’une campagne ou d’un Canvas.
- **Mappage des couleurs**: Dans votre rapport de rétention, les pourcentages ou le nombre d'utilisateurs les plus élevés sont en bleu plus foncé. Les pourcentages ou le nombre d'utilisateurs les plus faibles sont représentés par des tons de bleu plus clairs. C’est pour aider les utilisateurs à visualiser ces données.
- **Graphique du rapport de rétention**: Ce graphique récapitule les résultats pour toutes les cohortes pour la plage de dates sélectionnée.

### Performance par variante

L'affichage de votre rapport de rétention par variante vous permet de comparer la rétention glissante pour chaque variante ou variation de message pour la période sélectionnée, ainsi que pour le groupe de contrôle. Ce rapport peut être consulté en basculant l'option **Afficher les performances pour** sur **Par variante**.

Certains cas d’utilisation pour montrer les performances par variante :

- Vous avez des variantes ou des expériences dont les résultats semblent indiquer un effort inutile, ou n’ont pas de signification statistique ? Jetez-y un autre coup d’œil pour voir si une d’entre elles a eu un impact plus durable dans le temps.
- En explorant les données de rétention du groupe de contrôle, vous pouvez voir à quoi ressemblerait la rétention si vous n’envoyiez pas de message.

{% tabs %}
{% tab Campagne %}

![Vue par variante]({% image_buster /assets/img/variant_view.png %})

{% endtab %}
{% tab Canvas %}

![Vue par variante]({% image_buster /assets/img/variant_view_canvas.png %})

{% endtab %}
{% endtabs %}

#### Rapport de rétention par composants de variante

- **Plage de dates** : Définie sur la page **Détails de la** campagne ou du canevas, la plage de dates inclut tous les utilisateurs qui ont reçu la campagne ou le canevas pendant cette fenêtre, et parmi ces utilisateurs, les données de ceux qui ont effectué leur événement de rétention pendant la plage de dates apparaîtront dans le rapport. Le taux de rétention, le pourcentage d’écart par rapport au groupe de contrôle et la confiance sont mesurés chaque jour.
- **Taux de rétention**: Affiche le taux de rétention par variante. Le taux de rétention est équivalent au nombre d’utilisateurs ayant effectué l’événement de rétention divisé par le total des utilisateurs ayant reçu la campagne ou le Canvas.
- **Pourcentage de changement par rapport au contrôle**: Quantifie le pourcentage d’écart par variante par rapport au groupe de contrôle.
- **Confiance**: {% multi_lang_include metrics.md metric='Confidence' %} Braze compare le taux de conversion de chaque variante par rapport au taux de conversion du contrôle à l'aide d'une procédure statistique appelée test Z afin de calculer un pourcentage de [confiance]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#understanding-confidence).
- **Unités**: Vous pouvez ajuster les unités pour le pourcentage d’utilisateurs et le nombre d’utilisateurs dans le coin supérieur droit du graphique, des unités spécifiques peuvent s’avérer plus significatives pour juger l’impact d’une campagne ou d’un Canvas.
- **Graphique de variante** : Ce graphique résume les résultats par variante pour la plage de dates sélectionnée.

## Choses à rechercher dans vos rapports de rétention

Les rapports de rétention sont faciles à générer, mais difficiles à interpréter pour agir en conséquence. Pour aider les spécialistes du marketing, nous avons rassemblé quelques sujets et questions à prendre en compte lorsque vous vous penchez sur vos rapports de rétention.

- Tenez compte des tendances liées au jour de la semaine pour les campagnes récurrentes (par exemple, les cohortes du lundi obtiennent-elles de meilleurs résultats que celles du samedi ?)
- Où l’impact commence-t-il à décliner ? Cela peut être le signe qu'une nouvelle campagne ou un nouveau canvas ciblant les utilisateurs à ce moment-là est nécessaire pour stimuler la fidélisation. 
- Constatez-vous une lassitude par rapport aux messages ?
- Une optimisation spécifique que vous avez apportée à une campagne ou à un canvas il y a X jours a-t-elle eu un impact positif ?



