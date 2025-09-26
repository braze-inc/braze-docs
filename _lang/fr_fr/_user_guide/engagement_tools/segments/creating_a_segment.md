---
nav_title: Créer un segment
article_title: Créer un segment
page_order: 0
page_type: tutorial
description: "Cet article pratique vous explique comment configurer et créer un segment avec Braze."
tool: Segments
search_rank: 3
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}Création d’un segment

> La segmentation vous permet de cibler les utilisateurs en fonction de leurs actions et de leurs caractéristiques démographiques, comportementales, ou techniques. La segmentation et l’envoi de messages automatiques peuvent être utilisés de manière intelligente et créative pour transformer vos prospects en clients à long terme de manière harmonieuse. Les segments sont mis à jour en temps réel en fonction des modifications de données, et vous pouvez créer autant de segments que nécessaire pour remplir vos objectifs de ciblage et de communication.

## Étape 1 : Accédez à la section Segments

Sélectionnez **Audience** > **Segments**.

## Étape 2 : Nommez votre segment

Sélectionnez **Créer un segment** pour commencer à créer votre segment. Nommez votre segment en décrivant le type d’utilisateur que vous souhaitez cibler. Cela vous aidera à identifier le segment lorsque vous voudrez le cibler pour vos campagnes ou Canevas. Les titres vagues des segments peuvent prêter à confusion.

Si vous le souhaitez, vous pouvez effectuer les opérations suivantes :
- Ajoutez une description au segment pour fournir plus de détails sur l'intention de cette audience et laissez des notes auxquelles les autres membres de l'équipe pourront se référer.
- Ajoutez une [équipe]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) à votre segmentation.
- Ajoutez des [étiquettes]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) à votre segmentation pour mieux l'organiser.

![Créez une fenêtre modale/boîte de dialogue où le segment est nommé "Utilisateurs déchus" et la description du segment est la suivante : "Il s'agit de notre principal segment d'utilisateurs déchus pour cibler les non-actifs au cours des quatorze derniers jours", avec deux boutons, etc : Annuler et créer un segment.]({% image_buster /assets/img_archive/segment_app_selection.png %}){: style="max-width:80%;"}

## Étape 3 : Choisissez votre application ou plateforme

Choisissez les applications ou plateformes que vous souhaitez cibler en sélectionnant **Utilisateurs de toutes les applications** (par défaut) ou **Utilisateurs d'applications spécifiques.** Si vous choisissez **Utilisateurs de toutes les apps**, le segment inclut tous les utilisateurs, quelles que soient les données de session ou d'app. Si vous choisissez **Utilisateurs d'apps spécifiques**, vous pouvez ensuite sélectionner les apps ou plateformes que vous souhaitez inclure dans votre segmentation.

Par exemple, si vous souhaitez envoyer un message in-app uniquement aux appareils iOS, sélectionnez votre application iOS. Cela permettra aux utilisateurs qui peuvent utiliser à la fois un appareil iOS et Android de recevoir uniquement le message sur leur appareil iOS. Dans la liste des apps spécifiques, l'option **Utilisateurs ne provenant d'aucune app** vous permet d'inclure des utilisateurs sans sessions ni données d'apps (généralement créés via l'importation d'utilisateurs ou l'API REST).

![Panneau Détails du segment avec l'option "Utilisateurs de toutes les applications" sélectionnée dans la section Applications utilisées.]({% image_buster /assets/img_archive/Segment2.png %}){: style="max-width:80%;"}

## Étape 4 : Ajoutez des filtres à votre segment

Ajoutez au moins un filtre à votre segmentation. Vous pouvez combiner autant de filtres que vous le souhaitez pour rendre votre segmentation plus spécifique.

{% alert note %}
Braze ne crée pas de profils pour les utilisateurs tant qu’ils n’ont pas utilisé l’application une première fois, ce qui signifie que vous ne pouvez pas cibler des utilisateurs qui n’ont pas encore ouvert votre application.
{% endalert %}

#### Groupes de filtres

Les filtres sont organisés en groupes de filtres. Chaque filtre doit faire partie d'un groupe de filtres comprenant au minimum un filtre. Un segment peut avoir plusieurs groupes de filtres. Pour en ajouter un, sélectionnez **Ajouter un groupe de filtres**. Modifiez le nom du groupe de filtres en sélectionnant l'icône qui apparaît lorsque vous passez la souris à côté.

![Groupe interne avec une icône de modification à côté de son nom.]({% image_buster /assets/img_archive/edit_filter_group_name.png %})

Sélectionnez les icônes situées à côté de chaque filtre pour réduire l'éditeur de filtres ou dupliquer des filtres individuels. Après avoir dupliqué un filtre, vous pouvez ajuster ses valeurs dans chaque liste déroulante.

#### Logique de segmentation utilisant AND et OR

Au sein d'un groupe de filtres, les filtres peuvent être reliés par « AND » ou « OR ». Entre les groupes de filtres, les groupes peuvent être reliés par « AND » ou « OR ». Lorsque vous utilisez des groupes de filtres, vous pouvez créer une logique de segmentation, par exemple :
- (A ET B ET C) OU (C ET E ET F)
- (A OU B OU C) ET (C OU D OU F)

Si vous sélectionnez "OU" pour vos filtres, votre segmentation contiendra des utilisateurs répondant à n'importe quelle combinaison d'un, de plusieurs ou de tous ces filtres. Si vous sélectionnez "ET", les utilisateurs qui ne passent pas ce filtre ne seront pas inclus dans votre segmentation.

{% alert tip %}
Lorsque vous sélectionnez "OU" pour les filtres qui incluent un filtre négatif (tel que "n'est pas" dans un groupe d'abonnement), n'oubliez pas que les utilisateurs ne doivent remplir qu'un seul des filtres "OU" pour être inclus dans la segmentation. Pour appliquer le filtre négatif indépendamment des autres filtres, utilisez un [groupe d'exclusion](#exclusion).
{% endalert %}

#### Opérateurs de filtrage

Selon le filtre spécifique que vous sélectionnez, vous disposerez de différents opérateurs pour identifier les valeurs du filtre. Pour en savoir plus sur les opérateurs disponibles pour les différents types d'attributs personnalisés, reportez-vous à la section [Stockage des attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#setting-custom-attributes). Notez que lorsque vous utilisez l'opérateur « is any of », le nombre maximum d'éléments que vous pouvez inclure dans ce champ est de 256.

{% alert note %}
Braze ne crée pas de profils pour les utilisateurs tant qu’ils n’ont pas utilisé l’application une première fois, ce qui signifie que vous ne pouvez pas cibler des utilisateurs qui n’ont pas encore ouvert votre application.
{% endalert %}

![Filtre de segmentation des groupes avec l'opérateur AND.]({% image_buster /assets/img_archive/segmenter_filter_groups.png %})

{% alert important %}
Les segments utilisant déjà le filtre d'**appartenance à un segment** ne peuvent pas être inclus ou imbriqués dans d'autres segments. Cela permet d'éviter un cycle dans lequel le segment A inclut le segment B, qui essaie ensuite d'inclure à nouveau le segment A. Dans ce cas, la segmentation ne cesserait de se référer à elle-même, ce qui rendrait impossible le calcul de la personne qui en fait partie.

En outre, l'imbrication de segments de ce type ajoute de la complexité et peut ralentir les choses. Au lieu de cela, recréez le segment que vous essayez d'inclure en utilisant les mêmes filtres.
{% endalert %}

#### Groupes d'exclusion (facultatif) {#exclusion}

Lorsque vous créez un segment, vous pouvez appliquer un ou plusieurs groupes d'exclusion. Les groupes d'exclusion contiennent des critères qui identifient les utilisateurs à exclure de votre segmentation, et seront toujours reliés à vos groupes de filtres avec un opérateur "ET NON".

Les groupes d'exclusion ont la priorité sur les critères de segmentation. Si un utilisateur entre dans les critères de votre groupe d'exclusion, il ne fera pas partie de votre segmentation, même s'il répond aux critères de vos groupes de filtrage.

Créez un groupe d'exclusion en ajoutant des filtres comme vous le feriez pour les groupes de filtres. La statistique _Utilisateurs joignables estimés_ dans un groupe d'exclusion indique le nombre estimé d'utilisateurs restant dans votre segmentation après l'application des critères d'exclusion.

Les utilisateurs exclus ne seront pas comptabilisés dans les statistiques du _nombre total d'utilisateurs joignables_ de votre segmentation.

![Un groupe interne avec deux filtres.]({% image_buster /assets/img_archive/segmenter_exclusion_groups.png %})

#### Tester des segments

Après avoir ajouté des applications et des filtres à votre segment, vous pouvez tester si votre segment est configuré comme prévu en recherchant un utilisateur pour confirmer s'il correspond aux critères de segmentation. Pour ce faire, recherchez le `external_id` ou le `braze_id` d'un utilisateur dans la section **Recherche d'utilisateurs**.

![Section de recherche d'utilisateurs avec un champ de recherche.]({% image_buster /assets/img_archive/user_lookup.png %})

La recherche d’utilisateur est disponible lors de :
- La création d’un segment
- La configuration d’une campagne ou d’une audience Canvas
- La configuration d’une étape de Parcours d'audience

Lorsqu'un utilisateur correspond aux critères de segment, de filtre et d'application, une alerte l'indique.

![La consultation de l'utilisateur "testuser" déclenche une alerte indiquant que "testuser correspond à tous les segments, filtres et applications".]({% image_buster /assets/img_archive/user_lookup_match.png %})

Lorsqu'un utilisateur ne correspond pas à tout ou partie des critères de segmentation, de filtrage ou d'application, les critères manquants sont répertoriés à des fins de résolution des problèmes.

![Une recherche utilisateur avec une alerte indiquant "test1 ne correspond pas aux critères de ciblage suivants :" et affichant les critères manquants.]({% image_buster /assets/img_archive/user_lookup_nomatch.png %})

#### Segments mono-utilisateur

Vous pouvez créer des segments comportant un seul utilisateur (ou une poignée d’utilisateurs) en utilisant des attributs uniques qui identifient les utilisateurs, comme un nom d’utilisateur ou un ID utilisateur.

Cependant, il se peut que cet utilisateur individuel ne soit pas reflété dans les statistiques ou l’aperçu de segmentation, car les statistiques des segments sont calculées sur la base d’un échantillon aléatoire avec un degré de confiance de 95 % que le résultat est compris entre +/- 1 %. Plus votre base d’utilisateurs est grande, plus il est probable que la taille de votre segment soit une estimation approximative. Pour vous assurer que votre segmentation contient bien l'utilisateur unique que vous ciblez, sélectionnez **Calculer les statistiques exactes.** Cela permettra de calculer le nombre exact d'utilisateurs dans votre segmentation avec une précision supérieure à 99,999 %.

Braze propose des filtres de test pour cibler des utilisateurs spécifiques en fonction de leur ID utilisateur ou de leur adresse e-mail.

## Étape 5 : Enregistrez votre segment

Sélectionnez **Enregistrer**. Vous êtes maintenant prêt à envoyer des messages à vos utilisateurs !

## Mesurer la taille des segments

Pour en savoir plus sur le suivi de la composition et de la taille de votre segmentation, reportez-vous à la section [Mesurer la taille d'un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/).

## Archivage des segments

Si vous n'avez plus besoin d'un segment spécifique ou si vous souhaitez le retirer, vous pouvez l'archiver en accédant à la page **Segments** et en sélectionnant **Archiver** dans le menu de la ligne de ce segment.

{% alert warning %}
Lorsque vous archivez un segment, toutes les campagnes et tous les Canvas qui l’utilisent seront également archivés (même si le segment est uniquement utilisé dans un seul composant Canvas). Ceci comprend également les segments imbriqués dans lesquels seront archivés à la fois les segments et toutes les campagnes et Canvas qui les utilisent.
<br><br>
Vous recevrez un avertissement indiquant quels Canvas ou campagnes sont sur le point d’être archivés avec le segment associé.
{% endalert %}

Vous pouvez désarchiver le segment en naviguant jusqu'à lui dans la page **Segments**, puis en sélectionnant **Désarchiver.**

## Ciblage des comportements lorsque les utilisateurs disposent de plusieurs appareils.

Les utilisateurs disposent de plusieurs appareils s'ils se connectent au même compte sur plusieurs appareils. Vous pouvez vérifier la présence de plusieurs appareils dans la section **Appareils récents** d'un [profil utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/).

Lorsque vous effectuez une segmentation avec des filtres dépendant de l'appareil (modèle d'appareil, système d'exploitation de l'appareil et version de l'application), votre segment contiendra tous les utilisateurs qui correspondent à vos critères de segmentation. Ces utilisateurs recevront un message sur tous leurs appareils, y compris ceux qui ne répondent pas à vos critères de filtrage. Par exemple, supposons que l'utilisateur A possède deux appareils : L'appareil 1 est équipé du système d'exploitation 13.0 et l'appareil 2 du système d'exploitation 10.0. Si un segment cible les utilisateurs dotés du système d'exploitation 10.0, cet utilisateur fera partie de ce segment et recevra des messages sur ses deux appareils.

### Notifications push

Vous pouvez spécifier qu'une seule notification push est envoyée à chaque utilisateur. Lorsque vous [rédigez votre message]({{ssite.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message#step-4-compose-your-push-message), sélectionnez l'option **N'envoyer qu'au dernier appareil utilisé par l'utilisateur** sous **Paramètres supplémentaires.**

!["Paramètres supplémentaires" avec une case à cocher permettant de n'envoyer les données qu'au dernier appareil utilisé par l'utilisateur.]({% image_buster /assets/img_archive/send_to_last_device.png %}){: style="max-width:60%;"}

### Considérations

- **Les messages envoyés peuvent dépasser la taille de l'audience.** Lorsque certains utilisateurs possèdent plusieurs appareils, chaque appareil peut recevoir un message. Le nombre d'envois de messages est donc supérieur à celui des utilisateurs de votre segmentation.
- **L'appartenance d'un utilisateur à un segment peut être différente de ce à quoi vous vous attendez.**
    - Un utilisateur peut être ciblé sur son appareil actuel en fonction des attributs associés à un autre appareil. Si vous ne vous attendiez pas à ce qu'un utilisateur reçoive un message, vérifiez si son profil utilisateur comporte plusieurs appareils.
    - Un utilisateur peut avoir fait partie de votre segmentation cible au moment de l'envoi, mais en raison de comportements associés à l'un ou l'autre de ses appareils, il peut ne plus faire partie de ce segment par la suite. Un utilisateur peut ainsi recevoir une campagne ou un canvas alors qu'il ne correspond pas aux critères de filtre. <br><br>Par exemple, un utilisateur pourrait recevoir un message ciblant les utilisateurs dont la version la plus récente de l'application est OS 10.0, même s'ils utilisent actuellement OS 13.0. Dans ce cas, l'utilisateur disposait du système d'exploitation 10.0 au moment de l'envoi du message et a ensuite effectué une mise à niveau vers le système d'exploitation 13.0.<br><br> De même, si un utilisateur utilise ultérieurement un appareil avec une version d'application différente, son profil utilisateur sera mis à jour avec une nouvelle version d'application la plus récente. Ceci peut donner l'impression que l'utilisateur n'aurait pas dû être éligible pour recevoir le message, même s'il l’était au moment de l'envoi.


