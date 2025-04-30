---
nav_title: Ciblage des utilisateurs
article_title: Ciblage des utilisateurs
page_order: 9
page_type: reference
description: "Cet article de référence explique comment cibler votre audience dans votre campagne et les éditeurs de Canvas."
tool:
    - Campaigns
    - Canvas
---

# Ciblage des utilisateurs

> Déterminer comment cibler vos utilisateurs est l'une des étapes les plus cruciales lors de la création d'une campagne ou d'un Canvas. En comprenant comment segmenter votre audience en fonction de ses comportements, de ses préférences et de ses caractéristiques démographiques, vous pouvez adapter et personnaliser vos messages.

## Création d'une audience ciblée

### Étape 1 : Choisissez les utilisateurs

Sous **Options de ciblage**, vous pouvez utiliser les options suivantes pour choisir les utilisateurs que vous souhaitez cibler pour votre campagne ou Canvas. Seuls les utilisateurs correspondant aux critères que vous avez définis recevront le message. Gardez à l’esprit que l’appartenance à un segment exact est toujours calculée juste avant l’envoi du message.

{% tabs local %}
{% tab segmentation unique %}
Pour cibler les membres d'un segment précédemment créé, sélectionnez un segment dans le menu déroulant sous **Cibler les utilisateurs par segment.**
{% endtab %}

{% tab plusieurs segmentations %}
Pour cibler des utilisateurs appartenant à plusieurs segments créés précédemment, ajoutez plusieurs segments dans le menu déroulant sous **Cibler les utilisateurs par segment.** L’audience cible qui en résulte sera constituée des utilisateurs qui sont à la fois dans le premier segment, le deuxième segment et le troisième segment, etc.
{% endtab %}

{% tab filtres multiples %}
Pour cibler les utilisateurs sans ajouter un segment, vous pouvez utiliser une série de filtres. Il s'agit d'une audience improvisée lors de la création du message, qui vous permet d'ignorer la création de segments lors de l'envoi à des audiences ponctuelles.

![Filtres supplémentaires pour un message qui cible les utilisateurs qui ont ouvert une application pour la dernière fois dans la journée, qui n'ont jamais reçu de campagne ou d'étape du canvas et qui ont effectué un achat il y a moins de 30 jours.]({% image_buster /assets/img_archive/additional_filters.png %}){: style="max-width:70%;"}
{% endtab %}

{% tab segments et filtres %}
Vous pouvez également cibler les utilisateurs d’un ou plusieurs segments créés précédemment qui appartiennent également à des filtres supplémentaires. Après avoir sélectionné vos segments, vous pouvez affiner votre audience dans la section **Additional Filters (Filtres supplémentaires)**. La capture d'écran suivante en témoigne : elle cible les utilisateurs qui font partie du segment "Utilisateurs actifs par jour", du segment "N'ont jamais ouvert d'e-mail" et qui ont effectué un achat il y a plus de 30 jours.

![Options de ciblage pour un message comprenant deux segments et un filtre supplémentaire pour un dernier achat effectué il y a moins de 30 jours.]({% image_buster /assets/img_archive/target_segmenter.png %}){: style="max-width:70%;"}
{% endtab %}
{% endtabs %}

{% alert tip %}
Pour les campagnes d'e-mails, vous pouvez cibler les groupes initiateurs dans la section **Groupes initiateurs**. Notez que les groupes initiateurs ne sont pas disponibles pour les campagnes API, bien que vous puissiez inclure des groupes initiateurs via une entrée déclenchée par API dans une campagne. Pour plus d'informations, voir [Groupes initiateurs]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#seed-groups).
{% endalert %}

### Étape 2 : Testez votre audience

Après avoir ajouté des segments et des filtres à votre audience, vous pouvez tester si votre audience est configurée comme prévu en [recherchant un utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) pour confirmer s'il correspond aux critères de l'audience.

![La section "Recherche d'un utilisateur" avec un bouton "Recherche d'un utilisateur".]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%"}

#### Résumé de l’audience

Le **résumé de l'audience** donne un aperçu des personnes qui font partie de votre audience cible. Ici, vous pouvez limiter davantage votre audience en fixant un nombre maximum d'utilisateurs ou en [limitant la]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) vitesse de [réception/distribution]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/).

![La section "Résumé de l'audience" contient des options permettant de fixer un plafond d'utilisateurs ou une limite de débit pour la réception/distribution.]({% image_buster /assets/img_archive/audience_summary.png %})

#### Tests A/B

Dans la section **Test A/B**, vous pouvez configurer un test pour comparer les réponses des utilisateurs à plusieurs versions de la même campagne marketing. Ces versions partagent des objectifs marketing similaires, mais diffèrent en termes de formulation et de style. L’objectif est d’identifier la version de la campagne qui accomplit le mieux vos objectifs marketing. 

Pour plus d'informations et de bonnes pratiques, consultez les [tests multivariés et A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

#### Statistiques d’audience

Braze fournit des statistiques d’audience détaillées pour les canaux ciblés dans le pied de page. Plus votre base d'utilisateurs est importante, plus le nombre d'**utilisateurs joignables** est une estimation approximative. Le nombre d'utilisateurs joignables peut diminuer si vous utilisez un [groupe de contrôle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) ou si vous configurez l'éligibilité des messages. 

- Pour déterminer le nombre exact d'utilisateurs joignables, sélectionnez [Calculer les statistiques exactes]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics), car vous effectuerez une recherche parmi tous les utilisateurs de votre base.
- Pour connaître le pourcentage de votre base d'utilisateurs ciblé ou la valeur vie client (LTV) de ce segment, sélectionnez **Afficher les statistiques supplémentaires.**
- Pour connaître le pourcentage de votre base d'utilisateurs ciblé ou la valeur vie client (LTV) de ce segment, sélectionnez **Afficher les statistiques supplémentaires.**

![La section "Population totale" avec le nombre estimé d'utilisateurs joignables dans chaque canal ciblé.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

{% alert note %}
Le calcul de statistiques exactes peut prendre quelques minutes. Cette fonction ne calcule les statistiques exactes qu'au niveau du segment, et non au niveau du filtre ou du groupe de filtres.<br><br>
Pour les segments de grande taille, il est normal de constater de légères variations, même en calculant des statistiques exactes. La précision de cette fonctionnalité devrait être égale ou supérieure à 99,999 %.
{% endalert %}

