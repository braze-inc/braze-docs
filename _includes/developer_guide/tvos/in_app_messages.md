{% alert important %}
Keep in mind, you'll need to implement your own custom UI since in-app messaging is supported via headless UI using the Swift SDK&#8212;which does not include any default UI or views for tvOS.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Enabling in-app messages

### Step 1: Create a new iOS app

In Braze, select **Settings** > **App Settings**, then select **Add App**. Enter a name for your tvOS app, select **iOS**&#8212;_not tvOS_&#8212;then select **Add App**.

![ALT_TEXT.]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
If you select the **tvOS** checkbox, you will not be able to customize in-app messages for tvOS.
{% endalert %}

### Step 2: Get your app's API key

In your app settings, select your new tvOS app then take note of your app's API key. You'll use this key to configure your app in Xcode.

![ALT_TEXT]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### Step 3: Integrate BrazeKit

Use your app's API key to integrate the [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) into your tvOS project in Xcode. You only need to integrate BrazeKit from the Braze Swift SDK.

### Step 4: Create your custom UI

Because Braze doesn't provide a default UI for in-app messages on tvOS, you'll need to customize it yourself. For a full walkthrough, see our step-by-step tutorial: [Customizing in-app messages for tvOS](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization). For a sample project, see [Braze Swift SDK samples](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui).
