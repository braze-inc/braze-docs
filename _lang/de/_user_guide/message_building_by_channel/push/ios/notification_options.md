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

> Mit der Veröffentlichung von Apples iOS 12 bietet Braze Unterstützung für mehrere Features, darunter [Benachrichtigungsgruppen](#notification-groups), [stille Benachrichtigungen/vorläufige Autorisierung](#provisional-push-authentication--quiet-notifications) und [kritische Alarme](#critical-alerts).

## Benachrichtigungsgruppen

Wenn Sie Ihre Nachrichten kategorisieren und im Benachrichtigungsfeld Ihrer Nutzer:innen gruppieren möchten, können Sie über Braze die Funktion Benachrichtigungsgruppen von iOS nutzen.

Erstellen Sie Ihre iOS-Push-Kampagne, gehen Sie anschließend zum Tab **Einstellungen** und öffnen Sie das Dropdown-Menü **Benachrichtigungsgruppe**.

![Der Tab „Einstellungen" mit einem Dropdown-Menü „Benachrichtigungsgruppe", in dem der Wert „Gutscheine" ausgewählt wurde.]({% image_buster /assets/img_archive/notification_group_dropdown.png %}){: style="max-width:50%;" }

Wählen Sie Ihre Benachrichtigungsgruppen aus der Dropdown-Liste. Wenn Ihre Einstellungen für die Benachrichtigungsgruppe nicht korrekt funktionieren oder Sie **Keine** aus der Dropdown-Liste auswählen, wird die Nachricht automatisch wie gewohnt an alle definierten Nutzer:innen im Workspace gesendet.

Wenn hier keine Benachrichtigungsgruppen aufgeführt sind, können Sie eine mithilfe der iOS-Thread-ID hinzufügen. Sie benötigen eine iOS-Thread-ID für jede Benachrichtigungsgruppe, die Sie hinzufügen möchten. Fügen Sie sie dann zu Ihren Benachrichtigungsgruppen hinzu, indem Sie in der Dropdown-Liste auf **Benachrichtigungsgruppen verwalten** klicken und die erforderlichen Felder im Fenster **iOS-Push-Benachrichtigungsgruppen verwalten** ausfüllen, das dann erscheint.

![Fenster zur Verwaltung von iOS-Push-Benachrichtigungsgruppen.]({% image_buster /assets/img_archive/managenotgroups.png %}){: style="max-width:70%;" }

Erstellen Sie Ihre iOS-Push-Kampagne und sehen Sie sich dann den oberen Teil des Composers an. Dort sehen Sie ein Dropdown-Menü mit der Bezeichnung **Benachrichtigungsgruppen**.

### Zusammenfassende Argumente

Zusätzlich zur Gruppierung von Benachrichtigungen nach Thread-IDs erlaubt Apple Ihnen, die Zusammenfassungen zu bearbeiten, die angezeigt werden, wenn Benachrichtigungen gruppiert werden. Braze-Nutzer:innen können die Zusammenfassungskategorie, die Zusammenfassungsanzahl und das Zusammenfassungsargument angeben, wenn sie eine Push-Kampagne mit unserem Tool erstellen.

{% alert tip %}
Beachten Sie, dass die Art und Weise, wie Benachrichtigungen mit der gleichen Thread-ID in der Benachrichtigungsleiste gruppiert werden, vom Betriebssystem gesteuert wird. iOS kann Benachrichtigungen mit der gleichen Thread-ID separat oder in Gruppen anzeigen, je nachdem, was es für optimal hält.
{% endalert %}

Markieren Sie das Feld **Alarmoptionen** im **Push Composer**.

Wählen Sie dann `summary-arg` und `summary-arg-count` als Schlüssel und geben Sie die entsprechenden Werte in die zugehörige Spalte ein. Wenn Sie keinen Wert für `summary-arg` eingeben, wird dieser standardmäßig auf 1 festgelegt.

### Zusammenfassungskategorien

Mit den Zusammenfassungskategorien können Sie die gesamte Zusammenfassung anpassen, die erscheint, wenn Benachrichtigungen gruppiert werden. Sie können mehrere Kategorien erstellen und anwenden.

Um eine Kategorie in Ihrer Nachricht zu verwenden, arbeiten Sie mit Ihren Entwickler:innen zusammen, um die Implementierung anhand des folgenden Beispiels vorzunehmen:

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
Beachten Sie, dass `%u` und `%@` Formatierungs-Strings für die Zusammenfassungsanzahl bzw. das Zusammenfassungsargument sind. Wenn die Zusammenfassung angezeigt wird, werden diese Platzhalter durch die Werte für `summary-count` und `summary-arg` ersetzt.
{% endalert %}

Sobald dies in Ihrer App eingerichtet ist, verwenden Sie die Zusammenfassungskategorie, indem Sie das Feld **Benachrichtigungs-Buttons** markieren und die Option **Vorregistrierte iOS-Kategorie eingeben** wählen.

Geben Sie dann den Bezeichner der Zusammenfassungskategorie ein, den Sie in Ihrer App festgelegt haben.

### Vorläufige Push-Authentifizierung und stille Benachrichtigungen {#provisional-push}

Apple bietet Marken die Möglichkeit, stille Push-Benachrichtigungen an die Notification Center ihrer Nutzer:innen zu senden, bevor diese sich offiziell und explizit dafür entscheiden. So haben Sie die Chance, den Wert Ihrer Nachrichten frühzeitig zu demonstrieren. Alles, was Sie tun müssen, ist, [vorläufige Push-Benachrichtigungen](#set-up-provisional-push-notifications) in Ihrer App einzurichten. Dann erhält jede:r Nutzer:in mit einem vorläufigen Push-Token Ihre Nachrichten.

Im Gegensatz zu einem herkömmlichen iOS-Push-Token fungiert ein vorläufiges Push-Token als „Probezugang", der es Marken ermöglicht, neue Nutzer:innen zu erreichen, bevor diese die native Opt-in-Anfrage von Apple gesehen und angeklickt haben. Mit diesem Feature wird Ihre Push-Benachrichtigung direkt an die Benachrichtigungsleiste Ihrer neuen Nutzer:innen übermittelt – mit der Option, zukünftige Benachrichtigungen zu „Behalten" oder „Auszuschalten". Anstatt eine „Opt-in"-Journey zu durchlaufen, erleben die Nutzer:innen eher eine „Opt-out"-Journey.

{% alert tip %}
Die vorläufige Autorisierung hat das Potenzial, Ihre Opt-in-Rate drastisch zu erhöhen – aber nur, wenn die Nutzer:innen einen Wert in Ihren Nachrichten sehen. Nutzen Sie unsere Features zur [Segmentierung]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), zum [Standort-Targeting]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/) und zur [Personalisierung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/), um sicherzustellen, dass die richtigen Nutzer:innen diese „Test"-Benachrichtigungen zur richtigen Zeit erhalten. Dann können Sie die Nutzer:innen dazu ermutigen, sich vollständig für Ihre Push-Benachrichtigungen zu entscheiden, da diese einen Mehrwert für das App-Erlebnis Ihrer Nutzer:innen darstellen.
{% endalert %}

Je nachdem, für welche Option sich die Nutzer:innen entscheiden, wird das entsprechende Token oder der [Abo-Status]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) zu ihren [Kontakteinstellungen]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) auf dem Tab **Engagement** in ihrem Nutzerprofil hinzugefügt.

![Kontakteinstellungen mit Push-Abo-Status.]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

Mit unseren [Segmentierungsfiltern]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) können Sie Ihre Nutzer:innen gezielt ansprechen, je nachdem, ob sie vorläufig autorisiert sind oder nicht.

![Segmentdetails-Panel mit dem Beispiel-Segmentfilter „Vorläufig autorisiert auf iOS-Stoppuhr (iOS) ist wahr", um die Zielgruppe zusammenzustellen.]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
Wenn Nutzer:innen sich dafür entscheiden, den vorläufigen Push von Ihnen zu deaktivieren, werden sie keine vorläufigen Push-Nachrichten mehr von Ihnen sehen. Achten Sie auf den Inhalt und die Frequenz der Nachrichten, die Sie mit dieser Funktion versenden!
{% endalert %}

{% alert important %}
Sollten Sie zusätzliche Push-Aufforderungen oder [In-App-Push-Primer](https://www.braze.com/resources/glossary/priming-for-push/) (eine In-App-Nachricht, die Nutzer:innen dazu ermutigt, Push-Benachrichtigungen zu aktivieren) verwenden, wenden Sie sich bitte an Ihre Braze-Vertretung, um weitere Informationen zu erhalten.
{% endalert %}

#### Vorläufige Push-Benachrichtigungen einrichten

Braze ermöglicht es Ihnen, sich für die vorläufige Authentifizierung zu registrieren, indem Sie Ihren Code in Ihrem Token-Registrierungs-Snippet innerhalb Ihrer Braze iOS SDK-Implementierung anhand der folgenden Snippets als Beispiel aktualisieren (senden Sie diese an Ihre Entwickler:innen oder stellen Sie sicher, dass sie [die vorläufige Push-Authentifizierung während des Integrationsprozesses implementieren]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)).

{% alert warning %}
Die Implementierung der vorläufigen Push-Authentifizierung unterstützt nur iOS 12+ und schlägt fehl, wenn das Deployment-Target davor liegt. Mehr dazu erfahren Sie [in unserer ausführlichen Implementierungsdokumentation hier]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10).
{% endalert %}

{% tabs local %}
  {% tab Swift %}
**Swift**

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

Mit dem neuen Fokusmodus von iOS 15 haben Nutzer:innen mehr Kontrolle darüber, wann App-Benachrichtigungen sie mit einem Ton oder einer Vibration „unterbrechen" können.

![Die Seite „iOS-Benachrichtigungseinstellungen" zeigt Benachrichtigungen an, die für die sofortige Zustellung aktiviert sind, sowie zeitkritische Benachrichtigungen, die aktiviert sind.]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="max-width:40%"}

Apps können jetzt festlegen, welche Unterbrechungsstufe eine Benachrichtigung je nach Dringlichkeit haben soll.

Um die Unterbrechungsstufe für eine iOS-Push-Benachrichtigung zu ändern, wählen Sie den Tab **Einstellungen** und wählen Sie die gewünschte Stufe aus dem Dropdown-Menü **Unterbrechungsstufe**.

![Dropdown-Menü zum Auswählen der Unterbrechungsstufe.]({% image_buster /assets/img/ios/interruption_level.png %}){: style="max-width:50%"}

Für dieses Feature gibt es keine Mindestanforderungen an die SDK-Version, es gilt jedoch nur für Geräte mit iOS 15+.

Denken Sie daran, dass die Nutzer:innen letztlich die Kontrolle über ihren Fokus haben. Selbst wenn eine zeitkritische Benachrichtigung zugestellt wird, können sie festlegen, welche Apps ihren Fokus nicht durchbrechen dürfen.

In der folgenden Tabelle finden Sie die Unterbrechungsstufen und ihre Beschreibungen.

|Unterbrechungsstufe|Beschreibung|Wann zu verwenden|Fokusmodus durchbrechen|
|--|--|--|--|
|[Passiv](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive)|Sendet eine Benachrichtigung ohne Ton, Vibration oder Einschalten des Bildschirms.|Benachrichtigungen, die keine sofortige Aufmerksamkeit erfordern.|Nein|
|[Aktiv](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (Standard)|Erzeugt nur dann einen Ton, eine Vibration und schaltet den Bildschirm ein, wenn sich die Nutzer:innen nicht im Fokusmodus befinden.|Benachrichtigungen, die sofortige Aufmerksamkeit erfordern, es sei denn, der Fokusmodus ist aktiviert.|Nein|
|[Zeitkritisch](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive)|Erzeugt einen Ton, vibriert und schaltet den Bildschirm ein, auch im Fokusmodus. Dazu muss Ihrer App in Xcode die Funktion **Zeitkritische Benachrichtigungen** hinzugefügt werden.|Zeitkritische Benachrichtigungen, die Nutzer:innen unabhängig von ihrem Fokusmodus erreichen sollten, wie z. B. eine Mitfahrgelegenheits- oder Zustellungsbenachrichtigung.|Ja|
|[Kritisch](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical)|Gibt einen Ton aus, vibriert und schaltet den Bildschirm ein, auch wenn der Schalter **„Nicht stören"** des Telefons aktiviert ist. Dies [erfordert die ausdrückliche Genehmigung von Apple](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/).|Notfälle wie Unwetter- oder Sicherheitswarnungen|Ja|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Relevanzbewertung (iOS 15+) {#relevance-score}

![Eine Benachrichtigungsübersicht für iOS mit dem Titel „Ihre Abendübersicht" mit drei Benachrichtigungen.]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15 bietet Nutzer:innen außerdem eine neue Möglichkeit, optional einen Zeitplan für die Zusammenfassung mehrerer Benachrichtigungen zu bestimmten Zeiten im Laufe des Tages zu erstellen. Dies verhindert ständige Unterbrechungen durch Benachrichtigungen, die keine sofortige Aufmerksamkeit erfordern.

Apps können angeben, welche Push-Benachrichtigungen am relevantesten sind, indem sie eine **Relevanzbewertung** festlegen. Anhand dieser Bewertung bestimmt Apple, welche Benachrichtigungen in der geplanten Benachrichtigungsübersicht hervorgehoben werden, während andere erst verfügbar sind, wenn die Nutzer:innen auf die Zusammenfassung tippen.

Alle Benachrichtigungen werden weiterhin im Benachrichtigungszentrum der Nutzer:innen angezeigt.

Um die Relevanzbewertung einer iOS-Benachrichtigung festzulegen, geben Sie im Tab **Einstellungen** einen Wert zwischen `0.0` und `1.0` ein. Die wichtigste Nachricht sollte beispielsweise mit `1.0` gesendet werden, während eine Nachricht von mittlerer Wichtigkeit mit `0.5` gesendet werden kann.

![Relevanzbewertung von „0,5".]({% image_buster /assets/img/ios/relevance-score.png %}){: style="max-width:80%;"}

Für dieses Feature gibt es keine Mindestanforderungen an die SDK-Version, es gilt jedoch nur für Geräte mit iOS 15+.

Weitere Informationen zur maximalen Nachrichtenlänge für verschiedene Nachrichtentypen finden Sie in den folgenden Ressourcen:

- [Bild- und Textspezifikationen für Push]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push)
- [iOS-Richtlinien für die Zeichenanzahl]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)