---
nav_title: Créer un segment
article_title: Créer un segment
page_order: 1
page_type: tutoriel
description: "Cet article pratique vous guidera dans la façon de mettre en place et de créer un segment en utilisant Braze."
tool: Segments
---

# Création d'un segment

> Cet article vous guidera à travers les étapes de la création d'un segment, du filtrage de votre public cible, de la navigation et des archives.

Vos développeurs ont intégré le SDK, et les données de vos utilisateurs ont commencé à couler. Maintenant, quoi? Il est temps de commencer à segmenter vos utilisateurs. Suivez le guide ci-dessous ou consultez notre [cours de Segmentation LAB](https://lab.braze.com/segmentation-course)!

La segmentation vous permet de cibler les utilisateurs en fonction de leurs caractéristiques et actions démographiques, comportementales, sociales ou techniques. L'utilisation créative et intelligente de l'automatisation de la segmentation et de la messagerie vous permet de déplacer vos utilisateurs du premier contact vers un client à long terme. Les segments se mettent à jour en temps réel en fonction des changements de données, et vous pouvez créer autant de segments que nécessaire pour vos objectifs de ciblage et de messagerie.

## Étape 1 : Naviguer vers la section des segments

!\[Segments Menu\]\[1\]{: style="float:right;max-width:20%;"}

À partir du côté gauche du tableau de bord sous Engagement, cliquez sur **Segments**.

## Étape 2 : Nommez votre segment

Nommez votre segment en décrivant le type d'utilisateur pour lequel vous souhaitez filtrer. Cela permettra de s'assurer que ce segment peut être la cible de multiples campagnes ou Canvases à venir. Les titres de segment vagues peuvent causer une confusion sur la ligne.

Optionnellement, vous pouvez ajouter une description au segment pour fournir plus de détails sur l'intention de cet auditoire et laisser des notes à d'autres membres de l'équipe d'y faire référence.

!\[Create a Segment\]\[2\]{: style="max-width:70%;"}

## Étape 3 : Choisissez votre application ou votre plateforme

Choisissez quelles applications ou plates-formes vous souhaitez cibler en sélectionnant **Inclure les utilisateurs de toutes les applications** (par défaut), ou en décochant la case à cocher. Si vous désactivez cette option, vous pouvez ensuite sélectionner quelles applications ou plateformes vous souhaitez inclure dans votre segment. Par exemple, si vous souhaitez envoyer un message dans l'application uniquement aux appareils iOS, sélectionnez votre application iOS. Ceci assurera que les utilisateurs qui peuvent utiliser à la fois un appareil iOS et un appareil Android ne recevront le message que sur leur appareil iOS.

Pour plus d'informations sur cette option, reportez-vous à la section [Calcul de l'adhésion au segment](#segment-membership-calculation).

!\[Sélection d'App Segment\]\[5\]

## Étape 4 : Ajouter des filtres à votre segment

Ajoutez au moins un filtre à votre segment tel que décrit dans l'image ci-dessous. Vous pouvez combiner autant de filtres que vous le souhaitez afin de rendre votre segmentation plus spécifique.

{% alert note %}
Braze ne génère pas de profils pour les utilisateurs tant qu'ils n'ont pas utilisé l'application pour la première fois donc vous ne pouvez pas cibler les utilisateurs qui n'ont pas encore ouvert votre application.
{% endalert %}

!\[Filtres de segments\]\[3\]

Choisir "OU" pour vos filtres signifie que votre segment contiendra des utilisateurs satisfaisant n'importe quelle combinaison d'une, une, une, une, une, une, ou tous ces filtres, alors que « ET » signifie que les utilisateurs qui ne passent pas ce filtre ne seront pas inclus dans votre segment. Cette logique peut être combinée, de sorte que vous pouvez segmenter les utilisateurs qui passent un filtre "ET" l'un des deux autres filtres.

Notez que les statistiques de votre segment changent en temps réel au fur et à mesure que vous ajoutez et soustrayez des filtres. Gardez à l'esprit que ces statistiques sont des estimations (+/- 1%) et que l'adhésion exacte au segment est toujours calculée avant qu'un segment ne soit affecté par un message envoyé dans une campagne ou Canvas.

{% alert important %}
Les segments qui utilisent déjà le filtre d'abonnement de segment ne peuvent pas être inclus ou imbriqués dans d'autres segments.
{% endalert %}

### Segments pour un seul utilisateur

Vous pouvez créer des segments individuels (ou des segments d'une poignée d'utilisateurs) en utilisant des attributs uniques qui identifient les utilisateurs, comme un nom d'utilisateur ou un identifiant d'utilisateur.

Cependant, les statistiques de segmentation ou l'aperçu peuvent ne pas montrer cet utilisateur individuel, car les statistiques de segment sont calculées à partir d'un échantillon aléatoire avec un intervalle de confiance de 95% que le résultat est dans +/- 1%. Plus votre base d'utilisateurs est grande, plus il est probable que la taille de votre segment soit approximative. Pour vous assurer que votre segment contient le seul utilisateur que vous visez, cliquez sur **Calculer les statistiques exactes** sur la page **Détails du segment**. Cela calculera le nombre exact d'utilisateurs dans votre segment, sans arrondissement.

Braze a des filtres de test pour cibler des utilisateurs spécifiques par ID d'utilisateur ou par adresse e-mail.

## Étape 5 : Enregistrez votre segment

Une fois que vous avez cliqué sur "Enregistrer", vous êtes prêt à envoyer des messages à vos utilisateurs !

## Calcul de l'adhésion au segment {#segment-membership-calculation}

Braze met à jour le segment de membre de l'utilisateur lorsque les données sont renvoyées à nos serveurs et traitées, généralement instantanément. L’adhésion d’un utilisateur au segment ne changera pas avant que cette session ait été traitée. Par exemple, un utilisateur qui tombe dans un segment d'utilisateur expiré lorsque la session démarre pour la première fois sera immédiatement déplacé hors du segment utilisateur caducé lorsque la session sera traitée.

En outre, l'adhésion au segment est calculée différemment lorsque **Inclure les utilisateurs de toutes les applications** est sélectionnée, ou lorsqu'un groupe d'applications n'a qu'une seule application. Dans ces scénarios, l'adhésion au segment comprend tous les utilisateurs — tant ceux qui ont des sessions enregistrées, ainsi que les utilisateurs sans sessions et sans données d'application (généralement créées via l'importation de l'utilisateur ou REST API).

Si **Inclure des utilisateurs de toutes les applications** est effacé et que vous avez plus d'une application dans votre groupe d'applications, l'adhésion au segment inclura uniquement les utilisateurs ayant des sessions enregistrées dans les applications sélectionnées, et exclut les utilisateurs sans sessions ou données d'application. Par conséquent, le total des segments individuels avec une application sélectionnée ne sera pas égal à un segment avec **Inclure les utilisateurs de toutes les applications** sélectionnées.

## Segments d'archivage

Si vous n'avez plus besoin ou que vous souhaitez prendre la retraite d'un segment spécifique, vous pouvez l'archiver en allant à la page __Segments__ , cliquez sur l’équipement approprié, puis sélectionnez « Archiver » dans le menu déroulant qui apparaît.

{% alert warning %}
Lorsque vous archivez un segment, toutes les campagnes ou Canvases (même si le segment n'est utilisé que dans une seule étape de Canvas) en l'utilisant, __seront également archivées__. Vous obtiendrez une liste d'avertissement des Campagnes et Canvases sur le point d'être archivées en archivant le segment associé.
{% endalert %}

Vous pouvez désarchiver le segment en y naviguant dans Segments, puis en sélectionnant Désarchiver à partir du coin supérieur droit de sa page.
[1]: {% image_buster /assets/img_archive/Segment1.png %} [2]: {% image_buster /assets/img_archive/Segment2. ng %} [3]: {% image_buster /assets/img_archive/segment_step4.png %} [5]: {% image_buster /assets/img_archive/segment_app_selection.png %}
