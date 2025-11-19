---
nav_title: "Optionen für Benachrichtigungen"
article_title: iOS-Benachrichtigungsoptionen
page_order: 2
page_layout: reference
description: "Dieser Referenzartikel behandelt iOS-Benachrichtigungsoptionen wie kritische Alarme, stille Benachrichtigungen, vorläufige Push-Benachrichtigungen und mehr."

platform: iOS
channel:
  - push

---

# Optionen für Benachrichtigungen

> Mit der Veröffentlichung von Apples iOS 12 bietet Braze Unterstützung für mehrere seiner Funktionen, darunter [Benachrichtigungsgruppen](#notification-groups), [stille Benachrichtigungen/Provisorische Autorisierung](#provisional-push-authentication--quiet-notifications) und [kritische Alarme](#critical-alerts).

## Benachrichtigungsgruppen

Wenn Sie Ihre Nachrichten kategorisieren und im Benachrichtigungsfeld Ihres Benutzers gruppieren möchten, können Sie über Braze die Funktion Benachrichtigungsgruppen von iOS nutzen.

Erstellen Sie Ihre iOS Push-Kampagne, gehen Sie dann zum Tab **Einstellungen** und öffnen Sie die Dropdown-Liste **Benachrichtigungsgruppe**.

![Der Tab "Einstellungen" mit einem Dropdown-Menü "Benachrichtigungsgruppe", das den Wert "Gutscheine" ausgewählt hat.]({% image_buster /assets/img_archive/notification_group_dropdown.png %}){: style="max-width:50%;" }

Wählen Sie Ihre Benachrichtigungsgruppen aus der Dropdown-Liste. Wenn Ihre Einstellungen für die Benachrichtigungsgruppe nicht korrekt sind oder Sie **Keine** aus der Dropdown-Liste auswählen, wird die Nachricht automatisch wie gewohnt an alle definierten Benutzer im Arbeitsbereich gesendet.

Wenn hier keine Benachrichtigungsgruppen aufgeführt sind, können Sie eine mit Hilfe der iOS Thread ID hinzufügen. Sie benötigen eine iOS-Thread-ID für jede Benachrichtigungsgruppe, die Sie hinzufügen möchten. Fügen Sie sie dann zu Ihren Benachrichtigungsgruppen hinzu, indem Sie in der Dropdown-Liste auf **Benachrichtigungsgruppen verwalten** klicken und die erforderlichen Felder im Fenster **iOS Push-Benachrichtigungsgruppen verwalten** ausfüllen, das dann erscheint.

![Fenster zur Verwaltung von iOS Push-Benachrichtigungsgruppen.]({% image_buster /assets/img_archive/managenotgroups.png %}){: style="max-width:70%;" }

Erstellen Sie Ihre iOS-Push-Kampagne, und sehen Sie sich dann den oberen Teil des Editors an. Dort sehen Sie ein Dropdown-Menü mit der Bezeichnung **Benachrichtigungsgruppen**.

### Zusammenfassende Argumente

Zusätzlich zur Gruppierung von Benachrichtigungen nach Thread-IDs erlaubt Apple Ihnen, die Zusammenfassungen zu bearbeiten, die angezeigt werden, wenn Benachrichtigungen gruppiert werden. Braze-Benutzer können die Kategorie der Zusammenfassung, die Anzahl der Zusammenfassungen und das Argument der Zusammenfassung angeben, wenn sie eine Push-Kampagne mit unserem Tool erstellen.

{% alert tip %}
Beachten Sie, dass die Art und Weise, wie Benachrichtigungen mit der gleichen Thread-ID in der Benachrichtigungsleiste gruppiert werden, unter der Kontrolle des Betriebssystems steht. iOS kann wählen, ob Benachrichtigungen mit der gleichen Thread-ID separat oder in Gruppen angezeigt werden, je nachdem, was es für optimal hält.
{% endalert %}

Markieren Sie das Feld **Alarmoptionen** im **Push Composer**.

Wählen Sie dann `summary-arg` und `summary-arg-count` als Schlüssel und geben Sie diese Werte in die entsprechende Spalte ein. Wenn Sie keinen Wert für `summary-arg` eingeben, wird dieser standardmäßig auf 1 festgelegt.

### Zusammenfassungskategorien

Mit den Zusammenfassungskategorien können Sie die gesamte Zusammenfassung anpassen, die erscheint, wenn Benachrichtigungen gruppiert werden. Sie können mehrere Kategorien erstellen und anwenden.

Um eine Kategorie in Ihrer Nachricht zu verwenden, arbeiten Sie mit Ihren Entwicklern:innen zusammen, um das folgende Beispiel zu implementieren:

```
UNNotificationCategory *newsCategory = [UNNotificationCategory categoryWithIdentifier:@"news"
                                                      actions:@[likeAction, unlikeAction]
                                                      intentIdentifiers:@[]
                                                      hiddenPreviewsBodyPlaceholder:@""
                                                      categorySummaryFormat:@"%u more news articles from %@"
                                                       Options:0];
```

{% alert important %}
Ein SDK-Update ist dafür nicht erforderlich.
{% endalert %}

{% alert tip %}
Beachten Sie, dass `%u` und `%@` Formatierungs-Strings für die Zählung der Zusammenfassung bzw. das Argument der Zusammenfassung sind. Wenn die Zusammenfassung angezeigt wird, werden diese Platzhalter durch die Werte für `summary-count` und `summary-arg` ersetzt.
{% endalert %}

Sobald dies in Ihrer App eingerichtet ist, verwenden Sie die Übersichtskategorie, indem Sie das Feld **Benachrichtigungsschaltflächen** markieren und die Option **Vorregistrierte iOS-Kategorie eingeben** wählen.

Geben Sie dann die Zusammenfassungskategorie-ID ein, die Sie in Ihrer App festgelegt haben.

### Vorläufige Push-Authentifizierung und stille Benachrichtigungen {#provisional-push}

Apple bietet Marken die Möglichkeit, stille Push-Benachrichtigungen an die Notification Center ihrer Nutzer zu senden, bevor diese sich offiziell und explizit dafür entscheiden. So haben Sie die Chance, den Wert Ihrer Nachrichten frühzeitig zu demonstrieren. Alles, was Sie tun müssen, ist, [vorläufige Push-Benachrichtigungen](#set-up-provisional-push-notifications) in Ihrer App [einzurichten](#set-up-provisional-push-notifications). Dann erhält jeder Benutzer, der ein vorläufiges Push-Token hat, Ihre Nachrichten.

Im Gegensatz zu einem herkömmlichen iOS Push-Token fungiert ein provisorischer Push-Token als "Testpass", der es Marken erlaubt, neue Nutzer:innen zu erreichen, bevor sie Apples native Opt-in-Anfrage gesehen und angeklickt haben. Mit dieser Funktion wird Ihre Push-Benachrichtigung direkt an die Benachrichtigungsleiste Ihres neuen Benutzers übermittelt, mit der Option, zukünftige Benachrichtigungen zu behalten oder auszuschalten. Anstatt eine „Opt-in“-Journey zu machen, werden die Nutzer:innen eher eine „Opt-out“-Journey machen.

{% alert tip %}
Die vorläufige Autorisierung hat das Potenzial, Ihre Opt-in-Rate drastisch zu erhöhen, aber nur, wenn die Nutzer:innen einen Nutzen in Ihren Nachrichten sehen. Nutzen Sie unsere Funktionen zur [Benutzersegmentierung]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), [Standortbestimmung]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/) und [Personalisierung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/), um sicherzustellen, dass die richtigen Benutzer diese "Test"-Benachrichtigungen zur richtigen Zeit erhalten. Dann können Sie die Nutzer dazu ermutigen, sich für Ihre Push-Benachrichtigungen zu entscheiden, denn Sie wissen, dass diese einen Mehrwert für die Nutzer Ihrer App darstellen.
{% endalert %}

Je nachdem, für welche Option sich der Benutzer entscheidet, wird der entsprechende Token- oder [Abonnementstatus]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) zu seinen [Kontakteinstellungen]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) auf der Registerkarte **Engagement** in seinem Benutzerprofil hinzugefügt.

![Kontakteinstellungen mit einem Push-abonnierten Status.]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

Mit unseren [Segmentierungsfiltern]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) können Sie Ihre Benutzer gezielt ansprechen, je nachdem, ob sie vorläufig autorisiert sind oder nicht.

![Segment Details Panel mit dem Beispiel Segment Filter "Vorläufig autorisiert auf iOS Stoppuhr (iOS) ist wahr", um Nutzer:innen zu targetieren.]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
Wenn Nutzer:innen sich dafür entscheiden, den vorläufigen Push von Ihnen zu deaktivieren, werden sie keine vorläufigen Push-Nachrichten mehr von Ihnen sehen. Achten Sie auf den Inhalt und die Kadenz der Nachrichten, die Sie mit dieser Funktion versenden!
{% endalert %}

{% alert important %}
Wenn Sie zusätzliche Push-Prompts oder [In-App-Push-Primer](https://www.braze.com/resources/glossary/priming-for-push/) (eine In-App-Nachricht, die Benutzer dazu ermutigt, sich für Push-Benachrichtigungen zu entscheiden) verwenden, wenden Sie sich an Ihren Braze-Vertreter, um weitere Unterstützung zu erhalten.
{% endalert %}

#### Vorläufige Push-Benachrichtigungen einrichten

Braze ermöglicht es Ihnen, sich für die vorläufige Authentifizierung zu registrieren, indem Sie Ihren Code in Ihrem Token-Registrierungs-Snippet innerhalb Ihrer Braze iOS SDK-Implementierung anhand der folgenden Snippets als Beispiel aktualisieren (senden Sie diese an Ihre Entwickler oder stellen Sie sicher, dass sie [die vorläufige Push-Authentifizierung während des Integrationsprozesses implementieren]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)).

{% alert warning %}
Die Implementierung der provisorischen Push-Authentifizierung unterstützt nur iOS 12+ und schlägt fehl, wenn das Targeting vor diesem Datum liegt. Mehr dazu erfahren Sie [in unserer ausführlichen Dokumentation zur Implementierung hier]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10).
{% endalert %}

{% tabs local %}
  {% tab Swift %}
**Schnell**

```
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
```
  {% endtab %}
  {% tab Objective-C %}

**Objective-C**

```
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
    options = options | UNAuthorizationOptionProvisional;
}
```
  {% endtab %}
{% endtabs %}

### Unterbrechungsstufe (iOS 15+) {#interruption-level}

Mit dem neuen Fokusmodus von iOS 15 haben Sie mehr Kontrolle darüber, wann App-Benachrichtigungen Sie mit einem Ton oder einer Vibration "unterbrechen" können.

Die Seite mit den Einstellungen für iOS-Benachrichtigungen zeigt Benachrichtigungen an, die für die sofortige Zustellung aktiviert sind, sowie zeitabhängige Benachrichtigungen, die aktiviert sind.]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="max-width:40%"}

Apps können jetzt festlegen, welche Stufe der Unterbrechung eine Benachrichtigung je nach Dringlichkeit enthalten soll.

Um die Unterbrechungsstufe für eine iOS-Push-Benachrichtigung zu ändern, wählen Sie die Registerkarte **Einstellungen** und wählen Sie die gewünschte Stufe aus dem Dropdown-Menü **Unterbrechungsstufe**.

![Dropdown zum Auswählen der Unterbrechungsstufe.]({% image_buster /assets/img/ios/interruption_level.png %}){: style="max-width:50%"}

Für diese Funktion gibt es keine Mindestanforderungen an die SDK-Version, sie gilt jedoch nur für Geräte mit iOS 15+.

Denken Sie daran, dass der Benutzer letztlich die Kontrolle über seinen Fokus hat. Selbst wenn eine zeitabhängige Benachrichtigung zugestellt wird, kann er festlegen, welche Apps seinen Fokus nicht durchbrechen dürfen.

In der folgenden Tabelle finden Sie die Unterbrechungsstufen und ihre Beschreibungen.

|Unterbrechungsstufe|Beschreibung|Wann zu verwenden|Modus "Fokus durchbrechen|
|--|--|--|--|
|[Passiv](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive)|Sendet eine Benachrichtigung ohne Ton, Vibration oder Einschalten des Bildschirms.|Benachrichtigungen, die keine sofortige Aufmerksamkeit erfordern.|Kein:e|
|[Aktiv](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (Standard)|Erzeugt nur dann einen Ton, eine Vibration und schaltet den Bildschirm ein, wenn sich der Benutzer nicht im Fokusmodus befindet.|Benachrichtigungen, die sofortige Aufmerksamkeit erfordern, es sei denn, der Benutzer hat den Fokusmodus aktiviert.|Kein:e|
|[Zeitsensibel](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive)|Erzeugt ein Geräusch, vibriert und schaltet den Bildschirm ein, auch wenn er sich im Fokusmodus befindet. Dazu muss Ihrer App in Xcode die **Funktion Zeitabhängige Benachrichtigungen** hinzugefügt werden.|Rechtzeitige Benachrichtigungen, die Nutzer:innen unabhängig von ihrem Focus-Modus stören sollten, wie z.B. eine Mitfahrgelegenheit oder eine Zustellung.|Ja|
|[Kritisch](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical)|Gibt einen Ton aus, vibriert und schaltet den Bildschirm ein, auch wenn der Schalter **"Nicht stören"** des Telefons aktiviert ist. Dies [erfordert die ausdrückliche Zustimmung von Apple](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/).|Notfälle wie Unwetter oder Sicherheitswarnungen|Ja|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Bewertung der Relevanz (iOS 15+) {#relevance-score}

![Eine Benachrichtigungsübersicht für iOS mit dem Titel "Ihre Abendübersicht" mit drei Benachrichtigungen.]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15 bietet Nutzern:innen außerdem die Möglichkeit, einen Zeitplan für die Zusammenfassung mehrerer Benachrichtigungen zu bestimmten Zeiten im Laufe des Tages zu erstellen. Dies geschieht, um zu verhindern, dass Sie den ganzen Tag über ständig von Benachrichtigungen unterbrochen werden, die keine sofortige Aufmerksamkeit erfordern.

Apps können angeben, welche Push-Benachrichtigungen am relevantesten sind, indem sie einen **Relevanzwert** festlegen. Anhand dieser Punktzahl bestimmt Apple, welche Benachrichtigungen in der geplanten Benachrichtigungsübersicht angezeigt werden, während andere erst verfügbar sind, wenn der Benutzer auf die Zusammenfassung klickt. 

Alle Benachrichtigungen werden weiterhin im Benachrichtigungszentrum des Benutzers angezeigt.

Um den Relevanzwert einer iOS-Benachrichtigung festzulegen, geben Sie auf der Registerkarte **Einstellungen** einen Wert zwischen `0.0` und `1.0` ein. Die wichtigste Nachricht sollte beispielsweise mit `1.0` gesendet werden, während eine Nachricht von mittlerer Wichtigkeit mit `0.5` gesendet werden kann.

![Relevanzwert von "0.5".]({% image_buster /assets/img/ios/relevance-score.png %}){: style="max-width:80%;"}

Für diese Funktion gibt es keine Mindestanforderungen an die SDK-Version, sie gilt jedoch nur für Geräte mit iOS 15+.

Weitere Informationen zur maximalen Nachrichtenlänge für verschiedene Nachrichtentypen finden Sie in den folgenden Ressourcen:

- [Bild- und Textangaben]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [iOS-Richtlinien für die Anzahl der Zeichen]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)

