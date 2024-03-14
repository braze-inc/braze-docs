---
nav_title: Integration
article_title: Integrating the Cordova Braze SDK
page_order: 0
---

# Integrating the Cordova Braze SDK

> Learn how to integrate the Cordova Braze SDK into your iOS or Android app. After you're finished, you can [further customize the SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_setup/customizations/).

## Integrating the SDK

### Step 1: Add the SDK to your project

If you're on Cordova 6 or later, you can add the SDK directly from GitHub. Alternatively, you can download a ZIP of the [GitHub repository](https://github.com/braze-inc/braze-cordova-sdk) and add the SDK manually.

{% tabs local %}
{% tab geofence disabled %}
If you don't plan on using location collection and geofences, use the `master` branch from GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master
```
{% endtab %}

{% tab geofence enabled %}
If you plan on using location collection and geofences, use the `geofence-branch` from GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```
{% endtab %}
{% endtabs %}

{% alert tip %}
You can switch between `master` and `geofence-branch` at anytime by repeating Step 1.
{% endalert %}

### Step 2: Configure your project

Next, adding the following preferences to the `platform` element in your project's `config.xml` file.

{% tabs %}
{% tab ios %}
```xml
<preference name="com.braze.api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.ios_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}

{% tab android %}
```xml
<preference name="com.braze.api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.android_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}
{% endtabs %}

Replace the following:

| Value                 | Description                                                                                                                      |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_KEY`       | Your [Braze REST API key]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys).              |
| `CUSTOM_API_ENDPOINT` | A custom API endpoint. This endpoint is used to route your Braze instance data to the correct App Group in your Braze dashboard. |

The `platform` element in your `config.xml` file should be similar to the following:

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.ios_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.android_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}
{% endtabs %}

## Disabling automatic session tracking (Android only)

By default, the Android Cordova plugin automatically tracks sessions. To disable automatic session tracking, add the following preference to the `platform` element in your project's `config.xml` file:

```xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

To start tracking sessions again, call `BrazePlugin.startSessionTracking()`. Keep in mind, only sessions started after the next `Activity.onStart()` will be tracked.
