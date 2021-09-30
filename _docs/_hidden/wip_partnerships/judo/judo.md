---
nav_title: Judo
page_order: 1

description: "This is the Google Search and SEO description that will appear, try to make this informative and concise, yet brief."
alias: /partners/judo/

page_type: partner
hidden: true
---

# Judo

[Judo](https://judo.app)'s server-driven UI platform empowers publishers to efficiently deliver rich, engaging in-app user experiences without app updates.

Developers integrating Braze marketing automation with Judo experiences will find elevated value for their joint customers. Superior targeting, personalization and campaign orchestration from Braze are linked to bespoke experiences from Judo. Instead of a simple templated landing page experience a Braze campaign may incorporate content that comprises multiple screens, modals, video, custom fonts and support settings such as dark mode and accessibility built without code and deployed without app updates. Data from Braze may be used to support personalized content in a Judo experience. User data from the experience can feed back into Braze for attribution and targeting.

## Requirements or Prerequisites

First, you will need to have already integrated both Braze and Judo into your apps.

{% alert important %}
The requirements listed below are typical requirements you might need from Braze. We recommend using the attributed titling, origin, links, and phrasing as listed in the chart below. Be sure to adjust the description so that you know what each of these requirements is used to do.
{% endalert %}

| Requirement | Origin | Access | Description |
|---|---|---|---|
| Judo Account | Judo | [Judo](https://www.judo.app/) | You'll need a Judo account in order to host Experiences for launch from Braze |
| Judo SDK | Judo | [Judo iOS SDK](https://github.com/judoapp/judo-ios/) and [Judo Android SDK](https://github.com/judoapp/judo-android) | You'll need the Judo SDKs integrated into your iOS and/or Android apps. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Side-by-Side SDK Integration

Judo offers an additional libraries that automates some of the effort necessary to integrate the Judo and Braze SDKs, side-by-side in your mobile app(s).

### Step 1: Install the Judo-Braze Integration Library

For iOS, see the documentation bundled with the integration libraries: [iOS Installation Instructions](https://github.com/judoapp/judo-braze-ios/wiki#installation) and [Android Installation Instructions](https://github.com/judoapp/judo-braze-android/wiki#installation).

### Step 2: Configure In-App Messaging

This step involves creating custom `ABKInAppMessageControllerDelegate` and `IInAppMessageManagerListener` implementations for iOS and Android respectively. The details are also outlined in the Judo-Braze integration library documentation. 

For iOS, see the documentation bundled with the integration libraries: [iOS In-App Messaging Setup](https://github.com/judoapp/judo-braze-ios/wiki#in-app-messaging-setup) and [Android In-App Messaging Setup](https://github.com/judoapp/judo-braze-android/wiki#in-app-messaging-setup).

## Using this Integration

Create a Braze IAM Campaign in the Braze of the HTML Custom View type. Advance through each the below steps by clicking the "Forward" button in the bar at the very bottom of the display.

### Step 1: Creating an IAM Campaign

![Braze Create Campaign Menu][1]

### Step 2: Selecting "Custom Code" Message Type

While any of the Message Types should work, consider using the Custom Code type. You'll then need to populate the content of the Message with the minimum that Braze requires; note that this will not be shown on to the user, but Braze expects to use its own UI and so requires us to provide some content.

![Braze Custom Code Campaign][2]


With the Custom Code type, use the following minimal HTML snippet to satisfy the form validation: `<a href="appboy://close">X</a>`.

Note that this will not be displayed in production on your device, since this In-App Message will be intercepted and replaced with a Judo experience.

![Braze HTML Snippet][3]

### Step 3: Setting the `judo-experience` Extra

Then, set a custom Extra value on the Campaign with a key of `judo-experience`. Provide the URL of the Judo Experience you'd like to show here. This is what the Judo-Braze integration library will detect in the handler and use to inject your Judo Experience in lieu of the standard Braze IAM UI.

![Braze Campaign Extras Configuration][4]

### Step 4: Finishing the Campaign

You will need to complete the campaign, namely setting up a trigger for the Campaign and selecting users via Segments in the Delivery and Target User sections respectively. This is out of scope of this document, so please see [Braze's Creating an In-App Message Guide](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/create/#step-1-specify-delivery-platforms).


## Use Cases

This can be a critical part of your documentation. Though this is optional, this is a good place to outline typical or even novel use cases for the integration. This can be used as a way to sell or upsell the relationship - it provides context, ideas, and most importantly a way to visualize the capabilities of the integration.

[1]: {% image_buster /assets/img/judo/braze-create-campaign-menu.png %}
[2]: {% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %}
[3]: {% image_buster /assets/img/judo/braze-html-boilerplate.png %}
[4]: {% image_buster /assets/img/judo/braze-campaign-extras-judo-experience.png) %}
