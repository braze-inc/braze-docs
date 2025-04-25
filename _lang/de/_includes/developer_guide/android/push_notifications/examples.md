{% multi_lang_include developer_guide/prerequisites/android.md %} Sie müssen auch [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Angepasstes Benachrichtigungslayout

Braze-Benachrichtigungen werden als [Daten-Nachrichten](https://firebase.google.com/docs/cloud-messaging/concept-options) versendet. Das bedeutet, dass Ihre Anwendung immer die Möglichkeit hat, zu reagieren und ein entsprechendes Verhalten an den Tag zu legen, auch im Hintergrund (im Gegensatz zu Benachrichtigungen, die vom System automatisch verarbeitet werden können, wenn Ihre App im Hintergrund läuft). So hat Ihre Anwendung die Möglichkeit, das Erlebnis anzupassen, indem sie beispielsweise personalisierte UI-Elemente in der Benachrichtigung anzeigt, die dem Benachrichtigungsfach zugestellt wird. Auch wenn diese Art der Implementierung von Push für einige ungewohnt sein mag, ist eines unserer bekannten Features bei Braze, die [Push-Storys]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), ein Paradebeispiel für die Verwendung angepasster Ansichtskomponenten, um ein engagiertes Erlebnis zu schaffen!

{% alert important %}
Android schränkt ein, welche Komponenten für die Implementierung angepasster Benachrichtigungsansichten verwendet werden können. Layouts für Benachrichtigungsansichten dürfen _nur_ Ansichtsobjekte enthalten, die mit dem [RemoteViews-Framework](https://developer.android.com/reference/android/widget/RemoteViews) kompatibel sind.
{% endalert %}

## Personalisierte Push-Benachrichtigungen

Push-Benachrichtigungen können benutzerspezifische Informationen innerhalb einer angepassten Ansichtshierarchie anzeigen. Im folgenden Beispiel wird ein API-Trigger verwendet, um eine personalisierte Push-Benachrichtigung an einen Nutzer:in zu senden, damit dieser seinen aktuellen Fortschritt nach Abschluss einer bestimmten Aufgabe in der App verfolgen kann.

![Personalisiertes Push Dashboard Beispiel]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

Um einen personalisierten Push im Dashboard einzurichten, registrieren Sie die spezifische Kategorie, die angezeigt werden soll, und legen dann alle relevanten Nutzer:innen-Attribute fest, die Sie mit Liquid anzeigen möchten.

![Personalisiertes Push Dashboard Beispiel]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}
