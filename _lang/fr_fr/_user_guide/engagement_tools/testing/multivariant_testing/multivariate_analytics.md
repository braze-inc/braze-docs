---
nav_title: Analyse/analytique (si utilisé comme adjectif)
article_title: Analyse/analytique des tests multivariés et A/B (si utilisé comme asjectif)
page_order: 10
page_type: reference
description: "Cet article explique comment visualiser et interpréter les résultats d'une campagne multivariée ou A/B."
---

# Analyse/analytique des tests multivariés et A/B (si utilisé comme asjectif)

> Cet article explique comment afficher les résultats d'un test multivarié ou d'un test A/B. Si vous n'avez pas encore mis en place votre test, reportez-vous à la section [Création de tests multivariés et de tests A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) pour en connaître les étapes.

Une fois votre campagne lancée, vous pouvez vérifier les performances de chaque variante en sélectionnant votre campagne dans la section **Campagnes** du tableau de bord. 

## Analyse/analytique par option d'optimisation (si utilisée en tant qu'adjectif)

Votre vue d'analyse/analytique variera selon que vous avez sélectionné ou non une [optimisation]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) lors de votre configuration initiale.

### Pas d'optimisation

Si vous avez sélectionné **Pas d'optimisation** lors de l'implémentation de votre campagne, votre vue d'analyse restera la même. La page **Analyse/analytique de** votre campagne montrera les performances de vos variantes par rapport à votre groupe de contrôle (si vous en avez inclus un).

!section Performance de l'Analyse/analytique de campagne pour une campagne e-mail avec plusieurs variantes. Le tableau répertorie divers indicateurs de performance pour chaque variante, tels que les destinataires, les rebonds, les clics et les conversions.]({% image_buster /assets/img_archive/ab_analytics_no_optimization.png %})

Pour plus de détails, reportez-vous à l'article sur [l'analyse/analytique de campagne]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) correspondant à votre canal de communication.

### Variante gagnante

Si vous avez sélectionné **Variante gagnante** pour votre optimisation lors de la configuration de votre campagne, vous avez accès à un onglet supplémentaire de l'analyse de votre campagne appelé **Résultat du test A/B.** Après l'envoi de la variante gagnante aux utilisateurs restants de votre test, cet onglet présente les résultats de cet envoi.

Le **résultat du test A/B** est divisé en deux onglets : **Test initial** et **variante gagnante**.

{% tabs local %}
{% tab Initial Test %}

L'onglet **Test initial** présente les indicateurs de chaque variante du test A/B initial envoyé à une partie de votre segmentation cible. Vous pouvez consulter un résumé des performances de toutes les variantes et savoir s'il y a eu ou non un vainqueur au cours du test.

Si une variante surpasse toutes les autres avec un [taux de confiance]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#understanding-confidence) supérieur à 95 %, Braze marque cette variante d'un label "Gagnant".

Si aucune variante ne surpasse toutes les autres avec un niveau de confiance de 95 % et que vous choisissez d'envoyer quand même la variante la plus performante, celle-ci sera quand même envoyée et indiquée avec le label "Gagnant".

Résultats d'un premier test envoyé pour déterminer la variante gagnante, où aucune variante n'a obtenu de meilleurs résultats que les autres avec suffisamment de confiance pour atteindre le seuil de confiance de 95 % pour la signification statistique.]({% image_buster /assets/img_archive/ab_analytics_wv_insufficient_confidence.png %})

#### Comment la variante gagnante est-elle sélectionnée ?

Braze teste toutes les variantes les unes par rapport aux autres à l'aide de [tests du chi-carré de Pearson](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test). Cela permet de déterminer si une variante est statistiquement plus performante que toutes les autres à un niveau de signification de p < 0,05, ou ce que nous appelons la signification à 95 %. Si c'est le cas, la variante gagnante est indiquée par le label "Gagnant".

Il s'agit d'un test distinct du score de confiance, qui décrit uniquement la performance d'une variante par rapport au contrôle avec une valeur numérique comprise entre 0 et 100 %.

Une variante peut faire mieux que le groupe de contrôle, mais le test du chi carré permet de vérifier si une variante est meilleure que toutes les autres. Des [tests de suivi](#recommended-follow-ups) peuvent apporter plus de détails.

{% endtab %}
{% tab Winning Variant %}

L'onglet **Variante gagnante** montre les résultats du deuxième envoi, où chaque utilisateur restant a reçu la variante la plus performante du test initial. Votre **% d'audience** correspondra au pourcentage du segment cible que vous avez réservé au groupe de la variante gagnante.

Les résultats de la variante gagnante sont envoyés au groupe de la variante gagnante.]({% image_buster /assets/img_archive/ab_analytics_wv_1.png %})

{% endtab %}
{% endtabs %}

Si vous souhaitez voir les performances de la variante gagnante tout au long de la campagne, y compris les envois des tests A/B, consultez la page **Analyse de la campagne.** 

### Variante personnalisée {#personalized-variant}

Si vous avez sélectionné **Variante personnalisée** pour votre optimisation lors de l'implémentation de votre campagne, le **résultat du test A/B** est divisé en deux onglets : **Test initial** et **variante personnalisée**.

{% tabs local %}
{% tab Initial Test %}

L'onglet **Test initial** présente les indicateurs de chaque variante du test A/B initial envoyé à une partie de votre segmentation cible.

Résultats d'un test initial envoyé pour déterminer la variante la plus performante pour chaque utilisateur. Un tableau présente les performances de chaque variante en fonction de divers indicateurs pour le canal cible.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_1.png %})

Par défaut, le test recherche des associations entre les événements personnalisés de l'utilisateur et ses préférences en matière de variantes de messages. Cette analyse permet de déterminer si les événements personnalisés augmentent ou diminuent la probabilité de répondre à une variante de message donnée. Ces relations sont ensuite utilisées pour déterminer quels utilisateurs reçoivent quelle variante de message lors de l'envoi final.

Les relations entre les événements personnalisés et les préférences de message sont affichées dans le tableau de l'onglet **Envoi initial**.

\![]({% image_buster /assets/img_archive/ab_analytics_pv_3.png %})

Si le test ne parvient pas à établir une relation significative entre les événements personnalisés et les préférences variantes, il reviendra à une méthode d'analyse basée sur les sessions.

{% details Fallback analysis method %}

**Méthode d'analyse par session**<br>
Si la méthode de repli est utilisée pour déterminer les variantes personnalisées, l'onglet **Test initial** présente une répartition des variantes préférées des utilisateurs en fonction d'une combinaison de certaines caractéristiques. 

Ces caractéristiques sont les suivantes

- **Récence :** Date de la dernière session
- **Fréquence :** La fréquence des sessions
- **Durée du mandat :** Depuis combien de temps est-il utilisateur ?

Par exemple, le test peut révéler que la plupart des utilisateurs préfèrent la variante A, mais que les utilisateurs qui ont eu une session il y a environ 3 à 12 jours, qui ont un intervalle de 1 à 12 jours entre les sessions et qui ont été créés au cours des 67 à 577 derniers jours ont tendance à préférer la variante B. Par conséquent, les utilisateurs de cette sous-population ont reçu la variante B lors du deuxième envoi, tandis que les autres ont reçu la variante A.

Le tableau des caractéristiques des utilisateurs, qui indique quels utilisateurs sont prédisposés à préférer la variante A et la variante B en fonction des trois compartiments dans lesquels ils se situent pour la récurrence, la fréquence et l'ancienneté.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_2.png %})

**Comment les variantes personnalisées sont-elles sélectionnées ?**<br>
Avec cette méthode, le message recommandé à un utilisateur individuel est la somme des effets de sa récence, de sa fréquence et de son ancienneté. La récurrence, la fréquence et l'ancienneté sont réparties en compartiments, comme l'illustre le tableau des **caractéristiques de l'utilisateur**. L'intervalle de temps de chaque compartiment est déterminé par les données des utilisateurs de chaque campagne individuelle et changera d'une campagne à l'autre. 

Chaque compartiment peut avoir une contribution ou une "poussée" différente pour chaque variante de message. La force de la poussée pour chaque compartiment est déterminée à partir des réponses des utilisateurs lors de l'envoi initial à l'aide d'une [régression logistique](https://en.wikipedia.org/wiki/Logistic_regression). Ce tableau ne fait que résumer les résultats en affichant la variante avec laquelle les utilisateurs de chaque compartiment ont eu tendance à s'engager. La variante personnalisée réelle de chaque utilisateur dépend de la somme des effets des trois compartiments dans lesquels il se trouve - un pour chaque caractéristique.

{% enddetails %}

{% endtab %}
{% tab Personalized Variant %}

L'onglet **Variante personnalisée** montre les résultats du deuxième envoi, où chaque utilisateur restant a reçu la variante avec laquelle il était le plus susceptible de s'engager.

Les trois cartes de cette page montrent votre levée projetée, vos résultats globaux et les résultats projetés si vous aviez envoyé uniquement la variante gagnante à la place. Même s'il n'y a pas de lift, ce qui peut parfois arriver, le résultat est le même que si vous n'envoyez que la variante gagnante (un test A/B traditionnel). 

- **Levée prévue :** L'amélioration de votre indicateur d'optimisation sélectionné pour cet envoi grâce à l'utilisation de variantes personnalisées au lieu d'un test A/B standard (si les utilisateurs restants n'ont reçu que la variante gagnante).
- **Résultats globaux :** Les résultats du deuxième envoi en fonction de l'indicateur d'optimisation que vous avez choisi*(ouvertures uniques*, *clics uniques* ou *événement de conversion principal*).
- **Résultats prévus :** Les résultats projetés du deuxième envoi sur la base de l'indicateur d'optimisation que vous avez choisi, si vous aviez envoyé uniquement la variante gagnante. 

!onglet variante personnalisée pour une campagne optimisée pour des ouvertures uniques. Les cartes indiquent la levée projetée, l'ouverture unique globale (avec la variante personnalisée) et l'ouverture unique projetée (avec la variante gagnante).]({% image_buster /assets/img_archive/ab_analytics_pv_1.png %})

Le tableau de cette page présente les indicateurs pour chaque variante de l'envoi personnalisé de variantes. Le **pourcentage de votre audience** correspond au pourcentage du segment cible que vous avez réservé au groupe de la variante personnalisée.

\![]({% image_buster /assets/img_archive/ab_analytics_pv_2.png %})

{% endtab %}
{% endtabs %}

## Comprendre la confiance {#understanding-confidence}

La confiance est la mesure statistique du degré de certitude qu'une différence dans les données, comme les taux de conversion, est réelle et n'est pas due au hasard.

{% alert note %}
Vous n'avez pas confiance en vos résultats ? La confiance n'apparaîtra que si vous avez un groupe de contrôle.
{% endalert %}

Un élément important de vos résultats est la confiance qu'ils inspirent. Par exemple, que se passerait-il si le groupe de contrôle avait un taux de conversion de 20 % et la variante A un taux de conversion de 25 % ? Cela semble indiquer que l'envoi de la variante A est plus efficace que l'absence de message. Un taux de confiance de 95 % signifie que la différence entre les deux taux de conversion est probablement due à une différence réelle dans les réponses des utilisateurs et qu'il n'y a que 5 % de probabilité que la différence soit due au hasard.

Braze compare le taux de conversion de chaque variante au taux de conversion du témoin à l'aide d'une procédure statistique appelée [test Z.](https://en.wikipedia.org/wiki/Z-test) Un résultat de 95% ou plus de confiance, comme dans l'exemple précédent, indique que la différence est statistiquement significative. Cela est vrai partout où vous voyez une mesure de confiance dans le tableau de bord de Braze qui décrit la différence entre deux messages ou populations d'utilisateurs.

En général, un niveau de confiance d'au moins 95 % est nécessaire pour montrer que vos résultats reflètent les préférences réelles des utilisateurs et ne sont pas dus au hasard. Dans les tests scientifiques rigoureux, un niveau de confiance de 95 % (ou plus communément appelé valeur "p" inférieure à 0,05) est le critère couramment utilisé pour déterminer la signification statistique. Si vous n'arrivez toujours pas à atteindre un niveau de confiance de 95 %, essayez d'augmenter la taille de votre échantillon ou de diminuer le nombre de variantes. 

La confiance ne permet pas de savoir si une variante est meilleure que les autres. Il s'agit uniquement d'une mesure de la certitude que les deux (ou plus) taux de conversion sont réellement différents l'un de l'autre. Cela dépend uniquement de la taille de l'échantillon et des différences entre les taux de conversion apparents. Le fait que les taux globaux soient élevés ou faibles n'affecte pas la force de la mesure de confiance. Il est possible qu'une variante ait un taux de conversion très différent d'une autre sans pour autant que le taux de confiance soit de 95 % ou plus. Il est également possible que deux séries de variantes aient des taux de conversion/levée similaires, mais une confiance différente.

### Résultats statistiquement non significatifs

Un test dont le taux de confiance n'est pas de 95 % peut néanmoins fournir des informations importantes. Voici quelques enseignements que vous pouvez tirer d'un test dont les résultats ne sont pas statistiquement significatifs :

- Il est possible que toutes vos variantes aient eu à peu près le même effet. En sachant cela, vous enregistrez le temps que vous auriez passé à effectuer ces changements. Parfois, vous constaterez que les tactiques marketing classiques, telles que la répétition de votre appel à l'action, ne fonctionnent pas nécessairement pour votre audience.
- Bien que vos résultats puissent être dus au hasard, ils peuvent servir de base à l'hypothèse de votre prochain test. Si plusieurs variantes semblent donner à peu près les mêmes résultats, relancez certaines d'entre elles avec de nouvelles variantes pour voir si vous pouvez trouver une alternative plus efficace. Si une variante obtient de meilleurs résultats, mais pas de manière significative, vous pouvez effectuer un autre test dans lequel la différence de cette variante est plus exagérée.
- Continuez à tester ! Un test dont les résultats ne sont pas significatifs doit conduire à se poser certaines questions. N'y avait-il vraiment aucune différence entre vos variantes ? Auriez-vous dû structurer votre test différemment ? Vous pouvez répondre à ces questions en effectuant des tests de suivi.
- Si les tests sont utiles pour découvrir quel type de message suscite le plus de réactions de la part de votre audience, il est également important de comprendre quelles modifications du message n'ont qu'un effet négligeable. Cela vous permet soit de continuer à tester une autre solution plus efficace, soit d'enregistrer le temps que vous auriez pu passer à choisir entre deux envois de messages différents.

Que votre test aboutisse ou non à un résultat clair, il peut être utile d'effectuer un [test de suivi](#recommended-follow-ups) pour confirmer vos résultats ou appliquer vos conclusions à un scénario légèrement différent.

## Divergences entre le groupe de contrôle et la variante

Dans les campagnes de messages in-app, la façon dont les utilisateurs sont suivis et dont les impressions sont enregistrées peut entraîner des écarts dans la répartition attendue entre le groupe de contrôle et la variante. En effet, les impressions réelles enregistrées peuvent ne pas refléter ce fractionnement, et Braze n'a en définitive aucun contrôle sur le comportement individuel de l'utilisateur qui effectuera le déclenchement.

Par exemple, disons qu'une campagne a une audience cible de 200 utilisateurs au moment du lancement, avec 100 utilisateurs dans le groupe de contrôle et 100 utilisateurs dans la variante.

Les 100 utilisateurs de la variante reçoivent l'envoi du message in-app, et 50 d'entre eux effectuent l'action déclenchante et voient le message in-app. Les 100 utilisateurs du groupe de contrôle ne sont suivis que s'ils effectuent l'action déclenchante de la campagne, et 75 d'entre eux effectuent l'action déclenchante et enregistrent une impression, mais ne voient pas le message in-app.

Malgré la répartition initiale 50/50, les impressions uniques enregistrées ne sont pas équilibrées. Le groupe variante compte 50 impressions, tandis que le groupe contrôle en compte 75.

### Retards dans l'envoi des messages in-app 

Pour les campagnes de messages in-app déclenchés qui comprennent des affichages différés, les impressions du groupe contrôle seront enregistrées au moment où l'utilisateur final aurait initialement reçu le message in-app. Par exemple, si une campagne est réglée pour retarder l'affichage d'une heure, les impressions du groupe de contrôle ne seront pas enregistrées tant que le délai d'une heure ne sera pas écoulé. Cela permet de suivre avec précision les impressions liées au moment prévu pour la réception/distribution du message.

## Suivi recommandé {#recommended-follow-ups}

Un test multivarié et un test A/B peuvent (et doivent !) inspirer des idées pour des tests ultérieurs, et vous guider vers des changements dans votre stratégie d'envoi de messages. Les actions de suivi possibles sont les suivantes :

#### Modifiez votre stratégie d'envoi de messages en fonction des résultats des tests.

Vos résultats multivariés peuvent vous amener à modifier la formulation ou la mise en forme de vos messages.

#### Changez la façon dont vous comprenez vos utilisateurs

Chaque test mettra en lumière les comportements de vos utilisateurs, la façon dont ils réagissent aux différents canaux de communication et les différences (et similitudes) entre vos segments.

#### Améliorez la façon dont vous structurez vos futurs tests

Votre échantillon était-il trop petit ? Les différences entre vos variantes étaient-elles trop subtiles ? Chaque test est l'occasion d'apprendre comment améliorer les tests futurs. Si votre confiance est faible, la taille de votre échantillon est trop petite et doit être augmentée pour les prochains tests. Si vous ne constatez pas de différence claire entre les performances de vos variantes, il est possible que les différences soient trop subtiles pour avoir un effet perceptible sur les réponses des utilisateurs.

#### Effectuer un test de suivi avec un échantillon plus important

Des échantillons plus importants augmenteront les chances de détecter de petites différences entre les variantes.

#### Effectuez un test de suivi en utilisant un canal de communication différent.

Si vous constatez qu'une stratégie particulière est très efficace dans un canal, vous pouvez la tester dans d'autres canaux. Si un type de message est efficace dans un canal et ne l'est pas dans un autre, vous pouvez en conclure que certains canaux sont plus propices à certains types de messages. Ou peut-être existe-t-il une différence entre les utilisateurs qui sont plus susceptibles d'activer les notifications push et ceux qui sont plus susceptibles de prêter attention aux messages in-app. En fin de compte, ce type de test vous permettra de savoir comment votre audience interagit avec vos différents canaux de communication.

#### Effectuez un essai de suivi sur un segment différent d'utilisateurs.

Pour ce faire, créez un autre test avec le même canal de communication et les mêmes variantes, mais choisissez un segment d'utilisateurs différent. Par instance, si un type d'envoi de messages s'est avéré extrêmement efficace pour les utilisateurs engagés, il peut être utile d'étudier son effet sur les utilisateurs non engagés. Il est possible que les anciens utilisateurs réagissent de la même manière ou qu'ils préfèrent une autre variante. Ce test vous permettra d'en savoir plus sur vos différents segments et sur la façon dont ils réagissent aux différents types de messages. Pourquoi faire des hypothèses sur vos segments alors que vous pouvez fonder votre stratégie sur des données ?

#### Exécutez un test de suivi sur la base des informations recueillies lors d'un test précédent.

Utilisez les informations que vous avez recueillies lors des tests précédents pour orienter vos futurs tests. Un test antérieur indique-t-il qu'une technique d'envoi de messages est plus efficace ? Vous n'êtes pas sûr de savoir quel aspect spécifique d'une variante l'a rendue meilleure ? L'exécution de tests de suivi basés sur ces questions vous aidera à générer des informations pertinentes sur vos utilisateurs.

#### Comparer l'impact à long terme de différentes variantes

Si vous effectuez des tests A/B sur les messages de réengagement, n'oubliez pas de comparer l'impact à long terme des différentes variantes à l'aide des [rapports de rétention.]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) Vous pouvez utiliser les rapports de rétention pour analyser l'impact de chaque variante sur le comportement de l'utilisateur de votre choix quelques jours, semaines ou mois après la réception du message, et voir s'il y a une amélioration.
