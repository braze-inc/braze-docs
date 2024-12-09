---
nav_title: Implementação avançada (opcional)
article_title: Guia de implementação do cartão de conteúdo para iOS (opcional) 
platform: iOS
page_order: 7
description: "Este guia de implementação avançada aborda considerações sobre o código do cartão de conteúdo do iOS, três casos de uso criados por nossa equipe, acompanhando trechos de código e orientações sobre o registro de impressões, cliques e descartes de cartão."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

<br>
{% alert important %}
Está procurando o guia básico de integração do desenvolvedor do cartão de conteúdo? Encontre-o [aqui]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration/).
{% endalert %}

# Guia de implementação do cartão de conteúdo

> Este guia de implementação opcional e avançado aborda considerações sobre o código do Content Card, três casos de uso personalizados criados por nossa equipe, acompanhando trechos de código e orientações sobre o registro de impressões, cliques e descartes de cartão. Visite nosso Repositório de Demonstrações Braze [aqui](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Note que este guia de implementação está centrado em uma implementação Swift, mas são fornecidos trechos em Objective C para os interessados.

## Considerações sobre o código

### Cartões de conteúdo como objetos personalizados

Assim como um foguete que adiciona um impulsionador, seus próprios objetos personalizados podem ser estendidos para funcionar como cartões de conteúdo. Superfícies limitadas de API como essa oferecem flexibilidade para trabalhar com diferentes back-ends de dados de forma intercambiável. Isso pode ser feito em conformidade com o protocolo `ContentCardable` e implementando o inicializador (como visto nos trechos de código a seguir) e, por meio do uso da estrutura `ContentCardData`, permite acessar os dados `ABKContentCard`. A carga útil `ABKContentCard` será usada para inicializar a estrutura `ContentCardData` e o próprio objeto personalizado, tudo a partir de um tipo `Dictionary` por meio do inicializador fornecido com o protocolo.

O inicializador também inclui um enum `ContentCardClassType`. Esse enum é usado para decidir qual objeto será inicializado. Por meio do uso de pares chave-valor no dashboard da Braze, você pode definir uma chave `class_type` explícita que será usada para determinar qual objeto será inicializado. Esses pares de valores-chave para os cartões de conteúdo são exibidos na variável `extras` no site `ABKContentCard`. Outro componente central do inicializador é o parâmetro do dicionário `metaData`. O `metaData` inclui tudo do `ABKContentCard` analisado em uma série de chaves e valores. Depois que os cartões relevantes forem analisados e convertidos em seus objetos personalizados, o app estará pronto para começar a trabalhar com eles como se tivessem sido instanciados a partir do JSON ou de qualquer outra fonte. 

Depois de entender bem essas considerações de código, confira nossos [casos de uso](#sample-use-cases) para começar a implementar seus objetos personalizados.

{% tabs localização %}
{% tab ContentCardable %}
{% subtabs global %}
{% subtab Swift %}
**Protocolo ContentCardable**<br>
Um objeto `ContentCardData` que representa os dados `ABKContentCard` junto com um enum `ContentCardClassType`. Um inicializador usado para instanciar objetos personalizados com metadados do `ABKContentCard`.
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
**Estrutura de dados do cartão de conteúdo**<br>
`ContentCardData` representa os valores analisados de um `ABKContentCard`.

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
Um objeto `ContentCardData` que representa os dados `ABKContentCard` juntamente com um `ContentCardClassType` enum, um inicializador usado para instanciar objetos personalizados com metadados `ABKContentCard`.
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
**Estrutura de dados do cartão de conteúdo**<br>
`ContentCardData` representa os valores analisados de um `ABKContentCard`.

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
**Inicializador de objeto personalizado**<br>
Os metadados de um `ABKContentCard` são usados para preencher as variáveis do seu objeto. Os pares de valores-chave configurados no dashboard do Braze são representados no dicionário "extras".

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

**Identificação de tipos**<br>
O enum `ContentCardClassType` representa o valor `class_type` no dashboard da Braze. Esse valor também é usado como um identificador de filtro para exibir os cartões de conteúdo em lugares diferentes. 

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
**Inicializador de objeto personalizado**<br>
Os metadados de um `ABKContentCard` são usados para preencher as variáveis do seu objeto. Os pares de valores-chave configurados no dashboard do Braze são representados no dicionário "extras".


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

**Identificação de tipos**<br>
O enum `ContentCardClassType` representa o valor `class_type` no dashboard da Braze. Esse valor também é usado como um identificador de filtro para exibir os cartões de conteúdo em lugares diferentes. 

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

{% tab Manuseio de cartões de conteúdo %}
{% subtabs global %}
{% subtab Swift %}
**Solicitação de cartões de conteúdo**<br>
Desde que o observador ainda esteja retido na memória, o retorno de chamada de notificação do SDK da Braze pode ser esperado.

```swift
func loadContentCards() {
  BrazeManager.shared.addObserverForContentCards(observer: self, selector: #selector(contentCardsUpdated))
  BrazeManager.shared.requestContentCardsRefresh()
}
```

**Manipulação do retorno de chamada do SDK dos cartões de conteúdo**<br>
Encaminhe o retorno de chamada da notificação para o arquivo auxiliar para analisar os dados de carga útil de seu(s) objeto(s) personalizado(s).
```swift
@objc func contentCardsUpdated(_ notification: Notification) {
  guard let contentCards = BrazeManager.shared.handleContentCardsUpdated(notification, for: [.yourValue]) as? [CustomObject],!contentCards.isEmpty else { return }
 
 // do something with your array of custom objects
}
```

**Trabalhando com cartões de conteúdo**<br>
O `class_type` é passado como um filtro para retornar apenas os cartões de conteúdo que tenham um `class_type` correspondente.

```swift
func handleContentCardsUpdated(_ notification: Notification, for classTypes: [ContentCardClassType]) -> [ContentCardable] {
  guard let updateIsSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool, updateIsSuccessful, let cards = contentCards else { return [] }
             
  return convertContentCards(cards, for: classTypes)
}
```
{% endsubtab %}
{% subtab Objective-C %}
**Solicitação de cartões de conteúdo**<br>
Desde que o observador ainda esteja retido na memória, o retorno de chamada de notificação do SDK da Braze pode ser esperado.

```objc
- (void)loadContentCards {
  [[BrazeManager shared] addObserverForContentCards:self selector:@selector(contentCardsUpdated:)];
  [[BrazeManager shared] requestContentCardsRefresh];
}
```

**Manipulação do retorno de chamada do SDK dos cartões de conteúdo**<br>
Encaminhe o retorno de chamada da notificação para o arquivo auxiliar para analisar os dados de carga útil de seu(s) objeto(s) personalizado(s).
```objc
- (void)contentCardsUpdated:(NSNotification *)notification {
  NSArray *classTypes = @[@(ContentCardClassTypeYourValue)];
  NSArray *contentCards = [[BrazeManager shared] handleContentCardsUpdated:notification forClassTypes:classTypes];
 
  // do something with your array of custom objects
}
```

**Trabalhando com cartões de conteúdo**<br>
O `class_type` é passado como um filtro para retornar apenas os cartões de conteúdo que tenham um `class_type` correspondente.

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

{% tab Trabalhando com dados de carga útil %}
{% subtabs global %}
{% subtab Swift %}
**Trabalho com dados de carga útil**<br>
Percorre a matriz de cartões de conteúdo e analisa apenas os cartões com uma correspondência `class_type`. A carga útil de um ABKContentCard é analisada em um `Dictionary`.

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

**Inicialização de seus objetos personalizados a partir dos dados da carga útil do Content Card**<br>
O endereço `class_type` é usado para determinar quais de seus objetos personalizados serão inicializados a partir dos dados da carga útil.

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
**Trabalho com dados de carga útil**<br>
Percorre a matriz de cartões de conteúdo e analisa apenas os cartões com uma correspondência `class_type`. A carga útil de um ABKContentCard é analisada em um `Dictionary`.

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

**Inicialização de seus objetos personalizados a partir dos dados da carga útil do Content Card**<br>
O endereço `class_type` é usado para determinar quais de seus objetos personalizados serão inicializados a partir dos dados da carga útil.

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

## Casos de uso

Fornecemos três casos de uso abaixo. Cada caso de uso oferece uma explicação detalhada, trechos de código relevantes e uma visão de como as variáveis do cartão de conteúdo podem parecer e ser usadas no dashboard do Braze:
- [Cartões de conteúdo como conteúdo suplementar](#content-cards-as-supplemental-content)
- [Cartões de conteúdo em um centro de mensagens](#content-cards-in-a-message-center)
- [Cartões de conteúdo interativo](#interactive-content-cards)

### Cartões de conteúdo como conteúdo suplementar

![]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Você pode combinar perfeitamente os cartões de conteúdo em um feed existente, permitindo que os dados de vários feeds sejam carregados simultaneamente. Isso cria uma experiência coesa e harmoniosa com os cartões de conteúdo Braze e o conteúdo de feed existente.

O exemplo à direita mostra um site `UICollectionView` com uma lista híbrida de itens que são preenchidos por meio de dados de localização e cartões de conteúdo fornecidos pela Braze. Com isso, os cartões de conteúdo podem ser indistinguíveis do conteúdo existente.

#### Configuração do dashboard

Esse cartão de conteúdo é entregue por uma campanha disparada por API com pares de chave-valor disparados por API. Isso é ideal para campanhas em que os valores do cartão dependem de fatores externos para determinar o conteúdo a ser exibido ao usuário. Note que `class_type` deve ser conhecido no momento da configuração.

![Os pares de valores-chave para o caso de uso de cartões de conteúdo suplementar. Neste exemplo, diferentes aspectos do cartão, como "tile_id", "tile_deeplink" e "tile_title", são definidos usando o Liquid.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

##### Pronto para fazer a análise de dados?
Visite a [seção a seguir](#logging-impressions-clicks-and-dismissals) para entender melhor como deve ser o fluxo de dados.

### Cartões de conteúdo em um centro de mensagens
<br>
Os cartões de conteúdo podem ser usados em um formato de centro de mensagens em que cada mensagem é seu próprio cartão. Cada mensagem no centro de mensagens é preenchida por meio de uma carga útil de um cartão de conteúdo, e cada cartão contém pares de valores-chave adicionais que potencializam a UI/UX no clique. No exemplo a seguir, uma mensagem o direciona para uma visualização personalizada arbitrária, enquanto outra abre para uma visualização da Web que exibe HTML personalizado.

![]({% image_buster /assets/img/cc_implementation/message_center.png %}){: style="border:0;"}{: style="max-width:80%;border:0"}

#### Configuração do dashboard

Para os seguintes tipos de mensagens, o par chave-valor `class_type` deve ser adicionado à configuração de seu dashboard. Os valores atribuídos aqui são arbitrários, mas devem ser distinguíveis entre os tipos de classe. Esses pares de valores de chave são os identificadores de chave que o aplicativo examina ao decidir para onde ir quando o usuário clica em uma mensagem de caixa de entrada resumida.

{% tabs local %}
{% tab Mensagem de visualização personalizada arbitrária - página inteira %}

Os pares de valores-chave para esse caso de uso incluem:

- `message_header` definido como `Full Page`
- `class_type` definido como `message_full_page`

![]({% image_buster /assets/img/cc_implementation/full_page.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Mensagem do Webview - HTML %}

Os pares de valores-chave para esse caso de uso incluem:

- `message_header` definido como `HTML`
- `class_type` definido como `message_webview`
- `message_title`

Essa mensagem também procura um par chave-valor HTML, mas se estiver trabalhando com um domínio da Internet, um par chave-valor URL também é válido.

![]({% image_buster /assets/img/cc_implementation/html_webview.png %}){: style="max-width:60%;"}

{% endtab %}
{% endtabs %}

#### Explicação adicional

A lógica do centro de mensagens é orientada pelo site `contentCardClassType`, que é fornecido pelos pares de valores-chave da Braze. Usando o método `addContentCardToView`, você pode filtrar e identificar esses tipos de classe.

{% tabs %}
{% tab Rápido %}
**Usando `class_type` para comportamento ao clicar**<br>
Quando uma mensagem é clicada, o site `ContentCardClassType` trata de como a próxima tela deve ser preenchida.
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
{% tab Objective C %}
**Usando `class_type` para comportamento ao clicar**<br>
Quando uma mensagem é clicada, o site `ContentCardClassType` trata de como a próxima tela deve ser preenchida.
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

##### Pronto para fazer a análise de dados?
Visite a [seção a seguir](#logging-impressions-clicks-and-dismissals) para entender melhor como deve ser o fluxo de dados.

![Um cartão de conteúdo interativo mostrando uma promoção de 50% aparece no canto inferior esquerdo da tela. Após ser clicado, uma promoção será aplicada ao carrinho.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"} 

### Cartões de conteúdo interativo
<br>
Os cartões de conteúdo podem ser aproveitados para criar experiências dinâmicas e interativas para seus usuários. No exemplo à direita, temos um pop-up de cartão de conteúdo que aparece no checkout, oferecendo aos usuários promoções de última hora. 

Cartões bem posicionados como esse são uma ótima maneira de dar aos usuários um "empurrãozinho" em direção a ações específicas.
<br><br><br>
#### Configuração do dashboard

A configuração do dashboard para cartões de conteúdo interativos é simples. Os pares de valores-chave para esse caso de uso incluem `discount_percentage` definido como o valor do desconto desejado e `class_type` definido como `coupon_code`. Esses pares de valores-chave são como os cartões de conteúdo específicos do tipo são filtrados e exibidos na tela de checkout.

![]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:70%;"} 

##### Pronto para fazer a análise de dados?
Visite a [seção a seguir](#logging-impressions-clicks-and-dismissals) para entender melhor como deve ser o fluxo de dados.

## Personalização do modo escuro

Por padrão, as exibições do cartão de conteúdo responderão automaticamente às alterações do modo escuro no dispositivo com um conjunto de cores temáticas.

Esse comportamento pode ser substituído conforme detalhado em nosso [guia de estilo personalizado]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/customization/custom_styling#disabling-dark-mode).

## Registro de impressões, cliques e demissões

Depois de estender seus objetos personalizados para funcionarem como cartões de conteúdo, o registro de métricas valiosas, como impressões, cliques e descartes de cartões, é rápido. Isso pode ser feito usando um protocolo `ContentCardable` que faz referência e fornece dados a um arquivo auxiliar a ser registrado pelo SDK da Braze.

#### Componentes de implementação<br><br>

{% tabs %}
{% tab Rápido %}
**Análise de dados de registro**<br>
Os métodos de registro podem ser chamados diretamente de objetos em conformidade com o protocolo `ContentCardable`.
```swift
customObject.logContentCardImpression()
customObject.logContentCardClicked()
customObject.logContentCardDismissed()
```

**Recuperação do `ABKContentCard`**<br>
O `idString` passado do seu objeto personalizado é usado para identificar o cartão de conteúdo associado para análise de dados.

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
{% tab Objective C %}
**Análise de dados de registro**<br>
Os métodos de registro podem ser chamados diretamente de objetos em conformidade com o protocolo `ContentCardable`.
```objc
[customObject logContentCardImpression];
[customObject logContentCardClicked];
[customObject logContentCardDismissed];
```

**Recuperação do `ABKContentCard`**<br>
O `idString` passado do seu objeto personalizado é usado para identificar o cartão de conteúdo associado para análise de dados.

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
Para uma variante de controle Content Card, um objeto personalizado ainda deve ser instanciado, e a lógica da interface do usuário deve definir a exibição correspondente do objeto como oculta. O objeto pode então registrar uma impressão para informar nossa análise de dados sobre quando um usuário teria visto o cartão de controle.
{% endalert %}

## Arquivos auxiliares

{% details Arquivo auxiliar ContentCardKey %}
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
{% tab Objective C %}
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

