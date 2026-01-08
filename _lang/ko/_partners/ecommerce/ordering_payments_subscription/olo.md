---
nav_title: Olo
article_title: Olo
description: "This article outlines the partnership between Braze and Olo, a leading open SaaS platform for restaurants that enables hospitality at every touchpoint."
alias: /partners/olo/
page_type: partner
search_tag: Partner
---

# Olo

> [Olo](https://www.olo.com/) is a leading open SaaS platform for restaurants that enables hospitality at every touchpoint.

By integrating Olo and Braze, you can:

- Update user profiles in Braze to keep them consistent with Olo user profiles
- Send the right next best messaging from Braze based on Olo events

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Olo account | An Olo account with access to webhooks is required to take advantage of this partnership. Set up webhook subscriptions via the [self-service webhooks tool](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) within the Olo Dashboard. |
| Braze Data Transformation | A [Data Transformation URL]({{site.baseurl}}/data_transformation/) is necessary to receive data from Olo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

A webhook is a way for Olo to send event-driven information to Braze about users and their actions, including events like Order Placed, Guest Opt In, Order Picked Up and more. The Olo Webhook delivers the event to Braze generally within seconds of the action being performed.

## Disclaimer

In Olo, you're limited to one webhook per environment for each approved brand, all sent to the same **Destination URL**. Different brands can have different URLs, but events from the same brand must share a URL. In Braze, this means you can make only one transformation for use with Olo.

To handle multiple Olo events within this single transformation, look for the `X-Olo-Event-Type` header in each webhook. This header lets you conditionally process different Olo events.

## Integration

### Step 1: Set up the Braze Data Transformation to accept Olo's test event {#step-1}

{% multi_lang_include create_transformation.md location="default" %}

### Step 2: Set up Olo webhooks

Use the [self-service webhooks tool](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) within the Olo dashboard to set up webhooks to send to your Data Transformation.

1. Choose what events should be sent to Braze
2. Configure the **Destination URL**. This will be the Data Transformation URL created in [step 1](#step-1).

{% alert note %}
`OAuth` and the `X-Olo-Signature` header shared secret are not needed for the transformation.
{% endalert %}

{:start="3"}
3\. Verify that the webhook is configured correctly by sending a [Test Event](https://developer.olo.com/docs/load/webhooks#operation/test) to your Data Transformation. Only Olo Dashboard users with the [Developer Tools permission](https://olosupport.zendesk.com/hc/en-us/articles/115001427843-Dashboard-Permissions) can send Test Events.

Olo requires a successful response from the Test Event webhook before you will be able to complete the Olo webhook configuration process.

### Step 3: Write transformation code to accept your chosen Olo events

In this step, you will transform the webhook payload that will be sent from the source platform to a JavaScript object return value.

1. Send a request to your Data Transformation URL with a sample event payload of an Olo event you intend to support. See [request body format](#request-body-format) for help formatting your request.
2. Refresh your Data Transformation and make sure you can see the sample event payload in the **Webhook Details**.
3. Update your Data Transformation code to support your chosen Olo events.
4. Click **Validate** to return a preview of your code’s output and to check if it’s an acceptable `/users/track` request.
5. Save and activate your Data Transformation.

#### Request body format

This return value must adhere to Braze’s `/users/track` request body format:

- Transformation code is accepted in the JavaScript programming language. Any standard JavaScript control flow, such as if/else logic, is supported.
- Transformation code accesses the webhook request body via the payload variable. This variable is an object populated by parsing the request body JSON.
- Any feature supported in our `/users/track` endpoint is supported, including:
    - User attributes objects, event objects, and purchase objects
    - Nested attributes and nested custom event properties
    - Subscription group updates
    - Email address as an identifier

## Example Data Transformations for Olo webhooks

This section contains example templates that can be used as a starting point. Feel free to start from scratch, or to delete specific components as you see fit.

In each template the code defines a variable, `brazecall`, to build a `/users/track` request.

After the `/users/track `request is assigned to `brazecall`, you will explicitly return `brazecall` to create an output.

### Single event transformation

If you are only looking to support a single Olo event you will not need to use the `X-Olo-Event-Type` header to conditionally create the `/users/track` request payload. For example, logging a purchase event or a custom event to the user profile when an Olo Order Placed webhook is sent to Braze.

### Logging each product as a purchase

```javascript
// iterate through the items included within the order

const purchases = payload.items.map((item) => {
 return {
   external_id: payload.customer.customerId.toString(),
   product_id: item.productId.toString(),
   currency: 'USD',
   price: item.sellingPrice,
   time: new Date().toISOString(),
   quantity: item.quantity,
   properties: {
     customValues: item.customValues
   }
 };
});

// log a purchase per item in the order

let brazecall = {
 "purchases": purchases
};

return brazecall;
```

### Logging a custom event

```javascript
// log an event “Order Placed” to the profile that includes all items in the order as event properties.

let brazecall = { 
"events": [
   {
     "external_id": payload.customer.customerId.toString(),
     "_update_existing_only": false,
     "name": "Order Placed",
     "time": new Date().toISOString(),
     "properties": {
       "Delivery Method": payload.deliveryMethod,
       "Items": payload.items,
       "Total": payload.totals.total,
       "Location": payload.location.name
     }
   }
 ]
};

return brazecall;
```

## Multi-event transformation

Olo sends the event type within the `X-Olo-Event-Type` header of each webhook. To support multiple Olo webhook events within a single transformation, use conditional logic to transform the webhook payload based on the value of this header type.  

In the below transformation example, our JavaScript creates a particular payload for the events of `UserSignedUp` and `OrderPlaced`. Additionally, an `else` condition handles a payload for any Olo events sent to Braze without the X-Olo-Event-Type header of `UserSignedUp` and `OrderPlaced`.

```javascript
// captures the value within the X-Olo-Event-Type header for use in the conditional logic

let event_type = headers["X-Olo-Event-Type"];

// defines a variable 'brazecall' that will hold the request payload for the /users/track request

let brazecall;

// if the X-Olo-Event-Type header is 'UserSignedUp', define a variable for the different subscription statuses that could be included within the Olo event payload

if (event_type == "UserSignedUp") {
	let emailSubscribe;
	let emailSubscriptionGroup;
	let smsSubscriptionGroup;


// determine if the user has opted into marketing emails


	if (payload.allowEmail) {
		emailSubscribe = "opted_in";
		emailSubscriptionGroup = "subscribed";
	} else {
		emailSubscribe = "unsubscribed";
		emailSubscriptionGroup = "unsubscribed";
	}


	// determine if the user has opted into SMS


	if (payload.allowMarketingSms) {
		smsSubscriptionGroup = "subscribed";
	} else {
		smsSubscriptionGroup = "unsubscribed";
	}

	// build the /users/track request and pass in the appropriate subscription statuses


	brazecall = {
		"attributes": [{
			"external_id": payload.id.toString(),
			"_update_existing_only": false,
			"email": payload.emailAddress,
			"first_name": payload.firstName,
			"last_name": payload.lastName,
			"email_subscribe": emailSubscribe,
			"phone": payload.contactNumber,
			"subscription_groups": [{
					"subscription_group_id": "57e5307f-9084-490d-9d6d-8244dc919a48",
					"subscription_state": emailSubscriptionGroup
				},
				{
					"subscription_group_id": "6440ba26-86ea-47db-a935-6647941dc78b",
					"subscription_state": smsSubscriptionGroup
				}
			]
		}]
	}; // if the X-Olo-Event-Type header is 'OrderPlaced', build the /users/track request to log an event to the user profile
} else if (event_type == "OrderPlaced") {
	brazecall = {
		"events": [{
			"external_id": payload.customer.customerId.toString(),
			"_update_existing_only": false,
			"name": "Order Placed",
			"time": new Date().toISOString(),
			"properties": {
				"Delivery Method": payload.deliveryMethod,
				"Items": payload.items,
				"Total": payload.totals.total,
				"Location": payload.location.name
			}
		}]
	};
} else { // if the X-Olo-Event-Type header is anything else, build the /users/track request to log an event to the user profile
	brazecall = {
		"events": [{
			"external_id": payload.customer.customerId.toString(),
			"_update_existing_only": true,
			"name": "Another Event",
			"time": new Date().toISOString()
		}]

	};
}

// return `brazecall` to create an output.

return brazecall;
```

### Step 4: Publish your Olo webhook

After you have activated your Data Transformation in Braze, use the [self-service webhooks tool](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) within the Olo dashboard to publish your webhook. When the webhook is published, the Data Transformation will start to receive Olo webhook event messages.

## Things to know

### Retries

Olo will retry webhook calls resulting in an HTTP response status code of `429 - Too Many Requests` or in the `5xx` range (for example, because of a gateway timeout or server error), up to 50 times over a 24 hour period before dropping the request.

### At least once delivery

If a webhook call results in an HTTP response status code of `429 - Too Many Requests` or in the `5xx` range (for example, because of a gateway timeout or server error), Olo will retry the message up to 50 times over a 24 hour period before giving up.

Webhooks may therefore be received multiple times by a subscriber. It is up to the subscriber to ignore duplicates by checking the `X-Olo-Message-Id` header.


