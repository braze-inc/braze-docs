---
nav_title: Sélection intelligente
article_title: Sélection intelligente
page_order: 1.0
description: "Cet article traite de la sélection intelligente, une fonctionnalité qui analyse les performances d'une campagne récurrente ou d'un Canvas deux fois par jour et ajuste automatiquement le pourcentage d'utilisateurs qui reçoivent chaque variante de message."
search_rank: 10
toc_headers: h2
---

# Sélection intelligente {#intelligent-selection}

> La sélection intelligente est une fonctionnalité qui analyse les performances d'une campagne récurrente ou d'un Canvas deux fois par jour et ajuste automatiquement le pourcentage d'utilisateurs qui reçoivent chaque variante de message. 

## À propos de la sélection intelligente

Une variante qui semble plus performante que les autres sera envoyée à un plus grand nombre d'utilisateurs, tandis que les variantes moins performantes seront ciblées sur un plus petit nombre d'utilisateurs. Chaque Adjust est effectué à l'aide d'un [algorithme statistique](https://en.wikipedia.org/wiki/Multi-armed_bandit) qui garantit que Braze s'adapte à de réelles différences de performances et pas seulement au hasard.

!section de test A/B d'une campagne où la sélection intelligente est activée.]({% image_buster /assets/img/intelligent_selection1.png %})

La sélection intelligente le fera :
- Examinez à plusieurs reprises les données de performance et déplacez progressivement le trafic de la campagne vers les variantes gagnantes.
- Vérifiez que davantage d'utilisateurs reçoivent votre variante la plus performante sans sacrifier la confiance statistique.
- Éliminez les variantes peu performantes et identifiez les variantes performantes plus rapidement qu'un [test A/B traditionnel.]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)
- Testez plus fréquemment et avec une plus grande confiance que vos utilisateurs verront votre meilleur message. 

La sélection intelligente fonctionne mieux pour les campagnes qui sont envoyées plusieurs fois. Il a besoin de données de performance précoces pour commencer à optimiser, de sorte que les campagnes à envoi unique n'en bénéficieront pas. Pour ces campagnes, nous vous recommandons plutôt d'utiliser un [test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) traditionnel.

## Conditions préalables

{% tabs %}
{% tab Campaign %}
Avant d'ajouter la sélection intelligente à votre campagne, assurez-vous que vous avez correctement implémenté les choses :

- Votre campagne est envoyée selon une planification récurrente. Les campagnes à envoi unique ne sont pas prises en charge.
- Vous avez ajouté au moins deux variantes de message.
- Vous avez défini un événement de conversion pour mesurer les performances des variantes.
- La fenêtre de réadmissibilité est fixée à 24 heures ou plus. Les fenêtres plus courtes ne sont pas prises en charge, car elles affecteraient l'intégrité de la variante de contrôle. Pour en savoir plus, consultez [cette FAQ.]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection)
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
{% tab Campaign %}
La sélection intelligente peut être ajoutée à n'importe quelle campagne multi-envoi dans l'étape **Audiences ciblées** du compositeur de campagne de Braze. Les campagnes qui n'envoient qu'une seule fois ne peuvent pas bénéficier de cette fonctionnalité.

{% alert note %}
La sélection intelligente ne peut pas être utilisée dans les campagnes dont la période de rééligibilité est inférieure à 24 heures, car elle affecterait l'intégrité de la variante de contrôle. Pour en savoir plus, consultez la [FAQ sur le renseignement.]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection)
{% endalert %}
{% endtab %}

{% tab Canvas %}
Ajoutez au moins un événement de conversion et deux variantes à votre Canvas. Ensuite, sélectionnez l'un des pourcentages de variante à l'étape Créer. 

Une toile avec deux variantes, chacune réglée sur une distribution de 50 % des variantes, permettant d'activer la sélection intelligente.]({% image_buster /assets/img/intelligent_selection.png %})

Vous pouvez ainsi modifier la répartition des variantes et activer la sélection intelligente. 

L'option de sélection intelligente a été activée pour un canvas.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

La sélection intelligente ne sera pas disponible si vous n'avez pas encore ajouté d'événements de conversion à votre Canvas ou si votre campagne est composée d'une variante solo.
{% endtab %}
{% endtabs %}

## Durée d'exécution

Pour les campagnes et les canevas, la sélection intelligente fonctionnera jusqu'à ce qu'elle recueille suffisamment de preuves sur les "vrais" taux de conversion des variantes. Le terme "assez" est déterminé par un indicateur spécial appelé "regret". Vous pouvez l'assimiler à la confiance dans la mesure où la sélection intelligente se désactive lorsqu'il y a suffisamment de données pour savoir quelle variante est la meilleure. 

Dans la plupart des cas, la sélection intelligente choisira l'une des variantes comme variante gagnante. Cette variante recevra 100 % de l'audience pour les envois futurs.

{% alert note %}
Il est possible que la sélection intelligente cesse d'optimiser sans désigner un seul vainqueur. La sélection intelligente cesse d'optimiser lorsqu'elle est sûre à 95 % que la poursuite de l'expérience n'améliorera pas le taux de conversion de plus de 1 % par rapport au taux actuel.
{% endalert %}

## Sélection intelligente distribution variante

La sélection intelligente base la répartition des variantes sur l'état actuel des conversions de la campagne. Il ne détermine les distributions finales qu'après la période de formation. 

Cela signifie qu'au cours des premières phases de la campagne, les sélections intelligentes à 99 % et à 1 % peuvent recevoir des envois à peu près égaux, mais que les pourcentages finaux pour l'attribution des variantes peuvent être fixés à 99 %-1 %.

Si vous ne souhaitez pas que la sélection intelligente envoie 50/50 au cours des premières étapes de la campagne, nous vous recommandons d'utiliser un test A/B traditionnel avec des variantes fixes.

## Questions fréquemment posées {#faq}

### Pourquoi la rééligibilité en moins de 24 heures n'est-elle pas disponible lorsqu'elle est combinée à la sélection intelligente ?

Nous ne permettons pas aux campagnes de sélection intelligente de bénéficier d'une rééligibilité dans un délai trop court, car cela affecterait l'intégrité de la variante de contrôle. En créant un écart de 24 heures, nous contribuons à garantir que l'algorithme disposera d'un ensemble de données statistiquement valides pour travailler.

Normalement, les campagnes avec rééligibilité amènent les utilisateurs à saisir à nouveau la même variante que celle qu'ils ont reçue auparavant. Avec la sélection intelligente, Braze ne peut pas garantir qu'un utilisateur recevra la même variante de campagne parce que la distribution des variantes aurait changé en raison de l'aspect d'allocation optimale de cette fonctionnalité. Si l'utilisateur était autorisé à se réinscrire avant que la sélection intelligente ne réexamine les performances de la variante, les données pourraient être faussées en raison des utilisateurs qui se sont réinscrits.

Par exemple, si une campagne utilise les variantes suivantes :

- Variante A : 20%
- Variante B : 20%
- Contrôle : 60%

La distribution des variantes pourrait alors être la suivante pour le second tour :

- Variante A : 15%
- Variante B : 25%
- Contrôle : 60%

### Pourquoi mes variantes de sélection intelligente affichent-elles des envois égaux au cours des premières étapes de ma campagne ?

La sélection intelligente attribue les variantes à envoyer en fonction de l'état actuel de la conversion de la campagne. Il ne détermine les attributions finales de variantes qu'après une période de formation, au cours de laquelle les envois sont répartis de manière égale entre les variantes. Si vous ne souhaitez pas que la sélection intelligente envoie uniformément au cours des premières étapes de votre campagne, utilisez des variantes fixes pour un test A/B traditionnel.

### La sélection intelligente cessera-t-elle d'optimiser sans désigner un vainqueur clair ?

La sélection intelligente arrête l'optimisation lorsqu'elle est sûre à 95 % que la poursuite de l'expérience n'améliorera pas le taux de conversion de plus de 1 % par rapport au taux actuel.

### Pourquoi ne puis-je pas activer la sélection intelligente dans mon canvas ou ma campagne (grisé) ?

La sélection intelligente n'est pas disponible si :

- Vous n'avez pas ajouté d'événements de conversion à votre campagne ou à Canvas.
- Vous créez une campagne à envoi unique
- Vous avez activé la rééligibilité avec une fenêtre de moins de 24 heures
- Votre Canvas est composé d'une seule variante, sans ajout de variante supplémentaire ni de groupe de contrôle.
- Votre Canvas est composé d'un seul groupe de contrôle, sans aucune variante ajoutée
