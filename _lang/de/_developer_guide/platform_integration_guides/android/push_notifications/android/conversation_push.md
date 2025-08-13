---
nav_title: Conversation Push
article_title: Vonversation Push für Android
platform: Android
page_order: 5.92
description: "In dieser Anwendung erfahren Sie, wie Sie Android Conversation Push in Ihrer Android-Anwendung implementieren."
channel:
  - push

---

# Conversation Push

> In dieser Anwendung erfahren Sie, wie Sie Android Conversation Push in Ihrer Android-Anwendung implementieren.

![]({% image_buster /assets/img/android/push/conversations_android.png %}){: style="float:right;max-width:35%;margin-left:15px;border: 0;"}

Die [People and Conversation Initiative](https://developer.android.com/guide/topics/ui/conversations) ist eine mehrjährige Android-Initiative, die darauf abzielt, Menschen und Gespräche in den Systemoberflächen des Smartphones hervorzuheben. Diese Priorität beruht auf der Tatsache, dass die Kommunikation und Interaktion mit anderen Menschen für die Mehrheit der Android Nutzer:innen über alle Bevölkerungsschichten hinweg immer noch der am meisten geschätzte und wichtigste Funktionsbereich ist.

Für die Nutzung dieser Funktion sind keine zusätzliche Integration oder SDK-Änderungen erforderlich. Bei Geräten oder SDKs, die die Mindestanforderungen nicht erfüllen, wird stattdessen eine Standard-Push-Benachrichtigung angezeigt.

## Voraussetzungen

- Dieser Benachrichtigungstyp erfordert das Braze Android SDK v15.0.0+ und Android 11+ Geräte. 
- Bei nicht unterstützten Geräten oder SDKs wird auf eine standardmäßige Push-Benachrichtigung zurückgegriffen.

Dieses Feature ist nur über die Braze REST API verfügbar. Weitere Informationen finden Sie im [Android Push-Objekt]({{site.baseurl}}/api/objects_filters/messaging/android_object#android-conversation-push-object).

