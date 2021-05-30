---
nav_title: EventBridge Currents Connector
page_order: 0
alias: /partners/eventbridge_currents/

description: "This article outlines the partnership between Braze
Currents and AWS EventBridge, a real-time integration platform."
page_type: partner
tool: currents
---

# About EventBridge & Currents


> [AWS EventBridge](https://aws.amazon.com/eventbridge/)is a serverless event bus that makes it easier to build event-driven applications at scale using events generated from your applications, integrated Software-as-a-Service (SaaS) applications, and AWS services. EventBridge delivers a stream of real-time data from event sources such as Zendesk or Shopify to targets like AWS Lambda and other SaaS applications. You can set up routing rules to determine where to send your data to build application architectures that react in real- time to your data sources with event publisher and consumer completely decoupled.

To get started, find the following information from your AWS dashboard:

-   AWS Account ID
-   AWS Region


Add this information to the EventBridge integration page on the
dashboard, and press save. Braze will create a Partner Event Source,
which will be visible in your EventBridge UI as a "Pending" Partner
Event Source. To start receiving
events, go back to the EventBridge console and choose Partner event
sources in the navigation pane. Select the button next to the partner event source, and choose "Associate with event bus".


{% alert important %}
You must associate the Braze-created Partner Event Source with your
Event Bus in order to receive data. Event Sources that remain in a
pending state for more than one week will need to be re-created.
{% endalert %}

Amazon's documentation for setting up Partner Event Sources is available [here](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-saas-integration.html).

## Integration Details

All fields in all events are supported for EventBridge. Please refer
to the Currents Event Dictionary for a full list. At present, Braze
does not provide an EventBridge schema registry, and recommends using EventBridge's
schema discovery functionality.

Below is a sample event:
```json
{
    "event_type": "users.messages.sms.Delivery",
    "id": "a1234567-89ab-cdef-0123-456789abcdef",
    "time": 1477502783,
    "user": {
        "user_id": "0123456789abcdef01234567",
        "external_user_id": "user_id",
        "timezone": "America/Chicago"
    },
    "properties": {
        "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
        "canvas_name": "My Cool Canvas",
        "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
        "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
        "dispatch_id": "12345qwert",
        "to_phone_number": "+16462345678",
        "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
        "from_phone_number": "+12123470922"
    }
}
```

All events will contain:
-   event_type, to identify which event is being sent. Note that for
    Custom Events, the event_type will be
    "users.behaviors.CustomEvent", and the event name will be sent as
    the "name" property.
	-   "user" object with information about the user
	-   "properties" object with event-specific parameters. For events
    that support additional custom parameters, an additional object
    will be included within the "properties" object to reflect these properties.
	   - For Purchase events, this field is "purchase_properties" 
       - For Custom Events, this field is "custom_properties"


## Rate Limits

Currents connects to EventBridge's HTTP API, which has a
[Rate Limit](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-quota.html#eb-putevents-limits)
based on the integration's region. Above that threshold, EventBridge
will throttle events that are logged through Currents. If Braze
receives events above this rate limit, you may experience a delay
in event delivery.

[support]: {{site.baseurl}}/support_contact/
