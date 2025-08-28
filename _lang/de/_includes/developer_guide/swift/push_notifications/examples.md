{% multi_lang_include developer_guide/prerequisites/swift.md %} Sie müssen auch [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

{% alert note %}
Dieser Implementierungsleitfaden konzentriert sich auf eine Swift-Implementierung. Für Interessierte werden jedoch Objective-C-Snippets bereitgestellt.
{% endalert %}

## App-Erweiterungen für Benachrichtigungsinhalte

![Zwei nebeneinander angezeigte Push-Nachrichten. Die Nachricht auf der linken Seite zeigt, wie ein Push mit dem Standard UI aussieht. Die Nachricht auf der rechten Seite zeigt einen Push für eine Bonus-Kaffeekarte, der durch Implementieren einer angepassten Push-UI erstellt wurde.]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

Die Erweiterungen der App für Benachrichtigungsinhalte bieten Ihnen eine großartige Möglichkeit zur Anpassung von Push-Benachrichtigungen. App-Erweiterungen für Benachrichtigungsinhalte zeigen eine angepasste Schnittstelle für die Benachrichtigungen Ihrer App an, wenn eine Push-Benachrichtigung erweitert wird.

Push-Benachrichtigungen können auf drei verschiedene Arten erweitert werden:
- Langes Drücken auf das Push-Banner
- Auf dem Push-Banner nach unten streichen
- Wischen des Banners nach links und Auswählen von "Anzeigen"

Diese angepassten Ansichten bieten intelligente Möglichkeiten für das Engagement von Kund:in, indem sie verschiedene Arten von Inhalten anzeigen, darunter interaktive Benachrichtigungen, mit Nutzerdaten gefüllte Benachrichtigungen und sogar Push-Nachrichten, die Informationen wie Telefonnummern und E-Mails erfassen können. Eines unserer bekannten Features bei Braze, [Push-Storys]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), ist ein Paradebeispiel dafür, wie eine App-Erweiterung mit Push-Benachrichtigungen aussehen kann!

### Anforderungen

![]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) erfolgreich in Ihre App integriert
- Die folgenden Dateien werden von Xcode auf der Grundlage Ihrer Programmiersprache generiert:

**Swift**<br>
- `NotificationViewController.swift`
- `MainInterface.storyboard`

**Objective-C**<br>
- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

## Interaktive Push-Benachrichtigung

Push-Benachrichtigungen können auf Nutzer:innen-Aktionen innerhalb einer App-Erweiterung reagieren. Für Nutzer mit iOS 12 oder höher bedeutet dies, dass Sie Ihre Push-Benachrichtigungen in vollständig interaktive Nachrichten verwandeln können! Dies ist eine interessante Möglichkeit, Ihre Aktionen und Anwendungen interaktiv zu gestalten. Ihre Push-Benachrichtigung kann zum Beispiel ein Spiel, ein Drehrad für Rabatte oder einen "Gefällt mir"-Button zum Speichern eines Eintrags oder Songs enthalten.

Das folgende Beispiel zeigt eine Push-Benachrichtigung, bei der Nutzer innerhalb der erweiterten Benachrichtigung ein Spiel spielen können.

![Ein Diagramm, wie die Phasen einer interaktiven Push-Benachrichtigung aussehen könnten. Eine Sequenz zeigt einen Nutzer, der auf eine Push-Benachrichtigung drückt, die ein interaktives Spiel anzeigt.]({% image_buster /assets/img/push_implementation_guide/push12.png %}){: style="border:0"}

### Dashboard Konfiguration

Um eine interaktive Push-Benachrichtigung zu erstellen, müssen Sie in Ihrem Dashboard eine angepasste Ansicht einstellen. 

1. Klicken Sie auf der Seite **Kampagnen** auf **Kampagne erstellen**, um eine neue Kampagne mit Push-Benachrichtigungen zu starten.
2. Schalten Sie auf dem Tab **Verfassen** die **Benachrichtigungsbuttons** um. 
3. Geben Sie eine angepasste iOS-Kategorie in das Feld **iOS-Benachrichtigungskategorie** ein. 
4. Legen Sie in der `.plist` Ihres Notification Content Extension Target das Attribut `UNNotificationExtensionCategory` auf Ihre angepasste iOS-Kategorie fest. Der hier angegebene Wert muss mit dem übereinstimmen, der im Braze-Dashboard unter **iOS Benachrichtigungskategorie** eingestellt ist. 
5. Setzen Sie den Schlüssel `UNNotificationExtensionInteractionEnabled` auf `true`, um Nutzer in einer Push-Benachrichtigung zu aktivieren.

![Die Optionen für den Button zur Benachrichtigung, die in den Einstellungen des Nachrichten-Editors für Push-Nachrichten zu finden sind.]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

## Personalisierte Push-Benachrichtigungen

![Zwei iPhones werden nebeneinander angezeigt. Das erste iPhone zeigt die ungekürzte Ansicht der Push-Nachricht. Das zweite iPhone zeigt die erweiterte Version der Push-Nachricht mit einer Fortschrittsanzeige, die angibt, wie weit sie in einem Kurs fortgeschritten sind, den Namen der nächsten Sitzung und wann die nächste Sitzung abgeschlossen werden muss.]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

Push-Benachrichtigungen können benutzerspezifische Informationen innerhalb einer Inhaltserweiterung anzeigen. Damit ist es zulässig, Push-Inhalte für Nutzer zu erstellen, z. B. die Option, Ihren Fortschritt auf verschiedenen Plattformen zu teilen, freigeschaltete Erfolge anzuzeigen oder Onboarding-Checklisten anzuzeigen. Dieses Beispiel zeigt eine Push-Benachrichtigung, die einem Nutzer:innen angezeigt wird, nachdem sie eine bestimmte Aufgabe im Braze-Lernkurs erledigt haben. Wenn Sie die Benachrichtigung erweitern, können die Nutzer ihren Fortschritt auf ihrem Lernpfad sehen. Die hier bereitgestellten Informationen sind benutzerspezifisch und können über einen API-Trigger ausgelöst werden, wenn eine Sitzung abgeschlossen ist oder eine bestimmte Nutzeraktion durchgeführt wird. 

### Dashboard Konfiguration

Um eine personalisierte Push-Benachrichtigung zu erstellen, müssen Sie in Ihrem Dashboard eine angepasste Ansicht einstellen. 

1. Klicken Sie auf der Seite **Kampagnen** auf **Kampagne erstellen**, um eine neue Kampagne mit Push-Benachrichtigungen zu starten.
2. Schalten Sie auf dem Tab **Verfassen** die **Benachrichtigungsbuttons** um. 
3. Geben Sie eine angepasste iOS-Kategorie in das Feld **iOS-Benachrichtigungskategorie** ein. 
4. Auf dem Tab **Einstellungen** erstellen Sie Schlüssel-Wert-Paare mit dem Standard Liquid. Legen Sie die entsprechenden Nutzer:innen-Attribute fest, die in der Nachricht angezeigt werden sollen. Diese Ansichten können auf der Grundlage bestimmter Benutzerattribute eines bestimmten Benutzerprofils personalisiert werden.
5. Legen Sie in der `.plist` Ihres Notification Content Extension Target das Attribut `UNNotificationExtensionCategory` auf Ihre angepasste iOS-Kategorie fest. Der hier angegebene Wert muss mit dem übereinstimmen, der im Braze-Dashboard unter **iOS Benachrichtigungskategorie** eingestellt ist. 

![Vier Sätze von Schlüssel-Wert-Paaren, wobei "next_session_name" und "next_session_complete_date" als API-getriggerte Eigenschaft mit Liquid und "completed_session count" und "total_session_count" als angepasstes Nutzerattribut mit Liquid festgelegt werden.]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

### Umgang mit Schlüssel-Wert-Paaren

Die Methode `didReceive` wird aufgerufen, wenn die App-Erweiterung für Benachrichtigungsinhalte eine Benachrichtigung erhalten hat. Diese Methode finden Sie unter `NotificationViewController`. Die im Dashboard bereitgestellten Schlüssel-Wert-Paare werden im Code durch die Verwendung eines Wörterbuchs des Typs `userInfo` dargestellt.

#### Analysieren von Schlüssel-Werte-Paaren aus Push-Benachrichtigungen

{% tabs %}
{% tab Swift %}
``` swift 
func didReceive(_ notification: UNNotification) {
  let userInfo = notification.request.content.userInfo
     
  guard let value = userInfo["YOUR-KEY-VALUE-PAIR"] as? String,
        let otherValue = userInfo["YOUR-OTHER-KEY-VALUE-PAIR"] as? String,
  else { fatalError("Key-Value Pairs are incorrect.")}
 
  ...
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotification:(nonnull UNNotification *)notification {
  NSDictionary *userInfo = notification.request.content.userInfo;
   
  if (userInfo[@"YOUR-KEY-VALUE-PAIR"] && userInfo[@"YOUR-OTHER-KEY-VALUE-PAIR"]) {
 
  ...
 
  } else {
    [NSException raise:NSGenericException format:@"Key-Value Pairs are incorrect"];
  }
}
```
{% endtab %}
{% endtabs %}

## Push-Benachrichtigung zur Informationserfassung

Push-Benachrichtigungen können Nutzer auch in einer App-Erweiterung erfassen und so die Einsatzmöglichkeiten von Push noch zusätzlich erweitern. Wenn Sie über Push-Benachrichtigungen Benutzereingaben anfordern, können Sie nicht nur grundlegende Informationen wie Name oder E-Mail anfragen, sondern Nutzer:innen auch auffordern, Feedback zu geben oder ein unvollständiges Nutzerprofil zu vervollständigen. 

{% alert tip %}
Weitere Informationen finden Sie unter [Protokollierung von Daten für Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/analytics/logging_channel_data/push_notifications/).
{% endalert %}

Im folgenden Ablauf ist die angepasste Ansicht in der Lage, auf Zustandsänderungen zu reagieren. Diese Komponenten der Zustandsänderung werden in jedem Bild dargestellt. 

1. Der Benutzer erhält eine Push-Benachrichtigung.
2. Push ist geöffnet. Nach dem Erweitern fordert der Push den Nutzer zur Eingabe von Informationen auf. In diesem Beispiel wird die E-Mail Adresse des Nutzers angefragt, aber Sie können jede beliebige Information anfragen.
3. Die Informationen werden bereitgestellt und wenn sie das erwartete Format haben, wird der Button für die Registrierung angezeigt.
3. Die Bestätigungsansicht wird angezeigt, und Push wird abgebrochen. 

![]({% image_buster /assets/img/push_implementation_guide/push8.png %}){: style="border:0;"}

### Dashboard Konfiguration

Um eine Push-Benachrichtigung zur Informationserfassung zu erstellen, müssen Sie in Ihrem Dashboard eine angepasste Ansicht einstellen. 

1. Klicken Sie auf der Seite **Kampagnen** auf **Kampagne erstellen**, um eine neue Kampagne mit Push-Benachrichtigungen zu starten.
2. Schalten Sie auf dem Tab **Verfassen** die **Benachrichtigungsbuttons** um. 
3. Geben Sie eine angepasste iOS-Kategorie in das Feld **iOS-Benachrichtigungskategorie** ein. 
4. Auf dem Tab **Einstellungen** erstellen Sie Schlüssel-Wert-Paare mit dem Standard Liquid. Legen Sie die entsprechenden Nutzer:innen-Attribute fest, die in der Nachricht angezeigt werden sollen. 
5. Legen Sie in der `.plist` Ihres Notification Content Extension Target das Attribut `UNNotificationExtensionCategory` auf Ihre angepasste iOS-Kategorie fest. Der hier angegebene Wert muss mit dem übereinstimmen, der im Braze-Dashboard unter **iOS Benachrichtigungskategorie** eingestellt ist. 

Wie im Beispiel zu sehen, können Sie auch ein Bild in Ihre Push-Benachrichtigung einfügen. Dazu müssen Sie [Rich Notifications]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift) integrieren, den Benachrichtigungsstil in Ihrer Kampagne auf Rich Notification einstellen und ein Rich-Push-Bild einfügen.

![Eine Push-Nachricht mit drei Gruppen von Schlüssel-Wert-Paaren. 1\. "Braze_id" als Liquid-Aufruf zum Abrufen der Braze-ID eingestellt. 2\. "cert_title" als "Braze Marketer Certification" festgelegt. 3\. "Cert_description" ist auf "Certified Braze marketers drive..." festgelegt.]({% image_buster /assets/img/push_implementation_guide/push9.png %})

### Verarbeitung von Button-Aktionen

Jeder Aktions-Button ist eindeutig gekennzeichnet. Der Code prüft, ob der Antwort-Bezeichner mit `actionIndentifier` übereinstimmt. Wenn ja, weiß er, dass der Nutzer auf den Aktions-Button geklickt hat.

**Verarbeitung von Antworten auf Aktions-Buttons in Push-Benachrichtigungen**<br>

{% tabs %}
{% tab Swift %}
``` swift 
func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
  if response.actionIdentifier == "YOUR-REGISTER-IDENTIFIER" {
    // do something
  } else {
    // do something else
  }
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response completionHandler:(void (^)(UNNotificationContentExtensionResponseOption))completion {
  if ([response.actionIdentifier isEqualToString:@"YOUR-REGISTER-IDENTIFIER"]) {
    completion(UNNotificationContentExtensionResponseOptionDismiss);
  } else {
    completion(UNNotificationContentExtensionResponseOptionDoNotDismiss);
  }
}
```
{% endtab %}
{% endtabs %}

### Ausblenden von Pushes

Push-Benachrichtigungen können durch Drücken eines Aktions-Buttons automatisch ausgeblendet werden. Es gibt drei vorgefertigte Optionen zum Ausblenden von Push-Nachrichten, die wir empfehlen:

1. `completion(.dismiss)` - Weist die Benachrichtigung zurück
2. `completion(.doNotDismiss)` - Benachrichtigung bleibt offen
3. `completion(.dismissAndForward)` - Push lehnt ab und der Nutzer:innen wird in die Anwendung weitergeleitet
