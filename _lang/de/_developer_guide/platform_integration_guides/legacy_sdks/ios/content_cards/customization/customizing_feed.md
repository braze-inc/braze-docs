---
nav_title: Anpassen des Feeds
article_title: Content-Card-Feed für iOS anpassen
platform: iOS
page_order: 2
description: "Dieser Artikel behandelt die Anpassungsmöglichkeiten von Content-Card-Feeds in Ihrer iOS-Anwendung."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Anpassen des Content-Cards-Feeds

Sie können Ihre eigene Content-Cards-Schnittstelle erstellen, indem Sie `ABKContentCardsTableViewController` erweitern, um alle UI-Elemente und das Verhalten der Content-Cards anzupassen. Die Content-Card-Zellen können auch unterklassifiziert und dann programmatisch oder mithilfe eines angepassten Storyboards, das die neuen Klassen registriert, verwendet werden. Ein vollständiges Beispiel finden Sie in der Content-Cards [App](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp). 

Es ist auch wichtig zu überlegen, ob Sie lieber eine Strategie der Unterklassifizierung oder einen vollständig angepassten View Controller verwenden und [Daten-Updates abonnieren]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration/) wollen. Wenn Sie zum Beispiel die Unterklasse `ABKContentCardsTableViewController` verwenden, können Sie die [Methode`populateContentCards` ](#overriding-populated-content-cards) zum Filtern und Ordnen von Karten verwenden (empfohlen). Wenn Sie jedoch einen vollständig angepassten View-Controller verwenden, haben Sie mehr Kontrolle über das Verhalten der Karte - wie z.B. die Anzeige in einem Karussell oder das Hinzufügen interaktiver Elemente - aber Sie müssen sich dann auf einen Beobachter verlassen, um die Bestell- und Filterlogik zu implementieren. Sie müssen auch die entsprechenden Analytics-Methoden implementieren, um Impressionen, Abbrüche und Klicks ordnungsgemäß zu protokollieren.

## Anpassen der UI

Die folgenden Code-Snippets zeigen, wie Sie Content-Cards mit den vom SDK bereitgestellten Methoden gestalten und an Ihre UI-Anforderungen anpassen können. Diese Methoden erlauben es Ihnen, alle Aspekte der Content-Card UI anzupassen, einschließlich angepasster Schriftarten, angepasster Farbkomponenten, angepasster Texte und mehr. 

Es gibt zwei verschiedene Möglichkeiten, die Content-Card-UI anzupassen: 
- Dynamische Methode: Update der UI für jede Karte
- Statische Methode: Update des UI für alle Karten

### Dynamische UI

Die Content-Card-Methode `applyCard` kann das Kartenobjekt referenzieren und ihm Schlüssel-Wert-Paare übergeben, die für das Update der UI verwendet werden:

{% tabs %}
{% tab Objective-C %}
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

### Statische UI

Die Methode `setUpUI` kann den statischen Content-Card-Komponenten über alle Karten hinweg Werte zuweisen:

{% tabs %}
{% tab Objective-C %}
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

## Anpassen von Schnittstellen

Angepasste Schnittstellen können durch die Registrierung von angepassten Klassen für jeden gewünschten Kartentyp bereitgestellt werden. 

![Eine Banner-Content-Card. Eine Banner-Content-Card zeigt ein Bild rechts neben dem Banner mit dem Text "Thanks for downloading Braze Demo!".]({% image_buster /assets/img/interface1.png %}){: style="max-width:35%;margin-left:15px;"}
![Eine Content-Card mit Bildunterschrift. Eine hervorgehobene Content-Card zeigt ein Bild von Braze und unten den Schriftzug "Thanks for downloading Braze Demo!". ]({% image_buster /assets/img/interface2.png %}){: style="max-width:25%;margin-left:15px;"}
![Eine klassische Content-Card. Eine klassische Content-Card zeigt ein Bild in der Mitte der Karte und darunter die Worte "Vielen Dank für das Herunterladen der Braze-Demo".]({% image_buster /assets/img/interface3.png %}){: style="max-width:18%;margin-left:15px;"}

Braze bietet drei Content-Card-Templates (Banner, Bildunterschrift und klassisch). Wenn Sie eigene angepasste Schnittstellen bereitstellen möchten, referenzieren Sie die folgenden Code-Snippets:

{% tabs %}
{% tab Objective-C %}
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

## Überschreiben von ausgefüllten Content-Cards

Content-Cards können programmatisch mit der Methode `populateContentCards` geändert werden:

{% tabs %}
{% tab Objective-C %}
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