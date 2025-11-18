> Ao criar uma interface de usuário personalizada para cartões de conteúdo, é necessário registrar manualmente análises de dados como impressões, cliques e descartes de cartões, pois isso só é tratado automaticamente para modelos de cartões padrão. O registro desses eventos é uma parte padrão da integração do Content Card e é essencial para a geração de relatórios e o faturamento precisos da campanha. Para fazer isso, preencha a interface do usuário personalizada com dados dos modelos de dados do Braze e, em seguida, registre manualmente os eventos. Depois de entender como registrar a análise de dados, você poderá ver as maneiras comuns pelas quais os clientes do Braze [criam cartões de conteúdo personalizados]({{site.baseurl}}/developer_guide/content_cards/creating_cards/). 

## Ouvindo as atualizações do cartão

Ao implementar seus cartões de conteúdo personalizados, você pode analisar os objetos do cartão de conteúdo e extrair seus dados de carga útil, como `title`, `cardDescription` e `imageUrl`. Em seguida, você pode usar os dados do modelo resultante para preencher sua interface personalizada. 

Para obter os modelos de dados do cartão de conteúdo, inscreva-se para receber as atualizações do cartão de conteúdo. Preste atenção especial em duas propriedades:

* **`id`**: Representa a string de ID do cartão de conteúdo. Esse é o identificador exclusivo usado para registrar análises de dados de cartões de conteúdo personalizados.
* **`extras`**: Engloba todos os pares de valores-chave do dashboard do Braze. 

Todas as propriedades fora de `id` e `extras` são opcionais para análise de cartões de conteúdo personalizados. Para saber mais sobre o modelo de dados, consulte o artigo de integração de cada plataforma: [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android), [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift), [Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web).


{% tabs %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

### Etapa 1: Criar uma variável de assinante privada

Para assinar as atualizações do cartão, primeiro declare uma variável privada em sua classe personalizada para manter o assinante:

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

### Etapa 2: Inscrever-se para receber atualizações

Em seguida, adicione o seguinte código para inscrever-se para receber as atualizações dos cartões de conteúdo da Braze, normalmente dentro de `Activity.onCreate()` da atividade dos cartões de conteúdo personalizados:

```java
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
mContentCardsUpdatedSubscriber = new IEventSubscriber<ContentCardsUpdatedEvent>() {
    @Override
    public void trigger(ContentCardsUpdatedEvent event) {
        // List of all Content Cards
        List<Card> allCards = event.getAllCards();

        // Your logic below
    }
};
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber);
Braze.getInstance(context).requestContentCardsRefresh();
```

### Etapa 3: Cancelar inscrição

Também recomendamos cancelar a inscrição quando sua atividade personalizada sair de vista. Adicione o seguinte código ao método de ciclo de vida `onDestroy()` de sua atividade:

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

### Etapa 1: Criar uma variável de assinante privada

Para assinar as atualizações do cartão, primeiro declare uma variável privada em sua classe personalizada para manter o assinante:

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

### Etapa 2: Inscrever-se para receber atualizações

Em seguida, adicione o seguinte código para inscrever-se para receber as atualizações dos cartões de conteúdo da Braze, normalmente dentro de `Activity.onCreate()` da atividade dos cartões de conteúdo personalizados:

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).subscribeToContentCardsUpdates(contentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh()
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

### Etapa 3: Cancelar inscrição

Também recomendamos cancelar a inscrição quando sua atividade personalizada sair de vista. Adicione o seguinte código ao método de ciclo de vida `onDestroy()` de sua atividade:

```kotlin
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

Para acessar o modelo de dados dos cartões de conteúdo, chame [`contentCards.cards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cards) em sua instância `braze`.

{% subtabs local %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

Além disso, você também pode manter uma inscrição para observar as alterações em seus cartões de conteúdo. Você pode fazer isso de duas maneiras: 
1. Manutenção de um cancelável; ou 
2. Manutenção de um `AsyncStream`.

### Cancelável 

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] contentCards in
  // Implement your completion handler to respond to updates in `contentCards`.
}
```

### AsyncStream

```swift
let stream: AsyncStream<[Braze.ContentCard]> = AppDelegate.braze?.contentCards.cardsStream
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
NSArray<BRZContentCardRaw *> *contentCards = AppDelegate.braze.contentCards.cards;
```

Além disso, para manter uma inscrição em seus cartões de conteúdo, você poderá chamar [`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)):

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab web %}

Registre uma função de retorno de chamada para se inscrever para receber atualizações quando os cartões forem atualizados.

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
// For example:
  cards.forEach(card => {
    if (card.isControl) {
      // Do not display the control card, but remember to call `logContentCardImpressions([card])`
    }
    else if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      // Use `card.title`, `card.imageUrl`, etc.
    }
    else if (card instanceof braze.ImageOnly) {
      // Use `card.imageUrl`, etc.
    }
  })
});

braze.openSession();
```

{% alert note %}
Os cartões de conteúdo somente serão atualizados no início da sessão se uma solicitação de inscrição for chamada antes de `openSession()`. Você também pode optar por [atualizar manualmente o feed]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/).
{% endalert %}

{% endtab %}
{% endtabs %}

## Eventos de registro

O registro de métricas valiosas, como impressões, cliques e descartes, é rápido e simples. Defina um listener (ouvinte) de cliques personalizado para lidar manualmente com essas análises de dados.

{% tabs %}
{% tab Android %}

O [`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) pode fazer referência às dependências do SDK do Braze, como a lista de vetores de objetos do cartão de conteúdo, para obter o [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) para chamar os métodos de registro do Braze. Use a classe base `ContentCardable` para facilitar a referência e o fornecimento de dados para o `BrazeManager`. 

Para registrar uma impressão ou clicar em um cartão, ligue para [`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) ou [`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html) respectivamente. 

É possível registrar manualmente ou definir um cartão de conteúdo como "descartado" para a Braze com [`isDismissed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissed.html). Se um cartão já tiver sido marcado como descartado, ele não poderá ser marcado como descartado novamente.

Para criar um ouvinte de cliques personalizado, crie uma classe que implemente [`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html) e registre-a com o [`BrazeContentCardsManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.managers/-braze-content-cards-manager/index.html). Implemente o método [`onContentCardClicked()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/on-content-card-clicked.html) que será chamado quando o usuário clicar em um cartão de conteúdo. Em seguida, instrua a Braze a usar seu ouvinte de clique do cartão de conteúdo. 

{% subtabs local %}
{% subtab Java %}

Por exemplo:

```java
BrazeContentCardsManager.getInstance().setContentCardsActionListener(new IContentCardsActionListener() {
  @Override
  public boolean onContentCardClicked(Context context, Card card, IAction cardAction) {
    return false;
  }

  @Override
  public void onContentCardDismissed(Context context, Card card) {

  }
});
```

{% endsubtab %}
{% subtab Kotlin %}

Por exemplo:

```kotlin
BrazeContentCardsManager.getInstance().contentCardsActionListener = object : IContentCardsActionListener {
  override fun onContentCardClicked(context: Context, card: Card, cardAction: IAction): Boolean {
    return false
  }

  override fun onContentCardDismissed(context: Context, card: Card) {

  }
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Para lidar com a variante de controle dos cartões de conteúdo em sua interface personalizada, passe o objeto [`com.braze.models.cards.Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) e, em seguida, chame o método `logImpression` como faria com qualquer outro tipo de cartão de conteúdo. O objeto registrará implicitamente uma impressão de controle para informar nossa análise de dados sobre quando um usuário teria visto o cartão de controle.{% endalert %}

{% endtab %}
{% tab swift %}

Implemente o protocolo [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) e defina seu objeto delegado como a propriedade `delegate` de `BrazeContentCardUI.ViewController`. Esse delegado tratará de passar os dados do seu objeto personalizado de volta ao Braze para serem registrados. Para obter um exemplo, consulte o [tutorial da interface do usuário dos cartões de conteúdo](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/).

{% subtabs local %}
{% subtab Swift %}

```swift
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate

// Method to implement in delegate
func contentCard(
    _ controller: BrazeContentCardUI.ViewController,
    shouldProcess clickAction: Braze.ContentCard.ClickAction,
    card: Braze.ContentCard
  ) -> Bool {
  // Intercept the content card click action here.
  return true
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate;

// Method to implement in delegate
- (BOOL)contentCardController:(BRZContentCardUIViewController *)controller
                shouldProcess:(NSURL *)url
                         card:(BRZContentCardRaw *)card {
  // Intercept the content card click action here.
  return YES;
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Para lidar com a variante de controle dos cartões de conteúdo em sua interface personalizada, passe o objeto [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)) e, em seguida, chame o método `logImpression` como faria com qualquer outro tipo de cartão de conteúdo. O objeto registrará implicitamente uma impressão de controle para informar nossa análise de dados sobre quando um usuário teria visto o cartão de controle.
{% endalert %}
{% endtab %}

{% tab web %}

Registre eventos de impressão quando os cartões forem visualizados por usuários usando [`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions):

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardImpressions([card1, card2, card3]);
```

Registre os eventos de clique do cartão quando os usuários interagirem com um cartão usando [`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick):

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardClick(card);
```

{% endtab %}
{% endtabs %}
