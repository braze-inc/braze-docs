---
nav_title: Integração
article_title: Integração do cartão de conteúdo para iOS
platform: Swift
page_order: 0
description: "Este artigo aborda as etapas de integração, os modelos de dados e as propriedades específicas do cartão disponíveis no Swift SDK."
channel:
  - content cards

---

# Integração do cartão de conteúdo

> Este artigo de referência aborda a integração do Content Card e os diferentes modelos de dados e propriedades específicas do cartão disponíveis para seu aplicativo Swift. Quando estiver pronto para começar a implementação e a personalização, consulte o [Guia de personalização do cartão de conteúdo]({{site.baseurl}}/developer_guide/customization_guides/content_cards).

## Sobre a integração

A interface padrão dos cartões de conteúdo pode ser integrada a partir da biblioteca `BrazeUI` do SDK da Braze. Crie o controlador de visualização Content Cards usando a instância `braze`. Se quiser interceptar e reagir ao ciclo de vida da interface do usuário do Content Card, implemente [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) como o delegado de seu `BrazeContentCardUI.ViewController`.

{% alert note %}
Para saber mais sobre as opções de view controller do iOS, consulte a [documentação da Apple para desenvolvedores](https://developer.apple.com/documentation/uikit/view_controllers/showing_and_hiding_view_controllers).
{% endalert %}

A biblioteca `BrazeUI` do Swift SDK apresenta dois contextos de controle de exibição padrão: navegação ou modal. Isso significa que você pode integrar os cartões de conteúdo nesses contextos adicionando algumas linhas de código ao seu app ou site. Ambas as visualizações oferecem opções de personalização e estilo, conforme descrito no [guia de personalização]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_styles/?tab=ios). Você também pode criar um controlador de visualização de cartão de conteúdo personalizado em vez de usar o controlador padrão do Braze para ter ainda mais opções de personalização - consulte o [tutorial Content Cards UI](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/) para obter um exemplo.

{% alert important %}
Para lidar com a variante de controle dos cartões de conteúdo em sua interface personalizada, passe o objeto [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)) e, em seguida, chame o método `logImpression` como faria com qualquer outro tipo de cartão de conteúdo. O objeto registrará implicitamente uma impressão de controle para informar nossa análise de dados sobre quando um usuário teria visto o cartão de controle.
{% endalert %}

## Contexto de navegação

Um navigation controller é um view controller que gerencia um ou mais child view controllers em uma interface de navegação. Veja um exemplo de como inserir uma instância `BrazeContentCardUI.ViewController` em um navigation controller:

{% tabs %}
{% tab swift %}

```swift
func pushViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsController.delegate = self
  self.navigationController?.pushViewController(contentCardsController, animated: true)
}
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
- (void)pushViewController {
  BRZContentCardUIViewController *contentCardsController = [[BRZContentCardUIViewController alloc] initWithBraze:self.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsController setDelegate:self];
  [self.navigationController pushViewController:contentCardsController animated:YES];
}
```

{% endtab %}
{% endtabs %}

## Contexto modal

Use apresentações modais para criar interrupções temporárias no fluxo de trabalho do seu app, como solicitar informações importantes ao usuário. Essa visualização de modelo tem uma barra de navegação na parte superior e um botão **Concluído** na lateral da barra. Veja um exemplo de como inserir uma instância `BrazeContentCard.ViewController` em um modal controller:

{% tabs %}
{% tab swift %}

```swift
func presentModalViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsModal = BrazeContentCardUI.ModalViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsModal.viewController.delegate = self
  self.navigationController?.present(contentCardsModal, animated: true, completion: nil)
}
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
- (void)presentModalViewController {
  BRZContentCardUIModalViewController *contentCardsModal = [[BRZContentCardUIModalViewController alloc] initWithBraze:AppDelegate.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsModal.viewController setDelegate:self];
  [self.navigationController presentViewController:contentCardsModal animated:YES completion:nil];
}
```

{% endtab %}
{% endtabs %}

Para obter um exemplo de uso dos controladores de visualização `BrazeUI`, confira as amostras correspondentes da interface do usuário dos cartões de conteúdo em nosso [app Examples](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

## Modelo de dados dos cartões de conteúdo

O modelo de dados dos cartões de conteúdo está disponível no módulo `BrazeKit` para o iOS Swift SDK.

O Braze oferece cinco tipos de cartão de conteúdo: somente imagem, imagem com legenda, clássico, imagem clássica e controle. Cada tipo é uma implementação do tipo `Braze.ContentCard`. Observe que `BrazeKit` oferece uma classe [`ContentCardRaw`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw) alternativa para compatibilidade com Objective C.

Para obter uma lista completa das propriedades de cartões de conteúdo, bem como detalhes sobre o uso de cartões de conteúdo, consulte a [documentação da classe`ContentCard`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard).

Para acessar o modelo de dados dos cartões de conteúdo, chame `contentCards.cards` em sua instância `braze`. Consulte [Análise de registros]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics) para saber mais sobre a assinatura de dados de cartões.

## Métodos do cartão

Cada cartão é inicializado com um objeto `Context`, que contém vários métodos para gerenciar o estado do cartão. Chame esses métodos quando quiser modificar a propriedade de estado correspondente em um objeto de cartão específico.

| Método                               | Descrição                                                                                                                              |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `card.context?.logImpression()`      | Registre o evento de impressão do cartão de conteúdo.                                                                                                   |
| `card.context?.logClick()`           | Registre o evento de clique do cartão de conteúdo.                                                                                                        |
| `card.context?.processClickAction()` | Processa uma determinada [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/clickaction) entrada. |
| `card.context?.logDismissed()`       | Registre o evento de descarte do cartão de conteúdo.                                                                                                    |
| `card.context?.logError()`           | Registre um erro relacionado ao cartão de conteúdo.                                                                                                |
| `card.context?.loadImage()`          | Carregue uma determinada imagem de cartão de conteúdo a partir de um URL. Esse método pode ser nulo quando o cartão de conteúdo não tiver uma imagem.                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para saber mais, consulte a [`Context`documentação de referência da classe](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw/context-swift.class)

{% alert important %}
O Swift SDK não oferece suporte a GIFs animados por padrão. O suporte pode ser adicionado ao envolver um terceiro ou sua própria exibição em uma instância de `GIFViewProvider`.

Para saber mais sobre o suporte a GIFs, consulte este [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support).
{% endalert %}
