---
nav_title: Ícones
article_title: Crachás de cartão de conteúdo para iOS
platform: iOS
page_order: 5
description: "Este artigo aborda a adição de emblemas aos cartões de conteúdo em seu aplicativo iOS."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Ícones

## Solicitação de contagem de cartões de conteúdo não lidos

Se quiser exibir o número de cartões de conteúdo não lidos que seu usuário tem, sugerimos que solicite uma contagem de cartões e a represente com um emblema. Os emblemas são uma ótima maneira de chamar a atenção para novos conteúdos que aguardam seus usuários nos cartões de conteúdo. Se quiser adicionar um emblema aos seus cartões de conteúdo, o SDK da Braze oferece métodos para consultar o seguinte:

- Cartões de conteúdo não visualizados para o usuário atual
- Total de cartões de conteúdo visualizável para o usuário atual

As seguintes declarações de método em [`ABKContentCardsController`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_cards_controller.html) descrevem isso em detalhes:

```objc
- (NSInteger)unviewedContentCardCount;
/*
This method returns the number of currently active Content Cards that have not been viewed.
A "view" happens when a card becomes visible in the Content Cards view. This differentiates between cards that are off-screen in the scrolling view and those which are on-screen; when a card scrolls onto the screen, it's counted as viewed.
Cards are counted as viewed only once -- if a card scrolls off the screen and back on, it's not re-counted.
Cards are counted only once, even if they appear in multiple Content Cards views or across multiple devices.
*/

- (NSInteger)contentCardCount;
/* 
This method returns the total number of currently active Content Cards. Cards are counted only once even if they appear in multiple Content Cards views.
 */
```

## Exibição do número de cartões de conteúdo não visualizados na contagem do emblema do app

Além de servir como lembretes de notificação por push para um app, os emblemas também podem ser utilizados para indicar itens não visualizados no feed de cartões de conteúdo do usuário. A atualização da contagem de emblemas com base nas atualizações dos cartões de conteúdo não visualizados pode ser valiosa para atrair os usuários de volta ao seu app e aumentar as sessões.

Esse método registra a contagem de emblemas depois que o app é fechado e a sessão do usuário termina:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

Nesse método, implemente o seguinte código, que atualiza ativamente a contagem de emblemas enquanto o usuário visualiza os cartões durante uma determinada sessão:

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = [[Appboy sharedInstance].contentCardsController unviewedContentCardCount];
```

{% endtab %}
{% tab swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

Nesse método, implemente o seguinte código, que atualiza ativamente a contagem de emblemas enquanto o usuário visualiza os cartões durante uma determinada sessão:

```swift
UIApplication.shared.applicationIconBadgeNumber =
  Appboy.sharedInstance()?.contentCardsController.unviewedContentCardCount() ?? 0
```

{% endtab %}
{% endtabs %}

Para saber mais, consulte o [arquivo de cabeçalho](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) `Appboy.h`.
