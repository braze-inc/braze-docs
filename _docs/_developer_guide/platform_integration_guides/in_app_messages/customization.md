---
nav_title: Customization
page_order: 2
description: ""
---

# Customization

> Combine Android, iOS, Web, and FireOS. Combine with tabs and subtabs for code snippets?

Android & FireOS:


# Customization {#in-app-message-customization}

All of Braze’s in-app message types are highly customizable across messages, images, [Font Awesome][15]  icons, click actions, analytics, editable styling, custom display options, and custom delivery options. Multiple options can be configured on a per in-app message basis from [within the dashboard]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/). Braze additionally provides multiple levels of advanced customization to satisfy a variety of use cases and needs.

## Key Value Pair Extras

In-app message objects may carry key-value pairs as `extras`. They are specified on the dashboard under "Advanced Settings" when creating an in-app message campaign. These can be used to send data down along with an in-app message for further handling by the application.

Call the following when you get an in-app message object to retrieve its extras:

{% tabs %}
{% tab JAVA %}

```java
Map<String, String> getExtras()
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
extras: Map<String, String>
```

{% endtab %}
{% endtabs %}

See the [Javadoc][44] for more information.

## Custom Styling

Braze UI elements come with a default look and feel that matches the Android standard UI guidelines and provides a seamless experience. You can see these default styles in the Braze SDK's [`styles.xml`][6] file.

```xml
  <style name="Appboy"/>
    <!-- In-app Message -->
  <style name="Appboy.InAppMessage">
  </style>
  <style name="Appboy.InAppMessage.Header">
    <item name="android:layout_height">wrap_content</item>
    <item name="android:layout_width">wrap_content</item>
    <item name="android:padding">0.0dp</item>
    <item name="android:background">@android:color/transparent</item>
    <item name="android:textColor">@color/com_appboy_inappmessage_header_text_light</item>
    <item name="android:textSize">19.0sp</item>
    <item name="android:layout_gravity">center</item>
    <item name="android:singleLine">true</item>
    <item name="android:textStyle">bold</item>
  </style>
```

If you would prefer, you can override these styles to create a look and feel that better suits your app.

To override a style, copy it in its entirety to the `styles.xml` file in your project and make modifications. The whole style must be copied over to your local `styles.xml` file for all attributes to be correctly set. Please note that these custom styles are for changes to individual UI elements, not wholesale changes to layouts. Layout-level changes need to be handled with custom views.

### Using Custom Styling to Set a Custom Font

Braze allows for setting a custom font using the [font family guide][79]. To use it, override the style for message text, headers, and/or button text and use the `fontFamily` attribute to instruct Braze to use your custom font family.

For example, to update the font on your in-app message button text, override the `Appboy.InAppMessage.Button` style and reference your custom font family. The attribute value should point to a font family in your `res/font` directory.

Here is a truncated example with a custom font family, `my_custom_font_family`, referenced on the last line:

```xml
  <style name="Appboy.InAppMessage.Button">
    <item name="android:layout_height">wrap_content</item>
    ...
    <item name="android:paddingBottom">15.0dp</item>
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Aside from the `Appboy.InAppMessage.Button` style for button text, the style for message text is `Appboy.InAppMessage.Message` and the style for message headers is `Appboy.InAppMessage.Header`. If you want to use your custom font family across all possible in-app message text, you can set your font family on the `Appboy.InAppMessage` style, which is the parent style for all in-app messages.

{% alert important %}
As with other custom styles, the entire style must be copied over to your local `styles.xml` file for all attributes to be correctly set.
{% endalert %}

## Setting Custom Listeners

Before customizing in-app messages with custom listeners, it's important to understand the [`AppboyInAppMessageManager`][34], which handles the majority of in-app message handling. As described in [Step 1][5], it must be registered for in-app messages to function appropriately.

`AppboyInAppMessageManager` manages in-app message display on Android.  It contains helper class instances that help it manage the lifecycle and display of in-app messages. All of these classes have standard implementations and defining custom classes is completely optional. However, doing so can add another level of control over the display and behavior of in-app messages.  These customizable classes include:

- [`IInAppMessageManagerListener`][21] - Implement to [custom manage in-app message display and behavior](#setting-a-custom-manager-listener).
- [`IInAppMessageViewFactory`][42] - Implement to [build custom in-app message views](#setting-a-custom-view-factory).
- [`IInAppMessageAnimationFactory`][20] - Implement to [define custom in-app message animations](#setting-a-custom-animation-factory).
- [`IHtmlInAppMessageActionListener`][86] - Implement to [custom manage HTML in-app message display and behavior](#setting-a-custom-html-in-app-message-action-listener).
- [`IInAppMessageViewWrapperFactory`][88] - Implement to [custom manage in-app message view hierarchy interaction](#setting-a-custom-view-wrapper-factory).

### Custom Manager Listener

The `AppboyInAppMessageManager` automatically handles the display and lifecycle of in-app messages.  If you require more control over the lifecycle of a message, setting a custom manager listener will enable you to receive the in-app message object at various points in the in-app message lifecycle, allowing you to handle its display yourself, perform further processing, react to user behavior, process the object's [Extras][14], and much more.

#### Step 1: Implement an In-App Message Manager Listener

Create a class that implements [`IInAppMessageManagerListener`][21].

The callbacks in your `IInAppMessageManagerListener` will be called at various points in the in-app message lifecycle.

For example, if you set a custom manager listener when an in-app message is received from Braze, the `beforeInAppMessageDisplayed()` method will be called. If your implementation of this method returns [`InAppMessageOperation.DISCARD`][83], that signals to Braze that the in-app message will be handled by the host app and should not be displayed by Braze. If `InAppMessageOperation.DISPLAY_NOW` is returned, Braze will attempt to display the in-app message. This method should be used if you choose to display the in-app message in a customized manner.

`IInAppMessageManagerListener` also includes delegate methods for clicks on the message itself or one of the buttons.  A common use case would be intercepting a message when a button or message is clicked for further processing.

#### Step 2: Hook into In-App Message View Lifecycle Methods (Optional)

The [`IInAppMessageManagerListener`][21] interface has in-app message view methods that are called at distinct points in the in-app message view lifecycle. These methods are called in the following order:

- [beforeInAppMessageViewOpened][92] - Called just before the in-app message is added to the Activity's view. The in-app message is not yet visible to the user at this time.
- [afterInAppMessageViewOpened][93] - Called just after the in-app message is added to the Activity's view. The in-app message is now visible to the user at this time.
- [beforeInAppMessageViewClosed][94] - Called just before the in-app message is removed from the Activity's view. The in-app message is still visible to the user at this time.
- [afterInAppMessageViewClosed][95] - Called just after the in-app message is removed from the Activity's view. The in-app message is no longer visible to the user at this time.

For further context, the time between [afterInAppMessageViewOpened][93] and [beforeInAppMessageViewClosed][94] is when the in-app message view is on screen, visible to the user.

{% alert note %}
  No implementation of these methods is required. They are merely provided to track/inform of the in-app message view lifecycle. It is functionally acceptable to leave these method implementations empty.
{% endalert %}

#### Step 3: Instruct Braze to use your In-App Message Manager Listener

Once your `IInAppMessageManagerListener` is created, call `AppboyInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()` to instruct `AppboyInAppMessageManager`
to use your custom `IInAppMessageManagerListener` instead of the default listener.

We recommend setting your `IInAppMessageManagerListener` in your [`Application.onCreate()`][82] before any other calls to Braze. This will ensure that the custom listener is set before any in-app message is displayed.

##### In-Depth: Altering In-App Messages Before Display

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

The `InAppMessageOperation()` return value can be used to control when the message should be displayed. The suggested usage of this method would be to delay messages in certain parts of the app by returning `DISPLAY_LATER` when in-app messages would be distracting to the user's app experience.

| `InAppMessageOperation` return value | Behavior |
| -------------------------- | -------- |
| `DISPLAY_NOW` | The message will be displayed |
| `DISPLAY_LATER` | The message will be returned to the stack and displayed at the next available opportunity |
| `DISCARD` | The message will be discarded |
| `null` | The message will be ignored. This method should __NOT__ return `null` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

See [`InAppMessageOperation.java`][45] for more details.

{% alert tip %}
If you choose to `DISCARD` the in-app message and replace it with your own in-app message view, you will need to manually log in-app message clicks and impressions.
{% endalert %}

On Android, this is done by calling `logClick` and `logImpression` on in-app messages, and `logButtonClick` on immersive in-app messages.

{% alert tip %}
Once an in-app message has been placed on the stack, you can request for it to be retrieved and displayed at any time by calling [`AppboyInAppMessageManager.getInstance().requestDisplayInAppMessage()`](https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#requestDisplayInAppMessage--). Calling this method requests Braze to display the next available in-app message from the stack.
{% endalert %}

#### Step 4: Customizing Dark Theme Behavior (Optional) {#android-in-app-message-dark-theme-customization}

In the default `IInAppMessageManagerListener` logic, in `beforeInAppMessageDisplayed()`, the system settings are checked and conditionally enable Dark Theme styling on the message with the following code:

{% tabs %}
{% tab JAVA %}

```java
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  if (inAppMessage instanceof IInAppMessageThemeable && ViewUtils.isDeviceInNightMode(AppboyInAppMessageManager.getInstance().getApplicationContext())) {
    ((IInAppMessageThemeable) inAppMessage).enableDarkTheme();
  }
  return InAppMessageOperation.DISPLAY_NOW;
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
  if (inAppMessage is IInAppMessageThemeable && ViewUtils.isDeviceInNightMode(AppboyInAppMessageManager.getInstance().applicationContext!!)) {
    (inAppMessage as IInAppMessageThemeable).enableDarkTheme()
  }
  return InAppMessageOperation.DISPLAY_NOW
}
```

{% endtab %}
{% endtabs %}

If you would like to use your own conditional logic, then you can call [`enableDarkTheme`][97] at any step in the pre-display process.

### Custom View Factory

Braze's suite of in-app message types is versatile enough to cover the vast majority of custom use cases. However, if you would like to fully define the visual appearance of your in-app messages instead of using a default type, Braze makes this possible by setting a custom view factory.

#### Step 1: Implement an In-App Message View Factory

Create a class that implements [`IInAppMessageViewFactory`][87].

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
        final IInAppMessageViewFactory defaultInAppMessageViewFactory = AppboyInAppMessageManager.getInstance().getDefaultInAppMessageViewFactory(inAppMessage);
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
        val defaultInAppMessageViewFactory = AppboyInAppMessageManager.getInstance().getDefaultInAppMessageViewFactory(inAppMessage)
        return defaultInAppMessageViewFactory!!.createInAppMessageView(activity, inAppMessage)
      }
    }
  }
}
```

{% endtab %}
{% endtabs %}

#### Step 2: Instruct Braze to use your In-App Message View Factory

Once your `IInAppMessageViewFactory` is created, call `AppboyInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()` to instruct `AppboyInAppMessageManager`
to use your custom `IInAppMessageViewFactory` instead of the default view factory.

{% alert tip %}
We recommend setting your `IInAppMessageViewFactory` in your `Application.onCreate()` before any other calls to Braze. This will ensure that the custom view factory is set before any in-app message is displayed.
{% endalert %}

##### In-Depth: Implementing a Braze View Interface

Braze's `slideup` in-app message view implements [`IInAppMessageView`][25].  Braze's `full` and `modal` type message views implement [`IInAppMessageImmersiveView`][24].  Implementing one of these classes will allow Braze to add click listeners to your custom view where appropriate.  All Braze view classes extend Android's [View][18] class.

Implementing `IInAppMessageView` allows you to define a certain portion of your custom view as clickable. Implementing [`IInAppMessageImmersiveView`][24] allows you to define message button views and a close button view.

### Custom Animation Factory

In-app messages have preset animation behavior. `Slideup` type messages slide into the screen; `full` and `modal` messages fade in and out.  If you would like to define custom animation behaviors for your in-app messages, Braze makes this possible by setting a custom animation factory.

#### Step 1: Implement an In-App Message Animation Factory

Create a class that implements [`IInAppMessageAnimationFactory`][20]

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

#### Step 2: Instruct Braze to use your In-App Message View Factory

Once your `IInAppMessageAnimationFactory` is created, call `AppboyInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory()` to instruct `AppboyInAppMessageManager`
to use your custom `IInAppMessageAnimationFactory` instead of the default animation factory.

We recommend setting your `IInAppMessageAnimationFactory` in your [`Application.onCreate()`][82] before any other calls to Braze. This will ensure that the custom animation factory is set before any in-app message is displayed.

### Custom HTML In-App Message Action Listener

The Braze SDK has a default `AppboyDefaultHtmlInAppMessageActionListener` class that is used if no custom listener is defined and takes appropriate action automatically. If you require more control over how a user interacts with different buttons inside a custom HTML in-app message, implement a custom `IHtmlInAppMessageActionListener` class.

#### Step 1: Implement a Custom HTML In-App Message Action Listener

Create a class that implements [`IHtmlInAppMessageActionListener`][86].

The callbacks in your `IHtmlInAppMessageActionListener` will be called whenever the user initiates any of the following actions inside the HTML in-app message:
- Clicks on close button.
- Clicks on News Feed button.
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
    AppboyInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
  }

  @Override
  public boolean onCustomEventFired(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Custom event fired. Ignoring.", Toast.LENGTH_LONG).show();
    return true;
  }

  @Override
  public boolean onNewsfeedClicked(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Newsfeed button pressed. Ignoring.", Toast.LENGTH_LONG).show();
    AppboyInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
    return true;
  }

  @Override
  public boolean onOtherUrlAction(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Custom url pressed: " + url + " . Ignoring", Toast.LENGTH_LONG).show();
    AppboyInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
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
        AppboyInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
    }

    override fun onCustomEventFired(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast.makeText(mContext, "Custom event fired. Ignoring.", Toast.LENGTH_LONG).show()
        return true
    }

    override fun onNewsfeedClicked(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast.makeText(mContext, "Newsfeed button pressed. Ignoring.", Toast.LENGTH_LONG).show()
        AppboyInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
        return true
    }

    override fun onOtherUrlAction(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast.makeText(mContext, "Custom url pressed: $url . Ignoring", Toast.LENGTH_LONG).show()
        AppboyInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
        return true
    }
}
```

{% endtab %}
{% endtabs %}

#### Step 2: Instruct Braze to use your HTML In-App Message Action Listener

Once your `IHtmlInAppMessageActionListener` is created, call `AppboyInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener()` to instruct `AppboyInAppMessageManager` to use your custom `IHtmlInAppMessageActionListener` instead of the default action listener.

We recommend setting your `IHtmlInAppMessageActionListener` in your [`Application.onCreate()`][82] before any other calls to Braze. This will ensure that the custom action listener is set before any in-app message is displayed.

{% tabs %}
{% tab JAVA %}

```java
AppboyInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(new CustomHtmlInAppMessageActionListener(context));
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
AppboyInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(CustomHtmlInAppMessageActionListener(context))
```

{% endtab %}
{% endtabs %}

### Custom View Wrapper Factory

The `AppboyInAppMessageManager` automatically handles placing the in-app message model into the existing Activity view hierarchy by default using [`DefaultInAppMessageViewWrapper`][89]. If you need to customize how in-app messages are placed into the view hierarchy, you should use a custom [`IInAppMessageViewWrapperFactory`][88].

#### Step 1: Implement an In-App Message View Wrapper Factory

Create a class that implements [`IInAppMessageViewWrapperFactory`][88] and returns an [IInAppMessageViewWrapper][90].

This factory is called immediately after the in-app message view is created. The easiest way to implement a custom [IInAppMessageViewWrapper][90] is just to extend the default [`DefaultInAppMessageViewWrapper`][89].

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

#### Step 2: Instruct Braze to use your Custom View Wrapper Factory

Once your [IInAppMessageViewWrapper][90] is created, call [`AppboyInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory()`][91] to instruct `AppboyInAppMessageManager` to use your custom [`IInAppMessageViewWrapperFactory`][88] instead of the default view wrapper factory.

We recommend setting your [`IInAppMessageViewWrapperFactory`][88] in your [`Application.onCreate()`][82] before any other calls to Braze. This will ensure that the custom view wrapper factory is set before any in-app message is displayed.

{% tabs %}
{% tab JAVA %}

```java
AppboyInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapper());
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
AppboyInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapper())
```

{% endtab %}
{% endtabs %}

## Setting Fixed Orientation

To set a fixed orientation for an in-app message, first [set a custom in-app message manager listener][19]. Then, call `setOrientation()` on the `IInAppMessage` object in the `beforeInAppMessageDisplayed()` delegate method.

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


For *tablet* devices, in-app messages will appear in the style of the user's preferred orientation regardless of actual screen orientation.

## Disabling Back Button Dismissal

By default, the hardware back button dismisses Braze In-App Messages. This behavior can be disabled on a per-message basis via [`AppboyInAppMessageManager.setBackButtonDismissesInAppMessageView()`][96]. 

In the following example, `disable_back_button` is a custom key-value pair set on the In-App Message that signifies whether the message should allow for the back button to dismiss the message.

{% tabs %}
{% tab JAVA %}

```java
AppboyInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(new AppboyDefaultInAppMessageManagerListener() {
  @Override
  public void beforeInAppMessageViewOpened(View inAppMessageView, IInAppMessage inAppMessage) {
    super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage);
    final Map<String, String> extras = inAppMessage.getExtras();
    if (extras != null && extras.containsKey("disable_back_button")) {
      AppboyInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false);
    }
  }

  @Override
  public void afterInAppMessageViewClosed(IInAppMessage inAppMessage) {
    super.afterInAppMessageViewClosed(inAppMessage);
    AppboyInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true);
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
AppboyInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(object : AppboyDefaultInAppMessageManagerListener() {
  override fun beforeInAppMessageViewOpened(inAppMessageView: View, inAppMessage: IInAppMessage) {
    super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage)
    val extras = inAppMessage.extras
    if (extras != null && extras.containsKey("disable_back_button")) {
      AppboyInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false)
    }
  }

  override fun afterInAppMessageViewClosed(inAppMessage: IInAppMessage) {
    super.afterInAppMessageViewClosed(inAppMessage)
    AppboyInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true)
  }
})
```

{% endtab %}
{% endtabs %}

{% alert note %}
Note that if this functionality is disabled, the host Activity's hardware back button default behavior will be used instead. This may lead to the back button instead of closing the application instead of the displayed in-app message.
{% endalert %}


## GIFs {#gifs-IAMs}

Braze requires an external image library to display animated GIFs with {{ include.channel }}.

### Custom Image Library Integration {#gifs-delegate-integration}

Braze offers the ability to use a custom image library to display animated GIFs with {{ include.channel }}.

__Note:__ Although the example below uses [Glide][gifs-67], any image library that supports GIFs is compatible.

#### Step 1: Creating the Image Loader Delegate

The Image Loader delegate must implement the following methods:

* [`getInAppMessageBitmapFromUrl()`][gifs-71]
* [`getPushBitmapFromUrl()`][gifs-72]
* [`renderUrlIntoCardView()`][gifs-73]
* [`renderUrlIntoInAppMessageView()`][gifs-74]
* [`setOffline()`][gifs-70]

The integration example below is taken from the [Glide Integration Sample App][gifs-65] included with the Braze Android SDK.

{% tabs %}
{% tab JAVA %}

```java
public class GlideAppboyImageLoader implements IAppboyImageLoader {
  private static final String TAG = GlideAppboyImageLoader.class.getName();

  private RequestOptions mRequestOptions = new RequestOptions();

  @Override
  public void renderUrlIntoCardView(Context context, Card card, String imageUrl, ImageView imageView, AppboyViewBounds viewBounds) {
    renderUrlIntoView(context, imageUrl, imageView, viewBounds);
  }

  @Override
  public void renderUrlIntoInAppMessageView(Context context, IInAppMessage inAppMessage, String imageUrl, ImageView imageView, AppboyViewBounds viewBounds) {
    renderUrlIntoView(context, imageUrl, imageView, viewBounds);
  }

  @Override
  public Bitmap getPushBitmapFromUrl(Context context, Bundle extras, String imageUrl, AppboyViewBounds viewBounds) {
    return getBitmapFromUrl(context, imageUrl, viewBounds);
  }

  @Override
  public Bitmap getInAppMessageBitmapFromUrl(Context context, IInAppMessage inAppMessage, String imageUrl, AppboyViewBounds viewBounds) {
    return getBitmapFromUrl(context, imageUrl, viewBounds);
  }

  private void renderUrlIntoView(Context context, String imageUrl, ImageView imageView, AppboyViewBounds viewBounds) {
    Glide.with(context)
        .load(imageUrl)
        .apply(mRequestOptions)
        .into(imageView);
  }

  private Bitmap getBitmapFromUrl(Context context, String imageUrl, AppboyViewBounds viewBounds) {
    try {
      return Glide.with(context)
          .asBitmap()
          .apply(mRequestOptions)
          .load(imageUrl).submit().get();
    } catch (Exception e) {
      Log.e(TAG, "Failed to retrieve bitmap at url: " + imageUrl, e);
    }
    return null;
  }

  @Override
  public void setOffline(boolean isOffline) {
    // If the loader is offline, then we should only be retrieving from the cache
    mRequestOptions = mRequestOptions.onlyRetrieveFromCache(isOffline);
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class GlideAppboyImageLoader : IAppboyImageLoader {
  companion object {
    private val TAG = GlideAppboyImageLoader::class.qualifiedName
  }

  private var mRequestOptions = RequestOptions()

  override fun renderUrlIntoCardView(context: Context, card: Card, imageUrl: String, imageView: ImageView, viewBounds: AppboyViewBounds) {
    renderUrlIntoView(context, imageUrl, imageView, viewBounds)
  }

  override fun renderUrlIntoInAppMessageView(context: Context, inAppMessage: IInAppMessage, imageUrl: String, imageView: ImageView, viewBounds: AppboyViewBounds) {
    renderUrlIntoView(context, imageUrl, imageView, viewBounds)
  }

  override fun getPushBitmapFromUrl(context: Context, extras: Bundle, imageUrl: String, viewBounds: AppboyViewBounds): Bitmap? {
    return getBitmapFromUrl(context, imageUrl, viewBounds)
  }

  override fun getInAppMessageBitmapFromUrl(context: Context, inAppMessage: IInAppMessage, imageUrl: String, viewBounds: AppboyViewBounds): Bitmap? {
    return getBitmapFromUrl(context, imageUrl, viewBounds)
  }

  private fun renderUrlIntoView(context: Context, imageUrl: String, imageView: ImageView, viewBounds: AppboyViewBounds) {
    Glide.with(context)
        .load(imageUrl)
        .apply(mRequestOptions)
        .into(imageView)
  }

  private fun getBitmapFromUrl(context: Context, imageUrl: String, viewBounds: AppboyViewBounds): Bitmap? {
    try {
      return Glide.with(context)
          .asBitmap()
          .apply(mRequestOptions)
          .load(imageUrl).submit().get()
    } catch (e: Exception) {
      Log.e(TAG, "Failed to retrieve bitmap at url: $imageUrl", e)
    }

    return null
  }

  override fun setOffline(isOffline: Boolean) {
    // If the loader is offline, then we should only be retrieving from the cache
    mRequestOptions = mRequestOptions.onlyRetrieveFromCache(isOffline)
  }
}
```

{% endtab %}
{% endtabs %}

#### Step 2: Setting the Image Loader Delegate

The Braze SDK will use any custom image loader set with [setAppboyImageLoader][gifs-66]. Note that we recommend setting the custom image loader in a custom application subclass.

{% tabs %}
{% tab JAVA %}

```java
public class GlideIntegrationApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    Appboy.getInstance(context).setAppboyImageLoader(new GlideAppboyImageLoader());
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class GlideIntegrationApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    Appboy.getInstance(context).appboyImageLoader = GlideAppboyImageLoader()
  }
}
```

{% endtab %}
{% endtabs %}

## Android Dialogs

Braze doesn't support displaying in-app messages in [Android Dialogs][85] at this time.

## Google Play In-App Review Prompt

Due to the limitations and restrictions set by Google, custom Google Play review prompts are not currently supported by Braze. While some users have been able to integrate these prompts successfully, others have shown low success rates due to [Google Play quotas](https://developer.android.com/guide/playcore/in-app-review#quotas). Please integrate at your own risk. Documentation on Google Play in-app review prompts can be found [here](https://developer.android.com/guide/playcore/in-app-review).

## Youtube in HTML In-App messages

Youtube and other HTML5 content can play in HTML in-app messages. This requires hardware acceleration to be enabled in the Activity where the in-app message is being displayed, please see the [Android developer guide][84] for more details. Hardware acceleration is only available on Android API versions 11 and above.

The following is an example of an embedded Youtube video in an HTML snippet:

```html
<body>
    <div class="box">
        <div class="relativeTopRight">
            <a href="appboy://close">X</a>
        </div>
        <iframe width="60%" height="50%" src="https://www.youtube.com/embed/_x45EB3BWqI">
        </iframe>
    </div>
</body>
```


[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/#step-1-braze-in-app-message-manager-registration
[6]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml
[14]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/key-value_pairs/
[15]: http://fortawesome.github.io/Font-Awesome/
[18]: http://developer.android.com/reference/android/view/View.html
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/#setting-custom-listeners
[20]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/IInAppMessageAnimationFactory.html
[21]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/listeners/IInAppMessageManagerListener.html
[24]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/IInAppMessageImmersiveView.html
[25]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/java/com/appboy/ui/inappmessage/IInAppMessageView.java
[34]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/java/com/appboy/ui/inappmessage/AppboyInAppMessageManager.java
[42]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/IInAppMessageViewFactory.html
[44]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessage.html#getExtras--
[45]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/java/com/appboy/ui/inappmessage/InAppMessageOperation.java
[79]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization
[82]: https://developer.android.com/reference/android/app/Application.html#onCreate()
[83]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/java/com/appboy/ui/inappmessage/InAppMessageOperation.java
[84]: https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling
[85]: https://developer.android.com/guide/topics/ui/dialogs.html
[86]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/listeners/IHtmlInAppMessageActionListener.html
[87]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/IInAppMessageViewFactory.html
[88]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/IInAppMessageViewWrapperFactory.html
[89]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/java/com/appboy/ui/inappmessage/DefaultInAppMessageViewWrapper.java
[90]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/IInAppMessageViewWrapper.html
[91]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManagerBase.html#setCustomInAppMessageViewWrapperFactory-com.appboy.ui.inappmessage.IInAppMessageViewWrapperFactory-
[92]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/listeners/IInAppMessageManagerListener.html#beforeInAppMessageViewOpened-android.view.View-com.appboy.models.IInAppMessage-
[93]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/listeners/IInAppMessageManagerListener.html#afterInAppMessageViewOpened-android.view.View-com.appboy.models.IInAppMessage-
[94]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/listeners/IInAppMessageManagerListener.html#beforeInAppMessageViewClosed-android.view.View-com.appboy.models.IInAppMessage-
[95]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/listeners/IInAppMessageManagerListener.html#afterInAppMessageViewClosed-com.appboy.models.IInAppMessage-
[96]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManagerBase.html#setBackButtonDismissesInAppMessageView-boolean-
[97]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessageThemeable.html#enableDarkTheme--
[gifs-56]: http://developer.android.com/reference/android/app/Application.html
[gifs-59]: https://github.com/Appboy/appboy-android-sdk#version-support
[gifs-60]: http://developer.android.com/guide/topics/manifest/application-element.html#nm
[gifs-61]: https://github.com/Appboy/appboy-android-sdk/tree/master/droidboy
[gifs-64]: https://github.com/Appboy/appboy-android-sdk/tree/master/droidboy
[gifs-65]: https://github.com/Appboy/appboy-android-sdk/tree/master/samples/glide-image-integration
[gifs-66]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#setAppboyImageLoader-com.appboy.IAppboyImageLoader-
[gifs-67]: https://bumptech.github.io/glide/
[gifs-70]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/IAppboyImageLoader.html#setOffline-boolean-
[gifs-71]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/IAppboyImageLoader.html#getInAppMessageBitmapFromUrl-android.content.Context-com.appboy.models.IInAppMessage-java.lang.String-com.appboy.enums.AppboyViewBounds-
[gifs-72]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/IAppboyImageLoader.html#getPushBitmapFromUrl-android.content.Context-android.os.Bundle-java.lang.String-com.appboy.enums.AppboyViewBounds-
[gifs-73]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/IAppboyImageLoader.html#renderUrlIntoCardView-android.content.Context-com.appboy.models.cards.Card-java.lang.String-android.widget.ImageView-com.appboy.enums.AppboyViewBounds-
[gifs-74]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/IAppboyImageLoader.html#renderUrlIntoInAppMessageView-android.content.Context-com.appboy.models.IInAppMessage-java.lang.String-android.widget.ImageView-com.appboy.enums.AppboyViewBounds-

iOS:

# Customization {#in-app-message-customization}

All of Braze's in-app message types are highly customizable across messages, images, [Font Awesome][26] icons, click actions, analytics, editable styling, custom display options, and custom delivery options. Multiple options can be configured on a per in-app message basis from [within the dashboard][13]. Braze additionally provides multiple levels of advanced customization to satisfy a variety of use cases and needs.

{% alert important %}
By default, in-app messages are enabled after completing the standard SDK integration, including GIF support.
<br><br>
__Note that integration of `SDWebImage` is required if you plan on using our Braze UI for displaying images__ within iOS In-App Messages, News Feed, or Content Cards.
{% endalert %}

## Key Value Pair Extras

`ABKInAppMessage` objects may carry key-value pairs as `extras`. These are specified on the dashboard when creating a campaign. Key-value pairs can be used to send data down along with an in-app message for further handling by your app.

## Setting Delegates

In-app message display and delivery customizations can be accomplished in code by setting our optional delegates.

### In-App Message Delegate

The [`ABKInAppMessageUIDelegate`][34] delegate can be used to receive triggered in-app message payloads for further processing, receive display lifecycle events, and control display timing. 

Set your `ABKInAppMessageUIDelegate` delegate object on the Braze instance by calling:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController.setInAppMessageUIDelegate(self);
```

{% endtab %}
{% endtabs %}

See our [in-app message sample app][35] for an example. Note that if you are not including Braze's UI library in your project (uncommon), this delegate is unavailable.

### Core In-App Message Delegate

If you are not including Braze's UI library in your project and would like to receive triggered in-app message payloads for further processing or custom display in your app, implement the [`ABKInAppMessageControllerDelegate`][16] protocol.

Set your `ABKInAppMessageControllerDelegate` delegate object on the Braze instance by calling:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy sharedInstance].inAppMessageController.delegate = self;
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.delegate = self
```

{% endtab %}
{% endtabs %}

You can alternatively set your core in-app message delegate at initialization time via `appboyOptions` using the key `ABKInAppMessageControllerDelegateKey`.
{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKInAppMessageControllerDelegateKey : self }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKInAppMessageControllerDelegateKey : self ])
```
{% endtab %}
{% endtabs %}

## Customizing Orientation

### Setting Orientation For All In-App Messages

To set a fixed orientation for all in-app messages, you can set the `supportedOrientationMask` property on `ABKInAppMessageUIController`. Add the following code after your app's call to `startWithApiKey:inApplication:withLaunchOptions:`:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Set fixed in-app message orientation to portrait.
// Use UIInterfaceOrientationMaskLandscape to display in-app messages in landscape
id<ABKInAppMessageUIControlling> inAppMessageUIController = [Appboy sharedInstance].inAppMessageController.inAppMessageUIController;
((ABKInAppMessageUIController *)inAppMessageUIController).supportedOrientationMask = UIInterfaceOrientationMaskPortrait;
```

{% endtab %}
{% tab swift %}

```swift
// Set fixed in-app message orientation to portrait
// Use .landscape to display in-app messages in landscape
if let controller = Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController as? ABKInAppMessageUIController {
  controller.supportedOrientationMask = .portrait
}
```

{% endtab %}
{% endtabs %}

Following this, all in-app messages will be displayed in the supported orientation, regardless of device orientation. Please note that the device orientation must also be supported by the in-app message's `orientation` property in order for the message to display. For more information, see the section below.

### Setting Orientation Per In-App Message

You may alternatively set orientation on a per-message basis. To do this, [set an in-app message delegate][23]. Then, in your `beforeInAppMessageDisplayed:` delegate method, set the `orientation` property on the `ABKInAppMessage`. For example:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Set inAppMessage orientation to portrait
inAppMessage.orientation = ABKInAppMessageOrientationPortrait;

// Set inAppMessage orientation to landscape
inAppMessage.orientation = ABKInAppMessageOrientationLandscape;
```

{% endtab %}
{% tab swift %}

```swift    
  // Set inAppMessage orientation to portrait
  inAppMessage.orientation = ABKInAppMessageOrientation.portrait

  // Set inAppMessage orientation to landscape
  inAppMessage.orientation = ABKInAppMessageOrientation.landscape
```

{% endtab %}
{% endtabs %}

In-app messages will not display if the device orientation does not match the `orientation` property on the in-app message.

For *iPads*, in-app messages will appear in the style of the user's preferred orientation regardless of actual screen orientation.

## Custom Handling In-App Message Display

When the [`ABKInAppMessageControllerDelegate`][16] is set, the following delegate method will be called before in-app messages are displayed:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageDisplayChoice
```

{% endtab %}
{% endtabs %}

If you have only implemented [`ABKInAppMessageUIDelegate`][34], the following UI delegate method will be called instead:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage withKeyboardIsUp:(BOOL)keyboardIsUp;
```

{% endtab %}
{% tab swift %}

```swift
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!, withKeyboardIsUp keyboardIsUp: Bool) -> ABKInAppMessageDisplayChoice
```

{% endtab %}
{% endtabs %}

You can customize in-app message handling by implementing this delegate method and returning one of the following values for `ABKInAppMessageDisplayChoice`:

| `ABKInAppMessageDisplayChoice` | Behavior |
| -------------------------- | -------- |
| `ABKDisplayInAppMessageNow` | The message will be displayed immediately |
| `ABKDisplayInAppMessageLater` | The message will be not be displayed and will be placed back on the top of the stack |
| `ABKDiscardInAppMessage` | The message will be discarded and will not be displayed |

You can use the `beforeInAppMessageDisplayed:` delegate method to add in-app message display logic, customize in-app messages before Braze displays them, or opt-out of Braze's in-app message display logic and UI entirely.

For an implementation example, see our [In-App Message Sample Application][36].

### Overriding In-App Messages Before Display

If you would like to alter the display behavior of in-app messages, you should add any necessary display logic to your `beforeInAppMessageDisplayed:` delegate method. For example, you might want to display the in-app message from the top of the screen if the keyboard is currently being displayed, or take the in-app message data model and display the in-app message yourself.

If the IAM campaign is not displaying when the session has been started, make sure you have the necessary display logic added to your `beforeInAppMessageDisplayed:` delegate method. This allows the IAM campaign to display from the top of the screen even if the keyboard is being displayed.

### Hiding the Status Bar During Display

For `Full` and `HTML` in-app messages, the SDK will attempt to place the message over the status bar by default. However, in some cases the status bar may still appear on top of the in-app message. As of version [3.21.1 of the iOS SDK](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3211), you can force the status bar to hide when displaying `Full` and `HTML` in-app messages by setting `ABKInAppMessageHideStatusBarKey` to `YES` within the `appboyOptions` passed to `startWithApiKey:`.

### Logging Impressions and Clicks

Logging in-app message impressions and clicks is not automatic when you implement completely custom handling (*i.e.* if you circumvent Braze's in-app message display by returning `ABKDiscardInAppMessage` in your `beforeInAppMessageDisplayed:`). If you choose to implement your own UI using our in-app message models, you must log analytics with the following methods on the `ABKInAppMessage` class:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Registers that a user has viewed an in-app message with the Braze server.
- (void) logInAppMessageImpression;
// Registers that a user has clicked on an in-app message with the Braze server.
- (void) logInAppMessageClicked;
```

{% endtab %}
{% tab swift %}

```swift
// Registers that a user has viewed a in-app message with the Braze server.
func logInAppMessageImpression()
// Registers that a user has clicked on a in-app message with the Braze server.
func logInAppMessageClicked()
```

{% endtab %}
{% endtabs %}

Furthermore, you should be logging button clicks on subclasses of `ABKInAppMessageImmersive` (*i.e*., `Modal` and `Full` in-app messages):

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Logs button click analytics
- (void)logInAppMessageClickedWithButtonID:(NSInteger)buttonID;
```

{% endtab %}
{% tab swift %}

```swift
// Logs button click analytics
func logInAppMessageClickedWithButtonID(buttonId: NSInteger)
```

{% endtab %}
{% endtabs %}

## Customizing In-App Message Behavior on Click
The `inAppMessageClickActionType` property on the `ABKInAppMessage` defines the action behavior after the in-app message is clicked. This property is read-only. If you want to change the in-app message's click behavior, you can call the following method on `ABKInAppMessage`:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[inAppMessage setInAppMessageClickAction:clickActionType withURI:uri];
```

{% endtab %}
{% tab swift %}

```swift
inAppMessage.setInAppMessageClickAction(clickActionType: clickActionType, withURI: uri)
```

{% endtab %}
{% endtabs %}

The `inAppMessageClickActionType` can be set to one of the following values:

| `ABKInAppMessageClickActionType` | On-Click Behavior |
| -------------------------- | -------- |
| `ABKInAppMessageDisplayNewsFeed` | The News Feed will be displayed when the message is clicked, and the message will be dismissed. **Note**: The `uri` parameter will be ignored, and the `uri` property on the `ABKInAppMessage` will be set to nil. |
| `ABKInAppMessageRedirectToURI` | The given URI will be displayed when the message is clicked, and the message will be dismissed. **Note**: The `uri` parameter cannot be nil. |
| `ABKInAppMessageNoneClickAction` | The message will be dismissed when clicked. **Note**: The `uri` parameter will be ignored, and the `uri` property on the `ABKInAppMessage` will be set to nil. |

### Customizing In-App Message Body Clicks

The following [`ABKInAppMessageUIDelegate`][34] delegate method is called when an in-app message is clicked:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL) onInAppMessageClicked:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func onInAppMessageClicked(inAppMessage: ABKInAppMessage!) -> Bool
```

{% endtab %}
{% endtabs %}

### Customizing In-App Message Button Clicks

For clicks on in-app message buttons and HTML in-app message buttons (*i.e.*, links), [`ABKInAppMessageUIDelegate`][34] includes the following delegate methods:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)onInAppMessageButtonClicked:(ABKInAppMessageImmersive *)inAppMessage
                             button:(ABKInAppMessageButton *)button;

- (BOOL)onInAppMessageHTMLButtonClicked:(ABKInAppMessageHTML *)inAppMessage
                             clickedURL:(nullable NSURL *)clickedURL
                               buttonID:(NSString *)buttonID;
```

{% endtab %}
{% tab swift %}

```swift
func onInAppMessageButtonClicked(inAppMessage: ABKInAppMessageImmersive!,
                                 button: ABKInAppMessageButton) -> Bool

func onInAppMessageHTMLButtonClicked(inAppMessage: ABKInAppMessageHTML!,
                                     clickedURL: URL, buttonID: String) -> Bool
```

{% endtab %}
{% endtabs %}

Each method returns a `BOOL` value to indicate if Braze should continue to execute the click action.

To access the click action type of a button in a delegate method, you can use the following code:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
if ([inAppMessage isKindOfClass:[ABKInAppMessageImmersive class]]) {
      ABKInAppMessageImmersive *immersiveIAM = (ABKInAppMessageImmersive *)inAppMessage;
      NSArray<ABKInAppMessageButton *> *buttons = immersiveIAM.buttons;
      for (ABKInAppMessageButton *button in buttons) {
         // Button action type is accessible via button.buttonClickActionType
      }
   }
```

{% endtab %}
{% tab swift %}

```swift
if inAppMessage is ABKInAppMessageImmersive {
      let immersiveIAM = inAppMessage as! ABKInAppMessageImmersive;
      for button in inAppMessage.buttons as! [ABKInAppMessageButton]{
        // Button action type is accessible via button.buttonClickActionType
      }
    }
```

{% endtab %}
{% endtabs %}

>  When an in-app message has buttons, the only click actions that will be executed are the ones on the ABKInAppMessageButton model. The in-app message body will not be clickable even though the ABKInAppMessage model will have the default click action ("News Feed") assigned.

## Dismiss Modal on Outside Tap

The default value is `NO`. This determines if the modal in-app message will be dismissed when the user taps outside of the in-app message.

To enable outside tap dismissals, add a dictionary named `Braze` to your `Info.plist` file. Inside the `Braze` Dictionary add the `DismissModalOnOutsideTap` boolean subentry and set the value to `YES`. Note that prior to Braze iOS SDK v4.0.2, the dictionary key `Appboy` must be used in place of `Braze`.

Example `Info.plist` contents:

```
<key>Braze</key>
<dict>
	<key>DismissModalOnOutsideTap</key>
	<boolean>YES</boolean>
</dict>
```

### Description of Dismiss Modal on Outside Tap

| DismissModalOnOutsideTap | Description |
|----------|-------------|
| YES       | Modal in-app messages will be dismissed on outside tap     |
| NO        | Default, modal in-app messages will not be dismissed on outside tap |
{: .reset-td-br-1 .reset-td-br-2}

## Display In-App Messages In a Custom View Controller

In-app messages can also be displayed within a custom view controller which you pass to Braze. Braze will animate the customized in-app message in and out, as well as handle analytics of the in-app message. The view controller must meet the following requirements:

- It must be a subclass or an instance of `ABKInAppMessageViewController`.
- The view of the returned view controller should be an instance of `ABKInAppMessageView` or its subclass.

The following UI delegate method is called every time an in-app message is offered to `ABKInAppMessageViewController` to allow the app would like to pass a custom view controller to Braze for in-app message display:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func inAppMessageViewControllerWithInAppMessage(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageViewController!
```

{% endtab %}
{% endtabs %}

All of our in-app message view controllers are open-sourced. You can use subclasses or categories to customize the display or behavior of in-app messages.

See the [in-app message view controllers][37] for more details.

## Custom In-App Message Triggering

By default, in-app messages are triggered by event types that are logged by the SDK. If you would like to trigger in-app messages by server-sent events you are also able to achieve this.

To enable this feature you would send a silent push to the device which allows the device to log an SDK based event. This SDK event would subsequently trigger the user-facing in-app message.

### Step 1: Handle Silent Push and Key-Value Pairs
Add the following code within the `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` method:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [[Appboy sharedInstance] logCustomEvent:@"IAM Trigger" withProperties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
 };
```

{% endtab %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  NSLog("A push was received");
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    Appboy.sharedInstance()?.logCustomEvent("IAM Trigger", withProperties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% endtabs %}

When the silent push is received an SDK recorded event "In-App Message Trigger" will be logged against the user profile. Note that these In-App Messages will only trigger if the silent push is received while the application is in the foreground.

### Step 2: Create a Push Campaign

Create a silent push campaign which is triggered via the server sent event. For details on how to create a silent push campaign please review this section of our [Docs][39].

![serverEventTrigger][40]

The push campaign must include key-value pair extras which indicate that this push campaign is sent with the intention to log an SDK custom event. This event will be used to trigger the in-app message:

![IAMSilentPush][41]

The code within the `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` method checks for key `IS_SERVER_EVENT` and will log an SDK custom event if this is present.

You can alter either the event name or event properties by sending the desired value within the key-value pair extras of the push payload. These extras can be used as the parameter of either the event name or as an event property when logging the custom event.

### Step 3: Create an In-App Message Campaign

Create your user visible in-app message campaign from within Braze’s dashboard. This campaign should have an Action Based delivery, and be triggered from the custom event logged from within the `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` method.

In the example below the specific in-app message to be trigger has been configured by sending the event property as part of the initial silent push.

![IAMPushTrigger][42]

>  Due to a push message being used to record an SDK logged custom event, Braze will need to store a push token for each user to enable this solution. For iOS users, Braze will only store a token from the point that a user has been served the OS's push prompt. Before this, the user will not be reachable using push and the above solution will not be possible.

## Method Declarations

For additional information see the following header files:

- [`ABKInAppMessage.h`][14]
- [`ABKInAppMessageController.h`][15]
- [`ABKInAppMessageControllerDelegate.h`][16]

## Implementation Samples

See [`AppDelegate.m`][36], [`ViewController.m`][35] and [`CustomInAppMessageViewController.m`][19] in the in-app message sample app.

[13]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#creating-an-in-app-message
[14]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h
[15]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageController.h
[16]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h
[19]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/CustomInAppMessageViewController.m
[23]: #setting-delegates
[26]: http://fortawesome.github.io/Font-Awesome/
[33]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/troubleshooting/#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens
[34]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h
[35]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m
[36]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m
[37]: https://github.com/Appboy/appboy-ios-sdk/tree/master/AppboyUI/ABKInAppMessage/ViewControllers
[39]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/
[40]: {% image_buster /assets/img_archive/iosServerSentPush.png %}
[41]: {% image_buster /assets/img_archive/iOSServerPush.png %}
[42]: {% image_buster /assets/img_archive/iosIAMeventTrigger.png %}

Web:


# Customization {#in-app-message-customization}

All of Braze’s in-app message types are highly customizable across messages, images, [Font Awesome][15]  icons, click actions, analytics, editable styling, custom display options, and custom delivery options. Multiple options can be configured on a per in-app message basis from [within the dashboard]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/). Braze additionally provides multiple levels of advanced customization to satisfy a variety of use cases and needs.

## Key Value Pair Extras

In-app message objects may carry key-value pairs as their `extras` property. These are specified on the dashboard under "Additional Message Settings" when creating an in-app message campaign. These can be used to send data down along with an in-app message for further handling by your site. For example:

```javascript
appboy.subscribeToInAppMessage(function(inAppMessage) {
  if (inAppMessage instanceof appboy.InAppMessage) {
    var extras = inAppMessage.extras;
    for (var key in extras) {
      if (data.hasOwnProperty(key)) {
         console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }

  appboy.display.showInAppMessage(inAppMessage);
});
```

### In-App Message Default z-index

By default, In-App Messages are displayed using `z-index: 1050`. This is configurable using the `inAppMessageZIndex ` [initialization option][41] in the scenario that your website styles elements with higher values than that.

**Note**: This option was introduced in Web SDK v3.3.0. Older SDKs must be upgraded in order to use this option.

```javascript
import braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 9001
});
```

### Custom Styling

Braze UI elements come with a default look and feel that create a neutral in-app message experience and aims for consistency with other Braze mobile platforms. Braze's default styles are defined in CSS within the Braze SDK. By overriding selected styles in your application, it is possible to customize our standard in-app message types with your own background images, font families, styles, sizes, animations, and more. For instance, the following is an example override that will cause an in-app message's headers to appear italicized:

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

See the [JSDocs][2] for more information.

## Open Message Link in New Tab

To set your in-app message links to open in a new tab, set the `openInAppMessagesInNewTab` option to `true` to force all links from in-app message clicks open in a new tab or window.

```javascript
appboy.initialize('api-key', { openInAppMessagesInNewTab: true} );
```

[2]: https://js.appboycdn.com/web-sdk/latest/doc/ab.InAppMessage.html
[15]: https://fontawesome.com/?from=io
[41]: https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#initializationoptions