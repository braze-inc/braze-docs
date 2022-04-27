---
nav_title: Handling Clicks Manually
article_title: Handling Content Card Clicks Manually for Android and FireOS
page_order: 4.2
platform: 
  - Android
  - FireOS
description: "This article covers how to handle Content Card clicks manually in your Android ofr FireOS application."
channel:
  - content cards

---

# Handling clicks manually

You can handle Content Cards clicks manually by setting a custom click listener. This enables use cases such as selectively using the native web browser to open web links.

Create a class that implements [`IContentCardsActionListener`][43] and register it with `BrazeContentCardsManager`. Implement the `onContentCardClicked()` method, which will be called when the user clicks a Content Card. Next, instruct Braze to use your Content Card click listener. The following code snippet shows an example click listener:

{% tabs %}
{% tab JAVA %}

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

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeContentCardsManager.getInstance().contentCardsActionListener = object : IContentCardsActionListener {
  override fun onContentCardClicked(context: Context, card: Card, cardAction: IAction): Boolean {
    return false
  }

  override fun onContentCardDismissed(context: Context, card: Card) {

  }
}
```

{% endtab %}
{% endtabs %}

[43]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html
