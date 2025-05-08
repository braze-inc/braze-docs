---
nav_title: Ciblage des utilisateurs
article_title: Ciblage des utilisateurs
page_order: 4
tool: Campaigns
page_type: reference
description: "Cet article de référence couvre les options de ciblage qui se trouvent dans l'étape Audiences cibles de la création d'une campagne."
---

# Ciblage des utilisateurs

> Après avoir [composé votre campagne][1] et déterminé votre [planification de réception/distribution][2], vous pouvez définir les destinataires de votre campagne à l'étape **Publics cibles**. 

## Options de ciblage

Dans la section **Options de ciblage**, vous trouverez quelques options pour savoir à qui vous pouvez envoyer votre campagne.

{% alert note %}
Seuls les utilisateurs qui correspondent à vos critères définis recevront la campagne. Gardez à l’esprit que l’appartenance à un segment exact est toujours calculée juste avant l’envoi du message.
{% endalert %}

### Utilisateurs cibles dans un segment existant {#existing-segment}

Pour cibler les membres d'un segment précédemment créé, sélectionnez un segment dans le menu déroulant sous **Cibler les utilisateurs par segment.**

### Utilisateurs cibles dans plusieurs segments existants {#multiple-existing-segment}

Pour cibler des utilisateurs appartenant à plusieurs segments créés précédemment, ajoutez plusieurs segments dans le menu déroulant sous **Cibler les utilisateurs par segment.** L’audience cible qui en résulte sera constituée des utilisateurs qui sont à la fois dans le premier segment, le deuxième segment et le troisième segment, etc.

### Cibler les utilisateurs dans plusieurs segments et filtres existants {#existing_segment_filter}

Vous pouvez également cibler les utilisateurs d’un ou plusieurs segments créés précédemment qui appartiennent également à des filtres supplémentaires. Après avoir sélectionné vos segments, vous pouvez affiner votre audience dans la section **Additional Filters (Filtres supplémentaires)**. Ceci est démontré dans la capture d’écran suivante qui cible des utilisateurs qui se trouvent dans le segment « Utilisateurs actifs quotidiens », « E-mail non ouverts », et « A réalisé un achat il y a moins de 30 jours ».

![][25]

### Utilisateurs cibles sans segments {#without-segment}

Pour cibler les utilisateurs sans ajouter un segment, vous pouvez utiliser une série de filtres. Cela signifie que vous n'avez pas besoin de cibler une campagne sur un segment préexistant, vous pouvez créer une audience impromptue lors de la création de la campagne en utilisant simplement les filtres supplémentaires et en ne sélectionnant aucun segment sous **Cibler les utilisateurs par segment.** Cela vous permettra de sauter la création de segments lors de l’envoi de campagnes à une audience unique.

![][26]

## Ciblage des groupes initiateurs

Pour les campagnes d'e-mails, vous pouvez cibler les groupes initiateurs dans la section **Groupes initiateurs**. Notez que les groupes initiateurs ne sont pas disponibles pour les campagnes API, bien que vous puissiez inclure des groupes initiateurs via une entrée déclenchée par API dans une campagne. Pour plus d'informations, voir [Groupes initiateurs]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#seed-groups).

## Tester votre audience

Après avoir ajouté des segments et des filtres à votre audience, vous pouvez tester si votre audience est configurée comme prévu en [recherchant un utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) pour confirmer s'il correspond aux critères de l'audience.

![]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:60%"}

## Résumé de l’audience

Une fois que vous avez ajouté des segments ou des filtres pour affiner votre audience, le **résumé de l'audience** vous donnera un aperçu des personnes qui font partie de votre audience cible. Ici, vous pouvez limiter davantage l'audience de votre campagne en fixant un nombre maximum d'utilisateurs ou en [limitant la vitesse][3] de livraison. Pour les campagnes d’e-mail et de notification push, vous pouvez sélectionner le statut d’abonnement et l’état d’abonnement à cibler.

![][27]

## Tests A/B

Dans la section **Test A/B**, vous pouvez configurer un test pour comparer les réponses des utilisateurs à plusieurs versions de la même campagne marketing. Ces versions partagent des objectifs marketing similaires, mais diffèrent en termes de formulation et de style. L’objectif est d’identifier la version de la campagne qui accomplit le mieux vos objectifs marketing. 

Pour plus d'informations et de bonnes pratiques, consultez les [tests multivariés et A/B][4].

## Statistiques d’audience

Braze fournit des statistiques d’audience détaillées pour les canaux ciblés dans le pied de page. 

Plus votre base d'utilisateurs est importante, plus le nombre d'**utilisateurs joignables** est une estimation approximative. Le nombre d'utilisateurs joignables peut diminuer si vous utilisez un [groupe de contrôle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) ou si vous configurez l'éligibilité des messages. Sélectionnez [Calculer les statistiques exactes]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics) pour déterminer un nombre précis d'utilisateurs joignables, car la recherche se fera sur tous les utilisateurs de votre base. 

Remarques :

- Le calcul de statistiques exactes peut prendre quelques minutes. Cette fonction ne calcule les statistiques exactes qu'au niveau du segment, et non au niveau du filtre ou du groupe de filtres.
- Pour les segments de grande taille, il est normal de constater de légères variations, même en calculant des statistiques exactes. La précision de cette fonctionnalité devrait être égale ou supérieure à 99,999 %.

![][24]

Pour connaître le pourcentage de votre base d'utilisateurs ciblé ou la valeur vie client (LTV) de ce segment, sélectionnez **Afficher les statistiques supplémentaires.**

[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/
[3]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/
[4]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/
[24]: {% image_buster /assets/img_archive/multi_channel_footer.png %}
[25]: {% image_buster /assets/img_archive/target_segmenter.png %}
[26]: {% image_buster /assets/img_archive/additional_filters.png %}
[27]: {% image_buster /assets/img_archive/audience_summary.png %}
