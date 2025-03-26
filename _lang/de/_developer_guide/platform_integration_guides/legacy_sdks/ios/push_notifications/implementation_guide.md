---
nav_title: Erweiterte Implementierung (optional)
article_title: Erweiterte Implementierung von Push-Benachrichtigungen für iOS (optional)
platform: iOS
page_order: 28
description: "Dieser Leitfaden für die erweiterte Implementierung beschreibt, wie Sie die App-Erweiterungen für iOS-Push-Benachrichtigungen nutzen können, um den größtmöglichen Erfolg mit Ihren Push-Nachrichten zu erzielen. Außerdem enthalten sind drei von unserem Team erstellte Anwendungsfälle, begleitende Codeschnipsel und eine Anleitung zur Protokollierung von Analysen."
channel:
  - push
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

<br>
{% alert important %}
Suchen Sie nach dem Leitfaden für die Integration von Push-Benachrichtigungen für Entwickler? Sie finden es [hier]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/).
{% endalert %}

# Leitfaden zur Implementierung von Push-Benachrichtigungen

> Dieser Leitfaden für die optionale erweiterte Implementierung beschreibt, wie Sie die App-Erweiterungen für Push-Benachrichtigungen nutzen können, um den größtmöglichen Erfolg mit Ihren Push-Nachrichten zu erzielen. Er enthält drei von unserem Team angepasste Anwendungsfälle, begleitende Code-Snippets und eine Anleitung zur Protokollierung von Analytics. Besuchen Sie unser Braze Demo Repository [hier](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Beachten Sie, dass sich dieser Implementierungsleitfaden auf eine Swift-Implementierung konzentriert. Für Interessierte werden jedoch Objective-C-Snippets bereitgestellt.

## App-Erweiterungen für Benachrichtigungsinhalte

![Zwei nebeneinander angezeigte Push-Nachrichten. Die Nachricht auf der rechten Seite zeigt, wie ein Push mit der Standard-Benutzeroberfläche aussieht. Die Nachricht auf der rechten Seite zeigt einen Push für eine Bonus-Kaffeekarte, der durch Implementieren einer angepassten Push-UI erstellt wurde.]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

Push-Benachrichtigungen scheinen zwar auf verschiedenen Plattformen Standard zu sein, bieten jedoch immense Anpassungsmöglichkeiten, die über das hinausgehen, was normalerweise in der Standard-Benutzeroberfläche implementiert ist. Wenn eine Push-Benachrichtigung erweitert wird, ermöglichen Inhaltsbenachrichtigungserweiterungen eine benutzerdefinierte Ansicht der erweiterten Push-Benachrichtigung. 

Push-Benachrichtigungen können auf drei verschiedene Arten erweitert werden: <br>\- Langes Drücken auf den Push-Banner<br>\- Wischen Sie auf dem Push-Banner nach unten<br>\- Durch Wischen des Banners nach links und Auswählen von "Anzeigen" 

Diese benutzerdefinierten Ansichten bieten intelligente Möglichkeiten, Kunden einzubinden. Sie können viele verschiedene Arten von Inhalten anzeigen, z. B. interaktive Benachrichtigungen, mit Benutzerdaten gefüllte Benachrichtigungen und sogar Push-Nachrichten, die Informationen wie Telefonnummern und E-Mail erfassen können. Auch wenn die Implementierung von Push auf diese Weise für einige ungewohnt sein mag, ist eine unserer bekannten Funktionen bei Braze, [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), ein Paradebeispiel dafür, wie eine benutzerdefinierte Ansicht für eine App-Erweiterung mit Benachrichtigungsinhalten aussehen kann!

#### Anforderungen
![]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) erfolgreich in Ihre App integriert
- iOS 10 oder höher
- Die folgenden Dateien werden von Xcode auf der Grundlage Ihrer Programmiersprache generiert:

Schnell<br>
- `NotificationViewController.swift`<br>
- `MainInterface.storyboard`<br><br>
Objective-C<br>
- `NotificationViewController.h`<br>
- `NotificationViewController.m`<br>
- `MainInterface.storyboard`

### Benutzerdefinierte Kategoriekonfiguration

Um eine benutzerdefinierte Ansicht im Dashboard einzurichten, müssen Sie die Benachrichtigungsschaltflächen einschalten und Ihre benutzerdefinierte Kategorie eingeben. Die von Ihnen angegebene vorregistrierte benutzerdefinierte iOS-Kategorie wird dann mit der `UNNotificationExtensionCategory` in der `.plist` Ihres Ziels für die Erweiterung für Benachrichtigungsinhalte abgeglichen. Der hier angegebene Wert muss mit den Einstellungen im Braze Dashboard übereinstimmen.

![Optionen für den Benachrichtigungs-Button in den Einstellungen des Editors für Push-Nachrichten]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

{% alert tip %}
Da Push-Benachrichtigungen mit Inhaltserweiterungen nicht immer komplett zu sehen sind, empfiehlt es sich, eine Handlungsaufforderung einzufügen, um die Nutzer:innen zu veranlassen, die Push-Benachrichtigungen zu erweitern.
{% endalert %}

## Anwendungsfall und Implementierungsanleitung

Es gibt drei Arten von Erweiterungen für Push-Benachrichtigungsinhalte. Für jeden Typ gibt es eine Anleitung zum Konzept, mögliche Anwendungsfälle und einen Blick darauf, wie Variablen für Push-Benachrichtigungen im Braze-Dashboard aussehen und verwendet werden können:
- [Interaktive Push-Benachrichtigung](#interactive-push-notification)
- [Personalisierte Push-Benachrichtigungen](#personalized-push-notifications)
- [Push-Benachrichtigungen zur Informationserfassung](#information-capture-push-notification)

### Interaktive Push-Benachrichtigung

Push-Benachrichtigungen können auf Benutzeraktionen innerhalb einer Inhaltserweiterung reagieren. Für Benutzer mit iOS 12 oder höher bedeutet dies, dass Sie Ihre Push-Nachrichten in vollständig interaktive Push-Benachrichtigungen verwandeln können! Diese Interaktivität bietet viele Möglichkeiten, um Ihre Nutzer zur Interaktion mit Ihren Benachrichtigungen zu veranlassen. Das folgende Beispiel zeigt einen Push, bei dem die Nutzer in der erweiterten Benachrichtigung ein Spiel spielen können.

![Diagramm, wie die Phasen einer interaktiven Push-Benachrichtigung aussehen könnten. Die Abbildungen zeigen einen Nutzer, der auf eine Push-Benachrichtigung drückt, die ein interaktives Spiel anzeigt.]({% image_buster /assets/img/push_implementation_guide/push12.png %}){: style="border:0"}

#### Dashboard Konfiguration

Um eine benutzerdefinierte Ansicht im Dashboard einzurichten, geben Sie in den Einstellungen der Benachrichtigungsschaltfläche die spezifische Kategorie ein, die Sie anzeigen möchten. Als nächstes müssen Sie in der `.plist` Ihrer Erweiterung für Benachrichtigungsinhalte auch die benutzerdefinierte Kategorie auf das Attribut `UNNotificationExtensionCategory` setzen. Der hier angegebene Wert muss mit den Einstellungen im Braze Dashboard übereinstimmen. Um Nutzerinteraktionen mit einer Push-Benachrichtigung zu aktivieren, setzen Sie den Schlüssel `UNNotificationExtensionInteractionEnabled` auf true.

![]({% image_buster /assets/img/push_implementation_guide/push3.png %}){: style="float:right;max-width:45%;"}

![Optionen für den Benachrichtigungs-Button in den Einstellungen des Editors für Push-Nachrichten]({% image_buster /assets/img/push_implementation_guide/push14.png %}){: style="max-width:50%;"}

#### Andere Anwendungsfälle
Push-Inhaltserweiterungen sind eine spannende Option, um Werbeaktionen und Anwendungen interaktiv zu gestalten. Beispiele hierfür sind ein Spiel, für die Nutzer spielen können, ein Glücksrad für Rabatte oder ein "Gefällt mir"-Button für ein Listing oder einen Song.

##### Sind Sie bereit für die Protokollierung von Analysen?
Im [folgenden Abschnitt](#logging-analytics) wird näher beschrieben, wie der Datenfluss aussehen sollte.

### Personalisierte Push-Benachrichtigungen
![Zwei iPhones werden nebeneinander angezeigt. Das erste iPhone zeigt die ungekürzte Ansicht der Push-Nachricht. Das zweite iPhone zeigt die erweiterte Version der Push-Nachricht mit einer "Fortschrittsanzeige", die angibt, wie weit sie in einem Kurs sind, wann die nächste Sitzung stattfindet und bis wann die nächste Sitzungs-ID fällig ist.]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

Push-Benachrichtigungen können benutzerspezifische Informationen innerhalb einer Inhaltserweiterung anzeigen. Das Beispiel auf der rechten Seite zeigt eine Push-Benachrichtigung, nachdem ein Benutzer eine bestimmte Aufgabe (Braze Learning-Kurs) abgeschlossen hat und nun aufgefordert wird, diese Benachrichtigung zu erweitern, um seinen Fortschritt zu überprüfen. Die hier bereitgestellten Informationen sind benutzerspezifisch und können über einen API-Auslöser abgefeuert werden, wenn eine Sitzung abgeschlossen ist oder eine bestimmte Benutzeraktion durchgeführt wird. 

#### Dashboard Konfiguration

Um einen personalisierten Push im Dashboard einzurichten, müssen Sie die spezifische Kategorie registrieren, die angezeigt werden soll, und dann innerhalb der Schlüssel-Wert-Paare mit Hilfe von Standard-Liquid die entsprechenden Benutzerattribute einstellen, die in der Nachricht angezeigt werden sollen. Diese Ansichten können auf der Grundlage bestimmter Benutzerattribute eines bestimmten Benutzerprofils personalisiert werden.

![Vier Sätze von Schlüssel-Wert-Paaren, wobei "next_session_name" und "next_session_complete_date" als API-getriggerte Eigenschaft mit Liquid und "completed_session count" und "total_session_count" als angepasstes Nutzerattribut mit Liquid festgelegt werden.]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

#### Umgang mit Schlüssel-Wert-Paaren

Die folgende Methode `didReceive` wird aufgerufen, wenn die Inhaltserweiterung eine Benachrichtigung erhalten hat. Sie befindet sich in `NotificationViewController`. Die im Dashboard bereitgestellten Schlüssel-Wert-Paare werden im Code durch die Verwendung eines Wörterbuchs des Typs `userInfo` dargestellt.

**Analysieren von Schlüssel-Werte-Paaren aus Push-Benachrichtigungen**<br>

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

#### Andere Anwendungsfälle

Es gibt unendlich viele Möglichkeiten für fortschrittsbasierte und nutzerorientierte Push-Inhaltserweiterungen. Einige Beispiele: Eine Option zum Teilen des Fortschritts auf verschiedenen Plattformen, eine Option zum Freischalten von Errungenschaften, Bonuskarten oder sogar Onboarding-Checklisten. 

##### Sind Sie bereit für die Protokollierung von Analysen?
Im [folgenden Abschnitt](#logging-analytics) wird näher beschrieben, wie der Datenfluss aussehen sollte.

### Push-Benachrichtigung zur Informationserfassung

Push-Benachrichtigungen können Nutzerinformationen in einer Inhaltserweiterung erfassen, wodurch sich Ihnen völlig neue Möglichkeiten für Push-Benachrichtigungen eröffnen. Der folgende Ablauf zeigt, dass die Ansicht auf Statusänderungen reagieren kann. Diese Komponenten der Zustandsänderung werden in jedem Bild dargestellt. 

1. Der Benutzer erhält eine Push-Benachrichtigung.
2. Push wird geöffnet und fordert Informationen vom Nutzer an.
3. Die Informationen werden eingegeben und wenn sie gültig sind, wird der Button "Registrieren" angezeigt.
3. Es wird eine Bestätigungsansicht angezeigt und der Push wird ausgeblendet. 

![]({% image_buster /assets/img/push_implementation_guide/push8.png %}){: style="border:0;"}

Beachten Sie, dass es sich bei den hier angeforderten Informationen um eine Vielzahl von Dingen handeln kann, wie z.B. die Erfassung von SMS-Nummern, sie müssen nicht unbedingt auf E-Mails bezogen sein.

#### Dashboard Konfiguration

Um einen Push für die Informationserfassung im Dashboard einzurichten, müssen Sie Ihre benutzerdefinierte Kategorie registrieren und einstellen und die benötigten Schlüssel-Wert-Paare bereitstellen. Wie im Beispiel gezeigt, können Sie auch ein Bild in Ihren Push einfügen. Dazu müssen Sie [Rich Notifications]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/rich_notifications/) integrieren, den Benachrichtigungsstil in Ihrer Kampagne auf Rich Notification einstellen und ein Rich-Push-Bild einfügen.

![Eine Push-Nachricht mit drei Gruppen von Schlüssel-Wert-Paaren. 1\. "Braze_id" als Liquid-Aufruf zum Abrufen der Braze-ID eingestellt. 2\. "cert_title" als "Braze Marketer Certification" festgelegt. 3\. "Cert_description" ist auf "Certified Braze marketers drive..." festgelegt.]({% image_buster /assets/img/push_implementation_guide/push9.png %})

#### Verarbeitung von Button-Aktionen

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

##### Ausblenden von Pushes

Push-Benachrichtigungen können durch Drücken eines Aktions-Buttons automatisch ausgeblendet werden. Es gibt drei vorgefertigte Optionen für Push-Ausblendungen, die empfohlen werden:

1. `completion(.dismiss)` - Weist die Benachrichtigung zurück
2. `completion(.doNotDismiss)` - Benachrichtigung bleibt offen
3. `completion(.dismissAndForward)` - Push wird abgebrochen und der Benutzer wird in die Anwendung weitergeleitet.

#### Andere Anwendungsfälle

Das Anfordern von Nutzereingaben über Push-Benachrichtigungen ist eine spannende Möglichkeit, die viele Unternehmen nicht nutzen. In diesen Push-Nachrichten können Sie nicht nur grundlegende Informationen wie Name, E-Mail oder Telefonnummer abfragen, sondern Sie können die Benutzer auch auffordern, ein Benutzerprofil zu vervollständigen, falls es noch nicht abgeschlossen ist, oder sogar Feedback zu übermitteln. 

##### Sind Sie bereit für die Protokollierung von Analysen?
Im [folgenden Abschnitt](#logging-analytics) wird näher beschrieben, wie der Datenfluss aussehen sollte. 

## Protokollieren von Analytics

### Protokollierung mit der Braze API (empfohlen)

Das Protokollieren von Analytics kann nur in Echtzeit erfolgen, wenn der Server des Kunden auf unseren [Endpunkt `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) trifft. Zum Protokollieren von Analytics übermitteln Sie den Wert `braze_id` in das Feld Schlüssel-Wert-Paare (siehe folgenden Screenshot), um das zu aktualisierende Nutzerprofil zu identifizieren.

![Eine Push-Nachricht mit drei Gruppen von Schlüssel-Wert-Paaren. 1\. "Braze_id" als Liquid-Aufruf zum Abrufen der Braze-ID eingestellt. 2\. "cert_title" als "Braze Marketer Certification" festgelegt. 3\. "Cert_description" ist auf "Certified Braze marketers drive..." festgelegt.]({% image_buster /assets/img/push_implementation_guide/push18.png %}){: style="max-width:80%;"}

### Manuelles Protokollieren

Für die manuelle Protokollierung müssen Sie zunächst App-Gruppen in Xcode konfigurieren und anschließend Analytics erstellen, speichern und abrufen. Hierfür sind einige angepasste Entwicklungsarbeiten auf Ihrer Seite erforderlich. Die folgenden Codeschnipsel helfen Ihnen bei der Lösung dieses Problems. 

Ein weiterer wichtiger Punkt, den es zu beachten gilt, ist, dass Analytics erst dann an Braze gesendet werden, wenn die mobile Anwendung anschließend gestartet wird. Das bedeutet, dass je nach Ihren Einstellungen für die Beendigung oft eine unbestimmte Zeitspanne zwischen der Beendigung einer Push-Benachrichtigung und dem Start der mobilen App und dem Abrufen der Analysen vergeht. Auch wenn dieser Zeitpuffer möglicherweise nicht alle Anwendungsfälle betrifft, sollten Nutzer die Auswirkungen bedenken und ggf. die Nutzer-Journey so anpassen, dass sie die Öffnung der Anwendung beinhaltet. 

![Grafik, die die Verarbeitung von Analytics in Braze beschreibt. 1\. Es werden Analysedaten erstellt. 2\. Die Analysedaten werden gespeichert. 3\. Die Push-Benachrichtigung wird abgelehnt. 4\. Unbestimmte Zeitspanne zwischen der Ablehnung der Push-Benachrichtigung und dem Start der mobilen App. 5\. Die mobile App wird gestartet. 6\. Analysedaten werden empfangen. 7\. Die Analysedaten werden an Braze gesendet.]({% image_buster /assets/img/push_implementation_guide/push13.png %})

#### Schritt 1: Konfigurieren Sie App-Gruppen in Xcode
Fügen Sie eine Fähigkeit `App Groups` hinzu. Wenn Sie noch keine App-Gruppe in Ihrer App hatten, navigieren Sie zur Funktion der Hauptzielgruppe Ihrer App, aktivieren Sie `App Groups` und klicken Sie auf das Pluszeichen (+). Verwenden Sie die Bundle-ID Ihrer App, um die App-Gruppe zu erstellen. Wenn die Bundle-ID Ihrer App beispielsweise `com.company.appname` lautet, können Sie die App-Gruppe `group.com.company.appname.xyz` nennen. Vergewissern Sie sich, dass `App Groups` sowohl für die Hauptzielgruppe Ihrer App als auch für die Zielgruppe der Inhaltserweiterung aktiviert ist.

![]({% image_buster /assets/img/ios/push_story/add_app_groups.png %})

#### Schritt 2: Code-Snippets integrieren
Die folgenden Code-Snippets sind eine hilfreiche Referenz, wie Sie angepasste Events, angepasste Attribute und Nutzerattribute speichern und senden können. In dieser Anleitung wird von UserDefaults gesprochen. Die Codedarstellung erfolgt jedoch in Form der Hilfedatei `RemoteStorage`. Darüber hinaus gibt es die Hilfedateien `UserAttributes` und `EventName Dictionary`, die beim Senden und Speichern von Nutzerattributen verwendet werden. Alle Hilfedateien sind am Ende dieser Anleitung aufgeführt.

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

Nach der Initialisierung des SDK ist der beste Zeitpunkt, um alle gespeicherten Analytics von einer App-Erweiterung für Benachrichtigungsinhalte zu protokollieren. Dazu durchlaufen Sie alle ausstehenden Events, suchen nach dem Schlüssel "Ereignisname", setzen die entsprechenden Werte in Braze und löschen dann den Speicher für das nächste Mal, wenn diese Funktion benötigt wird.

1. Array der ausstehenden Events mit einer Schleife durchlaufen.
2. Jedes Schlüssel-Wert-Paar im Wörterbuch `pendingEvents` mit einer Schleife durchlaufen.
3. Schlüssel für "Ereignisname" expliziert überprüfen, um den Wert entsprechend festzulegen.
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
      logCustomEvent(eventName, withProperties: properties)
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
      [[Appboy sharednstance] logCustomEvent:eventName withProperties:properties];
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

Nach der Initialisierung des SDK ist der beste Zeitpunkt, um alle gespeicherten Analytics von einer App-Erweiterung für Benachrichtigungsinhalte zu protokollieren. Dazu durchlaufen Sie die ausstehenden Attribute, setzen das entsprechende angepasste Attribut in Braze und löschen dann den Speicher für das nächste Mal, wenn diese Funktion benötigt wird.

1. Schleife durch das Array der ausstehenden Attribute
2. Jedes Schlüssel-Wert-Paar im Wörterbuch `pendingAttributes` mit einer Schleife durchlaufen.
3. Individuelles benutzerdefiniertes Attribut mit entsprechendem Schlüssel und Wert protokollieren
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

Beim Speichern von Nutzerattributen empfiehlt es sich, ein angepasstes Objekt zu erstellen, um festzustellen, welche Art von Attribut aktualisiert wird (`email`, `first_name`, `phone_number` usw.). Das Objekt sollte mit der Speicherung/Abrufung von `UserDefaults` kompatibel sein. In der Hilfedatei `UserAttribute` finden Sie ein Beispiel dafür, wie Sie dies bewerkstelligen können.

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

Nach der Initialisierung des SDK ist der beste Zeitpunkt, um alle gespeicherten Analytics von einer App-Erweiterung für Benachrichtigungsinhalte zu protokollieren. Dazu durchlaufen Sie die ausstehenden Attribute, setzen das entsprechende angepasste Attribut in Braze und löschen dann den Speicher für das nächste Mal, wenn diese Funktion benötigt wird.

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
{% tab Hilfedateien %}

##### Hilfsdateien

{% details Hilfedatei "RemoteStorage" %}
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
{% details Hilfedatei "UserAttribute" %}
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

