---
nav_title: Style personnalisé
article_title: Style de carte de contenu personnalisé pour iOS
platform: iOS
page_order: 1
description: "Cet article couvre les options de style personnalisé de la carte de contenu pour votre application iOS."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Style personnalisé

## Remplacer les images par défaut

{% alert important %}
L’intégration de `SDWebImage` est requise si vous prévoyez d’utiliser notre interface utilisateur Braze pour afficher des images dans les messages in-app iOS ou les cartes de contenu.
{% endalert %}

Braze permet aux clients de remplacer les images par défaut existantes par leurs propres images personnalisées. Pour y parvenir, créez un nouveau fichier `png` avec l’image personnalisée et ajoutez-la à l’ensemble d’images de l’application. Renommez ensuite le fichier avec le nom de l’image pour remplacer l’image par défaut de notre bibliothèque. Assurez-vous également de télécharger les versions `@2x` et `@3x` des images pour permettre différentes tailles de téléphone. Les images pouvant être remplacées dans les cartes de contenu incluent :

- Image de marque substitutive : `appboy_cc_noimage_lrg`
- Image d’icône épinglée : `appboy_cc_icon_pinned`

Étant donné que les cartes de contenu ont une taille maximale de 2 Ko pour le contenu que vous saisissez dans le tableau de bord (y compris le texte des messages, les URL d’images, les liens et toutes les paires clé-valeur), vérifiez la taille avant d’envoyer. Dépasser ce montant empêchera la carte d’être envoyée.

{% alert important %}
Le remplacement des images par défaut n’est actuellement pas pris en charge dans notre intégration Xamarin iOS.
{% endalert %}

## Désactivation du mode sombre

Pour empêcher l'interface utilisateur de la carte de contenu d'adopter un style de thème sombre lorsque l'appareil de l'utilisateur a activé le mode sombre, définissez la propriété `ABKContentCardsTableViewController.enableDarkTheme`. Vous pouvez accéder à la propriété `enableDarkTheme` directement sur une instance `ABKContentCardsTableViewController` ou via la propriété `ABKContentCardsViewController.contentCardsViewController` pour mieux répondre à votre propre interface utilisateur.

{% tabs %}
{% tab OBJECTIF-C %}

```objc
// Accessing enableDarkTheme via ABKContentCardsViewController.contentCardsViewController.
- (IBAction)presentModalContentCards:(id)sender {
  ABKContentCardsViewController *contentCardsVC = [ABKContentCardsViewController new];
  contentCardsVC.contentCardsViewController.enableDarkTheme = NO;
  ...
  [self.navigationController presentViewController:contentCardsVC animated:YES completion:nil];
}

// Accessing enableDarkTheme directly.
- (IBAction)presentNavigationContentCards:(id)sender {
  ABKContentCardsTableViewController *contentCardsTableVC = [[ABKContentCardsTableViewController alloc] init];
  contentCardsTableVC.enableDarkTheme = NO;
  ...
  [self.navigationController pushViewController:contentCardsTableVC animated:YES];
}
```

{% endtab %}
{% tab swift %}

```swift
// Accessing enableDarkTheme via ABKContentCardsViewController.contentCardsViewController.
@IBAction func presentModalContentCards(_ sender: Any) {
  let contentCardsVC = ABKContentCardsViewController()
  contentCardsVC.contentCardsViewController.enableDarkTheme = false
  ...
  self.navigationController?.present(contentCardsVC, animated: true, completion: nil)
}

// Accessing enableDarkTheme directly.
@IBAction func presentNavigationContentCards(_ sender: Any) {
  let contentCardsTableVC = ABKContentCardsTableViewController()
  contentCardsTableVC.enableDarkTheme = false
  ...
  self.navigationController?.present(contentCardsTableVC, animated: true, completion: nil)
}
```

{% endtab %}
{% endtabs %}

