---
nav_title: Rapports de conservation
article_title: Rapports de rétention pour les campagnes et les toiles
page_order: 5
tool: Reports
page_type: reference
description: "Cette page explique comment mesurer la fidélisation des utilisateurs qui ont effectué un événement de fidélisation sélectionné dans une campagne ou un canvas spécifique."
---

# Rapports de conservation

> La fidélisation des utilisateurs est l'un des indicateurs les plus importants pour tout marketeur. Le fait que les utilisateurs engagés reviennent pour en savoir plus indique que l'entreprise est en bonne santé. Braze vous permet de mesurer la rétention des utilisateurs directement sur la page **Analytics** de votre campagne ou Canvas.

{% alert important %}
Les rapports de rétention ne sont pas disponibles pour les campagnes déclenchées par l'API.
{% endalert %}

## Exécuter un rapport de rétention

### Étape 1 : Sélectionnez une plage de dates

\![Date du rapport]({% image_buster /assets/img/date_select_retention.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Commencez par visiter n'importe quelle campagne ou Canvas dans votre tableau de bord de Braze, et sélectionnez une plage de dates pour votre rapport. La sélection d'une plage de dates appropriée est cruciale en raison de la manière dont elle affecte les rapports de conservation. 

Ce rapport inclura tous les utilisateurs qui sont entrés initialement dans la campagne ou le Canvas pendant cette fenêtre, et parmi ces utilisateurs, les données de ceux qui ont effectué leur événement de rétention pendant la plage de dates apparaîtront dans le rapport.

Pour sélectionner une plage de dates, naviguez jusqu'à la page de la campagne ou de Canvas **Analytics** et sélectionnez diverses plages ou définissez une plage personnalisée pour votre rapport.

### Étape 2 : Sélectionnez un événement de rétention

{% tabs %}
{% tab Campaign %}

Ensuite, allez dans la section **Rétention de la campagne.**  La rétention de la campagne vous indique le taux auquel tout utilisateur ayant reçu cette campagne spécifique a effectué un événement de rétention (spécifié par vous dans le rapport de rétention) au cours des 30 jours à partir du moment où il a reçu la campagne.

{% endtab %}
{% tab Canvas %}

Ensuite, sélectionnez **Analyser les variantes**. À partir de là, vous pouvez analyser vos variantes, consulter votre rapport d'entonnoir et votre rapport de rétention. La rétention des canevas vous indique le taux de rétention (spécifié par vous dans le rapport de rétention) de tout utilisateur ayant reçu ce canevas spécifique au cours des 30 jours qui ont suivi la réception du canevas.

{% endtab %}
{% endtabs %}

Sélectionnez un événement de rétention]({% image_buster /assets/img/retention_1.png %}){: style="max-width:80%"}

### Étape 3 : Générer le rapport

Après avoir sélectionné un événement de rétention, sélectionnez **Exécuter le rapport** pour lancer la requête.

!Exécuter/un rapport]({% image_buster /assets/img/retention_2.png %}){: style="max-width:80%"}

L'exécution de cette requête peut prendre quelques minutes, en fonction de la quantité de données à extraire pour générer les résultats. Si cela prend trop de temps, vous verrez une notification vous demandant de réessayer de charger le rapport. Il se peut que vous deviez attendre jusqu'à cinq minutes avant que le rapport ne soit chargé.

Une fois le rapport généré, il ne peut pas être exécuté à nouveau avec le même événement de rétention pendant 24 heures. Vous verrez toujours un horodatage de la date à laquelle le rapport a été généré pour la dernière fois, ainsi qu'une option de régénération, si cela fait plus d'un jour. Vous pouvez toutefois modifier l'événement de rétention et exécuter à nouveau le rapport pour examiner l'impact de la campagne sur différents ICP.

Le rapport ne répertorie que les jours au cours desquels la campagne ou le Canvas a envoyé des messages. Pour certaines campagnes et canevas, cela peut signifier que le rapport ne s'affiche qu'un jour s'il n'a été envoyé qu'une seule fois. S'il est récurrent ou déclenché, vous pouvez voir plusieurs jours dans le tableau.

{% tabs %}
{% tab Campaign %}

[Rapport complet]({% image_buster /assets/img/campaign_retention3.png %})

{% endtab %}
{% tab Canvas %}

[Rapport complet]({% image_buster /assets/img/canvas_retention_report.png %}){: style="max-width:70%"}

{% endtab %}
{% endtabs %}

## Explication du rapport

L'état de rétention propose une formule de rétention glissante et une formule de rétention par plage. Pour afficher votre campagne ou votre rapport Canvas avec l'un de ces types de rétention, sélectionnez **Rétention glissante** ou **Rétention par plage** pour votre **Type de rétention**.

### Rétention des rouleaux

La rétention mobile mesure le nombre d'utilisateurs qui reviennent et effectuent l'événement de rétention pendant ou après l'un des jours énumérés en haut du rapport. Ainsi, si un utilisateur a commencé une session entre le troisième et le septième jour, il sera comptabilisé comme retenu dans les colonnes "3 jours", "1 jour" et "0 jour". Tout utilisateur qui est compté comme retenu après la période de 30 jours suivant l'envoi de la campagne ou du canvas sera comptabilisé dans la colonne "30 jours" de cette ligne.

Un utilisateur qui accomplit l'événement plusieurs fois au cours d'une fenêtre de plus de 30 jours sera comptabilisé comme faisant partie de plusieurs périodes. Par exemple, un utilisateur qui termine une session après un jour sera incrémenté dans les colonnes >0 et >1. S'ils terminent ensuite l'événement après trois jours, ils seront à nouveau incrémentés dans les colonnes précédentes (>0 et >1), ce qui pourrait faire en sorte que le taux de rétention dépasse 100 %.

#### Comment lire les rapports de rétention glissants

La lecture du tableau du rapport de rétention pour une colonne de trois jours serait la suivante : Y% ou Y nombre d'utilisateurs (sur la base des unités choisies) ont réalisé l'événement trois jours ou plus après avoir reçu la campagne le jour Z.

\![Rolling Report]({% image_buster /assets/img/campaign_retention3.png %})

Autre exemple, si l'on se réfère au tableau de l'image précédente, le 25 mars, un total de 38 utilisateurs ont effectué l'événement de rétention. La rétention au jour zéro était de 68,42 %, ce qui signifie que 68,42 % des utilisateurs ont effectué l'événement de rétention zéro jour ou plus (au jour zéro ou plus tard) après avoir reçu la campagne. Le taux de rétention au septième jour était de 57,89 %, ce qui signifie que 57,89 % des utilisateurs ont réalisé l'événement sept jours ou plus (au septième jour ou plus tard) après avoir reçu la campagne.

Cette information peut être utile si vous souhaitez connaître le pourcentage d'utilisateurs qui ont ou n'ont pas utilisé votre produit 30 jours ou plus après la première utilisation. Un pourcentage ou un nombre dans la colonne du jour 30 vous indique le pourcentage d'utilisateurs qui sont revenus le jour 30 ou après.

### Maintien de la portée

La rétention des plages mesure le nombre d'utilisateurs qui reviennent dans la plage de jours indiquée en haut du rapport. Ainsi, si un utilisateur a commencé une session entre le troisième et le septième jour, puis à nouveau le treizième jour, il sera comptabilisé comme ayant été retenu à la fois dans les plages "3-7 jours" et "7-14 jours".

#### Comment lire les rapports de rétention des champs de tir

Les rapports de gamme sont parmi les rapports les plus intuitifs à lire. Ils indiquent clairement, parmi tous les utilisateurs d'une cohorte, le pourcentage de ceux qui ont effectué l'événement de rétention dans une plage de dates donnée. Par exemple, dans l'image suivante, se référant à la cohorte Tous les utilisateurs, sur la plage de dates "Jour 0 (0-24h)", 35,71% de la cohorte a effectué le rapport de rétention. Si un utilisateur effectue plusieurs événements de rétention dans plusieurs plages de dates, il sera compté comme retenu pour chaque plage.

\![Rapport de rétention]({% image_buster /assets/img/range_retention.png %})

### Composants du rapport de rétention

- **Colonne des utilisateurs**: La valeur indiquée correspond au nombre d'utilisateurs uniques ayant effectué l'action de démarrage au cours de la période sélectionnée ; le nombre d'utilisateurs pour la journée en cours sera exclu puisqu'il est en cours de calcul. 
- **Cohorte Z Rangs**: Affiche les jours au cours desquels la campagne ou le Canvas a envoyé des messages.
- **Jour X Colonnes**: Jours compris entre 0 et 30 jours, avec des incréments différents.
- **Tous les utilisateurs Rangée**: Également appelée ligne de résumé du rapport, elle résume les données de conservation pour l'ensemble de la période. Notez que si un utilisateur a reçu la campagne ou le Canvas dans plusieurs cohortes, ses résultats seront comptés deux fois ici. 
- **Pourcentages/Nombres**: Indique le pourcentage ou le nombre d'utilisateurs qui ont réalisé l'événement X jours ou plus après avoir reçu la campagne ou le Canvas le jour Z. Ces pourcentages sont les pourcentages moyens pondérés. Les valeurs incomplètes sont signalées par un astérisque.
- **Date d'entrée en vigueur**: Définie sur la page **Détails de la** campagne ou du Canvas, la plage de dates inclut tous les utilisateurs qui ont reçu la campagne ou le Canvas pendant cette fenêtre, et parmi ces utilisateurs, les données de ceux qui ont effectué leur événement de rétention pendant la plage de dates apparaîtront dans le rapport.
- **Unités**: Vous pouvez ajuster les unités entre le pourcentage d'utilisateurs et le nombre d'utilisateurs dans le coin supérieur droit du graphique, des unités spécifiques pouvant s'avérer plus significatives pour juger de l'impact d'une campagne ou d'un Canvas.
- **Mappage des couleurs**: Dans votre rapport sur la rétention, les pourcentages ou le nombre d'utilisateurs les plus élevés sont en bleu plus foncé. Les pourcentages ou le nombre d'utilisateurs les plus faibles sont indiqués en bleu plus clair. Ceci afin d'aider les utilisateurs à visualiser ces données.
- **Graphique du rapport de rétention**: Ce graphique résume les résultats de toutes les cohortes pour la plage de dates sélectionnée.

### Performances par variante

L'affichage de votre rapport de rétention par variante vous permet de comparer la rétention glissante pour chaque variante ou variation de message pour la période sélectionnée, ainsi que pour le groupe de contrôle. Ce rapport peut être consulté en basculant l'option **Afficher les performances pour** sur **Par variante**.

Quelques cas d'utilisation pour montrer la performance par variante :

- Avez-vous des variantes ou des expériences dont les résultats semblent être une perte de temps ou n'ont pas de signification statistique ? Regardez à nouveau et voyez si l'un ou l'autre a eu un impact sur la queue plus longue.
- Voyez ce qu'il en est de la fidélisation si vous n'avez pas envoyé de message en consultant les données de fidélisation du groupe de contrôle.

{% tabs %}
{% tab Campaign %}

!Vue par variante]({% image_buster /assets/img/variant_view.png %})

{% endtab %}
{% tab Canvas %}

!Vue par variante]({% image_buster /assets/img/variant_view_canvas.png %})

{% endtab %}
{% endtabs %}

#### Rapport de rétention par composantes variantes

- **Date d'entrée en vigueur**: Définie sur la page **Détails de la** campagne ou du canevas, la plage de dates inclut tous les utilisateurs qui ont reçu la campagne ou le canevas pendant cette fenêtre, et parmi ces utilisateurs, les données de ceux qui ont effectué leur événement de rétention pendant la plage de dates apparaîtront dans le rapport. Chaque jour, le taux de rétention, le pourcentage de changement par rapport au groupe de contrôle et la confiance sont mesurés.
- **Taux de rétention**: Indique le taux de rétention par variante. Le taux de rétention équivaut au nombre d'utilisateurs ayant effectué l'événement de rétention divisé par le nombre total d'utilisateurs ayant reçu la campagne ou le Canvas.
- **Pourcentage de changement par rapport au contrôle**: Quantifie le pourcentage de changement par variante par rapport au groupe de contrôle.
- **Confiance**: {% multi_lang_include analytics/metrics.md metric='Confidence' %} Braze compare le taux de conversion de chaque variante au taux de conversion du témoin à l'aide d'une procédure statistique appelée test Z afin de calculer un pourcentage de [confiance]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#understanding-confidence).
- **Unités**: Vous pouvez ajuster les unités entre le pourcentage d'utilisateurs et le nombre d'utilisateurs dans le coin supérieur droit du graphique, des unités spécifiques pouvant s'avérer plus significatives pour juger de l'impact d'une campagne ou d'un Canvas.
- **Graphique variante**: Ce graphique résume les résultats par variante pour la plage de dates sélectionnée.

## Ce qu'il faut rechercher dans vos rapports de rétention

Les rapports de rétention sont faciles à produire, mais difficiles à interpréter et à exploiter. Pour aider les marketeurs, nous avons rassemblé quelques sujets et questions à prendre en compte lors de l'examen de vos rapports de rétention.

- Tenez compte des tendances liées au jour de la semaine pour les campagnes récurrentes (par exemple, les cohortes du lundi obtiennent-elles de meilleurs résultats que celles du samedi ?)
- Où l'impact commence-t-il à diminuer ? Cela peut être le signe qu'une nouvelle campagne ou un nouveau canvas ciblant les utilisateurs à ce moment-là est nécessaire pour stimuler la fidélisation. 
- Constatez-vous une lassitude à l'égard de l'envoi des messages ?
- Une optimisation spécifique que vous avez apportée à une campagne ou à un canvas il y a X jours a-t-elle eu un impact positif ?



