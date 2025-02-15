---
nav_title: Integração
article_title: Integração do feed de notícias para iOS
platform: iOS
page_order: 0
description: "Este artigo aborda uma visão geral do modelo de dados do Feed de notícias, a integração do Feed de notícias em seu aplicativo iOS e um exemplo de integração de view controller personalizado."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integração do Feed de notícias

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Modelo de dados do feed de notícias

### Obtendo os dados

Para acessar o modelo de dados do Feed de notícias, assine os eventos de atualização do Feed de notícias:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
// Subscribe to feed updates
// Note: you should remove the observer where appropriate
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(feedUpdated:)
                                             name:ABKFeedUpdatedNotification
                                           object:nil];
```                                           

```objc
// Called when the feed is refreshed (via `requestFeedRefresh`)
- (void)feedUpdated:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKFeedUpdatedIsSuccessfulKey] boolValue];
  // check for success
  // get the cards using [[Appboy sharedInstance].feedController getCardsInCategories:ABKCardCategoryAll];
}
```

{% endtab %}
{% tab swift %}

```swift
// Subscribe to feed updates
// Note: you should remove the observer where appropriate
NotificationCenter.default.addObserver(self, selector:
  #selector(feedUpdated),
  name:NSNotification.Name.ABKFeedUpdated, object: nil)
```

```swift
// Called when the feed is refreshed (via `requestFeedRefresh`)
private func feedUpdated(_ notification: Notification) {
  if let updateSuccessful = notification.userInfo?[ABKFeedUpdatedIsSuccessfulKey] as? Bool {
    // check for success
    // get the cards using Appboy.sharedInstance()?.feedController.getCardsInCategories(.all);      
  }
}
```

{% endtab %}
{% endtabs %}

Se você quiser alterar os dados do cartão depois que eles forem enviados pelo Braze, recomendamos armazenar (cópia profunda) os dados do cartão na localização, atualizá-los e exibi-los você mesmo. Os cartões podem ser acessados por meio do [`ABKFeedController`](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html "controlador de feed da abk").

## Modelo de feed de notícias

O Braze tem cinco tipos de cartões exclusivos: imagem de banner, imagem com legenda, anúncio de texto e clássico. Cada tipo herda propriedades comuns de um modelo base e possui as seguintes propriedades adicionais.

### Propriedades do modelo do cartão básico

|Propriedade|Descrição|
|---|---|
| `idString` | (Somente leitura) O ID do cartão definido pelo Braze. |
| `viewed` | Essa propriedade reflete se o cartão foi lido ou não lido pelo usuário. |
| `created` | (Somente leitura) A propriedade é o registro de data e hora unix da hora de criação do cartão no dashboard da Braze. |
| `updated` | (Somente leitura) A propriedade é o registro de data e hora unix da última atualização do cartão no dashboard do Braze. |
| `categories` | A lista de categorias atribuídas ao cartão; os cartões sem uma categoria serão atribuídos a `ABKCardCategoryNoCategory`.<br><br>Categorias disponíveis:<br>- `ABKCardCategoryNoCategory`<br>- `ABKCardCategoryNews`<br>- `ABKCardCategoryAdvertising`<br>- `ABKCardCategoryAnnouncements`<br>- `ABKCardCategorySocial`<br>- `ABKCardCategoryAll` |
| `extras` | Um `NSDictionary` opcional de valores `NSString`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriedades do cartão de imagem de banner

|Propriedade|Descrição|
|---|---|
| `image` | (Obrigatório) Essa propriedade é o URL da imagem do cartão. |
| `URL` | (Opcional) O URL que será aberto depois que o cartão for clicado. Pode ser um URL HTTP(S) ou um URL de protocolo. |
| `domain` | (Opcional) O texto do link para o URL da propriedade, como @"blog.braze.com". Ele pode ser exibido na interface do usuário do cartão para indicar a ação e a direção do clique no cartão, mas fica oculto no feed de notícias padrão do Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriedades do cartão de imagem legendado

|Propriedade|Descrição|
|---|---|
| `image` | (Obrigatório) Essa propriedade é o URL da imagem do cartão. |
| `title` | (Obrigatório) O texto do título do cartão. |
| `description` (Obrigatório) O texto do corpo do cartão. |
| `URL` | (Opcional) O URL que será aberto depois que o cartão for clicado. Pode ser um URL HTTP(S) ou um URL de protocolo. |
| `domain` | (Opcional) O texto do link para o URL da propriedade, como @"blog.braze.com". Ele pode ser exibido na interface do usuário do cartão para indicar a ação e a direção do clique no cartão. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriedades do cartão de anúncio de texto (imagem legendada sem imagem)

|Propriedade|Descrição|
|---|---|
| `title` | (Obrigatório) O texto do título do cartão. |
| `description` | (Obrigatório) O texto do corpo do cartão. |
| `url` | (Opcional) O URL que será aberto depois que o cartão for clicado. Pode ser um URL HTTP(S) ou um URL de protocolo. |
| `domain` | (Opcional) O texto do link para o URL da propriedade, como @"blog.braze.com". Ele pode ser exibido na interface do usuário do cartão para indicar a ação e a direção do clique no cartão. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriedades do cartão clássico

|Propriedade|Descrição|
|---|---|
| `image` | (Obrigatório) Essa propriedade é o URL da imagem do cartão. |
| `title` | (Opcional) O texto do título do cartão. |
| `description` | (Obrigatório) O texto do corpo do cartão. |
| `URL` | (Opcional) O URL que será aberto depois que o cartão for clicado. Pode ser um URL HTTP(S) ou um URL de protocolo. |
| `domain` | (Opcional) O texto do link para o URL da propriedade, como @"blog.braze.com". Ele pode ser exibido na interface do usuário do cartão para indicar a ação e a direção do clique no cartão. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Métodos do cartão

|Método|Descrição|
|---|---|
| `logCardImpression` | Registre manualmente uma impressão no Braze para um determinado cartão. |
| `logCardClicked` | Registre manualmente um clique no Braze para um determinado cartão. O SDK só registrará um clique no cartão quando o cartão tiver a propriedade `url` com um valor válido. Todas as subclasses de `ABKCard` têm a propriedade `url`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Exibição do feed de registros

Ao exibir o Feed de notícias em sua própria interface de usuário, é possível registrar manualmente as impressões do Feed de notícias por meio do site `- (void)logFeedDisplayed;`. Por exemplo:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance] logFeedDisplayed];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logFeedDisplayed()
```

{% endtab %}
{% endtabs %}

## Integração do controlador de visualização do feed de notícias

A integração do controlador de visualizações `ABKNewsFeedViewController` exibirá o feed de notícias da Braze.

Você tem muita flexibilidade para escolher como exibir os controladores de visualização. Há diferentes versões dos controladores de visualização para acomodar diferentes estruturas de navegação.

{% alert note %}
O Feed de notícias que é chamado pelo comportamento padrão de um clique em uma mensagem no app não respeitará os delegados que você definir para o Feed de notícias. Se quiser respeitar isso, você deve [definir o delegado em `ABKInAppMessageUIController`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/) e implementar o método delegado `ABKInAppMessageUIDelegate` [`onInAppMessageClicked:`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/behavior_on_click/#customizing-in-app-message-body-clicks).
{% endalert %}

O feed de notícias pode ser integrado a dois contextos de controle de exibição: navegação ou modal.

### Contexto de navegação - ABKFeedViewControllerNavigationContext

{% tabs %}
{% tab OBJECTIVE C %}

```objc
ABKNewsFeedTableViewController *newsFeed = [[ABKNewsFeedTableViewController alloc] init];
[self.navigationController pushViewController:newsFeed animated:YES];
```

{% endtab %}
{% tab swift %}

```swift
let newsFeed = ABKNewsFeedTableViewController()
self.navigationController?.pushViewController(newsFeed, animated: true)
```

{% endtab %}
{% endtabs %}

Para personalizar o `title` da barra de navegação, defina a propriedade title do `navigationItem` da instância `ABKNewsFeedTableViewController`.

### Contexto modal - ABKFeedViewControllerModalContext

Esse modal é usado para apresentar o controlador de exibição em uma exibição modal, com uma barra de navegação na parte superior e um botão **Concluído** no lado direito da barra. Para personalizar o título do modal, defina a propriedade `title` do `navigationItem` da instância `ABKNewsFeedTableViewController`. 

Se um delegado **NÃO estiver definido**, o botão **Done (Concluído** ) encerrará a exibição modal. Se um delegado **for definido**, o botão **Done (Concluído** ) chamará o delegado, e o próprio delegado será responsável por encerrar a exibição.

{% tabs %}
{% tab OBJECTIVE C %}

```objc
ABKNewsFeedViewController *newsFeed = [[ABKNewsFeedViewController alloc] init];
[self presentViewController:newsFeed animated:YES completion:nil];
```

{% endtab %}
{% tab swift %}

```swift
let newsFeed = ABKNewsFeedViewController()
self.present(newsFeed, animated: true, completion: nil)
```

{% endtab %}
{% endtabs %}

Para ver exemplos de controladores de exibição, confira nosso [app de amostra do Feed de notícias](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/NewsFeed/BrazeNewsFeedSample).


