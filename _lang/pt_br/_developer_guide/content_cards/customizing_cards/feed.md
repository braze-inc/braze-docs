---
nav_title: Feed
article_title: Personalizando o feed para Cartões de Conteúdo
page_order: 3
description: "Este artigo aborda as opções de personalização do feed do Content Card."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Personalizando o feed para Cartões de Conteúdo

> Um feed de cartão de conteúdo é a sequência de cartões de conteúdo em seus aplicativos móveis ou da Web. Este artigo aborda a configuração de quando o feed é atualizado, a ordem dos cartões, o gerenciamento de vários feeds e as mensagens de erro de "feed vazio". Para a lista completa de tipos de cartões de conteúdo, veja [Sobre Cartões de Conteúdo]({{site.baseurl}}/developer_guide/content_cards/). 

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## Atualizar o feed

### Atualização automática

Por padrão, o feed de Cartões de Conteúdo será atualizado automaticamente quando:

- Uma nova sessão é iniciada
- O feed é aberto e mais de 60 segundos se passaram desde a última atualização. (Isso se aplica apenas ao feed padrão de Cartões de Conteúdo e ocorre uma vez por abertura do feed.)

{% alert tip %}
Para mostrar dinamicamente os cartões de conteúdo atualizados sem atualizar manualmente, selecione **Na primeira impressão** durante a criação do cartão. Esses cartões serão atualizados quando estiverem disponíveis.
{% endalert %}

### Atualização manual

Para atualizar manualmente o feed em um horário específico:

{% tabs %}
{% tab Android %}

Solicite uma atualização manual dos cartões de conteúdo Braze a partir do SDK do Android a qualquer momento, chamando [`requestContentCardsRefresh`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-content-cards-refresh.html). 

{% subtabs local %}
{% subtab Java %}

```java
Braze.getInstance(context).requestContentCardsRefresh();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).requestContentCardsRefresh()
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

Solicite uma atualização manual dos cartões de conteúdo da Braze a partir do SDK Swift a qualquer momento, chamando o método [`requestRefresh`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/requestrefresh(_:)) na [`Braze.ContentCards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class) classe:

{% subtabs local %}
{% subtab Swift %}

No Swift, os cartões de conteúdo podem ser atualizados com um manipulador de conclusão opcional ou com um retorno assíncrono usando as APIs de simultaneidade nativas do Swift.

#### Manipulador de conclusão

```swift
AppDelegate.braze?.contentCards.requestRefresh { result in
  // Implement completion handler
}
```

#### Async/Await

```swift
let contentCards = await AppDelegate.braze?.contentCards.requestRefresh()
```
{% endsubtab %}
{% subtab Objective-C %}

```objc
[AppDelegate.braze.contentCards requestRefreshWithCompletion:^(NSArray<BRZContentCardRaw *> * contentCards, NSError * error) {
  // Implement completion handler
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab web %}

Solicite uma atualização manual dos cartões de conteúdo da Braze a partir do SDK para Web a qualquer momento, chamando [`requestContentCardsRefresh()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh). 

Você também pode chamar [`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards) para obter todos os cartões disponíveis no momento a partir da última atualização dos cartões de conteúdo. 

```javascript
import * as braze from "@braze/web-sdk";

function refresh() {
  braze.requestContentCardsRefresh();    
}
```

{% endtab %}
{% endtabs %}

### Limite de taxa

A Braze usa um algoritmo de token bucket para impor os seguintes limites de taxa:
- Até 5 chamadas de atualização por dispositivo, compartilhadas entre usuários e chamadas para `openSession()`
- Após atingir o limite, uma nova chamada se torna disponível a cada 180 segundos (3 minutos)
- O sistema manterá até cinco chamadas para você usar a qualquer momento
- `subscribeToContentCards()` ainda retornará cartões em cache mesmo quando limitado por taxa

{% alert important %}
O limite global da rede SDK é de 30 solicitações a cada 30 segundos. Tenha isso em mente ao executar testes automatizados ou realizar QA manual.
{% endalert %}

## Personalização da ordem dos cartões exibidos

Você pode alterar a ordem em que seus cartões de conteúdo são exibidos. Isso permite ajustar a experiência do usuário, priorizando determinados tipos de conteúdo, como promoções sensíveis ao tempo.

{% tabs %}
{% tab Android %}
{% subtabs %}
{% subtab android view controller %}
O [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) se baseia em um [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html) para lidar com qualquer classificação ou modificação dos cartões de conteúdo antes que eles sejam exibidos no feed. Um manipulador de atualização personalizado pode ser definido por meio de [`setContentCardUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html) em seu site `ContentCardsFragment`.

O seguinte é o padrão `IContentCardsUpdateHandler` e pode ser usado como ponto de partida para a personalização:

{% details Mostrar exemplo em Java %}
```java
public class DefaultContentCardsUpdateHandler implements IContentCardsUpdateHandler {

  // Interface that must be implemented and provided as a public CREATOR
  // field that generates instances of your Parcelable class from a Parcel.
  public static final Parcelable.Creator<DefaultContentCardsUpdateHandler> CREATOR = new Parcelable.Creator<DefaultContentCardsUpdateHandler>() {
    public DefaultContentCardsUpdateHandler createFromParcel(Parcel in) {
      return new DefaultContentCardsUpdateHandler();
    }

    public DefaultContentCardsUpdateHandler[] newArray(int size) {
      return new DefaultContentCardsUpdateHandler[size];
    }
  };

  @Override
  public List<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
    List<Card> sortedCards = event.getAllCards();
    // Sort by pinned, then by the 'updated' timestamp descending
    // Pinned before non-pinned
    Collections.sort(sortedCards, new Comparator<Card>() {
      @Override
      public int compare(Card cardA, Card cardB) {
        // A displays above B
        if (cardA.getIsPinned() && !cardB.getIsPinned()) {
          return -1;
        }

        // B displays above A
        if (!cardA.getIsPinned() && cardB.getIsPinned()) {
          return 1;
        }

        // At this point, both A & B are pinned or both A & B are non-pinned
        // A displays above B since A is newer
        if (cardA.getUpdated() > cardB.getUpdated()) {
          return -1;
        }

        // B displays above A since A is newer
        if (cardA.getUpdated() < cardB.getUpdated()) {
          return 1;
        }

        // At this point, every sortable field matches so keep the natural ordering
        return 0;
      }
    });

    return sortedCards;
  }

  // Parcelable interface method
  @Override
  public int describeContents() {
    return 0;
  }

  // Parcelable interface method
  @Override
  public void writeToParcel(Parcel dest, int flags) {
    // No state is kept in this class so the parcel is left unmodified
  }
}
```
{% enddetails %}

{% details Mostrar exemplo em Kotlin %}
```kotlin
class DefaultContentCardsUpdateHandler : IContentCardsUpdateHandler {
  override fun handleCardUpdate(event: ContentCardsUpdatedEvent): List<Card> {
    val sortedCards = event.allCards
    // Sort by pinned, then by the 'updated' timestamp descending
    // Pinned before non-pinned
    sortedCards.sortWith(Comparator sort@{ cardA: Card, cardB: Card ->
      // A displays above B
      if (cardA.isPinned && !cardB.isPinned) {
        return@sort -1
      }

      // B displays above A
      if (!cardA.isPinned && cardB.isPinned) {
        return@sort 1
      }

      // At this point, both A & B are pinned or both A & B are non-pinned
      // A displays above B since A is newer
      if (cardA.updated > cardB.updated) {
        return@sort -1
      }

      // B displays above A since A is newer
      if (cardA.updated < cardB.updated) {
        return@sort 1
      }
      0
    })
    return sortedCards
  }

  // Parcelable interface method
  override fun describeContents(): Int {
    return 0
  }

  // Parcelable interface method
  override fun writeToParcel(dest: Parcel, flags: Int) {
    // No state is kept in this class so the parcel is left unmodified
  }

  companion object {
    // Interface that must be implemented and provided as a public CREATOR
    // field that generates instances of your Parcelable class from a Parcel.
    val CREATOR: Parcelable.Creator<DefaultContentCardsUpdateHandler?> = object : Parcelable.Creator<DefaultContentCardsUpdateHandler?> {
      override fun createFromParcel(`in`: Parcel): DefaultContentCardsUpdateHandler? {
        return DefaultContentCardsUpdateHandler()
      }

      override fun newArray(size: Int): Array<DefaultContentCardsUpdateHandler?> {
        return arrayOfNulls(size)
      }
    }
  }
}
```
{% enddetails %}

{% alert tip %}
O código-fonte do `ContentCardsFragment` pode ser encontrado no [GitHub](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/ContentCardsFragment.kt).
{% endalert %}
{% endsubtab %}
{% subtab Jetpack Compose %}
Para filtrar e classificar os cartões de conteúdo no Jetpack Compose, defina o parâmetro `cardUpdateHandler`. Por exemplo:

```kotlin
ContentCardsList(
    cardUpdateHandler = {
        it.sortedWith { cardA, cardB ->
            // A displays above B
            if (cardA.isPinned && !cardB.isPinned) {
                return@sortedWith -1
            }
            // B displays above A
            if (!cardA.isPinned && cardB.isPinned) {
                return@sortedWith 1
            }
            // At this point, both A & B are pinned or both A & B are non-pinned
            // A displays above B since A is newer
            if (cardA.updated > cardB.updated) {
                return@sortedWith -1
            }
            // B displays above A since A is newer
            if (cardA.updated < cardB.updated) {
                return@sortedWith 1
            }
            0
        }
    }
)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

{% subtabs %}
{% subtab Swift %}

Personalize a ordem de alimentação do cartão modificando diretamente a variável estática [`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults).

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
    cards.sorted {
        if $0.pinned && !$1.pinned {
            return true
        } else if !$0.pinned && $1.pinned {
            return false
        } else {
            return $0.createdAt > $1.createdAt
        }
    }
}
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

A personalização via `BrazeContentCardUI.ViewController.Attributes` não está disponível em Objective C. 

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab web %}

Personalize a ordem de exibição dos cartões de conteúdo em seu feed usando o param de [`filterFunction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards) `showContentCards():`. Por exemplo:

```javascript
braze.showContentCards(null, (cards) => {
  return sortBrazeCards(cards); // Where sortBrazeCards is your sorting function that returns the sorted card array
});
```

{% endtab %}
{% endtabs %}

## Personalização da mensagem "feed vazio

Quando um usuário não se qualifica para nenhum cartão de conteúdo, o SDK exibe uma mensagem de erro de "feed vazio" informando: "Não temos atualizações. Por favor, verifique novamente mais tarde". Você pode personalizar essa mensagem de erro de "feed vazio" de forma semelhante à seguinte:

![Uma mensagem de erro de feed vazio que diz "Esta é uma mensagem personalizada de estado vazio".]({% image_buster/assets/img/content_cards/content-card-customization-empty.png %})

{% tabs %}
{% tab Android %}
{% subtabs %}
{% subtab android view system %}

Se o [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) determinar que o usuário não se qualifica para nenhum cartão de conteúdo, ele exibirá a mensagem de erro de feed vazio.

Um adaptador especial, o [`EmptyContentCardsAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/EmptyContentCardsAdapter.kt)substitui o adaptador padrão [`ContentCardAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/ContentCardAdapter.kt) para exibir essa mensagem de erro. Para definir a própria mensagem personalizada, substitua o recurso de string `com_braze_feed_empty`.

O estilo usado para exibir essa mensagem pode ser encontrado em [`Braze.ContentCardsDisplay.Empty`](https://github.com/braze-inc/braze-android-sdk/blob/2e386dfa59a87bfc24ef7cb6ff5adf6b16f44d24/android-sdk-ui/src/main/res/values/styles.xml#L522-L530) e é reproduzido no trecho de código a seguir:

```xml
<style name="Braze.ContentCardsDisplay.Empty">
  <item name="android:lineSpacingExtra">1.5dp</item>
  <item name="android:text">@string/com_braze_feed_empty</item>
  <item name="android:textColor">@color/com_braze_content_card_empty_text_color</item>
  <item name="android:textSize">18.0sp</item>
  <item name="android:gravity">center</item>
  <item name="android:layout_height">match_parent</item>
  <item name="android:layout_width">match_parent</item>
</style>
```

Para saber mais sobre como personalizar os elementos de estilo do cartão de conteúdo, consulte [Personalização de estilo]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/).
{% endsubtab %}
{% subtab Jetpack Compose %}
Para personalizar a mensagem de erro "feed vazio" com Jetpack Compose, você pode passar um `emptyString` para [`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html). Você também pode passar [`emptyTextStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-list-styling/index.html#1193499348%2FProperties%2F-1725759721) para `ContentCardListStyling` para personalizar ainda mais esta mensagem.

```kotlin
ContentCardsList(
    emptyString = "No messages today",
    style = ContentCardListStyling(
        emptyTextStyle = TextStyle(...)
    )
)
```

Se você tiver um Composable que gostaria de exibir em vez disso, pode passar `emptyComposable` para [`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html). Se `emptyComposable` for especificado, o `emptyString` não será usado.

```kotlin
ContentCardsList(
    emptyComposable = {
        Image(
            painter = painterResource(id = R.drawable.noMessages),
            contentDescription = "No messages"
        )
    }
)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}
{% subtabs local %}
{% subtab Swift %}

Personalize o estado vazio do view controller configurando as opções relacionadas [`Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults).

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.emptyStateMessage = "This is a custom empty state message"
attributes.emptyStateMessageFont = .preferredFont(forTextStyle: .title1)
attributes.emptyStateMessageColor = .secondaryLabel
```

{% endsubtab %}
{% subtab Objective-C %}

Altere o idioma que aparece automaticamente nos feeds vazios do cartão de conteúdo redefinindo as strings localizáveis do cartão de conteúdo no arquivo [`ContentCardsLocalizable.strings`](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization/en.lproj) do aplicativo.

{% alert note %}
Se você quiser atualizar essa mensagem em diferentes idiomas de localização, localize o idioma correspondente na [estrutura da pasta Resources](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization) com a string `ContentCardsLocalizable.strings`.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab web %}

O Web SDK não oferece suporte à substituição programática da linguagem "feed vazio". Você pode aceitar substituí-lo sempre que o feed for exibido, mas isso não é recomendado porque o feed pode levar algum tempo para ser atualizado e o texto vazio do feed não será exibido imediatamente. 

{% endtab %}
{% endtabs %}

## Implementando múltiplos feeds

Os cartões de conteúdo podem ser filtrados em seu app para que apenas cartões específicos sejam exibidos, o que o capacita a ter vários feeds de cartões de conteúdo para diferentes casos de uso. Por exemplo, você pode manter um feed transacional e um feed de marketing. Para isso, crie diferentes categorias de cartões de conteúdo definindo pares de valores-chave no dashboard do Braze. Em seguida, crie feeds em seu app ou site que tratem esses tipos de cartões de conteúdo de forma diferente, filtrando alguns tipos e exibindo outros.

### Etapa 1: Definir pares de valores-chave nos cartões

Ao criar uma campanha de cartão de conteúdo, defina [os dados do par chave-valor]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior/) em cada cartão. Você usará esse par chave-valor para categorizar os cartões. Os pares de valores-chave são armazenados na propriedade `extras` no modelo de dados do cartão.

Para este exemplo, definiremos um par de valores chave com a chave `feed_type` que designará em qual feed do cartão de conteúdo o cartão deve ser exibido. O valor será o valor de seus feeds personalizados, como `home_screen` ou `marketing`.

### Etapa 2: Filtrar cartões de conteúdo

Depois que os pares de valores-chave tiverem sido atribuídos, crie um feed com lógica que exibirá os cartões que você deseja exibir e filtrará cartões de outros tipos. Neste exemplo, exibiremos apenas os cartões com um par de valores-chave correspondente a `feed_type: "Transactional"`.

{% tabs %}
{% tab Android %}
{% subtabs %}
{% subtab android view system %}

Por padrão, o feed do cartão de conteúdo é exibido em um [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) e [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html) retorna uma lista de cartões a serem exibidos após receber um [`ContentCardsUpdatedEvent`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-content-cards-updated-event/index.html) do SDK do Braze. No entanto, ele apenas classifica os cartões e não lida com nenhum filtro diretamente.

#### Etapa 2.1: Crie um manipulador personalizado

Você pode filtrar cartões de conteúdo implementando um [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html) personalizado usando os pares chave-valor definidos por [`Card.getExtras()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html) no dashboard, e então modificá-lo para remover quaisquer cartões da lista que não correspondam ao valor de `feed_type` que você definiu anteriormente.

{% details Mostrar exemplo em Java %}
```java
private IContentCardsUpdateHandler getUpdateHandlerForFeedType(final String desiredFeedType) {
  return new IContentCardsUpdateHandler() {
    @Override
    public List<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
      // Use the default card update handler for a first
      // pass at sorting the cards. This is not required
      // but is done for convenience.
      final List<Card> cards = new DefaultContentCardsUpdateHandler().handleCardUpdate(event);

      final Iterator<Card> cardIterator = cards.iterator();
      while (cardIterator.hasNext()) {
        final Card card = cardIterator.next();

        // Make sure the card has our custom KVP
        // from the dashboard with the key "feed_type"
        if (card.getExtras().containsKey("feed_type")) {
          final String feedType = card.getExtras().get("feed_type");
          if (!desiredFeedType.equals(feedType)) {
            // The card has a feed type, but it doesn't match
            // our desired feed type, remove it.
            cardIterator.remove();
          }
        } else {
          // The card doesn't have a feed
          // type at all, remove it
          cardIterator.remove();
        }
      }

      // At this point, all of the cards in this list have
      // a feed type that explicitly matches the value we put
      // in the dashboard.
      return cards;
    }
  };
}
```
{% enddetails %}

{% details Mostrar exemplo em Kotlin %}
```kotlin
private fun getUpdateHandlerForFeedType(desiredFeedType: String): IContentCardsUpdateHandler {
  return IContentCardsUpdateHandler { event ->
    // Use the default card update handler for a first
    // pass at sorting the cards. This is not required
    // but is done for convenience.
    val cards = DefaultContentCardsUpdateHandler().handleCardUpdate(event)

    val cardIterator = cards.iterator()
    while (cardIterator.hasNext()) {
      val card = cardIterator.next()

      // Make sure the card has our custom KVP
      // from the dashboard with the key "feed_type"
      if (card.extras.containsKey("feed_type")) {
        val feedType = card.extras["feed_type"]
        if (desiredFeedType != feedType) {
          // The card has a feed type, but it doesn't match
          // our desired feed type, remove it.
          cardIterator.remove()
        }
      } else {
        // The card doesn't have a feed
        // type at all, remove it
        cardIterator.remove()
      }
    }

    // At this point, all of the cards in this list have
    // a feed type that explicitly matches the value we put
    // in the dashboard.
    cards
  }
}
```
{% enddetails %}

#### Etapa 2.2: Adicione-o a um fragmento

Depois de criar um [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html), crie um [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) que o utilize. Esse feed personalizado pode ser usado como qualquer outro `ContentCardsFragment`. Nas diferentes partes de seu app, exiba diferentes feeds de cartão de conteúdo com base na chave fornecida no dashboard. Cada feed do `ContentCardsFragment` terá um conjunto exclusivo de cartões exibidos graças ao `IContentCardsUpdateHandler` personalizado em cada fragmento.

{% details Mostrar exemplo em Java %}
```java
// We want a Content Cards feed that only shows "Transactional" cards.
ContentCardsFragment customContentCardsFragment = new ContentCardsFragment();
customContentCardsFragment.setContentCardUpdateHandler(getUpdateHandlerForFeedType("Transactional"));
```
{% enddetails %}

{% details Mostrar exemplo em Kotlin %}
```kotlin
// We want a Content Cards feed that only shows "Transactional" cards.
val customContentCardsFragment = ContentCardsFragment()
customContentCardsFragment.contentCardUpdateHandler = getUpdateHandlerForFeedType("Transactional")
```
{% enddetails %}
{% endsubtab %}

{% subtab Jetpack Compose %}
Para filtrar quais cartões de conteúdo são mostrados nesse feed, use `cardUpdateHandler`. Por exemplo:

```kotlin
ContentCardsList(
     cardUpdateHandler = {
         it.filter { card ->
             card.extras["feed_type"] == "Transactional"
         }
     }
 )
 ```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

O exemplo a seguir mostrará o feed dos cartões de conteúdo para cartões do tipo `Transactional`:

{% subtabs %}
{% subtab Swift %}

```swift
// Filter cards by the `Transactional` feed type based on your key-value pair.
let transactionalCards = cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
```

Para ir além, os cartões apresentados no view controller podem ser filtrados definindo a propriedade `transform` em sua estrutura `Attributes` para exibir apenas os cartões filtrados por seus critérios.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
  cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
}

// Pass your attributes containing the transformed cards to the Content Card UI.
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// Filter cards by the `Transactional` feed type based on your key-value pair.
NSMutableArray<BRZContentCardRaw *> *transactionalCards = [[NSMutableArray alloc] init];
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if ([card.extras[@"feed_type"] isEqualToString:@"Transactional"]) {
    [transactionalCards addObject:card];
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab web %}

O exemplo a seguir mostrará o feed dos cartões de conteúdo para cartões do tipo `Transactional`:

```javascript

/**
 * @param {String} feed_type - value of the "feed_type" KVP to filter
 */
function showCardsByFeedType(feed_type) {
  braze.showContentCards(null, function(cards) {
    return cards.filter((card) => card.extras["feed_type"] === feed_type);
  });
}
```

Em seguida, você pode configurar um botão de alternância para seu feed personalizado:

```javascript
// show the "Transactional" feed when this button is clicked
document.getElementById("show-transactional-feed").onclick = function() {
  showCardsByFeedType("Transactional"); 
};
```

Para saber mais, consulte a [documentação do método SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards).

{% endtab %}
{% endtabs %}
