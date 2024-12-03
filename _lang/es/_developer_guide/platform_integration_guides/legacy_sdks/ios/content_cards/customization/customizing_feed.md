---
nav_title: Fuente personalizada
article_title: Personalizar la fuente de tarjetas de contenido para iOS
platform: iOS
page_order: 2
description: "Este artículo cubre las opciones de personalización de la fuente de la tarjeta de contenido en tu aplicación iOS."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Personalizar la fuente de tarjetas de contenido

Puedes crear tu propia interfaz de tarjetas de contenido ampliando `ABKContentCardsTableViewController` para personalizar todos los elementos de la interfaz de usuario y el comportamiento de las tarjetas de contenido. Las celdas de la tarjeta de contenido también pueden subclasificarse y luego utilizarse mediante programación o introduciendo un guión gráfico personalizado que registre las nuevas clases. Consulta la [aplicación de muestra](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp) Tarjetas de contenido para ver un ejemplo completo. 

También es importante considerar si debes utilizar una estrategia de subclase frente a un controlador de vista completamente personalizado y [suscribirte para las actualizaciones de datos]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration/). Por ejemplo, si subclasificas el `ABKContentCardsTableViewController`, puedes utilizar el método [`populateContentCards` ](#overriding-populated-content-cards) para filtrar y ordenar las tarjetas (recomendado). Sin embargo, si utilizas una personalización completa del controlador de vista, tendrás más control sobre el comportamiento de la tarjeta -como mostrarla en un carrusel o añadir elementos interactivos-, pero entonces tendrás que depender de un observador para implementar la lógica de ordenación y filtrado. También debes implementar los métodos de análisis respectivos para registrar correctamente las impresiones, los eventos de rechazo y los clics.

## Personalización de la interfaz de usuario

Los siguientes fragmentos de código muestran cómo dar estilo y cambiar las tarjetas de contenido para adaptarlas a tus necesidades de interfaz de usuario utilizando los métodos proporcionados por el SDK. Estos métodos te permiten personalizar todos los aspectos de la interfaz de usuario de la tarjeta de contenido, incluyendo fuentes personalizadas, componentes de color personalizados, texto personalizado y mucho más. 

Existen dos formas distintas de personalizar la interfaz de usuario de la tarjeta de contenido: 
- Método dinámico: actualizar la interfaz de usuario de la tarjeta por tarjeta
- Método estático: actualizar la IU en todas las tarjetas

### IU dinámica

El método de la tarjeta de contenido `applyCard` puede hacer referencia al objeto tarjeta y pasarle los pares clave-valor que se utilizarán para actualizar la interfaz de usuario:

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

### IU estática

El método `setUpUI` puede asignar valores a los componentes estáticos de la tarjeta de contenido en todas las tarjetas:

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

## Proporcionar interfaces personalizadas

Se pueden proporcionar interfaces personalizadas registrando clases personalizadas para cada tipo de tarjeta deseado. 

![Una tarjeta de contenido de banner. Una tarjeta de contenido de banner muestra una imagen a la derecha del banner con el texto "¡Gracias por descargar la Demo de Braze!".]({% image_buster /assets/img/interface1.png %}){: style="max-width:35%;margin-left:15px;"}
![Una imagen subtitulada Tarjeta de contenido. Una tarjeta de contenido subtitulada muestra una imagen de Braze con la leyenda superpuesta en la parte inferior "¡Gracias por descargar la Demo de Braze!". ]({% image_buster /assets/img/interface2.png %}){: style="max-width:25%;margin-left:15px;"}
![Una tarjeta de contenido clásica. Una tarjeta de contenido clásica muestra una imagen en el centro de la tarjeta con las palabras "Gracias por descargar la Demo de Braze" debajo.]({% image_buster /assets/img/interface3.png %}){: style="max-width:18%;margin-left:15px;"}

Braze proporciona tres plantillas de tarjetas de contenido (banner, imagen subtitulada y clásica). Alternativamente, si quieres proporcionar tus propias interfaces personalizadas, haz referencia a los siguientes fragmentos de código:

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

## Anulación de tarjetas de contenido pobladas

Las tarjetas de contenido pueden modificarse mediante programación utilizando el método `populateContentCards`:

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