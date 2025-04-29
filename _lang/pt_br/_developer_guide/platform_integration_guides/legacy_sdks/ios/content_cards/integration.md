---
nav_title: Integração
article_title: Integração do Controlador de Visualização do Cartão de Conteúdo para iOS
platform: iOS
page_order: 1
description: "Este artigo de referência cobre as etapas de integração, modelos de dados e propriedades específicas do cartão disponíveis para apps iOS."
channel:
  - content cards
search_rank: 3
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# integração do cartão de conteúdo

## Modelo de dados de Cartões de Conteúdo

O modelo de dados dos cartões de conteúdo está disponível no SDK para iOS.

### Obtenção dos dados

Para acessar o modelo de dados dos Cartões de Conteúdo, inscreva-se nos eventos de atualização dos Cartões de Conteúdo:

{% tabs %}
{% tab OBJECTIVE C %}
```objc
// Subscribe to Content Cards updates
// Note: you should remove the observer where appropriate
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(contentCardsUpdated:)
                                             name:ABKContentCardsProcessedNotification
                                           object:nil];
```

```objc
// Called when Content Cards are refreshed (via `requestContentCardsRefresh`)
- (void)contentCardsUpdated:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue];
  if (updateIsSuccessful) {
    // get the cards using [[Appboy sharedInstance].contentCardsController getContentCards];
  }
}
```
{% endtab %}
{% tab swift %}
```swift
// Subscribe to content card updates
// Note: you should remove the observer where appropriate
NotificationCenter.default.addObserver(self, selector:
  #selector(contentCardsUpdated),
  name:NSNotification.Name.ABKContentCardsProcessed, object: nil)
```

```swift
// Called when the Content Cards are refreshed (via `requestContentCardsRefresh`)
@objc private func contentCardsUpdated(_ notification: Notification) {
  if let updateIsSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool {
    if (updateIsSuccessful) {
      // get the cards using Appboy.sharedInstance()?.contentCardsController.contentCards
    }
  }
}
```
{% endtab %}
{% endtabs %}

Se você quiser alterar os dados do cartão depois de enviados pelo Braze, recomendamos armazenar uma cópia profunda dos dados do cartão localmente, atualizar os dados e exibi-los você mesmo. Os cartões são acessíveis via [`ABKContentCardsController`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_cards_controller.html).

## modelo de cartão de conteúdo

A Braze oferece três tipos de cartão de conteúdo: banner, imagem legendada e clássico. Cada tipo herda propriedades comuns de uma classe base `ABKContentCard` e possui as seguintes propriedades adicionais.

### Propriedades do modelo de cartão de conteúdo base - ABKContentCard

|Propriedade|Descrição|
|---|---|
|`idString` | (Somente leitura) O ID do cartão definido pelo Braze. |
| `viewed` | Essa propriedade reflete se o usuário visualizou o cartão ou não.|
| `created` | (Somente leitura) Esta propriedade é o timestamp unix do horário de criação do cartão da Braze. |
| `expiresAt` | (Somente leitura) Esta propriedade é o timestamp unix do tempo de expiração do cartão.|
| `dismissible` | Esta propriedade reflete se o usuário pode dispensar o cartão.|
| `pinned` | Essa propriedade reflete se o cartão foi configurado como "fixado" no dashboard.|
| `dismissed` | Esta propriedade reflete se o usuário descartou o cartão.|
| `url` | A URL que será aberta após o cartão ser clicado. Pode ser um URL HTTP(s) ou um URL de protocolo.|
| `openURLInWebView` | Esta propriedade determina se o URL será aberto dentro do app ou em um navegador web externo.|
| `extras`| Um `NSDictionary` opcional de valores `NSString`.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### propriedades do cartão de conteúdo de banner - ABKBannerContentCard

|Propriedade|Descrição|
|---|---|
| `image` | Esta propriedade é o URL da imagem do cartão.|
| `imageAspectRatio` | Esta propriedade é a proporção da imagem do cartão e serve como uma dica antes que o carregamento da imagem seja concluído. Observe que a propriedade pode não ser fornecida em certas circunstâncias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriedades do cartão de conteúdo da imagem legendada - ABKCaptionedImageCard

|Propriedade|Descrição|
|---|---|
| `image` | Esta propriedade é o URL da imagem do cartão.|
| `imageAspectRatio` | Esta propriedade é a proporção da imagem do cartão.|
| `title` | O texto do título do cartão.|
| `cardDescription` | O texto do corpo para o cartão.|
| `domain` | O texto do link para a URL da propriedade, como @"blog.braze.com". Ele pode ser exibido na interface do usuário do cartão para indicar a ação/direção de clicar no cartão.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriedades do cartão de conteúdo clássico - ABKClassicContentCard

|Propriedade|Descrição|
|---|---|
| `image` | (Opcional) Esta propriedade é a URL da imagem do cartão.|
| `title` | O texto do título do cartão. |
| `cardDescription` | O texto do corpo para o cartão. |
| `domain` | O texto do link para a URL da propriedade, como @"blog.braze.com". Ele pode ser exibido na interface do usuário do cartão para indicar a ação e a direção do clique no cartão. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Métodos do cartão

|Método|Descrição|
|---|---|
| `logContentCardImpression` | Registre manualmente uma impressão no Braze para um determinado cartão. |
| `logContentCardClicked` | Registre manualmente um clique no Braze para um determinado cartão. O SDK só registrará um clique no cartão quando o cartão tiver a propriedade `url` com um valor válido. |
| `logContentCardDismissed` | Registre manualmente uma dispensa no Braze para um cartão específico. O SDK só registrará um descarte de cartão se a propriedade `dismissed` do cartão ainda não estiver definida como `true`. |
| `isControlCard` | Determine se um cartão é o cartão de Controle para um teste A/B. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para saber mais, consulte a [documentação de referência da classe](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html)

## Integração do controlador de visualização de Cartões de Conteúdo

Os Cartões de Conteúdo podem ser integrados com dois contextos de controlador de visualização: navegação ou modal.

### Contexto de navegação

Exemplo de como inserir uma instância `ABKContentCardsTableViewController` em um controlador de navegação:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
ABKContentCardsTableViewController *contentCards = [[ABKContentCardsTableViewController alloc] init];
contentCards.title = @"Content Cards Title";
contentCards.disableUnreadIndicator = YES;
[self.navigationController pushViewController:contentCards animated:YES];
```

{% endtab %}
{% tab swift %}

```swift
let contentCards = ABKContentCardsTableViewController()
contentCards.title = "Content Cards Title"
contentCards.disableUnreadIndicator = true
navigationController?.pushViewController(contentCards, animated: true)
```

{% endtab %}
{% endtabs %}

{% alert note %}
Para personalizar o título da barra de navegação, defina a propriedade title do `navigationItem` da instância `ABKContentCardsTableViewController`.
{% endalert %}

### Contexto modal

Este modal é usado para apresentar o controlador de visualização em uma visualização modal, com uma barra de navegação no topo e um botão **Concluído** na lateral da barra.

{% tabs %}
{% tab OBJECTIVE C %}

```objc
ABKContentCardsViewController *contentCards = [[ABKContentCardsViewController alloc] init];
contentCards.contentCardsViewController.title = @"Content Cards Title";
contentCards.contentCardsViewController.disableUnreadIndicator = YES;
[self.navigationController presentViewController:contentCards animated:YES completion:nil];
```

{% endtab %}
{% tab swift %}

```swift
let contentCards = ABKContentCardsViewController()
contentCards.contentCardsViewController.title = "Content Cards Title"
contentCards.contentCardsViewController.disableUnreadIndicator = true
self.present(contentCards, animated: true, completion: nil)
```

{% endtab %}
{% endtabs %}

Para exemplos de controlador de visualização, confira o [app de exemplo de Cartões de Conteúdo](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp).

{% alert note %}
Para personalizar o cabeçalho, defina a propriedade de título do `navigationItem` pertencente à instância `ABKContentCardsTableViewController` incorporada na instância pai `ABKContentCardsViewController`.
{% endalert %}
