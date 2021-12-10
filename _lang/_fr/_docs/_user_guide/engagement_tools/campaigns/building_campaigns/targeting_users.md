---
nav_title: Utilisateurs ciblés
article_title: Utilisateurs ciblés
page_order: 4
tool: Campagnes
page_type: Référence
description: "Cet article de référence couvre l'étape de création de campagne des utilisateurs ciblés."
---

# Cibler les utilisateurs

Une fois que vous avez [composé votre campagne][1] et déterminé votre [calendrier de livraison][2], vous pouvez définir les destinataires cibles de votre campagne à l'étape **Utilisateurs cibles**. Seuls les utilisateurs qui correspondent à vos critères définis recevront la campagne. Gardez à l'esprit que l'adhésion exacte au segment est toujours calculée juste avant l'envoi du message.

## Options de ciblage

Dans la section **Options de ciblage** , vous trouverez quelques options pour qui vous pouvez envoyer votre campagne.

### Utilisateurs cibles dans un segment existant {#existing-segment}

Pour cibler les membres d'un segment créé précédemment, sélectionnez un segment dans la liste déroulante sous **Utilisateurs cibles par segment**.

### Utilisateurs cibles dans plusieurs segments existants {#multiple-existing-segment}

Pour cibler les utilisateurs qui tombent dans plusieurs segments précédemment créés, ajoutez plusieurs segments à partir du menu déroulant sous **Utilisateurs cibles par Segment**. Le public cible qui en résultera sera les utilisateurs du premier segment et du deuxième segment et du troisième segment, etc.

### Utilisateurs cibles dans plusieurs segments et filtres existants {#existing_segment_filter}

Vous pouvez également cibler les utilisateurs d'un ou de plusieurs segments précédemment créés qui tombent également sous des filtres supplémentaires. Après avoir d'abord sélectionné vos segments, vous pouvez affiner davantage votre public dans la section **Filtres supplémentaires**. Ceci est démontré dans la capture d'écran ci-dessous, qui cible les utilisateurs qui sont dans le segment Utilisateurs Actifs Quotidiens, Pas ouvrir le segment des E-mails, et a fait un achat il y a moins de 30 jours.

!\[Pied de page multicanal\]\[25\]

### Utilisateurs cibles sans segments {#without-segment}

Pour cibler les utilisateurs sans ajouter un segment, vous pouvez utiliser une série de filtres. Cela signifie que vous n'avez pas besoin de cibler une campagne sur un segment préexistant, vous pouvez faire une audience ad hoc lors de la création de la campagne en utilisant simplement les filtres supplémentaires, et ne sélectionnant aucun segment sous **Utilisateurs cibles par segment**. Cela vous permettra d'ignorer la création de segment lors de l'envoi de campagnes à un public unique.

!\[Utilisateurs cibles avec seulement des filtres\]\[26\]

## Résumé de l'audience

Une fois que vous avez ajouté des segments ou des filtres pour affiner votre public, le **Résumé de l'audience** affichera un aperçu de qui se trouve dans votre public cible. Ici, vous pouvez limiter davantage l'audience de votre campagne en définissant une limite maximale d'utilisateur, ou [limitant la vitesse de livraison de][3]. Pour les campagnes de notification par e-mail et push, vous pouvez choisir quel abonnement et quel statut opt-in à cibler.

!\[Résumé de l'audience\]\[27\]

## Tests A/B

Dans la section **A/B Testing** , vous pouvez configurer un test pour comparer les réponses des utilisateurs à plusieurs versions de la même campagne marketing. Ces versions partagent des objectifs de marketing similaires, mais diffèrent en termes de formulation et de style. L'objectif est d'identifier la version de la campagne qui réalise le mieux vos objectifs marketing.

Pour plus d'informations et de meilleures pratiques, reportez-vous à [Tests multivariés & A/B][4].

## Statistiques de l'audience

Braze fournit des statistiques détaillées sur les chaînes ciblées dans le pied de page.

!\[Segmenter\]\[24\]

Afin de voir quel pourcentage de votre base d'utilisateurs est ciblé ou la valeur à vie (LTV) pour ce segment, cliquez sur **Afficher les statistiques supplémentaires** situées en dessous du pied de page des statistiques.
[24]: {% image_buster /assets/img_archive/multi_channel_footer.png %} [25]: {% image_buster /assets/img_archive/target_segmenter. ng %} [26]: {% image_buster /assets/img_archive/additional_filters.png %} [27]: {% image_buster /assets/img_archive/audience_summary.png %}

[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/
[3]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/
[4]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/
