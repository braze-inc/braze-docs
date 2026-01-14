---
nav_title: Chemins personnalisés
article_title: "Chemins personnalisés dans les chemins d'expérience" 
page_type: reference
description: "Les parcours personnalisés vous permettent de personnaliser n'importe quel point d'un parcours Canvas pour des utilisateurs individuels en fonction de la probabilité de conversion."
tool: Canvas
---

# Chemins personnalisés dans les chemins d'expérience

> Les parcours personnalisés sont similaires à la [variante personnalisée]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/#personalized-variant) des campagnes et vous permettent de personnaliser n'importe quel point d'un parcours Canvas pour des utilisateurs individuels en fonction de la probabilité de conversion.

## Fonctionnement des parcours personnalisés

Lorsque l'option Chemins personnalisés est activée dans une étape des chemins d'expérience, le comportement est légèrement différent selon que votre Canvas est configuré pour être envoyé une seule fois ou de manière récurrente :

- **Canvas à envoi unique :** Un groupe d'utilisateurs est retenu dans un groupe de retard. Les utilisateurs restants passent dans un test initial pour entraîner un modèle prédictif pendant une durée que vous configurez - au moins 24 heures pour de meilleurs résultats. Après le test, un modèle est créé pour apprendre quels comportements de l'utilisateur ont été associés à une plus grande probabilité de conversion sur un chemin donné. Enfin, chaque utilisateur du groupe de retard est envoyé sur le chemin le plus susceptible d'aboutir à une conversion pour lui, sur la base des comportements qu'il affiche et de ce que le modèle prédictif a appris au cours du test initial.
- **Canevas récurrents, déclenchés par l'action et par l'API :** Une première expérience est effectuée sur tous les utilisateurs qui entrent dans le chemin d'expérience au cours d'une fenêtre spécifiée. Afin de préserver l'intégrité de l'expérience, si un utilisateur reçoit plusieurs messages avant la fin de la fenêtre, il sera assigné à la même variante à chaque fois. Après la fenêtre d'expérience, chaque utilisateur est envoyé sur le chemin d'expérience le plus susceptible d'aboutir à une conversion pour lui.

## Utilisation de parcours personnalisés

### Étape 1 : Ajouter un chemin d'expérience

Ajoutez un [chemin d'expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) à votre Canvas, puis activez les **chemins personnalisés**.

\![]({% image_buster /assets/img/experiment_step/experiment_personalized_path.png %})

### Étape 2 : Configurer les paramètres des parcours personnalisés

Indiquez l'événement de conversion qui doit déterminer le gagnant. Si aucun événement de conversion n'est disponible, revenez à la première étape de la configuration de Canvas et [attribuez des événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#choose-conversion-events). 

Si vous choisissez les ouvertures ou les clics comme événement de conversion, assurez-vous que la première étape du chemin est une [étape de Message.]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) Braze ne compte que l'engagement à partir de la première étape du message dans chaque voie respective. Si le parcours commence par une étape différente (comme une étape de retard ou de parcours d'audience) et que le message arrive plus tard, ce message ne sera pas pris en compte lors de l'évaluation de la performance.

Définissez ensuite la **fenêtre d'expérience**. La **fenêtre d'expérience** détermine la durée pendant laquelle les utilisateurs seront envoyés sur tous les chemins avant de choisir le meilleur chemin pour chaque utilisateur du groupe de retard. La fenêtre commence lorsque le premier utilisateur entre dans l'étape.

\![]({% image_buster /assets/img/experiment_step/experiment_personalized_settings.png %})

### Étape 3 : Déterminer la solution de repli

Par défaut, si les résultats du test ne sont pas suffisants pour déterminer un gagnant statistiquement significatif, tous les utilisateurs futurs seront envoyés sur le chemin unique le plus performant.

Vous pouvez également sélectionner **Continuer à envoyer le mélange de chemins à tous les futurs utilisateurs**.

\![]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

Cette option enverra les futurs utilisateurs dans la combinaison de chemins selon les pourcentages spécifiés dans la distribution des chemins d'expérience.

\![]({% image_buster /assets/img/experiment_step/experiment_personalized_percentages.png %})

### Étape 4 : Ajoutez vos chemins et lancez le Canvas

{% tabs local %}
{% tab Single-send Canvas %}

Un seul composant "chemin d'expérience" peut contenir jusqu'à quatre chemins. Toutefois, pour les toiles à envoi unique, vous pouvez ajouter jusqu'à trois chemins lorsque l'option Chemins personnalisés est activée. Le quatrième chemin doit être réservé au groupe de retard que Braze ajoute automatiquement à votre expérience.

Terminez la configuration de votre Canvas si nécessaire, puis lancez-le. Lorsque le premier utilisateur est entré dans l'expérience, vous pouvez consulter le Canvas pour voir les analyses/analytiques au fur et à mesure qu'elles arrivent et [suivre les performances de votre expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance).

\![]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_pending.png %}){: style="max-width:75%;" }

Lorsque la fenêtre d'expérience est passée et que l'expérience est terminée, Braze envoie les utilisateurs du groupe de retard vers leurs chemins d'expérience respectifs avec la probabilité de conversion personnalisée la plus élevée, sur la base de la recommandation du modèle prédictif.

\![]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_complete.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab Recurring or action-triggered or API-triggered Canvas %}

Vous pouvez tester jusqu'à quatre chemins dans un seul chemin d'expérience. Ajoutez vos chemins et terminez la configuration de votre Canvas si nécessaire, puis lancez-le.  

Lorsque le premier utilisateur est entré dans l'expérience, vous pouvez consulter le Canvas pour voir les analyses/analytiques au fur et à mesure qu'elles arrivent et [suivre les performances de votre expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance).

Lorsque la fenêtre d'expérience est passée et que l'expérience est terminée, tous les utilisateurs qui entreront ensuite dans le Canvas seront dirigés vers le chemin d'expérience le plus susceptible d'aboutir à une conversion pour eux.

\![]({% image_buster /assets/img/experiment_step/experiment_personalized_recurring_analytics.png %}){: style="max-width:75%;" }

{% endtab %}
{% endtabs %}

## Analyse/analytique (si utilisé comme adjectif) {#analytics}

Si l'option Chemins personnalisés a été activée, votre vue d'analyse/analytique est séparée en deux onglets : **Première expérience** et **chemins personnalisés**.

{% tabs local %}
{% tab Initial Experiment %}

L'onglet **Expérience initiale** affiche les indicateurs pour chaque chemin d'expérience pendant la fenêtre d'expérience. Vous pouvez consulter un résumé des performances de tous les chemins d'accès pour les événements de conversion spécifiés.

Résultats d'une première expérience envoyée pour déterminer le chemin le plus performant pour chaque utilisateur. Un tableau présente les performances de chaque chemin en fonction de divers indicateurs pour le canal cible.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1.png %})

Par défaut, le test recherche des associations entre les événements personnalisés des utilisateurs et leurs préférences de parcours, ou la variante de message à laquelle un utilisateur réagit le mieux. Cette analyse permet de déterminer si les événements personnalisés augmentent ou diminuent la probabilité de répondre à un chemin particulier. Ces relations sont ensuite utilisées pour déterminer quel utilisateur se voit attribuer quel chemin après la fin de la fenêtre d'expérience.

Les relations entre les événements personnalisés et les préférences de chemin sont affichées dans le tableau de l'onglet **Expérience initiale**.

\![]({% image_buster /assets/img_archive/experiment_personalized_analytics_custom_data.png %})

Si le test ne parvient pas à établir une relation significative entre les événements personnalisés et les préférences de parcours, il reviendra à une méthode d'analyse basée sur les sessions.

{% details Fallback analysis method %}

**Méthode d'analyse par session**<br>
Si la méthode de repli est utilisée pour déterminer les chemins personnalisés, l'onglet **Expérience initiale** présente une répartition des variantes préférées des utilisateurs en fonction d'une combinaison de certaines caractéristiques.

Ces caractéristiques sont les suivantes

- **Récence :** Date de la dernière session
- **Fréquence :** La fréquence des sessions
- **Durée du mandat :** Depuis combien de temps est-il utilisateur ?

Le tableau des caractéristiques de l'utilisateur, qui indique quels utilisateurs sont prédisposés à préférer le chemin 1 et le chemin 2 en fonction des trois compartiments dans lesquels ils se situent pour la récurrence, la fréquence et l'ancienneté.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1_2.png %})

Considérez la récence comme le caractère récent de leur dernière interaction avec vous, la fréquence comme le nombre de fois où ils s'engagent, et la durée comme la durée globale de leur engagement avec vous. Nous regroupons les utilisateurs en "compartiments" sur la base de ces trois éléments (comme expliqué dans le tableau des **caractéristiques de l'utilisateur** ) et nous voyons ensuite quel compartiment aime le plus tel ou tel chemin. Cela revient à classer les utilisateurs dans des centaines de listes différentes en fonction de la date de leur dernier achat chez vous, de la fréquence de leurs achats et de l'ancienneté de leur clientèle.

Lorsqu'il s'agit de choisir un message pour un utilisateur, Braze examine les compartiments dans lesquels il se situe. Chaque compartiment exerce une influence distincte sur le choix du chemin par les utilisateurs. Nous quantifions cette influence à l'aide d'une méthode statistique appelée [régression logistique](https://en.wikipedia.org/wiki/Logistic_regression), qui permet de prédire un comportement futur sur la base d'actions passées. Cette méthode tient compte des interactions de l'utilisateur lors de l'envoi initial du message. Ce tableau ne fait que résumer les résultats en affichant le chemin que les utilisateurs de chaque compartiment ont eu tendance à emprunter.

En fin de compte, Braze combine toutes ces données pour sélectionner un parcours de messages sur mesure pour chaque utilisateur, afin de s'assurer qu'il est aussi engageant et pertinent que possible pour lui.

{% alert note %}
Les intervalles de temps pour chaque compartiment sont déterminés en fonction des données des utilisateurs spécifiques à Canvas, qui peuvent varier d'un Canvas à l'autre.
{% endalert %}

**Comment les parcours personnalisés sont-ils sélectionnés ?**<br>
Avec cette méthode, le message recommandé à un utilisateur individuel est la somme des effets de sa récence, de sa fréquence et de son ancienneté. La récurrence, la fréquence et l'ancienneté sont réparties en compartiments, comme l'illustre le tableau des **caractéristiques de l'utilisateur**. La durée de chaque compartiment est déterminée par les données relatives aux utilisateurs de chaque Canvas et varie d'un Canvas à l'autre.

Chaque compartiment peut avoir une contribution ou une "poussée" différente vers chaque voie. La force de la poussée pour chaque compartiment est déterminée à partir des réponses des utilisateurs lors de l'expérience initiale à l'aide d'une [régression logistique](https://en.wikipedia.org/wiki/Logistic_regression). Ce tableau ne fait que résumer les résultats en affichant le chemin que les utilisateurs de chaque compartiment ont eu tendance à emprunter. Le parcours personnalisé de chaque utilisateur dépend de la somme des effets des trois compartiments dans lesquels il se trouve - un pour chaque caractéristique.

{% enddetails %}

{% endtab %}
{% tab Personalized Paths %}

L'onglet **Chemins personnalisés** présente les résultats de l'expérience finale, au cours de laquelle les utilisateurs du groupe Retard ont été dirigés vers le chemin le plus performant pour eux.

Les trois cartes de cette page indiquent votre taux de réussite, vos résultats globaux et les résultats projetés si vous envoyez uniquement le parcours gagnant à la place. Même s'il n'y a pas d'effet de levier, ce qui peut parfois arriver, le résultat est le même que si vous n'envoyez que le chemin gagnant (un test A/B traditionnel).

- **Levée prévue :** L'amélioration de votre événement de conversion sélectionné due à l'utilisation de Chemins personnalisés au lieu d'envoyer chaque utilisateur sur le chemin global le plus performant.
- **Résultats globaux :** Les résultats du deuxième envoi sont basés sur votre événement de conversion.
- **Résultats prévus :** Les résultats projetés du deuxième envoi sur la base de l'indicateur d'optimisation que vous avez choisi, si vous aviez envoyé uniquement la variante gagnante.

!onglet Chemins personnalisés pour un Canvas. Les cartes indiquent l'effet de levier projeté, les conversions globales (avec les chemins personnalisés) et les ouvertures uniques projetées (avec le chemin gagnant).]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab2.png %})

{% endtab %}
{% endtabs %}

## Utilisation de parcours personnalisés avec réception/distribution locale

Nous ne recommandons pas d'utiliser la diffusion selon l'heure/distribution locale dans les toiles avec chemins personnalisés. En effet, les fenêtres d'expérimentation commencent lorsque le premier utilisateur passe. Les utilisateurs qui se trouvent dans des fuseaux horaires très précoces peuvent entrer dans l'étape et déclencher le début de la fenêtre d'expérience beaucoup plus tôt que prévu, ce qui peut avoir pour conséquence que l'expérience se termine avant que la majorité de vos utilisateurs se trouvant dans des fuseaux horaires plus classiques aient eu le temps d'entrer dans le Canvas et de se convertir.

Par ailleurs, si vous souhaitez utiliser la réception/distribution locale, utilisez une fenêtre d'expérimentation de 24 à 48 heures ou plus. Ainsi, les utilisateurs situés dans les premiers fuseaux horaires entrent dans le Canvas et déclenchent le démarrage de l'expérience, mais il reste beaucoup de temps dans la fenêtre d'expérience. Les utilisateurs situés dans des fuseaux horaires plus tardifs auront encore suffisamment de temps pour entrer dans le Canvas et l'étape des chemins d'expérience d'une manière personnalisée et éventuellement se convertir avant que la fenêtre d'expérience n'expire.

