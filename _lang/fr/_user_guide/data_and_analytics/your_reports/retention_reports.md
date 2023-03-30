---
nav_title: Rapports de rétention
article_title: Rapports de rétention pour les campagnes et les Canvas
page_order: 5
tool: Reports
page_type: reference
description: "Cet article de référence explique comment mesurer la rétention des utilisateurs pour les utilisateurs qui ont effectué un événement de rétention donné dans une campagne ou un Canvas spécifique."
---

# Rapports de rétention pour les campagnes et les Canvas

> Cet article de référence explique comment mesurer la rétention des utilisateurs pour les utilisateurs ayant effectué un événement de rétention donné dans une campagne ou un Canvas spécifique. En sachant comment vos utilisateurs sont intéressés après avoir reçu un message, vous pouvez mesurer l’efficacité de vos parcours de communication.

La rétention d’utilisateur est l’un des indicateurs les plus importants pour un marketeur. Gagner la confiance des utilisateurs pour les fidéliser est un indicateur de la croissance de l’entreprise. Braze vous permet désormais de mesurer la rétention client directement sur la page **Analytics** de votre campagne ou votre Canvas.

{% alert important %}
Les rapports de rétention ne sont pas disponibles pour les campagnes déclenchées via API.
{% endalert %}

## Exécuter un rapport de rétention

### Étape 1 : Sélectionner une plage de dates

![Date du rapport][8]{: style="float:right;max-width:30%;margin-left:15px;"}

Commencez par aller sur une campagne ou un Canvas dans votre tableau de bord de Braze, et sélectionnez une plage de dates pour votre rapport. La sélection d’une plage de dates appropriée est cruciale, elle affecte les rapports de rétention. 

Ce rapport inclura tous les utilisateurs qui sont initialement entrés dans la campagne ou le Canvas pendant cette fenêtre. Parmi ces utilisateurs, ceux qui ont effectué leur événement de rétention pendant la période auront leurs données dans le rapport.

Pour sélectionner une plage de dates, vous devez naviguer dans le coin supérieur droit de la page **Analytics (Analyse analytique)** de la campagne ou du Canvas. Vous pouvez sélectionner plusieurs plages ou définir une plage personnalisée pour votre rapport.

### Étape 2 : Sélectionner un événement de rétention

{% tabs %}
{% tab Campaign %}

Ensuite, faites défiler jusqu’à la section **Campaign Retention (Rétention de la campagne)**. La rétention de campagne vous indique le pourcentage d’utilisateurs ayant reçu cette campagne spécifique qui ont eu un événement de rétention (spécifié par vous sur le rapport de rétention) dans les 30 jours suivant la réception de la campagne.

{% endtab %}
{% tab Canvas %}

Ensuite, cliquez sur **Analyze Variants (Analyser les variantes)** au bas de la page. À partir de là, vous pouvez analyser vos variantes, consulter votre rapport d’entonnoir et afficher votre rapport de rétention. La rétention Canvas vous indique le taux auquel un utilisateur ayant reçu ce Canvas spécifique a effectué un événement de rétention donné (tel que spécifié par vous dans le Rapport de Rétention) au cours des 30 jours suivant la réception du Canvas.

{% endtab %}
{% endtabs %}

![Sélectionner un événement de rétention][1]{: style="max-width:80%"}

### Étape 3 : Générer le rapport

Une fois que vous avez sélectionné un événement de rétention, cliquez sur **Run Report** pour démarrer la requête.

![Run Report][2]{: style="max-width:80%"}

Cette requête peut prendre quelques minutes pour exécuter, selon la quantité de données à récupérer pour générer les résultats. Si elle met trop de temps, vous verrez une notification vous demandant de réessayer de charger le rapport. Vous devrez peut-être attendre cinq minutes avant que le rapport ne soit chargé.

Une fois le rapport généré, il ne peut pas être réexécuté pour le même événement de rétention pendant 24 heures. Vous verrez toujours un horodatage du moment où le rapport a été généré pour la dernière fois, et une option pour le régénérer, si cela remonte à plus d’une journée. Vous pouvez toutefois modifier l’événement de rétention et relancer le rapport pour examiner l’impact de la campagne sur différents KPI.

Le rapport montre uniquement les jours où la campagne ou Canvas envoyait des messages. Pour certaines campagnes et Canvas, le rapport n’affichera donc qu’un seul jour si elles n’ont été envoyées qu’une seule fois. Si elles sont récurrentes ou déclenchées, vous pouvez voir plusieurs jours dans le tableau.

{% tabs %}
{% tab Campaign %}

![Rapport complet]({% image_buster /assets/img/campaign_retention3.png %})

{% endtab %}
{% tab Canvas %}

![Rapport complet]({% image_buster /assets/img/canvas_retention_report.png %}){: style="max-width:70%"}

{% endtab %}
{% endtabs %}

## Explication du rapport

Le rapport de rétention a une formule qui permet de calculer à la fois la rétention glissante et la rétention par plage. Pour afficher votre campagne ou votre rapport Canvas avec l’un de ces types de rétention, sélectionnez **Rolling Retention (Rétention glissante)** ou **Range Retention (Rétention par plage)** dans le champ **Type of Retention (Type de rétention)**.

### Rétention glissante

La rétention glissante x mesure le nombre d’utilisateurs qui reviennent et font l’événement de rétention le ou les jours (ou après) indiqués en haut du rapport. Ainsi, si un utilisateur a commencé une session entre le jour 3 et le jour 7, l’utilisateur sera comptabilisé comme conservé dans les colonnes « 3 jours », « 1 jour » et « 0 jours ». Tout utilisateur qui est compté comme conservé au bout de 30 jours à partir de la date de l’envoi de la campagne ou du Canvas sera comptabilisé sous la colonne « 30 jours » de cette ligne.

Un utilisateur qui effectue l’événement plusieurs fois pendant une fenêtre de plus de 30 jours sera comptabilisé dans plusieurs plages de dates. Par exemple, un utilisateur qui termine une session après 1 jour sera incrémenté dans les colonnes pour >0 et >1. S’ils complètent ensuite l’événement après 3 jours, ils seront de nouveau incrémentés dans les colonnes précédentes (> 0 et >1), ce qui pourrait donner un taux de rétention supérieur à 100 %.

#### Comment lire les rapports de rétention

La façon de lire le tableau de rapport de rétention pour une colonne du jour 3 serait : Y % ou Y utilisateurs (en fonction des unités choisies) ont effectué l’événement 3 jours ou plus après avoir reçu la campagne le jour Z.

![Rapport glissant]({% image_buster /assets/img/campaign_retention3.png %})

Par exemple, en se référant au tableau de l’image précédente, le 25 mars, un total de 38 utilisateurs a effectué l’événement de rétention. La rétention du Jour 0 était de 68,42 %, ce qui signifie que 68,42 % des utilisateurs ont effectué l’événement de rétention 0 jour ou plus (le Jour 0 ou plus tard) après avoir reçu la campagne. La rétention du Jour 7 était de 57,89 %, ce qui signifie que 57,89 % des utilisateurs ont effectué l’événement 7 jours ou plus (le Jour 7 ou plus tard) après avoir reçu la campagne.

Ces informations peuvent être utiles si vous souhaitez connaître le pourcentage d’utilisateurs qui ont et n’ont pas utilisé votre produit 30 jours ou plus après la première utilisation. Une valeur de pourcentage/nombre dans la colonne du jour 30 vous indique le pourcentage d’utilisateurs qui sont revenus le jour 30 ou après.

### Rétention par plage

La rétention par plage mesure le nombre d’utilisateurs qui reviennent pendant la période figurant dans la partie supérieure du rapport. Ainsi, si un utilisateur a commencé une session entre les jours 3 et 7, puis de nouveau le jour 13, il sera comptabilisé comme conservé dans les deux plages « Jours 3-7 » et « Jours 7-14 ».

#### Comment lire les rapports de rétention par plage

Les rapports par plage sont certains des rapports les plus intuitifs à lire. Ils indiquent clairement, parmi tous les utilisateurs d’une cohorte, le pourcentage de ceux qui ont eu l’événement de rétention dans une plage de dates donnée. Par exemple, dans l’image suivante, pour la cohorte Tous les utilisateurs et la période « Jour 0 (0-24 h) », 35,71 % de la cohorte a eu le rapport de rétention. Si un utilisateur effectue plusieurs événements de rétention dans plusieurs plages de dates, il sera comptabilisé comme conservé pour chaque plage.

![Rapport de rétention][5]

### Composants du rapport de rétention

- **Users Column (Colonne Utilisateurs)**: La valeur affichée est le nombre d’utilisateurs uniques qui ont effectué l’action de début dans le délai sélectionné ; le nombre d’utilisateurs pour le jour actuel sera exclu puisqu’il est en cours de calcul. 
- **Cohort Z Rows (Lignes de la cohorte Z)**: Affiche les jours où la campagne ou Canvas envoyait des messages.
- **Day X Columns (Colonnes du Jour X)**: Jours compris entre 0 et 30 jours à divers incréments.
- **All Users Row (Ligne « Tous les utilisateurs »)**: Également appelée Ligne récapitulative du rapport, elle résume les données de rétention sur toute la période. Notez que si un utilisateur a reçu la campagne ou le Canvas dans plusieurs cohortes, ses résultats seront comptabilisés deux fois ici. 
- **Percentages/Numbers (Pourcentages/nombres)** : Affiche le pourcentage/nombre d’utilisateurs qui ont effectué l’événement X jours ou plus après avoir reçu la campagne ou le Canvas. Ces pourcentages sont les pourcentages moyens pondérés. Les valeurs incomplètes seront indiquées par un astérisque.
- **Date Range (Plage de dates)** : Définie sur la page **Détails** de la campagne ou du Canvas, la plage de dates inclut tous les utilisateurs ayant reçu la campagne ou le Canvas pendant cette fenêtre. Parmi ces utilisateurs, ceux qui ont effectué leur événement de rétention pendant la période auront leurs données dans le rapport.
- **Units (Unités)** : Vous pouvez ajuster les unités pour le pourcentage d’utilisateurs et le nombre d’utilisateurs dans le coin supérieur droit du graphique, des unités spécifiques peuvent s’avérer plus significatives pour juger l’impact d’une campagne ou d’un Canvas.
- **Color Mapping (Mappage couleurs)** : Dans votre rapport de rétention, les pourcentages/nombre d’utilisateurs élevés sont affichés avec des nuances de bleu plus foncées. Le pourcentage/nombre d’utilisateurs moins élevé est affiché avec des nuances de bleu plus claires. C’est pour aider les utilisateurs à visualiser ces données.
- **Retention Report Graph (Graphique du rapport de rétention)** : Ce graphique récapitule les résultats pour toutes les cohortes pour la plage de dates sélectionnée.

### Performance par variante

La visualisation de votre rapport de rétention par variante vous permet de comparer la rétention glissante pour chaque variante ou variation de message pour la période sélectionnée, ainsi par rapport au groupe de contrôle. Ce rapport peut être visualisé en définissant **Show Performance For (Afficher les performances pour)** sur **By Variant (Par variante)**.

Certains cas d’utilisation pour montrer les performances par variante :

- Vous avez des variantes ou des expériences dont les résultats semblent indiquer un effort inutile, ou n’ont pas de signification statistique ? Jetez-y un autre coup d’œil pour voir si une d’entre elles a eu un impact plus durable dans le temps.
- En explorant les données de rétention du groupe de contrôle, vous pouvez voir à quoi ressemblerait la rétention si vous n’envoyiez pas de message.

{% tabs %}
{% tab Campaign %}

![Afficher par variante]({% image_buster /assets/img/variant_view.png %})

{% endtab %}
{% tab Canvas %}

![Afficher par variante]({% image_buster /assets/img/variant_view_canvas.png %})

{% endtab %}
{% endtabs %}

#### Rapport de rétention par composants de variante

- **Date Range (Plage de dates)** : Définie sur la page **Details (Détails)** de la campagne ou du Canvas, la plage de dates inclut tous les utilisateurs ayant reçu la campagne ou le Canvas pendant cette fenêtre. Parmi ces utilisateurs, ceux qui ont effectué leur événement de rétention pendant la période auront leurs données dans le rapport. Le taux de rétention, le pourcentage d’écart par rapport au groupe de contrôle et la confiance sont mesurés chaque jour.
- **Retention Rate (Taux de rétention)** : Affiche le taux de rétention par variante. Le taux de rétention est équivalent au nombre d’utilisateurs ayant effectué l’événement de rétention divisé par le total des utilisateurs ayant reçu la campagne ou le Canvas.
- **Percentage Change from Control (Pourcentage de variation par rapport au groupe de contrôle)**: Quantifie le pourcentage d’écart par variante par rapport au groupe de contrôle.
- **Confidence (Confiance)** : Braze compare le taux de conversion de chaque variante avec le taux de conversion du contrôle via une procédure statistique appelée Z Test pour calculer un pourcentage de [confiance]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#understanding-confidence). Ce pourcentage indique dans quelle mesure la variante fonctionne mieux que le groupe de groupe de contrôle.
- **Units (Unités)** : Vous pouvez ajuster les unités pour le pourcentage d’utilisateurs et le nombre d’utilisateurs dans le coin supérieur droit du graphique, des unités spécifiques peuvent s’avérer plus significatives pour juger l’impact d’une campagne ou d’un Canvas.
- **Variant Graph (Graphique de variante)** : Ce graphique résume les résultats par variante pour la plage de dates sélectionnée.

## Choses à rechercher dans vos rapports de rétention

Les rapports de rétention sont faciles à générer, mais difficiles à interpréter pour agir en conséquence. Pour aider les marketeurs, nous avons rassemblé quelques sujets et questions à prendre en compte lorsque vous vous penchez sur vos rapports de rétention.

- Envisagez les tendances de la semaine pour les campagnes récurrentes (par ex. les cohortes du lundi marchent-elles mieux que les cohortes du samedi ?).
- Où l’impact commence-t-il à décliner ? Il peut s’agir d’un signal indiquant qu’une nouvelle campagne/Canvas pour cibler les utilisateurs à ce moment-là est nécessaire afin d’améliorer la rétention. 
- Constatez-vous une lassitude par rapport aux messages ?
- Une optimisation spécifique que vous avez faite à une campagne/un Canvas il y a X jours a-t-elle eu un impact positif ?

[1]: {% image_buster /assets/img/retention_1.png %}
[2]: {% image_buster /assets/img/retention_2.png %}
[5]: {% image_buster /assets/img/range_retention.png %}
[8]: {% image_buster /assets/img/date_select_retention.png %}


