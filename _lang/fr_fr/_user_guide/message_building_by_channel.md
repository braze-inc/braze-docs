---
nav_title: Créer des messages par canal
article_title: Créer des messages par canal
page_order: 5
layout: dev_guide

guide_top_header: "Créer des messages par canal"
guide_top_text: "Les canaux de communication sont des moyens de communiquer virtuellement avec vos clients par le biais de notifications push sur leur téléphone ou leur navigateur web, d'e-mails, de messages in-app, et bien plus encore ! Si vous souhaitez en savoir plus sur ces canaux et sur la manière de les utiliser avec Braze, consultez les sections suivantes. Ou consultez nos cours d'apprentissage Braze sur les <a href='https://learning.braze.com/series/messaging-channels' target='_blank'>canaux d'envoi de messages</a>!<br><br>Vous pouvez utiliser Braze pour créer des campagnes d'envoi de messages accessibles sur chaque canal. Travaillez avec vos ingénieurs pour vous assurer que vous respectez les normes d'accessibilité dans votre mise en œuvre."
description: "Cette page d'atterrissage couvre les canaux d'envoi des messages de Braze. Les canaux de communication sont des moyens de communiquer virtuellement avec vos clients par le biais de notifications push sur leur téléphone ou leur navigateur web, d'e-mails, de messages in-app, et bien plus encore !"

guide_featured_title: "Chaînes disponibles"
guide_featured_list:
- name: Bannières
  link: /docs/user_guide/message_building_by_channel/banners/
  image: /assets/img/braze_icons/table.svg
- name: Cartes de contenu
  link: /docs/user_guide/message_building_by_channel/content_cards/
  image: /assets/img/braze_icons/table.svg
- name: Envoi de messages par e-mail
  link: /docs/user_guide/message_building_by_channel/email/
  image: /assets/img/braze_icons/mail-01.svg
- name: "Message in-app"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/
  image: /assets/img/braze_icons/annotation-dots.svg
- name: Envoi de messages en mode push
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

Vous pouvez utiliser Braze pour créer des campagnes d'envoi de messages accessibles sur chaque canal. Travaillez avec vos ingénieurs pour vous assurer que vous respectez les normes d'accessibilité dans votre mise en œuvre. Si vous souhaitez obtenir des conseils supplémentaires, nous vous recommandons :

- [Fondements de l'envoi de messages accessibles](https://learning.braze.com/accessible-messaging-foundations): Apprenez les principes fondamentaux de l'accessibilité qui s'appliquent aux communications de marque dans ce cours d'apprentissage de Braze.
- [Créer des messages accessibles]({{site.baseurl}}/help/accessibility/): Apprenez à ajouter du texte alt et à structurer votre contenu pour les technologies d'assistance directement dans Braze.

{% multi_lang_include accessibility/feedback.md %}

## Choix d'un canal de communication

Lorsque vous déterminez le canal de communication qui convient le mieux à vos campagnes et à vos toiles, pensez toujours au contenu et à l'urgence de votre message :

- Le **contenu** est le degré d'engagement visuel de votre message. Vous pouvez ajouter des ressources multimédias et autres à votre texte pour enrichir votre contenu.
- L'**urgence** est une mesure de la rapidité avec laquelle un message est capable de notifier votre utilisateur et d'attirer son attention. Les notifications que l'utilisateur peut consulter immédiatement ont un degré d'urgence élevé, tandis que les messages qui nécessitent que l'utilisateur se connecte à votre appli ont un degré d'urgence faible.

La matrice suivante illustre les forces et les faiblesses des principaux canaux de communication en termes de contenu et d'urgence. Pensez toujours à l'urgence et à la richesse du contenu de votre message, puis choisissez le canal adéquat pour votre campagne.

Les push mobiles/web ont un contenu simple et un degré d'urgence élevé ; les e-mails ont un contenu riche et un degré d'urgence élevé ; les messages in-app/navigateurs ont un contenu simple et un degré d'urgence faible ; les cartes de contenu ont un contenu riche et un degré d'urgence faible.]({% image_buster /assets/img_archive/messaging_matrix.png %})

Pour en savoir plus sur la manière dont vous pouvez tirer parti de cette matrice, consultez notre cours d'apprentissage Braze sur la [compréhension de la matrice d'envoi de messages.](https://learning.braze.com/understand-the-messaging-matrix)

<br><br>
