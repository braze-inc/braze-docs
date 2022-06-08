---
nav_title: Multiple Feeds
article_title: Using Multiple Content Card Feeds for Android and FireOS
page_order: 5
platform: 
  - Android
  - FireOS
description: "This reference article covers how to implement multiple Content Card feeds in your Android or FireOS application."
channel:
  - content cards

---

# Using multiple Content Card feeds

Content Cards can be filtered on the app to only display specific cards, enabling you to have multiple Content Card feeds for different use cases (for example, a transactional feed or a marketing feed).

The following documentation demonstrates an example implementation that can be changed to fit your specific integration.

## Step 1: Setting key-value pairs on cards

When creating a Content Card campaign, key-value pair data can be set on each card. Our filtering logic will use this key-value pair data to categorize cards. Note that we do not recommend sending nested JSON values as key-value pairs. Instead, we recommend flattening the JSON before sending it. 

For this example, we'll set a key-value pair with the key `feed_type` that will designate which Content Card feed the card should be displayed in. The value will be whatever your custom feeds will be, as in `Transactional`, `Marketing`, and more.

## Step 2: Create a Content Card update handler

To perform filtering on a [`ContentCardsFragment`][1], we will create a use a custom [`IContentCardsUpdateHandler`][2]. A [`IContentCardsUpdateHandler`][2] takes a [`ContentCardsUpdatedEvent`][3] from the Braze SDK and returns a list of cards to display.

In our example handler, we'll first sort the cards using the default [`IContentCardsUpdateHandler`][2]. The default Braze [`IContentCardsUpdateHandler`][2] only sorts cards and, by default, doesn't perform any removals or filtering on its own. Next, we'll remove any cards from the list that don't match our desired value for the `feed_type` that we set earlier:

{% tabs %}
{% tab JAVA %}

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
{% endtab %}
{% tab KOTLIN %}

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
{% endtab %}
{% endtabs %}

## Step 3: Create a Content Card feed using the custom update handler

Now that we have a custom [`IContentCardsUpdateHandler`][2], we can create a [`ContentCardsFragment`][1] that uses it. In the following example code, we'll create a [`ContentCardsFragment`][1] that only displays cards where the `feed_type` is "Transactional":

{% tabs %}
{% tab JAVA %}

```java
// We want a Content Cards feed that only shows "Transactional" cards.
ContentCardsFragment customContentCardsFragment = new ContentCardsFragment();
customContentCardsFragment.setContentCardUpdateHandler(getUpdateHandlerForFeedType("Transactional"));
```
{% endtab %}
{% tab KOTLIN %}

```kotlin
// We want a Content Cards feed that only shows "Transactional" cards.
val customContentCardsFragment = ContentCardsFragment()
customContentCardsFragment.contentCardUpdateHandler = getUpdateHandlerForFeedType("Transactional")
```
{% endtab %}
{% endtabs %}

## Step 4: Using the Content Cards fragment

This custom feed can be used like any other [`ContentCardsFragment`][1]. In the different parts of your app, you can display different Content Card feeds based on the key provided on the dashboard. Each [`ContentCardsFragment`][1] feed will have a unique set of cards displayed thanks to the custom [`IContentCardsUpdateHandler`][2] on each fragment.

When creating a Content Card campaign, set your key-value pair where the key is `feed_type` and the value is `Transactional`.

[1]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html
[2]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html
[3]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.events/-content-cards-updated-event/index.html
