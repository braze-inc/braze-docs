{% multi_lang_include developer_guide/prerequisites/android.md %} You'll also need to [set up in-app messages]({{site.baseurl}}/developer_guide/in_app_messages).

## Setting custom manager listeners

{% tabs %}
{% tab global listener %}
While the `BrazeInAppMessageManager` listener can automatically handle the display and lifecycle of in-app messages, you'll need to implement a custom manager listener if you'd like to fully customize your messages.
{% endtab %}

{% tab html listener %}
The Braze SDK has a default `DefaultHtmlInAppMessageActionListener` class that is used if no custom listener is defined and takes appropriate action automatically. If you require more control over how a user interacts with different buttons inside a custom HTML in-app message, implement a custom `IHtmlInAppMessageActionListener` class.
{% endtab %}
{% endtabs %}

### Step 1: Implement the custom manager listener

{% tabs %}
{% tab global listener %}
#### Step 1.1: Implement `IInAppMessageManagerListener` 

Create a class that implements [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html).

The callbacks in your `IInAppMessageManagerListener` will also be called at various points in the in-app message lifecycle. For example, if you set a custom manager listener when an in-app message is received from Braze, the [`beforeInAppMessageDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-displayed.html) method will be called. If your implementation of this method returns [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-c-a-r-d/index.html), that signals to Braze that the in-app message will be handled by the host app and should not be displayed by Braze. If [`InAppMessageOperation.DISPLAY_NOW`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-p-l-a-y_-n-o-w/index.html) is returned, Braze will attempt to display the in-app message. This method should be used if you choose to display the in-app message in a customized manner.

`IInAppMessageManagerListener` also includes delegate methods for message clicks and buttons, which can be used in cases like intercepting a message when a button or message is clicked for further processing.

#### Step 1.2: Hook into IAM view lifecycle methods (optional)

The [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) interface has in-app message view methods called at distinct points in the in-app message view lifecycle. These methods are called in the following order:

1. [`beforeInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-opened.html): Called just before the in-app message is added to the activity's view. The in-app message is not yet visible to the user at this time.
2. [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html): Called just after the in-app message is added to the activity's view. The in-app message is now visible to the user at this time.
3. [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html): Called just before the in-app message is removed from the activity's view. The in-app message is still visible to the user at this time.
4. [`afterInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-closed.html): Called just after the in-app message is removed from the activity's view. The in-app message is no longer visible to the user at this time.

Note that the time between [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html) and [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html) is when the in-app message view is on screen, visible to the user.

{% alert note %}
Implementation of these methods is not required. They're only provided to track and inform the in-app message view lifecycle. You can leave these method implementations empty.
{% endalert %}
{% endtab %}

{% tab html listener %}
Create a class that implements [`IHtmlInAppMessageActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html).

The callbacks in your `IHtmlInAppMessageActionListener` will be called whenever the user initiates any of the following actions inside the HTML in-app message:

- Clicks on the close button
- Fires a custom event
- Clicks on a URL inside HTML in-app message

{% subtabs %}
{% subtab JAVA %}
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
  public boolean onOtherUrlAction(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Custom url pressed: " + url + " . Ignoring", Toast.LENGTH_LONG).show();
    BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
    return true;
  }
}
```
{% endsubtab %}
{% subtab KOTLIN %}
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

    override fun onOtherUrlAction(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast.makeText(mContext, "Custom url pressed: $url . Ignoring", Toast.LENGTH_LONG).show()
        BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
        return true
    }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Step 2: Instruct Braze to use the custom manager listener

{% tabs %}
{% tab global listener %}
After you create `IInAppMessageManagerListener`, call `BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()` to instruct `BrazeInAppMessageManager`
to use your custom `IInAppMessageManagerListener` instead of the default listener. Do this in your [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) before any other calls to Braze, so the custom listener is set before any in-app messages are displayed.

#### Altering in-app messages before display

When a new in-app message is received, and there is already an in-app message being displayed, the new message will be put onto the top of the stack and can be displayed at a later time.

However, if there is no in-app message being displayed, the following delegate method in `IInAppMessageManagerListener` will be called:

{% subtabs %}
{% subtab JAVA %}
```java
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endsubtab %}
{% endsubtabs %}

The `InAppMessageOperation()` return value can control when the message should be displayed. The suggested usage of this method would be to delay messages in certain parts of the app by returning `DISPLAY_LATER` when in-app messages would be distracting to the user's app experience.

| `InAppMessageOperation` return value | Behavior |
| -------------------------- | -------- |
| `DISPLAY_NOW` | The message will be displayed |
| `DISPLAY_LATER` | The message will be returned to the stack and displayed at the next available opportunity |
| `DISCARD` | The message will be discarded |
| `null` | The message will be ignored. This method should **NOT** return `null` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

See [`InAppMessageOperation`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html) for more details.

{% alert tip %}
If you choose to `DISCARD` the in-app message and replace it with your in-app message view, you will need to log in-app message clicks and impressions manually.
{% endalert %}

On Android, this is done by calling `logClick` and `logImpression` on in-app messages and `logButtonClick` on immersive in-app messages.

{% alert tip %}
Once an in-app message has been placed on the stack, you can request for it to be retrieved and displayed at any time by calling [`BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/request-display-in-app-message.html). This method requests Braze to display the next available in-app message from the stack.
{% endalert %}
{% endtab %}

{% tab html listener %}
After your `IHtmlInAppMessageActionListener` is created, call `BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener()` to instruct `BrazeInAppMessageManager` to use your custom `IHtmlInAppMessageActionListener` instead of the default action listener.

We recommend setting your `IHtmlInAppMessageActionListener` in your [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) before any other calls to Braze. This will set the custom action listener before any in-app message is displayed:

{% subtabs %}
{% subtab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(new CustomHtmlInAppMessageActionListener(context));
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(CustomHtmlInAppMessageActionListener(context))
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Setting custom factories

You can override a number of defaults through custom factory objects. These can be registered with the Braze SDK as needed to achieve the desired results. However, if you decide to override a factory, you'll likely need to explicitly defer to the default or reimplement the functionality provided by the Braze default. The following code snippet illustrates how to supply custom implementations of the `IInAppMessageViewFactory` and the `IInAppMessageViewWrapperFactory` interfaces.

{% tabs local %}
{% tab Kotlin %}
**In-app message types**<br>

```kotlin
class BrazeDemoApplication : Application(){
 override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener(true, true))
    BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapperFactory())
    BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory(CustomInAppMessageViewFactory())
  }
}
```
{% endtab %}
{% tab Java %}
**In-app message types**<br> 

```java
public class BrazeDemoApplication extends Application {
  @Override
  public void onCreate{
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener(true, true));
    BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapperFactory());
    BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory(new CustomInAppMessageViewFactory());
  }
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab view %}
Braze in-app message types are versatile enough to cover most custom use cases. However, if you want to fully define the visual appearance of your in-app messages instead of using a default type, Braze makes this possible by setting a custom view factory.
{% endtab %}

{% tab view wrapper %}
The `BrazeInAppMessageManager` automatically handles placing the in-app message model into the existing activity view hierarchy by default using [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html). If you need to customize how in-app messages are placed into the view hierarchy, you should use a custom [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html).
{% endtab %}

{% tab animation %}
In-app messages have preset animation behavior. `Slideup` messages slide into the screen; `full` and `modal` messages fade in and out. If you want to define custom animation behaviors for your in-app messages, Braze makes this possible by setting up a custom animation factory.
{% endtab %}
{% endtabs %}

### Step 1: Implement the factory

{% tabs %}
{% tab view %}
Create a class that implements [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html):

{% subtabs %}
{% subtab JAVA %}
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
{% endsubtab %}
{% subtab KOTLIN %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab view wrapper %}
Create a class that implements [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) and returns an [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html).

This factory is called immediately after the in-app message view is created. The easiest way to implement a custom [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) is just to extend the default [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html):

{% subtabs %}
{% subtab JAVA %}
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
{% endsubtab %}
{% subtab KOTLIN %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab animation %}
Create a class that implements [`IInAppMessageAnimationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-animation-factory/index.html):

{% subtabs %}
{% subtab JAVA %}
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
{% endsubtab %}
{% subtab KOTLIN %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Step 2: Instruct Braze to use the factory

{% tabs %}
{% tab view %}
After your `IInAppMessageViewFactory` is created, call `BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()` to instruct `BrazeInAppMessageManager`
to use your custom `IInAppMessageViewFactory` instead of the default view factory.

{% alert tip %}
We recommend setting your `IInAppMessageViewFactory` in your `Application.onCreate()` before any other calls to Braze. This will set the custom view factory before any in-app message is displayed.
{% endalert %}

#### How it works

The `slideup` in-app message view implements [`IInAppMessageView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-view/index.html). The `full` and `modal` type message views implement [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html). Implementing one of these classes allows Braze to add click listeners to your custom view where appropriate. All Braze view classes extend Android's [`View`](http://developer.android.com/reference/android/view/View.html) class.

Implementing `IInAppMessageView` allows you to define a certain portion of your custom view as clickable. Implementing [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html) allows you to define message button views and a close button view.
{% endtab %}

{% tab view wrapper %}
After your [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) is created, call [`BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-custom-in-app-message-view-factory.html) to instruct `BrazeInAppMessageManager` to use your custom [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) instead of the default view wrapper factory.

We recommend setting your [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) in your [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) before any other calls to Braze. This will set the custom view wrapper factory before any in-app message is displayed:

{% subtabs %}
{% subtab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapper());
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapper())
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab animation %}
Once your `IInAppMessageAnimationFactory` is created, call `BrazeInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory()` to instruct `BrazeInAppMessageManager`
to use your custom `IInAppMessageAnimationFactory` instead of the default animation factory.

We recommend setting your `IInAppMessageAnimationFactory` in your [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) before any other calls to Braze. This will set the custom animation factory before any in-app message is displayed.
{% endtab %}
{% endtabs %}

## Custom styles

Braze UI elements come with a default look and feel that matches the Android standard UI guidelines and provides a seamless experience. This reference article covers custom in-app messaging styling for your Android or FireOS application.

### Setting a default style

You can see default styles in the Braze SDK's [`styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml) file:

```xml
  <style name="Braze"/>
  <style name="Braze.InAppMessage"/>
  <style name="Braze.InAppMessage.Header">
    <item name="android:layout_height">wrap_content</item>
    <item name="android:layout_width">match_parent</item>
    <item name="android:padding">0.0dp</item>
    <item name="android:background">@android:color/transparent</item>
    <item name="android:textColor">@color/com_braze_inappmessage_header_text</item>
    <item name="android:textSize">20.0sp</item>
    <item name="android:lineSpacingMultiplier">1.3</item>
    <item name="android:gravity">center</item>
    <item name="android:textStyle">bold</item>
    <item name="android:layout_centerHorizontal">true</item>
  </style>
```

If you would prefer, you can override these styles to create a look and feel that better suits your app.

To override a style, copy it in its entirety to the `styles.xml` file in your project and make modifications. The whole style must be copied over to your local `styles.xml` file for all attributes to be correctly set. Note that these custom styles are for changes to individual UI elements, not wholesale changes to layouts. Layout-level changes need to be handled with custom views.

{% alert note %}
You can customize some colors directly in your Braze campaign without modifying the XML. Keep in mind, colors set in the Braze dashboard will override colors you set anywhere else.
{% endalert %}

### Customizing the font

You can set a custom font by locating the typeface in the `res/font` directory. To use it, override the style for message text, headers, and button text and use the `fontFamily` attribute to instruct Braze to use your custom font family.

For example, to update the font on your in-app message button text, override the `Braze.InAppMessage.Button` style and reference your custom font family. The attribute value should point to a font family in your `res/font` directory.

Here is a truncated example with a custom font family, `my_custom_font_family`, referenced on the last line:

```xml
  <style name="Braze.InAppMessage.Button">
    <item name="android:layout_height">wrap_content</item>
    ...
    <item name="android:paddingBottom">15.0dp</item>
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Aside from the `Braze.InAppMessage.Button` style for button text, the style for message text is `Braze.InAppMessage.Message` and the style for message headers is `Braze.InAppMessage.Header`. If you want to use your custom font family across all possible in-app message text, you can set your font family on the `Braze.InAppMessage` style, which is the parent style for all in-app messages.

{% alert important %}
As with other custom styles, the entire style must be copied over to your local `styles.xml` file for all attributes to be correctly set.
{% endalert %}

## Message dismissals

### Disabling back button dismissals

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

### Enabling outside tap dismissals

By default, dismissing the modal using an outside tap is set to `false`. Setting this value to `true` will result in the modal in-app message being dismissed when the user taps outside of the in-app message. This behavior can be toggled on by calling:

```java
BrazeInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)
```

## Customizing the orientation

To set a fixed orientation for an in-app message, first [set a custom in-app message manager listener]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners). Then, update the orientation on the `IInAppMessage` object in the `beforeInAppMessageDisplayed()` delegate method:

{% tabs %}
{% tab JAVA %}
```java
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  // Set the orientation to portrait
  inAppMessage.setOrientation(Orientation.PORTRAIT);
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
  // Set the orientation to portrait
  inAppMessage.orientation = Orientation.PORTRAIT
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endtab %}
{% endtabs %}

For tablet devices, in-app messages will appear in the user's preferred orientation style regardless of actual screen orientation.

## Disabling dark theme {#android-in-app-message-dark-theme-customization}

By default, `IInAppMessageManagerListener`'s `beforeInAppMessageDisplayed()` checks the system settings and conditionally enables dark theme styling on the message with the following code:

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

To change this, you can call [`enableDarkTheme`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-themeable/enable-dark-theme.html) at any step in the pre-display process to implement your own conditional logic.

## Customizing the Google Play review prompt

Due to the limitations and restrictions set by Google, custom Google Play review prompts are not currently supported by Braze. While some users have been able to integrate these prompts successfully, others have shown low success rates due to [Google Play quotas](https://developer.android.com/guide/playcore/in-app-review#quotas). Integrate at your own risk. Refer to documentation on [Google Play in-app review prompts](https://developer.android.com/guide/playcore/in-app-review).
