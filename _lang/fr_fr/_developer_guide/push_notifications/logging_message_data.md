---
nav_title: Analytique push et journalisation d'événements personnalisés
article_title: Analytique push et journalisation d'événements personnalisés
page_order: 7.2
description: "Découvrez les données analytiques push que Braze enregistre automatiquement, comment préserver le suivi natif avec un gestionnaire push personnalisé, et comment journaliser des événements personnalisés ou des attributs à partir des données du payload push."
noindex: true
---

# Analytique push et journalisation d'événements personnalisés

> Cette page couvre les workflows suivants : l'analytique push native (ouvertures, ouvertures influencées et rapports de campagne) et la journalisation de données personnalisées (événements personnalisés et attributs) à partir des payloads push. Utilisez ce guide pour identifier le workflow qui correspond à votre cas d'utilisation et suivez les étapes pour votre plateforme.

## Conditions préalables

Avant de commencer, effectuez l'intégration initiale des notifications push pour votre plateforme :

- [Notifications push Android]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)
- [Notifications push Swift]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Notifications push Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## Analytique push native vs. journalisation d'événements personnalisés

Les workflows suivants ont chacun des surfaces de reporting différentes.

| Catégorie d'analytique | Description | Où elle apparaît |
| --- | --- | --- |
| Analytique push native | Indicateurs push tels que les ouvertures et les ouvertures influencées, liés aux campagnes push de Braze | Analytique des campagnes push, événements d'engagement lié aux messages Currents, générateur de rapports |
| Événements personnalisés et attributs | Données analytiques que vous définissez et journalisez via les méthodes du SDK ou l'endpoint `/users/track` | Profils utilisateur, segmentation, campagnes et Canvas basés sur des actions, analytique des événements personnalisés |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Journaliser un événement personnalisé (tel que `push_notification_opened`) n'est pas la même chose que le suivi natif des ouvertures push de Braze. Les événements personnalisés ne renseignent pas les indicateurs natifs d'ouverture des campagnes push ni l'attribution push.
{% endalert %}

## Ce que Braze enregistre automatiquement

Lorsque votre intégration SDK est configurée, Braze enregistre automatiquement les données d'interaction de base du canal, y compris les ouvertures push et les ouvertures influencées. Aucun code supplémentaire n'est nécessaire pour l'analytique push standard. Pour une liste complète des données collectées automatiquement, consultez [Collecte de données du SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/).

Pour plus de détails, consultez les ressources suivantes :

- [Collecte de données du SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/) pour une liste complète des données collectées automatiquement et facultatives.
- [Ouvertures influencées]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/) pour comprendre comment Braze calcule les ouvertures influencées.
- [Événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) pour les schémas d'événements en aval dans Currents.

## Préserver l'analytique push native avec un gestionnaire push personnalisé

Vous pouvez utiliser un gestionnaire push personnalisé lorsque vous devez intégrer plusieurs fournisseurs push, traiter des données de payload supplémentaires ou implémenter une logique d'affichage de notification personnalisée. Si vous utilisez un gestionnaire push personnalisé, vous devez tout de même transmettre les payloads push aux méthodes du SDK de Braze. Cela permet à Braze d'extraire les données de suivi intégrées et de journaliser l'analytique push native (ouvertures, ouvertures influencées et indicateurs de distribution).

{% tabs %}
{% tab Android %}

Si vous avez un `FirebaseMessagingService` personnalisé, appelez `BrazeFirebaseMessagingService.handleBrazeRemoteMessage(...)` dans votre méthode `onMessageReceived`. Gardez à l'esprit que votre sous-classe `FirebaseMessagingService` doit terminer son exécution dans les 9 secondes suivant l'invocation pour éviter d'être [signalée ou terminée](https://firebase.google.com/docs/cloud-messaging/android/receive) par le système Android.

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

Pour un exemple d'implémentation complet, consultez l'[application exemple Firebase push du SDK Android de Braze](https://github.com/braze-inc/braze-android-sdk/tree/master/samples/firebase-push).

{% endtab %}
{% tab Swift %}

Dans une intégration push manuelle, transmettez les rappels de notifications en arrière-plan et de notifications utilisateur à Braze.

**Notifications en arrière-plan :**

```swift
if let braze = AppDelegate.braze, braze.notifications.handleBackgroundNotification(
  userInfo: userInfo,
  fetchCompletionHandler: completionHandler
) {
  return
}
completionHandler(.noData)
```

**Réponses aux notifications utilisateur :**

```swift
if let braze = AppDelegate.braze, braze.notifications.handleUserNotification(
  response: response,
  withCompletionHandler: completionHandler
) {
  return
}
completionHandler()
```

**Notifications au premier plan :**

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

Pour un exemple d'implémentation complet, consultez l'[exemple push manuel du SDK Swift de Braze (`AppDelegate.swift`)](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotifications-Manual/AppDelegate.swift).

{% endtab %}
{% tab Web %}

Pour le push web, configurez votre service de traitement et l'initialisation du SDK comme décrit dans [Notifications push Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

Pour plus d'exemples de code, consultez le [dépôt du SDK Web de Braze](https://github.com/braze-inc/braze-web-sdk).

{% endtab %}
{% endtabs %}

## Journaliser des données personnalisées à partir des payloads push

Utilisez cette section lorsque vous devez journaliser des données supplémentaires à partir des paires clé-valeur du payload push, telles que des événements personnalisés ou des attributs liés à votre logique métier.

Pour plus d'informations sur les événements personnalisés, consultez [Événements personnalisés]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/). Pour journaliser des événements personnalisés via les méthodes du SDK, consultez [Journaliser des événements personnalisés]({{site.baseurl}}/developer_guide/analytics/logging_events/).

### Option A : Journaliser avec l'endpoint `/users/track`

Vous pouvez journaliser des données analytiques en temps réel en appelant l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

Pour identifier le profil utilisateur, incluez `braze_id` dans les paires clé-valeur de votre payload push.

{% alert note %}
Transmettre `braze_id` permet uniquement d'identifier le profil. Vous devez toujours implémenter la logique qui lit les valeurs du payload et envoie la requête `/users/track` avec les événements ou attributs que vous souhaitez journaliser.
{% endalert %}

### Option B : Journaliser avec les méthodes du SDK après le lancement de l'application

Vous pouvez également enregistrer les données du payload localement et journaliser les événements personnalisés et les attributs via les méthodes du SDK après l'initialisation de l'application. Cette approche est courante dans les flux d'extension de contenu de notification, où les données analytiques sont d'abord persistées puis envoyées au prochain lancement de l'application.

{% alert important %}
Les données analytiques ne sont pas envoyées à Braze tant que l'application n'est pas lancée. Selon vos paramètres de fermeture, il peut y avoir un délai entre le moment où l'utilisateur ferme la notification et celui où l'application s'ouvre et envoie les données analytiques.
{% endalert %}

## Journaliser depuis une extension de contenu de notification (Swift)

Les étapes suivantes décrivent comment enregistrer et envoyer des événements personnalisés, des attributs personnalisés et des attributs utilisateur depuis une extension de contenu de notification Swift.

### Étape 1 : Configurer les groupes d'applications dans Xcode

Dans Xcode, ajoutez la capacité `App Groups` à la cible de votre application principale. Activez **App Groups**, puis cliquez sur **+** pour ajouter un nouveau groupe. Utilisez l'identifiant de bundle de votre application pour créer l'identifiant du groupe (par exemple, `group.com.company.appname.xyz`). Activez **App Groups** à la fois pour la cible de votre application principale et pour la cible de l'extension de contenu.

![Xcode montrant la capacité App Groups activée pour l'application principale et l'extension de notification]({% image_buster /assets/img/swift/push_story/add_app_groups.png %})

### Étape 2 : Choisir ce que vous souhaitez journaliser

Avant d'implémenter les extraits de code, choisissez la catégorie d'analytique que vous souhaitez journaliser :

- **Événements personnalisés :** Actions effectuées par les utilisateurs (par exemple, compléter un flux ou appuyer sur un élément d'interface spécifique). Utilisez les événements personnalisés pour les déclencheurs basés sur des actions, la segmentation et l'analytique des événements. Pour plus d'informations, consultez [Événements personnalisés]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/) et [Journaliser des événements personnalisés]({{site.baseurl}}/developer_guide/analytics/logging_events/).
- **Attributs personnalisés :** Champs de profil que vous définissez (par exemple, `plan_tier` ou `preferred_language`) et mettez à jour au fil du temps. Pour plus d'informations, consultez [Attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/) et [Définir les attributs utilisateur]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/).
- **Attributs utilisateur :** Champs de profil standard (par exemple, e-mail, prénom et numéro de téléphone). Dans l'exemple de code, ceux-ci sont représentés par un modèle typé `UserAttribute` puis mappés aux champs utilisateur de Braze.

Les fichiers utilitaires de cette section (`RemoteStorage`, `UserAttribute` et `EventName Dictionary`) sont des fichiers utilitaires locaux utilisés par cet exemple d'implémentation. Ce ne sont pas des classes intégrées au SDK. Ils stockent les données dérivées du payload dans `UserDefaults`, définissent un modèle typé pour les mises à jour utilisateur en attente et standardisent la construction du payload d'événement. Pour plus d'informations sur le comportement du stockage local des données, consultez [Stockage]({{site.baseurl}}/developer_guide/storage/?tab=swift).

{% alert note %}
Les exemples de fichiers utilitaires de cette section sont spécifiques à iOS (Swift et Objective-C). Pour les approches Android et Web de journalisation des événements personnalisés et des attributs, consultez [Journaliser des événements personnalisés]({{site.baseurl}}/developer_guide/analytics/logging_events/) ([Android]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)) et [Définir les attributs utilisateur]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/) ([Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=web)).
{% endalert %}

{% tabs local %}
{% tab Custom events %}

#### Enregistrer des événements personnalisés

Créez le payload analytique en construisant un dictionnaire, en renseignant les métadonnées et en l'enregistrant avec le fichier utilitaire.

1. Initialisez un dictionnaire avec les métadonnées de l'événement.
2. Initialisez `userDefaults` pour récupérer et stocker les données d'événement.
3. Si un tableau existant est trouvé, ajoutez-y les données et enregistrez.
4. Si aucun tableau n'existe, enregistrez un nouveau tableau.

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

#### Envoyer des événements personnalisés à Braze

Journalisez les données analytiques enregistrées juste après l'initialisation du SDK.

1. Parcourez les événements en attente.
2. Parcourez les paires clé-valeur de chaque événement.
3. Vérifiez la présence de la clé `event_name`.
4. Ajoutez les paires clé-valeur restantes au dictionnaire `properties`.
5. Journalisez chaque événement personnalisé.
6. Supprimez les événements en attente du stockage.

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

#### Enregistrer des attributs personnalisés

Créez le dictionnaire analytique de zéro, puis persistez-le.

1. Initialisez un dictionnaire avec les métadonnées de l'attribut.
2. Initialisez `userDefaults` pour récupérer et stocker les données d'attribut.
3. Si un tableau existant est trouvé, ajoutez-y les données et enregistrez.
4. Si aucun tableau n'existe, enregistrez un nouveau tableau.

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

#### Envoyer des attributs personnalisés à Braze

Journalisez les données analytiques enregistrées juste après l'initialisation du SDK.

1. Parcourez les attributs en attente.
2. Parcourez chaque paire clé-valeur.
3. Journalisez chaque clé et valeur d'attribut personnalisé.
4. Supprimez les attributs en attente du stockage.

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

#### Enregistrer des attributs utilisateur

Lors de l'enregistrement des attributs utilisateur, créez un objet personnalisé pour capturer quel champ utilisateur est mis à jour (`email`, `first_name`, `phone_number`, etc.). L'objet doit être compatible avec le stockage et la récupération via `UserDefaults`. Consultez le fichier utilitaire `UserAttribute` dans l'onglet **Fichiers utilitaires** pour un exemple.

1. Initialisez un objet `UserAttribute` encodé avec le type correspondant.
2. Initialisez `userDefaults` pour récupérer et stocker les données.
3. Si un tableau existant est trouvé, ajoutez-y les données et enregistrez.
4. Si aucun tableau n'existe, enregistrez un nouveau tableau.

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

#### Envoyer des attributs utilisateur à Braze

Journalisez les données analytiques enregistrées juste après l'initialisation du SDK.

1. Parcourez les données `pendingAttributes`.
2. Décodez chaque `UserAttribute`.
3. Définissez les champs utilisateur en fonction du type d'attribut.
4. Supprimez les attributs utilisateur en attente du stockage.

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

#### Fichier utilitaire RemoteStorage

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

#### Fichier utilitaire UserAttribute

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

#### Fichier utilitaire EventName dictionary

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

## Analyser les résultats

Utilisez la surface de reporting correspondant à la catégorie d'analytique :

| Catégorie d'analytique | Où consulter dans Braze |
| --- | --- |
| Analytique push native | Pour consulter les indicateurs d'ouverture push au niveau de la campagne, accédez à la page **Analytique de la campagne** de votre campagne push. Pour les définitions des indicateurs, consultez [Ouvertures influencées]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/). Pour créer des vues analytiques personnalisées, accédez à **Analytique** > **Générateur de rapports (Nouveau)**. Pour les étapes de navigation, consultez [Générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/). Pour les schémas d'événements au niveau de l'entrepôt de données, consultez [Événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/). |
| Événements personnalisés et attributs | Pour consulter les tendances des événements personnalisés, accédez à **Analytique** > **Rapport des événements personnalisés**. Pour plus de détails, consultez [Événements personnalisés]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/). Pour inspecter les valeurs au niveau utilisateur, accédez à la page **Rechercher des utilisateurs** et ouvrez un profil. Pour les étapes, consultez [Profils utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/). Pour filtrer les audiences par ces valeurs, accédez à **Audience** > **Segments**. Pour les étapes de navigation, consultez [Créer un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) et les options de filtre dans [Filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour la création de rapports personnalisés, consultez [Générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/).

## Références associées

- [Notifications push]({{site.baseurl}}/developer_guide/push_notifications/)
- [Journaliser des événements personnalisés]({{site.baseurl}}/developer_guide/analytics/logging_events/)
- [Événements personnalisés]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/)
- [Endpoint de suivi des utilisateurs (`/users/track`)]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
- [Dépôt du SDK Android de Braze](https://github.com/braze-inc/braze-android-sdk)
- [Dépôt du SDK Swift de Braze](https://github.com/braze-inc/braze-swift-sdk)
- [Dépôt du SDK Web de Braze](https://github.com/braze-inc/braze-web-sdk)