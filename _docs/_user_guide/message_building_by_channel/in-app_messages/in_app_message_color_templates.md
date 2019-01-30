---
nav_title: Color Templates
platform: Message_Building_and_Personalization
subplatform: In-App Messages
page_order: 2
---
# In-App Message Templates {#in-app-message-color-templates}

You can save in-app message and in-browser message templates on the dashboard to swiftly build new campaigns and messages using your style. Go to __Templates & Media__, then the __In-App Message Templates__ tab. From this page, you can either edit existing templates, or click __+ Create__ and choose __Color Profile__ or __CSS Template__ to create new templates to use in your in-app messages.



## Color Profile {#adding-a-color-profile}

You can customize the color scheme of your message template by either entering HEX color code or by clicking the colored box and selecting a color with the color picker.

Click __Save Color Profile__ on the bottom right when you’re finished.

## CSS Template

You can customize a complete CSS template for your [Web Modal In-App Message][6].

Name and tag your CSS Template, then choose whether or not it will be your default template. You can write your own CSS in the provided space. This space is already pre-filled with the CSS shown in your message preview, and you should feel free to adjust it slightly to meet your needs.

```css
.ab-message-header, .ab-message-text {
  color: #252525;
  text-align: center;
}

.ab-message-header {
  font-size: 19px;
  font-weight: bold;
}

.ab-message-text {
  font-size: 14px;
  font-weight: normal;
}

.ab-close-button {
  color: #c4c4c4;
}

.ab-message-button {
  background-color: #1b78cf;
  color: #ffffff;
  font-size: 12px;
  font-weight: bold;
}

.ab-background {
  background-color: #f7f7f7;
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


[6]: {{ site.baseurl }}/creating_an_in-app_message/#step-2-compose-in-app-message
