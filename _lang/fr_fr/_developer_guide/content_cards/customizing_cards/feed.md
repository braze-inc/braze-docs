---
nav_title: Alimentation
article_title: Personnaliser le flux des cartes de contenu
page_order: 3
description: "Cet article traite des options de personnalisation du flux de la carte de contenu."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Personnaliser le flux des cartes de contenu

> Un flux de cartes de contenu correspond à la séquence de cartes de contenu dans vos applications mobiles ou Web. Cet article traite de la configuration du moment où le flux est actualisé, de l'ordre des cartes, de la gestion de plusieurs flux et des messages d'erreur "flux vide". Pour obtenir la liste complète des types de cartes de contenu, voir [À propos des cartes de contenu.]({{site.baseurl}}/developer_guide/content_cards/) 

## Rafraîchir le flux

Par défaut, le flux de cartes de contenu s'actualise automatiquement dans les instances suivantes : 
1. Une nouvelle session est lancée
2. Lorsque le flux est ouvert et que plus de 60 secondes se sont écoulées depuis la dernière actualisation. Cela ne s'applique qu'au flux par défaut de la carte de contenu et ne se produit qu'une seule fois par ouverture du flux.

Vous pouvez également configurer le SDK pour qu'il s'actualise manuellement à des moments précis.

{% alert tip %}
Pour afficher dynamiquement les cartes de contenu actualisées sans les rafraîchir manuellement, sélectionnez **À la première impression** lors de la création de cartes. Ces cartes seront actualisées dès qu'elles seront disponibles.
{% endalert %}

{% tabs local %}
{% tab Android %}

Demandez, à tout moment, une actualisation manuelle des cartes de contenu Braze à partir du SDK Android en appelant [`requestContentCardsRefresh`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-content-cards-refresh.html). 

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
{% tab iOS %}

Demandez, à tout moment, une actualisation manuelle des cartes de contenu Braze à partir du SDK Swift en appelant la méthode [`requestRefresh`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/requestrefresh(_:)) dans la classe [`Braze.ContentCards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class) :

{% subtabs local %}
{% subtab Swift %}

Dans Swift, les cartes de contenu peuvent être actualisées soit avec un gestionnaire d'achèvement facultatif, soit avec un retour asynchrone en utilisant les API de concurrence Swift natives.

### Gestionnaire d’achèvement

```swift
AppDelegate.braze?.contentCards.requestRefresh { result in
  // Implement completion handler
}
```

### Async/Attente

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
{% tab Web %}

Demandez, à tout moment, une actualisation manuelle des cartes de contenu Braze à partir du SDK Web en appelant [`requestContentCardsRefresh()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh). 

Vous pouvez également appeler [`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards) pour obtenir toutes les cartes actuellement disponibles depuis la dernière actualisation des cartes de contenu. 

```javascript
import * as braze from "@braze/web-sdk";

function refresh() {
  braze.requestContentCardsRefresh();    
}
```

{% endtab %}
{% endtabs %}


{% alert important %}
Vous pouvez effectuer jusqu'à cinq appels successifs. Ensuite, un nouvel appel sera disponible toutes les 180 secondes. Le système peut retenir jusqu'à cinq appels que vous pouvez utiliser à tout moment.
{% endalert %}

## Personnalisation de l'ordre des cartes affichées

Vous pouvez modifier l'ordre d'affichage de vos cartes de contenu. Cela vous permet d'affiner l'expérience utilisateur en donnant la priorité à certains types de contenu, tels que les promotions sensibles au facteur temps.

{% tabs %}
{% tab Système d'affichage Android %}

Les [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) s'appuie sur un [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html) pour gérer tout tri ou modification des cartes de contenu avant qu'elles ne soient affichées dans le flux. Un gestionnaire de mise à jour personnalisé peut être défini via [`setContentCardUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html) sur votre site `ContentCardsFragment`.

Voici le `IContentCardsUpdateHandler` par défaut, qui peut être utilisé comme point de départ pour la personnalisation :

{% subtabs local %}
{% subtab Java %}

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

{% endsubtab %}
{% subtab Kotlin %}

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

{% endsubtab %}
{% endsubtabs %}

La source de `ContentCardsFragment` est disponible sur [GitHub.](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/ContentCardsFragment.kt)

{% endtab %}
{% tab Jetpack Compose %}
Pour filtrer et trier les cartes de contenu dans Jetpack Compose, définissez le paramètre `cardUpdateHandler`. Par exemple :

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
{% endtab %}
{% tab iOS %}

{% subtabs %}
{% subtab Swift %}

Personnalisez l'ordre du flux de cartes en modifiant directement la variable statique [`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults).

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

La personnalisation via `BrazeContentCardUI.ViewController.Attributes` n'est pas disponible en Objective-C. 

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Personnalisez l'ordre d'affichage des cartes de contenu dans votre flux en utilisant le paramètre [`filterFunction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards) de `showContentCards():`. Par exemple :

```javascript
braze.showContentCards(null, (cards) => {
  return sortBrazeCards(cards); // Where sortBrazeCards is your sorting function that returns the sorted card array
});
```

{% endtab %}
{% endtabs %}

## Personnalisation du message "aliment vide".

Lorsqu'un utilisateur n'a droit à aucune carte de contenu, le SDK affiche un message d'erreur indiquant que le flux est vide : "Nous n'avons pas de nouvelles. Veuillez vérifier à nouveau plus tard". Vous pouvez personnaliser ce message d'erreur "flux vide" de la manière suivante :

![Un message d'erreur de flux vide indiquant "Ceci est un message d'état vide personnalisé".]({% image_buster/assets/img/content_cards/content-card-customization-empty.png %})

{% tabs %}
{% tab Système d'affichage Android %}

Si le [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) détermine que l'utilisateur n'a droit à aucune carte de contenu, il affiche le message d'erreur du flux vide.

Un adaptateur spécial, le [`EmptyContentCardsAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/EmptyContentCardsAdapter.kt)remplace l'adaptateur standard [`ContentCardAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/ContentCardAdapter.kt) pour afficher ce message d'erreur. Pour définir le message personnalisé lui-même, remplacez la ressource de chaîne de caractère `com_braze_feed_empty`.

Le style utilisé pour afficher ce message peut être trouvé via [`Braze.ContentCardsDisplay.Empty`](https://github.com/braze-inc/braze-android-sdk/blob/2e386dfa59a87bfc24ef7cb6ff5adf6b16f44d24/android-sdk-ui/src/main/res/values/styles.xml#L522-L530) et est reproduit dans l'extrait de code suivant :

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

Pour plus d'informations sur la personnalisation des éléments de style des cartes de contenu, voir [Personnaliser le style]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/).
{% endtab %}
{% tab Jetpack Compose %}
Pour personnaliser le message d'erreur de flux vide avec Jetpack Compose, vous pouvez transmettre une `emptyString` à `ContentCardsList`. Vous pouvez également transmettre `emptyTextStyle` à `ContentCardListStyling` pour personnaliser davantage ce message.

```kotlin
ContentCardsList(
    emptyString = "No messages today",
    style = ContentCardListStyling(
        emptyTextStyle = TextStyle(...)
    )
)
```

Si vous souhaitez plutôt afficher une fonction Composable, vous pouvez transmettre `emptyComposable` à `ContentCardsList`. Si `emptyComposable` est spécifié, la `emptyString` ne sera pas utilisée.

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
{% endtab %}
{% tab iOS %}
{% subtabs local %}
{% subtab Swift %}

Personnalisez l'état vide du contrôleur de vue en définissant les [`Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults) associés.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.emptyStateMessage = "This is a custom empty state message"
attributes.emptyStateMessageFont = .preferredFont(forTextStyle: .title1)
attributes.emptyStateMessageColor = .secondaryLabel
```

{% endsubtab %}
{% subtab Objective-C %}

Modifiez la langue qui s'affiche automatiquement dans les flux de cartes de contenu vides en redéfinissant les chaînes de caractères localisables des cartes de contenu dans le fichier [`ContentCardsLocalizable.strings`](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization/en.lproj) de votre application.

{% alert note %}
Si vous souhaitez mettre à jour ce message dans différentes langues locales, recherchez la langue correspondante dans la [structure du dossier Resources](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization) à l'aide de la chaîne de caractères `ContentCardsLocalizable.strings`.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Le SDK Web ne permet pas de remplacer par programme le langage du flux vide. Vous pouvez choisir de le remplacer à chaque fois que le flux est affiché, mais cela n'est pas recommandé car le flux peut mettre un certain temps à s'actualiser et le texte vide du flux ne s'affichera pas immédiatement. 

{% endtab %}
{% endtabs %}

## Fils multiples

Les cartes de contenu peuvent être filtrées sur votre application afin que seules certaines cartes spécifiques soient affichées. Ceci vous permet de disposer de plusieurs flux de cartes de contenu pour différents cas d'utilisation. Par exemple, vous pouvez gérer à la fois un flux transactionnel et un flux marketing. Pour ce faire, créez différentes catégories de cartes de contenu en définissant des paires clé-valeur dans le tableau de bord de Braze. Ensuite, créez des flux dans votre application ou votre site qui traitent ces types de cartes de contenu différemment, en filtrant certains types et en en affichant d'autres.

### Étape 1 : Définir des paires clé-valeur sur les cartes

Lors de la création d'une campagne de cartes de contenu, définissez des [données de type paire clé-valeur]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior/) sur chaque carte. Vous utiliserez cette paire clé-valeur pour classer les cartes. Les paires clé-valeur sont stockées dans la propriété `extras` du modèle de données de la carte.

Pour cet exemple, nous allons définir une paire clé-valeur avec la clé `feed_type` qui désignera dans quel flux la carte de contenu doit s’afficher. La valeur sera celle de vos flux personnalisés, par exemple `home_screen` ou `marketing`.

### Étape 2 : Filtrer les cartes de contenu

Une fois les paires clé-valeur attribuées, créez un flux avec une logique qui affichera les cartes que vous souhaitez afficher et filtrera les cartes d'autres types. Dans cet exemple, nous n'afficherons que les cartes dont la paire clé-valeur correspond à `feed_type: "Transactional"`.

{% tabs %}
{% tab Système d'affichage Android %}

Le filtrage des cartes de contenu peut être réalisé en lisant les paires clé-valeur définies dans le tableau de bord via l'option [`Card.getExtras()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html) et en filtrant (ou en exécutant toute autre logique que vous souhaitez) à l'aide d'un gestionnaire de mise à jour personnalisé.

Pour aller plus loin, votre flux de cartes de contenu est affiché dans un [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html). La version par défaut de `IContentCardsUpdateHandler` prend un [`ContentCardsUpdatedEvent`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-content-cards-updated-event/index.html) du SDK de Braze et renvoie une liste de cartes à afficher, mais ne fait que trier les cartes et n'effectue aucune suppression ni aucun filtrage de son propre chef.

Pour permettre à un `ContentCardsFragment` de filtrer, créez un [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html) personnalisé. Modifiez ce `IContentCardsUpdateHandler` pour retirer de la liste toutes les cartes qui ne correspondent pas à la valeur de `feed_type` que nous avons définie précédemment. Par exemple :

{% subtabs local %}
{% subtab Java %}

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

{% endsubtab %}
{% subtab Kotlin %}

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

{% endsubtab %}
{% endsubtabs %}

Une fois que vous avez créé un `IContentCardsUpdateHandler`, créez un `ContentCardsFragment` qui l'utilise. Ce flux personnalisé peut être utilisé comme n'importe quel autre `ContentCardsFragment`. Dans les différentes parties de votre application, affichez différents flux de cartes de contenu en fonction de la clé fournie dans le tableau de bord. Chaque flux `ContentCardsFragment` affichera un ensemble unique de cartes grâce au `IContentCardsUpdateHandler` personnalisé sur chaque fragment. 

Par exemple :

{% subtabs local %}
{% subtab Java %}

```java
// We want a Content Cards feed that only shows "Transactional" cards.
ContentCardsFragment customContentCardsFragment = new ContentCardsFragment();
customContentCardsFragment.setContentCardUpdateHandler(getUpdateHandlerForFeedType("Transactional"));
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
// We want a Content Cards feed that only shows "Transactional" cards.
val customContentCardsFragment = ContentCardsFragment()
customContentCardsFragment.contentCardUpdateHandler = getUpdateHandlerForFeedType("Transactional")
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Jetpack Compose %}
Pour filtrer les cartes de contenu affichées dans ce flux, utilisez `cardUpdateHandler`. Par exemple :

```kotlin
ContentCardsList(
     cardUpdateHandler = {
         it.filter { card ->
             card.extras["feed_type"] == "Transactional"
         }
     }
 )
 ```
{% endtab %}
{% tab iOS %}

L’exemple suivant montre le flux des cartes de contenu pour les types de cartes `Transactional` :

{% subtabs %}
{% subtab Swift %}

```swift
// Filter cards by the `Transactional` feed type based on your key-value pair.
let transactionalCards = cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
```

Pour aller plus loin, les cartes présentées dans le contrôleur de vue peuvent être filtrées en définissant la propriété `transform` sur votre structure `Attributes` afin de n'afficher que les cartes filtrées selon vos critères.

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
{% tab Web %}

L’exemple suivant montre le flux des cartes de contenu pour les types de cartes `Transactional` :

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

Ensuite, vous pouvez configurer un basculement pour votre flux personnalisé :

```javascript
// show the "Transactional" feed when this button is clicked
document.getElementById("show-transactional-feed").onclick = function() {
  showCardsByFeedType("Transactional"); 
};
```

Pour plus d'informations, consultez la [documentation sur les méthodes SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards).

{% endtab %}
{% endtabs %}


