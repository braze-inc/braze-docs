---
nav_title: Leitfaden für die erweiterte Implementierung (optional)
article_title: Erweiterte Implementierung von Push-Benachrichtigungen für Android (optional)
platform: Android
page_order: 29
description: "In diesem Leitfaden für fortgeschrittene Implementierungen erfahren Sie, wie Sie das Layout von Push-Benachrichtigungen anpassen können, um in Ihren Nachrichten Nutzer:innen-spezifische Informationen anzuzeigen. Außerdem enthalten sind ein von unserem Team erstellter Anwendungsfall, begleitende Code-Snippets und eine Anleitung zur Protokollierung von Analytics."
channel:
  - push
---

<br>
{% alert important %}
Suchen Sie nach dem Leitfaden für die Integration von Push-Benachrichtigungen für Entwickler? Sie finden es [hier]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/).
{% endalert %}

# Leitfaden für die erweiterte Implementierung

> Diese optionale und fortgeschrittene Implementierungsanleitung zeigt Ihnen, wie Sie eine angepasste FirebaseMessagingService-Unterklasse nutzen können, um Ihre Push-Nachrichten optimal zu nutzen. Darin enthalten sind ein von unserem Team angepasster Anwendungsfall, begleitende Code-Snippets und eine Anleitung zur Protokollierung von Analytics. Besuchen Sie unser Braze Demo Repository [hier](https://github.com/braze-inc/braze-growth-shares-android-demo-app)! Beachten Sie, dass sich dieser Implementierungsleitfaden auf eine Kotlin-Implementierung konzentriert. Für Interessierte werden jedoch Java-Snippets bereitgestellt.

## Angepasstes Benachrichtigungslayout

Braze-Benachrichtigungen werden als [Messaging-Nachrichten](https://firebase.google.com/docs/cloud-messaging/concept-options) versendet. Das bedeutet, dass Ihre Anwendung immer die Möglichkeit hat, zu reagieren und ein entsprechendes Verhalten an den Tag zu legen, auch im Hintergrund (im Gegensatz zu Benachrichtigungen, die automatisch vom System verarbeitet werden können, wenn Ihre App im Hintergrund läuft). So hat Ihre Anwendung die Möglichkeit, das Erlebnis anzupassen, indem sie beispielsweise personalisierte UI-Elemente in der Benachrichtigung anzeigt, die dem Benachrichtigungsfach zugestellt wird. Auch wenn diese Art der Implementierung von Push für einige ungewohnt sein mag, ist eines unserer bekannten Features bei Braze, die [Push-Storys]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), ein Paradebeispiel für die Verwendung angepasster Ansichtskomponenten, um ein engagiertes Erlebnis zu schaffen!

#### Anforderungen

Android schränkt ein, welche Komponenten für die Implementierung angepasster Benachrichtigungsansichten verwendet werden können. Layouts für Benachrichtigungsansichten dürfen _nur_ Ansichtsobjekte enthalten, die mit dem [RemoteViews-Framework](https://developer.android.com/reference/android/widget/RemoteViews) kompatibel sind.

### Personalisierte Push-Benachrichtigungen

Push-Benachrichtigungen können benutzerspezifische Informationen innerhalb einer angepassten Ansichtshierarchie anzeigen. Das folgende Beispiel zeigt eine Push-Benachrichtigung, nachdem ein Nutzer:innen eine bestimmte Aufgabe (Braze-Lernkurs) abgeschlossen hat und nun aufgefordert wird, diese Benachrichtigung zu erweitern, um seinen Fortschritt zu überprüfen. Die hier bereitgestellten Informationen sind benutzerspezifisch und können über einen API-Auslöser abgefeuert werden, wenn eine Sitzung abgeschlossen ist oder eine bestimmte Benutzeraktion durchgeführt wird. 

![Personalisiertes Push Dashboard Beispiel]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

#### Dashboard Konfiguration

Um einen personalisierten Push im Dashboard einzurichten, müssen Sie die spezifische Kategorie, die angezeigt werden soll, registrieren. Legen Sie die entsprechenden Nutzer:in-Attribute fest, die in der Nachricht in den Schlüssel-Wert-Paaren mit Hilfe von Standard Liquid angezeigt werden sollen. Diese Ansichten können auf der Grundlage bestimmter Benutzerattribute eines bestimmten Benutzerprofils personalisiert werden.

![Personalisiertes Push Dashboard Beispiel]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

##### Sind Sie bereit für die Protokollierung von Analysen?
Lesen Sie den [folgenden Abschnitt](#logging-analytics), um besser zu verstehen, wie der Datenfluss aussehen sollte.

## Protokollieren von Analytics

### Protokollierung mit der Braze API (empfohlen)

Das Protokollieren von Analytics kann nur in Echtzeit erfolgen, wenn der Server des Kunden auf unseren [Endpunkt `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) trifft. Senden Sie dazu den Wert `braze_id` in das Feld der Schlüssel-Wert-Paare (wie im folgenden Screenshot zu sehen), um das zu aktualisierende Nutzerprofil zu identifizieren.

![Personalisiertes Push Dashboard Beispiel]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:80%;"}

### Manuell protokollieren 

Sie können die Protokollierung manuell vornehmen, indem Sie die gewünschten Elemente entweder in Ihrer `FirebaseMessagingService.onMessageReceived`-Implementierung oder in Ihrer Startaktivität auf der Grundlage der in der Payload enthaltenen Extras protokollieren. Ein wichtiger Vorbehalt ist jedoch, dass Ihre `FirebaseMessagingService`-Unterklasse die Ausführung innerhalb von 10 Sekunden nach dem Aufruf beenden _muss_, um zu vermeiden, dass sie vom Android-System [markiert oder beendet](https://firebase.google.com/docs/cloud-messaging/android/receive) wird. 


