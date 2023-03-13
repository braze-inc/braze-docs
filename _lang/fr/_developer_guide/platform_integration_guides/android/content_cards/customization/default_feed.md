---
nav_title: Personnaliser le flux
article_title: Personnaliser le flux de carte de contenu pour Android et FireOS
page_order: 4.1
platform: 
  - Android
  - FireOS
description: "Cet article couvre les options de personnalisation du flux de cartes de contenu dans votre application Android ou FireOS."
channel:
  - cartes de contenu

---

# Personnalisation du flux des cartes de contenu par défaut {#content-cards-fragment-customization}

Cette section couvre la personnalisation du [ContentCardsFragment][49][dont la source se trouve sur GitHub][54].

## Personnaliser l’ordre d’affichage des cartes {#customizing-displayed-card-order-for-android}

Le `ContentCardsFragment` repose sur un [`IContentCardsUpdateHandler`][44] pour gérer tout tri ou modification des cartes de contenu avant qu’elles ne soient affichées dans le flux. Un gestionnaire de mise à jour personnalisé peut être défini via [`setContentCardUpdateHandler`][45] sur votre [`ContentCardsFragment`][49].

Filtrer les cartes de contenu avant qu’elles ne parviennent au flux de l’utilisateur est un cas d’usage commun et peut être obtenu en lisant les paires clé-valeur définies sur le tableau de bord via [`Card.getExtras()`][36] et en effectuant la logique que vous souhaitez dans le gestionnaire de mise à jour.

La valeur suivante est la valeur par défaut `IContentCardsUpdateHandler` et peut être utilisée comme point de départ pour les personnalisations :

{% tabs %}
{% tab JAVA %}

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

{% endtab %}
{% tab KOTLIN %}

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

{% endtab %}
{% endtabs %}

Ce code peut également être trouvé ici, [DefaultContentCardsUpdateHandler][46].

Voici comment utiliser cette classe :

{% tabs %}
{% tab JAVA %}

```java
IContentCardsUpdateHandler cardUpdateHandler = new DefaultContentCardsUpdateHandler();

ContentCardsFragment fragment = getMyCustomFragment();
fragment.setContentCardUpdateHandler(cardUpdateHandler);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val cardUpdateHandler = DefaultContentCardsUpdateHandler()

val fragment = getMyCustomFragment()
fragment.setContentCardUpdateHandler(cardUpdateHandler)
```

{% endtab %}
{% endtabs %}

## Personnaliser le message d’erreur de connexion au réseau

Si le [`ContentCardsFragment`][49] détermine qu’une actualisation de la carte de contenu a échoué, il affiche un message d’erreur de connexion réseau.

Un adaptateur spécial, le [`EmptyContentCardsAdapter`][50] remplace la norme [`ContentCardAdapter`][53] pour afficher le message d’erreur. Pour définir le message personnalisé lui-même, remplacez la ressource string `com_braze_feed_empty`..

Le style utilisé pour afficher ce message peut être trouvé via [`Braze.ContentCardsDisplay.Empty`][52] et est reproduit dans l’extrait de code suivant :

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

Pour personnaliser complètement le comportement d’erreur réseau, vous pouvez étendre [`ContentCardsFragment`][54] et définir la variable `mShowNetworkUnavailableRunnable` pour effectuer une autre action.

[49]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html
[52]: https://github.com/Appboy/appboy-android-sdk/blob/2e386dfa59a87bfc24ef7cb6ff5adf6b16f44d24/android-sdk-ui/src/main/res/values/styles.xml#L522-L530
[53]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/ContentCardAdapter.kt
[54]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/ContentCardsFragment.kt
[50]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/EmptyContentCardsAdapter.kt
[36]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-card/extras.html
[44]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html
[45]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html
[46]: https://github.com/Appboy/appboy-android-sdk/blob/v11.0.0/android-sdk-ui/src/main/java/com/appboy/ui/contentcards/handlers/DefaultContentCardsUpdateHandler.java

