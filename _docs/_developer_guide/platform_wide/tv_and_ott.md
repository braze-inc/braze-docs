---
nav_title: TV and OTT Integrations
article_title: TV and OTT Integrations
page_order: 4

description: "This article will give you details on Braze's TV and OTT features, integrations, available platforms, and other capabilities."
platform:
  - tvOS
  - Roku
  - Web
  - Android
  - FireOS
  
---

# TV and OTT integrations

As technology evolves to new platforms and devices, so can your messaging with Braze!

Braze offers different engagement channels for a number of different TV Operating Systems and "OTT" Set Top Boxes.

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
        </tr>
        <tr>
            <td>Kindle Fire</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Android TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>LG TV (webOS)</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">N/A</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Samsung Tizen TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">N/A</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Roku</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-times text-warning"></i></td>
            <td for="push">N/A</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Apple TV OS</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fa-solid fa-minus"></i></td>  
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
    </tbody>
</table>

- <i class="fas fa-check text-success"></i> = Supported
- <i class="fa-solid fa-minus"></i> = Partial support
- <i class="fas fa-times text-warning"></i> = Not supported by Braze
- N/A = Not supported by OTT platform

{% alert note %}
The following are not currently supported on OTT:
- Out-of-the-box slide-up in-app messages 
- Custom HTML
{% endalert %}

## Integration guides

### Amazon Fire TV {#fire-tv}

Use Braze's Fire OS SDK to integrate with Amazon Fire TV devices.

Features include:

- Data and Analytics collection for cross-channel engagement
- Push Notifications (known as ["Heads Up Notifications"][7])
  - The priority must be set to "HIGH" for these to appear. All notifications appear in the Fire TV settings menu.
- Content Cards
- In-app messages
  - To show HTML messages on non-touch environments like TVs, set `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` to `false` (available from [Android SDK v23.1.0][android-tv-html])

For more information, visit the [Fire OS integration guide][2].

### Kindle Fire {#kindle-fire}

Use Braze's Fire OS SDK to integrate with Amazon Kindle Fire devices.

Features include:

- Data and Analytics collection for cross-channel engagement
- Push Notifications
- Content Cards
- In-app messages

For more information, visit the [Fire OS integration guide][2].

### Android TV {#android-tv}

Use Braze's Android SDK to integrate with Android TV devices.

Features include:

- Data and Analytics collection for cross-channel engagement
- Content Cards
- In-app messages 
  - To show HTML messages on non-touch environments like TVs, set `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` to `false` (available from [Android SDK v23.1.0][android-tv-html])
- &#42; Push Notifications (Manual Integration Required)

For more information, visit the [Android SDK integration guide][2].

Push notifications are not supported natively on Android TV. For more information why, see Google's [Design Guidelines][5]. You may however, **do a manual integration of Push notification UI to achieve this**. See our [documentation][6] on how to set this up.

{% alert note %}
Make sure to create a new Android app in the dashboard for your Android OTT integration.
{% endalert %}

### LG webOS {#lg-webos}

Use Braze's Web SDK to integrate with [LG webOS TVs](https://webostv.developer.lge.com/discover).

Features include:

- Data and analytics collection for cross-channel engagement
- Content Cards (via [Headless UI](#custom-ui))
- In-app messages (via [Headless UI](#custom-ui))

For more information, visit the [Web Smart TV integration guide][8].

### Samsung Tizen {#tizen}

Use Braze's Web SDK to integrate with the [Samsung Tizen TVs](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html).

Features include:

- Data and analytics collection for cross-channel engagement
- Content Cards (via [Headless UI](#custom-ui))
- In-app messages (via [Headless UI](#custom-ui))

For more information, visit the [Web Smart TV integration guide][8].

### Roku {#roku}

Use Braze's Roku SDK to integrate with [Roku TVs](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md)

Features include:

- Data and analytics collection for cross-channel engagement
- In-app messages (via [Headless UI](#custom-ui))
  - Webviews are not supported by the Roku platform, so HTML in-app messages are therefore not supported.

For more information, visit the [Roku integration guide][3].

### Apple TV OS {#tvos}

Use Braze's Swift SDK to integrate on tvOS

For more information, visit the [iOS Swift SDK integration guide][4].

Features include:

- Data and analytics collection for cross-channel engagement
- Content Cards (via [Headless UI](#custom-ui))
- In-app messages (via [Headless UI](#custom-ui))
  - Webviews are not supported by the tvOS platform, so HTML in-app messages are therefore not supported.
  - See our [sample app][9] to learn more about how to use a Headless UI for customized messaging on tvOS.
- Silent push notifications and update badging

**Note**: To avoid showing mobile in-app messages to your TV users, be sure to set up either [App Targeting](#app-targeting) or use key-value pairs to filter out messages. For example, only displaying tvOS messages if they contain a special `tv = true` key-value pair.

## App targeting {#app-targeting}

To target OTT apps for messaging, we recommend creating a segment specific to your OTT app.

![A segment created using the Android OTT app.][1]

## Headless UI {#custom-ui}

For platforms that support in-app messages or Content Cards via headless UI, Braze will deliver a data model (i.e., JSON) that your app can read and use within a UI your app controls. These platforms don't include any default UI or views.

This data will contain the fields configured in the dashboard (title, body, button text, colors, etc.) which your app can read and display accordingly.

Read more about custom handling messaging:

**Android SDK**
- [In-App Message Customization](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/)
- [Content Cards Customization](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/content_cards/implementation_guide/)

**Swift SDK**
- [In-App Message Customization](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/)
- [Headless UI Sample App][9]
- [Content Cards Customization](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/)

**Web SDK**
- [In-App Message Customization](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/in-app_messaging/customization/key_value_pairs)
- [Content Cards Customization](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/content_cards/customization/custom_ui/)
 

[1]: {% image_buster /assets/img/android_ott.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/in-app_messaging/overview/
[4]: https://github.com/braze-inc/braze-swift-sdk
[5]: https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android_tv_push/
[7]: https://developer.amazon.com/docs/fire-tv/notifications.html#headsup
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/smart_tvs/
[android-tv-html]: https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#2310
[9]: https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui
