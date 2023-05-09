---
nav_title: Ciblage des utilisateurs
article_title: Ciblage des utilisateurs
page_order: 4
tool: Campaigns
page_type: reference
description: "Le présent article de référence couvre les options de ciblage que vous pouvez trouver dans l’étape de ciblage des utilisateurs de la création de campagne."
---

# Ciblage des utilisateurs

> Une fois que vous avez [composé votre campagne][1] et déterminé votre [planification de livraison][2], vous pouvez définir les destinataires cibles de votre campagne sur l’étape **Target Users (Utilisateurs cibles)**. Seuls les utilisateurs qui correspondent à vos critères définis recevront la campagne. Gardez à l’esprit que l’appartenance à un segment exact est toujours calculée juste avant l’envoi du message.

## Options de ciblage

Dans la section **Targeting Options (Options de ciblage)** vous trouverez quelques options pour définir à qui vous pouvez envoyer votre campagne.

### Utilisateurs cibles dans un segment existant {#existing-segment}

Pour cibler les membres d’un segment créé précédemment, sélectionnez un segment depuis la liste déroulante **Target Users by Segment (Utilisateurs cibles par segment)**.

### Utilisateurs cibles dans plusieurs segments existants {#multiple-existing-segment}

Pour cibler les utilisateurs qui appartiennent à plusieurs segments créés précédemment, ajoutez plusieurs segments depuis la liste déroulante **Target Users by Segment (Utilisateurs cibles par segment)**. L’audience cible qui en résulte sera constituée des utilisateurs qui sont à la fois dans le premier segment, le deuxième segment et le troisième segment, etc.

### Cibler les utilisateurs de plusieurs segments et filtres existants {#existing_segment_filter}

Vous pouvez également cibler les utilisateurs d’un ou plusieurs segments créés précédemment qui appartiennent également à des filtres supplémentaires. Après avoir sélectionné vos segments, vous pouvez affiner votre audience dans la section **Additional Filters (Filtres supplémentaires)**. Ceci est démontré dans la capture d’écran suivante qui cible des utilisateurs qui se trouvent dans le segment « Utilisateurs actifs quotidiens », « E-mail non ouverts », et « A réalisé un achat il y a moins de 30 jours ».

![][25]

### Utilisateurs cibles sans segments {#without-segment}

Pour cibler les utilisateurs sans ajouter un segment, vous pouvez utiliser une série de filtres. Cela signifie que vous n’avez pas besoin de cibler une campagne dans un segment préexistant, vous pouvez créer une audience ad hoc lors de la création de campagne en utilisant simplement les filtres supplémentaires et en ne sélectionnant aucun segment dans **Target Users By Segment (Utilisateurs cibles par segment)**. Cela vous permettra de sauter la création de segments lors de l’envoi de campagnes à une audience unique.

![][26]

## Tester votre audience

Après avoir ajouté des segments et des filtres à votre audience, vous pouvez tester si votre audience est configurée comme prévu en [recherchant un utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/user_lookup/) pour confirmer s’il correspond aux critères de l’audience.

![]({% image_buster /assets/img_archive/user_lookup.png %})

## Résumé de l’audience

Une fois que vous avez ajouté des segments ou des filtres pour affiner votre audience, le **Résumé de l’audience** affichera un aperçu des personnes qui sont dans votre audience cible. Vous pouvez ainsi limiter davantage l’audience de votre campagne en définissant un plafond utilisateur maximum ou une [limitation du taux][3] de vitesse de livraison. Pour les campagnes d’e-mail et de notification push, vous pouvez sélectionner le statut d’abonnement et l’état d’abonnement à cibler.

![][27]

## Tests A/B

Dans la section **Tests A/B** vous pouvez configurer un test pour comparer les réponses des utilisateurs à plusieurs versions de la même campagne marketing. Ces versions partagent des objectifs marketing similaires, mais diffèrent en termes de formulation et de style. L’objectif est d’identifier la version de la campagne qui accomplit le mieux vos objectifs marketing. 

Pour plus d’informations et des bonnes pratiques, consultez les [Tests multivariés et A/B][4].

## Statistiques d’audience

Braze fournit des statistiques d’audience détaillées pour les canaux ciblés dans le pied de page.

![][24]

Pour voir quel pourcentage de votre base d’utilisateurs est ciblé ou la valeur à vie (LTV) pour ce segment, cliquez sur **Afficher les statistiques supplémentaires** situé après le pied de page de statistiques.

[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/
[3]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/
[4]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/
[24]: {% image_buster /assets/img_archive/multi_channel_footer.png %}
[25]: {% image_buster /assets/img_archive/target_segmenter.png %}
[26]: {% image_buster /assets/img_archive/additional_filters.png %}
[27]: {% image_buster /assets/img_archive/audience_summary.png %}
