---
nav_title: Customizing Feed
article_title: Customizing Content Card Feed for Android and FireOS
page_order: 4.1
platform: 
  - Android
  - FireOS
description: "This article covers Content Card feed customization options for your Android or FireOS application."
channel:
  - content cards

---

# Customizing the default Content Card feed {#content-cards-fragment-customization}

This section covers customization of the [ContentCardsFragment][49] whose source can be found [here][54].

## Customizing displayed card order {#customizing-displayed-card-order-for-android}

The `ContentCardsFragment` relies on a [`IContentCardsUpdateHandler`][44] to handle any sorting or modifications of Content Cards before they are displayed in the feed. A custom update handler can be set via [`setContentCardUpdateHandler`][45] on your [`ContentCardsFragment`][49].

Filtering out Content Cards before they reach the user's feed is a common use-case and could be achieved by reading the key-value pairs set on the dashboard via [`Card.getExtras()`][36] and performing any logic you'd like in the update handler.

The following is the default `IContentCardsUpdateHandler` and can be used as a starting point for customizations:

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

This code can also be found here, [DefaultContentCardsUpdateHandler][46].

And here's how to use this class:

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

## Customizing the network connection error message

If the [`ContentCardsFragment`][49] determines that a Content Card refresh has failed, it will display a network connection error message.

A special adapter, the [`AppboyEmptyContentCardsAdapter`][50] replaces the standard [`AppboyCardAdapter`][53] to display the error message. To set the custom message itself, override the string resource `com_appboy_feed_empty`.

The style used to display this message can be found via [`Appboy.ContentCardsDisplay.Empty`][52] and is reproduced in the following code snippet:

```xml
<style name="Braze.ContentCardsDisplay.Empty">
  <item name="android:lineSpacingExtra">1.5dp</item>
  <item name="android:text">@string/com_appboy_feed_empty</item>
  <item name="android:textColor">@color/com_appboy_title</item>
  <item name="android:textSize">18.0sp</item>
  <item name="android:gravity">center</item>
  <item name="android:layout_height">match_parent</item>
  <item name="android:layout_width">match_parent</item>
</style>
```

To fully customize the network error behavior, you can extend the [`ContentCardsFragment`][54] and set the `mShowNetworkUnavailableRunnable` variable to perform some other action.

[49]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html
[52]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml#L552-L560
[53]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.ui.contentcards/-appboy-empty-content-cards-adapter/index.html
[54]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/ContentCardsFragment.java
[50]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.ui.contentcards/-appboy-empty-content-cards-adapter/index.html
[36]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-card/get-extras.html
[44]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html
[45]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html
[46]: https://github.com/Appboy/appboy-android-sdk/blob/v11.0.0/android-sdk-ui/src/main/java/com/appboy/ui/contentcards/handlers/DefaultContentCardsUpdateHandler.java

