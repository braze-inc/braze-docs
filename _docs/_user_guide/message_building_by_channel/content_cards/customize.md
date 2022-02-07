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

Best suited for teams with limited developer resources, the Crawl approach relies solely on out-of-the-box [Content Card templates]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/) to get you up and running with Content Cards in as little as one hour.

Some light development work is needed upfront to decide where Content Cards will appear in your app or website. With this approach, customization is in the hands of marketers, who determine the content, audience, and timing of each Content Card directly in Braze. However, styling options are limited.

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
    <td><b>Developer work</b></td>
    <td>0-1 hours</td>
  </tr>
  <tr>
    <td><b>Card style</b></td>
    <td>Choose from three Braze templates.</td>
  </tr>
  <tr>
    <td><b>Card behavior</b></td>
    <td>Choose from three "on-click behavior" options.</td>
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

{% endtab %}
{% tab Walk %}

![Alt text]({% image_buster/assets/img_archive/cc_pyrite_walk.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Summary text here 

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
    <td></td>
  </tr>
  <tr>
    <td><b>Developer work</b></td>
    <td></td>
  </tr>
  <tr>
    <td><b>Card style</b></td>
    <td></td>
  </tr>
  <tr>
    <td><b>Card behavior</b></td>
    <td></td>
  </tr>
  <tr>
    <td><b>Card order</b></td>
    <td></td>
  </tr>
  <tr>
    <td><b>Analytics tracking</b></td>
    <td></td>
  </tr>
  <tr>
    <td><b>Key-value pairs</b></td>
    <td></td>
  </tr>
</tbody>
</table>

{% endtab %}
{% tab Run %}

![Alt text]({% image_buster/assets/img_archive/cc_pyrite_run.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Summary text here 

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
    <td></td>
  </tr>
  <tr>
    <td><b>Developer work</b></td>
    <td></td>
  </tr>
  <tr>
    <td><b>Card style</b></td>
    <td></td>
  </tr>
  <tr>
    <td><b>Card behavior</b></td>
    <td></td>
  </tr>
  <tr>
    <td><b>Card order</b></td>
    <td></td>
  </tr>
  <tr>
    <td><b>Analytics tracking</b></td>
    <td></td>
  </tr>
  <tr>
    <td><b>Key-value pairs</b></td>
    <td></td>
  </tr>
</tbody>
</table>

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


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/customization/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/