---
nav_title: Erstellung von Nachrichten nach Kanal
article_title: Nachrichtenerstellung nach Kanal
page_order: 5
layout: dev_guide

guide_top_header: "Nachrichtenerstellung nach Kanal"
guide_top_text: "Messaging-Kanäle bieten Ihnen die Möglichkeit, virtuell mit Ihren Kund:innen zu kommunizieren: Push-Benachrichtigungen auf dem Telefon oder im Webbrowser, E-Mails, In-App-Nachrichten und vieles mehr! Wenn Sie mehr über diese Kanäle erfahren möchten und wie Sie sie mit Braze nutzen können, lesen Sie die folgenden Abschnitte. Oder sehen Sie sich unsere Braze-Lernkurse zu <a href='https://learning.braze.com/series/messaging-channels' target='_blank'>Messaging-Kanälen</a> an!<br><br>Mit Braze können Sie für jeden Kanal zugängliche Messaging-Kampagnen erstellen. Arbeiten Sie mit Ihren Ingenieuren zusammen, um sicherzustellen, dass Sie bei Ihrer Implementierung die Standards für Barrierefreiheit einhalten."
description: "Diese Landing Page deckt die Nachrichtenkanäle von Braze ab. Messaging-Kanäle bieten Ihnen die Möglichkeit, virtuell mit Ihren Kund:innen zu kommunizieren: Push-Benachrichtigungen auf dem Telefon oder im Webbrowser, E-Mails, In-App-Nachrichten und vieles mehr!"

guide_featured_title: "Verfügbare Kanäle"
guide_featured_list:
- name: Banner
  link: /docs/user_guide/message_building_by_channel/banners/
  image: /assets/img/braze_icons/table.svg
- name: Content-Cards
  link: /docs/user_guide/message_building_by_channel/content_cards/
  image: /assets/img/braze_icons/table.svg
- name: E-Mail Messaging
  link: /docs/user_guide/message_building_by_channel/email/
  image: /assets/img/braze_icons/mail-01.svg
- name: "In-App-Messaging"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/
  image: /assets/img/braze_icons/annotation-dots.svg
- name: Push Messaging
  link: /docs/user_guide/message_building_by_channel/push/
  image: /assets/img/braze_icons/marker-pin-01.svg
- name: "SMS, MMS und RCS"
  link: /docs/user_guide/message_building_by_channel/sms_mms_rcs/
  image: /assets/img/braze_icons/message-text-circle-01.svg
- name: Webhooks
  link: /docs/user_guide/message_building_by_channel/webhooks/
  image: /assets/img/braze_icons/brackets.svg
- name: WhatsApp
  link: /docs/user_guide/message_building_by_channel/whatsapp/
  image: /assets/img/braze_icons/whatsapp.svg
---

## Ressourcen zur Barrierefreiheit

Mit Braze können Sie für jeden Kanal zugängliche Messaging-Kampagnen erstellen. Arbeiten Sie mit Ihren Ingenieuren zusammen, um sicherzustellen, dass Sie bei Ihrer Implementierung die Standards für Barrierefreiheit einhalten. Wenn Sie zusätzliche Beratung wünschen, empfehlen wir Ihnen:

- [Grundlagen für barrierefreies Messaging](https://learning.braze.com/accessible-messaging-foundations): In diesem Braze-Lernkurs lernen Sie die grundlegenden Prinzipien der Barrierefreiheit kennen, die für die Markenkommunikation gelten.
- [Zugängliche Nachrichten erstellen]({{site.baseurl}}/help/accessibility/): Lernen Sie, wie Sie direkt in Braze Alt-Text hinzufügen und Ihre Inhalte für unterstützende Technologien strukturieren können.

{% multi_lang_include accessibility/feedback.md %}

## Auswahl eines Nachrichtenkanals

Wenn Sie entscheiden, welcher Nachrichtenkanal für Ihre Kampagnen und Canvases am besten geeignet ist, denken Sie immer an den Inhalt und die Dringlichkeit Ihrer Nachricht:

- **Inhalt** bedeutet, wie visuell ansprechend Ihre Botschaft ist. Sie können Ihren Texten Multimedia- und andere Elemente hinzufügen, um Ihren Inhalt zu bereichern.
- Die **Dringlichkeit** ist ein Maß dafür, wie schnell eine Nachricht Ihren Nutzer benachrichtigen und seine Aufmerksamkeit erregen kann. Benachrichtigungen, die der Benutzer sofort sehen kann, haben eine hohe Dringlichkeit, während Nachrichten, für die sich der Benutzer bei Ihrer App anmelden muss, eine geringe Dringlichkeit haben.

Die folgende Matrix veranschaulicht die Stärken und Schwächen der wichtigsten Messaging-Kanäle in Bezug auf Inhalt und Dringlichkeit. Überlegen Sie immer, wie dringend und inhaltsreich Ihre Nachricht sein sollte, und wählen Sie dann den richtigen Kanal für Ihre Kampagne.

![Mobile/Web-Push sind einfache Inhalte, hohe Dringlichkeit; E-Mails sind reichhaltige Inhalte, hohe Dringlichkeit; In-App/Browser-Nachrichten sind einfache Inhalte, niedrige Dringlichkeit; Content Cards sind niedrige Dringlichkeit, reichhaltige Inhalte]({% image_buster /assets/img_archive/messaging_matrix.png %})

Wenn Sie mehr darüber erfahren möchten, wie Sie diese Matrix nutzen können, sehen Sie sich unseren Braze Learning-Kurs zum Thema " [Understanding the Messaging Matrix"](https://learning.braze.com/understand-the-messaging-matrix) an.

<br><br>
