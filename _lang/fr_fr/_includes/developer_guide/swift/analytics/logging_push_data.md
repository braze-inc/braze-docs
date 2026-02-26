## Enregistrement des données avec l'API de Braze (recommandé)

L'enregistrement de l’analyse peut être effectué en temps réel à l'aide de [l'endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de l'API Braze. Pour enregistrer l’analyse, envoyez la valeur `braze_id` dans le champ des paires clé-valeur (comme indiqué dans la capture d’écran suivante) pour identifier le profil utilisateur à mettre à jour.

![Une notification push avec trois ensembles de paires clé-valeur. 1. "Braze_id" réglé comme un appel liquide pour récupérer l'ID de Braze. 2. "cert_title" défini comme "Braze Marketer Certification". 3. "Cert_description" défini comme "Entraîneur certifié pour le marché de la Braze...".]({% image_buster /assets/img/push_implementation_guide/push18.png %}){: style="max-width:80%;"}

## Enregistrement manuel des données

L’enregistrement manuel exigera la configuration préalable des espaces de travail dans Xcode, puis la création, l’enregistrement et la récupération des analyses. Cela nécessitera un travail de développeur personnalisé de votre côté. Les extraits de code suivants vous aideront à résoudre ce problème. 

Il est important de noter que les analyses ne seront pas envoyées à Braze tant que l’application mobile n’aura pas été lancée subséquemment. Cela signifie que, selon vos paramètres de rejet, il existe souvent une période indéterminée entre le moment où une notification push est rejetée et l’application mobile est lancée et que les analyses sont récupérées. Même si cette période tampon n’affecte pas tous les cas d’utilisation, vous devez prendre en compte l’impact et, si nécessaire, ajuster votre parcours utilisateur afin d’inclure l’ouverture de l’application pour répondre à ce problème. 

![Un graphique décrivant la manière dont les analyses sont traitées par Braze. 1\. Les données d'analyse sont créées. 2\. Les données d'analyse sont enregistrées. 3\. La notification push est rejetée. 4\. Période indéterminée entre le moment où la notification push est rejetée et l’application mobile est lancée. 5\. L’application mobile est lancée. 6\. Les données d'analyse sont reçues. 7\. Les données d'analyse sont envoyées à Braze.]({% image_buster /assets/img/push_implementation_guide/push13.png %})

### Étape 1 : Configurer les groupes d’applications dans Xcode

Dans Xcode, ajoutez la capacité `App Groups`. Si vous n'avez pas d'espace de travail dans votre application, allez dans la capacité de la cible d’application principale, activez `App Groups`, puis cliquez sur le bouton **+** Ajouter. Ensuite, utilisez l'ID du bundle de votre application pour créer l'espace de travail. Par exemple, si l'ID du bundle de votre application est `com.company.appname`, vous pouvez nommer votre espace de travail `group.com.company.appname.xyz`. Assurez-vous que les `App Groups` sont activés pour la cible de votre application principale et la cible de l’extension de contenu.

![]({% image_buster /assets/img/swift/push_story/add_app_groups.png %})

### Étape 2 : Intégrer les extraits de code

Les extraits de code suivants sont une référence utile sur la façon d’enregistrer et d’envoyer des événements personnalisés, des attributs personnalisés et des attributs utilisateur. Dans ce guide, nous parlerons en termes de `UserDefaults`, mais le code sera représenté sous la forme du fichier d'aide `RemoteStorage`. Il existe des fichiers d'aide supplémentaires, `UserAttributes` et `EventName Dictionary`, qui sont utilisés pour envoyer et enregistrer les attributs de l'utilisateur.

{% tabs local %}
{% tab Custom Events %}

#### Enregistrement des événements personnalisés

Pour enregistrer des événements personnalisés, vous devez créer l’analyse à partir de zéro. Pour ce faire, créez un dictionnaire, renseignez-le avec des métadonnées et enregistrez les données via l’utilisation d’un fichier d’aide.

1. Initialiser un dictionnaire avec des métadonnées d’événement
2. Initialiser `userDefaults` pour récupérer et stocker les données d’événements
3. Si un tableau existe déjà, ajoutez-y de nouvelles données et enregistrez
4. S’il n’y a pas de tableau existant, enregistrez le nouveau tableau sur `userDefaults`

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

#### Envoi d’événements personnalisés à Braze

Le meilleur moment pour enregistrer une analyse sauvegardée à partir d'une extension d'application de contenu de notification est juste après l'initialisation du SDK. Pour ce faire, vous pouvez parcourir en boucle tous les événements en attente, vérifier la présence de la touche "Nom de l'événement", définir les valeurs appropriées dans Braze, puis effacer la mémoire pour la prochaine fois que cette fonction sera nécessaire.

1. Passez en revue la série d’événements en attente
2. Passez en revue chaque paire clé-valeur dans le dictionnaire `pendingEvents`
3. Vérifiez explicitement la clé pour « Nom de l'événement » afin de définir la valeur en conséquence
4. Toutes les autres clés-valeurs seront ajoutées au dictionnaire `properties`
5. Consigner un événement personnalisé individuel 
6. Supprimer tous les événements en attente du stockage

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
{% tab Custom Attributes %}

#### Enregistrer des attributs personnalisés

Pour enregistrer des attributs personnalisés, vous devez créer l’analyse à partir de zéro. Pour ce faire, créez un dictionnaire, renseignez-le avec des métadonnées et enregistrez les données via l’utilisation d’un fichier d’aide.

1. Initialiser un dictionnaire avec des attributs de métadonnées
2. Initialiser `userDefaults` pour récupérer et stocker les données d’attributs
3. Si un tableau existe déjà, ajoutez-y de nouvelles données et enregistrez
4. S’il n’y a pas de tableau existant, enregistrez le nouveau tableau sur `userDefaults`

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

#### Envoyer des attributs personnalisés à Braze

Le meilleur moment pour enregistrer une analyse sauvegardée à partir d'une extension d'application de contenu de notification est juste après l'initialisation du SDK. Pour ce faire, vous pouvez parcourir tous les attributs en attente, en définissant l’attribut personnalisé approprié dans Braze, puis en effaçant l’enregistrement pour la prochaine fois que cette fonction sera nécessaire.

1. Passez en revue la série d’attributs en attente
2. Passez en revue chaque paire clé-valeur dans le dictionnaire `pendingAttributes`
3. Enregistrer les attributs personnalisés individuels avec la clé et la valeur correspondantes
4. Supprimer tous les attributs en attente du stockage

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
{% tab User Attributes %}

#### Enregistrer des attributs utilisateur

Lorsque vous enregistrez des attributs utilisateur, nous vous recommandons de créer un objet personnalisé pour déterminer le type d'attribut mis à jour (`email`, `first_name`, `phone_number`, etc.). L’objet doit être compatible avec ce qui a été stocké/récupéré dans `UserDefaults`. Voir le fichier d’aide `UserAttribute` pour un exemple de la manière d’y parvenir.

1. Initialiser un objet `UserAttribute` encodé avec le type correspondant
2. Initialiser `userDefaults` pour récupérer et stocker les données d’événements
3. Si un tableau existe déjà, ajoutez-y de nouvelles données et enregistrez
4. S’il n’y a pas de tableau existant, enregistrez le nouveau tableau sur `userDefaults`

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

#### Envoyer des attributs utilisateur à Braze

Le meilleur moment pour enregistrer une analyse sauvegardée à partir d'une extension d'application de contenu de notification est juste après l'initialisation du SDK. Pour ce faire, vous pouvez parcourir tous les attributs en attente, en définissant l’attribut personnalisé approprié dans Braze, puis en effaçant l’enregistrement pour la prochaine fois que cette fonction sera nécessaire.

1. Parcourir le tableau de données `pendingAttributes`
2. Initialiser un objet `UserAttribute` encodé à partir des données d’attribut
3. Définir un champ utilisateur spécifique basé sur le type d’attribut utilisateur (e-mail)
4. Supprimer tous les attributs utilisateur en attente du stockage

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
{% tab Helper Files %}

#### Fichiers d’aide

{% details RemoteStorage Helper File %}
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
{% details UserAttribute Helper File %}
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
{% details EventName Dictionary Helper File %}
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
