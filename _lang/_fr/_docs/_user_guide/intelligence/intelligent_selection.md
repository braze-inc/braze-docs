---
nav_title: Sélection intelligente
article_title: Sélection intelligente
page_order: 1
description: "La sélection intelligente est une fonctionnalité qui analyse les performances d'une campagne récurrente ou de Canvas deux fois par jour et ajuste automatiquement le pourcentage d'utilisateurs qui reçoivent chaque variante de message."
---

# Sélection intelligente {#intelligent-selection}

> La sélection intelligente est une fonctionnalité qui analyse les performances d'une campagne récurrente ou de Canvas deux fois par jour et ajuste automatiquement le pourcentage d'utilisateurs qui reçoivent chaque variante de message.

Une variante qui semble être plus performante que les autres ira à plus d'utilisateurs, alors que les variantes qui sont sous-performantes seront ciblées sur moins d'utilisateurs. Chaque ajustement est effectué à l'aide d'un [algorithme statistique][227] qui s'assure que nous ajustons pour des différences réelles de performances et pas seulement pour des chances aléatoires.

En regardant de façon répétée les données de performance et en déplaçant le trafic de campagne vers des variantes gagnantes progressivement, Slection intelligente garantit à plus d'utilisateurs de recevoir votre variante la plus performante, sans sacrifier en toute confiance statistique. La sélection intelligente exclura également les variantes sous-performantes et identifiera les variantes très performantes plus rapidement qu'un [test A/B traditionnel][1]. Grâce à Intelligent Selection, vous pouvez tester plus fréquemment et avec une plus grande confiance que vos utilisateurs verront votre meilleur message.

Intelligent Selection est idéal pour les campagnes qui sont planifiées pour envoyer plusieurs fois. Étant donné que la sélection intelligente a besoin de résultats initiaux pour commencer à ajuster votre campagne, une campagne qui n'envoie qu'une seule fois ne bénéficiera pas. Pour ces campagnes, un [test A/B][1] serait plus efficace.

!\[Intelligent_Selection_Shot\]\[271\]

## Pendant combien de temps cela va-t-il durer?

Pour les campagnes et les vases, la Sélection Intelligente s’exécutera jusqu’à ce qu’elle recueille suffisamment de preuves sur les taux de conversion « vrais » des variantes. "Asse" est déterminé par une mesure spéciale appelée "regret". Vous pouvez le considérer comme similaire à la confiance : quand il y a suffisamment de données pour savoir quelle variante est la meilleure, Intelligent Selection s'éteindra. Dans la plupart des cas, une des variantes sera choisie par l'algorithme comme variante gagnante. Cette variante sera donnée 100% du public pour les envois futurs.

{% alert note %}
Il est possible pour Intelligent Selection d'arrêter d'optimiser sans choisir un seul gagnant clair. Intelligent Selection cesse d'optimiser quand il a 95% de confiance que la poursuite de l'expérience n'améliorera pas le taux de conversion de plus de 1% de son taux actuel.
{% endalert %}
[271]: {% image_buster /assets/img/intelligent_selection1.png %}

[1]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/

[1]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/
[227]: https://en.wikipedia.org/wiki/Multi-armed_bandit
