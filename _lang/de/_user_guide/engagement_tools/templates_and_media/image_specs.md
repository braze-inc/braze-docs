---
nav_title: Bild-Spezifikationen
article_title: Bild-Spezifikationen
page_order: 4.1

page_type: reference
description: "Dieser Referenzartikel beschreibt die empfohlenen Bildgrößen und Spezifikationen für jeden Kanaltyp."
tool:
  - Templates
  - Media

---

# Bild-Spezifikationen

> Im Allgemeinen werden kleinere und qualitativ hochwertige Bilder schneller geladen. Wir empfehlen daher, das kleinstmögliche Asset zu verwenden, um das gewünschte Ergebnis zu erzielen. Um Ihre Bilder in bestimmten Kanälen optimal zu nutzen, lesen Sie die Details in diesem Artikel.

Sie sollten Ihre Nachrichten immer in [einer Vorschau anzeigen und auf verschiedenen Geräten testen]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/), um sicherzustellen, dass die wichtigsten Bereiche Ihres Bildes und Ihrer Nachricht wie erwartet erscheinen.

{% alert tip %} Erstellen Sie Assets mit Vertrauen! Unsere Templates für In-App-Nachricht-Bilder und Overlays für die Sicherheitszone sind so gestaltet, dass sie mit Geräten aller Größen gut funktionieren. [Download Design Templates ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}). {% endalert %}

{% multi_lang_include image_specs.md variable_name='payload size' %}

## In-App-Nachrichten

{% multi_lang_include image_specs.md variable_name='in-app messages' %}

### Font Awesome

Braze unterstützt die Verwendung von [Font Awesome v4.3.0](https://fontawesome.com/v4.7.0/cheatsheet/) für modale In-App-Nachricht-Symbole.

## Push-Benachrichtigungen

{% multi_lang_include image_specs.md variable_name='push notifications' %}

## E-Mail

{% multi_lang_include image_specs.md variable_name='email' %}

## Image Verhalten

{% multi_lang_include image_specs.md variable_name='image behavior' %}
