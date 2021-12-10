---
nav_title: Tests multivariés & A/B
article_title: Tests multivariés et A/B
page_order: 2
page_type: Référence
description: "Cet article de référence explique les tests Multivariate et A/B, leurs avantages et comment les créer avec Braze."
---

# Tests multivariés et A/B

Les tests multivariés et A/B peuvent être rapidement utilisés en utilisant notre fonctionnalité [Sélection intelligente]({{site.baseurl}}/user_guide/intelligence/intelligent_selection/).

## Que sont les tests multivariés et A/B?

Un test A/B est une expérience qui compare les réponses des utilisateurs à plusieurs versions de la même campagne marketing. Ces versions partagent des objectifs de marketing similaires, mais diffèrent en termes de formulation et de style.

L'objectif est d'identifier la version de la campagne qui réalise le mieux vos objectifs marketing. Dans cette section, nous allons examiner comment tester l'efficacité des différences de contenu.

{% alert note %}
Si vous souhaitez évaluer les différences dans la planification des messages ou le chronométrage (par exemple, envoyer un message de panier abandonné après 1 heure d'inactivité contre 1 jour d'inactivité), veuillez vous référer à notre section sur la mise en place d'un [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
{% endalert %}

Supposons que vous ayez deux options pour une notification push :

- « Cette offre expire demain! »
- « Cette offre expire dans 24 heures! »

En utilisant un test A/B, vous pouvez voir quel libellé donne un taux de conversion plus élevé. La prochaine fois que vous enverrez une notification push à propos d’un accord, vous saurez quel type de libellé est plus efficace.

Le test ci-dessus n'examine que l'effet d'une seule variable : la copie de la notification push. Un test multivarié est similaire, sauf qu'il teste les effets de deux ou plusieurs variables. Une autre variable que nous pourrions tester est d'inclure un émoji à la fin du message. Nous testions maintenant deux variables (ou variates) — à ne pas confondre avec des variantes; d'où le terme "multivariate". Pour cela, nous aurions besoin de tester quatre versions totales du message — deux options pour la copie multipliée par deux options pour l'émoji (présent ou non) équivaut à quatre variantes de message total.

Dans la documentation de Braze, "multivariate test" est utilisé de manière interchangeable avec "A/B test".

## Les avantages des tests multivariés et A/B {#the-benefits-of}

Les tests multivariés et A/B vous permettent de mieux connaître votre public. Vous n'avez plus à deviner à quoi les utilisateurs répondront. Chaque campagne devient l'occasion d'essayer différentes variantes d'un message et de mesurer la réponse de l'auditoire.

Des scénarios spécifiques dans lesquels des tests multivariés et A/B pourraient s'avérer utiles:

- **Lorsque vous essayez un type de messagerie pour la première fois :** Vous avez peur de recevoir la messagerie dans l'application dès la première fois ? Les tests multivariés vous permettent d’expérimenter et d’apprendre ce qui résonne avec vos utilisateurs.
- **Lors de la création de campagnes d'intégration et d'autres campagnes qui sont constamment envoyées :** Puisque la plupart de vos utilisateurs rencontreront cette campagne, pourquoi ne pas s'assurer que c'est aussi efficace que possible?
- **Lorsque vous avez plusieurs idées à envoyer des messages :** Si vous n'êtes pas sûr de savoir lequel choisir, exécuter un test et ensuite prendre une décision basée sur les données.
- **En vérifiant si vos utilisateurs répondent à des techniques de marketing "éprouvées et vraies" :**  Les marketeurs s'en tiennent souvent à des tactiques conventionnelles pour s'engager auprès des utilisateurs, mais la base d'utilisateurs de chaque produit est différente. Parfois, répéter votre appel à l'action et utiliser la preuve sociale ne vous donnera pas les résultats souhaités. Les tests multivariés et A/B vous permettent de sortir de la boîte et de découvrir des tactiques non conventionnelles qui conviennent à votre public spécifique.

## Cinq règles pour les tests multivariés et A/B {#five-rules-for}

Les tests multivariés et A/B peuvent révéler de puissantes connaissances concernant vos utilisateurs. Pour vous assurer que les résultats de votre test reflètent réellement les comportements de vos utilisateurs, suivez ces directives :

1. **Exécutez le test sur un grand nombre d'utilisateurs.** Les grands échantillons vous assurent que vos résultats reflètent les préférences de votre utilisateur moyen et sont moins susceptibles d'être influencés par des externes. De plus grandes tailles d'échantillons vous permettent également d'identifier les variantes gagnantes qui ont des marges de victoire plus petites.
2. **Triez aléatoirement les utilisateurs dans différents groupes de tests.** La fonctionnalité multivariée de Braze vous permet de créer jusqu'à huit groupes de test sélectionnés aléatoirement. Le Randomisation est conçu pour supprimer les biais dans le jeu de tests et augmenter la probabilité que les groupes de tests soient similaires dans la composition. Cela permet de s'assurer que les taux de réponse différents sont dus à des différences dans vos messages plutôt qu'à vos échantillons.
3. **Sachez quels éléments vous essayez de tester.** Le test multivarié et A/B vous permet de tester les différences entre plusieurs versions d'un message. Dans certains cas, un simple test peut être le plus efficace, car l'isolement des changements vous permet d'identifier les éléments qui ont le plus d'impact sur la réponse. D'autres fois, présenter plus de différences entre les variantes vous permettra d'examiner les antécédents et de comparer différents ensembles d'éléments. Aucune des deux méthodes n'est nécessairement erronée, à condition que vous sachiez dès le début pour quoi vous essayez de tester.
4. **Décidez combien de temps votre test sera exécuté avant de commencer le test, et ne finissez pas votre test tôt !** Les marketeurs sont souvent tentés d'arrêter les tests après avoir vu les résultats qu'ils aiment, en biaisant leurs conclusions. Résistez à la tentation de jeter un coup d'œil et de ne jamais terminer votre test tôt !
5. **Si possible, inclure un groupe de pilotage.** Y compris un [groupe de contrôle](#including-a-control-group) vous permet de savoir si vos messages ont un impact plus important sur la conversion de l'utilisateur que d'envoyer un message du tout.

## Création de tests multivariés et A/B avec Braze {#creating-tests}

### Étape 1 : Créer votre campagne

Cliquez sur **Créer une campagne** et sélectionnez un canal pour la campagne dans la section qui permet le test multivarié et A/B. Pour une documentation détaillée sur chaque canal de messagerie, reportez-vous à [Créer une Campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/).

!\[Create Your Campaign\]\[160\]{: style="max-width:30%" }

### Étape 2 : Composez vos variantes

Vous pouvez créer jusqu'à huit variantes de votre message, différenciant entre les titres, le contenu, les images et plus encore. Le nombre de différences entre les messages détermine s'il s'agit d'un test multivarié ou A/B.

Pour quelques idées sur la façon de commencer à différencier vos variantes, consultez la section dans cet article sur [Conseils pour différents canaux][70].

!\[Composez vos variants\]\[170\]

### Étape 3 : Planifier votre campagne

Le test de planification fonctionne de la même façon que la planification de toute autre campagne de Braze. Tous les [types de livraison standard de Braze][175] sont disponibles.

### Étape 4 : Choisissez un segment et distribuez vos utilisateurs entre les variantes

Sélectionnez les segments à cibler, puis distribuez ses membres à travers les variantes sélectionnées, en plus de réserver une portion à envoyer à la variante gagnante, si nécessaire.

Décidez quel pourcentage de votre segment cible doit recevoir chacune de vos variantes, être dans le groupe de contrôle (le cas échéant), et quel pourcentage doit recevoir la variante gagnante une fois que le test A/B est terminé.

#### Y compris un groupe de contrôle {#including-a-control-group}

Lorsque vous créez un test multivarié ou A/B, vous pouvez réserver un pourcentage de votre public cible à un groupe de contrôle aléatoire. Les utilisateurs du groupe de contrôle ne reçoivent pas le test, mais Braze surveille leur taux de conversion pour la durée de la campagne.

Lorsque vous visualisez vos résultats, vous pouvez comparer les taux de conversion de vos variantes à un taux de conversion de base fourni par votre groupe de contrôle. Cela vous permet de comparer non seulement les effets de vos variantes, mais comparez aussi les effets de vos variantes avec le taux de conversion qui résulterait si vous n'aviez pas envoyé de message du tout.

La taille du groupe de contrôle pour une campagne avec [Sélection intelligente][intelselection] est basée sur le nombre de variantes. Si chaque variante est envoyée à plus de 20% des utilisateurs, alors le groupe de contrôle est de 20% et les variantes sont réparties uniformément sur les 80% restants. Cependant, si vous avez plusieurs variantes de sorte que chaque variante est envoyée à moins de 20% des utilisateurs, alors le groupe de contrôle doit devenir plus petit. Une fois que la sélection intelligente commence à analyser les performances de votre test, le groupe de contrôle grandit ou se rétrécit en fonction des résultats.

{% alert important %}
Il n'est pas recommandé d'utiliser un groupe de contrôle pour déterminer le gagnant par Ouvertures ou Clics. Parce que le groupe de contrôle ne reçoit pas le message, ces utilisateurs ne peuvent effectuer aucune ouverture ou aucun clic. Par conséquent, le taux de conversion de ce groupe est de 0 % par définition et ne constitue pas une comparaison significative avec les variantes.
{% endalert %}

L'envoi automatique de la variante gagnante n'est disponible que pour les campagnes Email, Push et Webhook qui doivent être envoyées une fois.

!\[Choisissez un Segment\]\[180\]

Pour les meilleures pratiques concernant le choix d'un segment à tester, reportez-vous à la section ci-dessous sur [Choisir un segment][80].

### Étape 5 : Choisissez l'action qui détermine le gagnant

La Variante gagnante peut être mesurée en `Ouvertures uniques` ou `Clics` pour l'e-mail, `Ouvre` pour Push, ou `Taux de Conversion Primaire` pour tous les canaux. La sélection de `Ouvre` ou `Clics` pour déterminer le gagnant n'affecte pas ce que vous choisissez pour les [événements de conversion][2] de la campagne.

Gardez à l'esprit que si vous utilisez un groupe de contrôle, les utilisateurs du groupe de contrôle ne peuvent pas effectuer `Ouvre` ou `Clics`, ainsi la « performance » du groupe de contrôle est garantie d'être `0`. Par conséquent, le groupe de contrôle ne peut pas « gagner » le test A/B. Cependant, vous pouvez toujours utiliser un groupe de contrôle pour suivre d'autres mesures pour les utilisateurs qui ne reçoivent pas de message.

### Étape 6: Planifier quand envoyer la variante gagnante

Choisissez une date et une heure où la variante gagnante doit être envoyée.

{% alert note %}
Lors de l'envoi de l'heure locale des utilisateurs ou avec le Timing Intelligent, la variante gagnante doit être envoyée au moins 24 heures après le test A/B pour assurer la livraison à tous les utilisateurs du groupe de variantes gagnantes.
{% endalert %}

Dans la liste déroulante en dessous de la date, vous pouvez également choisir d'envoyer ou non la meilleure variante performante même si elle ne gagne pas par une marge statistiquement significative.

#### (Facultatif) Désigne un événement de conversion

Définir un événement de conversion pour une campagne vous permet de voir combien de destinataires de cette campagne ont effectué une action particulière après l'avoir reçue.

Cela n'affecte le test que si vous avez choisi **Taux de conversion primaire** dans les étapes précédentes. Pour plus d'informations, reportez-vous à [Événements de conversion][2].

### Étape 7 : Réviser et lancer

Sur la page de confirmation, vérifiez les détails de votre campagne multivariée et lancez le test!

## Visualisation des résultats d'une campagne multivariée

Une fois votre campagne lancée, vous pouvez vérifier la performance de chaque variante en sélectionnant votre campagne dans la section **Campagnes** du tableau de bord. Une fois la campagne de test terminée, vous pouvez voir un résumé de la façon dont toutes les variantes ont été réalisées et s'il y a eu ou non un gagnant pendant le test.

If one variant outperformed all the others with better than 95% [confidence][confidence], Braze marks that variant with a “Winner” banner. Si aucune variante ne bat tous les autres avec 95% de confiance et que vous avez choisi d'envoyer la meilleure variante de toute façon, la « meilleure » variante performante sera toujours envoyée et indiquée avec une étiquette indiquant « Envoyée comme Variante gagnante ».

Sur la page Analytics, vous pouvez également voir les performances de la Variante gagnante tout au long de la campagne (y compris les envois de test A/B).

!\[Voir les résultats\]\[210\]

{% alert note %}
Braze teste toutes les variantes les unes contre les autres grâce aux tests [Pearson du carré](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test). Cela mesure si oui ou non une variante surpasse statistiquement toutes les autres à un niveau de signification de p < 0. 5, ou ce que nous appelons une signification de 95 %. Si oui, la variante gagnante est indiquée avec le label « Gagnant ». <br><br> Ceci est un test séparé du score de confiance, qui ne décrit que la performance d'une variante par rapport au contrôle avec une valeur numérique comprise entre 0 et 100%.
{% endalert %}

Une variante peut faire mieux que le groupe de contrôle, mais le test de chi-squared vérifie si une variante est meilleure que tout le reste. [tests de suivi](#recommended-follow-ups) peuvent donner plus de détails.

### Comprendre la confiance {#understanding-confidence}

Une partie importante de vos résultats est la confiance de vos résultats. Par exemple, que se passe-t-il si le groupe de contrôle avait un taux de conversion de 20 % et que la variante A avait un taux de conversion de 25 %? Cela semble indiquer que l'envoi de la variante A est plus efficace que d'envoyer aucun message. Ayant une confiance de 95% signifie que la différence entre les deux taux de conversion est probablement due à une différence réelle dans les réponses des utilisateurs et qu’il n’y a que 5% de probabilité que la différence ait eu lieu par hasard.

Braze compare le taux de conversion de chaque variante au taux de conversion du contrôle avec une procédure statistique appelée [Z&nbsp;Test](https://en.wikipedia.org/wiki/Z-test). Un résultat de 95 % ou plus de confiance, comme dans l'exemple ci-dessus, indique que la différence est statistiquement significative. Ceci est vrai partout où vous voyez une métrique de confiance dans le tableau de bord de Braze qui décrit la différence entre deux messages ou des populations d'utilisateurs.

En général, une confiance d'au moins 95% est nécessaire pour montrer que vos résultats reflètent les préférences réelles des utilisateurs, et non en raison du hasard. Dans le cadre de tests scientifiques rigoureux, 95% de confiance (ou autrement communément appelée la valeur « p » étant inférieure à 0. 5) est le point de référence commun utilisé pour déterminer l'importance statistique. Si vous ne parvenez pas à obtenir 95 % de confiance, essayez d'augmenter la taille de votre échantillon ou de diminuer le nombre de variantes. La confiance ne décrit pas si une variante est meilleure que les autres.

{% details Statistically insignificant results %}

Un test qui n’a pas confiance en 95 % peut toujours avoir des idées importantes. Voici quelques choses que vous pouvez apprendre d'un test avec des résultats statistiquement insignifiants :

- Il est possible que toutes vos variantes aient eu le même effet. Savoir cela vous permet d'économiser le temps que vous auriez passé à effectuer ces changements. Parfois, il se peut que vous trouviez que les tactiques de marketing conventionnelles, comme la répétition de votre appel à l’action, ne fonctionnent pas nécessairement pour votre public.
- Bien que vos résultats aient été dus au hasard, ils peuvent vous informer de l'hypothèse pour votre prochain test. Si plusieurs variantes semblent avoir les mêmes résultats à peu près exécuter certaines d'entre elles à nouveau à côté des nouvelles variantes pour voir si vous pouvez trouver une alternative plus efficace. Si une variante fait mieux, mais pas par une quantité significative, vous pouvez effectuer un autre test dans lequel la différence de cette variante est plus exagérée.
- Continuez à tester! Un test avec des résultats insignifiants devrait conduire à certaines questions. N'y a-t-il vraiment pas de différence entre vos variantes? Devriez-vous avoir structuré votre test différemment ? Vous pouvez répondre à ces questions en effectuant des tests de suivi.
- Tout en testant est utile pour découvrir quel type de messagerie génère le plus de réponse de votre public, Il est également important de comprendre quelles modifications de la messagerie ont seulement un effet négligeable.  Cela vous permet soit de continuer à tester pour une autre alternative plus efficace, ou économiser le temps qui a pu être passé à décider entre deux messages alternatifs.

Si votre test a ou non un gagnant clair, il peut être utile d'exécuter un test de suivi pour confirmer vos résultats ou appliquer vos résultats à un scénario légèrement différent.

{% enddetails %}

### Conseils pour différents canaux {#tips-different-channels}

Selon le canal que vous choisissez, vous pourrez tester différents composants de votre message. Essayez de composer des variantes avec une idée de ce que vous voulez tester et de ce que vous espérez prouver.

Quels leviers faut-il tirer et quels sont les effets souhaités? Bien qu'il y ait des millions de possibilités que vous pouvez étudier à l'aide d'un test multivarié et A/B, nous avons quelques suggestions pour vous aider à démarrer :

| Chaîne              | Les aspects du message que vous pouvez modifier                                                                                                                                                                                                                                                  | Résultats à rechercher                     |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------ |
| Pousser             | Copier <br> Utilisation des images et des émoticônes <br> Liens profonds  <br> Présentation des nombres (par ex. "triple" vs. "augmentation de 200%")  <br> Présentation du temps (par exemple "se termine à minuit" vs. "se termine dans 6 heures")                     | Ouvre le taux de conversion de  <br> |
| Courriel            | Sujet <br> Nom affiché <br> Salutation <br> Corps Copie <br> Image et Utilisation Emoji <br> Présentation des nombres (e. . "triple" vs. "augmentation de 200%") <br> Présentation du temps (par exemple "se termine à minuit" vs. "se termine en 6 heures") | Ouvre le taux de conversion de  <br> |
| Notification In-App | Aspects listés pour "push" <br> [Format de message][273]                                                                                                                                                                                                                                   | Taux de conversion de clic <br>      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert tip %}
Lorsque vous exécutez des tests A/B, n'oubliez pas de générer des [rapports d'entonnoir]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/funnel_reports/) qui vous permettent de comprendre l'impact de chaque variante sur votre entonnoir de conversion, surtout si la "conversion" pour votre entreprise implique de prendre plusieurs mesures ou actions.
{% endalert %}

De plus, la durée idéale de votre test peut également varier selon le canal. Gardez à l'esprit le temps moyen que la plupart des utilisateurs peuvent avoir à engager avec chaque canal.

Par exemple, si vous testez une push, vous pouvez obtenir des résultats significatifs plus rapidement que lors du test de courriel, car les utilisateurs voient les messages pushes immédiatement, mais il peut s'écouler des jours avant qu'ils ne voient ou n'ouvrent un courriel. Si vous testez des messages dans l'application, gardez à l'esprit que les utilisateurs doivent ouvrir l'application pour voir la campagne, donc vous devriez attendre plus longtemps afin de recueillir les résultats de vos ouvertures d'applications les plus actives ainsi que de vos utilisateurs les plus ordinaires.

Si vous n'êtes pas sûr de la durée de votre test, la fonctionnalité [Sélection intelligente][272] peut être utile pour trouver une variante gagnante efficacement.

### Choix d'un segment {#choosing-a-segment}

Puisque différents segments de vos utilisateurs peuvent répondre différemment à la messagerie, le succès d'un message particulier dit quelque chose à la fois sur le message lui-même et sur son segment cible. Par conséquent, essayez de concevoir un test en gardant à l'esprit votre segment cible.

Par exemple, alors que les utilisateurs actifs peuvent avoir des taux de réponse égaux à « Cette transaction expire demain ! » et « Cette transaction expire dans 24 heures ! , les utilisateurs qui n'ont pas ouvert l'application pendant une semaine peuvent être plus réceptifs à ce dernier libellé car il crée un plus grand sens de l'urgence.

De plus, lors du choix du segment sur lequel exécuter votre test, Assurez-vous de vérifier si la taille de ce segment sera suffisamment grande pour votre test. En général, les tests multivariés et A/B avec un plus grand nombre de variantes nécessitent un plus grand groupe de tests pour obtenir des résultats statistiquement significatifs. Ceci est dû au fait que plus de variantes auront pour conséquence que moins d'utilisateurs verront chaque variante individuelle.

{% alert tip %}
À titre de guide brut, vous aurez probablement besoin d'environ 15 000 utilisateurs par variante (y compris le contrôle) pour obtenir 95% de confiance dans vos résultats de test. Cependant, le nombre exact d'utilisateurs dont vous avez besoin pourrait être supérieur ou inférieur à celui qui dépend de votre cas particulier. Pour une orientation plus exacte sur les tailles d'échantillons de variantes, envisagez de vous référer à [Calculateur de taille d'échantillon d'optimisation](https://www.optimizely.com/resources/sample-size-calculator/).
{% endalert %}

## Suivi recommandé {#recommended-follow-ups}

Un test multivarié et A/B peut (et devrait être !) inspirer des idées pour de futurs tests, ainsi que vous guider vers des changements dans votre stratégie de messagerie. Les actions de suivi possibles incluent les éléments suivants :

**Changez votre stratégie de messagerie en fonction des résultats de test**<br> Vos résultats multivariés peuvent vous conduire à modifier la façon dont vous parlez ou formatez votre messagerie.

**Changez la façon dont vous comprenez vos utilisateurs**<br> Chaque test fera la lumière sur les comportements de vos utilisateurs, comment les utilisateurs réagissent aux différents canaux de messagerie et les différences (et similaires) entre vos segments.

**Améliore la façon dont vous structurez les tests futurs**<br> Votre taille d'échantillon était-elle trop petite ? Les différences entre vos variantes étaient-elles trop subtiles ? Chaque test offre l’occasion d’apprendre comment améliorer les tests futurs. Si votre confiance est faible, la taille de votre échantillon est trop petite et devrait être agrandie pour de futurs tests.  Si vous ne trouvez pas de différence claire entre la façon dont vos variantes ont été effectuées, il est possible que les différences soient trop subtiles pour avoir un effet perceptible sur les réponses des utilisateurs.

**Exécuter un test de suivi avec une taille d'échantillon plus grande**<br> Des échantillons plus grands augmenteront les chances de détecter de petites différences entre les variantes.

**Exécuter un test de suivi en utilisant un canal de messagerie différent**<br> Si vous trouvez qu'une stratégie particulière est très efficace dans un canal, vous voudrez peut-être tester cette stratégie dans d'autres canaux.  Si un type de message est efficace dans un canal mais n'est pas efficace dans un autre, vous pouvez peut-être conclure que certains canaux sont plus propices à certains types de messages.  Ou peut-être y a-t-il une différence entre les utilisateurs qui sont plus susceptibles d'activer les notifications push et ceux qui sont plus susceptibles de prêter attention aux messages dans l'application.  En fin de compte, exécuter ce type de test vous aidera à apprendre comment votre public interagit avec vos différents canaux de communication.

**Exécuter un test de suivi sur un segment différent d'utilisateurs**<br> Pour faire cela, créer un autre test avec le même canal de messagerie et les mêmes variantes, mais choisir un segment différent des utilisateurs.  Par exemple, si un type de messagerie était extrêmement efficace pour les utilisateurs engagés, il peut être utile d'étudier son effet sur les utilisateurs en retard. Il est possible que les utilisateurs obsolètes répondent de la même manière, ou ils préfèrent peut-être une autre variante.  Ce type de test vous aidera à en savoir plus sur vos différents segments et comment ils répondent à différentes sortes de messages.  Pourquoi faire des hypothèses sur vos segments quand vous pouvez baser votre stratégie sur des données ?

**Effectuez un test de suivi basé sur les connaissances d'un test précédent**<br> Utilisez les aperçus que vous avez récoltés lors des tests passés pour guider vos futurs tests. Est-ce qu'un test précédent indique qu'une technique de messagerie est plus efficace ? Vous n'êtes pas sûr de quel aspect spécifique d'une variante l'a amélioré? Exécuter des tests de suivi basés sur ces questions vous aidera à générer des conclusions perspicaces sur vos utilisateurs.

**Comparer l'impact à long terme de différentes variantes**<br> Si vous testez des messages de réengagement A/B n'oubliez pas de comparer l'impact à long terme de différentes variantes via [Rapports de conservation]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/retention_reports/). Vous pouvez utiliser les rapports de rétention pour analyser l'impact de chaque variante sur le comportement de l'utilisateur des jours de votre choix semaines, un mois après le reçu du message, et voir s'il y a un ascenseur.
[160]: {% image_buster /assets/img/ab_create_1.png %} [170]: {% image_buster /assets/img/ab_create_2. ng %} [180]: {% image_buster /assets/img/ab_create_4.png %} [210]: {% image_buster /assets/img/ab_create_8.png %}

[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events

[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[70]: #tips-different-channels
[80]: #choosing-a-segment
[175]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/
[272]: #intelligent-selection
[273]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/
[intelselection]: {{site.baseurl}}/user_guide/intelligence/intelligent_selection/
[confidence]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/#understanding-confidence
