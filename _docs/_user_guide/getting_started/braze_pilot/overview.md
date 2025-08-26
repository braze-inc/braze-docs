---
nav_title: Overview
article_title: Braze Pilot Overview
page_order: 1
page_type: reference
description: "This reference article briefly covers the integration steps required from your engineers or developers."
---

# Braze Pilot overview

> This page introduces the core concepts you’ll need to know when working with Braze Pilot.

Braze Pilot is a mobile app that is designed to connect seamlessly with your Braze dashboard. This empowers you to launch campaigns and Canvases to the app, bringing Braze messages to life on your own phone. Braze Pilot includes a library of app simulations for fictional brands representing different industries, allowing you to experience how your messaging might look from your customers’ perspective.

## Pilot app simulations

The core of Braze Pilot is its library of app simulations. Each app is a realistic simulation of an industry-specific fictional brand, instrumented to log a rich assortment of events and attributes that create endless opportunities for powering common Braze use cases.

### Steppington

Steppington is a fitness app with workouts, exercise goals, and a Steppington+ premium service. It offers several places to demonstrate [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards), a section that can be revealed with [feature flags]({{site.baseurl}}/developer_guide/feature_flags), and a robust library of custom event logging that make it possible to illustrate many customer journeys for this industry.

![The home page for Steppington with icons for marathon training, yoga, cycling, and weights.]({% image_buster /assets/img/braze_pilot/steppington_app.png %}){:style="max-width:50%"}

### PantsLabyrinth

PantsLabyrinth is an eCommerce app that sells (you guessed it) pants! The PantsLabyrinth app includes full shopping cart checkout experience, an optional wishlist feature that can be enabled with a feature flag, and many opportunities for sly jokes with friends from the UK.

![A product page for PantsLabyrinth with options to add jeans to cart.]({% image_buster /assets/img/braze_pilot/pantslabyrinth_app.png %}){:style="max-width:50%"}

### MovieCanon 

MovieCanon is a streaming service perfectly designed to illustrate common Braze use cases around content engagement. 

![The MovieCanon app with different thrillers to watch.]({% image_buster /assets/img/braze_pilot/moviecanon_app.png %}){:style="max-width:50%"}

## How Pilot connects with your Braze dashboard

The Braze SDK is a code package that collects data from your users once it's integrated with your app or website. When you connect Pilot to your dashboard, you initialize this connection between the Pilot app on your phone and the Braze SDK, and establish a unique connection with your Braze instance by giving Pilot your API key identifier for your dashboard.

![The first step of setting up Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

After Pilot connects to your Braze dashboard, the Braze SDK functions in the app just as it will once you integrate the SDK with your own app or website. This means that Braze will:

- Store data on your user activity in Pilot, including custom data specific to the fictional brands in the app.
- Automatically collect session data, device info, and push tokens.
- Power push notifications, in-app messages, and Content Card messaging channels that require SDK integration to function.

For more on the Braze SDK, check out [Integration]({{site.baseurl}}/user_guide/getting_started/integration).

![The Braze customer engagement stack, which includes integrations, APIs, SDKs for data ingestion, classification, orchestration, personalization, and action with messaging channels for an interactive feedback loop with your customers.]({% image_buster /assets/img/braze_pilot/braze_sdk_diagram.png %}){:style="max-width:70%"}

## User profiles in Braze

Every piece of data sent to Braze is stored in a user profile dedicated to a particular user of your app or website. Once you connect Pilot with your Braze dashboard, Braze will start logging data about you as the user of Pilot. There are two types of users that could be created for you through this connection: anonymous and identified.

### Anonymous 

This connection status represents the experience of a guest of your app or website who hasn’t logged in yet. If you initialize Pilot as an anonymous user, Braze creates an [anonymous user profile]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users) for you and logs data about your activity there. Anonymous users can still be targeted with campaigns, but you won’t be able to look up their user profile directly in your Braze dashboard.

### Identified

This connection status means Braze recognizes your user profile through a unique identifier assigned to you, known as an external identifier. You can search for this external identifier in the **User Search** page of your dashboard to locate your user profile, which will store all user attributes and events logged from Pilot based on your activity in the app.

![An example of a Braze user profile for user "torchie-208117".]({% image_buster /assets/img/braze_pilot/user_profile.png %})

### Connection type

To check what type of connection you have, you can check the connection status at the top right of your screen.

{% tabs %}
{% tab Anonymous user  %}

**Anonymous** indicates you're logging data as an anonymous user.

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_anonymous.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Identified user %}

If you're logging data as an identified user, a user icon will display next to your external ID.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_identified_user.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Not connected %}

**Not connected** indicates you haven't yet initialized the Braze SDK connection with Pilot.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_not_connected.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Campaigns and Canvases

Campaigns and Canvases are how you send messages to your users. 

- Campaigns are best for single messages sent to a specific audience segment across various channels. 
- Canvases are advanced campaign workflows that allow you to automate and orchestrate personalized customer journeys across multiple channels. Within a Canvas, you can set up branching logic, delays, decision points, and conversion events to guide customers through a series of interactions. Canvases help ensure consistent and seamless communication across different touch points, increasing the chances of customer engagement and conversion.

## Supported messaging channels

Braze Pilot currently supports [in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about), which appear in your app, delivering timely messaging while the user is actively engaging.

![An in-app message in the MovieCanon app "Enjoying MovieCanon? Refer your friends!" with an option to enter your email address to send a referral.]({% image_buster /assets/img/braze_pilot/moviecanon_iam.png %}){:style="max-width:40%"}