---
nav_title: Manipulação manual de cliques
article_title: Manipulação manual de cliques em cartões de conteúdo para iOS
platform: iOS
page_order: 3
description: "Este artigo aborda como lidar manualmente com os cliques nos cartões de conteúdo em seu aplicativo iOS."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Tratamento manual de cliques

Você pode tratar manualmente os cliques no content card implementando o protocolo [`ABKContentCardsTableViewControllerDelegate`](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_content_cards_table_view_controller_delegate-p.html) e definindo seu objeto delegado como a propriedade `delegate` do `ABKContentCardsTableViewController`. Consulte o [app de amostra de content cards](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp) para obter um exemplo. 

{% tabs %}
{% tab Objective C %}
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
Se você substituir o método `handleCardClick:` em `ABKContentCardsTableViewController`, esses métodos delegados poderão não ser chamados.
{% endalert %}
