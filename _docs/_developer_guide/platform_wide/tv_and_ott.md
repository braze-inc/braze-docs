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
            <td for="iam"><i class="fas fa-times text-warning"></i></td>
            <td for="content-cards"><i class="fas fa-times text-warning"></i></td>
            <td for="push"><i class="fas fa-times text-warning"></i></td>  
            <td for="canvas">N/A</td>
        </tr>
    </tbody>
</table>

- <i class="fas fa-check text-success"></i> = Supported
- <i class="fas fa-times text-warning"></i> = Not supported by Braze
- N/A = Not supported by platform

## Integration guides

### Amazon Fire TV

Use Braze's Fire OS SDK to integrate with Amazon Fire TV devices.

Features include:

- Data and Analytics collection for cross-channel engagement
- Push Notifications (known as ["Heads Up Notifications"][7])
  - The priority must be set to "HIGH" for these to appear. All notifications appear in the Fire TV settings menu.
- Content Cards
- In-app messages

For more information, visit the [Fire OS Integration Guide][2].

### Kindle Fire

Use Braze's Fire OS SDK to integrate with Amazon Kindle Fire devices.

Features include:

- Data and Analytics collection for cross-channel engagement
- Push Notifications
- Content Cards
- In-app messages

For more information, visit the [Fire OS Integration Guide][2].

### Android TV

Use Braze's Android SDK to integrate with Android TV devices.

Features include:

- Data and Analytics collection for cross-channel engagement
- Content Cards
- In-app messages 
- &#42; Push Notifications (Manual Integration Required)

For more information, visit the [Android SDK Integration Guide][2].

Push notifications are not supported natively on Android TV. For more information why, see Google's [Design Guidelines][5]. You may however, **do a manual integration of Push notification UI to achieve this**. See our [documentation][6] on how to set this up.

### LG webOS

Use Braze's Web SDK to integrate with [LG webOS TVs](http://webostv.developer.lge.com/discover/discover-webos-tv/).

Features include:

- Data and analytics collection for cross-channel engagement
- Content Cards (via Custom UI)
- In-app messages (via Custom UI)

For more information, visit the [Web Smart TV Integration Guide][8].

### Samsung Tizen

Use Braze's Web SDK to integrate with the [Samsung Tizen TVs](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html).

Features include:

- Data and analytics collection for cross-channel engagement
- Content Cards (via Custom UI)
- In-app messages (via Custom UI)

For more information, visit the [Web Smart TV Integration Guide][8].

### Roku

Use Braze's Roku SDK to integrate with [Roku TVs](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md)

Features include:

- Data and analytics collection for cross-channel engagement
- In-app messages (via Custom UI)

For more information, visit the [Roku Integration Guide][3].

### Apple TV OS

Use Braze's iOS SDK to collect data and analytics on your TV OS users. These custom events and attributes can be used across your other channels for personalization and promotional messaging.

For more information, visit the [iOS SDK Integration Guide][4].

## In-app message with custom UI

For platforms that support in-app messages via Custom UI, your app can be configured to read the data model received by the Braze SDK. This information will contain the fields configured in the dashboard (title, body, button text, colors, etc.) which your app can read and display accordingly. This data can also be used to customize Braze's native in-app message templates into your existing app designs.

[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/in-app_messaging/overview/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/tvos/initial_sdk_setup/
[5]: https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android_tv_push/
[7]: https://developer.amazon.com/docs/fire-tv/notifications.html#headsup
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/smart_tvs/
