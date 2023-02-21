---
nav_title: Test A/B et multivarié
article_title: Test A/B et multivarié
page_order: 2
page_type: reference
description: "Cet article de référence explique ce que sont les tests A/B et multivariés et leurs avantages."
search_rank: 2
---

# Test A/B et multivarié

> Cette page explique ce que sont les tests A/B et multivariés et leurs avantages. Pour connaître les étapes permettant de créer un test A/B ou multivarié, consultez la section [Créer des tests A/B et multivariés avec Braze]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/). 

Les tests A/B et multivariés peuvent être rapidement utilisés à l’aide de la [Sélection intelligente]({{site.baseurl}}/user_guide/intelligence/intelligent_selection/).

## En quoi consiste les tests A/B et multivariés ?

### Test A/B

Un test A/B est une expérience qui compare les réponses des utilisateurs à plusieurs versions de la même campagne marketing. Ces versions partagent des objectifs marketing similaires, mais diffèrent en termes de formulation et de style.

L’objectif est d’identifier la version de la campagne qui remplit le mieux vos objectifs marketing. Dans cette section, nous examinerons comment tester l’efficacité des différences de contenu.

{% alert note %}
Si vous souhaitez évaluer les différences dans la programmation ou le timing des messages (par exemple, la différence entre envoyer un message de panier abandonné après une heure d’inactivité ou un jour d’inactivité), consultez notre section sur la configuration des [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
{% endalert %}

Supposons que vous ayez deux options pour une notification push :

- « Cette offre expire demain ! »
- « Cette offre expire dans 24 heures ! »

À l’aide d’un test A/B, vous pouvez voir quelle formulation produit le taux de conversion le plus élevé. Ainsi, la prochaine fois que vous envoyez une notification push à propos d’une offre, vous saurez quel type de formulation est le plus efficace. Cependant, ce type de test examine uniquement l’effet d’une variable, c’est-à-dire le texte d’une notification push.

### Test multivarié

Un test multivarié est similaire à un test A/B, mais il teste les effets de deux variables ou plus. Retournons à notre exemple de notification push. Une autre variable que nous pourrions tester est d’inclure un émoji à la fin du message. Nous allons maintenant tester deux variables (à ne pas confondre avec les variantes), d’où le terme « multivarié ». Pour ce faire, nous allons tester quatre versions du message : deux options pour le texte multipliées par deux options pour les émojis (avec et sans émoji), soit un total de quatre variantes du message.

Dans la documentation Braze, « test multivarié » est utilisé de façon interchangeable avec « test A/B » étant donné que le processus pour les créer est identique.

## Avantages des tests A/B et multivariés {#the-benefits-of}

Les tests A/B et multivariés sont un excellent moyen pour comprendre facilement et clairement votre audience. Grâce à ce type de tests, vous n’avez plus besoin de deviner ce qui fonctionnera le mieux auprès de vos utilisateurs ; chaque campagne devient une opportunité d’essayer plusieurs variantes d’un message et d’évaluer les réactions de votre audience.

Voici quelques scénarios dans lesquels les tests A/B et multivariés pourraient être utiles :

- **Lorsque vous essayez un type de message pour la première fois :** Vous n’êtes pas sûr(e) de proposer les bons messages in-app dès la première fois ? Les tests multivariés vous permettent d’expérimenter et d’apprendre ce qui fonctionne le mieux auprès de vos utilisateurs.
- **Lorsque vous créez des campagnes d’onboarding et d’autres campagnes qui sont envoyées de manière continue :** Étant donné que la plupart de vos utilisateurs recevront cette campagne, pourquoi ne pas faire en sorte qu’elle soit aussi efficace que possible ?
- **Lorsque vous avez plusieurs idées de message :** Si vous n’êtes pas sûr(e) de savoir quel message vous devriez choisir, lancez un test et prenez une décision en vous basant sur les données recueillies.
- **Lorsque vous essayez de savoir si des techniques marketing éprouvées seront efficaces pour vos utilisateurs :**  Les marketeurs suivent souvent des tactiques conventionnelles pour interagir avec leurs utilisateurs, mais la base utilisateur de chaque produit est différente. Parfois, le fait de renvoyer des messages d’appel à l’action ou d’utiliser des preuves sociales ne vous donnera pas les résultats escomptés. Les tests A/B et multivariés vous permettent de sortir des sentiers battus et de découvrir des tactiques non conventionnelles qui fonctionnent auprès de votre audience.

## Cinq règles pour les tests A/B et multivariés {#five-rules-for}

Les tests A/B et multivariés peuvent révéler d’importantes informations sur vos utilisateurs. Suivez les directives ci-dessous pour vous assurer que les résultats de votre test reflètent vraiment les comportements de vos utilisateurs.

#### Effectuez le test sur un grand nombre d’utilisateurs

Les échantillons de grande taille garantissent que vos résultats reflèteront les préférences de votre utilisateur moyen et seront moins susceptibles d’être altérés par des valeurs aberrantes. Ces grands échantillons vous permettent également d’identifier les variantes gagnantes qui ont des marges de réussite plus petites.

#### Classez les utilisateurs de manière aléatoire dans différents groupes de test

Les tests multivariés de Braze vous permettent de créer jusqu’à huit groupes de tests sélectionnés de manière aléatoire. La randomisation permet d’éliminer les biais dans les tests et augmente la probabilité que les groupes de tests aient une composition similaire. Cela garantit que les différences de réaction seront dues à des différences dans vos messages plutôt que dans vos échantillons.

#### Prenez note des éléments que vous essayez de tester

Les tests A/B et multivarié vous permettent de tester les différences entre plusieurs versions d’un message. Dans certains cas, un test simple peut s’avérer le plus efficace. Le fait d’isoler les changements dans votre message vous permet d’identifier les éléments qui ont eu le plus d’impact sur la réaction de vos utilisateurs. Dans d’autres cas, le fait de présenter plus de différences entre les variantes vous permet d’examiner les valeurs aberrantes et de comparer différents ensembles d’éléments. Aucune de ces méthodes n’est nécessairement meilleure que l’autre, à condition que vous sachiez clairement dès le début ce que vous essayez de tester.

#### Décidez de la durée de votre test et n’interrompez pas votre test prématurément

Décidez de la durée de votre test avant de le lancer, et ne l’interrompez pas prématurément. Les marketeurs sont souvent tentés d’interrompre leurs tests dès que les résultats vont en leur sens, ce qui a pour effet de biaiser les résultats. Résistez à la tentation de jeter un œil aux résultats avant la fin du test et ne terminez jamais votre test prématurément !

#### Si possible, ajoutez un groupe de contrôle

Ajouter un [groupe de contrôle]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#including-a-control-group) à votre test vous permet de savoir si le fait d’envoyer un message aura plus d’impact sur le taux de conversion des utilisateurs que de ne pas envoyer de message.


[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[70]: #tips-different-channels
[80]: #choosing-a-segment
[160]: {% image_buster /assets/img/ab_create_1.png %}
[170]: {% image_buster /assets/img/ab_create_2.png %}
[175]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/
[180]: {% image_buster /assets/img/ab_create_4.png %}
[210]: {% image_buster /assets/img/ab_create_8.png %}
[10]: {% image_buster /assets/img/ab_send_winning_variant.png %}
[272]: #intelligent-selection
[273]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/
[intelselection]: {{site.baseurl}}/user_guide/intelligence/intelligent_selection/
[confidence]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/#understanding-confidence
