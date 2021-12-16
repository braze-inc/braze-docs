---
nav_title: Sélection intelligente
article_title: Sélection intelligente
page_order: 1
description: "La sélection intelligente est une fonctionnalité qui analyse les performances d'une campagne récurrente ou de Canvas deux fois par jour et ajuste automatiquement le pourcentage d'utilisateurs qui reçoivent chaque variante de message."
---

# Sélection intelligente {#intelligent-selection}

> Cet article donne un aperçu de la sélection intelligente et de la façon dont vous pouvez l'implémenter dans vos campagnes et vos canvases.

La sélection intelligente est une fonctionnalité qui analyse les performances d'une campagne récurrente ou de Canvas deux fois par jour et ajuste automatiquement le pourcentage d'utilisateurs qui reçoivent chaque variante de message. Une variante qui semble être plus performante que les autres sera envoyée à plus d'utilisateurs, tandis que les variantes sous-performantes seront ciblées sur moins d'utilisateurs. Chaque ajustement est effectué à l'aide d'un [algorithme statistique][227] qui s'assure que nous ajustons pour des différences réelles de performances et pas seulement pour des chances aléatoires.

!\[Sélection Intelligence\]\[3\]

La sélection intelligente va :
- Examinez à plusieurs reprises les données de performance et déplacez progressivement le trafic de campagne vers des variantes gagnantes.
- Assurez-vous qu'un plus grand nombre d'utilisateurs reçoivent votre variante la plus performante sans sacrifier la confiance satistique.
- Règle les variantes sous-performantes et identifie les variantes très performantes plus rapidement qu'un [test A/B traditionnel][1].
- Vous permet de tester plus fréquemment et avec une plus grande confiance que vos utilisateurs verront votre meilleur message.

Intelligent Selection est idéal pour les campagnes qui sont planifiées pour envoyer plusieurs fois. Les premiers résultats sont nécessaires pour commencer à ajuster votre campagne; par conséquent, une campagne qui n'envoie qu'une seule fois ne sera pas bénéfique. Pour ces campagnes, un [test A/B][1] serait plus efficace.

## Comment ajouter une sélection intelligente à mes campagnes ?

Campagne : Une sélection intelligente peut être ajoutée à n'importe quelle campagne multi-envois dans l'étape « Utilisateurs cibles » de l'assistant de campagne Braze. Les campagnes d'envoi unique ne pourront pas tirer parti de cette fonctionnalité.

Canvas : Lorsque vous ajoutez des variantes dans votre Canevas, cliquez sur un des pourcentages de variantes. Cela vous permettra de modifier la distribution de variante et d'activer la sélection intelligente. La sélection intelligente ne sera pas disponible si vous n'avez pas encore ajouté d'événements de conversion à votre Canvas ou si votre campagne est composée d'une variante solo ou d'un groupe de contrôle solo.<br><br>!\[Sélection intelligente de Canvas\]\[2\]

{% alert note %}
Nous ne permettons pas que les campagnes de sélection intelligentes aient été rééligibles parce qu'elles affecteraient l'intégrité de la variante de contrôle. Consultez la [FAQ sur les renseignements]({{site.baseurl}}/user_guide/intelligence/faqs/#why-is-re-eligibility-not-available-when-combined-with-intelligent-selection) pour en savoir plus.
{% endalert %}

## Pendant combien de temps cela va-t-il durer?

Pour les campagnes et les vases, la Sélection Intelligente s’exécutera jusqu’à ce qu’elle recueille suffisamment de preuves sur les taux de conversion « vrais » des variantes. "Asse" est déterminé par une mesure spéciale appelée "regret". Vous pouvez le considérer comme similaire à la confiance : quand il y a suffisamment de données pour savoir quelle variante est la meilleure, Intelligent Selection s'éteindra. Dans la plupart des cas, l'algorithme choisira l'une des variantes comme variante gagnante. Cette variante sera donnée 100% du public pour les envois futurs.

{% alert note %}
Il est possible pour Intelligent Selection d'arrêter d'optimiser sans choisir un seul gagnant clair. Intelligent Selection cesse d'optimiser quand il a 95% de confiance que la poursuite de l'expérience n'améliorera pas le taux de conversion de plus de 1% de son taux actuel.
{% endalert %}
[3]: {% image_buster /assets/img/intelligent_selection1.png %} [2]: {% image_buster /assets/img/intelligent_selection.png %}

[1]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/

[1]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/
[227]: https://en.wikipedia.org/wiki/Multi-armed_bandit
