---
nav_title: Sélection intelligente
article_title: Sélection intelligente
page_order: 1.0
description: "Cette article décrit la sélection intelligente, une fonctionnalité qui analyse deux fois par jour les performances d’une campagne ou d’un Canvas récurrent et ajuste automatiquement le pourcentage d’utilisateurs qui reçoivent chaque variante de message."
search_rank: 10
toc_headers: h2
---

# Sélection intelligente {#intelligent-selection}

> La sélection intelligente est une fonctionnalité qui analyse deux fois par jour les performances d’une campagne ou d’un Canvas récurrent et ajuste automatiquement le pourcentage d’utilisateurs qui reçoivent chaque variante de message. 

## À propos de la sélection intelligente

Une variante qui semble être plus efficace qu’une autre sera envoyée à un plus grand nombre d’utilisateurs, tandis que les variantes moins efficaces cibleront moins d’utilisateurs. Chaque Adjust est effectué à l'aide d'un [algorithme statistique](https://en.wikipedia.org/wiki/Multi-armed_bandit) qui garantit que Braze s'adapte à de réelles différences de performances et pas seulement au hasard.

![Section de test A/B d'une campagne avec sélection intelligente activée.]({% image_buster /assets/img/intelligent_selection1.png %})

La sélection intelligente va :
- Examinez à plusieurs reprises les données de performance et déplacez progressivement le trafic de la campagne vers les variantes gagnantes.
- Vérifiez que davantage d'utilisateurs reçoivent votre variante la plus performante sans sacrifier la confiance statistique.
- Exclure les variantes moins efficaces et identifier les variantes très performantes plus rapidement qu’un [test A/B traditionnel]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
- Testez plus fréquemment et avec une plus grande confiance que vos utilisateurs verront votre meilleur message. 

La sélection intelligente fonctionne mieux pour les campagnes qui sont envoyées plusieurs fois. Il a besoin de données de performance précoces pour commencer à optimiser, de sorte que les campagnes à envoi unique n'en bénéficieront pas. Pour ces campagnes, nous vous recommandons plutôt d'utiliser un [test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) traditionnel.

## Conditions préalables

{% tabs %}
{% tab Campagne %}
Avant d'ajouter la sélection intelligente à votre campagne, assurez-vous que vous avez correctement implémenté les choses :

- Votre campagne est envoyée selon une planification récurrente. Les campagnes à envoi unique ne sont pas prises en charge.
- Vous avez ajouté au moins deux variantes de message.
- Vous avez défini un événement de conversion pour mesurer les performances des variantes.
- La fenêtre de réadmissibilité est fixée à 24 heures ou plus. Les fenêtres plus courtes ne sont pas prises en charge, car elles affecteraient l'intégrité de la variante de contrôle. Pour en savoir plus, consultez la [FAQ sur le renseignement.]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection)
{% endtab %}

{% tab Canvas %}
Pour utiliser la sélection intelligente dans un canvas, confirmez les points suivants :
- Votre canvas comprend au moins deux variantes de messages dans une étape du canvas.
- Vous avez ajouté au moins un événement de conversion.
{% endtab %}
{% endtabs %}

## Ajout d'une sélection intelligente

Vous pouvez ajouter la sélection intelligente à vos campagnes et à vos canevas.

{% tabs %}
{% tab Campagne %}
La sélection intelligente peut être ajoutée à n'importe quelle campagne multi-envoi dans l'étape **Audiences ciblées** du compositeur de campagne de Braze. Les campagnes qui n'envoient qu'une seule fois ne peuvent pas bénéficier de cette fonctionnalité.

{% alert note %}
La sélection intelligente ne peut pas être utilisée dans les campagnes dont la période de rééligibilité est inférieure à 24 heures, car elle affecterait l'intégrité de la variante de contrôle. Pour en savoir plus, consultez la [FAQ sur le renseignement.]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection)
{% endalert %}
{% endtab %}

{% tab Canvas %}
Ajoutez au moins un événement de conversion et deux variantes à votre Canvas. Ensuite, sélectionnez l'un des pourcentages de variante à l'étape Créer. 

![Un Canvas avec deux variantes, chacune réglée sur une distribution de variante de 50 %, permettant d'activer la sélection intelligente.]({% image_buster /assets/img/intelligent_selection.png %})

Vous pouvez ainsi modifier la répartition des variantes et activer la sélection intelligente. 

![Option de sélection intelligente activée pour un canvas]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

La sélection intelligente ne sera pas disponible si vous n'avez pas encore ajouté d'événements de conversion à votre Canvas ou si votre campagne est composée d'une variante solo.
{% endtab %}
{% endtabs %}

## Durée d'exécution

Pour les campagnes et les Canvas, la sélection intelligente s’exécutera jusqu’à ce qu’elle rassemble suffisamment de preuves des taux de conversion « réels » des variantes. Le niveau « suffisamment » est déterminé par un indicateur spécial appelé « regret ». Vous pouvez l'assimiler à la confiance dans la mesure où la sélection intelligente se désactive lorsqu'il y a suffisamment de données pour savoir quelle variante est la meilleure. 

Dans la plupart des cas, la sélection intelligente choisira l'une des variantes comme variante gagnante. Cette variante sera envoyée à 100 % de l’audience pour les envois futurs.

{% alert note %}
Il est possible qu’une sélection intelligente s’arrête d’optimiser sans avoir choisi un seul gagnant. La sélection intelligente cesse d'optimiser lorsqu'elle est sûre à 95 % que la poursuite de l'expérience n'améliorera pas le taux de conversion de plus de 1 % par rapport au taux actuel.
{% endalert %}

## Foire aux questions (FAQ) {#faq}

### Pourquoi la rééligibilité dans moins de 24 heures n’est-elle pas disponible lorsqu’elle est associée à une sélection intelligente ?

Nous ne permettons pas aux campagnes de sélection intelligente d’activer la rééligibilité au cours d’une fenêtre trop courte car cela affecterait l’intégrité de la variante de contrôle. En créant un intervalle de 24 heures, nous aidons à garantir que l’algorithme disposera d’un ensemble de données valide statistiquement à partir duquel travailler.

Normalement, les campagnes avec rééligibilité amèneront les utilisateurs à saisir de nouveau la même variante qu’auparavant. Avec une sélection intelligente, Braze ne peut pas garantir qu’un utilisateur recevra la même variante de campagne parce que la distribution de la variante aurait changé en raison de l’aspect d’allocation optimal pour cette fonctionnalité. Si l’utilisateur était autorisé à rentrer à nouveau avant que la sélection intelligente ne réexamine la performance de la variante, les données pourraient être biaisées en raison des utilisateurs étant entrés à nouveau.

Par exemple, si une campagne utilise ces variantes :

- Variante A : 20%
- Variante B : 20%
- Contrôle : 60 %

La distribution de la variante pourrait alors être la suivante au deuxième tour :

- Variante A : 15%
- Variante B : 25 %
- Contrôle : 60 %

### Pourquoi mes variantes de sélection intelligente affichent-elles des envois égaux pendant les premières étapes de ma campagne ?

La sélection intelligente alloue les variantes à envoyer en fonction du statut actuel de conversion de la campagne. Elle détermine uniquement les attributions de variantes finales après une période de formation durant laquelle les envois sont réalisés de manière uniforme entre les variantes. Si vous ne voulez pas que la sélection intelligente soit envoyée de manière uniforme pendant les premières étapes de votre campagne, utilisez des variantes fixes pour un test A/B traditionnel.

### La sélection intelligente cessera-t-elle d’optimiser sans choisir un gagnant clair ?

La sélection intelligente cessera d’optimiser lorsqu’elle sera sûre à 95 % que la poursuite de l’expérience n’améliorera pas le taux de conversion de plus de 1 % par rapport à son taux actuel.

### Pourquoi ne puis-je pas activer la sélection intelligente dans mon canvas ou ma campagne (grisé) ?

La sélection intelligente ne sera pas disponible si :

- Vous n’avez pas ajouté d’événements de conversion à votre campagne ou Canvas
- Vous créez une campagne à envoi unique
- Vous avez activé la rééligibilité avec une fenêtre de moins de 24 heures
- Votre Canvas est composé d’une seule variante sans ajout de variantes supplémentaires ou de groupes de contrôle
- Votre Canvas est composé d’un seul groupe de contrôle sans ajout de variantes
