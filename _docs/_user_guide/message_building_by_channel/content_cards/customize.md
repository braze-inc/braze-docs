---
nav_title: Customize
article_title: Customize Content Cards
page_order: 2
description: "Customizing Content Cards and the feed they'll sit in must be done with your engineers and developers."
channel:
  - content cards
  
---

# Customize Content Cards

> This article provides a breakdown in the different customization options available as part of your Content Card implementation. For technical details, visit our developer documentation for [Android][1], [iOS][2], or [Web][3].

Customizing Content Cards and the feed they are located in can't be done during the campaign creation process—you must work with your engineers and developers to build and customize your cards.

## Customization approaches

Content Cards are fully customizable! At Braze, we break down customization into three different approaches based on the associated effort and level of flexibility provided. These approaches are referred to as "crawl", "walk", or "run".

- **Crawl:** Take advantage of Braze's out-of-the-box Content Card styling options for a quick, low-effort implementation.
- **Walk:** Add some custom styling to out-of-the-box Content Cards to better match your brand experience.
- **Run:** Customize every part of your Content Card campaigns, from style to behavior to cross-channel connections.

<style>
table {
  width: 60%;
}
table td {
    word-break: break-word;
}
</style>

{% tabs %}
{% tab Crawl %}

![Sample finance app showing Captioned Image and Banner Content Cards]({% image_buster/assets/img_archive/cc_pyrite_crawl.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Best suited for teams with limited developer resources, the Crawl approach relies solely on out-of-the-box [Content Card templates]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/) to get you up and running with Content Cards with less than five lines of code.

With this approach, customization is in the hands of marketers, who determine the content, audience, and timing of each Content Card directly in Braze. Some light development work is needed upfront to decide where Content Cards will appear in your app or website, and styling options are limited.

<table>
<thead>
  <tr>
    <th>Customization</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Effort</b></td>
    <td>Low</td>
  </tr>
  <tr>
    <td><b>Card style</b></td>
    <td>Choose from three Braze templates.</td>
  </tr>
  <tr>
    <td><b>Card behavior</b></td>
    <td>Choose from three on-click behavior options.</td>
  </tr>
  <tr>
    <td><b>Card order</b></td>
    <td>Newer Content Cards appear toward the top of the feed. Pinned cards stay at the very top.</td> 
  </tr>
  <tr>
    <td><b>Analytics tracking</b></td>
    <td>Content Card analytics are captured in Braze.</td>
  </tr>
  <tr>
    <td><b>Key-value pairs</b></td>
    <td>Optional, powers additional UI/UX customization.</td>
  </tr>
</tbody>
</table>

{% alert tip %}
Content Cards are considered out-of-the-box when you leverage the Braze SDK table view to display cards. If you want your Content Cards to blend into your app or site within any location, or need additional functionality not mentioned in this section, consider a Walk or Run approach instead.
{% endalert %}

{% endtab %}
{% tab Walk %}

![Sample finance app showing Content Cards with customization]({% image_buster/assets/img_archive/cc_pyrite_walk.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

A hybrid approach to implementation, the Walk approach involves both marketing and developer teams pitching in to match your app or site's branding. 

During the implementation process, developers write custom code to match the look and feel of Content Cards to that of your brand. This includes font type, font size, rounded corners, and colors. This approach still uses the out-of-the-box Content Cards, however, template styling is handled programmatically by your developers.

Marketers still maintain control of the audience, content, on-click behavior, expiration, and pinning directly in the Braze dashboard.

<table>
<thead>
  <tr>
    <th>Customization</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Effort</b></td>
    <td>Low</td>
  </tr>
  <tr>
    <td><b>Card style</b></td>
    <td>Choose from three Braze templates or use your own developer-created templates.</td>
  </tr>
  <tr>
    <td><b>Card behavior</b></td>
    <td>Choose from three on-click behavior options.</td>
  </tr>
  <tr>
    <td><b>Card order</b></td>
    <td>Newer Content Cards appear toward the top of the feed. Pinned cards stay at the very top.</td>
  </tr>
  <tr>
    <td><b>Analytics tracking</b></td>
    <td>Content card analytics are captured in Braze.</td>
  </tr>
  <tr>
    <td><b>Key-value pairs</b></td>
    <td>Optional, powers additional UI/UX customization.</td>
  </tr>
</tbody>
</table>

{% endtab %}
{% tab Run %}

![Sample finance app showing custom Content Cards with email capture]({% image_buster/assets/img_archive/cc_pyrite_run.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

With the Run approach, developers take the lead with full control of the Content Card user experience. Custom code dictates what the cards will look like, how they behave, and how they interact with other messaging channels (e.g., triggering a Content Card based on a push notification). 

The Braze SDK does not handle the on-click behavior, order, or analytics. These traits must be handled programmatically by the developer for marketers to access valuable Content Card metrics in the Braze dashboard—like impressions, clicks, and dismissals.

<table>
<thead>
  <tr>
    <th>Customization</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Effort</b></td>
    <td>Depends on use case.</td>
  </tr>
  <tr>
    <td><b>Card style</b></td>
    <td>Custom</td>
  </tr>
  <tr>
    <td><b>Card behavior</b></td>
    <td>Custom</td>
  </tr>
  <tr>
    <td><b>Card order</b></td>
    <td>Custom</td>
  </tr>
  <tr>
    <td><b>Analytics tracking</b></td>
    <td>Custom</td>
  </tr>
  <tr>
    <td><b>Key-value pairs</b></td>
    <td>Required</td>
  </tr>
</tbody>
</table>

### Use cases

- Multiple Content Card feeds, such as adding a newsfeed, notification center, or promotions tab.
- Display Content Cards in an existing feed.
- Display Content Cards in a carousel view.
- Use a Content Card to capture user information.
- Trigger Content Cards based on other messaging channels.

{% alert tip %}
Check out the sample use cases for [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/implementation_guide/#sample-use-cases) and [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/implementation_guide/#sample-use-cases) outlined in our Advanced Content Card implementation guides to get an idea of what you can do with this approach.
{% endalert %}

{% endtab %}
{% endtabs %}

## Change "empty feed" language

You can change the language that appears automatically in empty Content Card feeds by [redefining the localizable content card strings](https://github.com/Appboy/appboy-ios-sdk/blob/3cca65b06f66085f5bc7c8e1ad267bf8bb1f0da7/AppboyUI/ABKContentCards/Resources/en.lproj/AppboyContentCardsLocalizable.strings) in your app’s localizable strings file: 
```
"Appboy.content-cards.no-card.text" = "No Cards!!!!";
"Appboy.content-cards.done-button.title" = "Done";
"Appboy.content-cards.no-card.text" = "We have no updates.\nPlease check again later.";
"Appboy.content-cards.no-connection.title" = "Connection Error";
"Appboy.content-cards.no-connection.message" = "Cannot establish network connection.\nPlease try again later.";
```
{% alert note %}
If you want to update it for different languages, find the corresponding language in the [Resources folder structure](https://github.com/Appboy/appboy-ios-sdk/tree/3cca65b06f66085f5bc7c8e1ad267bf8bb1f0da7/AppboyUI/ABKContentCards/Resources) with the same string `Appboy.content-cards.no-card.text`.
{% endalert %}


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/custom_styling/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/customization/custom_styling/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/custom_ui/