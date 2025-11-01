---
nav_title: Listes de suppression
article_title: Listes de suppression
page_order: 3
page_type: reference
tool: Segments
description: "Cette page explique comment utiliser les listes de suppression pour spécifier les utilisateurs qui ne doivent jamais recevoir vos messages."

---

# Listes de suppression

> Les listes de suppression sont des groupes d'utilisateurs qui ne reçoivent automatiquement aucune campagne ou Canvas. Les listes de suppression sont définies par des critères de segmentation, et les utilisateurs entrent et sortent des listes de suppression lorsqu'ils répondent aux critères de segmentation. Vous pouvez également définir des tags d'exception afin que la liste de suppression ne s'applique pas aux campagnes ou aux campagnes avec ces tags. Les messages provenant de campagnes ou de Canvases avec des étiquettes d'exception atteindront toujours les utilisateurs de la liste de suppression qui font partie des segments de ciblage.

## Pourquoi utiliser des listes de suppression ?

Les listes de suppression sont dynamiques et s'appliquent automatiquement à toutes les formes d'envoi de messages, mais vous pouvez définir des exceptions pour certaines étiquettes. Si les étiquettes d'exception que vous avez sélectionnées sont utilisées dans une campagne ou un canvas, cette liste de suppression ne s'appliquera pas à cette campagne ou à ce canvas. Les messages provenant de campagnes ou de Canvases avec des étiquettes d'exception atteindront toujours tous les utilisateurs de la liste de suppression qui font partie de vos segments de ciblage.

### Types de messages et canaux concernés par les listes de suppression

Les listes de suppression s'appliquent à tous les types de messages et à tous les canaux, à l'exception des [drapeaux de fonctionnalité]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/). Cela signifie que les listes de suppression s'appliquent par défaut à tous les canaux, campagnes et Canvases, y compris :
- [Campagnes API]({{site.baseurl}}/api/api_campaigns/)
- Campagnes déclenchées par l'API et Canvases
- [Les e-mails transactionnels]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/)

Le seul type de message auquel les listes de suppression ne s'appliquent pas est celui des drapeaux de fonctionnalité. Les utilisateurs figurant dans une liste de suppression ne seront pas exclus des drapeaux de fonctionnalité, mais seront exclus de tous les autres canaux. 

Vous pouvez utiliser des tags d'exception pour que les utilisateurs de la liste de suppression soient toujours ciblés par des campagnes et des canevas particuliers. Pour plus d'informations, reportez-vous à l'étape 4 de la section [Configuration des listes de suppression](#setup). Si vous n'ajoutez pas de tags d'exception à une liste de suppression, les utilisateurs de cette liste de suppression ne seront pas ciblés par des messages autres que les drapeaux de fonctionnalité. 

{% alert note %}
Les listes de suppression sont appliquées aux campagnes API créées dans le tableau de bord de Braze à l'aide d'une adresse `campaign_id`. Les listes de suppression ne s'appliquent pas aux messages envoyés par les [endpoints de messagerie de Braze]({{site.baseurl}}/api/endpoints/messaging/) sans `campaign_id`.
{% endalert %}

La section "Paramètres d'exception" avec une case à cocher pour ne pas appliquer la liste de suppression aux campagnes déclenchées par l'API et aux canevas.]({% image_buster /assets/img/suppression_list_checkbox.png %}){: style="max-width:70%;"}

## Mise en place de listes de suppression {#setup}

{% alert note %}
Tous les utilisateurs peuvent consulter les listes de suppression, mais seuls les utilisateurs disposant de [droits d'administrateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?tab=admin#list-of-permissions) peuvent créer et gérer des listes de suppression.
{% endalert %}

1. Allez dans **Audience** > **Listes de suppression**.<br><br>La page "Listes de suppression" contient une liste de trois listes de suppression.]({% image_buster /assets/img/suppression_lists_home.png %})<br><br>
2. Sélectionnez **Créer une liste de suppression** et ajoutez un nom.<br><br>Une fenêtre intitulée "Create a Suppression List" (Créer une liste de suppression) avec un champ pour saisir un nom.]({% image_buster /assets/img/create_suppression_list.png %}){: style="max-width:80%;"}<br><br>
3. Utilisez des filtres de segmentation pour identifier les utilisateurs de vos listes de suppression. Vous devez en sélectionner au moins un.

{% alert important %}
Bien que le processus de configuration semble similaire à la [création de segments]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), une liste de suppression est un groupe d'utilisateurs auxquels vous ne souhaitez **pas** envoyer de messages, quelle que soit leur appartenance à un segment.
{% endalert %}

Un générateur de liste de suppression avec un filtre pour les utilisateurs qui ont ouvert un e-mail il y a plus de 90 jours.]({% image_buster /assets/img/suppression_list_filters.png %})

{: start="4"}
4\. Déterminez si vous souhaitez des exceptions basées sur les étiquettes en cochant la case située sous le nom de votre segment (voir [Pourquoi utiliser les listes de suppression ?](#why-use-suppression-lists) pour plus d'informations), puis ajoutez les étiquettes des campagnes ou des toiles que les utilisateurs de cette liste de suppression doivent continuer à recevoir. <br><br>En d'autres termes, si vous ajoutez l'étiquette d'exception "Confirmation d'expédition", les utilisateurs de votre liste de suppression seront exclus de tous les messages, à l'exception de ceux qui utilisent l'étiquette "Confirmation d'expédition".<br><br>\![La section "Détails de la liste d'expédition" avec une étiquette d'exception appliquée appelée "Confirmation d'expédition".]({% image_buster /assets/img/exception_tags.png %})<br><br>
5\. Enregistrez ou activez votre liste de suppression.
- Lorsque vous enregistrez, votre liste de suppression est enregistrée mais n'est pas activée, ce qui signifie qu'elle n'entrera pas en vigueur. Votre liste de suppression restera inactive jusqu'à ce que vous l'activiez, et les listes de suppression inactives n'auront pas d'impact sur l'envoi des messages (les utilisateurs ne seront pas exclus des messages).
- Lorsque vous l'activez, votre liste de suppression sera enregistrée et entrera immédiatement en vigueur, ce qui signifie que les utilisateurs de votre liste de suppression seront immédiatement exclus des campagnes ou des Canvases (sauf ceux qui contiennent une étiquette d'exception).

{% alert note %}
Seuls les administrateurs peuvent enregistrer ou activer des listes de suppression. Dans la version bêta, vous pouvez avoir jusqu'à cinq listes de suppression actives à la fois.
{% endalert %}

Vous pouvez désactiver ou archiver les listes de suppression lorsque vous n'en avez plus besoin. 
- Pour désactiver, sélectionnez une liste de suppression active et sélectionnez **Désactiver**. Les listes de suppression désactivées peuvent être réactivées ultérieurement.
- Pour archiver, vous pouvez le faire à partir de la page **Listes de suppression**.

## Utilisation de la liste de suppression

Pour vérifier si votre liste de suppression a empêché un utilisateur de recevoir un message, utilisez la **Recherche d'utilisateur** dans l'étape **Audience ciblée** au sein de votre campagne ou Canvas. Vous pourrez ainsi voir de quelle liste de suppression ils font partie.

Fenêtre "User Lookup" montrant qu'un utilisateur figure dans une liste de suppression.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

{% alert tip %}
Vous pouvez également trouver les listes de suppression appliquées dans l'étape **Résumé**.
{% endalert %}

Lors de la création d'une campagne ou d'un canvas, utilisez la **recherche d'** utilisateurs dans l'étape de l' **audience** cible pour rechercher un utilisateur. S'il ne fait pas partie de l'audience cible, vous pouvez voir la liste de suppression dont il fait partie. 

Fenêtre "User Lookup" montrant qu'un utilisateur figure dans une liste de suppression.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

### Campagne 

Si un utilisateur figure dans une liste de suppression, il ne recevra pas de campagne pour laquelle cette liste de suppression s'applique. Reportez-vous à la section [Types de messages et canaux concernés par les listes de suppression](#message-types-and-channels-affected-by-suppression-lists) pour connaître les cas où une liste de suppression ne s'applique pas.

La section "Listes de suppression" comporte une liste de suppression active, appelée "Low marketing health scores".]({% image_buster /assets/img/active_suppression_list.png %})

### Canevas 

À partir du moment où un utilisateur est ajouté à une liste de suppression, il n'entrera pas dans Canvases. S'ils ont déjà saisi un Canvas, ils ne recevront pas les étapes du message. Cela signifie que si un utilisateur se trouve déjà dans un canvas lorsqu'il est ajouté à une liste de suppression, il avancera dans le canvas jusqu'à l'étape suivante du message, après quoi il quittera le canvas sans avoir reçu l'étape du message. 

Par exemple, supposons qu'un canvas comporte une étape de mise à jour de l'utilisateur suivie d'une étape d'envoi de messages. Si un utilisateur entre dans le Canvas et est ensuite ajouté à une liste de suppression, il passera quand même par l'étape de mise à jour de l'utilisateur (où il peut être mis à jour), puis sortira à l'étape du message, où il sera inclus dans les indicateurs quittés.
