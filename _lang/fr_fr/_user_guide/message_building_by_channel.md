---
nav_title: Création de message par canal
article_title: Création de message par canal
page_order: 5
layout: dev_guide

guide_top_header: "Création de message par canal"
guide_top_text: "Les canaux de communication vous permettent de communiquer virtuellement avec vos clients via des notifications push sur leur téléphone ou navigateur Web, e-mail, messages in-app et bien plus ! Si vous souhaitez en savoir plus sur ces canaux et comment les utiliser avec Braze, consultez les sections suivantes présentées ci-dessous. Ou consultez nos cours d’apprentissage Braze sur les <a href='https://learning.braze.com/series/messaging-channels' target='_blank'>Canaux de communication</a> !<br><br>Vous pouvez utiliser Braze pour créer des campagnes de communication accessibles sur chaque canal. Vérifiez avec vos ingénieurs que vous répondez aux normes d’accessibilité lors de la mise en place."
description: "Cette page d’accueil couvre les canaux de communication Braze. Les canaux de communication vous permettent de communiquer virtuellement avec vos clients via des notifications push sur leur téléphone ou navigateur Web, e-mail, messages in-app et bien plus !"

guide_featured_title: "Canaux disponibles"
guide_featured_list:
- name: Bannières
  link: /docs/user_guide/message_building_by_channel/banners/
  image: /assets/img/braze_icons/table.svg
- name: Cartes de contenu
  link: /docs/user_guide/message_building_by_channel/content_cards/
  image: /assets/img/braze_icons/table.svg
- name: Messagerie par e-mail
  link: /docs/user_guide/message_building_by_channel/email/
  image: /assets/img/braze_icons/mail-01.svg
- name: "in-app Messaging"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/
  image: /assets/img/braze_icons/annotation-dots.svg
- name: Messagerie de notification push
  link: /docs/user_guide/message_building_by_channel/push/
  image: /assets/img/braze_icons/marker-pin-01.svg
- name: "SMS, MMS et RCS"
  link: /docs/user_guide/message_building_by_channel/sms_mms_rcs/
  image: /assets/img/braze_icons/message-text-circle-01.svg
- name: Webhooks
  link: /docs/user_guide/message_building_by_channel/webhooks/
  image: /assets/img/braze_icons/brackets.svg
- name: WhatsApp
  link: /docs/user_guide/message_building_by_channel/whatsapp/
  image: /assets/img/braze_icons/whatsapp.svg
---

## Ressources en matière d'accessibilité

Vous pouvez utiliser Braze pour créer des campagnes de communication accessibles sur chaque canal. Vérifiez avec vos ingénieurs que vous répondez aux normes d’accessibilité lors de la mise en place. Si vous souhaitez obtenir des conseils supplémentaires, nous vous recommandons :

- [Fondements de l'envoi de messages accessibles](https://learning.braze.com/accessible-messaging-foundations): Apprenez les principes fondamentaux de l'accessibilité qui s'appliquent aux communications de marque dans ce cours d'apprentissage de Braze.
- [Créer des messages accessibles]({{site.baseurl}}/help/accessibility/): Apprenez à ajouter du texte alt et à structurer votre contenu pour les technologies d'assistance directement dans Braze.

{% multi_lang_include accessibility/feedback.md %}

## Choisir un canal de communication

Lorsque vous déterminez quel est le canal de communication le mieux adapté à vos campagnes et Canvas, pensez toujours au contenu et à l’urgence de votre message :

- Le **contenu** désigne le degré d'attrait visuel de votre message. Vous pouvez ajouter du multimédia et d’autres supports à votre copie pour enrichir votre contenu.
- L'**urgence** est une mesure de la rapidité avec laquelle un message est capable de notifier votre utilisateur et d'attirer son attention. Les notifications directement visibles par l’utilisateur ont un caractère urgent ; à l’inverse, les messages nécessitant une connexion de l’utilisateur à votre application n’ont pas de caractère d’urgence.

La matrice suivante illustre les avantages et les inconvénients des canaux de communication en termes de contenu et d’urgence. Pensez toujours au degré d’urgence et à la richesse du contenu de votre message puis choisissez le canal approprié pour votre campagne.

![Les push mobiles/web ont un contenu simple, un degré d'urgence élevé ; les e-mails ont un contenu riche, un degré d'urgence élevé ; les messages in-app/navigateurs ont un contenu simple, un degré d'urgence faible ; les cartes de contenu ont un degré d'urgence faible, un contenu riche]({% image_buster /assets/img_archive/messaging_matrix.png %}).

Pour en savoir plus sur la manière dont vous pouvez tirer parti de cette matrice, consultez notre cours d'apprentissage Braze sur la [compréhension de la matrice d'envoi de messages.](https://learning.braze.com/understand-the-messaging-matrix)

<br><br>
