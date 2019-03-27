---
nav_title: Overview
page_order: 0
---

# In-App Messages

__In-App Messages__ help you get content to your user without interrupting their day with a push notification. Customized and tailored in-app messages enhance the user experience and help your audience get the most value out of your app. With a variety of layouts and customization tools to choose from, in-app messages engage your users more than ever before.

To see examples of in-app messages, check out our [Client Integration Gallery][11].

{% alert note %}
Braze has refreshed in-app messages! Though the creation process is very much the same, our in-app messages have a new, modern look and feel optimized for the best experiences for your customers and give you more options to personalize the experience. For more information on our most recent upgrades and how to apply them to your messages, check out our [Generation Comparison documentation]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/generations/)!
{% endalert %}

[Create an in-app message]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/create/) now!

## When to Use In-App Messages

In-app messages are good for a lot of things. These messages don't deliver outside of the user's app and won't intrude on their home screen. In-app messages, by their nature, exist within your app and come with context and are almost never unwelcome! They're always delivered when the user is active within your app.

### Great Use Cases

- New App Features
- App Management
- Reviews
- App Upgrades/Updates
- Giveaways & Sweepstakes
- Sales and Promotions
- Product Sales
- Encouraging and rewarding discovery
- [Permission Requests/Push Priming][21]

## Expected Behaviors by Message Types

These are what it looks like for your users to open one of our out-of-the-box in-app message types.

{% tabs %}
  {% tab Slideup %}

  Our Slideups typically appear at the top and bottom of the app screen (you can set this when you create your message). These are great for alerting your users about new terms of service, cookies, and other snippets of information.

  <br>

  ![Slideup Behavior]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

  <br>

{% endtab %}
{% tab Modal %}

  Modals appear in the center of the device's screen with a screen overlay that helps it stand out from your app in the background. These are great call-to-action These are perfect for not-so-subtly suggesting that your user take advantage of a sale or giveaway.

  <br>

  ![Modal Behavior]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

  <br>

{% endtab %}
{% tab Full-Screen %}

Full-Screen messages are exactly what you'd expect - they take up the whole screen of the device! This message type is great when you really need your user's attention, like for mandatory app updates.

<br>

![Full-Screen Behavior]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% endtabs %}

[1]: http://yuml.me/e4562a3d.png
[11]: {{ site.baseurl }}/help/best_practices/client_integration_gallery/#client-integration-iam
[21]: {{ site.baseurl }}/help/best_practices/push/creating_custom_opt-in_prompts/#creating-custom-opt-in-prompts
