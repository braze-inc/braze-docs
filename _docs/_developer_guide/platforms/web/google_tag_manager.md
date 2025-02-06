---
nav_title: Google Tag Manager
article_title: Google Tag Manager for Web
platform: Web
page_order: 20
description: "This article covers how to use Google Tag Manager to deploy Braze to your website."

---

# Google Tag Manager

> This article provides a step-by-step guide on how to add the Braze Web SDK to your website using the Google Tag Manager (GTM). [Google Tag Manager](https://support.google.com/tagmanager/answer/6103696) lets you remotely add, remove, and edit tags on your website without requiring a production code release or engineering resources.

There are two Google Tag Manager templates built by Braze, the [Initialization Tag](#initialization-tag) and the [Actions Tag](#actions-tag).

Both tags can be added to your workspace from [Google's community gallery](https://tagmanager.google.com/gallery/#/?filter=braze) or by searching for Braze when adding a new tag from the Community Templates.

![image of gallery search]({% image_buster /assets/img/web-gtm/gtm-community-gallery-search.png %})

## Updated Google EU User Consent Policy

{% alert important %}
Google is updating their [EU User Consent Policy](https://www.google.com/about/company/user-consent-policy/) in response to changes to the [Digital Markets Act (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), which is in effect as of March 6, 2024. This new change requires advertisers to disclose certain information to their EEA and UK end users, as well as obtain necessary consents from them. Review the following documentation to learn more.
{% endalert %}

As part of Google's EU User Consent Policy, the following boolean custom attributes need to be logged to user profiles:

- `$google_ad_user_data`
- `$google_ad_personalization`

If setting these via the GTM integration, custom attributes require creating a custom HTML tag. The following is an example of how to log these values as boolean data types (not as strings):

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

For more information, refer to [Audience Sync to Google]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/).

## Initialization Tag template {#initialization-tag}

Use the Initialization Tag to add the Braze Web SDK to your website.

### Step 1: Push setup (optional)

Optionally, if you want to be able to send push through the Google Tag Manager, first follow the [push integration]({{site.baseurl}}/developer_guide/platforms/web/push_notifications/) guidelines to:
1. Configure your site's service worker, placing it in the root directory of your site
2. Set up browser registration - After the service worker is configured, you must set the `braze.requestPushPermission()` method either natively in their app or through a custom HTML tag (via the GTM dashboard). You will also need to make sure that the tag is fired after the SDK has been initialized.

### Step 2: Select the Initialization Tag

Search for Braze in the community template gallery, and select the **Braze Initialization Tag**.

![A dialog box showing the Braze Initialization Tag configuration settings. Settings included are "tag type", "API key", "API endpoint", "SDK version", "external user ID", and "Safari web push ID".]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

### Step 3: Configure settings

Enter your Braze API app identifier key and SDK endpoint, which can be found in your dashboard's **Manage Settings** page. Enter the Web SDK's most recent `major.minor` version. For example, if the latest version is `4.1.2`, enter `4.1`. You can view a list of SDK versions in our [changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).

### Step 4: Choose initialization options

Choose from the optional set of additional initialization options described in the [Initial setup]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-2-initialize-braze) guide.

### Step 5: Verify and QA

Once you've deployed this tag, there are two ways you can verify a proper integration:

1. Using Google Tag Manager's [debugging tool](https://support.google.com/tagmanager/answer/6107056?hl=en), you should see the Braze Initialization Tag has been triggered on your configured pages or events.
2. You should see network requests made to Braze, and the global `window.braze` library should now be defined on your web page.

## Actions Tag template {#actions-tag}

The Braze Actions Tag template lets you trigger custom events, track purchases, change user IDs, and stop or resume tracking for privacy requirements.

![]({% image_buster /assets/img/web-gtm/gtm-actions-tag.png %})

### Changing user external ID {#external-id}

The **Change User** tag type calls the [`changeUser` method](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser). 

Use this tag whenever a user logs in or is otherwise identified with their unique `external_id` identifier.

Be sure to enter the current user's unique ID in the **External User ID** field, typically populated using a data layer variable sent by your website.

![A dialog box showing the Braze Action Tag configuration settings. Settings included are "tag type" and "external user ID".]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})

### Log custom events {#custom-events}

The **Custom Event** tag type calls the [`logCustomEvent` method](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

Use this tag to send custom events to Braze, optionally including custom event properties.

Enter the **Event Name** by either using a variable or typing an event name.

Use the **Add Row** button to add event properties.

![A dialog box showing the Braze Action Tag configuration settings. Settings included are "tag type"(custom event), "event name" (button click), and "event properties".]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})

### eCommerce events {#ecommerce}

If your site logs purchases using the standard [ecommerce event](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) data layer item to Google Tag Manager, then you can use the **E-commerce Purchase** tag type. This action type will log a separate "purchase" in Braze for each item sent in the list of `items`.

You can also specify additional property names you want to include as purchase properties by specifying their keys in the Purchase properties list. Note that Braze will look within the individual `item` that is being logged for any purchase properties you add to the list.

For example, let's say your ecommerce payload contains the following `items`:

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

If you only want `item_brand` and `item_name` to be passed as purchase properties, then just add those two fields to the purchase properties table. If you don't supply any properties, then no purchase properties will be sent in the [`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) call to Braze.

### Track purchase {#purchases}

The **Purchase** tag type calls the [`logPurchase` method](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase).

Use this tag to track purchases to Braze, optionally including purchase properties.

The **Product ID** and **Price** fields are required.

Use the **Add Row** button to add purchase properties.

![A dialog box showing the Braze Action Tag configuration settings. Settings included are "tag type", "external ID", "price", "currency code", "quantity", and "purchase properties".]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})

### Stop and resume tracking {#stop-tracking}

Sometimes, you might be required to disable or re-enable Braze tracking on your website, for example, after a user indicates they've opted out of web tracking for privacy reasons.

Use the **Disable Tracking** or **Resume Tracking** tag type to disable or re-enable web tracking, respectively. These two options call [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) and [`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk).

### Custom user attributes {#custom-attributes}

Custom user attributes are not available due to a limitation in Google Tag Manager's scripting language. To log custom attributes, create a Custom HTML tag with the following content:

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
The GTM template does not support nested properties on events or purchases. You can use the preceding HTML to log any events or purchases that require nested properties.
{% endalert %}

### Standard user attributes {#standard-attributes}

Standard user attributes, such as a user's first name, should be logged in the same manner as custom user attributes. Ensure the values you're passing in for standard attributes match the expected format specified in the [User class](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) documentation.

For example, the gender attribute can accept any of the following as values: `"m" | "f" | "o" | "u" | "n" | "p"`. Therefore to set a user's gender as female, create a Custom HTML tag with the following content:

```html
<script>
window.braze.getUser().setGender("f")
</script>
```

## Integrating Content Cards

There are a few additional steps to integrate the [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) messaging channel using Google Tag Manager. Google Tag Manager works by injecting the [Braze CDN]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (a version of our Web SDK) directly into your website code, which means that all SDK methods are available just as if you had integrated the SDK without Google Tag Manager, except when implementing Content Cards.

### Option 1: Integrating using GTM

For a standard integration of the Content Card feed, you can use a **Custom HTML** tag in Google Tag Manager. Add the following to your Custom HTML tag, which will activate the standard Content Card feed:

```html
<script>
   window.braze.showContentCards();
</script>
```

![Tag Configuration in Google Tag Manager of a Custom HTML tag that shows the Content Card feed.]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})

### Option 2: Integrating directly in your website

For more freedom over customizing the appearance of Content Cards and their feed, you can directly integrate Content Cards into your native website. There are two approaches you can take with this: using the standard feed UI or creating a custom feed UI.

#### Standard feed

When implementing the [standard feed UI]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui), Braze methods must have `window.` added to the start of the method. For example, `braze.showContentCards` should instead be `window.braze.showContentCards`.

#### Custom feed UI

For [custom feed]({{site.baseurl}}/developer_guide/content_cards/creating_custom_content_cards/) styling, the steps are the same as if you had integrated the SDK without GTM. For example, if you want to customize the width of the Content Card feed, you can paste the following into your CSS file:

{% raw %}
```css
body .ab-feed { 
    width: 800px;
}
```
{% endraw %}

## Upgrading and updating templates {#upgrading}

To upgrade to the latest version of the Braze Web SDK, take the following three steps in your Google Tag Manager dashboard:

1. **Update tag template**<br>Go to the **Templates** page within your workspace. Here you should see an icon indicating an update is available.<br><br>![Templates page showing an update is available]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>Click that icon and after reviewing the change, click to **Accept Update**.<br><br>![A screen comparing the old and new tag templates with a button to "Accept Update"]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **Update version number**<br>Once your tag template has been updated, edit the Braze Initialization Tag, and update the SDK version to the most recent `major.minor` version. For example, if the latest version is `4.1.2`, enter `4.1`. You can view a list of SDK versions in our [changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).<br><br>![Braze Initialization Template with an input field to change the SDK Version]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **QA and publish**<br>Verify the new SDK version is working using Google Tag Manager's [debugging tool](https://support.google.com/tagmanager/answer/6107056?hl=en) prior to publishing an update to your tag container.

## Troubleshooting steps {#troubleshooting}

### Enable tag debugging {#debugging}

Each Braze tag template has an optional **GTM Tag Debugging** checkbox which can be used to log debug messages to your web page's JavaScript console.

![Google Tag Manager's Debug tool]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

### Enter debug mode

Another way to help debug your Google Tag Manager integration is using Google's [Preview mode](https://support.google.com/tagmanager/answer/6107056) feature.

This will help identify what values are being sent from your web page's data layer to each triggered Braze tag and will also explain which tags were or were not triggered.

![The Braze Initialization Tag summary page provides an overview of the tag, including information on which tags were triggered.]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

### Enable verbose logging

To allow Braze technical support to access logs while testing, you can enable verbose logging on your Google Tag Manager integration. These logs will appear in the **Console** tab of your browser's [developer tools](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools).

In your Google Tag Manager integration, navigate to your Braze Initialization Tag and select **Enable Web SDK Logging**.

![The Braze Initialization Tag summary page with the option to Enable Web SDK Logging turned on.]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md
