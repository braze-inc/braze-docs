---
nav_title: TV and OTT Integrations
page_order: 4
---

# TV and OTT Integrations

As technology evolves to new platforms and devices, so can your messaging with Braze!

Braze offers different engagement channels for a number of different TV Operating Systems and "OTT" Set Top Boxes.

## Platforms and Features

Below is a list of features and messaging channels supported today.

<style>
#tv-feature-table td {
    text-align: center !important;
    vertical-align: center;
}
</style>
<table id="tv-feature-table">
    <thead>
        <tr>
            <th>Device Type</th>
            <th>Data and Analytics</th>
            <th>Push Notifications</th>
            <th>In App Messages</th>
            <th>Content Cards</th>
            <th>Canvas</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Amazon Fire TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i><br>(via Data Model)</td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Kindle Fire</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Android TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i><br>(via Data Model)</td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Roku</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-times text-danger"></i></td>
            <td for="iam"><i class="fas fa-times text-danger"></i></td>
            <td for="content-cards"><i class="fas fa-times text-danger"></i></td>
            <td for="canvas">--</td>
        </tr>
        <tr>
            <td>Apple TV OS</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-times text-danger"></i></td>
            <td for="iam"><i class="fas fa-times text-danger"></i></td>
            <td for="content-cards"><i class="fas fa-times text-danger"></i></td>
            <td for="canvas">--</td>
        </tr>
    </tbody>
</table>

### Amazon Fire TV

Use Braze's Fire OS SDK to integrate with Amazon Fire TV devices.

Features include:

- Data and Analytics collection for cross-channel engagement
- Push Notifications (known as "Heads Up Notifications")
- Content Cards
- In App Messages are available using custom views with our Data Model

For more information, visit the [Fire OS Integration Guide]({{ site.baseurl }}/developer_guide/platform_integration_guides/fireos/initial_sdk_setup/).

### Kindle Fire

Use Braze's Fire OS SDK to integrate with Amazon Kindle Fire devices.

Features include:

- Data and Analytics collection for cross-channel engagement
- Push Notifications
- Content Cards
- In App Messages

For more information, visit the [Fire OS Integration Guide]({{ site.baseurl }}/developer_guide/platform_integration_guides/fireos/initial_sdk_setup/).

### Android TV

Use Braze's Android SDK to integrate with Android TV devices.

Features include:

- Data and Analytics collection for cross-channel engagement
- Push Notifications
- Content Cards
- In App Messages are available using custom views with our Data Model

### Roku

Use Braze's Roku SDK to collect data and analytics on your Roku users. These custom events and attributes can be used across your other channels for personalization and promotional messaging.

The ability to send In App Messages to your Roku users is coming soon - stay tuned!

For more information, visit the [Roku Integration Guide]({{ site.baseurl }}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/).

### Apple TV OS

Use Braze's iOS SDK to collect data and analytics on your TV OS users. These custom events and attributes can be used across your other channels for personalization and promotional messaging.

For more information, visit the [Roku Integration Guide]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/).
