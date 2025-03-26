---
nav_title: Android TV Push
article_title: Android TV Push
platform: Android
page_order: 8
description: "Dieser Artikel beschreibt, wie Sie Android TV Push implementieren und testen können."
channel:
  - push

---

# Android TV Push
![]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

> Obwohl es sich nicht um ein natives Feature handelt, wird die Push-Integration von Android TV ermöglicht, indem das Braze Android SDK und Firebase Cloud Messaging genutzt werden, um ein Push-Token für Android TV zu registrieren. Es ist jedoch notwendig, eine UI zu erstellen, um die Nutzdaten der Benachrichtigung nach deren Empfang anzuzeigen.

## Implementierung

1. **Braze Android SDK integrieren**<br>
Zunächst müssen Sie das [Braze Android SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/?redirected=true) integrieren (falls noch nicht geschehen).<br><br>
2. **Push-Benachrichtigungen integrieren**<br>
Als nächstes müssen Sie [Android Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/) integrieren (falls noch nicht geschehen).<br><br>
3. **Angepasste Toast-Ansicht erstellen**<br>
Als nächstes erstellen Sie eine benutzerdefinierte Ansicht in Ihrer App, um Ihre Benachrichtigungen anzuzeigen.<br><br>
4. **Angepasste Benachrichtigungs-Factory erstellen**<br>
Schließlich müssen Sie noch eine [angepasste Benachrichtigungs-Factory]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#custom-displaying-notifications) erstellen. Damit wird das Standardverhalten des SDK außer Kraft gesetzt und Sie können die Benachrichtigungen manuell anzeigen lassen. Die Rückgabe von `null` verhindert die Verarbeitung durch das SDK und erfordert angepassten Code, um die Benachrichtigung anzuzeigen. Nachdem diese Schritte abgeschlossen sind, können Sie mit dem Senden von Push-Nachrichten an Android TV beginnen!<br><br>
5. **Click Analytics-Tracking einrichten (optional)**<br>
Für ein effektives Click Analytics-Tracking müssen Sie manuell vorgehen, da Braze die Anzeige der Nachrichten nicht automatisch verarbeitet. Dies können Sie erreichen, indem Sie einen [Push-Callback]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback) erstellen, der auf die geöffneten und empfangenen Push-Intents von Braze wartet.

{% alert note %}
Beachten Sie, dass diese Benachrichtigungen **nicht bestehen bleiben** und für den Benutzer nur sichtbar sind, wenn das Gerät sie anzeigt. Das liegt daran, dass die Benachrichtigungszentrale von Android TV keine historischen Benachrichtigungen unterstützt.
{% endalert %} 

## Wie Sie Push auf Android TV testen

Um zu testen, ob Ihre Push-Implementierung erfolgreich ist, senden Sie eine Benachrichtigung vom Braze-Dashboard aus, wie Sie es normalerweise bei einem Android-Gerät tun würden.

- **Bei geschlossener Anwendung**: Die Push-Nachricht zeigt eine Toast-Benachrichtigung auf dem Bildschirm an.
- **Bei geöffneter Anwendung**: Sie haben die Möglichkeit, die Nachricht in Ihrer eigenen gehosteten Benutzeroberfläche anzuzeigen. Wir empfehlen, den UI-Stil der In-App-Nachrichten unseres Android Mobile SDK zu übernehmen.

## Zusätzliche Informationen
Für einen Marketing-Endbenutzer in Braze ist der Start einer Kampagne für Android TV identisch mit dem Start eines Push für mobile Android-Apps. Um ausschließlich diese Geräte anzusprechen, empfehlen wir, bei der Segmentierung die Android TV App auszuwählen. 

Die zugestellte und angeklickte Antwort, die von FCM zurückgegeben wird, folgt der gleichen Konvention wie bei einem Android-Mobilgerät; daher werden alle Fehler im Nachrichten-Aktivitätsprotokoll angezeigt.

