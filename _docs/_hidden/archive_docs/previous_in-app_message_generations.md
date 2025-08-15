---
nav_title: Previous generations
article_title: Previous In-App Message Generations
page_order: 20
page_type: reference
description: "This article reviews previous information around in-app messages in Braze."
channel: in-app messages
noindex: true
hidden : true
---

# Previous in-app message generations

{% alert important %}
This page reviews previous information around our in-app messages. To see the most up-to date information on our current in-app message generation, see our current [in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) documentation.
{% endalert %}

## Universal

This will review previous information around our in-app messages. To see the most up-to date information on our current in-app message generation, see our [in-app message overview documentation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/).

{% details Fullscreen %}
These are the most engaging, but also the most intrusive since they cover your user's entire screen. They are great for displaying large, rich images, and can be useful in conveying very important information, such as crucial new features and expiring promotions. Since they are more disruptive of the user experience, use these sparingly for top priority content.

![Fullscreen Message]({% image_buster /assets/img_archive/braze_fullscreen.png %}){: style="max-width:80%;"}

**Customizable Features**

- Header and body text
- A large image
- Up to two call to action buttons with separate on-click behavior and deep links
- Different colors for the header and body text, buttons and background
- Key-value pairs

{% enddetails %}
{% details  Modal %}
These messages aren't as intrusive as fullscreen messages, as they still allow users to see part of your app's UI. Since they still contain buttons and images, modal messages may be a better option than slideups if you desire a more interactive, visual campaign. These are great for medium priority content, such as app updates and non-urgent deals and events.

![Modal Message]({% image_buster /assets/img_archive/braze_modal.png %}){: style="max-width:80%;"}

**Customizable Features**

- Header and body text
- An image or customizable badge icon
- Up to two call to action buttons with separate on-click behavior and deep links
- Different colors for the header and body text, buttons and background
- Key-value pairs

{% enddetails %}

{% details Traditional Slideup %}
These are the least intrusive message type, though they can be more or less attention-grabbing depending on your usage of colors and badge icons. This may be the message format to use when onboarding new users and directing them toward particular in-app features, as they don't pause the app experience and allow for continuous exploration.

![Slideup Message]({% image_buster /assets/img_archive/stopwatch_slideup_IAM.gif %}){: style="max-width:50%;"}

**Customizable Features**

- Body text
- An image or customizable badge icon
- Different colors for slideup background, text and icon
- Message close behavior
- Slideup position (top or bottom of the app screen)
- Key-value pairs

{% enddetails %}

<br>

## Web

This will review previous information around more customized in-app messages. To see the most up-to date information on our current in-app message generation, see our [customization documentation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

{% details Email capture message %}
Email capture messages allow you to easily prompt users of your site to submit their email address, after which it will be available within the Braze system for use in all your messaging campaigns.

![Email capture message]({% image_buster /assets/img_archive/web-email-capture.png %}){: style="max-width:60%;"}

>  To enable email capture in-app messages through the Web SDK, you must supply the `allowUserSuppliedJavascript` initialization option to Braze, for example, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. This is for security reasons - HTML in-app messages can execute JavaScript so we require a site maintainer to enable them.

**Customizable Features**

- Header, body, and submit button text
- An optional image
- An optional "Terms of Service" link
- Different colors for the header and body text, buttons and background
- Key-value pairs

{% enddetails %}

{% details Custom HTML Message %}

While Braze's out-of-the box in-app messages can be customized in a variety of ways, you can gain even greater control over the look and feel of your campaigns using messages designed and built using HTML, CSS, and JavaScript. With some simple composition, you can unlock custom functionality and branding to match any of your needs. HTML in-app messages allow for greater control over the look and feel of a message, and anything supported by HTML5 is also supported by Braze.

**JavaScript Bridge (appboyBridge)**

HTML in-app messages support a JavaScript "bridge" interface to the Braze Web SDK, allowing you to trigger custom Braze actions when users click on elements with links or otherwise engage with your content. The following JavaScript methods are supported in Braze's HTML in-app messages:

{% multi_lang_include archive/appboyBridge.md platform="web" %}

Additionally, for analytics tracking, any `<a>` or `<button>` elements in your HTML will automatically log a "click" action to the campaign associated with the in-app message. To log a "button click" instead of a "body click," either provide a query string value of abButtonId on your link's href (for example, `<a href="http://mysite.com?abButtonId=0">click me</a>`), or provide an id on the HTML element (for example, `<a id="0" href="http://mysite.com">click me</a>`). Note that the only button ids currently accepted are "0" and "1." A link with a button id of 0 will be represented as "Button 1" on the dashboard, while a link with a button id of 1 will be represented as "Button 2."

>  To enable HTML in-app messages through the Web SDK, you must supply the `allowUserSuppliedJavascript` initialization option to Braze: for example `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. This is for security reasons - HTML in-app messages can execute JavaScript so we require a site maintainer to enable them.

{% enddetails %}

{% details HTML In App-Message Templates %}

We've designed a set of HTML5 in-app messages templates to help you get started. Check out our [GitHub repository](https://github.com/braze-inc/in-app-message-templates) which contains detailed instructions on how to use and customize these templates for your needs.

**Customizable Features**

- Fonts
- Styles
- Images + Videos
- On-click behaviors
- Interactive Components

{% enddetails %}

<br>

## Specifications

This will review previous information around our in-app message creative specifications. to see the most up-to date information on our current in-app message generation, see our [creative specs documentation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Character and image limits

For all of the in-app message types listed in the following table, the following additional guidelines apply:

- **Recommended image size:** 500&nbsp;KB 
- **Max image size:** 5&nbsp;MB
- **Supported file types:** PNG, JPEG, GIF

| Type                               | Aspect Ratio | Max Character Count |
| :--------------------------------- | :----------: | :-----------------: |
| Portrait Full Screen (Image Only)  |    10:16     |         240         |
| Portrait Full Screen (With Text)   |     5:4      |         240         |
| Landscape Full Screen (With Text)  |     16:5     |         240         |
| Landscape Full Screen (Image Only) |    16:10     |         240         |
| Slideup                            |     1:1      |         140         |
| Modal (Image Only)                 |     1:1      |         140         |
| Modal (With Text)                  |    29:10     |         140         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Keeping in-app message file sizes small

Braze recommends you keep your images, and HTML assets zips as small as possible for several reasons:

- Smaller HTML and image message payloads will download faster, and display more quickly and reliably for your customers.
- Smaller HTML and image message payloads will keep your customer's data costs down as well. Braze in-app messages are downloaded in the background on session start so they can be triggered in real-time based upon whatever criteria you select. As a result, if you have 10 HTML in-app messages of 1&nbsp;MB each, your customers would all incur 10&nbsp;MB of data charges even if they never triggered all of those messages. This can add up quickly over time, even though the in-app messages are cached and not re-downloaded session to session.

The following strategies are helpful for keeping file sizes down:

- Reference fonts embedded in your application or website to customize your HTML in-app messages rather than including the font files in your HTML asset ZIP folder.
- Ensure no extraneous or duplicative CSS or JavaScript are included in your HTML asset ZIPs.
- Use [ImageOptim](https://imageoptim.com/) on all images to compress images to their minimum possible size with no reduction in quality.

### iPhone 5 specs

![iPhone 5 Specs]({% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_05.png %})

### iPhone 6 specs

![iPhone 6 Specs]({% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_06.png %})




