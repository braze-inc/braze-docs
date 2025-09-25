---
nav_title: Judo
article_title: Judo
description: "This reference article outlines the partnership between Braze and Judo, a no-code server-driven UI platform that allows you to add location context and tracking to your iOS and Android apps."
alias: /partners/judo/
page_type: partner
search_tag: Partner

---

# Judo

> [Judo](https://judo.app) is a server-driven UI platform that empowers publishers to efficiently deliver rich, engaging in-app user experiences without app updates.

_This integration is maintained by Judo._

## About the integration

The Braze and Judo integration provides bespoke experiences in your campaigns and Canvases. Instead of a simple, templated landing page experience, a Braze campaign may incorporate content that comprises multiple screens, modals, video, custom fonts, and support settings such as dark mode and accessibility built without code and deployed without app updates. Data from Braze may also be used to support personalized content in a Judo Experience. User events and data from the experience can feedback into Braze for attribution and targeting.

## Prerequisites

| Requirement | Description |
|---|---|
| Judo Account | A [Judo](https://www.judo.app/) account is required to take advantage of this partnership. |
| Judo SDK | The Judo SDK must be integrated into your [iOS](https://github.com/judoapp/judo-ios/) and/or [Android](https://github.com/judoapp/judo-android) apps. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

**Onboarding**: App publishers using Judo build and deploy rich, native onboarding experiences. These experiences can now be one element in a personalized cross-channel onboarding journey coordinated via Braze. Experiences may be personalized and quickly updated without any app updates to test the effectiveness of different in-app flows.

**Conversion**: App publishers can use data from Braze to create a personalized rich in-app experience to drive in-app purchases, paid subscriptions, or contextual merchandising using integration hooks in Judo. Access to these experiences may be triggered via engagement marketing campaigns created in Braze.

**Event-Driven Content**: A primary use for Judo in sports and entertainment is building rich experiences to preview, promote, and recap events. This capability has broad applications in other verticals for seasonal and news-driven content. Linking messaging to promote or highlight events in a timely manner to rich in-app experiences empowers publishers to drive engagement by being contextually relevant.

## Side-by-side SDK integration

Judo offers additional libraries that automate some of the effort necessary to integrate the Judo and Braze SDKs side-by-side in your mobile apps. 

### Step 1: Install the Judo-Braze integration library

Install and set up the Judo-Braze integration library into your apps. This will automatically enable event tracking.

- [iOS installation
instructions](https://github.com/judoapp/judo-braze-ios/wiki#installation)
- [Android installation
instructions](https://github.com/judoapp/judo-braze-android/wiki#installation).

### Step 2: Configure in-app messaging

This step will involve creating custom `ABKInAppMessageControllerDelegate` and `IInAppMessageManagerListener` implementations for iOS and Android.

See the in-app message setup documentation bundled for each of the integration libraries:

- [iOS In-App Messaging
Setup](https://github.com/judoapp/judo-braze-ios/wiki#in-app-messaging-setup)
- [Android In-App Messaging
Setup](https://github.com/judoapp/judo-braze-android/wiki#in-app-messaging-setup).

## Using this integration

Once you have finished the app-side integration, you can test it by running a test Braze in-app message campaign for a Judo Experience to verify that it runs as expected.

### Step 1: Create a custom code in-app message campaign

From the Braze platform, create a Braze in-app message campaign with a **Custom Code** message type. Next, select **HTML Upload** as the custom type. Make sure to populate the content of the message with the base in-app messaging fields; this content will not be shown to the user.

![An image of what the dashboard looks like when selecting the "Custom Code" message type.]({% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %})

Next, use the following minimal HTML snippet to satisfy the form validation: 
```
<a href="appboy://close">X</a>
```

Note that this will not be displayed in production on your device as Judo will rewrite and replace this with a Judo Experience.

![An image showing the form validation code added to the compose step of your campaign.]({% image_buster /assets/img/judo/braze-html-boilerplate.png %})

### Step 2: Set a key-value pair for Judo
![This image shows the one key-value pair needed for this integration with the "key" being "judo-experience", and the "value" being your Judo link.]({% image_buster /assets/img/judo/braze-campaign-extras-judo-experience.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Set a [custom key-value pair]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) on the campaign with a key of `judo-experience`. Provide the URL of the Judo Experience you'd like to show here. The Judo-Braze integration library will then detect this key-value pair in the handler and use it to inject your Judo Experience in place of the standard Braze in-app message UI.
<br><br>
### Step 3: Finishing the campaign

Lastly, complete the campaign, setting up a trigger for the campaign and selecting users via Segments in the **Delivery** and **Target User** sections. Visit our in-app message [article]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/) on the different components of a Braze in-app message.


