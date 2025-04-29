---
nav_title: Personalizando feed
article_title: Personalizando o feed do cartão de conteúdo para iOS
platform: iOS
page_order: 2
description: "Este artigo cobre as opções de personalização do feed do cartão de conteúdo no seu aplicativo iOS."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Personalizando o feed dos Cartões de Conteúdo

Você pode criar sua própria interface de Cartões de Conteúdo estendendo `ABKContentCardsTableViewController` para personalizar todos os elementos da interface do usuário e o comportamento dos Cartões de Conteúdo. As células do cartão de conteúdo também podem ser subclassificadas e, em seguida, usadas programaticamente ou introduzindo um storyboard personalizado que registra as novas classes. Confira o [app de exemplo](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp) de Cartões de Conteúdo para um exemplo completo. 

Também é importante considerar se você deve usar uma estratégia de subclasse versus um controlador de visualização completamente personalizado e [inscrever-se para atualizações de dados]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration/). Por exemplo, se você criar uma subclasse do `ABKContentCardsTableViewController`, pode usar o método [`populateContentCards`](#overriding-populated-content-cards) para filtrar e ordenar cartões (recomendado). No entanto, se você usar uma personalização completa do controlador de visualização, terá mais controle sobre o comportamento do cartão—como exibir em um carrossel ou adicionar elementos interativos—mas, então, terá que contar com um observador para implementar a lógica de ordenação e filtragem. Você também deve implementar os respectivos métodos de análise de dados para registrar adequadamente as impressões, eventos de rejeição e cliques.

## Personalizando a IU

Os trechos de código a seguir mostram como estilizar e alterar os Cartões de Conteúdo para atender às suas necessidades de interface do usuário usando métodos fornecidos pelo SDK. Esses métodos permitem que você personalize todos os aspectos da UI do cartão de conteúdo, incluindo fontes personalizadas, componentes de cores personalizadas, texto personalizado e mais. 

Existem duas maneiras distintas de personalizar a interface do usuário do cartão de conteúdo: 
- Método dinâmico: atualizar a interface do usuário do cartão em uma base por cartão
- Método estático: atualizar a interface do usuário em todos os cartões

### Interface dinâmica

O método cartão de conteúdo `applyCard` pode referenciar o objeto cartão e passar pares chave-valor que serão usados para atualizar a interface do usuário:

{% tabs %}
{% tab Objective C %}
```objc
- (void)applyCard:(ABKCaptionedImageContentCard *)captionedImageCard {
  [super applyCard:captionedImageCard];    
 
  if ([card.extras objectForKey:ContentCardKeyBackgroundColorValue]) {
    NSString *backgroundColor = [card.extras objectForKey:ContentCardKeyBackgroundColor];
    if ([backgroundColor colorValue]) {
      self.rootView.backgroundColor = [backgroundColor colorValue];
    } else {
      self.rootView.backgroundColor = [UIColor lightGray];
    }
  } else {
    self.rootView.backgroundColor = [UIColor lightGray];
  }  
}
```
{% endtab %}
{% tab Swift %}
```swift
override func apply(_ captionedImageCard: ABKCaptionedImageContentCard!) {
  super.apply(captionedImageCard)         
 
  if let backgroundColor = card.extras?[ContentCardKey.backgroundColor.rawValue] as? String,
     let backgroundColorValue = backgroundColor.colorValue() {
    rootView.backgroundColor = backgroundColorValue
  } else {
    rootView.backgroundColor = .lightGray
  }
}
```
{% endtab %}
{% endtabs %}

### Interface de Usuário Estática

O método `setUpUI` pode atribuir valores aos componentes estáticos do cartão de conteúdo em todos os cartões:

{% tabs %}
{% tab Objective C %}
```objc
#import "CustomClassicContentCardCell.h"  
 
@implementation CustomClassicContentCardCell
 
- (void)setUpUI {
  [super setUpUI];
  self.rootView.backgroundColor = [UIColor lightGrayColor];
  self.rootView.layer.borderColor = [UIColor purpleColor].CGColor;
  self.unviewedLineView.backgroundColor = [UIColor redColor];
  self.titleLabel.font = [UIFont italicSystemFontOfSize:20];
}
```
{% endtab %}
{% tab Swift %}
```swift
override func setUpUI() {
  super.setUpUI()
     
  rootView.backgroundColor = .lightGray
  rootView.layer.borderColor = UIColor.purple.cgColor
  unviewedLineViewColor = .red
  titleLabel.font = .italicSystemFont(ofSize: 20)
}
```
{% endtab %}
{% endtabs %}

## Fornecendo interfaces personalizadas

Interfaces personalizadas podem ser fornecidas registrando classes personalizadas para cada tipo de cartão desejado. 

![Um cartão de conteúdo de banner. Um cartão de conteúdo de banner mostra uma imagem à direita do banner com o texto "Agradecemos por baixar a versão de demonstração da Braze!".]({% image_buster /assets/img/interface1.png %}){: style="max-width:35%;margin-left:15px;"}
![Um cartão de conteúdo de imagem legendada. Um cartão de conteúdo legendado mostra uma imagem da Braze com a legenda sobreposta na parte inferior "Agradecemos por baixar a versão de demonstração da Braze!". ]({% image_buster /assets/img/interface2.png %}){: style="max-width:25%;margin-left:15px;"}
![Um cartão de conteúdo clássico. Um cartão de conteúdo clássico mostra uma imagem no centro do cartão com as palavras "Obrigado por baixar o Braze Demo" abaixo.]({% image_buster /assets/img/interface3.png %}){: style="max-width:18%;margin-left:15px;"}

Braze fornece três modelos de cartão de conteúdo (banner, imagem legendada e clássico). Como alternativa, se você quiser fornecer suas próprias interfaces personalizadas, consulte os seguintes trechos de código:

{% tabs %}
{% tab Objective C %}
```objc
- (void)registerTableViewCellClasses {
  [super registerTableViewCellClasses];
 
  // Replace the default class registrations with custom classes for these two types of cards
  [self.tableView registerClass:[CustomCaptionedImageContentCardCell class] forCellReuseIdentifier:@"ABKCaptionedImageContentCardCell"];
  [self.tableView registerClass:[CustomClassicContentCardCell class] forCellReuseIdentifier:@"ABKClassicCardCell"];
}
```
{% endtab %}
{% tab Swift %}
```swift
override func registerTableViewCellClasses() {
  super.registerTableViewCellClasses()
     
  // Replace the default class registrations with custom classes
  tableView.register(CustomCaptionedImageContentCardCell.self, forCellReuseIdentifier: "ABKCaptionedImageContentCardCell")
  tableView.register(CustomBannerContentCardCell.self, forCellReuseIdentifier: "ABKBannerContentCardCell")
  tableView.register(CustomClassicImageContentCardCell.self, forCellReuseIdentifier: "ABKClassicImageCardCell")
  tableView.register(CustomClassicContentCardCell.self, forCellReuseIdentifier: "ABKClassicCardCell")
}
```
{% endtab %}
{% endtabs %}

## Substituindo Cartões de Conteúdo Populados

Os Cartões de Conteúdo podem ser alterados programaticamente usando o método `populateContentCards`:

{% tabs %}
{% tab Objective C %}
```objc
- (void)populateContentCards {
  NSMutableArray<ABKContentCard *> *cards = [NSMutableArray arrayWithArray:[Appboy.sharedInstance.contentCardsController getContentCards]];
  for (ABKContentCard *card in cards) {
    // Replaces the card description for all Classic Content Cards
    if ([card isKindOfClass:[ABKClassicContentCard class]]) {
      ((ABKClassicContentCard *)card).cardDescription = @"Custom Feed Override title [classic cards only]!";
    }
  }
  super.cards = cards;
}
```
{% endtab %}
{% tab Swift %}
```swift
override func populateContentCards() {
  guard let cards = Appboy.sharedInstance()?.contentCardsController.contentCards else { return }
  for card in cards {
    // Replaces the card description for all Classic Content Cards
    if let classicCard = card as? ABKClassicContentCard {
      classicCard.cardDescription = "Custom Feed Override title [classic cards only]!"
    }
  }
  super.cards = (cards as NSArray).mutableCopy() as? NSMutableArray
}
```
{% endtab %}
{% endtabs %}