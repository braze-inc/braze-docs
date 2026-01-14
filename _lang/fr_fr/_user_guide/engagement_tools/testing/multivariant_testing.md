---
nav_title: Test multivarié et test A/B
article_title: Test multivarié et test A/B
page_order: 2
page_type: reference
description: "Cet article de référence explique le test multivarié et le test A/B ainsi que leurs avantages."
search_rank: 2
---

# Test multivarié et test A/B

> Cette page explique ce que sont les tests multivariés et les tests A/B, ainsi que leurs avantages. Pour savoir comment créer un test multivarié ou A/B, reportez-vous à la section [Créer des tests multivariés et A/B avec Braze]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/). 

Les tests multivariés et A/B peuvent être utilisés à l'aide de la [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

## Que sont les tests multivariés et les tests A/B ?

### test A/B

Un test A/B est une expérience qui compare les réponses des utilisateurs à plusieurs versions d'une même campagne marketing. Ces versions partagent des objectifs marketing similaires mais diffèrent par leur formulation et leur style.

L'objectif est d'identifier la version de la campagne qui répond le mieux à vos objectifs de marketing. Dans cette section, nous verrons comment tester l'efficacité des différences de contenu.

{% alert note %}
Si vous souhaitez évaluer les différences de planification des messages (par exemple, l'envoi d'un message concernant un panier abandonné après une heure d'inactivité par rapport à un jour d'inactivité), reportez-vous à notre section sur la [mise en place d'un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
{% endalert %}

Supposons que vous ayez deux options pour une notification push :

- "Cette offre expire demain !"
- "Cette offre expire dans 24 heures !"

À l'aide d'un test A/B, vous pouvez voir quelle formulation entraîne un taux de conversion plus élevé. La prochaine fois que vous enverrez une notification push sur une offre, vous saurez quel type de formulation est le plus efficace. Cependant, ce test n'examine que l'effet d'une seule variable - la copie dans la notification push.

### Test multivarié

Un test multivarié est similaire à un test A/B, sauf qu'il teste les effets de deux variables ou plus. Revenons à notre exemple de notification push. Une autre variable que nous pourrions vouloir tester est l'inclusion ou non d'un emoji à la fin du message. Nous testerions alors deux variables (à ne pas confondre avec les variantes), d'où le terme "multivarié". Pour ce faire, nous devrions tester quatre versions du message au total - deux options pour le texte multipliées par deux options pour l'emoji (présent ou non) égalent quatre variantes de message au total.

Dans la documentation de Braze, "test multivarié" est utilisé indifféremment de "test A/B", car le processus de mise en place est le même.

## Avantages des tests multivariés et des tests A/B {#the-benefits-of}

Les tests multivariés et les tests A/B vous offrent un moyen simple et clair d'en savoir plus sur votre audience. Vous n'avez plus à deviner la réaction des utilisateurs : chaque campagne devient l'occasion d'essayer différentes variantes d'un message et d'évaluer la réaction de l'audience.

Parmi les scénarios spécifiques dans lesquels les tests multivariés et les tests A/B peuvent s'avérer utiles, citons les suivants :

- **Lorsque vous essayez un type d'envoi de messages pour la première fois :** Vous avez peur de ne pas réussir l'envoi de messages in-app du premier coup ? Les tests multivariés vous permettent d'expérimenter et d'apprendre ce qui résonne chez vos utilisateurs.
- **Lors de la création de campagnes d'onboarding et d'autres campagnes qui sont constamment envoyées :** Puisque la plupart de vos utilisateurs rencontreront cette campagne, pourquoi ne pas s'assurer qu'elle est aussi efficace que possible ?
- **Lorsque vous avez plusieurs idées de messages à envoyer :** Si vous ne savez pas lequel choisir, effectuez un test, puis prenez une décision fondée sur des données.
- **Lorsque vous cherchez à savoir si vos utilisateurs réagissent aux techniques de marketing "éprouvées" :** Les marketeurs s'en tiennent souvent à des tactiques conventionnelles pour engager le dialogue avec les utilisateurs, mais la base d'utilisateurs de chaque produit est différente. Parfois, la répétition de votre call-to-action et l'utilisation de la preuve sociale ne vous permettront pas d'obtenir les résultats escomptés. Les tests multivariés et A/B vous permettent de sortir des sentiers battus et de découvrir des tactiques non conventionnelles qui fonctionnent pour votre audience spécifique.

### Distribution des variantes

{% multi_lang_include multivariant_testing.md section='Variant distribution' %}

## Conseils pour les tests multivariés et les tests A/B

Les tests multivariés et les tests A/B peuvent dévoiler de puissantes informations concernant vos utilisateurs. Pour obtenir des résultats de test qui reflètent réellement les comportements de vos utilisateurs, suivez les lignes directrices suivantes.

#### Exécutez le test sur un grand nombre d'utilisateurs

De larges échantillons garantissent que vos résultats reflètent les préférences de l'utilisateur moyen et sont moins susceptibles d'être influencés par des valeurs aberrantes. Des échantillons de plus grande taille vous permettent également d'identifier les variantes gagnantes dont les marges de victoire sont plus faibles.

#### Répartir les utilisateurs de manière aléatoire dans différents groupes de test.

Les tests multivariés vous permettent de créer jusqu'à huit groupes de test sélectionnés de manière aléatoire. La randomisation est conçue pour éliminer les biais dans l'ensemble de test et augmenter les chances que les groupes de test soient similaires dans leur composition. Cela permet de s'assurer que les différences de taux de réponse sont dues à des différences dans vos messages plutôt que dans vos échantillons.

#### Sachez quels sont les éléments que vous essayez de tester

Le test multivarié et le test A/B vous permettent de tester les différences entre plusieurs versions d'un message. Dans certains cas, un simple test peut s'avérer plus efficace, car l'isolement des changements vous permet d'identifier les éléments qui ont eu le plus d'impact sur la réponse. Dans d'autres cas, la présentation d'un plus grand nombre de différences entre les variantes vous permettra d'examiner les valeurs aberrantes et de comparer différents ensembles d'éléments. Aucune des deux méthodes n'est nécessairement mauvaise, à condition que vous sachiez dès le départ ce que vous essayez de tester.

#### Décidez de la durée de votre test et n'y mettez pas fin prématurément.

Avant de commencer le test, décidez de sa durée et respectez-la. Les marketeurs sont souvent tentés d'arrêter les tests après avoir obtenu des résultats qui leur plaisent, ce qui biaise leurs conclusions. Résistez à la tentation de jeter un coup d'œil et ne terminez jamais votre test avant la fin !

#### Ajoutez votre test aux campagnes avant qu'elles ne soient lancées, et non après.

Si vous ajoutez votre test à une campagne après son lancement, le test ne se déroulera pas correctement et vous risquez de recevoir des statistiques incorrectes ou trompeuses. Par exemple, si vous ajoutez un test à une campagne lancée qui autorise la réinscription, les utilisateurs qui réintègrent la campagne passeront toujours par le même chemin afin d'éviter toute inexactitude des données avec le test. En outre, si vous modifiez l'une des variantes alors que le test est en cours d'exécution, la modification invalidera votre test et le relancera.

Pour des résultats de test précis :
1. Clonez la campagne lancée.
2. Arrêtez la campagne initiale.
3. Ajoutez ensuite le test à la campagne clonée. 

#### Si possible, incluez un groupe de contrôle.

L'inclusion d'un [groupe de contrôle]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#including-a-control-group) vous permet de savoir si vos messages ont un impact plus important sur la conversion des utilisateurs que l'absence de message.


