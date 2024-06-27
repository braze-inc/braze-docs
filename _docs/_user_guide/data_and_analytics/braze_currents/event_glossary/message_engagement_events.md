---
nav_title: Message Engagement Events
layout: message_engagement_events_glossary
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "This glossary lists the various Message Engagement Events that Braze can track and send to chosen Data Warehouses using Currents."
tool: Currents
search_rank: 6
---

Contact your account manager or open a [support ticket]({{site.baseurl}}/braze_support/) if you need access to additional event entitlements. If you can't find what you need in this article, check out our [Customer Behavior Events Library]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/) or our [Currents sample data examples](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explanation of message engagement event structure and platform values %}

### Event structure

This event breakdown shows what type of information is generally included in a message engagement event. With a solid understanding of its components, your developers and business intelligence strategy team can use the incoming Currents event data to make data-driven reports, charts and take advantage of other valuable data metrics.

![Breakdown of a message engagement event showing an email unsubscribe event with the listed properties grouped by user-specific properties, campaign or Canvas tracking properties, and event-specific properties]({% image_buster /assets/img/message_engagement_event.png %})

Message engagement events are comprised of **user-specific** properties, **campaign/canvas tracking** properties, and **event-specific** properties.

### Platform values

Certain events return a `platform` value that specifies the platform of the user's device.
<br>The following table details the possible returned values:

| User device | Platform value |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2}

{% enddetails %}

{% alert important %}
Storage schemas apply to the flat file event data we send to Data Warehouse partners (Google Cloud Storage, Amazon S3, and Microsoft Azure Blob Storage). Some event and destination combinations listed here are not yet generally available. For information on which events are supported by various partners, refer to our list of [available partners]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/) and check their respective pages.<br><br>Additionally, note that Currents will drop events with excessively large payloads of greater than 900&nbsp;KB.
{% endalert %}

{% alert note %}
Human-readable names for objects related to Canvas Flow are coming soon to Currents. In the meantime, the IDs can be used for grouping, and translated to human-readable names via the [Export Canvas details endpoint]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/).
{% endalert %}

{% api %}

## WhatsApp read events

{% apitags %}
WhatsApp, Read
{% endapitags %}

This event occurs when an WhatsApp message is read by the end user.



{% endapi %}
{% api %}

## WhatsApp delivery events

{% apitags %}
WhatsApp, Delivery
{% endapitags %}

This event occurs when an WhatsApp message sent made it successfully to the end-users device.

{% tabs %}
{% tab Braze Standard REST %}
```json
// WhatsApp Delivery: users.messages.whatsapp.Delivery

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, long) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Delivery: users.messages.whatsapp.Delivery

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, long) Unix timestamp at which the event happened",
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// WhatsApp Delivery: users.messages.whatsapp.Delivery

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Delivery: users.messages.whatsapp.Delivery

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) Unix timestamp at which the event happened",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// WhatsApp Delivery: users.messages.whatsapp.Delivery

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Delivery: users.messages.whatsapp.Delivery

{
  "context" : {
    "traits" : {
      "phone" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to"
  },
  "timestamp" : "(required, long) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## WhatsApp failure events

{% apitags %}
WhatsApp, Failure
{% endapitags %}

This event occurs when WhatsApp cannot deliver the message to the user. A hard bounce signifies a permanent deliverability failure.

{% tabs %}
{% tab Braze Standard REST %}
```json
// WhatsApp Failure: users.messages.whatsapp.Failure

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "provider_error_code" : "(required, string) Error code from WhatsApp",
    "provider_error_title" : "(required, string) Description of error from WhatsApp",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, long) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Failure: users.messages.whatsapp.Failure

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, long) Unix timestamp at which the event happened",
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "provider_error_code" : "(required, string) Error code from WhatsApp",
    "provider_error_title" : "(required, string) Description of error from WhatsApp",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// WhatsApp Failure: users.messages.whatsapp.Failure

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "provider_error_code" : "(required, string) Error code from WhatsApp",
  "provider_error_title" : "(required, string) Description of error from WhatsApp",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Failure: users.messages.whatsapp.Failure

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) Unix timestamp at which the event happened",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "provider_error_code" : "(required, string) Error code from WhatsApp",
          "provider_error_title" : "(required, string) Description of error from WhatsApp"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// WhatsApp Failure: users.messages.whatsapp.Failure

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "provider_error_code" : "(required, string) Error code from WhatsApp",
    "provider_error_title" : "(required, string) Description of error from WhatsApp"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Failure: users.messages.whatsapp.Failure

{
  "context" : {
    "traits" : {
      "phone" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "provider_error_code" : "(required, string) Error code from WhatsApp",
    "provider_error_title" : "(required, string) Description of error from WhatsApp"
  },
  "timestamp" : "(required, long) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## WhatsApp send events

{% apitags %}
WhatsApp, Sends
{% endapitags %}

This event occurs when a send request was successfully communicated between Braze and WhatsApp. Though, this does not mean the message was received by the end user.

{% tabs %}
{% tab Braze Standard REST %}
```json
// WhatsApp Send: users.messages.whatsapp.Send

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, long) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Send: users.messages.whatsapp.Send

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, long) Unix timestamp at which the event happened",
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// WhatsApp Send: users.messages.whatsapp.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Send: users.messages.whatsapp.Send

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) Unix timestamp at which the event happened",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// WhatsApp Send: users.messages.whatsapp.Send

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Send: users.messages.whatsapp.Send

{
  "context" : {
    "traits" : {
      "phone" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering"
  },
  "timestamp" : "(required, long) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## WhatsApp abort message events

{% apitags %}
WhatsApp, Abort
{% endapitags %}

This event occurs if a WhatsApp message was aborted based on Liquid aborts, Quiet Hours, etc.

{% tabs %}
{% tab Braze Standard REST %}
```json
// WhatsApp Abort: users.messages.whatsapp.Abort

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, long) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Abort: users.messages.whatsapp.Abort

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, long) Unix timestamp at which the event happened",
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// WhatsApp Abort: users.messages.whatsapp.Abort

{
  "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Abort: users.messages.whatsapp.Abort

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) Unix timestamp at which the event happened",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
          "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// WhatsApp Abort: users.messages.whatsapp.Abort

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Abort: users.messages.whatsapp.Abort

{
  "context" : {
    "traits" : {
      "phone" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)"
  },
  "timestamp" : "(required, long) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}
{% api %}

## WhatsApp inbound received events

{% apitags %}
WhatsApp, InboundReceived
{% endapitags %}

This event occurs when one of your users sends a WhatsApp message to a phone number in one of your Braze WhatsApp subscription groups.

{% tabs %}
{% tab Braze Standard REST %}
```json
// WhatsApp Inbound Received: users.messages.whatsapp.InboundReceive

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "user_phone_number" : "(required, string) The user's phone number from which the message was received",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "message_body" : "(optional, string) Typed response from the user",
    "quick_reply_text" : "(optional, string) Text of button pressed by the user",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, long) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Inbound Received: users.messages.whatsapp.InboundReceive

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, long) Unix timestamp at which the event happened",
    "user_phone_number" : "(required, string) The user's phone number from which the message was received",
    "distinct_id" : "(required, string) External ID of the user",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "message_body" : "(optional, string) Typed response from the user",
    "quick_reply_text" : "(optional, string) Text of button pressed by the user",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// WhatsApp Inbound Received: users.messages.whatsapp.InboundReceive

{
  "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
  "media_urls" : "(optional, array of string) Media URLs from the user",
  "message_body" : "(optional, string) Typed response from the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "quick_reply_text" : "(optional, string) Text of button pressed by the user",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(optional, string) BSON ID of the user who performed this event",
  "user_phone_number" : "(required, string) The user's phone number from which the message was received"
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Inbound Received: users.messages.whatsapp.InboundReceive

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) Unix timestamp at which the event happened",
        "custom_attributes" : {
          "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "message_body" : "(optional, string) Typed response from the user",
          "quick_reply_text" : "(optional, string) Text of button pressed by the user",
          "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None)."
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// WhatsApp Inbound Received: users.messages.whatsapp.InboundReceive

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "user_phone_number" : "(required, string) The user's phone number from which the message was received",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "message_body" : "(optional, string) Typed response from the user",
    "quick_reply_text" : "(optional, string) Text of button pressed by the user",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None)."
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Inbound Received: users.messages.whatsapp.InboundReceive

{
  "context" : {
    "traits" : {
      "phone" : "(required, string) The user's phone number from which the message was received"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "message_body" : "(optional, string) Typed response from the user",
    "quick_reply_text" : "(optional, string) Text of button pressed by the user",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None)."
  },
  "timestamp" : "(required, long) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## Content Card abort message events

{% apitags %}
Abort, Content Cards
{% endapitags %}

This event occurs if a Content Card message was aborted based on Liquid aborts, Quiet Hours, etc.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Content Card Abort: users.messages.contentcard.Abort

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Abort: users.messages.contentcard.Abort

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Content Card Abort: users.messages.contentcard.Abort

{
  "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Abort: users.messages.contentcard.Abort

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
          "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Content Card Abort: users.messages.contentcard.Abort

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Content Card Abort: users.messages.contentcard.Abort

{
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## Email abort message events

{% apitags %}
Abort, Email
{% endapitags %}

This event occurs if an email message was aborted based on Liquid aborts, Quiet Hours, etc.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Email Abort: users.messages.email.Abort

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Abort: users.messages.email.Abort

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Email Abort: users.messages.email.Abort

{
  "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) Email address of the user",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Abort: users.messages.email.Abort

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
          "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user",
    "email" : "(required, string) Email address of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Email Abort: users.messages.email.Abort

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Abort: users.messages.email.Abort

{
  "context" : {
    "traits" : {
      "email" : "(required, string) Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## Push notification abort events

{% apitags %}
Abort, Push
{% endapitags %}

This event occurs if a push notification message was aborted based on Liquid aborts, Quiet Hours, etc.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Push Notification Abort: users.messages.pushnotification.Abort

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Abort: users.messages.pushnotification.Abort

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Push Notification Abort: users.messages.pushnotification.Abort

{
  "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "platform" : "(required, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Push Notification Abort: users.messages.pushnotification.Abort

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
          "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Push Notification Abort: users.messages.pushnotification.Abort

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Abort: users.messages.pushnotification.Abort

{
  "context" : {
    "traits" : { },
    "device" : {
      "type" : "(required, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(required, string) Platform of the device",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## SMS abort message events

{% apitags %}
Abort, SMS
{% endapitags %}

This event occurs if an SMS message was aborted based on Liquid aborts, Quiet Hours, etc.

{% tabs %}
{% tab Braze Standard REST %}
```json
// SMS Abort: users.messages.sms.Abort

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Abort: users.messages.sms.Abort

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// SMS Abort: users.messages.sms.Abort

{
  "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Abort: users.messages.sms.Abort

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
          "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// SMS Abort: users.messages.sms.Abort

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Abort: users.messages.sms.Abort

{
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## Webhook abort message events

{% apitags %}
Abort, Webhooks
{% endapitags %}

This event occurs if a webhook message was aborted based on Liquid aborts or Quiet Hours.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Webhook Abort: users.messages.webhook.Abort

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Webhook Abort: users.messages.webhook.Abort

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Webhook Abort: users.messages.webhook.Abort

{
  "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Webhook Abort: users.messages.webhook.Abort

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
          "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Webhook Abort: users.messages.webhook.Abort

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Webhook Abort: users.messages.webhook.Abort

{
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "abort_type" : "(optional, string) Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
    "abort_log" : "(optional, string) Log message describing abort details (up to 128 chars)"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## Canvas exit performed event events

{% apitags %}
Exit, Canvas
{% endapitags %}

This event occurs when a user has exited a Canvas by performing an event.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Exit Perform Event: users.canvas.exit.PerformedEvent

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Exit Perform Event: users.canvas.exit.PerformedEvent

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Exit Perform Event: users.canvas.exit.PerformedEvent

{
  "app_group_api_id" : "(optional, string) [DEPRECATED]",
  "app_group_id" : "(required, string) API ID of the app group this user belongs to",
  "canvas_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_id" : "(required, string) API ID of the Canvas this event belongs to",
  "canvas_step_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_variation_id" : "(required, string) API ID of the Canvas variation this event belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Exit Perform Event: users.canvas.exit.PerformedEvent

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Exit Perform Event: users.canvas.exit.PerformedEvent

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Exit Perform Event: users.canvas.exit.PerformedEvent

{
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## Canvas exit matched audience events

{% apitags %}
Exit, Canvas
{% endapitags %}

This event occurs when a user has exited a Canvas by matching an audience.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Exit Match Audience: users.canvas.exit.MatchedAudience

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Exit Match Audience: users.canvas.exit.MatchedAudience

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Exit Match Audience: users.canvas.exit.MatchedAudience

{
  "app_group_api_id" : "(optional, string) [DEPRECATED]",
  "app_group_id" : "(required, string) API ID of the app group this user belongs to",
  "canvas_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_id" : "(required, string) API ID of the Canvas this event belongs to",
  "canvas_step_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_variation_id" : "(required, string) API ID of the Canvas variation this event belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Exit Match Audience: users.canvas.exit.MatchedAudience

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Exit Match Audience: users.canvas.exit.MatchedAudience

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Exit Match Audience: users.canvas.exit.MatchedAudience

{
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Experiment split entry events

{% apitags %}
Experiment Step, Canvas
{% endapitags %}

This event occurs when a user enters a Canvas experiment step path.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Experiment Split Entry: users.canvas.experimentstep.SplitEntry

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Experiment Split Entry: users.canvas.experimentstep.SplitEntry

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Experiment Split Entry: users.canvas.experimentstep.SplitEntry

{
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
  "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Experiment Split Entry: users.canvas.experimentstep.SplitEntry

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_attributes" : {
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
          "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
          "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Experiment Split Entry: users.canvas.experimentstep.SplitEntry

{
  "event_properties" : {
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Experiment Split Entry: users.canvas.experimentstep.SplitEntry

{
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## Experiment conversion events

{% apitags %}
Experiment Step, Canvas
{% endapitags %}

This event occurs when a user convert for a Canvas experiment step.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Experiment Step Conversion: users.canvas.experimentstep.Conversion

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Experiment Step Conversion: users.canvas.experimentstep.Conversion

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Experiment Step Conversion: users.canvas.experimentstep.Conversion

{
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
  "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
  "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Experiment Step Conversion: users.canvas.experimentstep.Conversion

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_attributes" : {
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
          "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
          "conversion_behavior_index" : "(optional, int) Index of the conversion behavior"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Experiment Step Conversion: users.canvas.experimentstep.Conversion

{
  "event_properties" : {
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Experiment Step Conversion: users.canvas.experimentstep.Conversion

{
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## Push send events

{% apitags %}
Push, Sends
{% endapitags %}

This event occurs when Braze processes a push message for a user, communicating this to Apple Push Notification Service or Fire Cloud Messaging. This does not mean the push was delivered to the device, just that a message was sent.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Push Notification Send: users.messages.pushnotification.Send

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Send: users.messages.pushnotification.Send

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Push Notification Send: users.messages.pushnotification.Send

{
  "ad_id" : "(optional, string) Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "platform" : "(required, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Push Notification Send: users.messages.pushnotification.Send

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "ios_advertising_id" : "(optional, string) Advertising identifier",
    "android_advertising_id" : "(optional, string) Advertising identifier",
    "microsoft_advertising_id" : "(optional, string) Advertising identifier",
    "roku_advertising_id" : "(optional, string) Advertising identifier",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Push Notification Send: users.messages.pushnotification.Send

{
  "adid" : "(optional, string) Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Send: users.messages.pushnotification.Send

{
  "context" : {
    "traits" : { },
    "device" : {
      "type" : "(required, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(required, string) Platform of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details
- For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you need to explicitly collect the iOS IDFA and Android Google advertising ID through the native SDKs. Learn more about this setup for [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/) and [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- If you are using Kafka to ingest [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) data, contact your customer success manager to enable sending `ad_id`.
- `message_extras` allow you to annotate your send events with dynamic data from Connected Content, custom attributes (such as language, country), and Canvas entry properties. Refer to [Message extras]({{site.baseurl}}/message_extras_tag/) to learn more.
  {% endapi %}
  {% api %}

## Push open events

{% apitags %}
Push, Opens
{% endapitags %}

This event occurs when a user directly clicks on the Push notification to open the application. Currently, Push Open Events refer specifically to "Direct Opens" rather than "Total Opens". This does not include statistics shown at the campaign level of "influenced opens" as these are not attributed at the user level.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Push Notification Open: users.messages.pushnotification.Open

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "device_model" : "(optional, string) Model of the device",
    "button_string" : "(optional, string) Identifier (button_string) of the push notification button clicked. null if not from a button click",
    "button_action_type" : "(optional, string) Action type of the push notification button, null if not from a button click. One of ['uri', 'deep_link', 'none', 'close']",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "timezone" : "(optional, string) Time zone of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Open: users.messages.pushnotification.Open

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "$os" : "(optional, string) Version of the operating system of the device",
    "$device" : "(optional, string) Model of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Push Notification Open: users.messages.pushnotification.Open

{
  "ad_id" : "(optional, string) Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "button_action_type" : "(optional, string) Action type of the push notification button, null if not from a button click. One of ['uri', 'deep_link', 'none', 'close']",
  "button_string" : "(optional, string) Identifier (button_string) of the push notification button clicked. null if not from a button click",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Push Notification Open: users.messages.pushnotification.Open

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) Advertising identifier",
    "android_advertising_id" : "(optional, string) Advertising identifier",
    "microsoft_advertising_id" : "(optional, string) Advertising identifier",
    "roku_advertising_id" : "(optional, string) Advertising identifier",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "device_id" : "(optional, string) ID of the device on which the event occurred"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Push Notification Open: users.messages.pushnotification.Open

{
  "adid" : "(optional, string) Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "device_model" : "(optional, string) Model of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Open: users.messages.pushnotification.Open

{
  "context" : {
    "traits" : { },
    "device" : {
      "type" : "(optional, string) Platform of the device",
      "model" : "(optional, string) Model of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details
- For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you need to explicitly collect the iOS IDFA and Android Google advertising ID through the native SDKs. Learn more about this setup for [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/) and [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- If you are using Kafka to ingest [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) data, contact your customer success manager to enable sending `ad_id`.
  {% endapi %}
  {% api %}

## Push notifications in the iOS foreground events

{% apitags %}
Push, iOS, Sends
{% endapitags %}

This event is not supported by our [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) and is now deprecated using our [Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk).

{% tabs %}
{% tab Braze Standard REST %}
```json
// Push Notification iOS Foreground Open: users.messages.pushnotification.IosForeground

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "device_model" : "(optional, string) Model of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "timezone" : "(optional, string) Time zone of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification iOS Foreground Open: users.messages.pushnotification.IosForeground

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "$os" : "(optional, string) Version of the operating system of the device",
    "$device" : "(optional, string) Model of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Push Notification iOS Foreground Open: users.messages.pushnotification.IosForeground

{
  "ad_id" : "(optional, string) Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "platform" : "(required, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Push Notification iOS Foreground Open: users.messages.pushnotification.IosForeground

{
  "adid" : "(optional, string) Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "device_model" : "(optional, string) Model of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification iOS Foreground Open: users.messages.pushnotification.IosForeground

{
  "context" : {
    "traits" : { },
    "device" : {
      "type" : "(optional, string) Platform of the device",
      "model" : "(optional, string) Model of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details
- For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you need to explicitly collect the iOS IDFA and Android Google advertising ID through the native SDKs. Learn more about this setup for [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/) and [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- If you are using Kafka to ingest [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) data, contact your customer success manager to enable sending `ad_id`.
  {% endapi %}
  {% api %}

## Push notifications bounce

{% apitags %}
Push, Sends, Bounce
{% endapitags %}

This event occurs when an error is received from either Apple Push Notification Service or Fire Cloud Messaging. This means that the push message was bounced, and therefore not delivered to the user's device.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Push Notification Bounce: users.messages.pushnotification.Bounce

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Bounce: users.messages.pushnotification.Bounce

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Push Notification Bounce: users.messages.pushnotification.Bounce

{
  "ad_id" : "(optional, string) Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Push Notification Bounce: users.messages.pushnotification.Bounce

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "ios_advertising_id" : "(optional, string) Advertising identifier",
    "android_advertising_id" : "(optional, string) Advertising identifier",
    "microsoft_advertising_id" : "(optional, string) Advertising identifier",
    "roku_advertising_id" : "(optional, string) Advertising identifier",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Push Notification Bounce: users.messages.pushnotification.Bounce

{
  "adid" : "(optional, string) Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Bounce: users.messages.pushnotification.Bounce

{
  "context" : {
    "traits" : { },
    "device" : {
      "type" : "(optional, string) Platform of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details
- If you are using Kafka to ingest [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) data, reach out to your customer success manager or account manager to enable the feature flipper for sending `ad_id`.
  {% endapi %}
  {% api %}

## Email send events

{% apitags %}
Email, Sends
{% endapitags %}

This event occurs when an email send request was successfully communicated between Braze and SendGrid. Though, this does not mean the email was received in the end user's inbox.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Email Send: users.messages.email.Send

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Send: users.messages.email.Send

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Email Send: users.messages.email.Send

{
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) Email address of the user",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Send: users.messages.email.Send

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
          "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
          "from_domain" : "(optional, string) Sending domain for the email"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user",
    "email" : "(required, string) Email address of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Email Send: users.messages.email.Send

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Send: users.messages.email.Send

{
  "context" : {
    "traits" : {
      "email" : "(required, string) Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details

- The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for entry steps, which can be scheduled) as triggered events, even when they are scheduled. Learn more about [dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
- `message_extras` allow you to annotate your send events with dynamic data from Connected Content, custom attributes (such as language, country), and Canvas entry properties. Refer to [Message extras]({{site.baseurl}}/message_extras_tag/) to learn more.
  {% endapi %}


{% api %}

## Email delivery events

{% apitags %}
Email, Delivery
{% endapitags %}

This event occurs when an email sent made it successfully to the end-users inbox.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Email Delivery: users.messages.email.Delivery

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "sending_ip" : "(optional, string) IP address from which the email send was made",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Delivery: users.messages.email.Delivery

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Email Delivery: users.messages.email.Delivery

{
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) Email address of the user",
  "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
  "external_user_id" : "(optional, string) External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "sending_ip" : "(optional, string) IP address from which the email send was made",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Delivery: users.messages.email.Delivery

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
          "from_domain" : "(optional, string) Sending domain for the email"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user",
    "email" : "(required, string) Email address of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Email Delivery: users.messages.email.Delivery

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Delivery: users.messages.email.Delivery

{
  "context" : {
    "traits" : {
      "email" : "(required, string) Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details

- The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for entry steps, which can be scheduled) as triggered events, even when they are scheduled. Learn more about [dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
  {% endapi %}

{% api %}

## Email open events

{% apitags %}
Email, Opens
{% endapitags %}

This event occurs when a user opens an email. Multiple events may be generated for the same campaign if a user opens the email multiple times.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Email Open: users.messages.email.Open

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "device_model" : "(optional, string) Model of the device",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "from_domain" : "(optional, string) Sending domain for the email",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Open: users.messages.email.Open

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "$device" : "(optional, string) Model of the device",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "from_domain" : "(optional, string) Sending domain for the email",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Email Open: users.messages.email.Open

{
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
  "device_model" : "(optional, string) Model of the device",
  "device_os" : "(optional, string) Device operating system extracted from user_agent",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) Email address of the user",
  "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
  "external_user_id" : "(optional, string) External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
  "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
  "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Open: users.messages.email.Open

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "device_model" : "(optional, string) Model of the device"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "user_agent" : "(optional, string) User agent on which the spam report occurred",
          "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
          "device_os" : "(optional, string) Device operating system extracted from user_agent",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
          "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
          "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
          "from_domain" : "(optional, string) Sending domain for the email",
          "is_amp" : "(optional, boolean) Indicates that this is an AMP event"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user",
    "email" : "(required, string) Email address of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Email Open: users.messages.email.Open

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "device_model" : "(optional, string) Model of the device",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "from_domain" : "(optional, string) Sending domain for the email",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Open: users.messages.email.Open

{
  "context" : {
    "traits" : {
      "email" : "(required, string) Email address of the user"
    },
    "device" : {
      "model" : "(optional, string) Model of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "from_domain" : "(optional, string) Sending domain for the email",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details

- The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for entry steps, which can be scheduled) as triggered events, even when they are scheduled. Learn more about [dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
  {% endapi %}

{% api %}

## Email clicks events

{% apitags %}
Email, Clicks
{% endapitags %}

This event occurs when a user clicks an email. Multiple events may be generated for the same campaign if a user clicks multiple times or clicks different links within the email.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Email Click: users.messages.email.Click

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "device_model" : "(optional, string) Model of the device",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
    "link_alias" : "(optional, string) Alias associated with this link ID",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Click: users.messages.email.Click

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "$device" : "(optional, string) Model of the device",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
    "link_alias" : "(optional, string) Alias associated with this link ID",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Email Click: users.messages.email.Click

{
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
  "device_model" : "(optional, string) Model of the device",
  "device_os" : "(optional, string) Device operating system extracted from user_agent",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) Email address of the user",
  "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
  "external_user_id" : "(optional, string) External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
  "link_alias" : "(optional, string) Alias associated with this link ID",
  "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
  "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "url" : "(optional, string) URL that the user clicked on",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Click: users.messages.email.Click

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "device_model" : "(optional, string) Model of the device"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "url" : "(optional, string) URL that the user clicked on",
          "user_agent" : "(optional, string) User agent on which the spam report occurred",
          "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
          "device_os" : "(optional, string) Device operating system extracted from user_agent",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
          "link_alias" : "(optional, string) Alias associated with this link ID",
          "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
          "is_amp" : "(optional, boolean) Indicates that this is an AMP event"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user",
    "email" : "(required, string) Email address of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Email Click: users.messages.email.Click

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "device_model" : "(optional, string) Model of the device",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
    "link_alias" : "(optional, string) Alias associated with this link ID",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Click: users.messages.email.Click

{
  "context" : {
    "traits" : {
      "email" : "(required, string) Email address of the user"
    },
    "device" : {
      "model" : "(optional, string) Model of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "url" : "(optional, string) URL that the user clicked on",
    "link_url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
    "link_alias" : "(optional, string) Alias associated with this link ID",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details

- The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for entry steps, which can be scheduled) as triggered events, even when they are scheduled. Learn more about [dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
  {% endapi %}

{% api %}

## Email bounce event

{% apitags %}
Email, Bounce
{% endapitags %}

This event occurs when an Internet Service Provider returns a hard bounce. A hard bounce signifies a permanent deliverability failure.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Email Bounce: users.messages.email.Bounce

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "sending_ip" : "(optional, string) IP address from which the email send was made",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "bounce_reason" : "(optional, string) The SMTP reason code and user friendly message received for this bounce event",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Bounce: users.messages.email.Bounce

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "bounce_reason" : "(optional, string) The SMTP reason code and user friendly message received for this bounce event",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Email Bounce: users.messages.email.Bounce

{
  "bounce_reason" : "(optional, string) The SMTP reason code and user friendly message received for this bounce event",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) Email address of the user",
  "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
  "external_user_id" : "(optional, string) External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "sending_ip" : "(optional, string) IP address from which the email send was made",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Bounce: users.messages.email.Bounce

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "bounce_reason" : "(optional, string) The SMTP reason code and user friendly message received for this bounce event",
          "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user",
    "email" : "(required, string) Email address of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Email Bounce: users.messages.email.Bounce

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "bounce_reason" : "(optional, string) The SMTP reason code and user friendly message received for this bounce event",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Bounce: users.messages.email.Bounce

{
  "context" : {
    "traits" : {
      "email" : "(required, string) Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "bounce_reason" : "(optional, string) The SMTP reason code and user friendly message received for this bounce event",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details

- The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for entry steps, which can be scheduled) as triggered events, even when they are scheduled. Learn more about [dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
  {% endapi %}

{% api %}

## Email soft bounce event

{% apitags %}
Email, Bounce
{% endapitags %}

This event occurs when an Internet Service Provider returns a soft bounce. A soft bounce signifies that an email could not be delivered because of a temporary deliverability failure.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Email Soft Bounce: users.messages.email.SoftBounce

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "sending_ip" : "(optional, string) IP address from which the email send was made",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "bounce_reason" : "(optional, string) The SMTP reason code and user friendly message received for this bounce event",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Soft Bounce: users.messages.email.SoftBounce

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "bounce_reason" : "(optional, string) The SMTP reason code and user friendly message received for this bounce event",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Email Soft Bounce: users.messages.email.SoftBounce

{
  "bounce_reason" : "(optional, string) The SMTP reason code and user friendly message received for this bounce event",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) Email address of the user",
  "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
  "external_user_id" : "(optional, string) External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "sending_ip" : "(optional, string) IP address from which the email send was made",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Soft Bounce: users.messages.email.SoftBounce

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "bounce_reason" : "(optional, string) The SMTP reason code and user friendly message received for this bounce event",
          "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
          "from_domain" : "(optional, string) Sending domain for the email"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user",
    "email" : "(required, string) Email address of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Email Soft Bounce: users.messages.email.SoftBounce

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "bounce_reason" : "(optional, string) The SMTP reason code and user friendly message received for this bounce event",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Soft Bounce: users.messages.email.SoftBounce

{
  "context" : {
    "traits" : {
      "email" : "(required, string) Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "bounce_reason" : "(optional, string) The SMTP reason code and user friendly message received for this bounce event",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details

- The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for entry steps, which can be scheduled) as triggered events, even when they are scheduled. Learn more about [dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
  {% endapi %}

{% api %}

## Email spam events

{% apitags %}
Email, Spam
{% endapitags %}

This event occurs when the end-user hits the "spam" button on the email. Note that this does not represent the fact the email went into the spam folder as Braze does not track this.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Email Mark As Spam: users.messages.email.MarkAsSpam

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Mark As Spam: users.messages.email.MarkAsSpam

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Email Mark As Spam: users.messages.email.MarkAsSpam

{
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) Email address of the user",
  "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
  "external_user_id" : "(optional, string) External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Mark As Spam: users.messages.email.MarkAsSpam

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "user_agent" : "(optional, string) User agent on which the spam report occurred",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
          "from_domain" : "(optional, string) Sending domain for the email"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user",
    "email" : "(required, string) Email address of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Email Mark As Spam: users.messages.email.MarkAsSpam

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Mark As Spam: users.messages.email.MarkAsSpam

{
  "context" : {
    "traits" : {
      "email" : "(required, string) Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "esp" : "(optional, string) ESP related to the event (Sparkpost or Sendgrid)",
    "from_domain" : "(optional, string) Sending domain for the email"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details

The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for entry steps, which can be scheduled) as triggered events, even when they are scheduled. Learn more about [dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}


{% api %}

## Email unsubscribe events

{% apitags %}
Email, Subscription
{% endapitags %}

This event occurs when the end-user has clicked "unsubscribe" from the email.

{% alert important %}
The `Unsubscribe` event is actually a specialized click event that is fired when your user clicks on the unsubscribe link in the email (either a normal unsubscribe link within the email body or footer, or using the [list-unsubscribe header]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings#include-a-list-unsubscribe-header)), not when the user changes state to unsubscribed. If subscription state change is sent through the API, it will not trigger an event on Currents.
{% endalert %}

{% tabs %}
{% tab Braze Standard REST %}
```json
// Email Unsubscribe: users.messages.email.Unsubscribe

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Unsubscribe: users.messages.email.Unsubscribe

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Email Unsubscribe: users.messages.email.Unsubscribe

{
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) Email address of the user",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Unsubscribe: users.messages.email.Unsubscribe

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "ip_pool" : "(optional, string) IP pool from which the email send was made"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user",
    "email" : "(required, string) Email address of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Email Unsubscribe: users.messages.email.Unsubscribe

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "email_address" : "(required, string) Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Unsubscribe: users.messages.email.Unsubscribe

{
  "context" : {
    "traits" : {
      "email" : "(required, string) Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "ip_pool" : "(optional, string) IP pool from which the email send was made"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details

The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for entry steps, which can be scheduled) as triggered events, even when they are scheduled. Learn more about [dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}

## In-app message impression events

{% apitags %}
In-App Messages, Impressions
{% endapitags %}

This event occurs when a user views an in-app message.

{% tabs %}
{% tab Braze Standard REST %}
```json
// In-App Message Impression: users.messages.inappmessage.Impression

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "card_id" : "(optional, string) API ID of the card",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "device_model" : "(optional, string) Model of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "timezone" : "(optional, string) Time zone of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// In-App Message Impression: users.messages.inappmessage.Impression

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "card_id" : "(optional, string) API ID of the card",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "$os" : "(optional, string) Version of the operating system of the device",
    "$device" : "(optional, string) Model of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// In-App Message Impression: users.messages.inappmessage.Impression

{
  "ad_id" : "(optional, string) Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "card_id" : "(optional, string) API ID of the card",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// In-App Message Impression: users.messages.inappmessage.Impression

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) Advertising identifier",
    "android_advertising_id" : "(optional, string) Advertising identifier",
    "microsoft_advertising_id" : "(optional, string) Advertising identifier",
    "roku_advertising_id" : "(optional, string) Advertising identifier",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "card_id" : "(optional, string) API ID of the card",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// In-App Message Impression: users.messages.inappmessage.Impression

{
  "adid" : "(optional, string) Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "card_id" : "(optional, string) API ID of the card",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "device_model" : "(optional, string) Model of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// In-App Message Impression: users.messages.inappmessage.Impression

{
  "context" : {
    "traits" : { },
    "device" : {
      "type" : "(optional, string) Platform of the device",
      "model" : "(optional, string) Model of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "card_id" : "(optional, string) API ID of the card",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% alert note %}
The `message_extras` field will be active on April 4, 2024.
{% endalert %}

#### Property details
- For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you need to explicitly collect the iOS IDFA and Android Google advertising ID through the native SDKs. Learn more about this setup for [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/) and [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- If you are using Kafka to ingest [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) data, contact your customer success manager to enable sending `ad_id`.
  {% endapi %}

{% api %}

## In-app message click events

{% apitags %}
In-App Messages, Clicks
{% endapitags %}

This event occurs when a user clicks on an in-app message.

{% tabs %}
{% tab Braze Standard REST %}
```json
// In-App Message Click: users.messages.inappmessage.Click

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "card_id" : "(optional, string) API ID of the card",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "device_model" : "(optional, string) Model of the device",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "timezone" : "(optional, string) Time zone of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// In-App Message Click: users.messages.inappmessage.Click

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "card_id" : "(optional, string) API ID of the card",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "$os" : "(optional, string) Version of the operating system of the device",
    "$device" : "(optional, string) Model of the device",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// In-App Message Click: users.messages.inappmessage.Click

{
  "ad_id" : "(optional, string) Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "card_id" : "(optional, string) API ID of the card",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// In-App Message Click: users.messages.inappmessage.Click

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) Advertising identifier",
    "android_advertising_id" : "(optional, string) Advertising identifier",
    "microsoft_advertising_id" : "(optional, string) Advertising identifier",
    "roku_advertising_id" : "(optional, string) Advertising identifier",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "card_id" : "(optional, string) API ID of the card",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// In-App Message Click: users.messages.inappmessage.Click

{
  "adid" : "(optional, string) Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "card_id" : "(optional, string) API ID of the card",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "device_model" : "(optional, string) Model of the device",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// In-App Message Click: users.messages.inappmessage.Click

{
  "context" : {
    "traits" : { },
    "device" : {
      "type" : "(optional, string) Platform of the device",
      "model" : "(optional, string) Model of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "card_id" : "(optional, string) API ID of the card",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details
- For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you need to explicitly collect the iOS IDFA and Android Google advertising ID through the native SDKs. Learn more about this setup for [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/) and [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- If you are using Kafka to ingest [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) data, contact your customer success manager to enable sending `ad_id`.
  {% endapi %}


{% api %}

## Webhook send events

{% apitags %}
Webhooks, Sends
{% endapitags %}

This event occurs when a webhook was processed and sent to the third party specified in that webhook. Note that this does not signify whether or not the request was received.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Webhook Send: users.messages.webhook.Send

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Webhook Send: users.messages.webhook.Send

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Webhook Send: users.messages.webhook.Send

{
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Webhook Send: users.messages.webhook.Send

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Webhook Send: users.messages.webhook.Send

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Webhook Send: users.messages.webhook.Send

{
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details

- `message_extras` allow you to annotate your send events with dynamic data from Connected Content, custom attributes (such as language, country), and Canvas entry properties. Refer to [Message extras]({{site.baseurl}}/message_extras_tag/) to learn more.

{% endapi %}

{% api %}
## Content Card send events

{% apitags %}
Content Cards, Sends
{% endapitags %}

This event occurs when a Content Card gets sent to a user.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Content Card Send: users.messages.contentcard.Send

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "content_card_id" : "(required, string) ID of the card that generated this event",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Send: users.messages.contentcard.Send

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "card_id" : "(required, string) ID of the card that generated this event",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Content Card Send: users.messages.contentcard.Send

{
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "content_card_id" : "(required, string) ID of the card that generated this event",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Send: users.messages.contentcard.Send

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "card_id" : "(required, string) ID of the card that generated this event",
          "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Content Card Send: users.messages.contentcard.Send

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "card_id" : "(required, string) ID of the card that generated this event",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Content Card Send: users.messages.contentcard.Send

{
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "card_id" : "(required, string) ID of the card that generated this event",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details

- `message_extras` allow you to annotate your send events with dynamic data from Connected Content, custom attributes (such as language, country), and Canvas entry properties. Refer to [Message extras]({{site.baseurl}}/message_extras_tag/) to learn more.
  {% endapi %}

{% api %}
## Content Card impression events

{% apitags %}
Content Cards, Impressions
{% endapitags %}

This event occurs when a user views a Content Card.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Content Card Impression: users.messages.contentcard.Impression

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "content_card_id" : "(required, string) ID of the card that generated this event",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "device_model" : "(optional, string) Model of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "timezone" : "(optional, string) Time zone of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Impression: users.messages.contentcard.Impression

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "card_id" : "(required, string) ID of the card that generated this event",
    "distinct_id" : "(required, string) External ID of the user",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "$os" : "(optional, string) Version of the operating system of the device",
    "$device" : "(optional, string) Model of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Content Card Impression: users.messages.contentcard.Impression

{
  "ad_id" : "(optional, string) Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "content_card_id" : "(required, string) ID of the card that generated this event",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Impression: users.messages.contentcard.Impression

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) Advertising identifier",
    "android_advertising_id" : "(optional, string) Advertising identifier",
    "microsoft_advertising_id" : "(optional, string) Advertising identifier",
    "roku_advertising_id" : "(optional, string) Advertising identifier",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "card_id" : "(required, string) ID of the card that generated this event",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "device_id" : "(optional, string) ID of the device on which the event occurred"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Content Card Impression: users.messages.contentcard.Impression

{
  "adid" : "(optional, string) Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "card_id" : "(required, string) ID of the card that generated this event",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "device_model" : "(optional, string) Model of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Content Card Impression: users.messages.contentcard.Impression

{
  "context" : {
    "traits" : { },
    "device" : {
      "type" : "(optional, string) Platform of the device",
      "model" : "(optional, string) Model of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "card_id" : "(required, string) ID of the card that generated this event",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details
- For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you need to explicitly collect the iOS IDFA and Android Google advertising ID through the native SDKs. Learn more about this setup for [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/) and [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- If you are using Kafka to ingest [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) data, contact your customer success manager to enable sending `ad_id`.
  {% endapi %}

{% api %}
## Content Card click events

{% apitags %}
Content Cards, Clicks
{% endapitags %}

This event occurs when a user clicks a Content Card.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Content Card Click: users.messages.contentcard.Click

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "content_card_id" : "(required, string) ID of the card that generated this event",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "device_model" : "(optional, string) Model of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "timezone" : "(optional, string) Time zone of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Click: users.messages.contentcard.Click

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "card_id" : "(required, string) ID of the card that generated this event",
    "distinct_id" : "(required, string) External ID of the user",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "$os" : "(optional, string) Version of the operating system of the device",
    "$device" : "(optional, string) Model of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Content Card Click: users.messages.contentcard.Click

{
  "ad_id" : "(optional, string) Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "content_card_id" : "(required, string) ID of the card that generated this event",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Click: users.messages.contentcard.Click

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) Advertising identifier",
    "android_advertising_id" : "(optional, string) Advertising identifier",
    "microsoft_advertising_id" : "(optional, string) Advertising identifier",
    "roku_advertising_id" : "(optional, string) Advertising identifier",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "card_id" : "(required, string) ID of the card that generated this event",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "device_id" : "(optional, string) ID of the device on which the event occurred"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Content Card Click: users.messages.contentcard.Click

{
  "adid" : "(optional, string) Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "card_id" : "(required, string) ID of the card that generated this event",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "device_model" : "(optional, string) Model of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Content Card Click: users.messages.contentcard.Click

{
  "context" : {
    "traits" : { },
    "device" : {
      "type" : "(optional, string) Platform of the device",
      "model" : "(optional, string) Model of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "card_id" : "(required, string) ID of the card that generated this event",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details
- For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you need to explicitly collect the iOS IDFA and Android Google advertising ID through the native SDKs. Learn more about this setup for [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/) and [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- If you are using Kafka to ingest [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) data, contact your customer success manager to enable sending `ad_id`.
  {% endapi %}


{% api %}
## Content Card dismissal events

{% apitags %}
Content Cards, Dismissal
{% endapitags %}

This event occurs when a user dismisses a Content Card.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Content Card Dismiss: users.messages.contentcard.Dismiss

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "content_card_id" : "(required, string) ID of the card that generated this event",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "device_model" : "(optional, string) Model of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "timezone" : "(optional, string) Time zone of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Dismiss: users.messages.contentcard.Dismiss

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "card_id" : "(required, string) ID of the card that generated this event",
    "distinct_id" : "(required, string) External ID of the user",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "$os" : "(optional, string) Version of the operating system of the device",
    "$device" : "(optional, string) Model of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Content Card Dismiss: users.messages.contentcard.Dismiss

{
  "ad_id" : "(optional, string) Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "content_card_id" : "(required, string) ID of the card that generated this event",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Dismiss: users.messages.contentcard.Dismiss

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) Advertising identifier",
    "android_advertising_id" : "(optional, string) Advertising identifier",
    "microsoft_advertising_id" : "(optional, string) Advertising identifier",
    "roku_advertising_id" : "(optional, string) Advertising identifier",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "card_id" : "(required, string) ID of the card that generated this event",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "device_id" : "(optional, string) ID of the device on which the event occurred"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Content Card Dismiss: users.messages.contentcard.Dismiss

{
  "adid" : "(optional, string) Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "card_id" : "(required, string) ID of the card that generated this event",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "platform" : "(optional, string) Platform of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "device_model" : "(optional, string) Model of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Content Card Dismiss: users.messages.contentcard.Dismiss

{
  "context" : {
    "traits" : { },
    "device" : {
      "type" : "(optional, string) Platform of the device",
      "model" : "(optional, string) Model of the device"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "card_id" : "(required, string) ID of the card that generated this event",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details
- For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you need to explicitly collect the iOS IDFA and Android Google advertising ID through the native SDKs. Learn more about this setup for [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/) and [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- If you are using Kafka to ingest [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) data, contact your customer success manager to enable sending `ad_id`.
  {% endapi %}


{% api %}

## SMS click events

{% apitags %}
SMS, Clicks
{% endapitags %}

This event occurs when a user clicks an SMS short link.

{% tabs %}
{% tab Braze Standard REST %}
```json
// SMS Short Link Click: users.messages.sms.ShortLinkClick

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "url" : "(optional, string) URL that the user clicked on",
    "short_url" : "(required, string) Shortened url that was clicked",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "user_phone_number" : "(optional, string) The user's phone number from which the message was received",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Short Link Click: users.messages.sms.ShortLinkClick

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "url" : "(optional, string) URL that the user clicked on",
    "short_url" : "(required, string) Shortened url that was clicked",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "user_phone_number" : "(optional, string) The user's phone number from which the message was received",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// SMS Short Link Click: users.messages.sms.ShortLinkClick

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "short_url" : "(required, string) Shortened url that was clicked",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "url" : "(required, string) URL that the user clicked on",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) BSON ID of the user who performed this event",
  "user_phone_number" : "(optional, string) The user's phone number from which the message was received"
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Short Link Click: users.messages.sms.ShortLinkClick

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "url" : "(optional, string) URL that the user clicked on",
          "short_url" : "(required, string) Shortened url that was clicked",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// SMS Short Link Click: users.messages.sms.ShortLinkClick

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "url" : "(optional, string) URL that the user clicked on",
    "short_url" : "(required, string) Shortened url that was clicked",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "user_phone_number" : "(optional, string) The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Short Link Click: users.messages.sms.ShortLinkClick

{
  "context" : {
    "traits" : {
      "phone" : "(optional, string) The user's phone number from which the message was received"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "url" : "(optional, string) URL that the user clicked on",
    "link_url" : "(optional, string) URL that the user clicked on",
    "short_url" : "(required, string) Shortened url that was clicked",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}
{% api %}
## SMS send events

{% apitags %}
SMS, Sends
{% endapitags %}

This event occurs when a user sends an SMS.

{% tabs %}
{% tab Braze Standard REST %}
```json
// SMS Send: users.messages.sms.Send

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Send: users.messages.sms.Send

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// SMS Send: users.messages.sms.Send

{
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Send: users.messages.sms.Send

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
          "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// SMS Send: users.messages.sms.Send

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Send: users.messages.sms.Send

{
  "context" : {
    "traits" : {
      "phone" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details
- `message_extras` allow you to annotate your send events with dynamic data from Connected Content, custom attributes (such as language, country), and Canvas entry properties. Refer to [Message extras]({{site.baseurl}}/message_extras_tag/) to learn more.

{% endapi %}

{% api %}

## SMS sends to carrier events

{% apitags %}
SMS, Delivery
{% endapitags %}

{% alert important %}
`CarrierSend` is supported only for users on legacy infrastructure.
{% endalert %}

This event occurs when an SMS is sent to the carrier.

{% tabs %}
{% tab Braze Standard REST %}
```json
// SMS Carrier Send: users.messages.sms.CarrierSend

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Carrier Send: users.messages.sms.CarrierSend

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// SMS Carrier Send: users.messages.sms.CarrierSend

{
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Carrier Send: users.messages.sms.CarrierSend

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// SMS Carrier Send: users.messages.sms.CarrierSend

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Carrier Send: users.messages.sms.CarrierSend

{
  "context" : {
    "traits" : {
      "phone" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## SMS delivery events

{% apitags %}
SMS, Delivery
{% endapitags %}

This event occurs when an SMS was successfully delivered to the users mobile phone.

{% tabs %}
{% tab Braze Standard REST %}
```json
// SMS Delivery: users.messages.sms.Delivery

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Delivery: users.messages.sms.Delivery

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// SMS Delivery: users.messages.sms.Delivery

{
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Delivery: users.messages.sms.Delivery

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// SMS Delivery: users.messages.sms.Delivery

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Delivery: users.messages.sms.Delivery

{
  "context" : {
    "traits" : {
      "phone" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## SMS rejection events

{% apitags %}
SMS, Rejection
{% endapitags %}

This event occurs when an SMS send gets rejected by the carrier, this can happen for several reasons. Use this event and the provided error codes to help troubleshoot issues with SMS delivery.

{% tabs %}
{% tab Braze Standard REST %}
```json
// SMS Rejection: users.messages.sms.Rejection

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "error" : "(optional, string) Error name",
    "provider_error_code" : "(optional, string) Error code from WhatsApp",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Rejection: users.messages.sms.Rejection

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "error" : "(optional, string) Error name",
    "provider_error_code" : "(optional, string) Error code from WhatsApp",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// SMS Rejection: users.messages.sms.Rejection

{
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "error" : "(optional, string) Error name",
  "external_user_id" : "(optional, string) External ID of the user",
  "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "provider_error_code" : "(optional, string) Error code from WhatsApp",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Rejection: users.messages.sms.Rejection

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "error" : "(optional, string) Error name",
          "provider_error_code" : "(optional, string) Error code from WhatsApp"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// SMS Rejection: users.messages.sms.Rejection

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "error" : "(optional, string) Error name",
    "provider_error_code" : "(optional, string) Error code from WhatsApp"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Rejection: users.messages.sms.Rejection

{
  "context" : {
    "traits" : {
      "phone" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "error" : "(optional, string) Error name",
    "provider_error_code" : "(optional, string) Error code from WhatsApp"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}


{% api %}

## SMS delivery failure events

{% apitags %}
SMS, Delivery
{% endapitags %}

This event occurs when an SMS experiences delivery failure. Use this event and the provided error codes to help troubleshoot issues with SMS delivery.

{% tabs %}
{% tab Braze Standard REST %}
```json
// SMS Delivery Failure: users.messages.sms.DeliveryFailure

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "error" : "(optional, string) Error name",
    "provider_error_code" : "(optional, string) Error code from WhatsApp",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Delivery Failure: users.messages.sms.DeliveryFailure

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "error" : "(optional, string) Error name",
    "provider_error_code" : "(optional, string) Error code from WhatsApp",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// SMS Delivery Failure: users.messages.sms.DeliveryFailure

{
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "error" : "(optional, string) Error name",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "provider_error_code" : "(optional, string) Error code from WhatsApp",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Delivery Failure: users.messages.sms.DeliveryFailure

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "error" : "(optional, string) Error name",
          "provider_error_code" : "(optional, string) Error code from WhatsApp"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// SMS Delivery Failure: users.messages.sms.DeliveryFailure

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "to_phone_number" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "error" : "(optional, string) Error name",
    "provider_error_code" : "(optional, string) Error code from WhatsApp"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Delivery Failure: users.messages.sms.DeliveryFailure

{
  "context" : {
    "traits" : {
      "phone" : "(optional, string) Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "error" : "(optional, string) Error name",
    "provider_error_code" : "(optional, string) Error code from WhatsApp"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}
{% api %}

## SMS inbound received events

{% apitags %}
SMS, InboundReceived
{% endapitags %}

This event occurs when one of your users sends an SMS to a phone number in one of your Braze SMS subscription groups.

When Braze receives an inbound SMS, we attribute that inbound message to any user that shares that phone number. As a result, you may receive multiple events per inbound message if multiple users in your Braze instance share the same phone number. If you require attribution of specific user IDs based on previous messages sent to that user, you can use the SMS Delivered event to attribute Inbound Received events to the user ID who most recently received a message from your Braze number.

If we detect that this inbound message is a reply to an outbound campaign or Canvas component sent from Braze, we will also include the campaign or Canvas metadata with the event. Braze defines a reply as an inbound message coming within four hours of an outbound message. However, there is a one-minute cache for the attributed campaign information of the last outbound SMS received.

{% tabs %}
{% tab Braze Standard REST %}
```json
// SMS Inbound Received: users.messages.sms.InboundReceive

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "user_phone_number" : "(required, string) The user's phone number from which the message was received",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "message_body" : "(optional, string) Typed response from the user",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Inbound Received: users.messages.sms.InboundReceive

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "user_phone_number" : "(required, string) The user's phone number from which the message was received",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "message_body" : "(optional, string) Typed response from the user",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// SMS Inbound Received: users.messages.sms.InboundReceive

{
  "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
  "app_group_id" : "(required, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
  "media_urls" : "(optional, array of string) Media URLs from the user",
  "message_body" : "(required, string) Typed response from the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) BSON ID of the user who performed this event",
  "user_phone_number" : "(required, string) The user's phone number from which the message was received"
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Inbound Received: users.messages.sms.InboundReceive

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
          "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
          "message_body" : "(optional, string) Typed response from the user",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// SMS Inbound Received: users.messages.sms.InboundReceive

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "user_phone_number" : "(required, string) The user's phone number from which the message was received",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "message_body" : "(optional, string) Typed response from the user",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Inbound Received: users.messages.sms.InboundReceive

{
  "context" : {
    "traits" : {
      "phone" : "(required, string) The user's phone number from which the message was received"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "message_body" : "(optional, string) Typed response from the user",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}


{% api %}

## Campaign conversion events

{% apitags %}
Campaign, Conversion
{% endapitags %}

This event occurs when a user does an action that has been set as a conversion event in a campaign.

{% alert important %}
Note that the conversion event is encoded in the `conversion_behavior` field, which includes the type of conversion event, the window (timeframe), and additional information depending on the conversion event type. The `conversion_behavior_index` field represents which conversion event, such as 0 = A, 1 = B, 2 = C, 3 = D.
{% endalert %}

{% tabs %}
{% tab Braze Standard REST %}
```json
// Campaign Conversion: users.campaigns.Conversion

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Campaign Conversion: users.campaigns.Conversion

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Campaign Conversion: users.campaigns.Conversion

{
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(required, string) API ID of the campaign this event belongs to",
  "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Campaign Conversion: users.campaigns.Conversion

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "conversion_behavior_index" : "(optional, int) Index of the conversion behavior"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Campaign Conversion: users.campaigns.Conversion

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Campaign Conversion: users.campaigns.Conversion

{
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}


{% api %}

## Canvas conversion events

{% apitags %}
Canvas, Conversion
{% endapitags %}

This event occurs when a user does an action that has been set as a conversion event in Canvas.

{% alert important %}
Note that the conversion event is encoded in the `conversion_behavior` field, which includes the type of conversion event, the window (timeframe), and additional information depending on the conversion event type. The `conversion_behavior_index` field represents which conversion event, such as 0 = A, 1 = B, 2 = C, 3 = D.
{% endalert %}

{% tabs %}
{% tab Braze Standard REST %}
```json
// Canvas Conversion: users.canvas.Conversion

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Canvas Conversion: users.canvas.Conversion

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Canvas Conversion: users.canvas.Conversion

{
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "canvas_id" : "(required, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(required, string) API ID of the Canvas variation this event belongs to",
  "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Canvas Conversion: users.canvas.Conversion

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "conversion_behavior_index" : "(optional, int) Index of the conversion behavior"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Canvas Conversion: users.canvas.Conversion

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Canvas Conversion: users.canvas.Conversion

{
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}


{% api %}

## Canvas entry events

{% apitags %}
Canvas, Entry
{% endapitags %}

This event occurs when a user enters into the Canvas. This event tells you which variant the user entered into.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Canvas Entry: users.canvas.Entry

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Canvas Entry: users.canvas.Entry

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Canvas Entry: users.canvas.Entry

{
  "canvas_id" : "(required, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(required, string) API ID of the Canvas variation this event belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Canvas Entry: users.canvas.Entry

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Canvas Entry: users.canvas.Entry

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Canvas Entry: users.canvas.Entry

{
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Campaign control group enrollment events

{% apitags %}
Campaign, Entry
{% endapitags %}

This event occurs when a user is enrolled in a control variant set on a multi-variant campaign. This event is generated as there will be no channel send event for this user.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Campaign Control Group Enrollment: users.campaigns.EnrollInControl

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Campaign Control Group Enrollment: users.campaigns.EnrollInControl

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Campaign Control Group Enrollment: users.campaigns.EnrollInControl

{
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(required, string) API ID of the campaign this event belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Campaign Control Group Enrollment: users.campaigns.EnrollInControl

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Campaign Control Group Enrollment: users.campaigns.EnrollInControl

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Campaign Control Group Enrollment: users.campaigns.EnrollInControl

{
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## Subscription events

{% apitags %}
Subscription
{% endapitags %}

This event occurs when the subscription state of a user in a subscription group changes.

{% alert important %}
Subscription groups are only available for email, SMS, and WhatsApp channels at this time.
{% endalert %}

{% tabs %}
{% tab Braze Standard REST %}
```json
// Subscription Group State Change: users.behaviors.subscriptiongroup.StateChange

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "email_address" : "(optional, string) Email address of the user",
    "phone_number" : "(optional, string) Phone number of the user in e.164 format (for example +14155552671)",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "subscription_group_id" : "(required, string) Subscription group API ID",
    "channel" : "(optional, string) Channel this event belongs to",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Subscription Group State Change: users.behaviors.subscriptiongroup.StateChange

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "email_address" : "(optional, string) Email address of the user",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "subscription_group_id" : "(required, string) Subscription group API ID",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Subscription Group State Change: users.behaviors.subscriptiongroup.StateChange

{
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "channel" : "(optional, string) Channel this event belongs to",
  "email_address" : "(optional, string) Email address of the user",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "phone_number" : "(optional, string) Phone number of the user in e.164 format (for example +14155552671)",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
  "subscription_group_id" : "(required, string) Subscription group API ID",
  "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Subscription Group State Change: users.behaviors.subscriptiongroup.StateChange

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "subscription_group_id" : "(required, string) Subscription group API ID",
          "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc."
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user",
    "email" : "(optional, string) Email address of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Subscription Group State Change: users.behaviors.subscriptiongroup.StateChange

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "email_address" : "(optional, string) Email address of the user",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "subscription_group_id" : "(required, string) Subscription group API ID",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
    "timezone" : "(optional, string) Time zone of the user",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc."
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Subscription Group State Change: users.behaviors.subscriptiongroup.StateChange

{
  "context" : {
    "traits" : {
      "email" : "(optional, string) Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "subscription_group_id" : "(required, string) Subscription group API ID",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc."
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details

`state_change_source` will return a string of the full source name. For example, the source CSV import will return the string `CSV Import`. Available sources are listed below:

| Source | Description |
| --- | --- |
| SDK | SDK endpoints |
| Dashboard | When a user's subscription state is updated from the User Profile page in Dashboard |
| Subscription Page | When a user unsubscribes through an email link that is not the preference center |
| REST API | REST API endpoints |
| CSV import | CSV user import |
| Preference Center | When a user is updated from the preference center |
| Inbound Message | When a user is updated by inbound messages from end-users through channels such as SMS |
| Migration | When a user is updated by internal migrations or maintenance scripts |
| User Merge | When a user is updated by the user merge process |
| Canvas User Update Step | When a user is updated by the Canvas user update step |
| List-Unsubscribe | When a user unsubscribes via Braze mailto or one-click list-unsubscribe header |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}

{% api %}

## Global state change events

{% apitags %}
Subscription
{% endapitags %}

This event occurs when Braze receives a request to update the global subscription state of the user, even if the request doesn't alter the current subscription state for the user.

{% tabs %}
{% tab Braze Standard REST %}
```json
// Global Subscription State Change: users.behaviors.subscription.GlobalStateChange

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "email_address" : "(optional, string) Email address of the user",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
    "channel" : "(optional, string) Channel this event belongs to",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "timezone" : "(optional, string) Time zone of the user"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Global Subscription State Change: users.behaviors.subscription.GlobalStateChange

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "email_address" : "(optional, string) Email address of the user",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Global Subscription State Change: users.behaviors.subscription.GlobalStateChange

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "channel" : "(optional, string) Channel this event belongs to",
  "email_address" : "(optional, string) Email address of the user",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
  "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Global Subscription State Change: users.behaviors.subscription.GlobalStateChange

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
          "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "send_id" : "(optional, string) Message send ID this message belongs to"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened",
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user",
    "email" : "(optional, string) Email address of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Global Subscription State Change: users.behaviors.subscription.GlobalStateChange

{
  "event_properties" : {
    "email_address" : "(optional, string) Email address of the user",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
    "timezone" : "(optional, string) Time zone of the user",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Global Subscription State Change: users.behaviors.subscription.GlobalStateChange

{
  "context" : {
    "traits" : {
      "email" : "(optional, string) Email address of the user"
    },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Property details

`state_change_source` will return a string of the full source name. For example, the source CSV import will return the string `CSV Import`. Available sources are listed below:

| Source | Description |
| --- | --- |
| SDK | SDK endpoints |
| Dashboard | When a user's subscription state is updated from the **User Profile** page in the dashboard |
| Subscription Page | When a user unsubscribes through an email link that is not the preference center |
| REST API | REST API endpoints |
| CSV import | CSV user import |
| Preference Center | When a user is updated from the preference center |
| Inbound Message | When a user is updated by inbound messages from end-users through channels, such as SMS |
| Migration | When a user is updated by internal migrations or maintenance scripts |
| User Merge | When a user is updated by the merging users process |
| Canvas User Update Step | When a user is updated by the Canvas User Update step |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
{% api %}
## Uninstall events

{% apitags %}
Uninstall
{% endapitags %}

This event occurs when a user uninstalls an app. Use this data to track when users uninstall an app. While this is currently a message engagement event, this will be changed to a user behavior event in the future.

{% alert important %}
This event is not fired when the user actually uninstalls the app, as that's impossible to track exactly. Braze sends a daily silent push to determine if the app still exists on your user's device, and if we get an error on that silent push, it is assumed the app has been uninstalled.
{% endalert %}

{% tabs %}
{% tab Braze Standard REST %}
```json
// Uninstall: users.behaviors.Uninstall

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "card_id" : "(optional, string) ID of the card this in app message comes from"
  },
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) BSON ID of the user who performed this event",
    "external_user_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Uninstall: users.behaviors.Uninstall

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "\\$partner_id" : "braze",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "distinct_id" : "(required, string) External ID of the user",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "time" : "(required, int) Unix timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Cloud Storage (S3/Azure Blob/Google Cloud Storage) %}
```json
// Uninstall: users.behaviors.Uninstall

{
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(required, string) BSON ID of the user who performed this event"
}
```
{% endtab %}

{% tab mParticle %}
```json
// Uninstall: users.behaviors.Uninstall

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "event" : [
    {
      "data" : {
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "custom_attributes" : {
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred"
        },
        "timestamp_unixtime_ms" : "(required, int) Unix timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "events" : [
    {
      "data" : {
        "custom_attributes" : { }
      }
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) External ID of the user"
  }
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Uninstall: users.behaviors.Uninstall

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) Unix timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}

{% tab Segment %}
```json
// Uninstall: users.behaviors.Uninstall

{
  "context" : {
    "traits" : { },
    "device" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred"
  },
  "timestamp" : "(required, int) Unix timestamp at which the event happened",
  "type" : "track",
  "userId" : "(required, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}
