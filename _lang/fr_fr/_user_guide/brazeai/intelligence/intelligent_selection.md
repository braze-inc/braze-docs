---
nav_title: Sélection intelligente
article_title: Sélection intelligente
page_order: 1
description: "Cette article décrit la sélection intelligente, une fonctionnalité qui analyse deux fois par jour les performances d’une campagne ou d’un Canvas récurrent et ajuste automatiquement le pourcentage d’utilisateurs qui reçoivent chaque variante de message."
search_rank: 10
---

# Sélection intelligente {#intelligent-selection}

> La sélection intelligente est une fonctionnalité qui analyse deux fois par jour les performances d’une campagne ou d’un Canvas récurrent et ajuste automatiquement le pourcentage d’utilisateurs qui reçoivent chaque variante de message. 

Une variante qui semble être plus efficace qu’une autre sera envoyée à un plus grand nombre d’utilisateurs, tandis que les variantes moins efficaces cibleront moins d’utilisateurs. Chaque ajustement est effectué en utilisant un [algorithme statistique][227] qui s’assure que l’ajustement est fait en fonction de réelles différences de performances et pas uniquement au hasard.

![Section de test A/B d'une campagne où la sélection intelligente est activée.][3]

La sélection intelligente va :
- Examinez à plusieurs reprises les données de performance et déplacez progressivement le trafic de la campagne vers les variantes gagnantes.
- Vérifiez que davantage d'utilisateurs reçoivent votre variante la plus performante sans sacrifier la confiance statistique.
- Exclure les variantes moins efficaces et identifier les variantes très performantes plus rapidement qu’un [test A/B traditionnel][1].
- Testez plus fréquemment et avec une plus grande confiance que vos utilisateurs verront votre meilleur message. 

La sélection intelligente est idéale pour les campagnes planifiées pour être envoyées plusieurs fois. Des résultats initiaux sont nécessaires pour commencer à ajuster votre campagne. Par conséquent, une campagne qui ne sera envoyée qu’une seule fois n’en tirera pas parti. Pour ces campagnes, un [test A/B][1] serait plus efficace.

## Comment ajouter une sélection intelligente à mes campagnes ?

### Sélection intelligente de la campagne
La sélection intelligente peut être ajoutée à n'importe quelle campagne multi-envoi dans l'étape **Audiences ciblées** du compositeur de campagne de Braze. Les campagnes qui n'envoient qu'une seule fois ne peuvent pas bénéficier de cette fonctionnalité.

### Sélection intelligente de canvas
Lorsque vous ajoutez des variantes dans votre Canvas, cliquez sur l’un des pourcentages de variante. Vous pouvez ainsi modifier la répartition des variantes et activer la sélection intelligente.

![Un Canvas avec deux variantes, chacune définie à 50 % de distribution de la variante, permettant ainsi l’activation de la sélection intelligente.][2]

La sélection intelligente ne sera pas disponible si vous n'avez pas encore ajouté d'événements de conversion à votre Canvas ou si votre campagne est composée d'une variante solo.

{% alert note %}
Nous n'autorisons pas l'utilisation de la sélection intelligente pour les campagnes dont la rééligibilité est activée en moins de 24 heures, car cela affecterait l'intégrité de la variante de contrôle. Pour en savoir plus, consultez la [FAQ Intelligence]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endalert %}

## Pendant combien de temps va-t-elle s’exécuter ?

Pour les campagnes et les Canvas, la sélection intelligente s’exécutera jusqu’à ce qu’elle rassemble suffisamment de preuves des taux de conversion « réels » des variantes. Le niveau « suffisamment » est déterminé par un indicateur spécial appelé « regret ». Vous pouvez l'assimiler à la confiance dans la mesure où la sélection intelligente se désactive lorsqu'il y a suffisamment de données pour savoir quelle variante est la meilleure. 

Dans la plupart des cas, la sélection intelligente choisira l'une des variantes comme variante gagnante. Cette variante sera envoyée à 100 % de l’audience pour les envois futurs.

{% alert note %}
Il est possible qu’une sélection intelligente s’arrête d’optimiser sans avoir choisi un seul gagnant. La sélection intelligente cesse d'optimiser lorsqu'elle est sûre à 95 % que la poursuite de l'expérience n'améliorera pas le taux de conversion de plus de 1 % par rapport au taux actuel.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/
[2]: {% image_buster /assets/img/intelligent_selection.png %}
[3]: {% image_buster /assets/img/intelligent_selection1.png %}
[227]: https://en.wikipedia.org/wiki/Multi-armed_bandit

