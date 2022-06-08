---
nav_title: Color Profiles and CSS Templates
article_title: Color Profiles and CSS Templates for In-App Messages
page_order: 4
page_type: reference
description: "This article provides an overview of in-app message color profiles and CSS templates."
channel:
  - in-app messages
---

# Color profiles and CSS templates {#reusable-color-profiles}

You can save in-app message and in-browser message templates on the dashboard to swiftly build new campaigns and messages using your style. Go to **Templates & Media**, then the **In-App Message Templates** tab. From this page, you can either edit existing templates or click **+ Create** and choose **Color Profile** or **CSS Template** to create new templates to use in your in-app messages.

## Color profile

You can customize the color scheme of your message template by either entering a HEX color code or by clicking the colored box and selecting a color with the color picker.

Click **Save Color Profile** when you’re finished.

### Managing color profiles

You can also [duplicate][6] and [archive][7] templates! Learn more about creating and managing templates and creative content in [Templates & Media][8].

## CSS template {#in-app-message-templates}

You can customize a complete CSS template for your [web modal in-app message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/modal_with_css/).

Name and tag your CSS Template, then choose whether or not it will be your default template. You can write your own CSS in the provided space. This space is already pre-filled with the CSS shown in your message preview, and you should feel free to adjust it slightly to meet your needs.

```css
.ab-message-header, .ab-message-text {
  color: #333333;
  text-align: center;
}

.ab-message-header {
  font-size: 20px;
  font-weight: bold;
}

.ab-message-text {
  font-size: 14px;
  font-weight: normal;
}

.ab-close-button svg {
  fill: #9b9b9b;
}

.ab-message-button {
  border: 1px solid #1b78cf;
  font-size: 14px;
  font-weight: bold;
}
.ab-message-button:first-of-type {
  background-color: white;
  color: #1b78cf;
}
.ab-message-button:last-of-type, .ab-message-button:first-of-type:last-of-type {
  background-color: #1b78cf;
  color: white;
}

.ab-background {
  background-color: white;
}

.ab-icon {
  background-color: #0073d5;
  color: white;
}

.ab-page-blocker {
  background-color: rgba(51, 51, 51, .75);
}
```

As you can see, you can edit everything from the background color to font size and weight, and so much more.

### Managing CSS templates

You can also [duplicate][6] and [archive][7] templates! Learn more about creating and managing templates and creative content in [Templates & Media][8].


[6]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/
[7]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/
[8]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/
