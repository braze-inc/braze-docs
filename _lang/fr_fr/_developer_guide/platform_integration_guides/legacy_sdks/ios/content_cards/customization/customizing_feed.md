---
nav_title: Personnaliser le flux
article_title: Personnalisation du flux de cartes de contenu pour iOS
platform: iOS
page_order: 2
description: "Cet article couvre les options de personnalisation du flux de cartes de contenu dans votre application iOS."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Personnalisation du flux des cartes de contenu

Vous pouvez créer votre propre interface de cartes de contenu en étendant le `ABKContentCardsTableViewController` pour personnaliser tous les éléments de l’interface utilisateur et le comportement des cartes de contenu. Les cellules de la carte de contenu peuvent également être sous-classées puis utilisées par programmation ou en introduisant un storyboard personnalisé qui enregistre les nouvelles classes. Consultez l'[exemple d'application](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp) Cartes de contenu pour un exemple complet. 

Il est également important de déterminer si vous devez utiliser une stratégie de sous-classement plutôt qu'un contrôleur de vue entièrement personnalisé et vous [abonner aux mises à jour de données]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration/). Par exemple, si vous sous-classez le `ABKContentCardsTableViewController`, vous pouvez utiliser la méthode [`populateContentCards`](#overriding-populated-content-cards) pour filtrer et commander des cartes (recommandé). Cependant, si vous utilisez une personnalisation complète du contrôleur de visualisation, vous disposez d’un plus grand contrôle sur le comportement de la carte, comme l’affichage dans un carrousel ou l’ajout d’éléments interactifs, mais vous devez ensuite compter sur un observateur pour implémenter la logique de tri et de filtrage. Vous devez également implémenter les méthodes d'analyse respectives pour enregistrer correctement les impressions, les événements de rejet et les clics.

## Personnalisation de l’interface utilisateur

Les extraits de code suivants montrent comment styliser et modifier les cartes de contenu pour répondre à vos besoins d’interface utilisateur à l’aide des méthodes fournies par le SDK. Ces méthodes vous permettent de personnaliser tous les aspects de l’interface utilisateur de la carte de contenu, y compris les polices personnalisées, les composants de couleur personnalisés, le texte personnalisé, etc. 

Il existe deux manières distinctes de personnaliser l’interface utilisateur de la carte de contenu : 
- Méthode dynamique : Mettre à jour l’interface utilisateur carte par carte
- Méthode statique : mettre à jour l’interface utilisateur sur toutes les cartes

### Interface utilisateur dynamique

La méthode `applyCard` de la carte de contenu peut référencer l’objet de carte et lui transmettre les paires clé-valeur qui seront utilisées pour mettre à jour l’IU :

{% tabs %}
{% tab Objectif-C %}
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

### Interface utilisateur statique

La méthode `setUpUI` peut affecter des valeurs aux composants statiques de la carte de contenu sur toutes les cartes :

{% tabs %}
{% tab Objectif-C %}
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

## Fournir des interfaces personnalisées

Des interfaces personnalisées peuvent être fournies en enregistrant des classes personnalisées pour tous les types de cartes souhaités. 

![Une bannière Content Card. Une carte de contenu de type bannière affiche une image à droite de la bannière avec le texte « Merci d’avoir téléchargé la démo de Braze ! ».]({% image_buster /assets/img/interface1.png %}){: style="max-width:35%;margin-left:15px;"}
![Une carte de contenu avec une image légendée. Une carte de contenu légendée affiche une image de Braze avec la légende superposée en bas « Merci d’avoir téléchargé la démo de Braze ! ». ]({% image_buster /assets/img/interface2.png %}){: style="max-width:25%;margin-left:15px;"}
![Une Classic Content Card. Une carte de contenu classique affiche une image au centre de la carte avec les mots « Merci d’avoir téléchargé la démo de Braze » en dessous.]({% image_buster /assets/img/interface3.png %}){: style="max-width:18%;margin-left:15px;"}

Braze propose trois types de modèles de cartes de contenu : (bannière, image légendée et classique). Sinon, si vous souhaitez fournir vos propres interfaces personnalisées, référez-vous aux extraits de code suivants :

{% tabs %}
{% tab Objectif-C %}
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

## Remplacer des cartes de contenu remplies

Les cartes de contenu peuvent être modifiées de façon programmatique à l’aide de la méthode `populateContentCards` :

{% tabs %}
{% tab Objectif-C %}
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