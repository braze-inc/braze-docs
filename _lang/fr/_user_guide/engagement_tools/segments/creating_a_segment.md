---
nav_title: Créer un segment
article_title: Créer un segment
page_order: 1
page_type: tutorial
description: "Cet article pratique vous explique comment configurer et créer un segment avec Braze."
tool: Segments
search_rank: 3
---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}La création d’un segment

> La segmentation vous permet de cibler les utilisateurs en fonction de leurs actions et de leurs caractéristiques démographiques, comportementales, ou techniques. La segmentation et l’envoi de messages automatiques peuvent être utilisés de manière intelligente et créative pour transformer vos prospects en clients à long terme de manière harmonieuse. Les segments sont mis à jour en temps réel en fonction des modifications de données, et vous pouvez créer autant de segments que nécessaire pour remplir vos objectifs de ciblage et de communication.

## Étape 1 : Accédez à la section Segments

![Section Engagement avec l’onglet Segments mis en surbrillance.][1]{: style="float:right;max-width:20%;"}

Accédez à la page **Segments** située dans **Engagements**.

## Étape 2 : Nommez votre segment

Cliquez sur <i class="fas fa-plus"></i> **Create Segment (Créer un segment)** pour concevoir votre segment. Nommez votre segment en décrivant le type d’utilisateur que vous souhaitez cibler. Cela garantira que ce segment pourra servir de cible pour plusieurs campagnes ou Canvas à venir. Les segments qui comportent des titres vagues peuvent prêter à confusion.

Vous pouvez aussi ajouter une description à votre segment pour fournir plus de détails sur l’intention de cette audience et laisser des notes pour les autres membres de votre équipe.

![Créez un modal de segment avec un segment nommé « Lapsed Users (Utilisateurs inactifs) » et pour lequel la description du segment est « This is our main Lapsed User segment to target non-actives within the past fourteen days (Il s’agit de notre principal segment d’utilisateurs inactifs pour cibler les utilisateurs non-actifs au cours des quatorze derniers jours) ». avec deux boutons : Cancel (Annuler) et Create Segment (Créer un segment).][2]{: style="max-width:70%;"}

## Étape 3 : Choisissez votre application ou plateforme

Choisissez les apps ou plateformes que vous voulez cibler en sélectionnant **Users from all apps (Utilisateurs de toutes les apps)** (option par défaut), ou **Users from specific apps (Utilisateurs d’apps spécifiques)**. Si vous choisissez **Utilisateurs de toutes les apps**, le segment inclura tous les utilisateurs, quelles que soient les sessions ou données d’application. Si vous choisissez **Users from specific apps (Utilisateurs d’apps spécifiques)**, vous pourrez sélectionner les applications ou plateformes à inclure dans votre segment. 

Par exemple, si vous souhaitez envoyer un message in-app uniquement aux appareils iOS, sélectionnez votre application iOS. Cela permettra aux utilisateurs qui peuvent utiliser à la fois un appareil iOS et Android de recevoir uniquement le message sur leur appareil iOS. Dans la liste des apps spécifiques, l’option **Users from no apps (Utilisateurs n’ayant pas d’apps)** vous permet d’inclure les utilisateurs sans sessions et sans données d’application (typiquement créés via une User Import ou l’API REST).

![Panneau Segment Details (Détails du segment) avec la case « Include users from all apps (Inclure les utilisateurs de toutes les applications) » non cochée dans la section Apps Used (Applications utilisées).][5]

## Étape 4 : Ajoutez des filtres à votre segment

Ajoutez au moins un filtre à votre segment comme illustré dans l’image ci-dessous. Vous pouvez combiner autant de filtres que vous le souhaitez pour que votre segmentation soit plus spécifique.

{% alert note %}
Braze ne crée pas de profils pour les utilisateurs tant qu’ils n’ont pas utilisé l’application une première fois, ce qui signifie que vous ne pouvez pas cibler des utilisateurs qui n’ont pas encore ouvert votre application.
{% endalert %}

![Filtres du segment avec la condition « OR (OU) » sélectionnée.][3]

Si vous choisissez « OR (OU) » pour vos filtres, votre segment contiendra des utilisateurs qui remplissent un filtre, certains filtres ou tous ces filtres, tandis que la condition « AND (ET) » signifie que les utilisateurs qui ne remplissent pas ce filtre ne seront pas inclus dans votre segment. Cette logique peut être combinée afin de segmenter les utilisateurs qui remplissent un filtre « ET » un ou deux autres filtres.

Notez que les statistiques de votre segment s’actualisent en temps réel lorsque vous ajoutez ou enlevez des filtres. Gardez à l’esprit que ces statistiques sont des estimations (+/- 1 %) et que la base utilisateur exacte du segment est toujours calculée avant qu’un segment ne reçoive un message envoyé dans le cadre d’une campagne ou d’un Canvas. Notez qu’une erreur s’affichera si le segment que vous indiquez dans l’un de vos segments imbriqués est déjà archivé.

{% alert important %}
Les segments qui utilisent déjà le filtre Segment Membership (Appartenance à un segment) ne peuvent pas être inclus ou imbriqués dans d’autres segments.
{% endalert %}

### Tester des segments

Après avoir ajouté des applications et des filtres à votre segment, vous pouvez tester si votre segment est configuré comme prévu en [recherchant un utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/user_lookup/) pour confirmer s’il correspond aux critères du segment.

![]({% image_buster /assets/img_archive/user_lookup.png %})

### Segments mono-utilisateur

Vous pouvez créer des segments comportant un seul utilisateur (ou une poignée d’utilisateurs) en utilisant des attributs uniques qui identifient les utilisateurs, comme un nom d’utilisateur ou un ID utilisateur.

Cependant, il se peut que cet utilisateur individuel ne soit pas reflété dans les statistiques ou l’aperçu de segmentation, car les statistiques des segments sont calculées sur la base d’un échantillon aléatoire avec un degré de confiance de 95 % que le résultat est compris entre +/- 1 %. Plus votre base d’utilisateurs est grande, plus il est probable que la taille de votre segment soit une estimation approximative. Pour vous assurer que votre segment contient le seul utilisateur que vous souhaitez cibler, cliquez sur **Calculate Exact Statistics (Calculer les statistiques exactes)** sur la page **Informations relatives au segment**. Cela calculera le nombre exact d’utilisateurs dans votre segment, sans arrondi.

Braze propose des filtres de test pour cibler des utilisateurs spécifiques en fonction de leur ID utilisateur ou de leur adresse e-mail.

## Étape 5 : Enregistrez votre segment

Cliquez sur **Save (Enregistrer)** et vous serez prêt(e) à envoyer des messages à vos utilisateurs !

## Calcul d’appartenance à un segment {#segment-membership-calculation}

Braze met à jour l’appartenance des utilisateurs à un segment au fur et à mesure que nos serveurs reçoivent et traitent les données, ce qui se produit généralement de manière instantanée. L’appartenance d’un utilisateur à un segment donné ne changera pas tant que cette session n’a pas été traitée. Par exemple, un utilisateur faisant partie d’un segment d’utilisateurs inactifs au début d’une session sera immédiatement sorti du segment d’utilisateurs inactifs une fois la session traitée.

### Calcul du nombre total d’utilisateurs pouvant être atteints

Chaque segment affiche le nombre total d’utilisateurs qui sont membres de ce segment. Lorsque vous filtrez pour les **Utilisateurs de toutes les applications**, il affiche aussi tous les canaux disponibles pour communiquer avec ces utilisateurs, comme les notifications push Web ou l’e-mail. Il est possible que le nombre total d’utilisateurs diffère du nombre d’utilisateurs pouvant être atteints par chaque canal. Pourquoi donc ?

![Un tableau affichant un nombre total d’utilisateurs pouvant être atteints de 9 100, 8 899 pouvant être atteints par e-mail, 6 720 par notification push Web, 4 521 par notification push Android et 5 122 par notification push iOS.][4]

Pour qu’un utilisateur soit indiqué comme pouvant être atteint par un canal donné, il doit avoir à la fois :
*Une adresse e-mail/jeton de notification push valide associé avec son profil ; et
* Être abonné ou inscrit à votre application.

Un utilisateur donné peut appartenir à plusieurs groupes d’utilisateurs atteignables. Par exemple, un utilisateur peut disposer d’une adresse e-mail valide et d’un jeton de notification push Android valide et être abonné aux deux, mais ne pas avoir de jeton de notification push associé. La différence entre le nombre total d’utilisateurs pouvant être atteints et la somme des différents canaux est le nombre d’utilisateurs qualifiés pour le segment mais ne pouvant pas être atteints par ces canaux de communication.

## Archivage des segments

Si vous n’avez plus besoin d’un segment ou que vous souhaitez l’abandonner, vous pouvez l’archiver en allant sur la page **Segments**, en cliquant sur l’icône en forme d’engrenage, puis en sélectionnant « Archive (Archiver) » dans la liste déroulante qui apparaît.

{% alert warning %}
Lorsque vous archivez un segment, toutes les campagnes et tous les Canvas qui l’utilisent seront également archivés (même si le segment est uniquement utilisé dans un seul composant Canvas). Ceci comprend également les segments imbriqués dans lesquels seront archivés à la fois les segments et toutes les campagnes et Canvas qui les utilisent.

Vous recevrez un avertissement indiquant quels Canvas ou campagnes sont sur le point d’être archivés avec le segment associé.
{% endalert %}

Vous pouvez décompresser le segment en y accédant via la page Segments, puis en sélectionnant **Unarchive (Décompresser)**.

[1]: {% image_buster /assets/img_archive/Segment1.png %}
[2]: {% image_buster /assets/img_archive/Segment2.png %}
[3]: {% image_buster /assets/img_archive/segment_step4.png %}
[4]: {% image_buster /assets/img_archive/reachable_users.png %}
[5]: {% image_buster /assets/img_archive/segment_app_selection.png %}
