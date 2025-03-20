## Using the Google Tag Manager {#initialization-tag}

### Step 1: Push setup (optional)

Optionally, if you want to be able to send push through the Google Tag Manager, first follow the [push integration]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) guidelines to:
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
