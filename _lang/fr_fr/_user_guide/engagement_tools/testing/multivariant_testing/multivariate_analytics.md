---
nav_title: Analyse
article_title: Analyses des tests A/B et multivariés
page_order: 10
page_type: reference
description: "Cet article explique comment afficher et interpréter les résultats d’une campagne A/B ou multivariée."
---

# Analyses des tests A/B et multivariés

> Cet article explique comment afficher les résultats d’un test A/B ou multivarié. Si vous n'avez pas encore mis en place votre test, reportez-vous à la section [Création de tests multivariés et de tests A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) pour en connaître les étapes.

Une fois votre campagne lancée, vous pouvez vérifier les performances de chaque variante en sélectionnant votre campagne dans la section **Campagnes** du tableau de bord. 

## Analyses par option d’optimisation

Votre vue d'analyse/analytique variera selon que vous avez sélectionné ou non une [optimisation]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) lors de votre configuration initiale.

### Sans optimisation

Si vous avez sélectionné **Pas d'optimisation** lors de l'implémentation de votre campagne, votre vue analytique restera la même. La page **Analyse/analytique de** votre campagne affichera les performances de vos variantes par rapport à votre groupe de contrôle (si vous en avez inclus un).

![Section performance des analyses de campagne pour une campagne par e-mail avec plusieurs variantes. Le tableau répertorie divers indicateurs de performance pour chaque variante, tels que les destinataires, les rebonds, les clics et les conversions.]({% image_buster /assets/img_archive/ab_analytics_no_optimization.png %})

Pour plus de détails, reportez-vous à l'article [Analyse de campagne]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) correspondant à votre canal de communication.

### Variante gagnante

Si vous avez sélectionné **Variante gagnante** pour votre optimisation lors de la configuration de votre campagne, vous avez accès à un onglet supplémentaire de l'analyse de votre campagne appelé **Résultat du test A/B.** Après l'envoi de la variante gagnante aux utilisateurs restants de votre test, cet onglet présente les résultats de cet envoi.

Le **résultat du test A/B** est divisé en deux onglets : **Test initial** et **variante gagnante**.

{% tabs local %}
{% tab Test initial %}

L'onglet **Test initial** présente les indicateurs de chaque variante du test A/B initial envoyé à une partie de votre segmentation cible. Vous pouvez consulter un résumé des performances de chaque variante et savoir si le test a renvoyé une variante gagnante.

Si une variante surpasse toutes les autres avec un [taux de confiance]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#understanding-confidence) supérieur à 95 %, Braze marque cette variante d'un label "Gagnant".

Si aucune variante ne surpasse les autres avec un niveau de confiance de 95 % et que vous avez choisi tout de même d’envoyer la variante ayant obtenu les meilleurs résultats, la « meilleure » variante sera envoyée et marquée avec une étiquette indiquant « Gagnante ».

![Résultats d'un test initial envoyé pour déterminer la variante gagnante où aucune variante n'a obtenu de meilleurs résultats que les autres avec suffisamment de confiance pour atteindre le seuil de confiance de 95 % pour la signification statistique.]({% image_buster /assets/img_archive/ab_analytics_wv_insufficient_confidence.png %})

#### Comment la variante gagnante est-elle sélectionnée ?

Braze teste toutes les variantes les unes par rapport aux autres à l'aide de [tests du khi-carré de Pearson](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test). Ce test mesure si une variante dépasse ou non toutes les autres sur le plan statistique avec un niveau d’importance de p < 0,05 (ou ce que nous appelons une importance de 95 %). Si c’est le cas, la variante gagnante est indiquée par ’étiquette « Winner (Gagnante) ».

Ce test est différent du score de confiance, qui décrit uniquement la performance d’une variante par rapport au groupe de contrôle avec une valeur numérique comprise entre 0 et 100 %.

Une variante peut fournir de meilleurs résultats que le groupe de contrôle, mais le test du χ² vérifie si une variante est meilleure que tous les autres. Des [tests de suivi](#recommended-follow-ups) peuvent apporter davantage d’informations.

{% endtab %}
{% tab Variante gagnante %}

L'onglet **Variante gagnante** montre les résultats du deuxième envoi, où chaque utilisateur restant a reçu la variante la plus performante du test initial. Votre **% d'audience** correspondra au pourcentage du segment cible que vous avez réservé au groupe de la variante gagnante.

![Résultats de la variante gagnante envoyés au groupe de la variante gagnante.]({% image_buster /assets/img_archive/ab_analytics_wv_1.png %})

{% endtab %}
{% endtabs %}

Si vous souhaitez voir les performances de la variante gagnante tout au long de la campagne, y compris les envois des tests A/B, consultez la page **Analyse de la campagne.** 

### Variante personnalisée {#personalized-variant}

Si vous avez sélectionné **Variante personnalisée** pour votre optimisation lors de l'implémentation de votre campagne, le **résultat du test A/B** est divisé en deux onglets : **Test initial** et **variante personnalisée**.

{% tabs local %}
{% tab Test initial %}

L'onglet **Test initial** présente les indicateurs de chaque variante du test A/B initial envoyé à une partie de votre segmentation cible.

![Les résultats du test d’origine envoyé pour déterminer la variante la plus performante pour chaque utilisateur. Un tableau montre la performance de chaque variante sur la base de divers indicateurs pour le canal cible.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_1.png %})

Par défaut, le test recherche des associations entre les événements personnalisés de l'utilisateur et ses préférences en matière de variantes de messages. Cette analyse permet de déterminer si les événements personnalisés augmentent ou diminuent la probabilité de répondre à une variante de message donnée. Ces relations sont ensuite utilisées pour déterminer quels utilisateurs reçoivent quelle variante de message lors de l'envoi final.

Les relations entre les événements personnalisés et les préférences de message sont affichées dans le tableau de l'onglet **Envoi initial**.

![]({% image_buster /assets/img_archive/ab_analytics_pv_3.png %})

Si le test ne parvient pas à établir une relation significative entre les événements personnalisés et les préférences variantes, il reviendra à une méthode d'analyse basée sur les sessions.

{% details Méthode d'analyse de repli %}

**Méthode d'analyse par session**<br>
Si la méthode de repli est utilisée pour déterminer les variantes personnalisées, l'onglet **Test initial** présente une répartition des variantes préférées des utilisateurs en fonction d'une combinaison de certaines caractéristiques. 

Ces caractéristiques sont :

- **Récence :** La date de leur dernière session
- **Fréquence :** La fréquence de leurs sessions
- **Ancienneté :** Depuis combien de temps ils sont utilisateurs

Par exemple, le test peut déterminer que la majorité des utilisateurs préfèrent la variante A, mais les utilisateurs ayant eu une session il y a 3 à 12 jours, ont eu un intervalle entre deux sessions de 1 à 12 jours et ont été créé entre les derniers 67 à 577 jours ont tendance à préférer la Variante B. De fait, les utilisateurs de cette sous-population ont reçu la Variante B au cours du second envoi alors que les autres ont reçu la Variante A.

![Le tableau des caractéristiques des utilisateurs, qui montre quels utilisateurs sont prédisposés à préférer la variante A et la variante B en fonction des trois compartiments dans lesquels ils se trouvent pour la récurrence, la fréquence et l'ancienneté.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_2.png %})

**Comment les variantes personnalisées sont-elles sélectionnées ?**<br>
Avec cette méthode, le message recommandé à un utilisateur individuel correspond à la somme des effets de sa récence, de sa fréquence et de son ancienneté. La récurrence, la fréquence et l'ancienneté sont réparties en compartiments, comme l'illustre le tableau des **caractéristiques de l'utilisateur**. La fenêtre temporelle de chaque compartiment est déterminée par les données des utilisateurs dans chaque campagne individuelle et variera entre deux campagnes. 

Chaque compartiment peut avoir une contribution ou une "poussée" différente pour chaque variante de message. La force de cette « poussée»  pour chaque compartiment est déterminée à partir des réponses des utilisateurs lors de l'envoi initial à l'aide d'une [régression logistique](https://en.wikipedia.org/wiki/Logistic_regression). Ce tableau ne fait que résumer les résultats en affichant avec quelle variante s’engagent le plus les utilisateurs de chaque compartiment. La variante personnalisée réelle de chaque utilisateur dépend de la somme des effets des trois compartiments dans lesquels il se trouve - un pour chaque caractéristique.

{% enddetails %}

{% endtab %}
{% tab Variante personnalisée %}

L'onglet **Variante personnalisée** montre les résultats du deuxième envoi, où chaque utilisateur restant a reçu la variante avec laquelle il était le plus susceptible de s'engager.

Les trois cartes de cette page affichent l’augmentation projetée, vos résultats globaux et les résultats projetés si vous envoyez uniquement la variante gagnante. Même s'il n'y a pas d'effet de levier, ce qui peut parfois arriver, le résultat est le même que si vous n'envoyez que la variante gagnante (un test A/B traditionnel). 

- **Augmentation projetée :** L'amélioration de votre indicateur d'optimisation sélectionné pour cet envoi grâce à l'utilisation de variantes personnalisées au lieu d'un test A/B standard (si les utilisateurs restants n'ont reçu que la variante gagnante).
- **Résultats globaux :** Les résultats du deuxième envoi en fonction de l'indicateur d'optimisation que vous avez choisi*(ouvertures uniques*, *clics uniques* ou *événement de conversion principal*).
- **Résultats projetés :** Les résultats projetés du deuxième envoi sur la base de l'indicateur d'optimisation que vous avez choisi, si vous aviez envoyé uniquement la variante gagnante. 

![Onglet Variante personnalisée pour une campagne optimisée pour les ouvertures uniques. Les cartes affichent l’augmentation projetée, les ouvertures uniques globales (avec une variante personnalisée) et les ouvertures uniques projetées (avec la variante gagnante).]({% image_buster /assets/img_archive/ab_analytics_pv_1.png %})

Le tableau de cette page présente les indicateurs pour chaque variante de l'envoi de variantes personnalisées. Votre **% d'audience** correspond au pourcentage du segment cible que vous avez réservé au groupe de variante personnalisée.

![]({% image_buster /assets/img_archive/ab_analytics_pv_2.png %})

{% endtab %}
{% endtabs %}

## Comprendre la confiance {#understanding-confidence}

La confiance est la mesure statistique du degré de certitude qu'une différence dans les données, comme les taux de conversion, est réelle et n'est pas due au hasard.

{% alert note %}
Vous n'avez pas confiance en vos résultats ? La confiance n'apparaîtra que si vous avez un groupe de contrôle.
{% endalert %}

Une partie importante de vos résultats est la confiance dans l’exactitude de vos résultats. Par exemple, que se passe-t-il si le groupe de contrôle avait un taux de conversion de 20 % et que la variante A avait un taux de conversion de 25 % ? Cela indique qu’il est préférable d’envoyer la variante A que de n’envoyer aucun message. Avoir une confiance de 95 % signifie que la différence entre les deux taux de conversion est probablement due à une différence réelle dans les réactions des utilisateurs et qu’il n’y a qu’une probabilité de 5 % que la différence se soit produite par hasard.

Braze compare le taux de conversion de chaque variante au taux de conversion du groupe de contrôle à l'aide d'une procédure statistique appelée [test Z](https://en.wikipedia.org/wiki/Z-test). Un résultat de 95 % de confiance ou plus, comme dans l’exemple précédent, indique que la différence est significative sur le plan statistique. Cela est vrai pour toutes les mesures de confiance du tableau de bord de Braze qui décrivent la différence entre deux messages ou populations d’utilisateurs.

En général, une confiance d’au moins 95 % est nécessaire pour montrer que vos résultats reflètent bien les préférences réelles des utilisateurs, et qu’ils ne sont pas simplement dus au hasard. Dans des tests scientifiques rigoureux, le pourcentage de confiance de 95 % (ou autrement appelé la valeur « p », qui est inférieure à 0,05) est la référence utilisée pour déterminer la pertinence statistique. Si vous ne parvenez pas à obtenir une confiance de 95 %, essayez d’augmenter la taille de votre échantillon ou de diminuer le nombre de variantes. 

La confiance ne permet pas de déterminer si une variante est meilleure que les autres. Il s’agit simplement d’une mesure qui évalue à quel point nous sommes sûrs que les deux taux de conversion (ou plus) sont réellement différents les uns des autres. Il s’agit uniquement d’une fonction de la taille de l’échantillon et des différences entre les taux de conversion apparents. Le degré des taux globaux n’affecte pas la fiabilité de la mesure de confiance. Une variante peut avoir un taux de conversion très différent d’une autre sans forcément atteindre une confiance de 95 %. Il est également possible que deux ensembles de variantes aient des taux de conversion ou d’augmentation similaires, mais un niveau de confiance différent.

### Résultats statistiquement insignifiants

Un test peut fournir des informations importantes même si son niveau de confiance est inférieur à 95 %. Voici quelques éléments à prendre en compte lorsque les résultats d’un test ne sont pas significatifs sur le plan statistique :

- Il est possible que toutes vos variantes aient eu le même effet. En prenant cela en compte, vous évitez de perdre du temps à effectuer ces changements. Vous pourrez parfois vous rendre compte que les tactiques marketing classiques, comme renvoyer votre appel à l’action, ne fonctionnent pas nécessairement avec votre audience.
- Bien que vos résultats aient pu être dus au hasard, ils peuvent tout de même vous aider à formuler une hypothèse pour votre prochain test. Si plusieurs variantes semblent avoir plus ou moins les mêmes résultats, testez-les de nouveau en ajoutant de nouvelles variantes pour voir s’il existe une alternative plus efficace. Si une variante obtient de meilleurs résultats, mais pas par une marge considérable, vous pouvez effectuer un autre test en accentuant la différence de cette variante.
- Continuez à tester des variantes ! Un test dont les résultats ne sont pas probants doit vous amener à vous poser certaines questions. N’y a-t-il eu vraiment aucune différence entre vos variantes ? Auriez-vous dû structurer votre test différemment ? Vous pouvez répondre à ces questions en effectuant des tests de suivi.
- Bien que les tests soient utiles pour découvrir quel type de message génère la plus forte réaction auprès de votre audience, il est également important de comprendre quels changements dans le message ont eu un effet négligeable. Cela vous permet soit de poursuivre vos tests pour trouver une alternative plus efficace, soit de gagner du temps que vous auriez passé à choisir entre deux messages alternatifs.

Que votre test aboutisse ou non à un résultat clair, il peut être utile d'effectuer un [test de suivi](#recommended-follow-ups) pour confirmer vos résultats ou appliquer vos conclusions à un scénario légèrement différent.

## Suivis recommandés {#recommended-follow-ups}

Un test A/B ou multivarié peut (et devrait !) vous donner des idées pour vos prochains tests, et vous inciter à réorienter votre stratégie de communication. Voici quelques exemples d’actions de suivi :

#### Modifier votre stratégie de communication en fonction des résultats des tests

Vos résultats multivariés peuvent vous amener à changer la façon dont vous formulez ou formatez votre message.

#### Modifier votre compréhension de vos utilisateurs

Chaque test apportera des informations sur les comportements de vos utilisateurs, la manière dont ils réagissent face à différents canaux de communication et les différences (et similarités) entre vos segments.

#### Améliorer la façon dont vous structurez vos prochains tests

Votre échantillon était-il trop petit ? Les différences entre vos variantes étaient-elles trop subtiles ? Chaque test est une occasion d’améliorer les suivants. Si votre confiance est faible, cela signifie que la taille de votre échantillon est trop petite et qu’il doit être agrandi lors des prochains tests. Si vous n’observez aucune différence notable entre les résultats de vos variantes, il est possible que les différences aient été trop subtiles pour avoir un effet discernable par rapport aux réactions des utilisateurs.

#### Effectuer un test de suivi avec un plus grand échantillon

Les échantillons de grande taille augmentent le risque de détecter de petites différences entre les variantes.

#### Effectuer un test de suivi en utilisant un autre canal de communication

Si vous constatez qu’une stratégie donnée est très efficace pour un canal, vous pouvez tester cette stratégie avec d’autres canaux. Si un type de message est efficace dans un canal, mais pas dans un autre, vous pouvez raisonnablement conclure que certains canaux sont plus propices à certains types de messages. Ou bien, il existe peut-être une différence entre les utilisateurs qui sont plus susceptibles d’activer les notifications push et ceux qui sont plus susceptibles de prêter attention aux messages in-app. En fin de compte, ce type de test vous aidera à découvrir comment votre audience interagit avec vos différents canaux de communication.

#### Effectuer un test de suivi sur un autre segment d’utilisateurs

Pour ce faire, créez un autre test avec le même canal de communication et les mêmes variantes, mais choisissez un segment d’utilisateurs différent. Par exemple, si un type de message était extrêmement efficace auprès des utilisateurs actifs, il peut être utile d’enquêter sur son effet auprès des utilisateurs inactifs. Les utilisateurs inactifs pourraient réagir de manière similaire ou préférer une des autres variantes. Ce test vous aidera à en savoir plus sur vos différents segments et sur la manière dont ils réagissent à différents types de messages. Pourquoi formuler des hypothèses sur vos segments lorsque vous pouvez baser votre stratégie sur les données ?

#### Effectuer un test de suivi basé sur les informations issues d’un test précédent

Utilisez les informations issues de vos tests passés pour mieux orienter vos futurs projets. L’un de vos précédents tests semble-t-il indiquer qu’une technique de communication est plus efficace que les autres ? Quel élément de la variante gagnante l’a rendue plus efficace ? Baser vos tests de suivi sur ces questions vous aidera à obtenir des résultats pertinents sur vos utilisateurs.

#### Comparer l’impact à long terme de différentes variantes

Si vous effectuez des tests A/B sur les messages de réengagement, n'oubliez pas de comparer l'impact à long terme des différentes variantes à l'aide des [rapports de rétention.]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) Vous pouvez utiliser les rapports de rétention pour analyser la façon dont chaque variante a affecté le comportement des utilisateurs sur une période de plusieurs jours ou semaines, ou même un mois après réception du message, et voir s’il y a une augmentation.
