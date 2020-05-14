---
nav_title: Factual
alias: /partners/factual/

description: "This article outlines the partnership between Braze and Factual, a location data company powering innovation in product development, mobile marketing, and real-world analytics."
page_type: partner

---

# Factual Integration

> [Factual](https://www.factual.com/) is a location data company powering innovation in product development, mobile marketing, and real-world analytics.

Leverage Factual to better understand and uplevel mobile experiences through location data. Obtain a comprehensive picture of your customers' online interests and behaviors with Factual's [Engine SDK](https://www.factual.com/products/engine/) and gain greater insight on end-user journeys and places visited. With this integration, available for both iOS and Android, developers are able to implement location intelligence and build personalized user engagement. This can by made possible by allowing Braze to receive custom events when the user is at a known Factual place or when an engine circumstance with the actionId ```push-to-braze``` is met.

# Pre-Requisites
{% tabs %}
{% tab iOS %}
| Requirement   |Origin| Description |
| --------------|------|------------- |
| Engine SDK    |[Factual Engine SDK](http://developer.factual.com/engine/ios/)| In order to successfully integrate Factual's Engine SDK with Braze, ensure the Engine client has been configured properly and starts successfully. This requires confirming an API key has been acquired and the Engine SDK has been properly imported into the project. |
|Appboy Client|[Braze SDK iOS Setup]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/) | Also ensure the Appboy client is properly configured. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% endtab %}
{% tab Android %}
| Requirement   |Origin | Description |
| --------------|-------|------------- |
| Engine SDK    |[Factual Engine SDK](http://developer.factual.com/engine/android/) | In order to successfully integrate Factual's Engine SDK with Braze, ensure the Engine client has been configured properly and starts successfully. This requires confirming an api key has been acquired and the Engine SDK has been properly imported into the project. |
| Appboy Client|[Braze SDK Android Setup]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/?redirected=true#step-2-configure-the-braze-sdk-in-appboyxml) | Also ensure the Appboy client is properly configured. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% endtab %}
{% endtabs %}

# Events
{% raw %}

The following are custom user events that can be sent to the Braze SDK from Factual's Engine and are available for both iOS and Android integrations:

## User Journey Events

***Name***: ```engine_user_journey```

***Description***: User has visited a known Factual location.

***Properties***:
```json
{
  "name": (string)
  "factual_id": (string)
  "latitude": (double)
  "longitude": (double)
  "user_latitude": (double)
  "user_longitude": (double)
  "place_categories": (string) (place_categories is a comma-separated list of factual category IDs)
}
```
## Circumstance Met Events
***Name***: ```engine_circumstance_[CIRCUMSTANCE_NAME]```

***Description***: A circumstance with actionId ```push-to-braze``` has been met.

***Properties***:
```json
{
  "incidence_id": (string)
  "user_latitude": (double)
  "user_longitude": (double)
}
```

## Circumstance Met At Place
***Name***: ```engine_circumstance_place_at_[CIRCUMSTANCE_NAME]```

***Properties***:
```json
{
  "incidence_id": (string)
  "name": (string)
  "factual_id": (string)
  "latitude": (double)
  "longitude": (double)
  "user_latitude": (double)
  "user_longitude": (double)
  "place_categories": (string) place_categories is a comma-separated list of factual category IDs
}
```

{% endraw %}

{% alert important %}
This event returns location and additional information on a visited place based on where this circumstance was met. In order to simplify usage within the Braze dashboard, since it is possible for multiple places to simultaneously trigger this event, all of the places are not included within a single event's properties. As an alternative, a slightly different custom event will be sent with each location that triggers the original event.

Use ```incidence_id``` to map the different Braze circumstance events to a single instance of an Engine circumstance met.
{% endalert %}

# Using This Integration

## Using a Circumstance in the Braze Dashboard

### Step 1: Create a Circumstance in the Garage Web UI

In order to use this integration we first have to set up the circumstance for Engine to trigger our action. This can be done through Engine's [Garage Web UI](https://engine.factual.com/garage) and Factual's [developer documentation](http://developer.factual.com/engine/circumstances/) is highly detailed in regards to a circumstance's usage and creation.

The important step to remember in creating a new circumstance is setting our action to custom by selecting the **Add custom action** button in the Select an action drop down.

![Add Action to Circumstances in Engine]({% image_buster /assets/img_archive/factual_circumstance_add_action.png %})

From there, we will need to specify an ID name for our action as shown below.
![Circumstance Custom Action ID Name]({% image_buster /assets/img_archive/factual_circumstance_action_idname.png %})

Once it is completed, our updates will happen **over the air to any Engine live instance matching your ENGINE/GARAGE API key**. Copy your ENGINE/GARAGE API as a reference then click on the **Next** button and lastly the **Push Changes** button found on the next screen. Our updates will occur typically in 30 minutes, but this time can also be set programmatically to whatever is needed by your teams.

{% alert important %}
After setting our conditions, be sure to note the ID name you created for your action. This will be found in the Braze Dashboard later when you select it as your delivery trigger as an action-based event.
{% endalert %}

### Step 2: Compose Your Message in Braze

{% raw %}
After logging into your Braze dashboard and going to __Campaigns__, then __Create Campaign__, you can follow the standard Braze flow to create a new message. **To add location names dynamically** use the following snippet in either the title or body of your message: ```{{event_properties.${name}}}```. Depending on your use case, it's recommended to use this snippet in the body of your message as some location have long names and would be truncated in a message title.
{% endraw %}

![Braze Compose New Message]({% image_buster /assets/img_archive/braze_factual_compose.png %})

### Step 3: Delivery
From within the Delivery tab, select Action-Based Delivery, then in the Perform Custom Event drop down menu, select the custom event you created in the first step.

Every time a user or device meets the criteria of the custom event, like being **NEAR** (200m) a designated location, Braze will trigger the appropriate action, which in this example is sending a push notification.
![Braze Select Circumstance]({% image_buster /assets/img_archive/braze_factual_delivery.png %})

### Step 4: Testing Your Implementation
To test in-app and push notifications via command-line, you can send a single notification through the terminal via CURL and the Messaging API. You will need to replace the following fields with the correct values for your test case:

| Field| Description|
|---|---|
|YOUR_API_KEY | Available on the Developer Console page. |
|YOUR_EXTERNAL_USER_ID | Available on the User Profile Search Page. See documentation on assigning user IDs.|
|YOUR_KEY1 | Optional. |
|YOUR_VALUE1 | Optional. |


Curl Command:
{% raw %}
```
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {{YOUR_API_KEY}}" -d "{\"external_user_ids\":[\"YOUR_EXTERNAL_USER_ID\"],\"messages\":{\"apple_push\":{\"alert\":\"Test push\",\"extra\":{\"YOUR_KEY1\":\"YOUR_VALUE1\"}}}}" https://rest.iad-01.braze.com/messages/send
```
{% endraw %}

### Message Output Example
When a user/device meets the `engine_circumstance_braze_near` (or other specified circumstance) they will receive the below push notification.

![Braze Factual Engine Example]({% image_buster /assets/img_archive/braze_factual_message_example.png %})

## Installation

{% tabs %}
{% tab iOS %}
### iOS Installation
#### Installation via CocoaPods
{% raw %}
```
source 'https://github.com/Factual/cocoapods.git'
source 'https://github.com/CocoaPods/Specs.git'

platform :ios, '10.3'

target 'YourApp' do
  pod 'BrazeEngine'
end
```
{% endraw %}

### Manual Installation
Download the library from [Bintray](https://factual.bintray.com/files/) and add it to your Xcode project.

You must have the Engine SDK already added to your Xcode project in order to use the library properly.

{% endtab %}

{% tab Android %}
### Android Installation
#### Project Artifacts
For Android, project artifacts are available within Factual's Bintray Maven repository and can be implemented as shown below.

{% raw %}

```
// repository for the Factual artifacts
repositories {
  maven {
    url "https://factual.bintray.com/maven"
  }
}
```
```
dependencies {
  compile 'com.factual.engine:braze-engine:1.1.0'
}
```
{% endraw %}

{% endtab %}
{% endtabs %}

# Usage

{% tabs %}

{% tab iOS %}

On iOS, developers can start tracking Factual's Engine UserJourney and Circumstance events after receiving the engine started callback within FactualEngineDelegate.

{% raw %}

```
-(void)engineDidStartWithInstance:(FactualEngine *)engine {
  //Track both user journey and circumstance events
  [BrazeEngine trackUserJourneyAndCircumstancesWithEngine:engine]
}
```
```
-(void)engineDidStartWithInstance:(FactualEngine *)engine {
  //track only circumstance events
  [BrazeEngine trackCircumstancesWithEngine:engine withUserJourneyEnabled:false]
}
```
{% endraw %}

{% endtab%}

{% tab Android %}

{% raw %}

```
//Whether user journey events should be sent to Braze
boolean enableUserJourney = true;

/*
Max number of "circumstance_met_at_place" that should be sent to user in case
where multiple places simultaneously trigger the same circumstance. Default is
set to 10.
*/
numMaxEventsPerCircumstance = 3;

BrazeEngineIntegration.initializeBrazeEngineIntegration(androidApplicationContext, enableUserJourney, numMaxEventsPerCircumstance);
```
{% endraw %}

{% endtab %}
{% endtabs %}

## Demo App
A demo app implementing the iOS integration can be found within Factual's Engine Demo repository [here](https://github.com/Factual/braze-factual-engine-ios/tree/master/demo), while a demo app implementing the Android integration can be found within Factual's Demo repository located [here](https://github.com/Factual/braze-factual-engine-android/tree/master/demo).
