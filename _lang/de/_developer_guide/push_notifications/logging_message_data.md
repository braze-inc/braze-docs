---
nav_title: Push-Analytics und Protokollierung angepasster Events
article_title: Push-Analytics und Protokollierung angepasster Events
page_order: 7.2
description: "Erfahren Sie, welche Push-Analytics Braze automatisch protokolliert, wie Sie natives Tracking bei angepasster Push-Verarbeitung beibehalten und wie Sie angepasste Events oder Attribute aus Push-Payload-Daten protokollieren."
noindex: true
---

# Push-Analytics und Protokollierung angepasster Events

> Diese Seite behandelt die folgenden Workflows: native Push-Analytics (Öffnungen, beeinflusste Öffnungen und Kampagnen-Reporting) sowie die Protokollierung angepasster Daten (angepasste Events und Attribute) aus Push-Payloads. Nutzen Sie diesen Leitfaden, um festzustellen, welcher Workflow für Ihren Anwendungsfall gilt, und folgen Sie den Schritten für Ihre Plattform.

## Voraussetzungen

Bevor Sie beginnen, schließen Sie die initiale Push-Benachrichtigungs-Integration für Ihre Plattform ab:

- [Android-Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)
- [Swift-Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Web-Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## Native Push-Analytics vs. Protokollierung angepasster Events

Die folgenden Workflows haben jeweils unterschiedliche Reporting-Oberflächen.

| Analytics-Kategorie | Beschreibung | Wo sie angezeigt wird |
| --- | --- | --- |
| Native Push-Analytics | Push-Metriken wie Öffnungen und beeinflusste Öffnungen, die mit Braze-Push-Kampagnen verknüpft sind | Push-Kampagnen-Analytics, Currents-Nachrichten-Engagement-Events, Berichts-Builder |
| Angepasste Events und Attribute | Analytics, die Sie definieren und über SDK-Methoden oder den `/users/track`-Endpunkt protokollieren | Nutzerprofile, Segmentierung, aktionsbasierte Kampagnen und Canvase, Analytics für angepasste Events |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Das Protokollieren eines angepassten Events (z. B. `push_notification_opened`) ist nicht dasselbe wie das native Braze-Push-Öffnungs-Tracking. Angepasste Events füllen keine nativen Push-Kampagnen-Öffnungsmetriken oder Push-Attribution.
{% endalert %}

## Was Braze automatisch protokolliert

Wenn Ihre SDK-Integration konfiguriert ist, protokolliert Braze automatisch grundlegende Kanal-Interaktionsdaten, einschließlich Push-Öffnungen und beeinflusster Öffnungen. Für Standard-Push-Analytics ist kein zusätzlicher Code erforderlich. Eine vollständige Liste der automatisch erfassten Daten finden Sie unter [SDK-Datenerfassung]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/).

Weitere Details finden Sie hier:

- [SDK-Datenerfassung]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/) für eine vollständige Liste automatisch erfasster und optionaler Daten.
- [Beeinflusste Öffnungen]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/) für Informationen darüber, wie Braze beeinflusste Öffnungen berechnet.
- [Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) für nachgelagerte Event-Schemas in Currents.

## Native Push-Analytics bei angepasster Push-Verarbeitung beibehalten

Sie verwenden möglicherweise einen angepassten Push-Handler, wenn Sie mehrere Push-Anbieter integrieren, zusätzliche Payload-Daten verarbeiten oder eine angepasste Logik für die Benachrichtigungsanzeige implementieren müssen. Wenn Sie einen angepassten Push-Handler verwenden, müssen Sie Push-Payloads dennoch an Braze-SDK-Methoden übergeben. Dadurch kann Braze die eingebetteten Tracking-Daten extrahieren und native Push-Analytics (Öffnungen, beeinflusste Öffnungen und Zustellungsmetriken) protokollieren.

{% tabs %}
{% tab Android %}

Wenn Sie einen angepassten `FirebaseMessagingService` haben, rufen Sie `BrazeFirebaseMessagingService.handleBrazeRemoteMessage(...)` innerhalb Ihrer `onMessageReceived`-Methode auf. Beachten Sie, dass Ihre `FirebaseMessagingService`-Unterklasse die Ausführung innerhalb von 9 Sekunden nach dem Aufruf abschließen muss, um nicht vom Android-System [markiert oder beendet](https://firebase.google.com/docs/cloud-messaging/android/receive) zu werden.

```java
public class MyFirebaseMessagingService extends FirebaseMessagingService {
  @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    super.onMessageReceived(remoteMessage);
    if (BrazeFirebaseMessagingService.handleBrazeRemoteMessage(this, remoteMessage)) {
      // Braze processed a Braze push payload.
    } else {
      // Non-Braze payload: pass to your other handlers.
    }
  }
}
```

Ein vollständiges Implementierungsbeispiel finden Sie in der [Braze Android SDK Firebase Push-Beispiel-App](https://github.com/braze-inc/braze-android-sdk/tree/master/samples/firebase-push).

{% endtab %}
{% tab Swift %}

Bei einer manuellen Push-Integration leiten Sie Hintergrund- und Nutzerbenachrichtigungs-Callbacks an Braze weiter.

**Hintergrund-Benachrichtigungen:**

```swift
if let braze = AppDelegate.braze, braze.notifications.handleBackgroundNotification(
  userInfo: userInfo,
  fetchCompletionHandler: completionHandler
) {
  return
}
completionHandler(.noData)
```

**Nutzerbenachrichtigungs-Antworten:**

```swift
if let braze = AppDelegate.braze, braze.notifications.handleUserNotification(
  response: response,
  withCompletionHandler: completionHandler
) {
  return
}
completionHandler()
```

**Vordergrund-Benachrichtigungen:**

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter,
  willPresent notification: UNNotification,
  withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void
) {
  if let braze = AppDelegate.braze {
    braze.notifications.handleForegroundNotification(notification: notification)
  }
  if #available(iOS 14.0, *) {
    completionHandler([.banner, .list, .sound])
  } else {
    completionHandler([.alert, .sound])
  }
}
```

Ein vollständiges Implementierungsbeispiel finden Sie im [Braze Swift SDK Manual Push-Beispiel (`AppDelegate.swift`)](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotifications-Manual/AppDelegate.swift).

{% endtab %}
{% tab Web %}

Für Web-Push konfigurieren Sie Ihren Service Worker und die SDK-Initialisierung wie unter [Web-Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) beschrieben.

Weitere Code-Beispiele finden Sie im [Braze Web SDK-Repository](https://github.com/braze-inc/braze-web-sdk).

{% endtab %}
{% endtabs %}

## Angepasste Daten aus Push-Payloads protokollieren

Verwenden Sie diesen Abschnitt, wenn Sie zusätzliche Daten aus Push-Payload-Schlüssel-Wert-Paaren protokollieren müssen, z. B. angepasste Events oder Attribute, die mit Ihrer Geschäftslogik verknüpft sind.

Weitere Informationen zu angepassten Events finden Sie unter [Angepasste Events]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/). Informationen zum Protokollieren angepasster Events über SDK-Methoden finden Sie unter [Angepasste Events protokollieren]({{site.baseurl}}/developer_guide/analytics/logging_events/).

### Option A: Protokollierung über den `/users/track`-Endpunkt

Sie können Analytics in Echtzeit protokollieren, indem Sie den [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)-Endpunkt aufrufen.

Um das Nutzerprofil zu identifizieren, fügen Sie `braze_id` in Ihre Push-Payload-Schlüssel-Wert-Paare ein.

{% alert note %}
Die Übergabe von `braze_id` identifiziert nur das Profil. Sie benötigen weiterhin Implementierungslogik, die Payload-Werte liest und die `/users/track`-Anfrage mit den Events oder Attributen sendet, die Sie protokollieren möchten.
{% endalert %}

### Option B: Protokollierung über SDK-Methoden nach dem App-Start

Sie können Payload-Daten auch lokal speichern und angepasste Events und Attribute über SDK-Methoden protokollieren, nachdem die App initialisiert wurde. Dieser Ansatz ist üblich in Notification Content Extension-Flows, bei denen Analytics-Daten zuerst persistiert und beim nächsten App-Start gesendet werden.

{% alert important %}
Analytics werden erst an Braze gesendet, wenn die App gestartet wird. Abhängig von Ihren Einstellungen zum Schließen kann es eine Verzögerung zwischen dem Zeitpunkt geben, an dem die Nutzer:innen die Benachrichtigung schließen, und dem Zeitpunkt, an dem die App öffnet und Analytics sendet.
{% endalert %}

## Protokollierung aus einer Notification Content Extension (Swift)

Die folgenden Schritte beschreiben, wie Sie angepasste Events, angepasste Attribute und Nutzerattribute aus einer Swift Notification Content Extension speichern und senden.

### 1. Schritt: App-Gruppen in Xcode konfigurieren

Fügen Sie in Xcode die `App Groups`-Fähigkeit zu Ihrem Haupt-App-Target hinzu. Aktivieren Sie **App Groups** und klicken Sie dann auf **+**, um eine neue Gruppe hinzuzufügen. Verwenden Sie die Bundle-ID Ihrer App, um den Gruppenbezeichner zu erstellen (z. B. `group.com.company.appname.xyz`). Aktivieren Sie **App Groups** sowohl für Ihr Haupt-App-Target als auch für das Content Extension-Target.

![Xcode zeigt die aktivierte App Groups-Fähigkeit für die Haupt-App und die Notification Extension]({% image_buster /assets/img/swift/push_story/add_app_groups.png %})

### 2. Schritt: Auswählen, was protokolliert werden soll

Bevor Sie die Snippets implementieren, wählen Sie aus, welche Analytics-Kategorie Sie protokollieren möchten:

- **Angepasste Events:** Aktionen, die Nutzer:innen ausführen (z. B. einen Flow abschließen oder auf ein bestimmtes UI-Element tippen). Verwenden Sie angepasste Events für aktionsbasierte Trigger, Segmentierung und Event-Analytics. Weitere Informationen finden Sie unter [Angepasste Events]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/) und [Angepasste Events protokollieren]({{site.baseurl}}/developer_guide/analytics/logging_events/).
- **Angepasste Attribute:** Profilfelder, die Sie definieren (z. B. `plan_tier` oder `preferred_language`) und im Laufe der Zeit aktualisieren. Weitere Informationen finden Sie unter [Angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/) und [Nutzerattribute festlegen]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/).
- **Nutzerattribute:** Standard-Profilfelder (z. B. E-Mail, Vorname und Telefonnummer). Im Beispielcode werden diese durch ein typisiertes `UserAttribute`-Modell dargestellt und dann auf Braze-Nutzerfelder abgebildet.

Die Hilfsdateien in diesem Abschnitt (`RemoteStorage`, `UserAttribute` und `EventName Dictionary`) sind lokale Hilfsdateien, die von dieser Beispielimplementierung verwendet werden. Sie sind keine integrierten SDK-Klassen. Sie speichern aus Payloads abgeleitete Daten in `UserDefaults`, definieren ein typisiertes Modell für ausstehende Nutzer-Updates und standardisieren die Event-Payload-Konstruktion. Weitere Informationen zum lokalen Datenspeicherverhalten finden Sie unter [Speicher]({{site.baseurl}}/developer_guide/storage/?tab=swift).

{% alert note %}
Die Beispiele für Hilfsdateien in diesem Abschnitt sind iOS-spezifisch (Swift und Objective-C). Für Android- und Web-Ansätze zur Protokollierung angepasster Events und Attribute siehe [Angepasste Events protokollieren]({{site.baseurl}}/developer_guide/analytics/logging_events/) ([Android]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)) und [Nutzerattribute festlegen]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/) ([Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=web)).
{% endalert %}

{% tabs local %}
{% tab Custom events %}

#### Angepasste Events speichern

Erstellen Sie den Analytics-Payload, indem Sie ein Dictionary aufbauen, Metadaten befüllen und es mit der Hilfsdatei speichern.

1. Initialisieren Sie ein Dictionary mit Event-Metadaten.
2. Initialisieren Sie `userDefaults`, um Event-Daten abzurufen und zu speichern.
3. Wenn ein vorhandenes Array gefunden wird, anhängen und speichern.
4. Wenn kein Array vorhanden ist, ein neues Array speichern.

{% subtabs global %}
{% subtab Swift %}
```swift
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
    [remoteStorage store:pendingEvents forKey:RemoteStorageKeyPendingCustomEvents];
  } else {
    // 4
    [remoteStorage store:@[ customEventDictionary ] forKey:RemoteStorageKeyPendingCustomEvents];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

#### Angepasste Events an Braze senden

Protokollieren Sie gespeicherte Analytics direkt nach der SDK-Initialisierung.

1. Durchlaufen Sie die ausstehenden Events.
2. Durchlaufen Sie die Schlüssel-Wert-Paare in jedem Event.
3. Prüfen Sie auf den `event_name`-Schlüssel.
4. Fügen Sie die verbleibenden Schlüssel-Wert-Paare zum `properties`-Dictionary hinzu.
5. Protokollieren Sie jedes angepasste Event.
6. Entfernen Sie ausstehende Events aus dem Speicher.

{% subtabs global %}
{% subtab Swift %}
```swift
func logPendingCustomEventsIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) as? [[String: Any]] else { return }
  
  // 1
  for event in pendingEvents {
    var eventName: String?
    var properties: [AnyHashable: Any] = [:]
    
    // 2
    for (key, value) in event {
      if key == "event_name" {
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
      AppDelegate.braze?.logCustomEvent(name: eventName, properties: properties)
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
{% tab Custom attributes %}

#### Angepasste Attribute speichern

Erstellen Sie das Analytics-Dictionary von Grund auf und persistieren Sie es.

1. Initialisieren Sie ein Dictionary mit Attribut-Metadaten.
2. Initialisieren Sie `userDefaults`, um Attributdaten abzurufen und zu speichern.
3. Wenn ein vorhandenes Array gefunden wird, anhängen und speichern.
4. Wenn kein Array vorhanden ist, ein neues Array speichern.

{% subtabs global %}
{% subtab Swift %}
```swift
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
```objc
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

#### Angepasste Attribute an Braze senden

Protokollieren Sie gespeicherte Analytics direkt nach der SDK-Initialisierung.

1. Durchlaufen Sie die ausstehenden Attribute.
2. Durchlaufen Sie jedes Schlüssel-Wert-Paar.
3. Protokollieren Sie jeden angepassten Attribut-Schlüssel und -Wert.
4. Entfernen Sie ausstehende Attribute aus dem Speicher.

{% subtabs global %}
{% subtab Swift %}
```swift
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
{% tab User attributes %}

#### Nutzerattribute speichern

Beim Speichern von Nutzerattributen erstellen Sie ein angepasstes Objekt, das erfasst, welches Nutzerfeld aktualisiert wird (`email`, `first_name`, `phone_number` usw.). Das Objekt sollte mit dem Speichern und Abrufen über `UserDefaults` kompatibel sein. Ein Beispiel finden Sie in der `UserAttribute`-Hilfsdatei im Tab **Hilfsdateien**.

1. Initialisieren Sie ein codiertes `UserAttribute`-Objekt mit dem entsprechenden Typ.
2. Initialisieren Sie `userDefaults`, um die Daten abzurufen und zu speichern.
3. Wenn ein vorhandenes Array gefunden wird, anhängen und speichern.
4. Wenn kein Array vorhanden ist, ein neues Array speichern.

{% subtabs global %}
{% subtab Swift %}
```swift
func saveUserAttribute() {
  // 1
  guard let data = try? PropertyListEncoder().encode(UserAttribute.email("USER-ATTRIBUTE-VALUE")) else { return }
  
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

#### Nutzerattribute an Braze senden

Protokollieren Sie gespeicherte Analytics direkt nach der SDK-Initialisierung.

1. Durchlaufen Sie die `pendingAttributes`-Daten.
2. Decodieren Sie jedes `UserAttribute`.
3. Setzen Sie Nutzerfelder basierend auf dem Attributtyp.
4. Entfernen Sie ausstehende Nutzerattribute aus dem Speicher.

{% subtabs global %}
{% subtab Swift %}
```swift
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
      AppDelegate.braze?.user.set(email: email)
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
{% tab Helper files %}

#### RemoteStorage-Hilfsdatei

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
      // Use the App Group identifier you created in Step 1.
      return UserDefaults(suiteName: "group.com.company.appname.xyz")!
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
  if (!_defaults) {
    switch (self.storageType) {
      case StorageTypeStandard:
        _defaults = [NSUserDefaults standardUserDefaults];
        break;
      case StorageTypeSuite:
        _defaults = [[NSUserDefaults alloc] initWithSuiteName:@"group.com.company.appname.xyz"];
        break;
    }
  }
  return _defaults;
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

#### UserAttribute-Hilfsdatei

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
      try values.encodeIfPresent(email, forKey: .email)
    }
  }
   
  init(from decoder: Decoder) throws {
    let values = try decoder.container(keyedBy: CodingKeys.self)
     
    let email = try values.decodeIfPresent(String.self, forKey: .email)
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

#### EventName-Dictionary-Hilfsdatei

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
@implementation NSMutableDictionary (Helper)

+ (instancetype)dictionaryWithEventName:(NSString *)eventName
                              properties:(NSDictionary *)properties {
  NSMutableDictionary *dict = [NSMutableDictionary dictionary];
  dict[@"event_name"] = eventName;

  if (properties) {
    for (id key in properties) {
      dict[key] = properties[key];
    }
  }

  return dict;
}
 
@end
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

## Ergebnisse analysieren

Verwenden Sie die Reporting-Oberfläche, die zur Analytics-Kategorie passt:

| Analytics-Kategorie | Wo Sie es in Braze einsehen können |
| --- | --- |
| Native Push-Analytics | Um Push-Öffnungsmetriken auf Kampagnenebene anzuzeigen, navigieren Sie zur Seite **Kampagnen-Analytics** Ihrer Push-Kampagne. Für Metrik-Definitionen siehe [Beeinflusste Öffnungen]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/). Um angepasste Analytics-Ansichten zu erstellen, navigieren Sie zu **Analytics** > **Berichts-Builder (Neu)**. Für Navigationsschritte siehe [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/). Für Event-Schemas auf Warehouse-Ebene siehe [Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/). |
| Angepasste Events und Attribute | Um Trends angepasster Events anzuzeigen, navigieren Sie zu **Analytics** > **Bericht für angepasste Events**. Weitere Details finden Sie unter [Angepasste Events]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/). Um Werte auf Nutzerebene zu prüfen, navigieren Sie zur Seite **Nutzer:innen suchen** und öffnen Sie ein Profil. Für die Schritte siehe [Nutzerprofile]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/). Um Zielgruppen nach diesen Werten zu filtern, navigieren Sie zu **Zielgruppe** > **Segmente**. Für Navigationsschritte siehe [Segment erstellen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) und Filteroptionen unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Informationen zur Erstellung angepasster Berichte finden Sie unter [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/).

## Weiterführende Referenzen

- [Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/)
- [Angepasste Events protokollieren]({{site.baseurl}}/developer_guide/analytics/logging_events/)
- [Angepasste Events]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/)
- [Nutzer:innen-Tracking-Endpunkt (`/users/track`)]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
- [Braze Android SDK-Repository](https://github.com/braze-inc/braze-android-sdk)
- [Braze Swift SDK-Repository](https://github.com/braze-inc/braze-swift-sdk)
- [Braze Web SDK-Repository](https://github.com/braze-inc/braze-web-sdk)