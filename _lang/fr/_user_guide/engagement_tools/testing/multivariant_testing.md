---
nav_title: Test A/B et multivarié
article_title: Test A/B et multivarié
page_order: 2
page_type: reference
description: "Cet article de référence explique ce que sont les tests A/B et multivariés, leurs avantages et comment les créer avec Braze."

---
# Test A/B et multivarié

Les tests multivariés et A/B peuvent être rapidement utilisés à l’aide de notre fonction [Sélection intelligente]({{site.baseurl}}/user_guide/intelligence/intelligent_selection/).

## En quoi consiste les tests A/B et multivariés ?

Un test A/B est une expérience qui compare les réponses des utilisateurs à plusieurs versions de la même campagne marketing. Ces versions partagent des objectifs marketing similaires, mais diffèrent en termes de formulation et de style.

L’objectif est d’identifier la version de la campagne qui remplit le mieux vos objectifs marketing. Dans cette section, nous examinerons comment tester l’efficacité des différences de contenu.

{% alert note %}
Si vous souhaitez évaluer les différences dans la programmation ou le timing des messages (par exemple, la différence entre envoyer un message de panier abandonné après une heure d’inactivité ou un jour d’inactivité), consultez notre section sur la configuration des [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
{% endalert %}

Supposons que vous ayez deux options pour une notification push :

- « Cette offre expire demain !"
- « Cette offre expire dans 24 heures !"

À l’aide d’un test A/B, vous pouvez voir quelle formulation produit le taux de conversion le plus élevé. Ainsi, la prochaine fois que vous envoyez une notification push à propos d’une offre, vous saurez quel type de formulation est le plus efficace.

Ce type de test examine uniquement l’effet d’une variable, c’est-à-dire le texte d’une notification push. Un test multivarié est similaire, mais il teste les effets de deux variables ou plus. Une autre variable que nous pourrions tester est d’inclure un émoji à la fin du message. Nous allons maintenant tester deux variables (à ne pas confondre avec les variantes), d’où le terme « multivarié ». Pour ce faire, nous allons tester quatre versions du message : deux options pour le texte multipliées par deux options pour les émojis (avec et sans émoji), soit un total de quatre variantes du message.

Dans la documentation de Braze, « test multivarié » est utilisé de manière interchangeable avec « test A/B ».

## Avantages des tests A/B et multivariés {#the-benefits-of}

Les tests A/B et multivariés sont un excellent moyen pour comprendre facilement et clairement votre audience. Grâce à ce type de tests, vous n’avez plus besoin de deviner ce qui fonctionnera le mieux auprès de vos utilisateurs ; chaque campagne devient une opportunité d’essayer plusieurs variantes d’un message et d’évaluer les réactions de votre audience.

Voici quelques scénarios dans lesquels les tests A/B et multivariés pourraient être utiles :

- **Lorsque vous essayez un type de message pour la première fois :** Vous n’êtes pas sûr(e) de proposer les bons messages in-app dès la première fois ? Les tests multivariés vous permettent d’expérimenter et d’apprendre ce qui fonctionne le mieux auprès de vos utilisateurs.
- **Lorsque vous créez des campagnes d’onboarding et d’autres campagnes qui sont envoyées de manière continue :** Étant donné que la plupart de vos utilisateurs recevront cette campagne, pourquoi ne pas faire en sorte qu’elle soit aussi efficace que possible ?
- **Lorsque vous avez plusieurs idées de message :** Si vous n’êtes pas sûr(e) de savoir quel message vous devriez choisir, lancez un test et prenez une décision en vous basant sur les données recueillies.
- **Lorsque vous essayez de savoir si des techniques marketing éprouvées seront efficaces pour vos utilisateurs :**  Les marketeurs suivent souvent des tactiques conventionnelles pour interagir avec leurs utilisateurs, mais la base utilisateur de chaque produit est différente. Parfois, le fait de renvoyer des messages d’appel à l’action ou d’utiliser des preuves sociales ne vous donnera pas les résultats escomptés. Les tests A/B et multivariés vous permettent de sortir des sentiers battus et de découvrir des tactiques non conventionnelles qui fonctionnent auprès de votre audience.

## Cinq règles pour les tests A/B et multivariés {#five-rules-for}

Les tests A/B et multivariés peuvent révéler d’importantes informations sur vos utilisateurs. Suivez les directives ci-dessous pour vous assurer que les résultats de votre test reflètent vraiment les comportements de vos utilisateurs :

1. **Effectuez le test sur un grand nombre d’utilisateurs.** Les échantillons de grande taille garantissent que vos résultats reflèteront les préférences de votre utilisateur moyen et seront moins susceptibles d’être altérés par des valeurs aberrantes. Ces grands échantillons vous permettent également d’identifier les variantes gagnantes qui ont des marges de réussite plus petites.
2. **Classez les utilisateurs de manière aléatoire dans différents groupes de test.** Les tests multivariés de Braze vous permettent de créer jusqu’à huit groupes de tests sélectionnés de manière aléatoire. La randomisation permet d’éliminer les biais dans les tests et augmente la probabilité que les groupes de tests aient une composition similaire. Cela garantit que les différences de réaction seront dues à des différences dans vos messages plutôt que dans vos échantillons.
3. **Prenez note des éléments vous essayez de tester.** Les tests A/B et multivarié vous permettent de tester les différences entre plusieurs versions d’un message. Dans certains cas, un test simple peut s’avérer le plus efficace. Le fait d’isoler les changements dans votre message vous permet d’identifier les éléments qui ont eu le plus d’impact sur la réaction de vos utilisateurs. Dans d’autres cas, le fait de présenter plus de différences entre les variantes vous permet d’examiner les valeurs aberrantes et de comparer différents ensembles d’éléments. Aucune de ces méthodes n’est nécessairement meilleure que l’autre, à condition que vous sachiez clairement dès le début ce que vous essayez de tester.
4. **Décidez de la durée de votre test avant de le lancer, et n’interrompez pas votre test prématurément !** Les marketeurs sont souvent tentés d’interrompre leurs tests dès que les résultats vont en leur sens, ce qui a pour effet de biaiser les résultats. Résistez à la tentation de jeter un œil aux résultats avant la fin du test et ne terminez jamais votre test prématurément !
5. **Si possible, ajoutez un groupe de contrôle à votre test.** Ajouter un [groupe de contrôle](#including-a-control-group) à votre test vous permet de savoir si le fait d’envoyer un message aura plus d’impact sur le taux de conversion des utilisateurs que de ne pas envoyer de message.

## Créer des tests A/B et multivariés avec Braze {#creating-tests}

### Étape 1 : Créer votre campagne

Cliquez sur **Create Campaign (Créer une campagne)** et sélectionnez un canal pour la campagne dans la section qui prend en charge les tests A/B et multivariés. Pour obtenir des informations détaillées sur chaque canal de messagerie, consultez l’article [Créer une campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/).

![][160]{: style="max-width:30%" }

### Étape 2 : Composer vos variantes

Vous pouvez créer jusqu’à huit variantes de votre message, en changeant les titres, le contenu, les images, etc. Le nombre de différences entre les messages détermine s’il s’agit d’un test multivarié ou A/B : un test A/B examine l’effet lié au changement d’une seule variable, tandis qu’un test multivarié examine deux variables ou plus.

![][170]

Découvrez de nouvelles idées sur la manière de différencier vos variantes en consultant nos [Conseils pour différents canaux][70].

### Étape 3 : Planifier votre campagne

La planification des tests fonctionne comme pour toute autre campagne Braze. Tous les [types de livraison][175] standards de Braze sont disponibles. Cependant, l’option permettant d’envoyer une variante gagnante n’est disponible que lorsque vous planifiez une campagne à envoyer une seule fois pour certains canaux de messagerie.

### Étape 4 : Choisir un segment et répartir vos utilisateurs entre les variantes

Sélectionnez les segments à cibler, puis répartissez leurs membres entre les différentes variantes que vous avez choisies. Pour les campagnes de notification push, d’e-mail et de webhook programmées pour un seul envoi, vous pouvez également garder une partie de vos segments pour leur envoyer la variante gagnante, si nécessaire.

Déterminez quel pourcentage de votre segment cible doit recevoir chacune de vos variantes, faire partie du groupe de contrôle (le cas échéant), et quel pourcentage doit recevoir la variante gagnante une fois le test A/B terminé.

#### Inclure un groupe de contrôle {#including-a-control-group}

Lorsque vous créez un test A/B ou multivarié, vous pouvez réserver un pourcentage de votre audience cible pour créer un groupe de contrôle randomisé. Les utilisateurs du groupe de contrôle ne reçoivent pas le test, mais Braze surveille leur taux de conversion pendant la durée de la campagne.

Lorsque vous visualisez vos résultats, vous pouvez comparer les taux de conversion de vos variantes par rapport au taux de conversion de référence fourni par votre groupe de contrôle. Cela vous permet non seulement de comparer les effets de vos variantes, mais aussi de comparer les effets de vos variantes au taux de conversion que vous obtiendriez si vous n’aviez envoyé aucun message.

La taille du groupe de contrôle d’une campagne avec [Sélection intelligente][intelselection] est basée sur le nombre de variantes. Si chaque variante est envoyée à plus de 20 % des utilisateurs, cela signifie que le groupe de contrôle représente 20 % de votre audience et que les variantes sont réparties uniformément entre les 80 % restants. Cependant, si vous avez plusieurs variantes et que chaque variante est envoyée à moins de 20 % des utilisateurs, le groupe de contrôle doit alors être plus petit. Lorsque la Sélection intelligente commence à analyser les performances de votre test, le groupe de contrôle augmente ou diminue en fonction des résultats.

![Panneau des tests A/B montrant la répartition en pourcentage du groupe de contrôle, de la variante 1, de la variante 2 et de la variante 3 avec 25 % pour chaque groupe.][180]

Pour connaître les meilleures pratiques concernant le choix d’un segment à tester, consultez la section [Choisir un segment][80].

{% alert important %}
Notez qu’il n’est pas recommandé d’utiliser un groupe de contrôle pour trouver la variante gagnante en se basant sur les ouvertures ou les clics. Étant donné que le message n’est pas envoyé au groupe de contrôle, ces utilisateurs ne peuvent pas effectuer d’ouverture ou de clics. Par conséquent, le taux de conversion de ce groupe est de 0 % par définition et ne peut être comparé avec les variantes.
{% endalert %}

#### Envoi de la variante gagnante

Pour les campagnes de notification push, d’e-mail et de webhook programmées pour un seul envoi, vous pouvez également garder une partie de votre audience pour l’inclure dans le groupe « variante gagnante ». Les utilisateurs de ce groupe recevront la variante gagnante une fois le test A/B terminé.

![Un exemple de variante gagnante dans le cadre d’une campagne de notification push, d’e-mail ou de webhook avec test A/B.][10]

Indiquez quel pourcentage de l’audience de votre campagne doit être affecté au groupe de la variante gagnante, puis configurez les paramètres d’envoi suivants :

- Ce qui détermine la variante gagnante
- Lorsque le test A/B commence
- Lorsque le test A/B se termine
- Que faire si les résultats du test ne sont pas représentatifs sur le plan statistique (abandonner le message ou l’envoyer quand même)

### Étape 5 : Choisir l’action qui détermine la variante gagnante

La variante gagnante peut être mesurée par `Unique Opens` ou `Clicks` pour les campagnes par e-mail, `Opens` pour les campagnes de notification push, ou `Primary Conversion Rate` pour tous les canaux. Le fait de sélectionner `Opens` ou `Clicks` pour déterminer la variante gagnante n’affecte pas les [événements de conversion][2] que vous choisissez pour la campagne.

N’oubliez pas que si vous utilisez un groupe de contrôle, les utilisateurs du groupe de contrôle ne peuvent pas effectuer d’`Opens` ou de `Clicks`, la « performance » du groupe de contrôle sera donc systématiquement `0`. Par conséquent, le groupe de contrôle ne peut pas gagner le test A/B. Cependant, vous pouvez toujours utiliser un groupe de contrôle afin de suivre d’autres mesures pour les utilisateurs qui ne reçoivent pas de message.

### Étape 6 : Programmer quand envoyer la variante gagnante

Choisissez une date et une heure à laquelle la variante gagnante doit être envoyée.

{% alert note %}
Si la variante gagnante est envoyée en fonction de l’heure locale des utilisateurs ou avec la fonction Timing Intelligent, celle-ci doit être envoyée au moins 24 heures après le test A/B afin de s’assurer que tous les utilisateurs du groupe de la variante gagnante la reçoivent.
{% endalert %}

Dans le menu déroulant qui se trouve après la date, vous pouvez également choisir si vous souhaitez ou non envoyer la variante la plus performante, même si elle ne gagne pas par une marge significative d’un point de vue statistique.

#### (Facultatif) Désigner un événement de conversion

Définir un événement de conversion pour une campagne vous permet de voir combien de destinataires de la campagne ont effectué une action donnée après réception.

Cela affecte uniquement le test si vous avez sélectionné **Primary Conversion Rate (Taux de conversion primaire)** aux étapes précédentes. Pour plus d’informations, consultez l’article sur les [Événements de conversion][2]. 

### Étape 7 : Vérifier et lancer le test

Sur la page de confirmation, vérifiez les informations de votre campagne multivariée et lancez le test une fois terminé !

## Consulter les résultats d’une campagne multivariée

Une fois votre campagne lancée, vous pouvez vérifier la performance de chaque variante en sélectionnant votre campagne dans la section **Campaigns (Campagnes)** du tableau de bord. Lorsque la campagne de test est terminée, vous pouvez consulter un résumé des performances de chaque variante et savoir si le test a renvoyé une variante gagnante.

Si une variante a surpassé toutes les autres avec un niveau de [confiance][confidence] de plus de 95 %, Braze marquera cette variante avec une bannière « Winner (Gagnante) ». Si aucune variante ne surpasse les autres avec un niveau de confiance de 95 % et que vous avez choisi tout de même d’envoyer la variante ayant obtenu les meilleurs résultats, la « meilleure » variante sera envoyée et marquée avec une étiquette indiquant « Sent as Winning Variant (Envoyée comme variante gagnante) ».

Sur la page des analyses, vous pouvez également suivre les performances de la variante gagnante tout au long de la campagne (y compris les envois liés au test A/B).

![][210]

{% alert note %}
Braze compare toutes les variantes entre elles en utilisant le [test du χ² de Pearson](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test). Ce test mesure si une variante dépasse ou non toutes les autres sur le plan statistique avec un niveau d’importance de p < 0,05 (ou ce que nous appelons une importance de 95 %). Si c’est le cas, la variante gagnante reçoit alors l’étiquette « Winner (Gagnante) ».
<br><br>Ce test est différent du score de confiance, qui décrit uniquement la performance d’une variante par rapport au groupe de contrôle avec une valeur numérique comprise entre 0 et 100 %.
{% endalert %}

Une variante peut fournir de meilleurs résultats que le groupe de contrôle, mais le test du χ² vérifie si une variante est meilleure que tous les autres. Des [tests de suivi](#recommended-follow-ups) peuvent apporter davantage d’informations.

### Comprendre le niveau de confiance {#understanding-confidence}

Une partie importante de vos résultats est la confiance dans l’exactitude de vos résultats. Par exemple, que se passe-t-il si le groupe de contrôle avait un taux de conversion de 20 % et que la variante A avait un taux de conversion de 25 % ? Cela indique qu’il est préférable d’envoyer la variante A que de n’envoyer aucun message. Avoir une confiance de 95 % signifie que la différence entre les deux taux de conversion est probablement due à une différence réelle dans les réactions des utilisateurs et qu’il n’y a qu’une probabilité de 5 % que la différence se soit produite par hasard.

Braze compare le taux de conversion de chaque variante avec le taux de conversion du groupe de contrôle via une procédure statistique appelée [Test&nbsp;Z](https://en.wikipedia.org/wiki/Z-test). Un résultat de 95 % de confiance ou plus, comme dans l’exemple précédent, indique que la différence est significative sur le plan statistique. Cela est vrai pour toutes les mesures de confiance du tableau de bord de Braze qui décrivent la différence entre deux messages ou populations d’utilisateurs.

En général, une confiance d’au moins 95 % est nécessaire pour montrer que vos résultats reflètent bien les préférences réelles des utilisateurs, et qu’ils ne sont pas simplement dus au hasard. Dans des tests scientifiques rigoureux, le pourcentage de confiance de 95 % (ou autrement appelé la valeur « p », qui est inférieure à 0,05) est la référence utilisée pour déterminer la pertinence statistique. Si vous ne parvenez pas à obtenir une confiance de 95 %, essayez d’augmenter la taille de votre échantillon ou de diminuer le nombre de variantes. 

La confiance ne permet pas de déterminer si une variante est meilleure que les autres. Il s’agit simplement d’une mesure qui évalue à quel point nous sommes sûrs que les deux taux de conversion (ou plus) sont réellement différents les uns des autres. Il s’agit uniquement d’une fonction de la taille de l’échantillon et des différences entre les taux de conversion apparents. Le degré des taux globaux n’affecte pas la fiabilité de la mesure de confiance. Une variante peut avoir un taux de conversion très différent d’une autre sans forcément atteindre une confiance de 95 %. Il est également possible que deux ensembles de variantes aient des taux de conversion ou d’augmentation similaires, mais un niveau de confiance différent.

{% details Statistically insignificant results %}

Un test peut fournir des informations importantes même si son niveau de confiance est inférieur à 95 %. Voici quelques éléments à prendre en compte lorsque les résultats d’un test ne sont pas significatifs sur le plan statistique :

- Il est possible que toutes vos variantes aient eu le même effet. En prenant cela en compte, vous évitez de perdre du temps à effectuer ces changements. Vous pourrez parfois vous rendre compte que les tactiques marketing classiques, comme renvoyer votre appel à l’action, ne fonctionnent pas nécessairement avec votre audience.
- Bien que vos résultats aient pu être dus au hasard, ils peuvent tout de même vous aider à formuler une hypothèse pour votre prochain test. Si plusieurs variantes semblent avoir plus ou moins les mêmes résultats, testez-les de nouveau en ajoutant de nouvelles variantes pour voir s’il existe une alternative plus efficace. Si une variante obtient de meilleurs résultats, mais pas par une marge considérable, vous pouvez effectuer un autre test en accentuant la différence de cette variante.
- Continuez à tester des variantes ! Un test dont les résultats ne sont pas probants doit vous amener à vous poser certaines questions. N’y a-t-il eu vraiment aucune différence entre vos variantes ? Auriez-vous dû structurer votre test différemment ? Vous pouvez répondre à ces questions en effectuant des tests de suivi.
- Bien que les tests soient utiles pour découvrir quel type de message génère la plus forte réaction auprès de votre audience, il est également important de comprendre quels changements dans le message ont eu un effet négligeable.  Cela vous permet soit de poursuivre vos tests pour trouver une alternative plus efficace, soit de gagner du temps que vous auriez passé à choisir entre deux messages alternatifs.

Que votre test ait ou non un grand gagnant, il peut être utile d’effectuer un test de suivi pour confirmer vos résultats ou appliquer ces résultats à un scénario légèrement différent.

{% enddetails %}

### Conseils pour différents canaux {#tips-different-channels}

Vous pouvez tester différents composants de votre message en fonction du canal que vous avez choisi. Essayez de créer des variantes en ayant une idée de ce que vous voulez tester et de ce que vous espérez prouver.

Quels leviers devez-vous utiliser et quels sont les effets souhaités ? Bien qu’il existe des millions d’éléments à étudier à l’aide d’un test A/B ou multivarié, nous avons réuni quelques suggestions pour vous aider à démarrer :

| Canal | Aspects du message que vous pouvez modifier | Résultats à rechercher |
| ---------------------| --------------- | ------------- |
| Notification push | Texte <br> Utilisation des images et des émojis <br> Liens profonds <br> Présentation des chiffres (par ex. « triple » contre « augmentation de 200 % ») <br> Présentation de la durée (p. ex. « se termine à minuit » par rapport à « se termine dans 6 heures ») | Ouvertures <br> Taux de conversion |
| E-mail | Sujet <br> Nom affiché <br> Formule de politesse <br> Corps du message <br> Utilisation des images et des émojis <br> Présentation des chiffres (par ex. « triple » contre « augmentation de 200 % ») <br> Présentation de la durée (p. ex. « se termine à minuit » par rapport à « se termine dans 6 heures ») | Ouvertures <br> Taux de conversion |
| Notification dans l’application | Aspects listés pour « notifications push » <br> [Format du message][273] | Clics <br> Taux de conversion |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert tip %}
Lorsque vous effectuez des tests A/B, n’oubliez pas de générer des [rapports d’entonnoir]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/funnel_reports/) afin de comprendre comment chaque variante a affecté votre entonnoir de conversion, surtout si cette « conversion » implique pour vous de prendre plusieurs mesures ou actions.
{% endalert %}

De plus, la longueur idéale de votre test peut également varier en fonction du canal. Gardez à l’esprit la durée moyenne dont la plupart des utilisateurs peuvent avoir besoin pour interagir avec chaque canal.

Par exemple, si vous testez une notification push, vous pouvez obtenir des résultats probants plus rapidement qu’en testant des e-mails, car les utilisateurs voient immédiatement les notifications push, alors qu’ils peuvent mettre plusieurs jours à voir et ouvrir un e-mail. Si vous testez des messages dans l’application, gardez à l’esprit que les utilisateurs doivent ouvrir l’application pour voir la campagne, il est donc préférable d’attendre plus longtemps avant de recueillir les résultats concernant les personnes qui ouvrent le plus souvent l’application et vos utilisateurs type.

Si vous n’êtes pas sûr de la durée de votre test, la [Sélection intelligente][272] peut vous aider à trouver rapidement une variante gagnante.

### Choisir un segment {#choose-a-segment}

Étant donné que différents segments d’utilisateurs peuvent réagir différemment à votre message, la réussite d’un message donné révèle quelque chose à la fois sur le message lui-même et sur son segment cible. Essayez donc de créer un test en pensant à votre segment cible.

Par exemple, même si les utilisateurs actifs peuvent réagir de la même manière à « Cette offre se termine demain ! » et « Cette offre se termine dans 24 heures ! », les utilisateurs qui n’ont pas ouvert l’application pendant une semaine peuvent être plus réceptifs à la deuxième formulation, car elle crée un plus grand sentiment d’urgence.

Par ailleurs, lorsque vous choisissez un segment à tester, assurez-vous que la taille de ce segment sera suffisamment grande pour votre test. En général, les tests A/B et multivariés qui comportent un plus grand nombre de variantes nécessitent un groupe de test plus grand pour obtenir des résultats probants sur le plan statistique. En effet, plus le nombre de variantes est important, plus le nombre d’utilisateurs voyant chaque variante sera réduit.

{% alert tip %}
À titre de référence, vous aurez probablement besoin d’environ 15 000 utilisateurs par variante (y compris le groupe de contrôle) pour obtenir une confiance de 95 % dans vos résultats de test. Cependant, le nombre exact d’utilisateurs dont vous aurez besoin pourrait être supérieur ou inférieur en fonction de la situation. Pour obtenir des conseils plus précis sur la taille des échantillons pour les tests de variantes, utilisez le [Calculateur de taille d’échantillon d’Optimizely](https://www.optimizely.com/resources/sample-size-calculator/).
{% endalert %}

## Actions de suivi recommandées {#recommended-follow-ups}

Un test A/B ou multivarié peut (et devrait !) vous donner des idées pour vos prochains tests, et vous inciter à réorienter votre stratégie de communication. Voici quelques exemples d’actions de suivi :

**Modifier votre stratégie de communication en fonction des résultats des tests**<br>
Vos résultats multivariés peuvent vous amener à changer la façon dont vous formulez ou formatez votre message.

**Modifier votre compréhension de vos utilisateurs**<br>
Chaque test apportera des informations sur les comportements de vos utilisateurs, la manière dont ils réagissent face à différents canaux de communication et les différences (et similarités) entre vos segments.

**Améliorer la façon dont vous structurez vos prochains tests**<br>
Votre échantillon était-il trop petit ? Les différences entre vos variantes étaient-elles trop subtiles ? Chaque test est une occasion d’améliorer les suivants. Si votre confiance est faible, cela signifie que la taille de votre échantillon est trop petite et qu’il doit être agrandi lors des prochains tests.  Si vous n’observez aucune différence notable entre les résultats de vos variantes, il est possible que les différences aient été trop subtiles pour avoir un effet discernable par rapport aux réactions des utilisateurs.

**Effectuer un test de suivi avec un plus grand échantillon**<br>
Les échantillons de grande taille augmentent le risque de détecter de petites différences entre les variantes.

**Effectuer un test de suivi en utilisant un autre canal de communication**<br>
Si vous constatez qu’une stratégie donnée est très efficace pour un canal, vous pouvez tester cette stratégie avec d’autres canaux.  Si un type de message est efficace dans un canal, mais pas dans un autre, vous pouvez raisonnablement conclure que certains canaux sont plus propices à certains types de messages.  Ou bien, il existe peut-être une différence entre les utilisateurs qui sont plus susceptibles d’activer les notifications push et ceux qui sont plus susceptibles de prêter attention aux messages dans l’application.  En fin de compte, ce type de test vous aidera à découvrir comment votre audience interagit avec vos différents canaux de communication.

**Effectuer un test de suivi sur un autre segment d’utilisateurs**<br>
Pour ce faire, créez un autre test avec le même canal de communication et les mêmes variantes, mais choisissez un segment d’utilisateurs différent.  Par exemple, si un type de message était extrêmement efficace auprès des utilisateurs actifs, il peut être utile d’enquêter sur son effet auprès des utilisateurs inactifs. Les utilisateurs inactifs pourraient réagir de manière similaire ou préférer une des autres variantes.  Ce test vous aidera à en savoir plus sur vos différents segments et sur la manière dont ils réagissent à différents types de messages.  Pourquoi formuler des hypothèses sur vos segments lorsque vous pouvez baser votre stratégie sur les données ?

**Effectuer un test de suivi basé sur les informations issues d’un test précédent**<br>
Utilisez les informations issues de vos tests passés pour mieux orienter vos futurs projets. L’un de vos précédents tests semble-t-il indiquer qu’une technique de communication est plus efficace que les autres ? Quel élément de la variante gagnante l’a rendu plus efficace ? Baser vos tests de suivi sur ces questions vous aidera à obtenir des résultats pertinents sur vos utilisateurs.

**Comparer l’impact à long terme de différentes variantes**<br>
Si vous menez un test A/B sur des messages de ré-engagement, n’oubliez pas de comparer l’impact à long terme de différentes variantes dans les [Rapports de rétention]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/retention_reports/). Vous pouvez utiliser les rapports de rétention pour analyser la façon dont chaque variante a affecté le comportement des utilisateurs sur une période de plusieurs jours ou semaines, ou même un mois après réception du message, et voir s’il y a une augmentation.

[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[70]: #tips-different-channels
[80]: #choosing-a-segment
[160]: {% image_buster /assets/img/ab_create_1.png %}
[170]: {% image_buster /assets/img/ab_create_2.png %}
[175]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/
[180]: {% image_buster /assets/img/ab_create_4.png %}
[210]: {% image_buster /assets/img/ab_create_8.png %}
[10]: {% image_buster /assets/img/ab_send_winning_variant.png %}
[272]: #intelligent-selection
[273]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/
[intelselection]: {{site.baseurl}}/user_guide/intelligence/intelligent_selection/
[confidence]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/#understanding-confidence
