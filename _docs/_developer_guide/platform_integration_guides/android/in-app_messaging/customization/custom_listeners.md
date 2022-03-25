---
nav_title: Custom Listeners
article_title: Custom In-App Message Listeners for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 3
description: "This reference article covers in-app messaging customization options for your Android application."
channel:
  - in-app messages

---

# Setting custom listeners

Before customizing in-app messages with custom listeners, it's important to understand the [`BrazeInAppMessageManager`][34], which handles the majority of in-app message handling. As described in [step 1][5] of the in-app message integration guide, it must be registered for in-app messages to function appropriately.

`BrazeInAppMessageManager` manages in-app message display on Android. It contains helper class instances that help it manage the lifecycle and display of in-app messages. All of these classes have standard implementations and defining custom classes is completely optional. However, doing so can add another level of control over the display and behavior of in-app messages. These customizable classes include:

- [`IInAppMessageManagerListener`][21] - [Custom manage in-app message display and behavior](#setting-a-custom-manager-listener)
- [`IInAppMessageViewFactory`][42] - [Build custom in-app message views](#setting-a-custom-view-factory)
- [`IInAppMessageAnimationFactory`][20] - [Define custom in-app message animations](#setting-a-custom-animation-factory)
- [`IHtmlInAppMessageActionListener`][86] - [Custom manage HTML in-app message display and behavior](#setting-a-custom-html-in-app-message-action-listener)
- [`IInAppMessageViewWrapperFactory`][88] - [Custom manage in-app message view hierarchy interaction](#setting-a-custom-view-wrapper-factory)

## Custom manager listener

The `BrazeInAppMessageManager` automatically handles the display and lifecycle of in-app messages. If you require more control over the lifecycle of a message, setting a custom manager listener will enable you to receive the in-app message object at various points in the in-app message lifecycle, allowing you to handle its display yourself, perform further processing, react to user behavior, process the object's [extras][14], and much more.

### Step 1: Implement an in-app message manager listener

Create a class that implements [`IInAppMessageManagerListener`][21].

The callbacks in your `IInAppMessageManagerListener` will be called at various points in the in-app message lifecycle.

For example, if you set a custom manager listener when an in-app message is received from Braze, the `beforeInAppMessageDisplayed()` method will be called. If your implementation of this method returns [`InAppMessageOperation.DISCARD`][83], that signals to Braze that the in-app message will be handled by the host app and should not be displayed by Braze. If `InAppMessageOperation.DISPLAY_NOW` is returned, Braze will attempt to display the in-app message. This method should be used if you choose to display the in-app message in a customized manner.

`IInAppMessageManagerListener` also includes delegate methods for clicks on the message itself or one of the buttons. A common use case would be intercepting a message when a button or message is clicked for further processing.

### Step 2: Hook into in-app message view lifecycle methods (optional)

The [`IInAppMessageManagerListener`][21] interface has in-app message view methods called at distinct points in the in-app message view lifecycle. These methods are called in the following order:

- [`beforeInAppMessageViewOpened`][92] - Called just before the in-app message is added to the activity's view. The in-app message is not yet visible to the user at this time.
- [`afterInAppMessageViewOpened`][93] - Called just after the in-app message is added to the activity's view. The in-app message is now visible to the user at this time.
- [`beforeInAppMessageViewClosed`][94] - Called just before the in-app message is removed from the activity's view. The in-app message is still visible to the user at this time.
- [`afterInAppMessageViewClosed`][95] - Called just after the in-app message is removed from the activity's view. The in-app message is no longer visible to the user at this time.

For further context, the time between [`afterInAppMessageViewOpened`][93] and [`beforeInAppMessageViewClosed`][94] is when the in-app message view is on screen, visible to the user.

{% alert note %}
Implementation of these methods is not required. They are merely provided to track and inform the in-app message view lifecycle. It is functionally acceptable to leave these method implementations empty.
{% endalert %}

### Step 3: Instruct Braze to use your in-app message manager listener

Once your `IInAppMessageManagerListener` is created, call `BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()` to instruct `BrazeInAppMessageManager`
to use your custom `IInAppMessageManagerListener` instead of the default listener.

We recommend setting your `IInAppMessageManagerListener` in your [`Application.onCreate()`][82] before any other calls to Braze. This will ensure that the custom listener is set before any in-app message is displayed.

#### Altering in-app messages before display

When a new in-app message is received, and there is already an in-app message being displayed, the new message will be put onto the top of the stack and can be displayed at a later time.

However, if there is no in-app message being displayed, the following delegate method in `IInAppMessageManagerListener` will be called:

{% tabs %}
{% tab JAVA %}
```java
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessageBase) {
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessageBase: IInAppMessage): InAppMessageOperation {
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endtab %}
{% endtabs %}

The `InAppMessageOperation()` return value can control when the message should be displayed. The suggested usage of this method would be to delay messages in certain parts of the app by returning `DISPLAY_LATER` when in-app messages would be distracting to the user's app experience.

| `InAppMessageOperation` return value | Behavior |
| -------------------------- | -------- |
| `DISPLAY_NOW` | The message will be displayed |
| `DISPLAY_LATER` | The message will be returned to the stack and displayed at the next available opportunity |
| `DISCARD` | The message will be discarded |
| `null` | The message will be ignored. This method should **NOT** return `null` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

See [`InAppMessageOperation.java`][45] for more details.

{% alert tip %}
If you choose to `DISCARD` the in-app message and replace it with your in-app message view, you will need to log in-app message clicks and impressions manually.
{% endalert %}

On Android, this is done by calling `logClick` and `logImpression` on in-app messages and `logButtonClick` on immersive in-app messages.

{% alert tip %}
Once an in-app message has been placed on the stack, you can request for it to be retrieved and displayed at any time by calling [`BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()`](https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html#requestDisplayInAppMessage--). This method requests Braze to display the next available in-app message from the stack.
{% endalert %}

### Step 4: Customizing dark theme behavior (optional) {#android-in-app-message-dark-theme-customization}

In the default `IInAppMessageManagerListener` logic, in `beforeInAppMessageDisplayed()`, the system settings are checked and conditionally enable dark theme styling on the message with the following code:

{% tabs %}
{% tab JAVA %}
```java
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  if (inAppMessage instanceof IInAppMessageThemeable && ViewUtils.isDeviceInNightMode(BrazeInAppMessageManager.getInstance().getApplicationContext())) {
    ((IInAppMessageThemeable) inAppMessage).enableDarkTheme();
  }
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
  if (inAppMessage is IInAppMessageThemeable && ViewUtils.isDeviceInNightMode(BrazeInAppMessageManager.getInstance().applicationContext!!)) {
    (inAppMessage as IInAppMessageThemeable).enableDarkTheme()
  }
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endtab %}
{% endtabs %}

If you want to use your own conditional logic, you can call [`enableDarkTheme`][97] at any step in the pre-display process.

## Custom view factory

Braze's suite of in-app message types is versatile enough to cover most custom use cases. However, if you would like to fully define the visual appearance of your in-app messages instead of using a default type, Braze makes this possible by setting a custom view factory.

### Step 1: Implement an in-app message view factory

Create a class that implements [`IInAppMessageViewFactory`][87]:

{% tabs %}
{% tab JAVA %}
```java
public class CustomInAppMessageViewFactory implements IInAppMessageViewFactory {
  @Override
  public View createInAppMessageView(Activity activity, IInAppMessage inAppMessage) {
    // Uses a custom view for slideups, modals, and full in-app messages.
    // HTML in-app messages and any other types will use the Braze default in-app message view factories
    switch (inAppMessage.getMessageType()) {
      case SLIDEUP:
      case MODAL:
      case FULL:
        // Use a custom view of your choosing
        return createMyCustomInAppMessageView();
      default:
        // Use the default in-app message factories
        final IInAppMessageViewFactory defaultInAppMessageViewFactory = BrazeInAppMessageManager.getInstance().getDefaultInAppMessageViewFactory(inAppMessage);
        return defaultInAppMessageViewFactory.createInAppMessageView(activity, inAppMessage);
    }
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
class CustomInAppMessageViewFactory : IInAppMessageViewFactory {
  override fun createInAppMessageView(activity: Activity, inAppMessage: IInAppMessage): View {
    // Uses a custom view for slideups, modals, and full in-app messages.
    // HTML in-app messages and any other types will use the Braze default in-app message view factories
    when (inAppMessage.messageType) {
      MessageType.SLIDEUP, MessageType.MODAL, MessageType.FULL ->
        // Use a custom view of your choosing
        return createMyCustomInAppMessageView()
      else -> {
        // Use the default in-app message factories
        val defaultInAppMessageViewFactory = BrazeInAppMessageManager.getInstance().getDefaultInAppMessageViewFactory(inAppMessage)
        return defaultInAppMessageViewFactory!!.createInAppMessageView(activity, inAppMessage)
      }
    }
  }
}
```
{% endtab %}
{% endtabs %}

### Step 2: Instruct Braze to use your in-app message view factory

Once your `IInAppMessageViewFactory` is created, call `BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()` to instruct `BrazeInAppMessageManager`
to use your custom `IInAppMessageViewFactory` instead of the default view factory.

{% alert tip %}
We recommend setting your `IInAppMessageViewFactory` in your `Application.onCreate()` before any other calls to Braze. This will ensure that the custom view factory is set before any in-app message is displayed.
{% endalert %}

#### Implementing a Braze view interface

Braze's `slideup` in-app message view implements [`IInAppMessageView`][25].  Braze's `full` and `modal` type message views implement [`IInAppMessageImmersiveView`][24]. Implementing one of these classes will allow Braze to add click listeners to your custom view where appropriate. All Braze view classes extend Android's [`View`][18] class.

Implementing `IInAppMessageView` allows you to define a certain portion of your custom view as clickable. Implementing [`IInAppMessageImmersiveView`][24] allows you to define message button views and a close button view.

## Custom animation factory

In-app messages have preset animation behavior. `Slideup` messages slide into the screen; `full` and `modal` messages fade in and out. If you want to define custom animation behaviors for your in-app messages, Braze makes this possible by setting up a custom animation factory.

### Step 1: Implement an in-app message animation factory

Create a class that implements [`IInAppMessageAnimationFactory`][20]:

{% tabs %}
{% tab JAVA %}
```java
public class CustomInAppMessageAnimationFactory implements IInAppMessageAnimationFactory {

  @Override
  public Animation getOpeningAnimation(IInAppMessage inAppMessage) {
    Animation animation = new AlphaAnimation(0, 1);
    animation.setInterpolator(new AccelerateInterpolator());
    animation.setDuration(2000L);
    return animation;
  }

  @Override
  public Animation getClosingAnimation(IInAppMessage inAppMessage) {
    Animation animation = new AlphaAnimation(1, 0);
    animation.setInterpolator(new DecelerateInterpolator());
    animation.setDuration(2000L);
    return animation;
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
class CustomInAppMessageAnimationFactory : IInAppMessageAnimationFactory {
  override fun getOpeningAnimation(inAppMessage: IInAppMessage): Animation {
    val animation: Animation = AlphaAnimation(0, 1)
    animation.interpolator = AccelerateInterpolator()
    animation.duration = 2000L
    return animation
  }

  override fun getClosingAnimation(inAppMessage: IInAppMessage): Animation {
    val animation: Animation = AlphaAnimation(1, 0)
    animation.interpolator = DecelerateInterpolator()
    animation.duration = 2000L
    return animation
  }
}
```
{% endtab %}
{% endtabs %}

### Step 2: Instruct Braze to use your in-app message view factory

Once your `IInAppMessageAnimationFactory` is created, call `BrazeInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory()` to instruct `BrazeInAppMessageManager`
to use your custom `IInAppMessageAnimationFactory` instead of the default animation factory.

We recommend setting your `IInAppMessageAnimationFactory` in your [`Application.onCreate()`][82] before any other calls to Braze. This will ensure that the custom animation factory is set before any in-app message is displayed.

## Custom HTML in-app message action listener

The Braze SDK has a default `DefaultHtmlInAppMessageActionListener` class that is used if no custom listener is defined and takes appropriate action automatically. If you require more control over how a user interacts with different buttons inside a custom HTML in-app message, implement a custom `IHtmlInAppMessageActionListener` class.

### Step 1: Implement a custom HTML in-app message action listener

Create a class that implements [`IHtmlInAppMessageActionListener`][86].

The callbacks in your `IHtmlInAppMessageActionListener` will be called whenever the user initiates any of the following actions inside the HTML in-app message:
- Clicks on the close button.
- Clicks on the News Feed button.
- Fires a custom event.
- Clicks on a URL inside HTML in-app message.

{% tabs %}
{% tab JAVA %}
```java
public class CustomHtmlInAppMessageActionListener implements IHtmlInAppMessageActionListener {
  private final Context mContext;

  public CustomHtmlInAppMessageActionListener(Context context) {
    mContext = context;
  }

  @Override
  public void onCloseClicked(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "HTML In App Message closed", Toast.LENGTH_LONG).show();
    BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
  }

  @Override
  public boolean onCustomEventFired(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Custom event fired. Ignoring.", Toast.LENGTH_LONG).show();
    return true;
  }

  @Override
  public boolean onNewsfeedClicked(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Newsfeed button pressed. Ignoring.", Toast.LENGTH_LONG).show();
    BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
    return true;
  }

  @Override
  public boolean onOtherUrlAction(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Custom url pressed: " + url + " . Ignoring", Toast.LENGTH_LONG).show();
    BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
    return true;
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
class CustomHtmlInAppMessageActionListener(private val mContext: Context) : IHtmlInAppMessageActionListener {

    override fun onCloseClicked(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle) {
        Toast.makeText(mContext, "HTML In App Message closed", Toast.LENGTH_LONG).show()
        BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
    }

    override fun onCustomEventFired(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast.makeText(mContext, "Custom event fired. Ignoring.", Toast.LENGTH_LONG).show()
        return true
    }

    override fun onNewsfeedClicked(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast.makeText(mContext, "Newsfeed button pressed. Ignoring.", Toast.LENGTH_LONG).show()
        BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
        return true
    }

    override fun onOtherUrlAction(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast.makeText(mContext, "Custom url pressed: $url . Ignoring", Toast.LENGTH_LONG).show()
        BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
        return true
    }
}
```
{% endtab %}
{% endtabs %}

### Step 2: Instruct Braze to use your HTML in-app message action listener

Once your `IHtmlInAppMessageActionListener` is created, call `BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener()` to instruct `BrazeInAppMessageManager` to use your custom `IHtmlInAppMessageActionListener` instead of the default action listener.

We recommend setting your `IHtmlInAppMessageActionListener` in your [`Application.onCreate()`][82] before any other calls to Braze. This will ensure that the custom action listener is set before any in-app message is displayed:

{% tabs %}
{% tab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(new CustomHtmlInAppMessageActionListener(context));
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(CustomHtmlInAppMessageActionListener(context))
```
{% endtab %}
{% endtabs %}

## Custom view wrapper factory

The `BrazeInAppMessageManager` automatically handles placing the in-app message model into the existing activity view hierarchy by default using [`DefaultInAppMessageViewWrapper`][89]. If you need to customize how in-app messages are placed into the view hierarchy, you should use a custom [`IInAppMessageViewWrapperFactory`][88].

### Step 1: Implement an in-app message view wrapper factory

Create a class that implements [`IInAppMessageViewWrapperFactory`][88] and returns an [`IInAppMessageViewWrapper`][90].

This factory is called immediately after the in-app message view is created. The easiest way to implement a custom [`IInAppMessageViewWrapper`][90] is just to extend the default [`DefaultInAppMessageViewWrapper`][89]:

{% tabs %}
{% tab JAVA %}
```java
public class CustomInAppMessageViewWrapper extends DefaultInAppMessageViewWrapper {
  public CustomInAppMessageViewWrapper(View inAppMessageView,
                                       IInAppMessage inAppMessage,
                                       IInAppMessageViewLifecycleListener inAppMessageViewLifecycleListener,
                                       BrazeConfigurationProvider brazeConfigurationProvider,
                                       Animation openingAnimation,
                                       Animation closingAnimation, View clickableInAppMessageView) {
    super(inAppMessageView,
        inAppMessage,
        inAppMessageViewLifecycleListener,
        brazeConfigurationProvider,
        openingAnimation,
        closingAnimation,
        clickableInAppMessageView);
  }

  @Override
  public void open(@NonNull Activity activity) {
    super.open(activity);
    Toast.makeText(activity.getApplicationContext(), "Opened in-app message", Toast.LENGTH_SHORT).show();
  }

  @Override
  public void close() {
    super.close();
    Toast.makeText(mInAppMessageView.getContext().getApplicationContext(), "Closed in-app message", Toast.LENGTH_SHORT).show();
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
class CustomInAppMessageViewWrapper(inAppMessageView: View,
                                    inAppMessage: IInAppMessage,
                                    inAppMessageViewLifecycleListener: IInAppMessageViewLifecycleListener,
                                    brazeConfigurationProvider: BrazeConfigurationProvider,
                                    openingAnimation: Animation,
                                    closingAnimation: Animation, clickableInAppMessageView: View) : 
    DefaultInAppMessageViewWrapper(inAppMessageView, 
        inAppMessage, 
        inAppMessageViewLifecycleListener, 
        brazeConfigurationProvider, 
        openingAnimation, 
        closingAnimation, 
        clickableInAppMessageView) {

  override fun open(activity: Activity) {
    super.open(activity)
    Toast.makeText(activity.applicationContext, "Opened in-app message", Toast.LENGTH_SHORT).show()
  }

  override fun close() {
    super.close()
    Toast.makeText(mInAppMessageView.context.applicationContext, "Closed in-app message", Toast.LENGTH_SHORT).show()
  }
}
```
{% endtab %}
{% endtabs %}

### Step 2: Instruct Braze to use your custom view wrapper factory

Once your [`IInAppMessageViewWrapper`][90] is created, call [`BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory()`][91] to instruct `BrazeInAppMessageManager` to use your custom [`IInAppMessageViewWrapperFactory`][88] instead of the default view wrapper factory.

We recommend setting your [`IInAppMessageViewWrapperFactory`][88] in your [`Application.onCreate()`][82] before any other calls to Braze. This will ensure that the custom view wrapper factory is set before any in-app message is displayed:

{% tabs %}
{% tab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapper());
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapper())
```
{% endtab %}
{% endtabs %}

[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/#step-1-braze-in-app-message-manager-registration
[14]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/key-value_pairs/
[18]: http://developer.android.com/reference/android/view/View.html
[20]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.ui.inappmessage/-i-in-app-message-animation-factory/index.html
[21]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html
[24]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html
[25]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/java/com/appboy/ui/inappmessage/IInAppMessageView.java
[34]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html
[42]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.ui.inappmessage/-i-in-app-message-view-factory/index.html
[45]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html
[82]: https://developer.android.com/reference/android/app/Application.html#onCreate()
[83]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html#DISCARD
[86]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html
[87]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.ui.inappmessage/-i-in-app-message-view-factory/index.html
[88]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html
[90]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.ui.inappmessage/-i-in-app-message-view-wrapper/index.html
[91]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-custom-in-app-message-view-factory.html
[92]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html#beforeInAppMessageViewOpened-android.view.View-com.braze.models.inappmessage.IInAppMessage-
[93]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html#afterInAppMessageViewOpened-android.view.View-com.braze.models.inappmessage.IInAppMessage-
[94]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html#beforeInAppMessageViewClosed-android.view.View-com.braze.models.inappmessage.IInAppMessage-
[95]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html#afterInAppMessageViewClosed-com.braze.models.inappmessage.IInAppMessage-
[97]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-themeable/enable-dark-theme.html
[98]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html#requestDisplayInAppMessage--
[89]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html
