---
nav_title: Customize
platform: Message_Building_and_Personalization
subplatform: In-App Messages
page_order: 2
description: "In addition to the out-of-the-box In-App Message templates, Braze also offers customized messaging templates that allow custom HTML, Modals with custom CSS, Video, and more."
---

# Customization

Craft and customize the perfect In-App or In-Browser Message using your own HTML, CSS, and Javascript!

{% alert important %}
This guide references our Beta HTML Preview feature for In-App Messages. If this option is not enabled for your account, please contact Braze Support, or use our standard HTML Upload documentation.
{% endalert %}

{% alert note %}
To enable HTML in-app messages in the Web SDK, your SDK integration must supply the `enableHtmlInAppMessages` initialization option to Braze: for example `appboy.initialize('YOUR-API_KEY', {enableHtmlInAppMessages: true})`. This is for security reasons - HTML in-app messages can execute javascript so we require a site maintainer to enable them.
{% endalert %}

## Quickstart Templates

Get a head start using our pre-built HTML templates. Just click "View Code", copy the HTML, and paste it into your In-App message campaign. Swap out images, text, and launch!


|Quickstart Template|Download Link|Screenshot|
|--------|----------|---------|
|Multiple Page Carousel| [View Code](https://raw.githubusercontent.com/braze-inc/in-app-message-templates/master/braze-templates/1-braze-dashboard-carousel-modal/index.html){:target="_blank"}|![Screenshot](https://raw.githubusercontent.com/braze-inc/in-app-message-templates/master/braze-templates/1-braze-dashboard-carousel-modal/screenshot.gif){: style="max-width:200px;width:100%"}|
|Multiple Page Carousel| [View Code](https://raw.githubusercontent.com/braze-inc/in-app-message-templates/master/braze-templates/2-braze-dashboard-simple-modal/index.html){:target="_blank"}|![Screenshot](https://raw.githubusercontent.com/braze-inc/in-app-message-templates/master/braze-templates/2-braze-dashboard-simple-modal/screenshot.gif){: style="max-width:200px;width:100%"}|
|Multiple Page Carousel| [View Code](https://raw.githubusercontent.com/braze-inc/in-app-message-templates/master/braze-templates/3-braze-dashboard-survey-modal/index.html){:target="_blank"}|![Screenshot](https://raw.githubusercontent.com/braze-inc/in-app-message-templates/master/braze-templates/3-braze-dashboard-survey-modal/screenshot.gif){: style="max-width:200px;width:100%"}|
|Multiple Page Carousel| [View Code](https://raw.githubusercontent.com/braze-inc/in-app-message-templates/master/braze-templates/5-fullscreen-pagination/index.html){:target="_blank"}|![Screenshot](https://raw.githubusercontent.com/braze-inc/in-app-message-templates/master/braze-templates/5-fullscreen-pagination/screenshot.gif){: style="max-width:200px;width:100%"}|

## Customizing your HTML




[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/
