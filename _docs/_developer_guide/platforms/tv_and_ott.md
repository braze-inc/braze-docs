---
nav_title: TV and OTT
article_title: TV and OTT Integrations for Braze
page_order: 15

description: "This article will give you details on Braze TV and OTT features, integrations, available platforms, and other capabilities."
platform:
  - tvOS
  - Roku
  - Web
  - Android
  - FireOS
---

# TV and OTT integrations

> As technology evolves to new platforms and devices, so can your messaging with Braze! Braze offers different engagement channels for a number of different TV Operating Systems and Over-the-Top (OTT) content delivery methods.

## Platforms and features

The following lists features and messaging channels supported today.

<style>
#tv-feature-table td,
#tv-feature-table th {
    text-align: center !important;
    vertical-align: center;
}

</style>
<table id="tv-feature-table">
    <thead>
        <tr>
            <th>Device type</th>
            <th>Data and analytics</th>
            <th>In-app messages</th>
            <th>Content Cards</th>
            <th>Push notifications</th>
            <th>Canvas</th>
            <th>Feature Flags</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Amazon Fire TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Kindle Fire</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Android TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>LG TV (webOS)</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">N/A</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Samsung Tizen TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">N/A</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Roku</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-times text-warning"></i></td>
            <td for="push">N/A</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Apple TV OS</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
             <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fa-solid fa-minus"></i></td>  
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
       <tr>
          <td>Apple Vision Pro</td>
          <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
           <td for="iam"><i class="fas fa-check text-success"></i></td>
          <td for="content-cards"><i class="fas fa-check text-success"></i></td>
          <td for="push"><i class="fa-solid fa-minus"></i></td>  
          <td for="canvas"><i class="fas fa-check text-success"></i></td>
          <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
      </tr>
    </tbody>
</table>

- <i class="fas fa-check text-success"></i> = Supported
- <i class="fa-solid fa-minus"></i> = Partial support
- <i class="fas fa-times text-warning"></i> = Not supported by Braze
- N/A = Not supported by OTT platform

## Integration guides

### Amazon Fire TV {#fire-tv}

Use the Braze Fire OS SDK to integrate with Amazon Fire TV devices.

Features include:

- Data and Analytics collection for cross-channel engagement
- Push Notifications (known as ["Heads Up Notifications"](https://developer.amazon.com/docs/fire-tv/notifications.html#headsup))
  - The priority must be set to "HIGH" for these to appear. All notifications appear in the Fire TV settings menu.
- Content Cards
- Feature Flags
- In-app messages
  - To show HTML messages on non-touch environments like TVs, set `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` to `false` (available from [Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310))

For more information, visit the [Fire OS integration guide]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).

### Kindle Fire {#kindle-fire}

Use the Braze Fire OS SDK to integrate with Amazon Kindle Fire devices.

Features include:

- Data and Analytics collection for cross-channel engagement
- Push Notifications
- Content Cards
- Feature Flags
- In-app messages

For more information, visit the [Fire OS integration guide]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).

### Android TV {#android-tv}

Use the Braze Android SDK to integrate with Android TV devices.

Features include:

- Data and Analytics collection for cross-channel engagement
- Content Cards
- Feature Flags
- In-app messages 
  - To show HTML messages on non-touch environments like TVs, set `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` to `false` (available from [Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310))
- &#42; Push Notifications (Manual Integration Required)
  - Push notifications are not supported natively on Android TV. To learn why, see Google's [Design Guidelines](https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html). You may however, **do a manual integration of Push notification UI to achieve this**. See our [documentation]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android%20tv) on how to set this up.

For more information, visit the [Android SDK integration guide]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).

{% alert note %}
Make sure to create a new Android app in the dashboard for your Android OTT integration.
{% endalert %}

### LG webOS {#lg-webos}

Use the Braze Web SDK to integrate with [LG webOS TVs](https://webostv.developer.lge.com/discover).

Features include:

- Data and analytics collection for cross-channel engagement
- Content Cards (via [Headless UI](#custom-ui))
- Feature Flags
- In-app messages (via [Headless UI](#custom-ui))

For more information, visit the [Web Smart TV integration guide]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs/).

### Samsung Tizen {#tizen}

Use the Braze Web SDK to integrate with the [Samsung Tizen TVs](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html).

Features include:

- Data and analytics collection for cross-channel engagement
- Content Cards (via [Headless UI](#custom-ui))
- Feature Flags
- In-app messages (via [Headless UI](#custom-ui))

For more information, visit the [Web Smart TV integration guide]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs/).

### Roku {#roku}

Use the Braze Roku SDK to integrate with [Roku TVs](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md).

Features include:

- Data and analytics collection for cross-channel engagement
- In-app messages (via [Headless UI](#custom-ui))
  - Webviews are not supported by the Roku platform, so HTML in-app messages are therefore not supported.
- Feature Flags

For more information, visit the [Roku integration guide]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=roku).

### Apple TV OS {#tvos}

Use the Braze Swift SDK to integrate with tvOS. Keep in mind, the Swift SDK doesn't include any default UI or views for tvOS, so you will need to implement your own.

Features include:

- Data and analytics collection for cross-channel engagement
- Content Cards (via [Headless UI](#custom-ui))
- Feature Flags
- In-app messages (via [Headless UI](#custom-ui))
  - Webviews are not supported by the tvOS platform, so HTML in-app messages are therefore not supported.
  - See our [sample app](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui) to learn more about how to use a Headless UI for customized messaging on tvOS.
- Silent push notifications and update badging

For more information, visit the [iOS Swift SDK integration guide](https://github.com/braze-inc/braze-swift-sdk).

{% alert note %}
To avoid showing mobile in-app messages to your TV users, be sure to set up either [App Targeting](#app-targeting) or use key-value pairs to filter out messages. For example, only displaying tvOS messages if they contain a special `tv = true` key-value pair.
{% endalert %}

### Apple Vision Pro {#vision-pro}

Use the Braze Swift SDK to integrate with visionOS. Most features available on iOS are also available on visionOS, including:

- Analytics (sessions, custom events, purchases, etc.)
- In-App Messaging (data models and UI)
- Content Cards (data models and UI)
- Push Notifications (user-visible with action buttons and silent notifications)
- Feature Flags
- Location Analytics

For more information, visit the [iOS Swift SDK integration guide](https://github.com/braze-inc/braze-swift-sdk).

{% alert important %}
Some iOS features are partially-supported or unsupported. For the full list, see [visionOS support](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/visionos).
{% endalert %}

## App targeting {#app-targeting}

To target OTT apps for messaging, we recommend creating a segment specific to your OTT app.

![A segment created using the Android OTT app.]({% image_buster /assets/img/android_ott.png %})

## Headless UI {#custom-ui}

{% alert important %}
Platforms that support in-app messages or Content Cards via headless UI **do not** include any default UI or views, so be sure to implement your own custom UI.
{% endalert %}

With headless UI, Braze will deliver a data model, such as JSON, that your app can read and use within a UI your app controls. This data will contain the fields configured in the dashboard (title, body, button text, colors, etc.) which your app can read and display accordingly. For more information about custom handling messaging, see the following:

**Android SDK**
- [In-App Message Customization]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners)
- [Content Cards Customization]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/)

**Swift SDK**
- [In-App Message Customization](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/)
- [Headless UI Sample App](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui)
- [Content Cards Customization](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/)

**Web SDK**
- [In-App Message Customization]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web)
- [Content Cards Customization]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/)

