# Message dismissal

> This reference article covers in-app messaging dismissal for your Android or FireOS application.

## Disabling back button dismissal

By default, the hardware back button dismisses Braze in-app messages. This behavior can be disabled on a per-message basis via [`BrazeInAppMessageManager.setBackButtonDismissesInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-back-button-dismisses-in-app-message-view.html). 

In the following example, `disable_back_button` is a custom key-value pair set on the in-app message that signifies whether the message should allow for the back button to dismiss the message:

{% tabs %}
{% tab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(new DefaultInAppMessageManagerListener() {
  @Override
  public void beforeInAppMessageViewOpened(View inAppMessageView, IInAppMessage inAppMessage) {
    super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage);
    final Map<String, String> extras = inAppMessage.getExtras();
    if (extras != null && extras.containsKey("disable_back_button")) {
      BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false);
    }
  }

  @Override
  public void afterInAppMessageViewClosed(IInAppMessage inAppMessage) {
    super.afterInAppMessageViewClosed(inAppMessage);
    BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true);
  }
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(object : DefaultInAppMessageManagerListener() {
  override fun beforeInAppMessageViewOpened(inAppMessageView: View, inAppMessage: IInAppMessage) {
    super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage)
    val extras = inAppMessage.extras
    if (extras != null && extras.containsKey("disable_back_button")) {
      BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false)
    }
  }

  override fun afterInAppMessageViewClosed(inAppMessage: IInAppMessage) {
    super.afterInAppMessageViewClosed(inAppMessage)
    BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true)
  }
})
```
{% endtab %}
{% endtabs %}

{% alert note %}
Note that if this functionality is disabled, the host activity's hardware back button default behavior will be used instead. This may lead to the back button closing the application instead of the displayed in-app message.
{% endalert %}

## Dismiss modal on outside tap

The default and historical value is `false`, meaning clicks outside the modal will not close the modal. Setting this value to `true` will result in the modal in-app message being dismissed when the user taps outside of the in-app message. This behavior can be toggled on by calling:

```java
BrazeInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)
```

