---
nav_title: Initial SDK Setup
platform: Web
page_order: 0

---
# Initial SDK Setup

Integrating the Braze SDK will provide you with basic analytics functionality as well as in-app messages with which you can engage your users. Note that the web SDK file size is 32.3 KB.

## Integrate the Braze Library

To integrate the Braze Web SDK, follow the instructions in the "Getting Started" section of the [Braze Web SDK Github Repository][2].

Substitute the API key found within the "App Settings" page (labeled "API Key" in the "Settings for ..." block) of your Braze account for `YOUR-API-KEY-HERE`. For more detailed technical documentation, refer to [the complete JSDocs][9].

![API Key Location][14]

Your Braze representative should have already advised you of the [correct endpoint]({{ site.baseurl }}/user_guide/administrative/access_braze/sdk_endpoints). Reference the endpoint within your initialization snippet, for example:

*For US-03* : `appboy.initialize(‘YOUR-API-KEY-HERE’,{baseUrl:’https://sdk.iad-03.braze.com/api/v3’})`

*For EU-01* : `appboy.initialize(‘YOUR-API-KEY-HERE’,{baseUrl:’https://sdk-01.iad-01.braze.eu/api/v3’})`

## Enable Error Logging {#error-logging}

To enable logging, you can pass the option `enableLogging: true` to your initialize function (or call `appboy.toggleAppboyLogging()` after initialization), which will cause Braze to log to the javascript console. This is useful for development but is visible to all users, so you should remove this option or provide an alternate logger with `appboy.setLogger()` before you release your page to production.

## Initialize Tag Managers

### Google Tag Manager

#### Initializing the SDK

Braze's SDK can be initialized and controlled within tags configured from Google Tag Manager.

To initialize Braze’s SDK create a ‘Custom HTML’ tag within your Google Tag Manager workspace.  Place Braze’s [Web SDK/javascript code from the Google Tag Manager integration instructions][13] within the tag.

> This is instead of directly placing the snippet directly within the <head> section of your website.

Subsequent tags which fire after page load can then reference this. For example `<script type="text/javascript">window.appboy.logCustomEvent("test event")</script>`.

Please also ensure to replace the API key and custom SDK endpoint (if assigned one) in the code with your API key.

Braze suggests the tag has the trigger configuration of **Page View > DOM Ready**. Other Page View triggers can fire the tag, provided that no other Braze related tags are fired to prior to this.

![GTM_trigger_example][11]

#### Logging Events and using Braze's Messaging Channels

For Push, In-App Message, News Feed integration instructions please follow the standard integration instructions.

For Analytics integration, reference `<script type="text/javascript">window.appboy.logCustomEvent("test event")</script>` instead of re-using Braze's [Web SDK/javascript code][6].

![GTM_tag_configuration][12]

#### AMD Module Loader
If you are using Google Tag Manager alongside an AMD module loader such as RequireJS to load Braze's SDK you will need to use the RequireJS-compatible integration snippet in your <head> tag.

For further instruction on this please see the appropriate section of our [Braze Web SDK Github Repository][2].

### Tealium iQ

Tealium iQ offers a basic turnkey Braze integration. To configure the integration, just search for Braze in the Tealium Tag Management interface, and provide the Web SDK API key from your dashboard.

For more details, or in-depth Tealium configuration support, check out our [integration documentation]({{ site.baseurl }}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) or reach out to your Tealium Account Manager.

### Other Tag Managers

Braze may also be compatible with other tag management solutions. Please reach out to a Braze representative if you need help evaluating these solutions.

## Increasing the Security of the Braze SDK

As an additional layer of Web SDK security on the developer side, Braze suggests the simple set up of a bundler tool for Javascript. This can help prevent the SDK from being exposed to others, overall making it harder for malicious users to leverage Braze's SDK API in customer web apps.

The steps to do this can be found in the Braze Web SDK Github Repository under [Alternative NPM installation][15].

## Upgrading the SDK

When you reference the Braze Web SDK from our content delivery network, for example, https://js.appboycdn.com/web-sdk/a.a/appboy.min.js (as recommended by our default integration instructions), your users will receive minor updates (bug fixes and backward compatible features, versions a.a.a through a.a.z in the above examples) automatically when they refresh your site. When we release major changes however, we require you to upgrade the Braze Web SDK manually to ensure that nothing in your integration will be impacted by any breaking changes. Additionally, if you download our SDK and rehost it yourself (which is also a valid integration path), you won't receive any version updates automatically and should upgrade manually from time-to-time to receive the latest features and bug fixes.

You can keep up-to-date with our latest release [following our release feed](https://github.com/Appboy/appboy-web-sdk/tags.atom) with the RSS Reader or service of your choice, and see [our changelog](https://github.com/Appboy/appboy-web-sdk/blob/master/CHANGELOG.md) for a full accounting of our Web SDK release history. To upgrade the Braze Web SDK:

* Update the Braze JavaScript file - in the default integration, this means changing the version number of `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/appboy.min.js` in the `<head>` of your site to `https://js.appboycdn.com/web-sdk/[NEW VERSION NUMBER]/appboy.min.js`
* If you have web push integrated, update the service worker file on your site - by default, this is located at `/service-worker.js` at the root of your site, but the location may be customized in some integrations.

These files must be updated in coordination with each other to ensure proper functionality.

[1]: {{ site.baseurl }}/user_guide/introduction/
[2]: https://github.com/Appboy/appboy-web-sdk#getting-started "Braze Web SDK Github Repository"
[3]: https://www.google.com/analytics/tag-manager/ "Google Tag Manager"
[6]: https://github.com/Appboy/appboy-web-sdk#getting-started "Web SDK Documentation"
[9]: https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html "JSDocs"
[11]: {% image_buster /assets/img_archive/gtm_trigger.png %}
[12]: {% image_buster /assets/img_archive/gtm_example.png %}
[13]: https://github.com/appboy/appboy-web-sdk#alternative-google-tag-manager-installation
[14]: {% image_buster /assets/img/api_key_location.png %}
[15]: https://github.com/Appboy/appboy-web-sdk#alternative-npm-installation
