---
nav_title: Quikly
article_title: Quikly
description: "This reference article outlines the partnership between Braze and Quickly, a urgency marketing platform, that allows you to accelerate conversions on events within a Braze customer journey."
alias: /partners/quikly/
page_type: partner
search_tag: Partner

---

# Quikly

> [Quikly](https://www.quikly.com), an urgency marketing platform, leverages psychology to motivate consumers, so brands can immediately increase response around their key marketing initiatives.

_This integration is maintained by Quikly._

## About the integration

The Braze and Quikly partnership allows you to accelerate conversions on events within a Braze customer journey. Quikly does this by using urgency psychology to motivate consumers in fun — and instant — ways. For example, brands can use Quikly to immediately acquire new email and SMS subscribers directly into Braze or to motivate other key marketing objectives like downloading your mobile app.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Quikly account | A [Quikly](https://www.quikly.com) brand partner account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track`, `subscription.status.set`, `users.export.ids`, and `subscription.status.get` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. |
| Quikly API key (optional) | A Quikly API key provided by your client success manager (webhook only). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

Quikly allows brands to accelerate email or SMS acquisition and motivates subscribers to provide first-party data directly within Braze. You can also use Braze to target lapsed customers with a Quikly activation that will reactivate and retain that audience. Additionally, marketers can use this integration to incentivize specific customer journey events with unique reward structures. 

For example:
 - Build anticipation and engagement over days as consumers opt-in for a chance to claim exciting rewards with [Quikly Hype](https://www.quikly.com/urgency-marketing/platform/product-overview/hype). First-party data is automatically pushed to Braze.
 - Accelerate acquisition of new email and SMS subscribers using unique, real-time offers based on a consumer's speed of response, rank against others, randomly, or before time or quantities run out with [Quikly Swap](https://www.quikly.com/urgency-marketing/platform/product-overview/swap).
 - Motivate specific steps in the customer journey with unique reward structures using webhooks.
 - Apply custom attributes or events to the user's profile upon participating in a Quikly activation.

## Integration

Outlined below are four different integrations: email acquisition, SMS acquisition, custom attributes, and webhooks. The integration you choose will depend on your Quikly activation and use case.

{% tabs %}
{% tab Email Acquisition %}

### Email Acquisition

If your Quikly activations collect customer email addresses or profile data, the only required step is to provide Quikly with your REST API key and endpoint. Quikly will configure your brand account to pass this data to Braze. If there are additional user attributes you'd like included, mention this when you provide the API credentials to Quikly.

Here is an outline of how Quikly executes this workflow.
1. Upon participating in a Quikly activation, Quikly schedules a user lookup using the [export API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) to see if a user exists with a given `email_address`.
2. Log or update the user.
  - If the user exists:
    - Do not create a new profile.
    - If desired, Quikly can log a custom attribute on the user's profile to indicate that the user participated in the activation.
  - If the user does not exist:
    - Quikly creates an alias-only profile via the Braze [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), setting the user's email as the user alias to reference that user in the future (as the user won't have an external ID).
    - If desired, Quikly can log custom events to indicate this profile participated in Quikly activation.

{% details /users/track request %}

#### Request headers
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### Request body
```
{
  "attributes": [{
    "_update_existing_only": false,
    "user_alias:": {
      "alias_name": "email@example.com",
      "alias_label: "email"
    },
    "email": "email@example.com"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab SMS Acquisition %}

### SMS subscriptions

Quikly activations can collect mobile phone numbers directly from customers and initiate a new SMS subscription. To enable this integration, provide your Quikly client success manager with the `subscription_group_id`. You can access a subscription group's `subscription_group_id` by navigating to the **Subscription Group** page.

Quikly will perform a subscription lookup using the customer's phone number and automatically credit them in the activation if an SMS subscription already exists. Otherwise, a new subscription will be initiated, and after the subscription status is verified, the customer will be credited.

Here is the complete workflow when a customer provides their mobile number and consent via Quikly:
1. Quikly performs a subscription lookup using the [subscription group status]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) to see if a given `phone` is subscribed to a `subscription_group_id`. If a subscription exists, credit the user in the Quikly activation. No further action is necessary.
2. Quikly performs a user lookup using the [Export user profile by identifier endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) to see if a user profile exists with a given `email_address`. If no user exists, create an alias-only profile via the Braze [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), setting the user's email as the user alias to reference that user in the future (as the user won't have an external ID).
3. Update the subscription status using the [Update user's subscription group status endpoint]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).

To support existing double opt-in SMS subscription workflows, Quikly can send a custom event to Braze rather than the workflow above. In that case, rather than updating the subscription status directly, the [custom event triggers the double opt-in process]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/) and the subscription status is periodically monitored to verify the user has fully opted-in before crediting them in the Quikly activation.

{% alert important %}
Braze advises that when creating new users via the `/users/track` endpoint, there should be a delay of about 2 minutes before adding users to the relevant subscription group to allow Braze time to fully create the user profile.
{% endalert %}

{% details Detailed /subscription/status/set request %}
#### Request headers
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### Request body
```
{
  "subscription_group_id": "the-id-of-the-subscription-group",
    "subscription_status": "subscribed",
    "phone": "+13135551212"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab Custom Attributes %}
### Custom attributes

Depending on your Braze implementation, you may want events within Quikly activation to cascade through Braze for further processing. For example, you may wish to apply a custom user attribute based on what level or incentive was achieved in Quikly activation, allowing you to display the relevant Content Card when they open your app or log in to your website. Quikly will work with you directly to implement these integrations.

{% endtab %}
{% tab Webhooks %}
### Webhooks
Use webhooks to trigger incentives for specific events in the customer journey. For example, if you have a Braze event for when a user logs into your app, turns on push notifications, or uses your store locator, you can use a webhook to trigger a custom offer to that user based on the configuration of a specific Quikly activation. Example tactics include rewarding the first X number of users who perform an action (such as logging into your app) with a custom offer or providing an offer that decreases in value as more time elapses to motivate an immediate response.

### Create a Quikly webhook in Braze

To create a Quikly webhook template for future campaigns or Canvases, navigate to **Templates** > **Webhook Templates** in the Braze platform. 

If you would like to create a one-off Quikly webhook campaign or use an existing template, select **Webhook** in Braze when creating a new campaign.

Select **Blank Template**, and enter the following for the webhook URL and request body:
- **Webhook URL**: https://api.quikly.com/webhook/braze
- **Request body**: JSON key/value pairs

#### Request headers and method

Quikly requires an `HTTP Header` for authorization.

- **HTTP Method**: POST
- **Request Header**:
  - **Authorization**: Bearer [PARTNER_AUTHORIZATION_HEADER]
  - **Content-Type**: application/json

#### Request body

Select ***JSON key/value pairs*** and add the following pairs:
{% raw %}
```
"q_scope": "your-activations-scope-id"
"event": "your-event-identifier"
"email": {{${email_address}}
```
{% endraw %}

### Preview your request

Preview your request in the **Preview** panel or navigate to the `Test` tab, where you can select a random user, an existing user, or customize your own to test your webhook.

{% alert important %}
Remember to save your template before leaving the page! <br>Updated webhook templates can be found in the **Saved Webhook Templates** list when creating a new [webhook campaign]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}

{% endtab %}
{% endtabs %}

## Support
Reach out to your client success manager at Quikly with any questions.


