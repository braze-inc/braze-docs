---
nav_title: Google Tag Manager
article_title: Google Tag Manager for Web
platform: Web
page_order: 20
description: "This article covers how to use Google Tag Manager to deploy Braze to your website."

---

# Google Tag Manager

> Description.

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

For [custom feed]({{site.baseurl}}/developer_guide/content_cards/creating_cards/) styling, the steps are the same as if you had integrated the SDK without GTM. For example, if you want to customize the width of the Content Card feed, you can paste the following into your CSS file:

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
