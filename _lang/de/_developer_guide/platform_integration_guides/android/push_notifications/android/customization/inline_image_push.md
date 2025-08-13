---
nav_title: Inline Image Push
article_title: Inline Image Push für Android
platform: Android
page_order: 5.9
description: "Dieser Referenzartikel beschreibt, wie Sie Inline-Image-Push in Ihre Android-Anwendung implementieren."
channel:
  - push

---

# Inline Image Push

![]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="float:right;max-width:30%;margin-left:15px;border: 0;"}

> Präsentieren Sie ein größeres Bild innerhalb Ihrer Android-Push-Benachrichtigung mit Inline Image Push. Bei diesem Design müssen Nutzer die Push-Benachrichtigung nicht mehr manuell erweitern, um das Bild zu vergrößern. 

Für die Nutzung dieser Funktion sind keine zusätzliche Integration oder SDK-Änderungen erforderlich. Bei Geräten oder SDKs, die die Mindestanforderungen an die Version nicht erfüllen, wird stattdessen eine standardmäßige Push-Benachrichtigung mit einem großen Bild angezeigt.

## Voraussetzungen

- Dieser Benachrichtigungstyp erfordert das Braze Android SDK v10.0.0+ und Geräte mit Android M+. 
- Nicht unterstützte Geräte oder SDKs greifen auf die standardmäßige große Bild-Push-Benachrichtigung zurück.
- Im Gegensatz zu normalen Android-Push-Benachrichtigungen haben die Inline-Image-Push-Bilder ein Seitenverhältnis von 3:2.

{% alert note %}
Geräte mit Android 12 werden aufgrund von Änderungen in den benutzerdefinierten Push-Benachrichtigungsstilen anders dargestellt.
{% endalert %}

## Dashboard einrichten

Wenn Sie eine Android-Push-Nachricht erstellen, ist diese Funktion in der Dropdown-Liste **Benachrichtigungstyp** verfügbar.

![Der Push-Kampagnen-Editor zeigt die Position des Dropdown-Menüs "Benachrichtigungstyp" (oberhalb der Standard-Push-Vorschau).]({% image_buster /assets/img/android/push/android_inline_image_notification_type.png %})
