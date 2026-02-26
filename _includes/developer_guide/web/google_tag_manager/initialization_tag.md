### Prerequisites

Before you can use this integration method, you'll need to [create an account and container for Google Tag Manager](https://support.google.com/tagmanager/answer/14842164).

### Step 1: Open the tag template gallery

In [Google Tag Manager](https://tagmanager.google.com/), choose your workspace, then select **Templates**. In the **Tag Template** pane, select **Search Gallery**.

![The templates page for an example workspace in Google Tag Manager.]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### Step 2: Add the initialization tag template

In the template gallery, search for `braze-inc`, then select **Braze Initialization Tag**.

![The template gallery showing the various 'braze-inc' templates.]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

Select **Add to workspace** > **Add**.

![The 'Braze Initialization Tag' page in Google Tag Manager.]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### Step 3: Configure the tag

From the **Templates** section, select your newly added template.

![The "Templates" page in Google Tag Manager showing the Braze Initialization Tag template.]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

Select the pencil icon to open the **Tag Configuration** dropdown.

![The Tag Configuration tile with the 'pencil' icon shown.]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

Enter the minimum required information:

| Field         | Description |
| ------------- | ----------- |
| **API Key**   | Your [Braze API Key]({{site.baseurl}}/api/basics/#about-rest-api-keys), found in the Braze dashboard under **Settings** > **App Settings**. |
| **API Endpoint** | Your REST endpoint URL. Your endpoint will depend on the Braze URL for [your instance]({{site.baseurl}}/api/basics/#endpoints). |
| **SDK Version**  | The most recent `MAJOR.MINOR` version of the Web Braze SDK listed in the [changelog]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web). For example, if the latest version is `4.1.2`, enter `4.1`. For more information, see [About SDK version management]({{site.baseurl}}/developer_guide/sdk_integration/version_management/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

For additional initialization settings, select **Braze Initialization Options** and choose any options you need.

![The list of Braze Initialization Options in under 'Tag Configuration'.]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### Step 4: Choose initialization options

The Braze Initialization Tag exposes the following options. Most of these map directly to the [Web SDK `InitializationOptions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions), and some correspond to Web SDK methods that the tag will call during initialization. Select the options that match your integration needs:

| GTM option | Web SDK configuration or method | Description |
| --- | --- | --- |
| **Allow HTML In-App Messages** | `allowUserSuppliedJavascript` | Enables HTML in-app messages, Banners, and user-supplied JavaScript click actions. Required for [HTML in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/) and [Banners]({{site.baseurl}}/developer_guide/banners/placements/?sdktab=web) that use custom HTML. Only enable this when you trust the HTML and JavaScript content, as it allows user-supplied JavaScript execution. |
| **Automatically show new in app messages** | `braze.automaticallyShowInAppMessages()` | Automatically displays new in-app messages when they arrive from the server by calling this method after initialization. |
| **Automatically Open New Session** | `braze.openSession()` | Opens a new session after the SDK is initialized by calling this method for you. |
| **Open Cards in New Tab** | `openCardsInNewTab` | Opens Content Card links in a new tab when using the default Feed UI. |
| **Disable Automatic Push Token Maintenance** | `disablePushTokenMaintenance` | Stops the SDK from syncing push tokens with the Braze backend on new sessions. |
| **Disable Font Awesome** | `doNotLoadFontAwesome` | Prevents the SDK from loading Font Awesome from the CDN. Use if your site has its own Font Awesome. |
| **Enable Web SDK Logging** | `enableLogging` | Enables console logging for debugging. Remove before production. |
| **Disable Automatic Service Worker Registration** | `manageServiceWorkerExternally` | Use if you register and control the service worker yourself. |
| **Disable Cookies** | `noCookies` | Uses localStorage instead of cookies for user/session data. Prevents cross-subdomain recognition. |
| **Enable SDK Authentication** | `enableSdkAuthentication` | Enables [SDK Authentication]({{site.baseurl}}/developer_guide/sdk_integration/authentication/). |
| **Minimum Interval Between Triggered Messages** | `minimumIntervalBetweenTriggerActionsInSeconds` | Minimum seconds between trigger actions (default: 30). |
| **Service Worker Location** | `serviceWorkerLocation` | Custom path for the service worker file (default: `/service-worker.js`). |
| **Session Timeout (seconds)** | `sessionTimeoutInSeconds` | Session timeout in seconds (default: 1800). |
| **App Version Number** | `appVersion`, `appVersionNumber` | App version for segmentation (for example, `1.2.3.4`). |

For options not exposed in the GTM template (such as `contentSecurityNonce`, `localization`, or `devicePropertyAllowlist`), use [runtime initialization]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) instead.

### Step 5: Set to Trigger on *all pages*

The initialization tag should be run on all pages of your site. This allows you to use Braze SDK methods and record web push analytics.

### Step 6: Verify your integration

You can verify your integration using either of the following options:

- **Option 1:** Using Google Tag Manager's [debugging tool](https://support.google.com/tagmanager/answer/6107056?hl=en), you can check if the Braze Initialization Tag is triggering correctly on your configured pages or events.
- **Option 2:** Check for any network requests made to Braze from your web page. Additionally, the global `window.braze` library should now be defined.
