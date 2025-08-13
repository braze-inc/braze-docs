---
nav_title: Erweiterte Implementierung (optional)
article_title: Erweiterte Implementierung von Push-Benachrichtigungen für iOS (optional)
platform: Swift
page_order: 30
description: "Dieser Leitfaden für die erweiterte Implementierung beschreibt, wie Sie die App-Erweiterungen für iOS-Push-Benachrichtigungen nutzen können, um den größtmöglichen Erfolg mit Ihren Push-Nachrichten im Swift SDK zu erzielen."
channel:
  - push
---

<br>
{% alert important %}
Suchen Sie nach dem Leitfaden für die Integration von Push-Benachrichtigungen für Entwickler? Sie finden es [hier]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/).
{% endalert %}

# Leitfaden für die erweiterte Implementierung

> Dieser optionale Leitfaden für die erweiterte Implementierung beschreibt, wie Sie die App-Erweiterungen für Benachrichtigungen nutzen können, um den größtmöglichen Erfolg mit Ihren Push-Nachrichten zu erzielen. 

In diesem Leitfaden finden Sie drei Beispielimplementierungen von App-Erweiterungen für Benachrichtigungsinhalte, jeweils mit einem Konzept-Walkthrough, potenziellen Anwendungsfällen und einem Blick darauf, wie Push-Benachrichtigungsvariablen im Braze-Dashboard aussehen und verwendet werden können:
- [Interaktive Push-Benachrichtigung](#interactive-push-notification)
- [Personalisierte Push-Benachrichtigungen](#personalized-push-notifications)
- [Push-Benachrichtigungen zur Informationserfassung](#information-capture-push-notification)

Dieser Artikel enthält auch eine [Anleitung zur Protokollierung von Analytics](#logging-analytics) für diese angepassten Implementierungen.

Beachten Sie, dass sich dieser Implementierungsleitfaden auf eine Swift-Implementierung konzentriert, aber für Interessierte auch Objective-C-Snippets bereitstellt.

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
- [Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) erfolgreich in Ihre App integriert
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

### Sind Sie bereit für die Protokollierung von Analysen?
Besuchen Sie den Abschnitt [Protokollieren von Analytics](#logging-analytics), um ein besseres Verständnis dafür zu bekommen, wie der Datenfluss aussehen sollte.

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

### Sind Sie bereit für die Protokollierung von Analysen?
Besuchen Sie den Abschnitt [Protokollieren von Analytics](#logging-analytics), um ein besseres Verständnis dafür zu bekommen, wie der Datenfluss aussehen sollte.

## Push-Benachrichtigung zur Informationserfassung

Push-Benachrichtigungen können Nutzer auch in einer App-Erweiterung erfassen und so die Einsatzmöglichkeiten von Push noch zusätzlich erweitern. Wenn Sie über Push-Benachrichtigungen Benutzereingaben anfordern, können Sie nicht nur grundlegende Informationen wie Name oder E-Mail anfragen, sondern Nutzer:innen auch auffordern, Feedback zu geben oder ein unvollständiges Nutzerprofil zu vervollständigen. 

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

Wie im Beispiel zu sehen, können Sie auch ein Bild in Ihre Push-Benachrichtigung einfügen. Dazu müssen Sie [Rich Notifications]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/) integrieren, den Benachrichtigungsstil in Ihrer Kampagne auf Rich Notification einstellen und ein Rich-Push-Bild einfügen.

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

### Sind Sie bereit für die Protokollierung von Analysen?
Im [folgenden Abschnitt](#logging-analytics) wird näher beschrieben, wie der Datenfluss aussehen sollte. 

## Protokollieren von Analytics

### Protokollierung mit der Braze API (empfohlen)

Mit Hilfe des [`/users/track`-Endpunkts]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) der Braze API können Sie Analytics in Realtime protokollieren. Senden Sie dazu den Wert `braze_id` in das Feld der Schlüssel-Wert-Paare (wie im folgenden Screenshot zu sehen), um das zu aktualisierende Nutzerprofil zu identifizieren.

![Eine Push-Nachricht mit drei Gruppen von Schlüssel-Wert-Paaren. 1\. "Braze_id" als Liquid-Aufruf zum Abrufen der Braze-ID eingestellt. 2\. "cert_title" als "Braze Marketer Certification" festgelegt. 3\. "Cert_description" ist auf "Certified Braze marketers drive..." festgelegt.]({% image_buster /assets/img/push_implementation_guide/push18.png %}){: style="max-width:80%;"}

### Manuell protokollieren

Für die manuelle Protokollierung müssen Sie zunächst Workspaces-in Xcode konfigurieren und anschließend Analytics erstellen, speichern und abrufen. Dies erfordert einige Anpassungen auf Ihrer Seite. Die folgenden Codeschnipsel helfen Ihnen bei der Lösung dieses Problems. 

Ein wichtiger Punkt, den es zu beachten gilt, ist, dass Analytics erst dann an Braze gesendet werden, wenn die mobile Anwendung anschließend gestartet wird. Das bedeutet, dass je nach Ihren Einstellungen für die Beendigung oft eine unbestimmte Zeitspanne zwischen der Beendigung einer Push-Benachrichtigung und dem Start der mobilen App und dem Abrufen der Analysen vergeht. Auch wenn dieser Zeitpuffer nicht alle Anwendungsfälle betrifft, sollten Sie diese Auswirkung berücksichtigen und Ihre Nutzer:innen so anpassen, dass sie die Öffnung der Anwendung einbeziehen, um dieses Problem zu lösen. 

![Grafik, die die Verarbeitung von Analytics in Braze beschreibt. 1\. Es werden Analysedaten erstellt. 2\. Die Analysedaten werden gespeichert. 3\. Die Push-Benachrichtigung wird abgelehnt. 4\. Unbestimmte Zeitspanne zwischen der Ablehnung der Push-Benachrichtigung und dem Start der mobilen App. 5\. Die mobile App wird gestartet. 6\. Analysedaten werden empfangen. 7\. Die Analysedaten werden an Braze gesendet.]({% image_buster /assets/img/push_implementation_guide/push13.png %})

#### Schritt 1: App-Gruppen in Xcode konfigurieren
Fügen Sie in Xcode die Funktion `App Groups` hinzu. Wenn Sie noch keine Workspaces in Ihrer App hatten, gehen Sie zu den Fähigkeiten des Haupt-Targetings der App, aktivieren Sie `App Groups` und klicken Sie auf den Button **+** Hinzufügen. Verwenden Sie dann die Bundle ID Ihrer App, um den Workspace zu erstellen. Wenn die Bundle-ID Ihrer App zum Beispiel `com.company.appname` lautet, können Sie Ihren Workspace `group.com.company.appname.xyz` nennen. Vergewissern Sie sich, dass `App Groups` sowohl für die Hauptzielgruppe Ihrer App als auch für die Zielgruppe der Inhaltserweiterung aktiviert ist.

![]({% image_buster /assets/img/swift/push_story/add_app_groups.png %})

#### Schritt 2: Code-Snippets integrieren
Die folgenden Code-Snippets sind eine hilfreiche Referenz, wie Sie angepasste Events, angepasste Attribute und Nutzerattribute speichern und senden können. Diese Anleitung bezieht sich auf `UserDefaults`, aber der Code wird in Form der Hilfsdatei `RemoteStorage` dargestellt. Es gibt zusätzliche Hilfsdateien, `UserAttributes` und `EventName Dictionary`, die beim Senden und Speichern von Nutzerattributen verwendet werden.

{% tabs local %}
{% tab Benutzerdefinierte Ereignisse %}

##### Speichern von benutzerdefinierten Ereignissen

Um angepasste Events zu speichern, müssen Sie die Analytics von Grund auf neu erstellen. Dazu erstellen Sie ein Wörterbuch, füllen es mit Metadaten und speichern die Daten mit Hilfe einer Hilfsdatei.

1. Initialisieren Sie ein Wörterbuch mit Event-Metadaten
2. Initialisieren Sie `userDefaults`, um die Event-Daten abzurufen und zu speichern.
3. Wenn es ein bestehendes Array gibt: Fügen Sie die neuen Daten an das bestehende Array an und speichern Sie.
4. Wenn es kein bestehendes Array gibt: Speichern Sie das neue Array in `userDefaults`.

{% subtabs global %}
{% subtab Swift %}
``` swift 
func saveCustomEvent(with properties: [String: Any]? = nil) {
  // 1
  let customEventDictionary = Dictionary(eventName: "YOUR-EVENT-NAME", properties: properties)
  
  // 2
  let remoteStorage = RemoteStorage(storageType: .suite)
  
  // 3   
  if var pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) as? [[String: Any]] {
    pendingEvents.append(contentsOf: [customEventDictionary])
    remoteStorage.store(pendingEvents, forKey: .pendingCustomEvents)
  } else {
  // 4
    remoteStorage.store([customEventDictionary], forKey: .pendingCustomEvents)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)saveCustomEvent:(NSDictionary<NSString *, id> *)properties {
  // 1 
  NSDictionary<NSString *, id> *customEventDictionary = [[NSDictionary alloc] initWithEventName:@"YOUR-EVENT-NAME" properties:properties];
  
  // 2
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingEvents = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomEvents] mutableCopy];
  
  // 3 
  if (pendingEvents) {
    [pendingEvents addObject:customEventDictionary];
    [remoteStorage store:pendingEvents forKey:RemoteStorageKeyPendingCustomAttributes];
  } else {
  // 4
    [remoteStorage store:@[ customEventDictionary ] forKey:RemoteStorageKeyPendingCustomAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

##### Senden von angepassten Events an Braze

Der beste Zeitpunkt, um gespeicherte Analytics von einer App-Erweiterung für Benachrichtigungsinhalte zu protokollieren, ist direkt nach der Initialisierung des SDK. Dazu durchlaufen Sie alle ausstehenden Events, suchen nach dem Schlüssel "Ereignisname", setzen die entsprechenden Werte in Braze und löschen dann den Speicher für das nächste Mal, wenn diese Funktion benötigt wird.

1. Array der ausstehenden Events mit einer Schleife durchlaufen
2. Jedes Schlüssel-Wert-Paar im Wörterbuch `pendingEvents` mit einer Schleife durchlaufen
3. Schlüssel für "Event-Name" expliziert überprüfen, um den Wert entsprechend festzulegen
4. Jeder andere Schlüsselwert wird dem `properties` Wörterbuch hinzugefügt.
5. Individuelles benutzerdefiniertes Ereignis protokollieren 
6. Alle ausstehenden Events aus dem Speicher entfernen.

{% subtabs global %}
{% subtab Swift %}
``` swift 
func logPendingCustomEventsIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) as? [[String: Any]] else { return }
  
  // 1    
  for event in pendingEvents {
    var eventName: String?
    var properties: [AnyHashable: Any] = [:]
    
  // 2
    for (key, value) in event {
      if key == PushNotificationKey.eventName.rawValue {
  // 3      
        if let eventNameValue = value as? String {
          eventName = eventNameValue
        } else {
          print("Invalid type for event_name key")
        }
      } else {
  // 4 
        properties[key] = value
      }
    }
  // 5    
    if let eventName = eventName {
      AppDelegate.braze?.logCustomEvent(eventName, properties: properties)
    }
  }

  // 6    
  remoteStorage.removeObject(forKey: .pendingCustomEvents)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingEventsIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingEvents = [remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomEvents];
  
  // 1 
  for (NSDictionary<NSString *, id> *event in pendingEvents) {
    NSString *eventName = nil;
    NSMutableDictionary *properties = [NSMutableDictionary dictionary];
    
  // 2 
    for (NSString* key in event) {
      if ([key isEqualToString:@"event_name"]) {
  // 3       
        if ([[event objectForKey:key] isKindOfClass:[NSString class]]) {
          eventName = [event objectForKey:key];
        } else {
          NSLog(@"Invalid type for event_name key");
        }
      } else {
  // 4 
        properties[key] = event[key];
      }
    }
  // 5  
    if (eventName != nil) {
      [AppDelegate.braze logCustomEvent:eventName properties:properties];
    }
  }

  // 6  
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingCustomEvents];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Benutzerdefinierte Attribute %}

##### Speichern von benutzerdefinierten Attributen

Um angepasste Attribute zu speichern, müssen Sie die Analytics von Grund auf neu erstellen. Dazu erstellen Sie ein Wörterbuch, füllen es mit Metadaten und speichern die Daten mit Hilfe einer Hilfsdatei.

1. Initialisieren Sie ein Wörterbuch mit Attribut-Metadaten
2. Initialisieren Sie `userDefaults`, um die Attributdaten abzurufen und zu speichern.
3. Wenn es ein bestehendes Array gibt: Fügen Sie die neuen Daten an das bestehende Array an und speichern Sie.
4. Wenn es kein bestehendes Array gibt: Speichern Sie das neue Array in `userDefaults`.

{% subtabs global %}
{% subtab Swift %}
``` swift 
func saveCustomAttribute() {
  // 1 
  let customAttributeDictionary: [String: Any] = ["YOUR-CUSTOM-ATTRIBUTE-KEY": "YOUR-CUSTOM-ATTRIBUTE-VALUE"]
  
  // 2 
  let remoteStorage = RemoteStorage(storageType: .suite)
  
  // 3 
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) as? [[String: Any]] {
    pendingAttributes.append(contentsOf: [customAttributeDictionary])
    remoteStorage.store(pendingAttributes, forKey: .pendingCustomAttributes)
  } else {
  // 4 
    remoteStorage.store([customAttributeDictionary], forKey: .pendingCustomAttributes)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
``` objc
- (void)saveCustomAttribute {
  // 1 
  NSDictionary<NSString *, id> *customAttributeDictionary = @{ @"YOUR-CUSTOM-ATTRIBUTE-KEY": @"YOUR-CUSTOM-ATTRIBUTE-VALUE" };
  
  // 2  
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingAttributes = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomAttributes] mutableCopy];
  
  // 3
  if (pendingAttributes) {
    [pendingAttributes addObject:customAttributeDictionary];
    [remoteStorage store:pendingAttributes forKey:RemoteStorageKeyPendingCustomAttributes];
  } else {
  // 4 
    [remoteStorage store:@[ customAttributeDictionary ] forKey:RemoteStorageKeyPendingCustomAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

##### Senden von benutzerdefinierten Attributen an Braze

Der beste Zeitpunkt, um gespeicherte Analytics von einer App-Erweiterung für Benachrichtigungsinhalte zu protokollieren, ist direkt nach der Initialisierung des SDK. Dazu durchlaufen Sie die ausstehenden Attribute, setzen das entsprechende angepasste Attribut in Braze und löschen dann den Speicher für das nächste Mal, wenn diese Funktion benötigt wird.

1. Schleife durch das Array der ausstehenden Attribute
2. Jedes Schlüssel-Wert-Paar im Wörterbuch `pendingAttributes` mit einer Schleife durchlaufen
3. Individuelle angepasste Attribute mit entsprechendem Schlüssel und Wert protokollieren
4. Alle ausstehenden Attribute aus dem Speicher entfernen

{% subtabs global %}
{% subtab Swift %}
``` swift 
func logPendingCustomAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) as? [[String: Any]] else { return }
     
  // 1
  pendingAttributes.forEach { setCustomAttributesWith(keysAndValues: $0) }
  
  // 4 
  remoteStorage.removeObject(forKey: .pendingCustomAttributes)
}
   
func setCustomAttributesWith(keysAndValues: [String: Any]) {
  // 2 
  for (key, value) in keysAndValues {
  // 3
    if let value = value as? [String] {
      setCustomAttributeArrayWithKey(key, andValue: value)
    } else {
      setCustomAttributeWithKey(key, andValue: value)
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingCustomAttributesIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingAttributes = [remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomAttributes];
   
  // 1
  for (NSDictionary<NSString*, id> *attribute in pendingAttributes) {
    [self setCustomAttributeWith:attribute];
  }

  // 4 
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingCustomAttributes];
}
 
- (void)setCustomAttributeWith:(NSDictionary<NSString *, id> *)keysAndValues {
  // 2
  for (NSString *key in keysAndValues) {
  // 3 
    [self setCustomAttributeWith:key andValue:[keysAndValues objectForKey:key]];
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Benutzerattribute %}

##### Speichern von Benutzerattributen

Beim Speichern von Nutzerattributen empfehlen wir, ein angepasstes Objekt zu erstellen, um zu entschlüsseln, welche Art von Attribut aktualisiert wird (`email`, `first_name`, `phone_number` usw.). Das Objekt sollte mit der Speicherung/Abrufung von `UserDefaults` kompatibel sein. In der Hilfsdatei `UserAttribute` finden Sie ein Beispiel dafür, wie Sie dies bewerkstelligen können.

1. Initialisieren Sie ein kodiertes `UserAttribute` Objekt mit dem entsprechenden Typ
2. Initialisieren Sie `userDefaults`, um die Event-Daten abzurufen und zu speichern.
3. Wenn es ein bestehendes Array gibt: Fügen Sie die neuen Daten an das bestehende Array an und speichern Sie.
4. Wenn es kein bestehendes Array gibt: Speichern Sie das neue Array in `userDefaults`.

{% subtabs global %}
{% subtab Swift %}
``` swift 
func saveUserAttribute() {
  // 1 
  guard let data = try? PropertyListEncoder().encode(UserAttribute.userAttributeType("USER-ATTRIBUTE-VALUE")) else { return }
  
  // 2       
  let remoteStorage = RemoteStorage(storageType: .suite)
  
  // 3    
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) as? [Data] {
    pendingAttributes.append(contentsOf: [data])
    remoteStorage.store(pendingAttributes, forKey: .pendingUserAttributes)
  } else {
  // 4 
    remoteStorage.store([data], forKey: .pendingUserAttributes)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)saveUserAttribute {
  // 1 
  UserAttribute *userAttribute = [[UserAttribute alloc] initWithUserField:@"USER-ATTRIBUTE-VALUE" attributeType:UserAttributeTypeEmail];
   
  NSError *error;
  NSData *data = [NSKeyedArchiver archivedDataWithRootObject:userAttribute requiringSecureCoding:YES error:&error];

  if (error != nil) {
    // log error
  }
  // 2  
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingAttributes = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingUserAttributes] mutableCopy];
  
  // 3 
  if (pendingAttributes) {
    [pendingAttributes addObject:data];
    [remoteStorage store:pendingAttributes forKey:RemoteStorageKeyPendingUserAttributes];
  } else {
  // 4 
    [remoteStorage store:@[data] forKey:RemoteStorageKeyPendingUserAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

##### Senden von Benutzerattributen an Braze

Der beste Zeitpunkt, um gespeicherte Analytics von einer App-Erweiterung für Benachrichtigungsinhalte zu protokollieren, ist direkt nach der Initialisierung des SDK. Dazu durchlaufen Sie die ausstehenden Attribute, setzen das entsprechende angepasste Attribut in Braze und löschen dann den Speicher für das nächste Mal, wenn diese Funktion benötigt wird.

1. Array der Daten von `pendingAttributes` mit einer Schleife durchlaufen
2. Initialisieren Sie ein verschlüsseltes `UserAttribute` Objekt aus Attributdaten
3. Bestimmtes Benutzerfeld basierend auf dem Typ des Benutzerattributs (E-Mail) festlegen
4. Alle ausstehenden Benutzerattribute aus dem Speicher entfernen

{% subtabs global %}
{% subtab Swift %}
``` swift 
func logPendingUserAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) as? [Data] else { return }
  
  // 1    
  for attributeData in pendingAttributes {
  // 2 
    guard let userAttribute = try? PropertyListDecoder().decode(UserAttribute.self, from: attributeData) else { continue }
    
  // 3    
    switch userAttribute {
    case .email(let email):
      user?.email = email
    }
  }
  // 4   
  remoteStorage.removeObject(forKey: .pendingUserAttributes)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingUserAttributesIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingAttributes = [remoteStorage retrieveForKey:RemoteStorageKeyPendingUserAttributes];
  
  // 1  
  for (NSData *attributeData in pendingAttributes) {
    NSError *error;
  
  // 2 
    UserAttribute *userAttribute = [NSKeyedUnarchiver unarchivedObjectOfClass:[UserAttribute class] fromData:attributeData error:&error];

    if (error != nil) {
      // log error
    }
    
  // 3  
    if (userAttribute) {
      switch (userAttribute.attributeType) {
        case UserAttributeTypeEmail:
          [self user].email = userAttribute.userField;
          break;
      }
    }
  }
  // 4 
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingUserAttributes];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Hilfsdateien %}

##### Hilfsdateien

{% details Hilfsdatei "RemoteStorage" %}
{% subtabs global %}
{% subtab Swift %}
```swift
enum RemoteStorageKey: String, CaseIterable {
   
  // MARK: - Notification Content Extension Analytics
  case pendingCustomEvents = "pending_custom_events"
  case pendingCustomAttributes = "pending_custom_attributes"
  case pendingUserAttributes = "pending_user_attributes"
}
 
enum RemoteStorageType {
  case standard
  case suite
}
 
class RemoteStorage: NSObject {
  private var storageType: RemoteStorageType = .standard
  private lazy var defaults: UserDefaults = {
    switch storageType {
    case .standard:
      return .standard
    case .suite:
      return UserDefaults(suiteName: "YOUR-DOMAIN-IDENTIFIER")!
    }
  }()
   
  init(storageType: RemoteStorageType = .standard) {
    self.storageType = storageType
  }
   
  func store(_ value: Any, forKey key: RemoteStorageKey) {
    defaults.set(value, forKey: key.rawValue)
  }
   
  func retrieve(forKey key: RemoteStorageKey) -> Any? {
    return defaults.object(forKey: key.rawValue)
  }
   
  func removeObject(forKey key: RemoteStorageKey) {
    defaults.removeObject(forKey: key.rawValue)
  }
   
  func resetStorageKeys() {
    for key in RemoteStorageKey.allCases {
      defaults.removeObject(forKey: key.rawValue)
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@interface RemoteStorage ()
 
@property (nonatomic) StorageType storageType;
@property (nonatomic, strong) NSUserDefaults *defaults;
 
@end
 
@implementation RemoteStorage
 
- (id)initWithStorageType:(StorageType)storageType {
  if (self = [super init]) {
    self.storageType = storageType;
  }
  return self;
}
 
- (void)store:(id)value forKey:(RemoteStorageKey)key {
  [[self defaults] setValue:value forKey:[self rawValueForKey:key]];
}
 
- (id)retrieveForKey:(RemoteStorageKey)key {
  return [[self defaults] objectForKey:[self rawValueForKey:key]];
}
 
- (void)removeObjectForKey:(RemoteStorageKey)key {
  [[self defaults] removeObjectForKey:[self rawValueForKey:key]];
}
 
- (void)resetStorageKeys {
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingCustomEvents]];
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingCustomAttributes]];
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingUserAttributes]];
}
 
- (NSUserDefaults *)defaults {
  if (!self.defaults) {
    switch (self.storageType) {
      case StorageTypeStandard:
        return [NSUserDefaults standardUserDefaults];
        break;
      case StorageTypeSuite:
        return [[NSUserDefaults alloc] initWithSuiteName:@"YOUR-DOMAIN-IDENTIFIER"];
    }
  } else {
    return self.defaults;
  }
}
 
- (NSString*)rawValueForKey:(RemoteStorageKey)remoteStorageKey {
    switch(remoteStorageKey) {
    case RemoteStorageKeyPendingCustomEvents:
      return @"pending_custom_events";
    case RemoteStorageKeyPendingCustomAttributes:
      return @"pending_custom_attributes";
    case RemoteStorageKeyPendingUserAttributes:
      return @"pending_user_attributes";
    default:
      [NSException raise:NSGenericException format:@"Unexpected FormatType."];
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
{% details Hilfsdatei "UserAttribute" %}
{% subtabs global %}
{% subtab Swift %}
```swift
enum UserAttribute: Hashable {
  case email(String?)
}
 
// MARK: - Codable
extension UserAttribute: Codable {
  private enum CodingKeys: String, CodingKey {
    case email
  }
   
  func encode(to encoder: Encoder) throws {
    var values = encoder.container(keyedBy: CodingKeys.self)
     
    switch self {
    case .email(let email):
      try values.encode(email, forKey: .email)
    }
  }
   
  init(from decoder: Decoder) throws {
    let values = try decoder.container(keyedBy: CodingKeys.self)
     
    let email = try values.decode(String.self, forKey: .email)
    self = .email(email)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation UserAttribute
 
- (id)initWithUserField:(NSString *)userField attributeType:(UserAttributeType)attributeType {
  if (self = [super init]) {
    self.userField = userField;
    self.attributeType = attributeType;
  }
  return self;
}
 
- (void)encodeWithCoder:(NSCoder *)encoder {
  [encoder encodeObject:self.userField forKey:@"userField"];
  [encoder encodeInteger:self.attributeType forKey:@"attributeType"];
}
 
- (id)initWithCoder:(NSCoder *)decoder {
  if (self = [super init]) {
    self.userField = [decoder decodeObjectForKey:@"userField"];
     
    NSInteger attributeRawValue = [decoder decodeIntegerForKey:@"attributeType"];
    self.attributeType = (UserAttributeType) attributeRawValue;
  }
  return self;
}
 
@end
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
{% details Hilfedatei "EventName Dictionary" %}
{% subtabs global %}
{% subtab Swift %}
```swift
extension Dictionary where Key == String, Value == Any {
  init(eventName: String, properties: [String: Any]? = nil) {
    self.init()
    self[PushNotificationKey.eventName.rawValue] = eventName
     
    if let properties = properties {
      for (key, value) in properties {
        self[key] = value
      }
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation NSDictionary (Helper)
 
- (id)initWithEventName:(NSString *)eventName properties:(NSDictionary *)properties {
  self = [self init];
  if (self) {
    dict[@"event_name"] = eventName;
     
    for(id key in properties) {
      dict[key] = properties[key];
    }
  }
  return self;
}
 
@end
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
<br>
{% endtab %}
{% endtabs %}

