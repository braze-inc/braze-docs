---
nav_title: Implémentation avancée (facultatif)
article_title: Guide d'implémentation de la carte de contenu pour iOS (facultatif)
platform: iOS
page_order: 7
description: "Ce guide de mise en œuvre avancé couvre les considérations de code de la carte de contenu iOS, trois cas d'utilisation construits par notre équipe, accompagnant des extraits de code, et des conseils sur la journalisation des impressions, les clics et les licenciements."
channel:
  - cartes de contenu
---

{% alert important %}
Vous recherchez le guide d'intégration des développeurs de cartes de contenu ? Trouvez-le [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/data_model/).
{% endalert %}

# Guide d'implémentation de la carte de contenu

> Ce guide de mise en œuvre optionnel et avancé couvre les considérations de code de la carte de contenu, trois cas d'utilisation personnalisés construits par notre équipe, accompagnant des extraits de code, et des conseils sur la journalisation des impressions, les clics et les licenciements. Visitez notre Dépôt de Démo de Braze [ici](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Veuillez noter que ce guide de mise en œuvre est centré sur une implémentation Swift, mais des extraits Objective-C sont fournis pour ceux qui sont intéressés.

## Considérations de code

### Cartes de contenu en tant qu'objets personnalisés

Tout comme une fusée qui ajoute un booster, vos propres objets personnalisés peuvent être étendus pour fonctionner comme des cartes de contenu. Les surfaces limitées de l'API telles que celle-ci offrent une flexibilité pour travailler avec différents backends de données de manière interchangeable. Cela peut être fait en se conformant au protocole `ContentCardable` et en implémentant l'initialiseur (comme vu ci-dessous) et, par l'utilisation de la structure `ContentCardData` vous permet d'accéder aux données de `ABKContentCard`. Le bloc `ABKContentCard` sera utilisé pour initialiser la structure `ContentCardData` et l'objet personnalisé lui-même, le tout à partir d'un type `Dictionnaire` via l'initialiseur avec lequel le protocole est fourni.

L'initialiseur inclut également une énumération `ContentCardClassType`. Cette énumération est utilisée pour décider quel objet initialiser. Grâce à l'utilisation de paires clé-valeur dans le tableau de bord Braze, vous pouvez définir une clé explicite `class_type` qui sera utilisée pour déterminer l'objet à initialiser. Ces paires de valeurs clés pour les cartes de contenu arrivent dans la variable `extras` de la `ABKContentCard`. Un autre composant central de l'initialiseur est le paramètre de dictionnaire `metaData`. Les `metaData` incluent tout ce qui se trouve dans la `ABKContentCard` analysée en une série de clés et de valeurs. Une fois que les cartes pertinentes ont été analysées et converties en objets personnalisés, l'application est prête à commencer à travailler avec elle comme si elle était instanciée à partir de JSON ou de toute autre source.

Une fois que vous avez une bonne compréhension de ces considérations de code, consultez nos [cas d'utilisation](#sample-use-cases) ci-dessous pour commencer à implémenter vos objets personnalisés.

{% tabs local %}
{% tab ContentCardable %}
{% subtabs global %}
{% subtab Swift %}
__ContentCardable Protocol__<br> Un objet `ContentCardData` qui représente les données `ABKContentCard` avec une énumération `ContentCardClassType`. Un initialiseur utilisé pour instancier des objets personnalisés avec les métadonnées `ABKContentCard`.
```swift
protocol ContentCardable {
  var contentCardData: ContentCardData? { get }
  initiale? metaData : [ContentCardKey : Any], classType contentCardClassType: ContentCardClassType)
}

extension ContentCardable {
  var isContentCard: Bool {
    return contentCardData ! nil
  }

  func logContentCardClicked() {
    BrazeManager. hared.logContentCardClicked(idString: contentCardData?. ontentCardId)
  }

  func logContentCardDismissed() {
    BrazeManager.shared.logContentCardDismissed(idString: contentCardData?. ontentCardId)
  }

  func logContentCardImpression() {
    BrazeManager.shared.logContentCardImpression(idString: contentCardData?.contentCardId)
  }
}
```
__Content Card Data Struct__<br> `ContentCardData` représente les valeurs analysées d'une `ABKContentCard`.

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
__ContentCardable Protocol__<br> Un objet `ContentCardData` qui représente les données `ABKContentCard` avec une énumération `ContentCardClassType` un initialiseur utilisé pour instancier des objets personnalisés avec les métadonnées `ABKContentCard`.
```objc
@protocol ContentCardable <NSObject>

@property (non-atomic, fort) ContentCardData *contentCardData ;
- (instancetype __nullable)initWithMetaData:(NSDictionary *)metaData
                                  classType:(enum ContentCardClassType)classType ;

- (BOOL)isContentCard ;
- (void)logContentCardImpression ;
- (void)logContentCardClick;
- (void)logContentCardDismissed;

@end
```
__Content Card Data Struct__<br> `ContentCardData` représente les valeurs analysées d'une `ABKContentCard`.

```objc
@interface ContentCardData : NSObject

+ (ContentCardClassType)contentCardClassTypeForString:(NSString *)rawValue;

- (instancetype)initWithIdString:(NSString *)idString
                       classType:(ContentCardClassType)classType
                       createdAt:(double)createdAt isDismissible:(BOOL)isDismissible;

@property (nonatomic, readonly) NSString *contentCardId;
@property (nonatomic) ContentCardClassType classType ;
@property (nonatomic, readonly) double *createdAt;
@property (nonatomic, readonly) BOOL isDismissible;
...
// autres propriétés de la carte de contenu telles que expiresAt, épinglé, etc.    

@end
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Custom Objects %}
{% subtabs global %}
{% subtab Swift %}
__Custom Object Initializer__<br> MetaData from an `ABKContentCard` is used to populate your object's variables. Les paires clé-valeur installées dans le tableau de bord Braze sont représentées dans le dictionnaire "extras".

```swift
Extension CustomObject: ContentCardable {
  init?(metaData: [ContentCardKey: Any], classType contentCardClassType: ContentCardClassType) {
    guard let idString = metaData[.idString] comme? String,
      let createdAt = metaData[.created] comme? Double,
      let isDismissable = metaData[.dismissable] en tant que ? Bool,
      let extras = metaData[.extras] comme? [AnyHashable: Any],
      else { return nil }

    let contentCardData = ContentCardData(contentCardId: idString, contentCardClassType: contentCardClassType, createdAt: createdAt, isDismissable: isDismissable)
    let customObjectProperty = extras["VOTRE-CLIENT-OBJECT-PROPERTY"] as? String

    self.init(contentCardData: contentCardData, property: customObjectProperty)
  }
}
```

__Identifying Types__<br> L'enum `ContentCardClassType` représente la valeur `class_type` dans le tableau de bord Braze. Cette valeur est également utilisée comme identifiant de filtre pour afficher les Cartes de Contenu à différents endroits.

```swift
enum ContentCardClassType: Hashable {
  case yourValue
  case yourOtherValue
...
  case none

  init(rawType: String?) {
    basculer rawType?. owercased() {
    case "your_value": // ces valeurs correspondent beaucoup à la valeur définie dans le tableau de bord de Braze
      self = . ourValue
    case "your_other_value": // ces valeurs correspondent beaucoup à la valeur définie dans le tableau de bord de Braze
      self = . ourOtherValue
...
    par défaut :
      self = .none
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
__Custom Object Initializer__<br> MetaData from an `ABKContentCard` is used to populate your object's variables. Les paires clé-valeur installées dans le tableau de bord Braze sont représentées dans le dictionnaire "extras".


```objc
- (id _Nullable)initWithMetaData:(nonnull NSDictionary *)metaData classType:(enum ContentCardClassType)classType {
  self = [super init];
  if (self) {
    if ([metaData objectForKey:ContentCardKeyIdString] && [metaData objectForKey:ContentCardKeyCreated] && [metaData objectForKey:ContentCardKeyDismissible] && [metaData objectForKey:ContentCardKeyExtras]) {
      NSDictionary *extras = metaData[ContentCardKeyExtras];
      NSString *idString = metaData[ContentCardKeyIdString];
      double createdAt = [metaData[ContentCardKeyCreated] doubleValue];
      BOOL isDismissible = metaData[ContentCardKeyDismissible];

      if ([extras objectForKey : @"VOTRE PROPRIÉTÉ DE CUSTOM")
        _customObjectProperty = extras[@"VOTRE PROPRIÉTA-OBJECT-OBJET"];

      soi. ontentCardData = [[ContentCardData alloc] initWithIdString:idString classType:classType createdAt:createdAt isDismissible:isDismissible];

      se remet à soi-même;
    }
  }
  Nil retour ;
}
```

__Identifying Types__<br> L'enum `ContentCardClassType` représente la valeur `class_type` dans le tableau de bord Braze. Cette valeur est également utilisée comme identifiant de filtre pour afficher les Cartes de Contenu à différents endroits.

```objc
typedef NS_ENUM(NSInteger, ContentCardClassType) {
  ContentCardClassTypeNone = 0,
  ContentCardClassTypeYourValue,
  ContentCardClassTypeYourOtherValue,
  ...
};

+ (NSArray *)contentCardClassTypeArray {
  return @[ @"", @"votre_valeur", @"votre_autre_valeur" ];
}

+ (ContentCardClassType)contentCardClassTypeForString:(NSString*)rawValue {
  if ([[self contentCardClassTypeArray] indexOfObject:rawValue] == NSNotFound) {
    return ContentCardClassTypeNone;
  } sinon {
    valeur NSInteger = [[self contentCardClassTypeArray] indexOfObject:rawValue] ;
    valeur de retour (ContentCardClassType) ;
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Handling Content Cards %}
{% subtabs global %}
{% subtab Swift %}
__Demander des Cartes de Contenu__<br> Tant que l'observateur est toujours en mémoire, le rappel de notification du Braze SDK peut être attendu.

```swift
func loadContentCards() {
  BrazeManager.shared.addObserverForContentCards(observer: self, selector: #selector(contentCardsUpdated))
  BrazeManager.shared.requestContentCardsRefresh()
}
```

__Manipulation des cartes de contenu SDK Callback__<br> Transférer la callback de notification vers le fichier d'aide pour analyser les données de la charge utile de vos objets personnalisés.
```swift
@objc func contentCardsUpdated(_ notification: Notification) {
  garde laisser contentCards = BrazeManager.shared.handleContentCardsUpdated(notification, pour: [.yourValue]) comme? [CustomObject],!contentCards.isEmpty else { return }

 // fait quelque chose avec votre table d'objets personnalisés
}
```

__Travailler avec des Cartes de Contenu__<br> Le `class_type` est passé comme un filtre pour ne renvoyer que les Cartes de Contenu qui ont un `class_type` correspondant.

```swift
func handleContentCardsUpdated(_ notification: Notification, pour les types de classe: [ContentCardClassType]) -> [ContentCardable] {
  garde let updateIsSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] comme? Bool, updateIsSuccessful, let cards = contentCards else { return [] }

  return convertContentCards(cards, for: classTypes)
}
```
{% endsubtab %}
{% subtab Objective-C %}
__Demander des Cartes de Contenu__<br> Tant que l'observateur est toujours en mémoire, le rappel de notification du Braze SDK peut être attendu.

```objc
- (void)loadContentCards {
  [[BrazeManager partagé] addObserverForContentCards:self selector:@selector(contentCardsUpdated:)];
  [[BrazeManager partagé] requestContentCardsRefresh];
}
```

__Manipulation des cartes de contenu SDK Callback__<br> Transférer la callback de notification vers le fichier d'aide pour analyser les données de la charge utile de vos objets personnalisés.
```objc
- ((void)contentCardsUpdated:(NSNotification *)notification {
  NSArray *classTypes = @[@(ContentCardClassTypeYourValue)];
  NSArray *contentCards = [[BrazeManager shared] handleContentCardsUpdated:notification forClassTypes:classTypes] ;

  // fait quelque chose avec votre table d'objets personnalisés
}
```

__Travailler avec des Cartes de Contenu__<br> Le `class_type` est passé comme un filtre pour ne renvoyer que les Cartes de Contenu qui ont un `class_type` correspondant.

```objc
- (NSArray *)handleContentCardsUpdated:(NSNotification *)notification forClassType:(ContentCardClassType)classType {  
  BOOL updateIsSuccessful = [notification. serInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue];
  if (updateIsSuccessful) {
    return [self convertContentCards:self. ontentCards forClassType:classType];
  } else {
    return @[];
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Working with Payload Data %}
{% subtabs global %}
{% subtab Swift %}
__Travailler avec Payload Data__<br> boucle à travers le tableau de Cartes de Contenu et n'analyse les cartes qu'avec un `class_type` correspondant. Le bloc d'une ABKContentCard est analysé dans un `Dictionnaire`.

```swift
func convertContentCards(_ cartes: [ABKContentCard], pour les types de classe : [ContentCardClassType]) -> [ContentCardable] {
  var contentCardables: [ContentCardable] = []

  pour les cartes {
    let classTypeString = card. xtras?[ContentCardKey.classType.rawValue] comme? String
    let classType = ContentCardClassType(rawType: classTypeString)
    garde classTypes. ontains(classType) else { continue }

    var metaData: [ContentCardKey: Any] = [:]
    switch card {
    case let banner as ABKBannerContentCard:
      metaData[.image] = banner. mage
    cas laissé sous-titré comme ABKCaptionedImageContentCard :
      metaData[.title] = sous-titré. itle
      metaData[.cardDescription] = sous-titrée.cardDescription
      metaData[.image] = sous-titré. mage
    boîtier classique comme ABKClassicContentCard :
      metaData[.title] = classique. itle
      metaData[.cardDescription] = classique. ardDescription
    par défaut :
      break
    }

    metaData[.idString] = carte. dString
    metaData[.created] = card.cre
    metaData[.dismissible] = card. ismisable
    metaData[.urlString] = carte. rlString
    metaData[.extras] = card.extras
...
    // autres propriétés de la carte de contenu telles que expiresAt, épinglé, etc.

    si laissez contentCardable = contentCardable(with: metaData, for: classType) {
      contentCardables. ppend(contentCardable)
    }
  }
  retourne contentCardables
}
```

__Initialisation de vos objets personnalisés à partir de données Payload de carte de contenu__<br> Le `class_type` est utilisé pour déterminer lequel de vos objets personnalisés sera initialisé à partir des données de la charge utile.

```swift
func contentCardable(with metaData: [ContentCardKey: Any], for classType: ContentCardClassType) -> ContentCardable? {
  switch classType {
  case .yourValue:
    return CustomObject(metaData: metaData, classType: classType)
  case .yourOtherValue:
    return OtherCustomObject(metaData: metaData, classType: classType)
...
  par défaut :
    return nil
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
__Travailler avec Payload Data__<br> boucle à travers le tableau de Cartes de Contenu et n'analyse les cartes qu'avec un `class_type` correspondant. Le bloc d'une ABKContentCard est analysé dans un `Dictionnaire`.

```objc
- (NSArray *)convertContentCardCards:(NSArray<ABKContentCard*> *)cards forClassType:(ContentCardClassType)classType {
  NSMutableArray *contentCardables = [[NSMutableArray alloc] init]; pour (ABKContentCard *carte en cartes) {
    NSString *classTypeString = [carte. xtras objectForKey:ContentCardKeyClassType] ;
    ContentCardClassType cardClassType = [ContentCardData contentCardClassTypeForString: classTypeString] ;
    if (cardClassType ! classType) { continue; }

    NSMutableDictionary *metaData = [[NSMutableDictionary alloc] init];
    if ([carte isKindOfClass:[classe ABKBannerContentCard]]) {
      ABKBannerContentCard *banner = (ABKBannerContentCard *)card;
      metaData[ContentCardKeyImage] = bannière. mage;
    } sinon if ([card isKindOfClass:[ABKCaptionedImageContentCard class]]) {
      ABKCaptionedImageContentCard *captioned = (ABKCaptionImageContentCard *)card;
      metaData[ContentCardKeyTitle] = sous-titré. itle;
      metaData[ContentCardKeyCardDescription] = sous-titré. ardDescription;
      metaData[ContentCardKeyImage] = sous-titré. mage;
    } sinon if ([card isKindOfClass:[ABKClassicContentCard class]]) {
      ABKClassicContentCard *classic = (ABKClassicContentCard *)card;
      metaData[ContentCardKeyCardDescription] = classique. itle;
      metaData[ContentCardKeyImage] = classique. mage;
    }

    metaData[ContentCardKeyIdString] = carte. dString;
    metaData[ContentCardKeyCreated] = [NSNumber numberWithDouble:card. reated];
    metaData[ContentCardKeyDismissible] = [NSNumber numberWithBool:card.dismissible];
    metaData[ContentCardKeyUrlString] = card. rlString;
    metaData[ContentCardKeyExtras] = card.extras;
...
    // autres propriétés de la carte de contenu telles que expiresAt, épinglé, etc.   

    id<ContentCardable> contentCardable = [self contentCardableWithMetaData:metaData forClassType:classType];
    if (contentCardable) {
      [contentCardables addObject:contentCardable];
    }
  }

  renvoyer les fiches de contenu ;
}
```

__Initialisation de vos objets personnalisés à partir de données Payload de carte de contenu__<br> Le `class_type` est utilisé pour déterminer lequel de vos objets personnalisés sera initialisé à partir des données de la charge utile.

```obj-c
- (id<ContentCardable>)contentCardableWithMetaData:(NSDictionary *)metaData forClassType:(ContentCardClassType)classType {
  switch (classType) {
    case ContentCardClassTypeYourValue:
      return [[CustomObject alloc] initWithMetaData:metaData classType:classType];
    case ContentCardClassTypeYourOtherValue:
      return nil;
...
    par défaut :
      return nil;
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exemple de cas d'utilisation

Il y a trois exemples de cas d'utilisation des clients fournis. Chaque cas d'utilisation offre une explication détaillée, des extraits de code pertinents, et voir comment les variables de la carte de contenu peuvent être utilisées dans le tableau de bord Braze :
- [Cartes de Contenu comme Contenu Supplémentaire](#content-cards-as-supplemental-content)
- [Cartes de contenu dans un centre de messages](#content-cards-in-a-message-center)
- [Cartes de contenu interactives](#interactive-content-cards)

### Cartes de contenu en tant que contenu complémentaire

!\[Supplementary Content PNG\]\[1\]{: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Vous pouvez combiner de façon transparente les cartes de contenu dans un flux existant, permettant aux données provenant de plusieurs flux de se charger simultanément. Cela crée une expérience cohésive et harmonieuse avec les cartes de contenu Braze et le contenu de flux existant.

L'exemple à droite montre un `UICollectionView` avec une liste hybride d'éléments qui sont remplis par des données locales et des cartes de contenu propulsées par Braze. Grâce à cela, les cartes de contenu peuvent être indissociables du contenu existant.

#### Configuration du tableau de bord

Cette carte de contenu est délivrée par une campagne déclenchée par l'API, avec des paires clé-valeur déclenchées par l'API. Ceci est idéal pour les campagnes où les valeurs de la carte dépendent de facteurs externes pour déterminer le contenu à afficher à l'utilisateur. Notez que `class_type` doit être connu lors de la configuration.

!\[Supplementary Content PNG\]\[2\]{: style="max-width:60%;"}

##### Prêt à enregistrer des analyses ?
Visitez la section [suivante](#logging-impressions-clicks-and-dismissals) pour mieux comprendre à quoi devrait ressembler le flux de données.

### Cartes de contenu dans un centre de messages
<br>
Les cartes de contenu peuvent être utilisées dans un format de centre de messages où chaque message est sa propre carte. Chaque message dans le centre de messages est rempli via une charge utile de la carte de contenu et chaque carte contient des paires de valeur clé supplémentaires qui allument l'UI/UX sur le clic. Dans l'exemple ci-dessous, un message vous dirige vers une vue personnalisée arbitraire, tandis qu'un autre s'ouvre sur un webview qui affiche du HTML personnalisé.

!\[Message Center PNG\]\[3\]{: style="border:0;"}{: style="max-width:80%;border:0"}

#### Configuration du tableau de bord

Pour les types de messages suivants, la paire clé-valeur `class_type` doit être ajoutée à la configuration de votre tableau de bord. Les valeurs assignées ici sont arbitraires, mais doivent être distinguées entre les types de classe. Ces paires de valeurs clés sont les identifiants clés que l'application regarde quand elle décide où aller lorsque l'utilisateur clique sur un message de boîte de réception abrégée.

| Message de vue personnalisée arbitraire (page pleine)                                                                                                                                                                                                                                  | Message Webview (HTML)                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Les paires clé-valeur pour ce cas d'utilisation incluent :<br><br>- `message_header` défini comme `Page Pleine`<br>- `class_type` défini comme `message_full_page`<br><br><br>! Centre de messages JPG1][4]{: style="largeur-max-100%;"} | Les paires clé-valeur pour ce cas d'utilisation incluent :<br><br>- `message_header` défini comme `HTML`<br>- `class_type` défini comme `message_webview`<br>- `message_title`<br><br>Ce message recherche également une paire clé-valeur HTML, mais si vous travaillez avec un domaine web, une paire clé-valeur d'URL est également valide.<br><br>!\[Message Center JPG2\]\[5\] |
{: .reset-td-br-1 .reset-td-br-2}

#### Explication supplémentaire

La logique du centre de messages est dictée par la `contentCardClassType` qui est fournie par les paires clé-valeur de Braze. En utilisant la méthode `addContentCardToView` , vous pouvez à la fois filtrer et identifier ces types de classe.

{% tabs %}
{% tab Swift %}
__En utilisant `class_type` pour On Click Behavior__<br> Quand un message est cliqué, le `ContentCardClassType` gère la façon dont l'écran suivant doit être rempli.
```swift
func addContentCardToView(avec message: Message) {
    switch message.contentCardData?.contentCardClassType {
      case .message(.fullPage):
        loadContentCardFullPageView(with: message as! FullPageMessage)
      case .message(.webView):
        loadContentCardWebView(with: message as! WebViewMessage)
      par défaut :
        break
    }
}
```
{% endtab %}
{% tab Objective-C %}
__En utilisant `class_type` pour On Click Behavior__<br> Quand un message est cliqué, le `ContentCardClassType` gère la façon dont l'écran suivant doit être rempli.
```objc
- (void)addContentCardToView:(Message *)message {
  switch (message.contentCardData. lassType) {
    case ContentCardClassTypeMessageFullPage:
      [self loadContentCardFullPageView:(FullPageMessage *)message];
      pause ;
    case ContentCardClassTypeMessageWebview:
      [self loadContentCardWebView:(WebViewMessage *)message];
      saut ;
    par défaut :
      pause ;
  }
}
```
{% endtab %}
{% endtabs %}

##### Prêt à enregistrer des analyses ?
Visitez la section [suivante](#logging-impressions-clicks-and-dismissals) pour mieux comprendre à quoi devrait ressembler le flux de données.

!\[Interactive Content PNG\]\[6\]{: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"}

### Cartes de contenu interactives
<br>
Les cartes de contenu peuvent être exploitées pour créer des expériences dynamiques et interactives pour vos utilisateurs. Dans l'exemple à droite, nous avons un pop-up de carte de contenu apparaît à la caisse fournissant aux utilisateurs des promotions de dernière minute.

De telles cartes bien placées sont un excellent moyen de donner aux utilisateurs un "coup de pouce" vers des actions spécifiques de l'utilisateur. <br><br><br>
#### Configuration du tableau de bord

La configuration du tableau de bord pour les cartes de contenu interactives est rapide et simple. Les paires clé-valeur pour ce cas d'utilisation incluent un `discount_percentage` défini comme le montant de la remise désirée et `class_type` défini comme `coupon_code`. Ces paires de valeurs clés sont la façon dont les cartes de contenu spécifiques à chaque type sont filtrées et affichées sur l'écran de paiement.

!\[Interactive Content JPG\]\[7\]{: style="max-width:70%;"}

##### Prêt à enregistrer des analyses ?
Visitez la section [suivante](#logging-impressions-clicks-and-dismissals) pour mieux comprendre à quoi devrait ressembler le flux de données.

## Logs d'impressions, de clics et de licenciements

Après avoir élargi vos objets personnalisés pour fonctionner comme des Cartes de Contenu, la journalisation de précieuses métriques comme des impressions, des clics et des licenciements est rapide et simple. Cela peut être fait par l'utilisation d'un protocole `ContentCardable` qui fait référence et fournit des données à un fichier d'aide qui sera enregistré par le Braze SDK.

#### __Composants d'implémentation__<br><br>

{% tabs %}
{% tab Swift %}
__Analyses de Logging__<br> Les méthodes de journalisation peuvent être appelées directement à partir d'objets conformes au protocole `ContentCardable`.
```swift
customObject.logContentCardImpression()
customObject.logContentCardClicked()
customObject.logContentCardDismissed()
```

__Retreiving the `ABKContentCard`__<br> The `idString` passed from your custom object is used to identify the associated Content Card to log analytics.

```swift
extension BrazeManager {
  func logContentCardImpression(idString: String?) {
    guard let contentCard = getContentCard(forString: idString) else { return }

    contentCard.logContentCardImpression()
  }

  private func getContentCard(forString idString: String?) -> ABKContentCard? {
    return contentCards?.first(where: { $0.idString == idString })
  }

```
{% endtab %}
{% tab Objective-C %}
__Analyses de Logging__<br> Les méthodes de journalisation peuvent être appelées directement à partir d'objets conformes au protocole `ContentCardable`.
```objc
[customObject logContentCardImpression];
[customObject logContentCardClicked];
[customObject logContentCardDismissed];
```

__Retreiving the `ABKContentCard`__<br> The `idString` passed from your custom object is used to identify the associated Content Card to log analytics.

```objc
- (void)logContentCardImpression:(NSString *)idString {
  ABKContentCard *contentCard = [self getContentCard:idString];
  [contentCard logContentCardImpression];
}

- (ABKContentCard *)getContentCard:(NSString *)idString {
  NSPredicate *predicate = [NSPredicate predicateWithFormat:@"self. dString == %@", idString];
  NSArray *filteredArray = [self.contentCards filteredArrayUsingPredicate:predicate];

  return filteredArray.firstObject;
}
```
{% endtab %}
{% endtabs %}

{% alert important %}
Pour une carte de contenu de variante de contrôle, un objet personnalisé devrait toujours être instancié, et la logique de l'interface utilisateur devrait définir la vue correspondante de l'objet comme masquée. L'objet peut alors enregistrer une impression pour informer nos analytiques de quand un utilisateur aurait vu la carte de contrôle.
{% endalert %}

## Fichiers d'aide

{% details ContentCardKey Helper File %}
{% tabs %}
{% tab Swift %}
```swift
enum ContentCardKey: String {
  case idString
  créée
  case classType = "class_type"
  casse dismissible
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
\[1]: {% image_buster /assets/img/cc_implementation/supplementary.png %} [2]: {% image_buster /assets/img/cc_implementation/supplementary_content. ng %} [3\]\[3\] : {% image_buster /assets/img/cc_implementation/message_center.png %} [4]: {% image_buster /assets/img/cc_implementation/full_page. ng %} [5]: {% image_buster /assets/img/cc_implementation/html_webview.png %} [6]: {% image_buster /assets/img/cc_implementation/discount2. ng %} [7]: {% image_buster /assets/img/cc_implementation/discount.png %}
