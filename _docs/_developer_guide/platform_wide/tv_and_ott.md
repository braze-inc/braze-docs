---
nav_title: TV and OTT Integrations
page_order: 4

description: "This article will give you details on Braze's TV and OTT features, integrations, available platforms, and other capabilities."
platform:
  - roku
  - fireos
  - ios
  - android
channel:
  - tv
  - ott
---

# TV and OTT Integrations

As technology evolves to new platforms and devices, so can your messaging with Braze!

Braze offers different engagement channels for a number of different TV Operating Systems and "OTT" Set Top Boxes.

## Platforms and Features

Below is a list of features and messaging channels supported today.

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
            <th>Device Type</th>
            <th>Data and Analytics</th>
            <th>In App Messages</th>
            <th>Push Notifications</th>
            <th>Content Cards</th>
            <th>Canvas</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Amazon Fire TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Kindle Fire</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Android TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-times text-danger"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Roku</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-times text-danger"></i></td>
            <td for="push"><i class="fas fa-times text-danger"></i></td>
            <td for="content-cards"><i class="fas fa-times text-danger"></i></td>
            <td for="canvas">--</td>
        </tr>
        <tr>
            <td>Apple TV OS</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-times text-danger"></i></td>
            <td for="push"><i class="fas fa-times text-danger"></i></td>
            <td for="content-cards"><i class="fas fa-times text-danger"></i></td>
            <td for="canvas">--</td>
        </tr>
    </tbody>
</table>

## Integration Guides

### Amazon Fire TV

Use Braze's Fire OS SDK to integrate with Amazon Fire TV devices.

Features include:

- Data and Analytics collection for cross-channel engagement
- Push Notifications (known as "Heads Up Notifications")
- Content Cards
- In App Messages are available using custom views with our Data Model

For more information, visit the [Fire OS Integration Guide][1].

### Kindle Fire

Use Braze's Fire OS SDK to integrate with Amazon Kindle Fire devices.

Features include:

- Data and Analytics collection for cross-channel engagement
- Push Notifications
- Content Cards
- In App Messages

For more information, visit the [Fire OS Integration Guide][1].

### Android TV

Use Braze's Android SDK to integrate with Android TV devices.

Features include:

- Data and Analytics collection for cross-channel engagement
- Content Cards
- In App Messages are available using custom views with our Data Model

For more information, visit the [Android SDK Integration Guide][2].

For more information on why Push Notifications are not supported on Android TV, see Google's [Design Guidelines][5].

### Roku

Use Braze's Roku SDK to collect data and analytics on your Roku users. These custom events and attributes can be used across your other channels for personalization and promotional messaging.

The ability to send In App Messages to your Roku users is coming soon - stay tuned!

For more information, visit the [Roku Integration Guide][3].

### Apple TV OS

Use Braze's iOS SDK to collect data and analytics on your TV OS users. These custom events and attributes can be used across your other channels for personalization and promotional messaging.

For more information, visit the [iOS SDK Integration Guide][4].

## In-App Message with Custom UI

For platforms which support In-App Messages via Custom UI, your app can be configured to read the data model received by the Braze SDK. This information will contain the fields configured in the dashboard (title, body, button text, colors, etc.) which your app can read and display accordingly. This data can also be used to customize Braze's native In App Message templates into your existing app designs.

[1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/fireos/initial_sdk_setup/
[2]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[3]: {{ site.baseurl }}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/
[4]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/
[5]: https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html
