---
nav_title: RudderStack
article_title: RudderStack
description: "This article outlines the partnership between Braze and RudderStack, an open-source customer data infrastructure offering seamless Braze integration for your Android, iOS, and web applications. With RudderStack, you can send your in-app customer event data directly to Braze for contextual analysis."
page_type: partner
search_tag: Partner

---

# RudderStack

> [RudderStack](https://rudderstack.com/) is an open-source customer data infrastructure for collecting and routing customer event data to your preferred data warehouse and dozens of other analytics providers, such as Braze. It is enterprise-ready and offers a robust transformation framework to process your event data on the fly.

The Braze and RudderStack integration offers a native SDK integration for your Android, iOS, and web applications and a server-to-server integration from your backend services.

## Prerequisites

| Requirement | Description |
| --- | --- |
| RudderStack account | A [RudderStack account](https://app.rudderstack.com/) is required to take advantage of this partnership. |
| Configured source | A [source](https://www.rudderstack.com/docs/dashboard-guides/sources/) is essentially the origin of any data sent to RudderStack, such as websites, mobile apps, or backend servers. You are required to configure the source before setting up Braze as a destination in RudderStack. |
| Braze REST API key | A Braze REST API key with `users.track`, `users.identify`, `users.delete`, and `users.alias.new` permissions.<br><br>This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze app key | To get your app key in the Braze dashboard go to **Settings** > **App Settings** > **Identification** and find your app name. Save the associated identifier string.
| Data center | Your data center aligns with your Braze dashboard [instance]({{site.baseurl}}/api/basics/#endpoints).  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

### Step 1: Add a source

To start sending data to Braze, you first need to make sure a source is set up in your RudderStack app. Visit [RudderStack](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#getting-started) to learn how to set up your data source.

### Step 2: Configure destination

Now that your data source is set up, in the RudderStack dashboard, select **ADD DESTINATION** under **Destinations**. From the list of available destinations, select **Braze** and click **Next**.

In the Braze destination, provide the app key, Braze REST API key, data cluster, and native SDK option (device mode only). The native SDK option will use the Braze native SDK to send events if toggled on. 

![]({% image_buster /assets/img/RudderStack/braze_settings.png %}){: style="max-width:70%;margin-bottom:15px;border:none;"}

### Step 3: Choose the type of integration

You can choose to integrate RudderStack's web and native client-side libraries with Braze using one the following approaches:

- [Side-by-side / device mode](#device-mode)**:** RudderStack will send the event data to Braze directly from your client (browser or mobile application).
- [Server-to-server / cloud mode](#cloud-mode)**:** The Braze SDK sends the event data directly to RudderStack, which is then transformed and routed to Braze.
- [Hybrid mode](#hybrid-mode)**:** Use hybrid mode to send iOS and Android auto-generated and user-generated events to Braze using a single connection.

{% alert note %}
Learn more about RudderStack's [connection modes](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/) and the benefits of each.
{% endalert %}

#### Side-by-side integration (device mode) {#device-mode}

With this mode, you can send your events to Braze using the Braze SDK set up on your website or mobile app.

Set up the mappings to the RudderStack SDK for your platform on the Braze GitHub repository, as described under [supported methods](#supported-methods):

- [Android](https://github.com/rudderlabs/rudder-integration-braze-android)
- [iOS](https://github.com/rudderlabs/rudder-integration-braze-ios/tree/master)
- [Swift](https://github.com/rudderlabs/rudder-integration-braze-swift)
- [Web](https://github.com/rudderlabs/rudder-sdk-js/tree/production/src/integrations/Braze)
- [React Native](https://github.com/rudderlabs/rudder-sdk-react-native/tree/develop/libs/rudder-integration-braze-react-native)
- [Flutter](https://github.com/rudderlabs/rudder-sdk-flutter/tree/develop/packages/integrations/rudder_integration_braze_flutter)

To complete the device mode integration, refer to the detailed RudderStack instructions for [adding Braze to your project](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration).

#### Server-to-server integration (cloud mode) {#cloud-mode}

In this mode, the SDK sends the event data directly to the RudderStack server. RudderStack then transforms this data and routes it to the desired destination. This transformation is done in the RudderStack backend using RudderStack's transformer module.

To enable the integration, you will need to map the RudderStack methods to Braze, as described under [supported methods](#supported-methods).

{% alert note %}
RudderStack's server-side SDKs (Java, Python, Node.js, Go, Ruby) support only cloud mode. This is because their server-side SDKs operate in the RudderStack backend and cannot load any Braze-specific SDK.
{% endalert %}

{% alert important %}
The server-to-server integration does not support Braze UI features, such as push notifications or in-app messaging. These features are, however, supported by the device mode integration.
{% endalert %}

#### Hybrid mode {#hybrid-mode}

Use hybrid mode to send all events to Braze from your iOS and Android sources. 

When you choose hybrid mode to send events to Braze, RudderStack:
1. Initializes the Braze SDK.
2. Sends all the user-generated events (identify, track, page, screen, and group) to Braze only through cloud mode and blocks them from being sent via device mode.
3. Sends the auto-generated events (in-app messages, push notifications that require the Braze SDK) via device mode.

To [send events via hybrid mode](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-events-in-hybrid-mode), use the hybrid mode option while connecting your source to the Braze destination. Then, add the Braze integration to your project.

## Step 4: Configure additional settings

After completing the initial setup, configure the following settings to correctly receive your data in Braze:

- **Enable subscription groups in group call**: Enable this setting to send the subscription group status in your group events. For more information, see [Group](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#group).
- **Use Custom Attributes Operation**: Enable this setting if you want to use the [nested custom attributes]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) functionality in Braze to create segments and personalize your messages using a custom attribute object. For more information, see [Send user traits as nested custom attributes](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-user-traits-as-nested-custom-attributes).
- **Track events for anonymous users**: Enable this setting to track anonymous user activity and send this information to Braze.

### Device mode settings

The following settings are applicable only if you’re sending events to Braze via the [device mode](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode):

- **Client-side Events Filtering**: This setting lets you specify which events should be blocked or allowed to flow through to Braze. For more information on this setting, see [Client-side Events Filtering](https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/).
- **Deduplicate Traits**: Enable this setting to deduplicate the user traits in the [`identify`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#identify) call.
- **Show Braze logs**: This setting is applicable only while using the [JavaScript SDK](https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/) as a source. Enable it to show the Braze logs to your users.
- **OneTrust Cookie Categories**: This setting lets you associate the [OneTrust](https://www.rudderstack.com/docs/sources/event-streams/sdks/onetrust/javascript/) cookie consent groups to Braze.

## Supported methods

Braze supports the RudderStack methods identify, track, screen, page, group, and alias.

{% tabs %}
{% tab Identify %}

The RudderStack [`identify` method](https://rudderstack.com/docs/destinations/marketing/braze/#identify) associates users with their actions. RudderStack captures a unique user ID and optional traits associated with that user, such as name, email, IP address, etc.

**Delta management for identify calls**<br>
If you send events to Braze via device mode, you can save costs by deduplicating your `identify` calls. To do so, enable the Deduplicate Traits dashboard setting. RudderStack then sends only the changed or modified attributes (traits) to Braze.

**Deleting a user**<br>
You can delete a user in Braze using the [Suppression with Delete regulation](https://www.rudderstack.com/docs/api/data-regulation-api/#adding-a-suppression-with-delete-regulation) of the RudderStack [Data Regulation API](https://www.rudderstack.com/docs/api/data-regulation-api/).

{% endtab %}
{% tab Track %}

RudderStack's [`track` method](https://rudderstack.com/docs/destinations/marketing/braze/#track) captures all the user activities and the properties associated with those activities.

**Order completed**<br>
On using the [RudderStack eCommerce API](https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/) to call the track method for an event with the name `Order Completed`, RudderStack sends the products listed in that event to Braze as [`purchases`]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).

{% endtab %}
{% tab Screen %}

RudderStack's [`screen` method](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#screen) allows you to record your users’ mobile screen views with any additional information about the viewed screen.

{% endtab %}
{% tab Page %}

RudderStack's [`page` method](https://rudderstack.com/docs/destinations/marketing/braze/#page) lets you record your website's page views. It also captures any other relevant information about that page.

{% endtab %}
{% tab Group %}

RudderStack's [`group` method](https://rudderstack.com/docs/destinations/marketing/braze/#group) allows you to associate a user with a group.

**Subscription group status**<br>
To update the subscription group status, enable the "Enable subscription groups in group call" setting in the RudderStack dashboard and send the subscription group status in the group call.

{% endtab %}
{% tab Alias %}

RudderStack's [`alias` method](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#alias) allows you to merge different identities of a known user. Note that RudderStack supports the alias call for Braze only in cloud mode.

{% endtab %}
{% endtabs %}

## Send user traits as nested custom attributes

You can send the user traits to Braze as nested custom attributes and perform add, update, and remove operations on them. To do so, enable the "Use Custom Attributes Operation dashboard" setting in RudderStack while configuring the Braze destination. This feature is only available in cloud mode.

You can send the user traits as nested custom attributes in your `identify` events in the following format:
```javascript
rudderanalytics.identify("1hKOmRA4GRlm", {
  "cars": {
    "add": [{
      "age": 27,
      "id": 1,
      "name": "Alex Keener"
    }],
    "update": [{
        "age": 30,
        "id": 2,
        "identifier": "id",
        "name": "Rowan"
      },
      {
        "age": 27,
        "id": 1,
        "identifier": "id",
        "name": "Mike"
      }
    ]
  },
  "country": "USA",
  "email": "alex@example.com",
  "firstName": "Alex",
  "gender": "M",
  "pets": [{
      "breed": "beagle",
      "id": 1,
      "name": "Scooby",
      "type": "dog"
    },
    {
      "breed": "calico",
      "id": 2,
      "name": "Garfield",
      "type": "cat"
    }
  ]
})
```

To send the user traits as custom user attributes via the `track`, `page`, or `screen` calls, pass `traits` as a contextual field in the event:
```javascript
rudderanalytics.track("Product Viewed", {
    revenue: 8.99,
    currency: "USD",
 },{
  "traits": {
    "cars": {
      "add": [{
        "age": 27,
        "id": 1,
        "name": "Alex Keener"
      }],
      "update": [{
          "age": 30,
          "id": 2,
          "identifier": "id",
          "name": "Mike"
        },
        {
          "age": 27,
          "id": 1,
          "identifier": "id",
          "name": "Rowan"
        }
      ]
    },
    "city": "Disney",
    "country": "USA",
    "email": "alexa@example.com",
    "firstName": "Alexa",
    "gender": "woman",
    "pets": [{
        "breed": "beagle",
        "id": 1,
        "name": "Scooby",
        "type": "dog"
      },
      {
        "breed": "calico",
        "id": 2,
        "name": "Garfield",
        "type": "cat"
      }
    ]
  }
});
```

{% alert note %}
For the update and remove operations, `identifier` is a required key. If add, update, or remove operations are not present in the nested array, RudderStack uses the create operation to create the properties by default. Refer to [Array of objects]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) for more information on sending nested custom attributes.
{% endalert %}

