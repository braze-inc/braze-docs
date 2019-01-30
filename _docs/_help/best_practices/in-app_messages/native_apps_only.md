---
nav_title: Native (Apps Only)
page_order: 2
---

# Native (Apps Only)

## Custom HTML Message {#native-html-messages}
While Braze’s out-of-the box in-app messages can be customized in a variety of ways, you can gain even greater control over the look and feel of your campaigns using messages designed and built using HTML5. With some simple composition, you can unlock custom functionality and branding to match any of your needs.

![HTML5 In App Message][16]

Select the “Custom HTML” message type in your in-app message campaign composer. From here, you’ll see a field to input the HTML for your custom in-app message, as well as a file uploader section. This uploader accepts zipped files that should include all of the assets your HTML references (fonts, images, styles, etc.). Since the assets file and HTML code are uploaded separately, it should not be expected that the HTML will automatically populate per asset file upload. Also, as we do not currently support a preview of your HTML in-app messages, we recommend sending yourself a test HTML message before launching this type of campaign to your users.

HTML5 in-app messages allow for greater control over the look and feel of a message, and anything supported by HTML5 is also supported by Braze. For example, Soundcloud uses HTML5 in-app messages to conduct a user satisfaction survey:

![HTML5 Gif][17]

### JavaScript Bridge (appboyBridge)

From iOS version `2.29.0` and Android version `2.0.0`, HTML in-app messages support a Javascript "bridge" interface to the Braze SDK, allowing you to trigger custom Braze actions when users click on elements with links or otherwise engage with your content. The following javascript methods are supported in Braze's HTML in-app messages:

{% include archive/appboyBridge.md platform="native" %}

### Link-Based Actions

HTML in-app messages can trigger custom Braze actions when users click on elements with links. The supported link schemes are:

Supported Scheme | Corresponding Action | Supported Query Strings
--- | --- |---
Normal Web URL or Deep Linking | For web URLs, Braze will open the new content of the link in a webview within your app by default, or in an external browser when query `abExternalOpen` is true. The HTML5 in-app message will be dismissed before opening the link. For deep linking, Braze will open your URL regardless of the value of `abExternalOpen`. | `abExternalOpen` and `abButtonId`
`appboy://close` | Braze will dismiss the HTML in-app message. | None
`appboy://feed` | Braze will dismiss the HTML in-app message and display a modal News Feed. | `abButtonId`
`appboy://customEvent` | Braze will log a custom event and will NOT dismiss the HTML in-app message. | `name`<br>All additional queries will be set as properties of the custom event.

### Supported Query Strings

You can customize your link actions by appending the optional URL query strings below to your HTTP(S) link:

Query String Name | Value | Action
-----------|-------|-------
`abButtonId` | `{0,1}` | Braze will use the value specified as the button's ID for analytics tracking<br>([https://www.picsart.com?abButtonId=0][23]) *
`name` | Arbitrary string | This represents the custom event name for use with `appboy://customEvent` (e.g., `appboy://customEvent?name=eventName`).
`abExternalOpen` | `{true, false}` | When this query string parameter is absent or set to `false`, Braze will try to open the web link in an internal web browser inside the host app. To have Braze open the web link in an external web browser, set this parameter to `true`.
`abDeepLink` | `{true, false}` | When this query string parameter is absent or set to `false`, Braze will try to open the web link in an internal web browser inside the host app. To have Braze handle your HTTP(S) link as a deep link, set this parameter to `true`.

Analytics tracking is enabled by default for all links that have the `abButtonId` query (see above). A link with `abButtonId=0` will be represented as Button 1 on the Dashboard, while a link with `abButtonId=1` will be represented as Button 2.


Examples:

- `appboy://close`
	- sample close button: `<a href="appboy://close">Close</a>`
- `appboy://feed?abButtonId=0`
- `appboy://customEvent?name=eventName&property1=value1&property2=value2`
	- This would log an event called `eventName` with the properties `property1`=`value1` and `property2`=`value2`.

If you are interested in customizing your in-app messages, please make sure your design or development team is aware of these parameters.

### HTML5 In-App Message Templates

We've designed a set of six HTML5 in-app messages templates to help you get started. Check out our [Github repository][22] which contains detailed instructions on how to use and customize these templates for your needs.

### Customizable Features

- Fonts
- Styles
- Images + Videos
- On-click behaviors
- Interactive Components

[1]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content
[5]: {% image_buster /assets/img_archive/inappexample.png %}
[7]: {{ site.baseurl }}/help/faqs/
[8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/#manually-queue-in-app-message-display
[9]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/in_app_messaging/#slideup-in-app-messages
[10]: {% image_buster /assets/img_archive/braze_fullscreen.png %}
[11]: {% image_buster /assets/img_archive/braze_modal.png %}
[12]: {% image_buster /assets/img_archive/stopwatch_slideup_IAM.gif %}
[13]: {% image_buster /assets/img_archive/braze_campaigndetails.png %}
[14]: {% image_buster /assets/img_archive/web-email-capture.png %}
[15]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/scheduling_your_campaign/#action-based-delivery-event-triggered-campaigns
[16]: {% image_buster /assets/img_archive/braze_customhtml.png %}
[17]: {% image_buster /assets/img_archive/HTML5.gif %}
[18]: {% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_05.png %}
[19]: {% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_06.png %}
[20]: {% image_buster /assets/img_archive/braze_campaignpriority.png %}
[21]: {{ site.baseurl }}/help/best_practices/push/#creating-custom-opt-in-prompts
[22]: https://github.com/Appboy/appboy-custom-html5-in-app-message-templates
[23]: https://www.picsart.com?abButtonId=0
[25]: https://imageoptim.com/
