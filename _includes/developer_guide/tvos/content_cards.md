## Prerequisites

Before you can use Content Cards, you'll need to integrate the [Braze Swift SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) into your app. Then you'll need to complete the steps for setting up your tvOS app.

{% alert important %}
Keep in mind, you'll need to implement your own custom UI since Content Cards are supported via headless UI using the Swift SDK&#8212;which does not include any default UI or views for tvOS.
{% endalert %}

## Setting up your tvOS app

### Step 1: Create a new iOS app

In Braze, select **Settings** > **App Settings**, then select **Add App**. Enter a name for your tvOS app, select **iOS**&#8212;_not tvOS_&#8212;then select **Add App**.

![ALT_TEXT.]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
If you select the **tvOS** checkbox, you will not be able to customize Content Cards for tvOS.
{% endalert %}

### Step 2: Get your app's API key

In your app settings, select your new tvOS app then take note of your app's API key. You'll use this key to configure your app in Xcode.

![ALT_TEXT]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### Step 3: Integrate BrazeKit

Use your app's API key to integrate the [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) into your tvOS project in Xcode. You only need to integrate BrazeKit from the Braze Swift SDK.

### Step 4: Create your custom UI

Because Braze doesn't provide a default UI for content cards on tvOS, you'll need to customize it yourself. For a full walkthrough, see our step-by-step tutorial: [Customizing content cards for tvOS](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization/). For a sample project, see [Braze Swift SDK samples](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#contentcards-custom-ui).
