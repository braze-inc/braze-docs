---
nav_title: Sélection intelligente
article_title: Sélection intelligente
page_order: 1
description: "Cette article décrit la sélection intelligente, une fonctionnalité qui analyse deux fois par jour les performances d’une campagne ou d’un Canvas récurrent et ajuste automatiquement le pourcentage d’utilisateurs qui reçoivent chaque variante de message."
search_rank: 10
---

# Sélection intelligente {#intelligent-selection}

> Le présent article fournit un aperçu de la sélection intelligente et de la manière dont vous pouvez l’implémenter dans vos campagnes et vos Canvas.

La sélection intelligente est une fonctionnalité qui analyse deux fois par jour les performances d’une campagne ou d’un Canvas récurrent et ajuste automatiquement le pourcentage d’utilisateurs qui reçoivent chaque variante de message. Une variante qui semble être plus efficace qu’une autre sera envoyée à un plus grand nombre d’utilisateurs, tandis que les variantes moins efficaces cibleront moins d’utilisateurs. Chaque ajustement est effectué en utilisant [algorithme statistique][227] qui s’assure que l’ajustement est fait en fonction de réelles différences de performances et non pas seulement hasard.

![Section Test A/B d’une campagne ou d’un Canvas avec la sélection intelligente activée.][3]

La sélection intelligente va :
- Examiner de manière répétée les données de performance et faire évoluer progressivement le trafic de la campagne vers les variantes gagnantes.
- S’assurer que plus d’utilisateurs reçoivent votre variante la plus efficace sans sacrifier la confiance statistique.
- Exclure les variantes moins efficaces et identifier les variantes à haute performance plus rapidement qu’un [test A/B traditionnel][1].
- Vous permettre de tester plus fréquemment et avec plus de confiance que vos utilisateurs verront votre meilleur message. 

La sélection intelligente est idéale pour les campagnes planifiées pour être envoyées plusieurs fois. Des résultats initiaux sont nécessaires pour commencer à ajuster votre campagne. Par conséquent, une campagne qui ne sera envoyée qu’une seule fois n’en tirera pas parti. Pour ces campagnes, un [test A/B][1] serait plus efficace.

## Comment ajouter une sélection intelligente à mes campagnes ?

Campagne :
La sélection intelligente peut être ajoutée à toutes les campagnes à plusieurs envois dans l’étape « Target Users » (Utilisateurs cibles) de l’assistant de campagne Braze. Les campagnes à envoi unique ne pourront pas tirer parti de cette fonctionnalité.

Canvas :
Lorsque vous ajoutez des variantes dans votre Canvas, cliquez sur l’un des pourcentages de variante. Cela vous permettra de modifier la distribution de la variante et d’activer la sélection intelligente. La sélection intelligente ne sera pas disponible si vous n’avez pas encore ajouté d’événements de conversion à votre Canvas ou si votre campagne est composée d’une variante ou d’un groupe de contrôle unique.

![Un Canvas avec deux variantes, chacune définie à 50 % de distribution de la variante, permettant ainsi l’activation de la sélection intelligente.][2]

{% alert note %}
Nous ne permettons pas l’utilisation de la sélection intelligente avec des campagnes ayant une rééligibilité de moins de 24 heures car cela affecterait l’intégrité de la variante de contrôle. Consultez la [FAQ Intelligence]({{site.baseurl}}/user_guide/intelligence/faqs/#why-is-re-eligibility-not-available-when-combined-with-intelligent-selection) pour en savoir plus.
{% endalert %}

## Pendant combien de temps va-t-elle s’exécuter ?

Pour les campagnes et les Canvas, la sélection intelligente s’exécutera jusqu’à ce qu’elle rassemble suffisamment de preuves des taux de conversion « réels » des variantes. « Suffisamment » est déterminé par une métrique spéciale appelée « regret ». Vous pouvez l’imaginer comme étant similaire à la confiance : lorsque vous disposez de suffisamment de données pour savoir quelle variante est la meilleure, la sélection intelligente s’éteint. Dans la plupart des cas, l’algorithme choisira l’une des variantes comme variante gagnante. Cette variante sera envoyée à 100 % de l’audience pour les envois futurs.

{% alert note %}
Il est possible qu’une sélection intelligente s’arrête d’optimiser sans avoir choisi un seul gagnant. La sélection intelligente cessera d’optimiser lorsqu’elle sera sûre à 95 % que la poursuite de l’expérience n’améliorera pas le taux de conversion de plus de 1 % par rapport à son taux actuel.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/
[227]: https://en.wikipedia.org/wiki/Multi-armed_bandit
[3]: {% image_buster /assets/img/intelligent_selection1.png %}
[2]: {% image_buster /assets/img/intelligent_selection.png %}
