---
nav_title: Aplicación avanzada (Opcional)
article_title: Guía de implementación de la tarjeta de contenido para iOS (Opcional) 
platform: iOS
page_order: 7
description: "Esta guía de implementación avanzada abarca consideraciones sobre códigos de tarjetas de contenido de iOS, tres casos de uso creados por nuestro equipo, fragmentos de código que los acompañan y orientaciones sobre el registro de impresiones, clics y descartes."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

<br>
{% alert important %}
¿Buscas la guía básica de integración del desarrollador de la tarjeta de contenido? Encuéntralo [aquí]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration/).
{% endalert %}

# Guía de implantación de la tarjeta de contenido

> Esta guía de implementación opcional y avanzada abarca consideraciones sobre códigos de tarjetas de contenido, tres casos de uso personalizados creados por nuestro equipo, fragmentos de código que los acompañan y orientaciones sobre el registro de impresiones, clics y descartes. ¡Visita nuestro repositorio de demostraciones Braze [aquí](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Ten en cuenta que esta guía de implementación se centra en una implementación Swift, pero se proporcionan fragmentos de código Objective-C para los interesados.

## Consideraciones sobre códigos

### Tarjetas de contenido como objetos personalizados

Al igual que un cohete que añade un propulsor, tus propios objetos personalizados pueden ampliarse para funcionar como tarjetas de contenido. Las superficies API limitadas como esta proporcionan flexibilidad para trabajar con diferentes backends de datos indistintamente. Esto puede hacerse ajustándose al protocolo `ContentCardable` e implementando el inicializador (como se ve en los siguientes fragmentos de código) y, mediante el uso de la estructura `ContentCardData`, te permite acceder a los datos de `ABKContentCard`. La carga útil `ABKContentCard` se utilizará para inicializar la estructura `ContentCardData` y el propio objeto personalizado, todo ello a partir de un tipo `Dictionary` mediante el inicializador que incluye el protocolo.

El inicializador también incluye una enumeración `ContentCardClassType`. Esta enumeración se utiliza para decidir qué objeto inicializar. Mediante el uso de pares clave-valor dentro del panel Braze, puedes establecer una clave `class_type` explícita que se utilizará para determinar qué objeto inicializar. Estos pares clave-valor de las tarjetas de contenido aparecen en la variable `extras` en `ABKContentCard`. Otro componente básico del inicializador es el parámetro del diccionario `metaData`. El `metaData` incluye todo lo que hay en el `ABKContentCard` analizado en una serie de claves y valores. Una vez analizadas las tarjetas relevantes y convertidas en tus objetos personalizados, la aplicación está lista para empezar a trabajar con ellas como si se hubieran instanciado desde JSON o cualquier otra fuente. 

Una vez que tengas una sólida comprensión de estas consideraciones sobre códigos, consulta nuestros [casos de uso](#sample-use-cases) para empezar a implementar tus objetos personalizados.

{% tabs local %}
{% tab ContentCardable %}
{% subtabs global %}
{% subtab Swift %}
**Protocolo ContentCardable**<br>
Un objeto `ContentCardData` que representa los datos de `ABKContentCard` junto con una enumeración `ContentCardClassType`. Un inicializador utilizado para instanciar objetos personalizados con metadatos `ABKContentCard`.
```swift
protocol ContentCardable {
  var contentCardData: ContentCardData? { get }
  init?(metaData: [ContentCardKey: Any], classType contentCardClassType: ContentCardClassType)
}
 
extension ContentCardable {
  var isContentCard: Bool {
    return contentCardData != nil
  }
   
  func logContentCardClicked() {
    BrazeManager.shared.logContentCardClicked(idString: contentCardData?.contentCardId)
  }
   
  func logContentCardDismissed() {
    BrazeManager.shared.logContentCardDismissed(idString: contentCardData?.contentCardId)
  }
   
  func logContentCardImpression() {
    BrazeManager.shared.logContentCardImpression(idString: contentCardData?.contentCardId)
  }
}
```
**Estructura de datos de la tarjeta de contenido**<br>
`ContentCardData` representa los valores analizados de un `ABKContentCard`.

```swift
struct ContentCardData: Hashable {
  let contentCardId: String
  let contentCardClassType: ContentCardClassType
  let createdAt: Double
  let isDismissable: Bool
  ...
  // other Content Card properties such as expiresAt, pinned, etc.
}
 
extension ContentCardData: Equatable {
  static func ==(lhs: ContentCardData, rhs: ContentCardData) -> Bool {
    return lhs.contentCardId == rhs.contentCardId
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
**Protocolo ContentCardable**<br>
Un objeto `ContentCardData` que representa los datos `ABKContentCard` junto con una enumeración `ContentCardClassType`, un inicializador utilizado para instanciar objetos personalizados con metadatos `ABKContentCard`.
```objc
@protocol ContentCardable <NSObject>
 
@property (nonatomic, strong) ContentCardData *contentCardData;
- (instancetype __nullable)initWithMetaData:(NSDictionary *)metaData
                                  classType:(enum ContentCardClassType)classType;
 
- (BOOL)isContentCard;
- (void)logContentCardImpression;
- (void)logContentCardClicked;
- (void)logContentCardDismissed;
 
@end
```
**Estructura de datos de la tarjeta de contenido**<br>
`ContentCardData` representa los valores analizados de un `ABKContentCard`.

```objc
@interface ContentCardData : NSObject
 
+ (ContentCardClassType)contentCardClassTypeForString:(NSString *)rawValue;
 
- (instancetype)initWithIdString:(NSString *)idString
                       classType:(ContentCardClassType)classType
                       createdAt:(double)createdAt isDismissible:(BOOL)isDismissible;
 
@property (nonatomic, readonly) NSString *contentCardId;
@property (nonatomic) ContentCardClassType classType;
@property (nonatomic, readonly) double *createdAt;
@property (nonatomic, readonly) BOOL isDismissible;
...
// other Content Card properties such as expiresAt, pinned, etc.    
 
@end
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Objetos personalizados %}
{% subtabs global %}
{% subtab Swift %}
**Inicializador de objetos personalizado**<br>
Los metadatos de un `ABKContentCard` se utilizan para rellenar las variables de tu objeto. Los pares clave-valor configurados en el panel de Braze se representan en el diccionario "extras".

```swift
extension CustomObject: ContentCardable {
  init?(metaData: [ContentCardKey: Any], classType contentCardClassType: ContentCardClassType) {
    guard let idString = metaData[.idString] as? String,
      let createdAt = metaData[.created] as? Double,
      let isDismissable = metaData[.dismissable] as? Bool,
      let extras = metaData[.extras] as? [AnyHashable: Any],
      else { return nil }
 
    let contentCardData = ContentCardData(contentCardId: idString, contentCardClassType: contentCardClassType, createdAt: createdAt, isDismissable: isDismissable)
    let customObjectProperty = extras["YOUR-CUSTOM-OBJECT-PROPERTY"] as? String
           
    self.init(contentCardData: contentCardData, property: customObjectProperty)
  }
}
```

**Tipos identificadores**<br>
La enumeración `ContentCardClassType` representa el valor `class_type` en el panel Braze. Este valor también se utiliza como identificador de filtro para mostrar tarjetas de contenido en distintos lugares. 

```swift
enum ContentCardClassType: Hashable {
  case yourValue
  case yourOtherValue
  ...
  case none
 
  init(rawType: String?) {
    switch rawType?.lowercased() {
    case "your_value": // these values much match the value set in the Braze dashboard
      self = .yourValue
    case "your_other_value": // these values much match the value set in the Braze dashboard
      self = .yourOtherValue
    ...
    default:
      self = .none
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
**Inicializador de objetos personalizado**<br>
Los metadatos de un `ABKContentCard` se utilizan para rellenar las variables de tu objeto. Los pares clave-valor configurados en el panel de Braze se representan en el diccionario "extras".


```objc
- (id _Nullable)initWithMetaData:(nonnull NSDictionary *)metaData classType:(enum ContentCardClassType)classType {
  self = [super init];
  if (self) {
    if ([metaData objectForKey:ContentCardKeyIdString] && [metaData objectForKey:ContentCardKeyCreated] && [metaData objectForKey:ContentCardKeyDismissible] && [metaData objectForKey:ContentCardKeyExtras]) {
      NSDictionary  *extras = metaData[ContentCardKeyExtras];
      NSString *idString = metaData[ContentCardKeyIdString];
      double createdAt = [metaData[ContentCardKeyCreated] doubleValue];
      BOOL isDismissible = metaData[ContentCardKeyDismissible];
 
      if ([extras objectForKey: @"YOUR-CUSTOM-PROPERTY")
        _customObjectProperty = extras[@"YOUR-CUSTOM-OBJECT-PROPERTY"];
 
      self.contentCardData = [[ContentCardData alloc] initWithIdString:idString classType:classType createdAt:createdAt isDismissible:isDismissible];
 
      return self;
    }
  }
  return nil;
}
```

**Tipos identificadores**<br>
La enumeración `ContentCardClassType` representa el valor `class_type` en el panel Braze. Este valor también se utiliza como identificador de filtro para mostrar tarjetas de contenido en distintos lugares. 

```objc
typedef NS_ENUM(NSInteger, ContentCardClassType) {
  ContentCardClassTypeNone = 0,
  ContentCardClassTypeYourValue,
  ContentCardClassTypeYourOtherValue,
  ...
};
 
+ (NSArray *)contentCardClassTypeArray {
  return @[ @"", @"your_value", @"your_other_value" ];
}
 
+ (ContentCardClassType)contentCardClassTypeForString:(NSString*)rawValue {
  if ([[self contentCardClassTypeArray] indexOfObject:rawValue] == NSNotFound) {
    return ContentCardClassTypeNone;
  } else {
    NSInteger value = [[self contentCardClassTypeArray] indexOfObject:rawValue];
    return (ContentCardClassType) value;
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Manipulación de tarjetas de contenido %}
{% subtabs global %}
{% subtab Swift %}
**Solicitud de tarjetas de contenido**<br>
Mientras el observador siga retenido en memoria, se puede esperar la devolución de llamada de notificación del SDK de Braze.

```swift
func loadContentCards() {
  BrazeManager.shared.addObserverForContentCards(observer: self, selector: #selector(contentCardsUpdated))
  BrazeManager.shared.requestContentCardsRefresh()
}
```

**Manejo de la devolución de llamada SDK de las tarjetas de contenido**<br>
Reenvía la devolución de llamada de notificación al archivo de ayuda para analizar los datos de carga útil de tu(s) objeto(s) personalizado(s).
```swift
@objc func contentCardsUpdated(_ notification: Notification) {
  guard let contentCards = BrazeManager.shared.handleContentCardsUpdated(notification, for: [.yourValue]) as? [CustomObject],!contentCards.isEmpty else { return }
 
 // do something with your array of custom objects
}
```

**Trabajar con tarjetas de contenido**<br>
El `class_type` se pasa como filtro para devolver sólo las tarjetas de contenido que tengan un `class_type` coincidente.

```swift
func handleContentCardsUpdated(_ notification: Notification, for classTypes: [ContentCardClassType]) -> [ContentCardable] {
  guard let updateIsSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool, updateIsSuccessful, let cards = contentCards else { return [] }
             
  return convertContentCards(cards, for: classTypes)
}
```
{% endsubtab %}
{% subtab Objective-C %}
**Solicitud de tarjetas de contenido**<br>
Mientras el observador siga retenido en memoria, se puede esperar la devolución de llamada de notificación del SDK de Braze.

```objc
- (void)loadContentCards {
  [[BrazeManager shared] addObserverForContentCards:self selector:@selector(contentCardsUpdated:)];
  [[BrazeManager shared] requestContentCardsRefresh];
}
```

**Manejo de la devolución de llamada SDK de las tarjetas de contenido**<br>
Reenvía la devolución de llamada de notificación al archivo de ayuda para analizar los datos de carga útil de tu(s) objeto(s) personalizado(s).
```objc
- (void)contentCardsUpdated:(NSNotification *)notification {
  NSArray *classTypes = @[@(ContentCardClassTypeYourValue)];
  NSArray *contentCards = [[BrazeManager shared] handleContentCardsUpdated:notification forClassTypes:classTypes];
 
  // do something with your array of custom objects
}
```

**Trabajar con tarjetas de contenido**<br>
El `class_type` se pasa como filtro para devolver sólo las tarjetas de contenido que tengan un `class_type` coincidente.

```objc
- (NSArray *)handleContentCardsUpdated:(NSNotification *)notification forClassType:(ContentCardClassType)classType {  
  BOOL updateIsSuccessful = [notification.userInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue];
  if (updateIsSuccessful) {
    return [self convertContentCards:self.contentCards forClassType:classType];
  } else {
    return @[];
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Trabajar con datos de carga útil %}
{% subtabs global %}
{% subtab Swift %}
**Trabajar con datos de carga útil**<br>
Recorre la matriz de tarjetas de contenido y sólo analiza las tarjetas que coincidan con `class_type`. La carga útil de una ABKContentCard se analiza en `Dictionary`.

```swift
func convertContentCards(_ cards: [ABKContentCard], for classTypes: [ContentCardClassType]) -> [ContentCardable] {
  var contentCardables: [ContentCardable] = []
    
  for card in cards {
    let classTypeString = card.extras?[ContentCardKey.classType.rawValue] as? String
    let classType = ContentCardClassType(rawType: classTypeString)
    guard classTypes.contains(classType) else { continue }
       
    var metaData: [ContentCardKey: Any] = [:]
    switch card {
    case let banner as ABKBannerContentCard:
      metaData[.image] = banner.image
    case let captioned as ABKCaptionedImageContentCard:
      metaData[.title] = captioned.title
      metaData[.cardDescription] = captioned.cardDescription
      metaData[.image] = captioned.image
    case let classic as ABKClassicContentCard:
      metaData[.title] = classic.title
      metaData[.cardDescription] = classic.cardDescription
    default:
      break
    }
 
    metaData[.idString] = card.idString
    metaData[.created] = card.created
    metaData[.dismissible] = card.dismissible
    metaData[.urlString] = card.urlString
    metaData[.extras] = card.extras
    ...
    // other Content Card properties such as expiresAt, pinned, etc.
      
    if let contentCardable = contentCardable(with: metaData, for: classType) {
      contentCardables.append(contentCardable)
    }
  }
  return contentCardables
}
```

**Inicializar tus objetos personalizados a partir de los datos de la carga útil de la tarjeta de contenido**<br>
La dirección `class_type` se utiliza para determinar cuál de tus objetos personalizados se inicializará a partir de los datos de carga útil.

```swift
func contentCardable(with metaData: [ContentCardKey: Any], for classType: ContentCardClassType) -> ContentCardable? {
  switch classType {
  case .yourValue:
    return CustomObject(metaData: metaData, classType: classType)
  case .yourOtherValue:
    return OtherCustomObject(metaData: metaData, classType: classType)
  ...
  default:
    return nil
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
**Trabajar con datos de carga útil**<br>
Recorre la matriz de tarjetas de contenido y sólo analiza las tarjetas que coincidan con `class_type`. La carga útil de una ABKContentCard se analiza en `Dictionary`.

```objc
- (NSArray *)convertContentCards:(NSArray<ABKContentCard*> *)cards forClassType:(ContentCardClassType)classType {
  NSMutableArray *contentCardables = [[NSMutableArray alloc] init];      for (ABKContentCard *card in cards) {
    NSString *classTypeString = [card.extras objectForKey:ContentCardKeyClassType];
    ContentCardClassType cardClassType = [ContentCardData contentCardClassTypeForString: classTypeString];
    if (cardClassType != classType) { continue; }
     
    NSMutableDictionary *metaData = [[NSMutableDictionary alloc] init];
    if ([card isKindOfClass:[ABKBannerContentCard class]]) {
      ABKBannerContentCard *banner = (ABKBannerContentCard *)card;
      metaData[ContentCardKeyImage] = banner.image;
    } else if ([card isKindOfClass:[ABKCaptionedImageContentCard class]]) {
      ABKCaptionedImageContentCard *captioned = (ABKCaptionedImageContentCard *)card;
      metaData[ContentCardKeyTitle] = captioned.title;
      metaData[ContentCardKeyCardDescription] = captioned.cardDescription;
      metaData[ContentCardKeyImage] = captioned.image;
    } else if ([card isKindOfClass:[ABKClassicContentCard class]]) {
      ABKClassicContentCard *classic = (ABKClassicContentCard *)card;
      metaData[ContentCardKeyCardDescription] = classic.title;
      metaData[ContentCardKeyImage] = classic.image;
    }
     
    metaData[ContentCardKeyIdString] = card.idString;
    metaData[ContentCardKeyCreated] = [NSNumber numberWithDouble:card.created];
    metaData[ContentCardKeyDismissible] = [NSNumber numberWithBool:card.dismissible];
    metaData[ContentCardKeyUrlString] = card.urlString;
    metaData[ContentCardKeyExtras] = card.extras;
    ...
    // other Content Card properties such as expiresAt, pinned, etc.   
 
    id<ContentCardable> contentCardable = [self contentCardableWithMetaData:metaData forClassType:classType];
    if (contentCardable) {
      [contentCardables addObject:contentCardable];
    }
  }
 
  return contentCardables;
}
```

**Inicializar tus objetos personalizados a partir de los datos de la carga útil de la tarjeta de contenido**<br>
La dirección `class_type` se utiliza para determinar cuál de tus objetos personalizados se inicializará a partir de los datos de carga útil.

```obj-c
- (id<ContentCardable>)contentCardableWithMetaData:(NSDictionary *)metaData forClassType:(ContentCardClassType)classType {
  switch (classType) {
    case ContentCardClassTypeYourValue:
      return [[CustomObject alloc] initWithMetaData:metaData classType:classType];
    case ContentCardClassTypeYourOtherValue:
      return nil;
    ...
    default:
      return nil;
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Casos prácticos

A continuación te presentamos tres casos de uso. Cada caso de uso ofrece una explicación detallada, fragmentos de código relevantes y una visión de cómo pueden verse y utilizarse las variables de la tarjeta de contenido en el panel Braze:
- [Tarjetas de contenido como contenido complementario](#content-cards-as-supplemental-content)
- [Tarjetas de contenido en un centro de mensajes](#content-cards-in-a-message-center)
- [Tarjetas interactivas de contenido](#interactive-content-cards)

### Tarjetas de contenido como contenido complementario

![]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Puedes integrar fácilmente las tarjetas de contenido en una fuente existente, permitiendo que los datos de varias fuentes se carguen simultáneamente. Esto crea una experiencia cohesiva y armoniosa con las tarjetas de contenido Braze y el contenido de la fuente existente.

El ejemplo de la derecha muestra un `UICollectionView` con una lista híbrida de elementos que se rellenan mediante datos locales y tarjetas de contenido impulsadas por Braze. Con esto, las tarjetas de contenido pueden ser indistinguibles de los contenidos existentes.

#### Configuración del panel de control

Esta tarjeta de contenido se entrega mediante una campaña desencadenada por API con pares clave-valor desencadenados por API. Esto es ideal para campañas en las que los valores de la tarjeta dependen de factores externos para determinar qué contenido mostrar al usuario. Ten en cuenta que `class_type` debe conocerse en el momento de la configuración.

![Los pares clave-valor para el caso de uso de las tarjetas de contenido suplementario. En este ejemplo, diferentes aspectos de la tarjeta como "tile_id", "tile_deeplink" y "tile_title" se configuran utilizando Liquid.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

##### ¿Listo para el análisis de registros?
Visita la [sección siguiente](#logging-impressions-clicks-and-dismissals) para comprender mejor cómo debe ser el flujo de datos.

### Tarjetas de contenido en un centro de mensajes
<br>
Las tarjetas de contenido pueden utilizarse en un formato de centro de mensajes en el que cada mensaje es su propia tarjeta. Cada mensaje del centro de mensajes se rellena mediante una carga útil de tarjeta de contenido, y cada tarjeta contiene pares clave-valor adicionales que potencian la UI/UX al hacer clic. En el siguiente ejemplo, un mensaje te dirige a una vista personalizada arbitraria, mientras que otro se abre en una vista web que muestra HTML personalizado.

![]({% image_buster /assets/img/cc_implementation/message_center.png %}){: style="border:0;"}{: style="max-width:80%;border:0"}

#### Configuración del panel de control

Para los siguientes tipos de mensaje, el par clave-valor `class_type` debe añadirse a la configuración de tu panel. Los valores asignados aquí son arbitrarios, pero deben poder distinguirse entre tipos de clases. Estos pares clave-valor son los identificadores clave en los que se fija la aplicación para decidir a dónde ir cuando el usuario hace clic en un mensaje de buzón de entrada abreviado.

{% tabs local %}
{% tab Mensaje personalizado arbitrario - página completa %}

Los pares clave-valor para este caso de uso incluyen:

- `message_header` configurado como `Full Page`
- `class_type` configurado como `message_full_page`

![]({% image_buster /assets/img/cc_implementation/full_page.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Mensaje Webview - HTML %}

Los pares clave-valor para este caso de uso incluyen:

- `message_header` configurado como `HTML`
- `class_type` configurado como `message_webview`
- `message_title`

Este mensaje también busca un par clave-valor HTML, pero si trabajas con un dominio Web, también es válido un par clave-valor URL.

![]({% image_buster /assets/img/cc_implementation/html_webview.png %}){: style="max-width:60%;"}

{% endtab %}
{% endtabs %}

#### Más explicaciones

La lógica del centro de mensajes se rige por la dirección `contentCardClassType` que proporcionan los pares clave-valor de Braze. Con el método `addContentCardToView` puedes filtrar e identificar estos tipos de clases.

{% tabs %}
{% tab Swift %}
**Utilizando `class_type` para el comportamiento al hacer clic**<br>
Cuando se hace clic en un mensaje, `ContentCardClassType` gestiona cómo debe rellenarse la siguiente pantalla.
```swift
func addContentCardToView(with message: Message) {
    switch message.contentCardData?.contentCardClassType {
      case .message(.fullPage):
        loadContentCardFullPageView(with: message as! FullPageMessage)
      case .message(.webView):
        loadContentCardWebView(with: message as! WebViewMessage)
      default:
        break
    }
}
```
{% endtab %}
{% tab Objective-C %}
**Utilizando `class_type` para el comportamiento al hacer clic**<br>
Cuando se hace clic en un mensaje, `ContentCardClassType` gestiona cómo debe rellenarse la siguiente pantalla.
```objc
- (void)addContentCardToView:(Message *)message {
  switch (message.contentCardData.classType) {
    case ContentCardClassTypeMessageFullPage:
      [self loadContentCardFullPageView:(FullPageMessage *)message];
      break;
    case ContentCardClassTypeMessageWebview:
      [self loadContentCardWebView:(WebViewMessage *)message];
      break;
    default:
      break;
  }
}
```
{% endtab %}
{% endtabs %}

##### ¿Listo para el análisis de registros?
Visita la [sección siguiente](#logging-impressions-clicks-and-dismissals) para comprender mejor cómo debe ser el flujo de datos.

![En la esquina inferior izquierda de la pantalla aparece una tarjeta de contenido interactiva que muestra una promoción del 50%. Después de hacer clic, se aplicará una promoción al carrito.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"} 

### Tarjetas interactivas de contenido
<br>
Las tarjetas de contenido pueden aprovecharse para crear experiencias dinámicas e interactivas para tus usuarios. En el ejemplo de la derecha, tenemos una ventana emergente de una tarjeta de contenido que aparece en el momento de la compra y que ofrece a los usuarios promociones de última hora. 

Las tarjetas bien colocadas como ésta son una forma estupenda de dar a los usuarios un "empujoncito" hacia acciones específicas del usuario.
<br><br><br>
#### Configuración del panel de control

La configuración del panel para las tarjetas de contenido interactivas es sencilla. Los pares clave-valor para este caso de uso incluyen un `discount_percentage` configurado como el importe de descuento deseado y `class_type` configurado como `coupon_code`. Estos pares clave-valor son la forma en que se filtran las tarjetas de contenido específicas de cada tipo y se muestran en la pantalla de pago.

![]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:70%;"} 

##### ¿Listo para el análisis de registros?
Visita la [sección siguiente](#logging-impressions-clicks-and-dismissals) para comprender mejor cómo debe ser el flujo de datos.

## Personalización del modo oscuro

Por predeterminado, las vistas de la tarjeta de contenido responderán automáticamente a los cambios del modo oscuro en el dispositivo con un conjunto de colores temáticos.

Este comportamiento puede anularse como se detalla en nuestra [guía de estilo personalizado]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/customization/custom_styling#disabling-dark-mode).

## Registro de impresiones, clics y rechazos

Tras ampliar tus objetos personalizados para que funcionen como tarjetas de contenido, el registro de métricas valiosas como impresiones, clics y rechazos es rápido. Esto puede hacerse utilizando un protocolo `ContentCardable` que haga referencia y proporcione datos a un archivo de ayuda para que sea registrado por el SDK de Braze.

#### Componentes de aplicación<br><br>

{% tabs %}
{% tab Swift %}
**Análisis de registros**<br>
Los métodos de registro pueden llamarse directamente desde objetos que cumplan el protocolo `ContentCardable`.
```swift
customObject.logContentCardImpression()
customObject.logContentCardClicked()
customObject.logContentCardDismissed()
```

**Recuperar el `ABKContentCard`**<br>
El `idString` pasado desde tu objeto personalizado se utiliza para identificar la tarjeta de contenido asociada a los análisis de registro.

```swift
extension BrazeManager {
  func logContentCardImpression(idString: String?) {
    guard let contentCard = getContentCard(forString: idString) else { return }
 
    contentCard.logContentCardImpression()
  }
   
  private func getContentCard(forString idString: String?) -> ABKContentCard? {
    return contentCards?.first(where: { $0.idString == idString })
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Análisis de registros**<br>
Los métodos de registro pueden llamarse directamente desde objetos que cumplan el protocolo `ContentCardable`.
```objc
[customObject logContentCardImpression];
[customObject logContentCardClicked];
[customObject logContentCardDismissed];
```

**Recuperar el `ABKContentCard`**<br>
El `idString` pasado desde tu objeto personalizado se utiliza para identificar la tarjeta de contenido asociada a los análisis de registro.

```objc
- (void)logContentCardImpression:(NSString *)idString {
  ABKContentCard *contentCard = [self getContentCard:idString];
  [contentCard logContentCardImpression];
}
 
- (ABKContentCard *)getContentCard:(NSString *)idString {
  NSPredicate *predicate = [NSPredicate predicateWithFormat:@"self.idString == %@", idString];
  NSArray *filteredArray = [self.contentCards filteredArrayUsingPredicate:predicate];
 
  return filteredArray.firstObject;
}
```
{% endtab %}
{% endtabs %}

{% alert important %}
Para una variante de control Tarjeta de contenido, aún debe instanciarse un objeto personalizado, y la lógica de la interfaz de usuario debe establecer la vista correspondiente del objeto como oculta. El objeto puede entonces registrar una impresión para informar a nuestro análisis de cuándo un usuario habría visto la tarjeta de control.
{% endalert %}

## Archivos de ayuda

{% details Archivo de ayuda ContentCardKey %}
{% tabs %}
{% tab Swift %}
```swift
enum ContentCardKey: String {
  case idString
  case created
  case classType = "class_type"
  case dismissible
  case extras
  ...
}
```
{% endtab %}
{% tab Objective-C %}
```objc
static NSString *const ContentCardKeyIdString = @"idString";
static NSString *const ContentCardKeyCreated = @"created";
static NSString *const ContentCardKeyClassType = @"class_type";
static NSString *const ContentCardKeyDismissible = @"dismissible";
static NSString *const ContentCardKeyExtras = @"extras";
...
```
{% endtab %}
{% endtabs %}
{% enddetails %}

