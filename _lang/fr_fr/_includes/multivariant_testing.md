{% if include.section == "Variant distribution" %}

La répartition entre les variantes n'est pas toujours homogène. Voici comment fonctionne la répartition des variantes.

Chaque fois qu'un message est envoyé dans le cadre d'une campagne multivariée, le système sélectionne de manière indépendante une option aléatoire en fonction des pourcentages que vous avez définis et attribue une variante en fonction du résultat. C'est comme jouer à pile ou face : des anomalies sont possibles. Si vous avez déjà tiré 100 fois à pile ou face, vous savez que vous n'obtiendrez probablement pas exactement 50-50 entre pile et face à chaque fois, même si vous n'avez que deux choix. Vous obtiendrez peut-être 52 face et 48 pile.

Si vous avez plusieurs variantes que vous souhaitez répartir de manière égale, vous devez également vous assurer que le nombre de variantes est un multiple de 100. Sinon, certaines variantes auront un pourcentage plus élevé d'utilisateurs distribués à cette variante par rapport à d'autres. Par exemple, si votre campagne comporte 7 variantes, il ne peut y avoir de répartition égale des variantes puisque 7 ne se divise pas également par 100 en tant que nombre entier. Dans ce cas, vous auriez 2 variantes de 15 % et 5 variantes de 14 %.

#### Remarque concernant les messages in-app

Lors de l'exécution d'un test A/B sur les messages in-app, vos analyses peuvent sembler montrer une distribution plus élevée entre une variante et une autre, même si elles ont une répartition en pourcentage égale. Par exemple, considérez le graphique suivant des *destinataires uniques* pour la variante A et la variante C.

![Graphique des destinataires uniques pour deux variantes avec une forme similaire entre la variante A et la variante C, où la variante A a un plus grand nombre de destinataires uniques par jour]({% image_buster /assets/img/variant_distribution_iam.png %})

La variante A a un nombre de *destinataires uniques* systématiquement plus élevé que la variante C. Cela n'est pas dû à la distribution des variantes, mais plutôt à la façon dont les *destinataires uniques* sont calculés pour les messages in-app. Pour les messages in-app, les *Destinataires uniques* sont en fait des *Impressions uniques*, c'est-à-dire le nombre total de personnes qui ont reçu et consulté le message in-app. Cela signifie que si un utilisateur ne reçoit pas le message pour une raison quelconque ou décide de ne pas le consulter, il n'est pas inclus dans le décompte des *destinataires uniques* et la distribution des variantes peut apparaître faussée.

{% endif %}