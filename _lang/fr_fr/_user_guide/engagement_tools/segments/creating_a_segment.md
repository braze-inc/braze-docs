---
nav_title: "Création d'une segmentation"
article_title: "Création d'une segmentation"
page_order: 0
page_type: tutorial
description: "Cet article pratique vous explique comment configurer et créer une segmentation à l'aide de Braze."
tool: Segments
search_rank: 3
---

# ![cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"} Création d'un segment

> La segmentation vous permet de cibler les utilisateurs en fonction de leurs caractéristiques et actions démographiques, comportementales ou techniques. L'utilisation créative et intelligente de la segmentation et de l'automatisation de l'envoi des messages vous permet de faire passer de façon fluide/sans heurts vos utilisateurs du statut de premier contact à celui de client à long terme. Les segments sont mis à jour en temps réel en fonction de l'évolution des données, et vous pouvez créer autant de segments que nécessaire pour vos objectifs de ciblage et d'envoi de messages.

## Étape 1 : Naviguez jusqu'à la section des segments

Allez dans **Audience** > Segments.

## Étape 2 : Nommez votre segmentation

Sélectionnez **Créer un segment** pour commencer à créer votre segment. Nommez votre segmentation en décrivant le type d'utilisateur que vous avez l'intention de filtrer. Cela vous aidera à identifier le segment lorsque vous voudrez le cibler pour vos campagnes ou Canevas. Les titres vagues des segments peuvent prêter à confusion.

En option, vous pouvez effectuer les opérations suivantes :
- Ajoutez une description au segment pour fournir plus de détails sur l'intention de cette audience et laissez des notes auxquelles les autres membres de l'équipe pourront se référer.
- Ajoutez une [équipe]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) à votre segmentation.
- Ajoutez des [étiquettes]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) à votre segmentation pour mieux l'organiser.

\![Fenêtre modale Créer un segment où le segment est nommé "Utilisateurs déchus" avec la description du segment comme "Ceci est notre principal segment d'utilisateurs déchus pour cibler les non-actifs dans les quatorze derniers jours" avec deux boutons : Annuler et Créer un segment.]({% image_buster /assets/img_archive/segment_app_selection.png %}){: style="max-width:80%;"}

## Étape 3 : Choisissez votre application ou plateforme

Choisissez les applications ou les plateformes que vous souhaitez cibler en sélectionnant **Utilisateurs de toutes les applications** (par défaut) ou **Utilisateurs d'applications spécifiques.** **Utilisateurs d'apps spécifiques** cible les utilisateurs ayant au moins une session dans les apps spécifiées.

Par exemple, si vous souhaitez envoyer un message in-app aux seuls appareils iOS, sélectionnez votre application iOS. Ainsi, les utilisateurs qui pourraient utiliser à la fois un appareil iOS et un appareil Android ne recevront le message que sur leur appareil iOS. Dans la liste des apps spécifiques, l'option **Utilisateurs ne provenant d'aucune app** vous permet d'inclure des utilisateurs sans sessions ni données d'apps (généralement créés via l'importation d'utilisateurs ou l'API REST).

!panneau Détails du segment avec l'option "Utilisateurs de toutes les applications" sélectionnée dans la section Apps utilisées.]({% image_buster /assets/img_archive/Segment2.png %}){: style="max-width:80%;"}

## Étape 4 : Ajouter des filtres à votre segmentation

Ajoutez au moins un filtre à votre segmentation. Vous pouvez combiner autant de filtres que vous le souhaitez pour rendre votre segmentation plus spécifique. 

{% alert note %}
Braze ne génère pas de profil utilisateur tant que les utilisateurs n'ont pas utilisé l'application pour la première fois. Vous ne pouvez donc pas cibler les utilisateurs qui n'ont pas encore ouvert votre application.
{% endalert %}

#### Groupes de filtres

Les filtres sont organisés en groupes de filtres. Chaque filtre doit faire partie d'un groupe de filtres comprenant au minimum un filtre. Un segment peut avoir plusieurs groupes de filtres. Pour en ajouter un, sélectionnez **Ajouter un groupe de filtres**. Modifiez le nom du groupe de filtres en sélectionnant l'icône qui apparaît lorsque vous passez la souris à côté.

\![Groupe de filtrage avec une icône de modification à côté de son nom.]({% image_buster /assets/img_archive/edit_filter_group_name.png %})

Sélectionnez les icônes situées à côté de chaque filtre pour réduire l'éditeur de filtres ou dupliquer des filtres individuels. Après avoir dupliqué un filtre, vous pouvez ajuster ses valeurs dans chaque liste déroulante.

#### Logique de segmentation utilisant AND et OR

Au sein d'un groupe de filtres, les filtres peuvent être reliés par "ET" ou "OU". Entre les groupes de filtrage, les groupes peuvent être reliés par "AND" ou "OR". Lorsque vous utilisez des groupes de filtres, vous pouvez créer une logique de segmentation, par exemple :
- (A ET B ET C) OU (C ET E ET F)
- (A OU B OU C) ET (C OU D OU F)

Si vous sélectionnez "OU" pour vos filtres, votre segmentation contiendra des utilisateurs répondant à n'importe quelle combinaison d'un, de plusieurs ou de tous ces filtres. Si vous sélectionnez "ET", les utilisateurs qui ne passent pas ce filtre ne seront pas inclus dans votre segmentation.

{% alert tip %}
Lorsque vous sélectionnez "OU" pour les filtres qui incluent un filtre négatif (tel que "n'est pas" dans un groupe d'abonnement), n'oubliez pas que les utilisateurs ne doivent remplir qu'un seul des filtres "OU" pour être inclus dans la segmentation. Pour appliquer le filtre négatif indépendamment des autres filtres, utilisez un [groupe d'exclusion](#exclusion).
{% endalert %}

{% details When to avoid the OR operator %}

Dans certaines situations de ciblage de l'utilisateur, l'utilisation de l'opérateur `OR` peut être évitée. L'opérateur `OR` crée une instruction qui s'avère vraie si un utilisateur répond aux critères d'un ou de plusieurs filtres d'une instruction. Par exemple, si vous souhaitez créer un segment d'utilisateurs qui appartiennent à la catégorie "Foodies" mais qui n'appartiennent ni à la catégorie "Non-foodies" ni à la catégorie "Candy-lovers", vous pouvez utiliser l'opérateur `OR`.

\![Filtrer le groupe pour les utilisateurs dans le segment "foodies" et non dans les segments "non-foodies" ou "candy-lovers".]({% image_buster /assets/img_archive/or_operator_segment.png %})

Cependant, si votre objectif est de segmenter les utilisateurs qui appartiennent au segment "Foodies" et ne font partie d'aucun des segments "Non-foodies" et "Candy-lovers", utilisez l'opérateur `AND`. De cette manière, les utilisateurs qui reçoivent la campagne ou le canvas font partie du segment visé ("foodies") et non des autres segments ("Non-foodies" et "Candy-lovers") en même temps. 

Les critères de ciblage négatifs suivants ne doivent pas être utilisés avec l'opérateur `OR` lorsque deux filtres ou plus font référence au même attribut :

- `not included`
- `is not`
- `does not equal`
- `does not match regex`

Si `not included`, `is not`, `does not equal`, ou `does not match regex` sont utilisés avec l'opérateur `OR` deux fois ou plus dans une déclaration, les utilisateurs ayant toutes les valeurs de l'attribut concerné seront ciblés.

{% enddetails %}

#### Opérateurs de filtrage

Selon le filtre spécifique que vous sélectionnez, vous disposerez de différents opérateurs pour identifier les valeurs du filtre. Pour en savoir plus sur les opérateurs disponibles pour les différents types d'attributs personnalisés, reportez-vous à la section [Stockage des attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#setting-custom-attributes). Notez que lorsque vous utilisez l'opérateur "is any of", le nombre maximum d'éléments que vous pouvez inclure dans ce champ est de 256.

{% alert note %}
Braze ne génère pas de profil utilisateur tant que les utilisateurs n'ont pas utilisé l'application pour la première fois. Vous ne pouvez donc pas cibler les utilisateurs qui n'ont pas encore ouvert votre application.
{% endalert %}

\![La segmentation filtre les groupes avec l'opérateur AND.]({% image_buster /assets/img_archive/segmenter_filter_groups.png %})

{% alert important %}
Les segments utilisant déjà le filtre d'**appartenance à un segment** ne peuvent pas être inclus ou imbriqués dans d'autres segments. Cela permet d'éviter un cycle dans lequel le segment A inclut le segment B, qui essaie ensuite d'inclure à nouveau le segment A. Dans ce cas, la segmentation ne cesserait de se référer à elle-même, ce qui rendrait impossible le calcul de la personne qui en fait partie.

En outre, l'imbrication de segments de ce type ajoute de la complexité et peut ralentir les choses. Au lieu de cela, recréez le segment que vous essayez d'inclure en utilisant les mêmes filtres.
{% endalert %}

#### Groupes d'exclusion (facultatif) {#exclusion}

Lorsque vous créez un segment, vous pouvez appliquer un ou plusieurs groupes d'exclusion. Les groupes d'exclusion contiennent des critères qui identifient les utilisateurs à exclure de votre segmentation, et seront toujours reliés à vos groupes de filtrage avec un opérateur "ET NON".

Les groupes d'exclusion ont la priorité sur les critères de segmentation. Si un utilisateur entre dans les critères de votre groupe d'exclusion, il ne fera pas partie de votre segmentation, même s'il répond aux critères de vos groupes de filtrage.

Créez un groupe d'exclusion en ajoutant des filtres comme vous le feriez pour les groupes de filtres. La statistique _Utilisateurs joignables estimés_ dans un groupe d'exclusion indique le nombre estimé d'utilisateurs restant dans votre segmentation après l'application des critères d'exclusion.

Les utilisateurs exclus ne seront pas comptabilisés dans les statistiques du _nombre total d'utilisateurs joignables_ de votre segmentation.

\![Un groupe d'exclusion avec deux filtres.]({% image_buster /assets/img_archive/segmenter_exclusion_groups.png %})

#### Visualisation des statistiques de l'entonnoir

Sélectionnez **Afficher les statistiques de l'entonnoir** pour afficher les statistiques de ce groupe de filtres et voir l'impact de chaque filtre ajouté sur les statistiques de votre segmentation. Vous obtiendrez une estimation du nombre et du pourcentage d'utilisateurs ciblés par tous les filtres jusqu'à ce point. Une fois que les statistiques sont affichées pour un groupe de filtres, elles sont automatiquement mises à jour lorsque vous modifiez les filtres. Ces statistiques sont estimées et peuvent prendre un certain temps pour être générées.

Gardez à l'esprit que si vous utilisez AND entre vos filtres, les statistiques de l'entonnoir diminueront ; si vous utilisez OR entre vos filtres, les statistiques de l'entonnoir augmenteront.

!Deux filtres avec des statistiques sur l'entonnoir des segments.]({% image_buster /assets/img_archive/segment_funnel_statistics.png %})

En ajoutant des filtres qui documentent votre flux d'utilisateurs, vous pouvez voir les points où les utilisateurs décrochent. Par exemple, si vous êtes une application de réseau social et que vous souhaitez voir où vous pourriez perdre des utilisateurs au cours de votre processus d'onboarding, vous pouvez ajouter des filtres de données personnalisés pour l'inscription, l'ajout d'amis et l'envoi du premier message. Si vous constatez que 85 % des utilisateurs s'inscrivent et ajoutent des amis, mais que seuls 45 % d'entre eux envoient le premier message, vous saurez qu'il faut encourager l'envoi d'un plus grand nombre de messages lors de vos campagnes d'onboarding et de marketing.

#### Segments d'essai

Après avoir ajouté des applications et des filtres à votre segment, vous pouvez tester si votre segment est configuré comme prévu en recherchant un utilisateur pour confirmer s'il correspond aux critères de segmentation. Pour ce faire, recherchez le `external_id` ou le `braze_id` d'un utilisateur dans la section **Recherche d'utilisateurs**. Notez que vous ne pouvez pas effectuer de recherche d'**utilisateurs** par adresse e-mail dans la **recherche d'utilisateurs**.

\![Section de recherche d'utilisateurs avec un champ de recherche.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%;"}

La recherche d'utilisateur est disponible lorsque :
- Création d'une segmentation
- Implémenter une campagne ou une audience Canvas
- Mise en place d'une étape de parcours d'audience

Lorsqu'un utilisateur correspond aux critères de segmentation, de filtrage et d'application, une alerte l'indique.

Une recherche de l'utilisateur "testuser" déclenche une alerte indiquant que "testuser correspond à tous les segments, filtres et applications".]({% image_buster /assets/img_archive/user_lookup_match.png %})

Lorsqu'un utilisateur ne correspond pas à tout ou partie des critères de segmentation, de filtrage ou d'application, les critères manquants sont répertoriés à des fins de résolution des problèmes.

Une recherche utilisateur avec une alerte indiquant "test1 ne correspond pas aux critères de ciblage suivants :" et affichant les critères manquants.]({% image_buster /assets/img_archive/user_lookup_nomatch.png %})

#### Segmentations pour utilisateurs uniques

Vous pouvez créer des segments d'utilisateurs uniques (ou des segments d'une poignée d'utilisateurs) en utilisant des attributs uniques qui identifient les utilisateurs, comme un nom d'utilisateur ou un ID d'utilisateur.

Cependant, les statistiques de segmentation ou l'aperçu peuvent ne pas montrer cet utilisateur individuel parce que les statistiques de segmentation sont calculées sur la base d'un échantillon aléatoire avec un intervalle de confiance de 95 % selon lequel le résultat se situe dans une fourchette de +/- 1 %. Plus votre base d'utilisateurs est importante, plus il est probable que la taille de votre segment soit une estimation approximative. Pour vous assurer que votre segmentation contient bien l'utilisateur unique que vous ciblez, sélectionnez **Calculer les statistiques exactes**. Cela permettra de calculer le nombre exact d'utilisateurs dans votre segmentation avec une précision supérieure à 99,999 %.

Braze dispose de filtres de test permettant de cibler des utilisateurs spécifiques en fonction de leur ID ou de leur adresse e-mail.

## Étape 5 : Enregistrez votre segmentation

Sélectionnez **Enregistrer**. Vous êtes maintenant prêt à envoyer des messages à vos utilisateurs !

## Mesurer la taille des segments

Pour en savoir plus sur le suivi de la composition et de la taille de votre segmentation, reportez-vous à la section [Mesurer la taille d'un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/).

## Archivage des segments

Si vous n'avez plus besoin d'un segment spécifique ou si vous souhaitez le retirer, vous pouvez l'archiver en accédant à la page **Segments** et en sélectionnant **Archiver** dans le menu de la ligne de ce segment.

{% alert warning %}
Lorsque vous archivez un segment, toutes les campagnes ou Canvas qui l'utilisent (même si le segment n'est utilisé que dans un seul composant Canvas) seront également archivés. Cela inclut également les segments imbriqués où les deux segments et toutes les campagnes ou canevas qui les utilisent seront également archivés.
<br><br>
Vous recevrez un avertissement indiquant les campagnes et les toiles sur le point d'être archivées par l'archivage du segment associé.
{% endalert %}

Vous pouvez désarchiver le segment en naviguant jusqu'à lui dans la page **Segments**, puis en sélectionnant **Désarchiver**.

## Ciblage des comportements lorsque les utilisateurs disposent de plusieurs appareils.

Les utilisateurs disposent de plusieurs appareils s'ils se connectent au même compte sur plusieurs appareils. Vous pouvez vérifier la présence de plusieurs appareils dans la section **Appareils récents** d'un [profil utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/).

Lorsque vous effectuez une segmentation avec des filtres dépendant de l'appareil (modèle d'appareil, système d'exploitation de l'appareil et version de l'application), votre segment contiendra tous les utilisateurs qui correspondent à vos critères de segmentation. Ces utilisateurs recevront un message sur tous leurs appareils, y compris ceux qui ne répondent peut-être pas à vos critères de filtrage. Par exemple, supposons que l'utilisateur A possède deux appareils : L'appareil 1 est équipé du système d'exploitation 13.0 et l'appareil 2 du système d'exploitation 10.0. Si un segment cible les utilisateurs dotés du système d'exploitation 10.0, cet utilisateur fera partie de ce segment et recevra des messages sur ses deux appareils.

### Notifications push

Vous pouvez spécifier qu'une seule notification push est envoyée à chaque utilisateur. Lorsque vous [rédigez votre message]({{ssite.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message#step-4-compose-your-push-message), sélectionnez l'option **N'envoyer qu'au dernier appareil utilisé par l'utilisateur** sous **Paramètres supplémentaires.**

\!["Paramètres supplémentaires" avec une case à cocher pour l'envoi uniquement vers le dernier appareil utilisé par l'utilisateur.]({% image_buster /assets/img_archive/send_to_last_device.png %}){: style="max-width:60%;"}

### Considérations

- **Les messages envoyés peuvent dépasser la taille de l'audience.** Lorsque certains utilisateurs possèdent plusieurs appareils, chaque appareil peut recevoir un message. Le nombre d'envois de messages est donc supérieur à celui des utilisateurs de votre segmentation.
- **L'appartenance d'un utilisateur à un segment peut être différente de ce à quoi vous vous attendez.**
    - Un utilisateur peut être ciblé sur son appareil actuel en fonction des attributs associés à un autre appareil. Si vous ne vous attendiez pas à ce qu'un utilisateur reçoive un message, vérifiez si son profil utilisateur comporte plusieurs appareils.
    - Un utilisateur peut avoir fait partie de votre segmentation cible au moment de l'envoi, mais en raison de comportements associés à l'un ou l'autre de ses appareils, il peut ne plus faire partie de ce segment par la suite. Un utilisateur peut ainsi recevoir une campagne ou un Canvas alors qu'il ne correspond pas aux critères de filtrage. <br><br>Par exemple, un utilisateur pourrait recevoir un message ciblant les utilisateurs dont la version la plus récente de l'application est OS 10.0, même s'ils ont actuellement OS 13.0. Dans ce cas, l'utilisateur avait le système d'exploitation 10.0 au moment de l'envoi du message et a ensuite effectué une mise à niveau vers le système d'exploitation 13.0.<br><br> De même, si un utilisateur utilise ultérieurement un appareil avec une version d'application différente, son profil utilisateur sera mis à jour avec une nouvelle version d'application la plus récente. Cela peut donner l'impression que l'utilisateur n'aurait pas dû se qualifier pour le message, même s'il s'est qualifié au moment de l'envoi.


