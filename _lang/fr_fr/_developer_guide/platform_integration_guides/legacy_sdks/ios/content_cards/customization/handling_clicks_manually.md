---
nav_title: Gestion manuelle des clics
article_title: Gestion manuelle des clics de carte de contenu pour iOS
platform: iOS
page_order: 3
description: "Cet article explique comment gérer les clics des cartes de contenu manuellement dans votre application iOS."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Gestion manuelle des clics

Vous pouvez gérer manuellement les clics sur les cartes de contenu en implémentant le protocole [`ABKContentCardsTableViewControllerDelegate`](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_content_cards_table_view_controller_delegate-p.html) et en définissant votre objet délégué comme la propriété `delegate` du `ABKContentCardsTableViewController`. Reportez-vous à l'exemple d'application [Content Cards](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp) pour un exemple. 

{% tabs %}
{% tab Objectif-C %}
```objc
contentCardsTableViewController.delegate = delegate;

// Methods to implement in delegate
- (BOOL)contentCardTableViewController:(ABKContentCardsTableViewController *)viewController
                 shouldHandleCardClick:(NSURL *)url {
  if ([[url.host lowercaseString] isEqualToString:@"my-domain.com"]) {
    // Custom handle link here
    NSLog(@"Manually handling Content Card click with URL %@", url.absoluteString);
    return NO;
  }
  // Let the Braze SDK handle the click action
  return YES;
}

- (void)contentCardTableViewController:(ABKContentCardsTableViewController *)viewController
                    didHandleCardClick:(NSURL *)url {
  NSLog(@"Braze SDK handled Content Card click with URL %@", url.absoluteString);
}
```
{% endtab %}
{% tab Swift %}
```swift
contentCardsTableViewController.delegate = delegate

// Methods to implement in delegate
func contentCardTableViewController(_ viewController: ABKContentCardsTableViewController!,
                                    shouldHandleCardClick url: URL!) -> Bool {
  if (url.host?.lowercased() == "my-domain.com") {
    // Custom handle link here
    NSLog("Manually handling Content Card click with URL %@", url.absoluteString)
    return false
  }
  // Let the Braze SDK handle the click action
  return true
}

func contentCardTableViewController(_ viewController: ABKContentCardsTableViewController!,
                                    didHandleCardClick url: URL!) {
  NSLog("Braze SDK handled Content Card click with URL %@", url.absoluteString)
}
```
{% endtab %}
{% endtabs %}

{% alert important %}
Si vous remplacez la méthode `handleCardClick:` dans `ABKContentCardsTableViewController`, ces méthodes de délégation ne peuvent pas être employées.
{% endalert %}
