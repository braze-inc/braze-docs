## Protokollierung von Daten mit der Braze API (empfohlen)

Mit Hilfe des [`/users/track`-Endpunkts]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) der Braze API können Sie Analytics in Realtime protokollieren. Senden Sie dazu den Wert `braze_id` in das Feld der Schlüssel-Wert-Paare (wie im folgenden Screenshot zu sehen), um das zu aktualisierende Nutzerprofil zu identifizieren.

![Eine Push-Nachricht mit drei Gruppen von Schlüssel-Wert-Paaren. 1\. "Braze_id" als Liquid-Aufruf zum Abrufen der Braze-ID eingestellt. 2\. "cert_title" als "Braze Marketer Certification" festgelegt. 3\. "Cert_description" ist auf "Certified Braze marketers drive..." festgelegt.]({% image_buster /assets/img/push_implementation_guide/push18.png %}){: style="max-width:80%;"}

## Daten manuell protokollieren

Für die manuelle Protokollierung müssen Sie zunächst Workspaces-in Xcode konfigurieren und anschließend Analytics erstellen, speichern und abrufen. Dies erfordert einige Anpassungen auf Ihrer Seite. Die folgenden Codeschnipsel helfen Ihnen bei der Lösung dieses Problems. 

Ein wichtiger Punkt, den es zu beachten gilt, ist, dass Analytics erst dann an Braze gesendet werden, wenn die mobile Anwendung anschließend gestartet wird. Das bedeutet, dass je nach Ihren Einstellungen für die Beendigung oft eine unbestimmte Zeitspanne zwischen der Beendigung einer Push-Benachrichtigung und dem Start der mobilen App und dem Abrufen der Analysen vergeht. Auch wenn dieser Zeitpuffer nicht alle Anwendungsfälle betrifft, sollten Sie diese Auswirkung berücksichtigen und Ihre Nutzer:innen so anpassen, dass sie die Öffnung der Anwendung einbeziehen, um dieses Problem zu lösen. 

![Grafik, die die Verarbeitung von Analytics in Braze beschreibt. 1\. Es werden Analysedaten erstellt. 2\. Die Analysedaten werden gespeichert. 3\. Die Push-Benachrichtigung wird abgelehnt. 4\. Unbestimmte Zeitspanne zwischen der Ablehnung der Push-Benachrichtigung und dem Start der mobilen App. 5\. Die mobile App wird gestartet. 6\. Analysedaten werden empfangen. 7\. Die Analysedaten werden an Braze gesendet.]({% image_buster /assets/img/push_implementation_guide/push13.png %})

### Schritt 1: App-Gruppen in Xcode konfigurieren

Fügen Sie in Xcode die Funktion `App Groups` hinzu. Wenn Sie noch keine Workspaces in Ihrer App hatten, gehen Sie zu den Fähigkeiten des Haupt-Targetings der App, aktivieren Sie `App Groups` und klicken Sie auf den Button **+** Hinzufügen. Verwenden Sie dann die Bundle ID Ihrer App, um den Workspace zu erstellen. Wenn die Bundle-ID Ihrer App zum Beispiel `com.company.appname` lautet, können Sie Ihren Workspace `group.com.company.appname.xyz` nennen. Vergewissern Sie sich, dass `App Groups` sowohl für die Hauptzielgruppe Ihrer App als auch für die Zielgruppe der Inhaltserweiterung aktiviert ist.

![]({% image_buster /assets/img/swift/push_story/add_app_groups.png %})

### Schritt 2: Code-Snippets integrieren

Die folgenden Code-Snippets sind eine hilfreiche Referenz, wie Sie angepasste Events, angepasste Attribute und Nutzerattribute speichern und senden können. Diese Anleitung bezieht sich auf `UserDefaults`, aber der Code wird in Form der Hilfsdatei `RemoteStorage` dargestellt. Es gibt zusätzliche Hilfsdateien, `UserAttributes` und `EventName Dictionary`, die beim Senden und Speichern von Nutzerattributen verwendet werden.

{% tabs local %}
{% tab Benutzerdefinierte Ereignisse %}

#### Speichern von benutzerdefinierten Ereignissen

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

#### Senden von angepassten Events an Braze

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

#### Speichern von benutzerdefinierten Attributen

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

#### Senden von benutzerdefinierten Attributen an Braze

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

#### Speichern von Benutzerattributen

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

#### Senden von Benutzerattributen an Braze

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

#### Hilfsdateien

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
