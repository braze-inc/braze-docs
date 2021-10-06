---
nav_title: Judo
page_order: 1
description: "Use the Judo no-code server-driven UI platform with the Braze marketing automation platform"
alias: /partners/judo/
page_type: partner
hidden: true
---

# Judo

[Judo](https://judo.app) is a server-driven UI platform that empowers publishers
to efficiently deliver rich, engaging in-app user experiences without app
updates.

Developers integrating Braze marketing automation with Judo experiences will
find elevated value for their joint customers. Superior targeting,
personalization and campaign orchestration from Braze are linked to bespoke
experiences from Judo. Instead of a simple templated landing page experience a
Braze campaign may incorporate content that comprises multiple screens, modals,
video, custom fonts and support settings such as dark mode and accessibility
built without code and deployed without app updates. Data from Braze may be used
to support personalized content in a Judo experience. User events and data from
the experience can feed back into Braze for attribution and targeting.

## Requirements or Prerequisites

First, you will need to have already integrated both Braze and Judo into your
apps.


| Requirement | Origin | Access | Description |
|---|---|---|---|
| Judo Account | Judo | [Judo](https://www.judo.app/) | You'll need a Judo account in order to host Experiences for launch from Braze. |
| Judo SDK | Judo | [Judo iOS SDK](https://github.com/judoapp/judo-ios/) and [Judo Android SDK](https://github.com/judoapp/judo-android) | You'll need the Judo SDKs integrated into your iOS and/or Android apps. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Side-by-Side SDK Integration

Judo offers additional libraries that automate some of the effort necessary to
integrate the Judo and Braze SDKs, side-by-side, in your mobile app(s). There
are two steps, installing the SDK (which automatically enables event tracking),
and setting up the In-App-Messaging (IAM) integration.

### Step 1: Install the Judo-Braze Integration Library

Install and set up the Judo-Braze integration library into your apps.

[iOS installation
instructions](https://github.com/judoapp/judo-braze-ios/wiki#installation) and
[Android installation
instructions](https://github.com/judoapp/judo-braze-android/wiki#installation).

### Step 2: Configure In-App Messaging

This step will involve creating custom `ABKInAppMessageControllerDelegate` and
`IInAppMessageManagerListener` implementations for iOS and Android respectively.

See the IAM Setup documentation bundled for each of the integration libraries:
[iOS In-App Messaging
Setup](https://github.com/judoapp/judo-braze-ios/wiki#in-app-messaging-setup)
and [Android In-App Messaging
Setup](https://github.com/judoapp/judo-braze-android/wiki#in-app-messaging-setup).

## Using this Integration

Once you have finished the app-side integration, you can test it by actually
running a test Braze IAM campaign for a Judo Experience to verify that it works
to your satisfaction.

Create a Braze IAM Campaign in the Braze of the HTML Custom View type. Advance
through each the below steps by clicking the "Forward" button in the bar at the
very bottom of the display.

### Step 1: Creating an IAM Campaign

![Braze Create Campaign Menu][1]

### Step 2: Selecting "Custom Code" Message Type

While any of the Message Types should work, consider using the Custom Code type.
You'll then need to populate the content of the Message with the minimum that
Braze requires; note that this will not be shown on to the user, but Braze
expects to use its own UI and so requires us to provide some content.

![Braze Custom Code Campaign][2]

With the Custom Code type, use the following minimal HTML snippet to satisfy the
form validation: `<a href="appboy://close">X</a>`.

Note that this will not be displayed in production on your device, since this
In-App Message will be intercepted and replaced with a Judo experience.

![Braze HTML Snippet][3]

### Step 3: Setting an Extra Field for Judo

Then, set a [custom extra key-value
pair](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/key_value_pairs/)
on the Campaign with a key of `judo-experience`. Provide the URL of the Judo
Experience you'd like to show here. This is what the Judo-Braze integration
library will detect in the handler and use to inject your Judo Experience in
lieu of the standard Braze IAM UI.

![Braze Campaign Extras Configuration][4]

### Step 4: Finishing the Campaign

You will need to complete the campaign, namely setting up a trigger for the
Campaign and selecting users via Segments in the Delivery and Target User
sections respectively. This is out of scope of this document, so please see the
[Creating an In-App Message
Guide](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/create/).

## Use Cases

The Judo no-code, server-driven UI platform can support delivery of new custom
user experiences to an application without any app updates. There are numerous
use cases when used in conjunction with Braze’s marketing automation.

**On-Boarding**: App publishers using Judo build and deploy rich, native
on-boarding experiences. These experiences can now be one element in a
personalized cross-channel onboarding journey coordinated via Braze. Experiences
may be personalized and may be quickly iterated on without any app updates to
test the effectiveness of different in-app flows.

**Conversion**: App publishers can use data from Braze to create a personalized
rich in app experience to drive in app purchases, paid subscriptions or
contextual merchandising using integration hooks in Judo. Access to these
experiences may be triggered via engagement marketing campaigns created in
Braze.

**Event-Driven Content**: A primary use for Judo in sports and entertainment is
building rich experiences to preview, promote and recap events. This capability
has broad application in other verticals for seasonal and news-driven content.
Linking messaging to promote or highlight events in a timely manner to rich in
app experiences empowers publishers to drive engagement by being contextually
relevant.

[1]: {% image_buster /assets/img/judo/braze-create-campaign-menu.png %}
[2]: {% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %}
[3]: {% image_buster /assets/img/judo/braze-html-boilerplate.png %}
[4]: {% image_buster /assets/img/judo/braze-campaign-extras-judo-experience.png %}
