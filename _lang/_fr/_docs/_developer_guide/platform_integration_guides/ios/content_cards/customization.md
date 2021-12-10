---
nav_title: Personnalisation
article_title: Personnalisation de la carte de contenu pour iOS
platform: iOS
page_order: 2
description: "Cet article couvre les options de personnalisation de vos Cartes de Contenu dans votre application iOS."
channel:
  - Cartes de contenu
---

# Personnalisation

## Surcharge des images par défaut

{% alert important %}
__Notez que l'intégration de `SDWebImage` est nécessaire si vous prévoyez d'utiliser notre interface utilisateur Braze pour afficher des images__ dans les messages In-App iOS, Flux d'actualités ou Cartes de contenu.
{% endalert %}

Braze permet aux clients de remplacer les images existantes par leurs propres images personnalisées. Pour cela, créez un nouveau fichier `png` avec l'image personnalisée et ajoutez-le au lot d'images de l'application. Ensuite, renommez le fichier avec le nom de l'image (voir ci-dessous) pour remplacer l'image par défaut dans notre bibliothèque. Les images disponibles à remplacer dans les cartes de contenu comprennent:

- Placeholder image: `appboy_cc_noimage_lrg`.
- Image d'icône épinglée : `appboy_cc_icon_pinned`.

Parce que les cartes de contenu ont une taille maximale de 2 Ko pour le contenu que vous entrez dans le tableau de bord (y compris le texte du message les URLs d'image, les liens et toutes les paires clé-valeurs), assurez-vous de vérifier la taille avant d'envoi. Le dépassement de ce montant empêchera l'envoi de la carte.

{% alert note %}
Assurez-vous de télécharger les versions `@2x` et `@3x` des images pour s'adapter aux différentes tailles du téléphone.
{% endalert %}

{% alert note %}
Notez que le remplacement des images par défaut n'est actuellement pas pris en charge dans notre intégration Xamarin iOS.
{% endalert %}

## Personnalisation du flux des cartes de contenu

Vous pouvez créer votre propre interface de cartes de contenu en étendant `ABKContentCardsTableViewController` pour personnaliser tous les éléments de l'interface utilisateur et le comportement des cartes de contenu. Les cellules de la carte de contenu peuvent également être sous-classées et ensuite utilisées par programme ou en introduisant un Storyboard personnalisé qui enregistre les nouvelles classes. Voir le modèle [d'app](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp) de Cartes de Contenu pour un exemple complet. Alternativement, vous pouvez créer un contrôleur de vue entièrement personnalisé et [vous abonner aux mises à jour des données]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/data_model/). Dans ce dernier cas, vous devrez enregistrer tous les événements de vue, les événements rejetés et les clics manuellement.

### Personnalisation de l'interface

Les extraits de code suivants montrent comment styliser et modifier les cartes de contenu hors de la boîte pour correspondre à vos besoins d'interface en utilisant les méthodes fournies par le SDK. Ces méthodes vous permettent de personnaliser tous les aspects de l'interface de la carte de contenu, tels que les polices personnalisées, les composants de couleurs personnalisés, le texte personnalisé, et plus encore.

Il existe deux façons distinctes de personnaliser l'interface utilisateur de la carte de contenu :
- Méthode dynamique : mettre à jour l'interface utilisateur de la carte par carte
- Méthode statique : mettre à jour l'interface utilisateur sur toutes les cartes

#### Interface dynamique

La méthode de la carte de contenu `applyCard` peut référencer l'objet de la carte et lui passer des paires clé-valeur qui seront utilisées pour mettre à jour l'interface utilisateur.

{% tabs %}
{% tab Objective-C %}
```objc
- (void)applyCard:(ABKCaptionedImageContentCard *)captionedImageCard {
  [super applyCard:captionedImageCard];    

  if ([card). xtras objectForKey:ContentCardKeyBackgroundColorValue]) {
    NSString *backgroundColor = [card. xtras objectForKey:ContentCardKeyBackgroundColor];
    if ([backgroundColor colorValue]) {
      self. ootView.backgroundColor = [backgroundColor colorValue];
    } else {
      self.rootView. ackgroundColor = [UIColor lightGray];
    }
  } autre {
    moi-même. ootView.backgroundColor = [UIColor lightGray];
  }  
}
```
{% endtab %}
{% tab Swift %}
```swift
surcharger la fonction application(_ captionedImageCard: ABKCaptionedImageContentCard!) {
  super.apply(captionedImageCard)         

  si laissé backgroundColor = card.extras?[ContentCardKey.backgroundColor.rawValue] comme? String,
     let backgroundColorValue = backgroundColor.colorValue() {
    rootView.backgroundColor = backgroundColorValue
  } else {
    rootView.backgroundColor = .lightGray
  }
}
```
{% endtab %}
{% endtabs %}

#### Interface statique

La méthode `setUpUI` peut assigner des valeurs aux composants statiques de la Carte de Contenu sur toutes les cartes.

{% tabs %}
{% tab Objective-C %}
```objc
#import "CustomClassicContentCardCell.h"  

@implementation CustomClassicContentCardCell

- (void)setUpUI {
  [super setUpUI];
  même. ootView.backgroundColor = [UIColor lightGrayColor];
  même. ootView.layer.borderColor = [UIColor purpleColor].CGColor;
  self.unviewedLineView.backgroundColor = [UIColor redColor];
  self.titleLabel.font = [UIFont italicSystemFontOfSize:20];
}
```
{% endtab %}
{% tab Swift %}
```swift
remplacer func setUpUI() {
  super.setUpUI()

  rootView.backgroundColor = .lightGray
  rootView.layer.borderColor = UIColor.purple.cgColor
  unviewedLineViewColor = .red
  titleLabel.font = .italicSystemFont(ofSize: 20)
}
```
{% endtab %}
{% endtabs %}

### Fournir des interfaces personnalisées

Des interfaces personnalisées peuvent être fournies en enregistrant des classes personnalisées pour chaque type de carte désiré.

![Classes personnalisées]({% image_buster /assets/img/interface1.png %}){: style="max-width:35%;margin-left:15px;"}
![Custom Classes]({% image_buster /assets/img/interface2.png %}){: style="max-width:25%;margin-left:15px;"}
![Custom Classes]({% image_buster /assets/img/interface3.png %}){: style="max-width:18%;margin-left:15px;"}

Braze fournit trois modèles de carte de contenu (bannière, image sous-titrée et classique). Alternativement, si vous souhaitez fournir vos propres interfaces personnalisées, référencez les extraits de code suivants :

{% tabs %}
{% tab Objective-C %}
```objc
- (void)registerTableViewCellClasses {
  [super registerTableViewCellClasses];

  // Remplace les enregistrements de classe par défaut par des classes personnalisées pour ces deux types de cartes
  [self. ableView registerClass:[CustomCaptionedImageContentCardCell class] forCellReuseIdentifier:@"ABKCaptionedImageContentCardCell"];
  [self.tableView registerClass:[CustomClassicContentCardCell class] forCellReuseIdentifier:@"ABKClassicCardCell"];
}
```
{% endtab %}
{% tab Swift %}
```swift
override func registerTableViewCellClasses() {
  super.registerTableViewCellClasses()

  // Remplace les enregistrements de la classe par défaut par des classes personnalisées
  tableView. egister(CustomCaptionedImageContentCardCell.self, forCellReuseIdentifier: "ABKCaptionedImageContentCardCell")
  tableView. egister(CustomBannerContentCardCell.self, forCellReuseIdentifier: "ABKBannerContentCardCell")
  tableView.register(CustomClassicImageContentCardCell.self, forCellReuseIdentifier: "ABKClassicImageCardCell")
  tableView.register(CustomClassicContentCardCell.self, forCellReuseIdentifier: "ABKClassicCardCell")
}
```
{% endtab %}
{% endtabs %}

### Remplacer les cartes de contenu remplies

Les cartes de contenu peuvent être modifiées par programme en utilisant la méthode `populateContentCards`.

{% tabs %}
{% tab Objective-C %}
```objc
- (void)populateContentCards {
  NSMutableArray<ABKContentCard *> *cartes = [NSMutableArray arrayWithArray:[Appboy.sharedInstance. ontentCardsController getContentCards]];
  pour (ABKContentCard *carte en cartes) {
    // Remplace la description de la carte pour toutes les cartes de contenu classiques
    if ([carte isKindOfClass:[classe ABKClassicContentCard]]) {
      ((ABKClassicContentCard *)card). ardDescription = @"Titre de surcharge du flux personnalisé [cartes classiques seulement]!";
    }
  }
  super. cartes = cartes;
}
```
{% endtab %}
{% tab Swift %}
```swift
override func populateContentCards() {
  guard let cards = Appboy.sharedInstance()?.contentCardsController. ontentCards sinon { return }
  pour la carte dans les cartes {
    // Remplace la description de la carte pour toutes les Cartes de Contenu Classiques
    si laisser classicCard = carte comme? ABKClassicContentCard {
      classicCard.cardDescription = "Personnaliser le titre [cartes classiques seulement]!"
    }
  }
  super.cards = (cartes comme NSArray).mutableCopy() comme? NSMutableArray
}
```
{% endtab %}
{% endtabs %}

## Gérer les clics manuellement

Vous pouvez gérer manuellement les clics de carte de contenu en implémentant le protocole [ABKContentCardsTableViewControllerDelegate](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_content_cards_table_view_controller_delegate-p.html) et en définissant votre objet délégué comme la propriété `déléguer` de la `ABKContentCardsTableViewController`. Voir l'échantillon [de Cartes de Contenu](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp) pour un exemple.

{% tabs %}
{% tab Objective-C %}
```objc
Compatible avec le contrôle de la vue. Élégant = délégué;

// Méthodes à implémenter en délégué
- (BOOL)contentCardTableViewController:(ABKContentCardsTableViewController *)viewController
                 shouldHandleCardClick:(NSURL *)url {
  if ([[url. ost lowercaseString] isEqualToString:@"mon-domaine. om"]) {
    // Lien de gestion personnalisée ici
    NSLog(@"Manually handling Content Card click with URL %@", url. bsoluteString);
    retourne NON;
  }
  // Laisser Braze SDK gérer l'action de clic
  retourner OUI;
}

- (void)contentCardTableViewController:(ABKContentCardsTableViewController *)viewController
                    didHandleCardClick:(NSURL *)url {
  NSLog(@"Braze SDK a géré le clic sur la carte de contenu avec l'URL %@", url. bsoluteString);
}
```
{% endtab %}
{% tab Swift %}
```swift
contentCardsTableViewController.delegate = delegate

// Méthodes à implémenter en délégué
func contentCardTableViewController(_ viewController: ABKContentCardsTableViewController!,
                                    should dHandleCardClick url: URL!) -> Bool {
  if (url.host?.lowercased() == "mon-domaine. om") {
    // Lien de gestion personnalisée ici
    NSLog("Manually handling Content Card click with URL %@", url. bsoluteString)
    return false
  }
  // Laisser le Braze SDK gérer l'action de clic
  return true
}

func contentCardTableViewController(_ viewController: ABKContentCardsTableViewController!
                                    didHandleCardClick url: URL!) {
  NSLog("Braze SDK a géré le clic de carte de contenu avec l'URL %@", url.absoluteString)
}
```
{% endtab %}
{% endtabs %}

{% alert important %}
Si vous remplacez la méthode `handleCardClick :` dans `ABKContentCardsTableViewController`, ces méthodes déléguées pourraient ne pas être appelées.
{% endalert %}
