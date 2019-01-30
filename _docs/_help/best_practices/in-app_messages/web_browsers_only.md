---
nav_title: Web (Browsers Only)
page_order: 3
---

# Web (Browsers Only)

## Email Capture Message
Email capture messages allow you to easily prompt users of your site to submit their email address, after which it will be available within the Braze system for use in all your messaging campaigns.

![Email Capture Message][14]

>  To enable Email Capture in-app messages, your SDK integration must supply the `enableHtmlInAppMessages` initialization option to Braze, e.g. `appboy.initialize('YOUR-API_KEY', {enableHtmlInAppMessages: true})`. This is for security reasons - HTML in-app messages can execute javascript so we require a site maintainer to enable them.

### Customizable Features

- Header, body, and submit button text
- An optional image
- An optional "Terms of Service" link
- Different colors for the header and body text, buttons and background
- Key-value pairs

## Custom HTML Message {#web-html-messages}

While Braze’s out-of-the box in-app messages can be customized in a variety of ways, you can gain even greater control over the look and feel of your campaigns using messages designed and built using HTML, CSS, and Javascript. With some simple composition, you can unlock custom functionality and branding to match any of your needs. HTML in-app messages allow for greater control over the look and feel of a message, and anything supported by HTML5 is also supported by Braze.

### JavaScript Bridge (appboyBridge)

HTML in-app messages support a Javascript "bridge" interface to the Braze Web SDK, allowing you to trigger custom Braze actions when users click on elements with links or otherwise engage with your content. The following javascript methods are supported in Braze's HTML in-app messages:

{% include archive/appboyBridge.md platform="web" %}

Additionally, for analytics tracking, any `<a>` or `<button>` elements in your HTML will automatically log a "click" action to the campaign associated with the in-app message. To log a "button click" instead of a "body click," either provide a query string value of abButtonId on your link's href (e.g. `<a href="http://mysite.com?abButtonId=0">click me</a>`), or provide an id on the HTML element (e.g. `<a id="0" href="http://mysite.com">click me</a>`). Note that the only button ids currently accepted are "0" and "1." A link with a button id of 0 will be represented as "Button 1" on the Dashboard, while a link with a button id of 1 will be represented as "Button 2."

>  To enable HTML in-app messages, your SDK integration must supply the `enableHtmlInAppMessages` initialization option to Braze: for example `appboy.initialize('YOUR-API_KEY', {enableHtmlInAppMessages: true})`. This is for security reasons - HTML in-app messages can execute javascript so we require a site maintainer to enable them.

### HTML In App-Message Templates

We've designed a set of HTML5 in-app messages templates to help you get started. Check out our [Github repository][22] which contains detailed instructions on how to use and customize these templates for your needs.

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
