---
nav_title: "Rich-Benachrichtigungen erstellen"
article_title: "Erstellen umfangreicher Push-Benachrichtigungen für Android"
page_order: 3
page_layout: tutorial
description: "In diesem Tutorial erfahren Sie, wie Sie Android Rich Notifications für Ihre Braze-Kampagnen einrichten."
platform: Android
channel:
  - Push
tool:
  - Campaigns
  
---

# Erstellen umfangreicher Push-Benachrichtigungen für Android

> Mit Rich Notifications können Sie Ihre Push-Benachrichtigungen noch individueller gestalten, indem Sie zusätzliche Inhalte hinzufügen, die über den reinen Text hinausgehen. Android-Benachrichtigungen enthalten schon seit einiger Zeit Bilder in Push-Benachrichtigungen, die als "erweitertes Benachrichtigungsbild" bezeichnet werden.

## Voraussetzungen

Bevor Sie eine Rich-Push-Benachrichtigung für Android erstellen, sollten Sie die folgenden Details beachten:

- Rich-Push-Benachrichtigungen für Android sind nicht verfügbar, wenn Sie eine Quick-Push-Kampagne erstellen.
- Android Extended Notification-Bilder müssen im Verhältnis 2:1 sein, haben aber keine Größenbeschränkung.
- Android erlaubt auch die Einstellung eines separaten Bildes für die Standard-Benachrichtigungsansicht. Dies sind die empfohlenen Bildgrößen: 
  - **Klein:** 512x256
  - **Medium:** 1024x512 
  - **Groß:** 2048x1024
- Derzeit sind für Rich-Benachrichtigungen unter Android nur statische Bilder zulässig, einschließlich der Bildformate JPEG und PNG. GIF und andere Bildformate werden noch nicht unterstützt.
- Das Hinzufügen von Aktionsschaltflächen zu Ihrer Push-Benachrichtigung kann sich auf den Bereich des Bildes auswirken, der angezeigt werden kann. Testen Sie mit der Vorschau des Dashboards und den aktiven Geräten, um sicherzustellen, dass die Ergebnisse den Erwartungen entsprechen.
- Das Braze Android SDK muss aktiviert sein, damit das Bild gerendert werden kann.

{% alert note %}
Braze bietet zwar Anleitungen zur Einrichtung von Rich-Push-Benachrichtigungen, aber die tatsächliche Darstellung von Rich-Push-Benachrichtigungen kann je nach äußeren Faktoren wie dem Seitenverhältnis des Geräts, der Android-Version, OEM-spezifischen Einschränkungen und anderen variieren. Wir empfehlen, einen Sendetest an mehrere Android-Geräte durchzuführen, um sicherzustellen, dass Ihre Rich-Push-Benachrichtigungen so erscheinen, wie Sie es wünschen.
{% endalert %}

## Einrichten Ihrer Android Rich Notification

### Schritt 1: Erstellen Sie eine Push-Kampagne

Folgen Sie den Schritten zum [Erstellen einer Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message), um eine Push-Benachrichtigung für Android zu verfassen. Sie werden denselben Composer für die Einrichtung von Push-Benachrichtigungen verwenden, die keine umfangreichen Inhalte enthalten.

### Schritt 2: Untertitel hinzufügen

Fügen Sie den **Zusammenfassungstext/Bildunterschrift** hinzu, den Sie vor dem Bild in der Benachrichtigung anzeigen möchten.

![Der Bereich Erweitertes Benachrichtigungsbild, wo Sie ein Bild hinzufügen oder eine Bild-URL eingeben können.]({% image_buster /assets/img_archive/android_rich_summarytext.png %})

### Schritt 3: Medien hinzufügen

Fügen Sie Ihr Bild in das Feld **Erweitertes Benachrichtigungsbild** im Composer der Nachricht ein. Bilder können direkt über das Dashboard hochgeladen werden oder indem Sie eine URL angeben, die anderswo gehostet wird.

Details zu den unterstützten Bildern finden Sie unter [Bildspezifikationen]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push).

![Ein Nutzer:innen erhält eine Push-Benachrichtigung für iOS mit dem Titel "Hallo" und dem Text "Danke, dass Sie an unserem Kundenbindungs-Programm teilnehmen!]({% image_buster /assets/img_archive/android_rich_image.png %})

### Schritt 4: Fahren Sie mit der Erstellung Ihrer Kampagne fort

Nachdem der Inhalt Ihrer Rich Notification in das Dashboard hochgeladen wurde, können Sie mit der [Planung Ihrer Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) fortfahren.

