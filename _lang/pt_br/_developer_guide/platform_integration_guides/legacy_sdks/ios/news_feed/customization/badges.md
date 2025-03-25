---
nav_title: Emblemas
article_title: Emblemas do feed de notícias para iOS
platform: iOS
page_order: 3
description: "Este artigo de referência aborda como implementar a contagem de emblemas do feed de notícias em seu aplicativo iOS."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Emblemas

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Solicitação de contagem de cartões não lidos do Feed de notícias

![]({% image_buster /assets/img_archive/newsfeed_badges.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Os emblemas são uma ótima maneira de chamar a atenção para novos conteúdos que aguardam seus usuários no Feed de notícias. Se quiser adicionar um emblema aos seu feed de notícias, o SDK da Braze oferece métodos para consultar o seguinte:

- Cartões do feed de notícias não lidos do usuário atual
- Total de cartões do feed de notícias visualizáveis para o usuário atual

As declarações de método a seguir em [`ABKFeedController`](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html "abk feed controller") descrevem isso em detalhes:

```
- (NSInteger)unreadCardCountForCategories:(ABKCardCategory)categories;
/*
This method returns the number of currently active Content Cards that have not been viewed.
A "view" happens when a card becomes visible in the Content Cards view. This differentiates between cards that are off-screen in the scrolling view and those which are on-screen; when a card scrolls onto the screen, it's counted as viewed.
Cards are counted as viewed only once -- if a card scrolls off the screen and back on, it's not re-counted.
Cards are counted only once, even if they appear in multiple Content Cards views or across multiple devices.
*/

- (NSInteger)cardCountForCategories:(ABKCardCategory)categories;
/* 
This method returns the total number of currently active Content Cards. Cards are counted only once, even if they appear in multiple Content Cards views.
 */
 ```

## Exibição do número de itens não lidos do feed de notícias na contagem do emblema do app

Além de servir como lembretes de notificações por push para um app, os emblemas também podem indicar itens não visualizados no feed de notícias do usuário. A atualização da contagem de emblemas com base nas atualizações não lidas do Feed de notícias pode ser uma ferramenta valiosa para atrair os usuários de volta ao seu app e aumentar as sessões.

Chame esse método que registra a contagem de emblemas depois que o app é fechado e a sessão do usuário termina:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

{% endtab %}
{% tab swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

{% endtab %}
{% endtabs %}

Nesse método, implemente o seguinte código, que atualiza ativamente a contagem de emblemas enquanto o usuário visualiza os cartões durante uma determinada sessão.

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = [[Appboy sharedInstance].feedController unreadCardCountForCategories:ABKCardCategoryAll];
```

{% endtab %}
{% tab swift %}

```swift
UIApplication.shared.applicationIconBadgeNumber = Appboy.sharedInstance()?.feedController.unreadCardCount(forCategories: ABKCardCategory.all) ?? 0
```

{% endtab %}
{% endtabs %}

Em qualquer ponto, por exemplo, no método `applicationDidBecomeActive`, use o código a seguir para limpar a contagem de emblemas:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% tab swift %}

```swift
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% endtabs %}

Para saber mais, veja o `Appboy.h` [arquivo de cabeçalho](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h "Appboy.h Arquivo de Cabeçalho").

