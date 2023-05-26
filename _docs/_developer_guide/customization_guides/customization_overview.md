---
nav_title: Customization Overview
article_title: Customization Overview
page_order: 1
description: "This reference article covers the essential concepts of customizing and extending the SDK messaging channels."
  
---

# Customization overview

> Almost everything at Braze is fully customizable! The articles in this Customization Guide show you how to approach refining your Braze experience through a mixture of configuration and customization. During this process, Marketing and Engineering teams should work closely together to coordinate exactly how to customize Braze's messaging channels.

{% alert note %}
The Braze SDK is a powerful toolkit, but at a high level it provides two important pieces of functionality: it helps collect and sync user data across platforms to a consolidated user profile, and also handles messaging channels like in-app messages, push notifications, and Content Cards. The articles in the Customization Guide assume you've already gone through the [SDK implementation process]({{site.baseurl}}/developer_guide/home).
{% endalert %}

All Braze components are crafted with the following principles in mind:


| **Accessible** | {::nomarkdown} <ul><li>Follow accessibility guidelines and are compatible with VoiceOver</li><li>Support Dynamic Type </li></ul> {:/}|
| **Adaptive** | {::nomarkdown} <ul><li>Light and dark mode compatible</li><li>Support multiple device sizes and orientations, including multitasking UIs</li><li>Support Safe Area and Layout Margins</li><li>Support right-to-left layouts</li><li>Support on-screen keyboard</li></ul> {:/}|
| **Customizable** | {::nomarkdown} <ul><li>Padding, margin, spacing, font, image size, and more</li><li>Sensible defaults</li><li>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 border: none;}

**Accessible**
* Follow accessibility guidelines and are compatible with VoiceOver
* Support Dynamic Type

**Adaptive**
* Light and dark mode compatible
* Support multiple device sizes and orientations, including multitasking UIs
* Support Safe Area and Layout Margins
* Support right-to-left layouts
* Support on-screen keyboard

**Customizable**
* Padding, margin, spacing, font, image size, and more
* Sensible defaults

For these reasons, we recommend starting with the default `BrazeUI` components and customizing them to suit your brand needs and use case. At Braze, we break down customization into three different approaches based on the associated effort and level of flexibility provided. These approaches are referred to as "crawl", "walk", or "run."

- **Crawl:** Take advantage of Braze's basic styling options for a quick, low-effort implementation.
- **Walk:** Add some custom styling to the default templates to better match your brand experience.
- **Run:** Customize every part of your messaging, from style to behavior to cross-channel connections.

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

The Crawl approach puts the power of customization directly in the hands of marketers. While some light development work is necessary upfront to integrate Braze's messaging channels with your app or site, this approach allows you to get up and running quickly. 

Marketers determine the the content, audience, and timing of messages through the dashboard. Styling options are limited, however. This approach is best suited for teams with limited developer resources or who want to quickly share simple content. 

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
    <td><b>Developer Work</b></td>
    <td>0-1 hours</td>
  </tr>
  <tr>
    <td><b>Card style</b></td>
    <td>Use Braze's default templates.</td>
  </tr>
  <tr>
    <td><b>Behavior</b></td>
    <td>Choose from default behavior options.</td>
  </tr>
  <tr>
    <td><b>Analytics tracking</b></td>
    <td>Analytics are captured in Braze.</td>
  </tr>
  <tr>
    <td><b>Key-value pairs</b></td>
    <td>Optional, powers additional UI/UX customization.</td>
  </tr>
</tbody>
</table>

{% endtab %}
{% tab Walk %}

![Sample finance app showing Content Cards with customization]({% image_buster/assets/img_archive/cc_pyrite_walk.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

A hybrid approach to implementation, the Walk approach involves both marketing and developer teams pitching in to match your app or site's branding. 

During the implementation process, developers write custom code to update a message channel's look and feel to more closely match your brand. This includes changing font type, font size, rounded corners, and colors. This approach still uses the default options, just with programmatic template styling.

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
    <td><b>Developer Work</b></td>
    <td>0-4 hours</td>
  </tr>
  <tr>
    <td><b>UI</b></td>
    <td>Use Braze's templates or use your own developer-created templates.</td>
  </tr>
  <tr>
    <td><b>Behavior</b></td>
    <td>Choose from default behavior options.</td>
  </tr>
  <tr>
    <td><b>Analytics tracking</b></td>
    <td>Default analytics are captured in Braze.</td>
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

With the Run approach, developers take the lead with full control of the user experience. Custom code dictates what the messages will look like, how they behave, and how they interact with other messaging channels (e.g., triggering a Content Card based on a push notification).

When you create completely new custom content, such as new types of Content Cards or in-app messages with bespoke UI, the Braze SDK won’t automatically [track analytics]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/). You must be programmatically handle analytics so marketers continue to have access to metrics like impressions, clicks, and dismissals in the Braze dashboard. Call the Braze SDK’s analytics methods to have the SDK pass this data back to Braze. Each messaging channel has an analytics article to help facilitate this.

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
    <td><b>Developer Work</b></td>
    <td>Low effort: 1-4 hours<br>Medium effort: 4-8 hours<br>High effort: 8+ hours</td>
  </tr>
  <tr>
    <td><b>UI</b></td>
    <td>Custom</td>
  </tr>
  <tr>
    <td><b>Behavior</b></td>
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
{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/custom_styling/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/customization/customizing_feed/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/custom_ui/
