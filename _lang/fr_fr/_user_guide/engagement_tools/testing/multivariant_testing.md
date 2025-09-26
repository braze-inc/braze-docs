---
nav_title: Test A/B et multivarié
article_title: Test A/B et multivarié
page_order: 2
page_type: reference
description: "Cet article de référence explique ce que sont les tests A/B et multivariés et leurs avantages."
search_rank: 2
---

# Test A/B et multivarié

> Cette page explique ce que sont les tests A/B et multivariés et leurs avantages. Pour savoir comment créer un test multivarié ou A/B, consultez la section [Créer des tests A/B et multivariés avec Braze]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/). 

Les tests multivariés et A/B peuvent être utilisés à l'aide de la [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

## En quoi consiste les tests A/B et multivariés ?

### Test A/B

Un test A/B est une expérience qui compare les réponses des utilisateurs à plusieurs versions de la même campagne marketing. Ces versions partagent des objectifs marketing similaires, mais diffèrent en termes de formulation et de style.

L’objectif est d’identifier la version de la campagne qui accomplit le mieux vos objectifs marketing. Dans cette section, nous examinerons comment tester l’efficacité des différences de contenu.

{% alert note %}
Si vous souhaitez évaluer les différences de planification des messages (par exemple, l'envoi d'un message concernant un panier abandonné après une heure d'inactivité par rapport à un jour d'inactivité), reportez-vous à notre section sur la [mise en place d'un Canvas.]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
{% endalert %}

Supposons que vous ayez deux options pour une notification push :

- "Cette offre expire demain !"
- "Cette offre expire dans 24 heures !"

À l’aide d’un test A/B, vous pouvez voir quelle formulation produit le taux de conversion le plus élevé. Ainsi, la prochaine fois que vous envoyez une notification push à propos d’une offre, vous saurez quel type de formulation est le plus efficace. Cependant, ce type de test examine uniquement l’effet d’une variable, c’est-à-dire le texte d’une notification push.

### Test multivarié

Un test multivarié est similaire à un test A/B, mais il teste les effets de deux variables ou plus. Retournons à notre exemple de notification push. Une autre variable que nous pourrions tester est d’inclure un émoji à la fin du message. Nous allons maintenant tester deux variables (à ne pas confondre avec les variantes), d’où le terme « multivarié ». Pour ce faire, nous allons tester quatre versions du message : deux options pour le texte multipliées par deux options pour les émojis (avec et sans émoji), soit un total de quatre variantes du message.

Dans la documentation Braze, « test multivarié » est utilisé de façon interchangeable avec « test A/B » étant donné que le processus pour les créer est identique.

## Avantages des tests A/B et multivariés {#the-benefits-of}

Les tests A/B et multivariés sont un excellent moyen pour comprendre facilement et clairement votre audience. Grâce à ce type de tests, vous n’avez plus besoin de deviner ce qui fonctionnera le mieux auprès de vos utilisateurs ; chaque campagne devient une opportunité d’essayer plusieurs variantes d’un message et d’évaluer les réactions de votre audience.

Voici quelques scénarios dans lesquels les tests A/B et multivariés pourraient être utiles :

- **Lorsque vous essayez un type d'envoi de messages pour la première fois :** Vous n’êtes pas sûr(e) de proposer les bons messages in-app dès la première fois ? Les tests multivariés vous permettent d’expérimenter et d’apprendre ce qui fonctionne le mieux auprès de vos utilisateurs.
- **Lorsque vous créez des campagnes d’onboarding et d’autres campagnes qui sont envoyées de manière continue :** Étant donné que la plupart de vos utilisateurs recevront cette campagne, pourquoi ne pas faire en sorte qu’elle soit aussi efficace que possible ?
- **Lorsque vous avez plusieurs idées de messages à envoyer :** Si vous n’êtes pas sûr(e) de savoir quel message vous devriez choisir, lancez un test et prenez une décision en vous basant sur les données recueillies.
- **Lorsque vous essayez de savoir si des techniques marketing éprouvées seront efficaces pour vos utilisateurs :** Les spécialistes du marketing suivent souvent des tactiques conventionnelles pour interagir avec leurs utilisateurs, mais la base utilisateur de chaque produit est différente. Parfois, le fait de renvoyer des messages d’appel à l’action ou d’utiliser des preuves sociales ne vous donnera pas les résultats escomptés. Les tests A/B et multivariés vous permettent de sortir des sentiers battus et de découvrir des tactiques non conventionnelles qui fonctionnent auprès de votre audience.

### Distribution variante

La répartition entre les variantes n'est pas toujours homogène. Voici comment fonctionne la répartition des variantes.

Chaque fois qu'un message est envoyé dans le cadre d'une campagne multivariée, le système sélectionne de manière indépendante une option aléatoire en fonction des pourcentages que vous avez définis et attribue une variante en fonction du résultat. C'est comme jouer à pile ou face : des anomalies sont possibles. Si vous avez déjà tiré 100 fois à pile ou face, vous savez que vous n'obtiendrez probablement pas exactement 50-50 entre pile et face à chaque fois, même si vous n'avez que deux choix. Vous obtiendrez peut-être 52 face et 48 pile.

Si vous avez plusieurs variantes que vous souhaitez répartir de manière égale, vous devez également vous assurer que le nombre de variantes est un multiple de 100. Sinon, certaines variantes auront un pourcentage plus élevé d'utilisateurs distribués à cette variante par rapport à d'autres. Par exemple, si votre campagne comporte 7 variantes, il ne peut y avoir de répartition égale des variantes puisque 7 ne se divise pas également par 100 en tant que nombre entier. Dans ce cas, vous auriez 2 variantes de 15 % et 5 variantes de 14 %.

#### Remarque concernant les messages in-app

Lors de l'exécution d'un test A/B sur des messages in-app, vos analyses peuvent sembler montrer une distribution plus élevée entre une variante et une autre, même si elles ont un pourcentage de répartition égal. Par exemple, considérez le graphique suivant des *destinataires uniques* pour la variante A et la variante C.

![Graphique des destinataires uniques pour deux variantes avec une forme similaire entre la variante A et la variante C, où la variante A a un plus grand nombre de destinataires uniques par jour]({% image_buster /assets/img/variant_distribution_iam.png %})

La variante A a un nombre de *destinataires uniques* systématiquement plus élevé que la variante C. Cela n'est pas dû à la distribution des variantes, mais plutôt à la façon dont les *destinataires uniques* sont calculés pour les messages in-app. Pour les messages in-app, les *Destinataires uniques* sont en fait des *Impressions uniques*, c'est-à-dire le nombre total de personnes qui ont reçu et consulté le message in-app. Cela signifie que si un utilisateur ne reçoit pas le message pour une raison quelconque ou décide de ne pas le consulter, il n'est pas inclus dans le décompte des *destinataires uniques* et la distribution des variantes peut apparaître faussée.

## Conseils pour les tests multivariés et les tests A/B

Les tests A/B et multivariés peuvent révéler d’importantes informations sur vos utilisateurs. Pour obtenir des résultats de test qui reflètent réellement les comportements de vos utilisateurs, suivez les lignes directrices suivantes.

#### Effectuez le test sur un grand nombre d’utilisateurs

Les échantillons de grande taille garantissent que vos résultats reflèteront les préférences de votre utilisateur moyen et seront moins susceptibles d’être altérés par des valeurs aberrantes. Des échantillons de plus grande taille vous permettent également d'identifier les variantes gagnantes dont les marges de victoire sont plus faibles.

#### Classez les utilisateurs de manière aléatoire dans différents groupes de test

Les tests multivariés vous permettent de créer jusqu'à huit groupes de test sélectionnés de manière aléatoire. La randomisation permet d’éliminer les biais dans les tests et augmente la probabilité que les groupes de tests aient une composition similaire. Cela garantit que les différences de réaction seront dues à des différences dans vos messages plutôt que dans vos échantillons.

#### Prenez note des éléments que vous essayez de tester

Les tests A/B et multivarié vous permettent de tester les différences entre plusieurs versions d’un message. Dans certains cas, un test simple peut s’avérer le plus efficace. Le fait d’isoler les changements dans votre message vous permet d’identifier les éléments qui ont eu le plus d’impact sur la réaction de vos utilisateurs. Dans d’autres cas, le fait de présenter plus de différences entre les variantes vous permet d’examiner les valeurs aberrantes et de comparer différents ensembles d’éléments. Aucune de ces méthodes n’est nécessairement meilleure que l’autre, à condition que vous sachiez clairement dès le début ce que vous essayez de tester.

#### Décidez de la durée de votre test et n’interrompez pas votre test prématurément

Décidez de la durée de votre test avant de le lancer, et ne l’interrompez pas prématurément. Les spécialistes du marketing sont souvent tentés d’interrompre leurs tests dès que les résultats vont en leur sens, ce qui a pour effet de biaiser les résultats. Résistez à la tentation de jeter un œil aux résultats avant la fin du test et ne terminez jamais votre test prématurément !

#### Ajoutez votre test aux campagnes avant qu'elles ne soient lancées, et non après.

Si vous ajoutez votre test à une campagne après son lancement, le test ne se déroulera pas correctement et vous risquez de recevoir des statistiques incorrectes ou trompeuses. Par exemple, si vous ajoutez un test à une campagne lancée qui autorise la réinscription, les utilisateurs qui réintègrent la campagne passeront toujours par le même chemin afin d'éviter toute inexactitude des données avec le test. En outre, si vous modifiez l'une des variantes alors que le test est en cours d'exécution, la modification invalidera votre test et le relancera.

Pour des résultats de test précis :
1. Clonez la campagne lancée.
2. Arrêtez la campagne initiale.
3. Ajoutez ensuite le test à la campagne clonée. 

#### Si possible, ajoutez un groupe de contrôle

L'inclusion d'un [groupe de contrôle]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#including-a-control-group) vous permet de savoir si vos messages ont un impact plus important sur la conversion des utilisateurs que l'absence de message.


