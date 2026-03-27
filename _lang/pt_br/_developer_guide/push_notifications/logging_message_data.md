---
nav_title: Análise de dados de push e registro de eventos personalizados
article_title: Análise de dados de push e registro de eventos personalizados
page_order: 7.2
description: "Saiba quais análises de dados de push a Braze registra automaticamente, como preservar o rastreamento nativo com tratamento personalizado de push e como registrar eventos personalizados ou atributos a partir dos dados da carga útil de push."
noindex: true
---

# Análise de dados de push e registro de eventos personalizados

> Esta página aborda os seguintes fluxos de trabalho: análise de dados nativa de push (aberturas, aberturas por influência e relatórios de campanha) e registro de dados personalizados (eventos personalizados e atributos) a partir de cargas úteis de push. Use este guia para identificar qual fluxo de trabalho se aplica ao seu caso de uso e siga as etapas para a sua plataforma.

## Pré-requisitos

Antes de começar, conclua a integração inicial de notificações por push para a sua plataforma:

- [Notificações por push para Android]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)
- [Notificações por push para Swift]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Notificações por push para web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## Análise de dados nativa de push vs. registro de eventos personalizados

Os fluxos de trabalho a seguir possuem superfícies de relatório diferentes.

| Categoria de análise de dados | Descrição | Onde aparece |
| --- | --- | --- |
| Análise de dados nativa de push | Métricas de push como aberturas e aberturas por influência, vinculadas a campanhas de push da Braze | Análise de dados de campanhas de push, eventos de engajamento com mensagem do Currents, Report Builder |
| Eventos personalizados e atributos | Análise de dados que você define e registra por meio de métodos do SDK ou do endpoint `/users/track` | Perfis de usuário, segmentação, campanhas e Canvas baseados em ação, análise de dados de eventos personalizados |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Registrar um evento personalizado (como `push_notification_opened`) não é o mesmo que o rastreamento nativo de abertura de push da Braze. Eventos personalizados não preenchem as métricas nativas de abertura de campanhas de push nem a atribuição de push.
{% endalert %}

## O que a Braze registra automaticamente

Quando a integração do SDK está configurada, a Braze registra automaticamente os dados principais de interação do canal, incluindo aberturas de push e aberturas por influência. Nenhum código adicional é necessário para a análise de dados padrão de push. Para uma lista completa dos dados coletados automaticamente, consulte [Coleta de dados do SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/).

Para saber mais, consulte:

- [Coleta de dados do SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/) para uma lista completa de dados coletados automaticamente e opcionais.
- [Aberturas por influência]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/) para saber como a Braze calcula as aberturas por influência.
- [Eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) para esquemas de eventos downstream no Currents.

## Preservando a análise de dados nativa de push com tratamento personalizado de push

Você pode usar um manipulador de push personalizado quando precisa integrar vários provedores de push, processar dados adicionais da carga útil ou implementar lógica personalizada de exibição de notificações. Se você usar um manipulador de push personalizado, ainda precisará passar as cargas úteis de push para os métodos do SDK da Braze. Isso permite que a Braze extraia os dados de rastreamento incorporados e registre a análise de dados nativa de push (aberturas, aberturas por influência e métricas de entrega).

{% tabs %}
{% tab Android %}

Se você tiver um `FirebaseMessagingService` personalizado, chame `BrazeFirebaseMessagingService.handleBrazeRemoteMessage(...)` dentro do seu método `onMessageReceived`. Lembre-se de que a subclasse do seu `FirebaseMessagingService` deve concluir a execução em até 9 segundos após a invocação para evitar ser [sinalizada ou encerrada](https://firebase.google.com/docs/cloud-messaging/android/receive) pelo sistema Android.

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

Para um exemplo completo de implementação, consulte o [app de exemplo de push Firebase do SDK Android da Braze](https://github.com/braze-inc/braze-android-sdk/tree/master/samples/firebase-push).

{% endtab %}
{% tab Swift %}

Em uma integração manual de push, encaminhe os retornos de chamada de notificações em segundo plano e de notificações do usuário para a Braze.

**Notificações em segundo plano:**

```swift
if let braze = AppDelegate.braze, braze.notifications.handleBackgroundNotification(
  userInfo: userInfo,
  fetchCompletionHandler: completionHandler
) {
  return
}
completionHandler(.noData)
```

**Respostas de notificações do usuário:**

```swift
if let braze = AppDelegate.braze, braze.notifications.handleUserNotification(
  response: response,
  withCompletionHandler: completionHandler
) {
  return
}
completionHandler()
```

**Notificações em primeiro plano:**

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

Para um exemplo completo de implementação, consulte o [exemplo de push manual do SDK Swift da Braze (`AppDelegate.swift`)](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotifications-Manual/AppDelegate.swift).

{% endtab %}
{% tab Web %}

Para push na web, configure seu service worker e a inicialização do SDK conforme descrito em [Notificações por push para web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

Para mais exemplos de código, consulte o [repositório do SDK Web da Braze](https://github.com/braze-inc/braze-web-sdk).

{% endtab %}
{% endtabs %}

## Registrando dados personalizados a partir de cargas úteis de push

Use esta seção quando precisar registrar dados adicionais a partir de pares chave-valor da carga útil de push, como eventos personalizados ou atributos vinculados à sua lógica de negócios.

Para saber mais sobre eventos personalizados, consulte [Eventos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/). Para registrar eventos personalizados por meio de métodos do SDK, consulte [Registrando eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/).

### Opção A: Registrar com o endpoint `/users/track`

Você pode registrar análise de dados em tempo real chamando o endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

Para identificar o perfil de usuário, inclua `braze_id` nos pares chave-valor da carga útil de push.

{% alert note %}
Passar `braze_id` identifica apenas o perfil. Você ainda precisa de lógica de implementação que leia os valores da carga útil e envie a requisição `/users/track` com os eventos ou atributos que deseja registrar.
{% endalert %}

### Opção B: Registrar com métodos do SDK após a inicialização do app

Você também pode salvar os dados da carga útil localmente e registrar eventos personalizados e atributos por meio de métodos do SDK após a inicialização do app. Essa abordagem é comum em fluxos de extensão de conteúdo de notificação, onde os dados de análise são persistidos primeiro e enviados na próxima inicialização do app.

{% alert important %}
Os dados de análise não são enviados para a Braze até que o app seja iniciado. Dependendo das suas configurações de descarte, pode haver um atraso entre o momento em que o usuário descarta a notificação e quando o app abre e envia os dados de análise.
{% endalert %}

## Registrando a partir de uma extensão de conteúdo de notificação (Swift)

As etapas a seguir descrevem como salvar e enviar eventos personalizados, atributos personalizados e atributos de usuário a partir de uma extensão de conteúdo de notificação Swift.

### Etapa 1: Configurar grupos de app no Xcode

No Xcode, adicione a capacidade `App Groups` ao target principal do seu app. Ative **App Groups** e clique em **+** para adicionar um novo grupo. Use o bundle ID do seu app para criar o identificador do grupo (por exemplo, `group.com.company.appname.xyz`). Ative **App Groups** tanto para o target principal do app quanto para o target da extensão de conteúdo.

![Xcode mostrando a capacidade App Groups ativada para o app principal e a extensão de notificação]({% image_buster /assets/img/swift/push_story/add_app_groups.png %})

### Etapa 2: Escolher o que registrar

Antes de implementar os trechos de código, escolha qual categoria de análise de dados você deseja registrar:

- **Eventos personalizados:** Ações que os usuários realizam (por exemplo, concluir um fluxo ou tocar em um elemento específico da interface). Use eventos personalizados para gatilhos baseados em ação, segmentação e análise de dados de eventos. Para saber mais, consulte [Eventos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/) e [Registrando eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/).
- **Atributos personalizados:** Campos de perfil que você define (por exemplo, `plan_tier` ou `preferred_language`) e atualiza ao longo do tempo. Para saber mais, consulte [Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/) e [Definindo atributos de usuário]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/).
- **Atributos de usuário:** Campos padrão de perfil (por exemplo, e-mail, nome e número de telefone). No código de exemplo, eles são representados por um modelo tipado `UserAttribute` e então mapeados para campos de usuário da Braze.

Os arquivos auxiliares nesta seção (`RemoteStorage`, `UserAttribute` e `EventName Dictionary`) são arquivos utilitários locais usados por esta implementação de exemplo. Eles não são classes integradas do SDK. Eles armazenam dados derivados da carga útil em `UserDefaults`, definem um modelo tipado para atualizações pendentes de usuário e padronizam a construção da carga útil de eventos. Para saber mais sobre o comportamento de armazenamento local de dados, consulte [Armazenamento]({{site.baseurl}}/developer_guide/storage/?tab=swift).

{% alert note %}
Os exemplos de arquivos auxiliares nesta seção são específicos para iOS (Swift e Objective-C). Para abordagens de Android e Web para registrar eventos personalizados e atributos, consulte [Registrando eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/) ([Android]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)) e [Definindo atributos de usuário]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/) ([Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=web)).
{% endalert %}

{% tabs local %}
{% tab Custom events %}

#### Salvando eventos personalizados

Crie a carga útil de análise de dados construindo um dicionário, preenchendo os metadados e salvando com o arquivo auxiliar.

1. Inicialize um dicionário com os metadados do evento.
2. Inicialize `userDefaults` para recuperar e armazenar os dados do evento.
3. Se um array existente for encontrado, adicione e salve.
4. Se nenhum array existir, salve um novo array.

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

#### Enviando eventos personalizados para a Braze

Registre os dados de análise salvos logo após a inicialização do SDK.

1. Percorra os eventos pendentes.
2. Percorra os pares chave-valor em cada evento.
3. Verifique a chave `event_name`.
4. Adicione os pares chave-valor restantes ao dicionário `properties`.
5. Registre cada evento personalizado.
6. Remova os eventos pendentes do armazenamento.

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

#### Salvando atributos personalizados

Crie o dicionário de análise de dados do zero e persista-o.

1. Inicialize um dicionário com os metadados do atributo.
2. Inicialize `userDefaults` para recuperar e armazenar os dados do atributo.
3. Se um array existente for encontrado, adicione e salve.
4. Se nenhum array existir, salve um novo array.

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

#### Enviando atributos personalizados para a Braze

Registre os dados de análise salvos logo após a inicialização do SDK.

1. Percorra os atributos pendentes.
2. Percorra cada par chave-valor.
3. Registre cada chave e valor de atributo personalizado.
4. Remova os atributos pendentes do armazenamento.

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

#### Salvando atributos de usuário

Ao salvar atributos de usuário, crie um objeto personalizado para capturar qual campo de usuário está sendo atualizado (`email`, `first_name`, `phone_number` e assim por diante). O objeto deve ser compatível com armazenamento e recuperação via `UserDefaults`. Consulte o arquivo auxiliar `UserAttribute` na guia **Arquivos auxiliares** para um exemplo.

1. Inicialize um objeto `UserAttribute` codificado com o tipo correspondente.
2. Inicialize `userDefaults` para recuperar e armazenar os dados.
3. Se um array existente for encontrado, adicione e salve.
4. Se nenhum array existir, salve um novo array.

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

#### Enviando atributos de usuário para a Braze

Registre os dados de análise salvos logo após a inicialização do SDK.

1. Percorra os dados de `pendingAttributes`.
2. Decodifique cada `UserAttribute`.
3. Defina os campos de usuário com base no tipo de atributo.
4. Remova os atributos de usuário pendentes do armazenamento.

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

#### Arquivo auxiliar RemoteStorage

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

#### Arquivo auxiliar UserAttribute

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

#### Arquivo auxiliar de dicionário EventName

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

## Analisando resultados

Use a superfície de relatório que corresponde à categoria de análise de dados:

| Categoria de análise de dados | Onde visualizar na Braze |
| --- | --- |
| Análise de dados nativa de push | Para visualizar as métricas de abertura de push no nível da campanha, navegue até a página **Análise de dados da campanha** da sua campanha de push. Para definições de métricas, consulte [Aberturas por influência]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/). Para criar visualizações personalizadas de análise de dados, navegue até **Análise de dados** > **Report Builder (Novo)**. Para etapas de navegação, consulte [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/). Para esquemas de eventos em nível de data warehouse, consulte [Eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/). |
| Eventos personalizados e atributos | Para visualizar tendências de eventos personalizados, navegue até **Análise de dados** > **Relatório de eventos personalizados**. Para mais informações, consulte [Eventos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/). Para inspecionar valores no nível do usuário, navegue até a página **Pesquisar usuários** e abra um perfil. Para ver as etapas, consulte [Perfis de usuário]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/). Para filtrar públicos por esses valores, navegue até **Público** > **Segmentos**. Para etapas de navegação, consulte [Criar um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) e opções de filtro em [Filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para criação de relatórios personalizados, consulte [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/).

## Referências relacionadas

- [Notificações por push]({{site.baseurl}}/developer_guide/push_notifications/)
- [Registrando eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/)
- [Eventos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/)
- [Endpoint de rastreamento de usuários (`/users/track`)]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
- [Repositório do SDK Android da Braze](https://github.com/braze-inc/braze-android-sdk)
- [Repositório do SDK Swift da Braze](https://github.com/braze-inc/braze-swift-sdk)
- [Repositório do SDK Web da Braze](https://github.com/braze-inc/braze-web-sdk)