---
nav_title: Best Practices
hidden: true
layout: dev_guide
---

# User lifecycle and identifiers best practices

## Data collection

Learn more about how Braze collects data:
- [SDK data collection]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/)
- [Data collection best practices]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/)
- [User profile lifecycle]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/)

## Braze identifiers

- `Braze_id`: A Braze-assigned identifier that is unchangeable and associated with a particular user when created within our database. 
- `External_id`: A customer-assigned identifier, typically a UUID. We recommend customers assign the `external_id` once the user can be uniquely identified. Once a user is identified, they cannot be reverted to anonymous.
- `User_alias`: A unique alternate identifier that the customer can assign as a means of referencing the user by an ID before an `external_id` being assigned. User aliases can later be merged with other aliases or an `external_id` when one becomes available through Braze’s [User identify](https://www.braze.com/docs/api/endpoints/user_data/post_user_identify/) endpoint.
    - Within the [User identify](https://www.braze.com/docs/api/endpoints/user_data/post_user_identify/) endpoint the `merge_behavior` field can be used to specify what data from the user alias profile should persist on the known user profile.
    - Note: For the User Alias to be a sendable profile, you must still include email and/or phone as a standard attribute on the profile.
- `Device_id`: An automatically generated, device-specific identifier. A user profile can have a number of `device_ids` associated with it. For example, a user who has logged in to their account on their work computer, home computer, tablet, and iOS app would have 4 `device_ids` associated with their profile.
- Email Address (in Early Access):
    - Supported as an identifier in Braze’s track user endpoint. 
    - When using the email address as the identifier within a request, there are three possible outcomes:
        - If a user with this email address does not exist within Braze, an email-only user profile will be created, and any data in the request will be added to the profile.
        - If a profile with this email address already exists within Braze, it will be updated to include any data sent within the request.
        - In a use case with more than one profile with this email address, the most recently updated profile will be prioritized.
    - Note: if an email-only user profile exists and then an identified profile with the same email address is created (i.e., another profile with the same email address AND an external ID), Braze will create a second profile. Subsequent updates will go to the profile with the external ID.
        - Braze is working on adding a new API endpoint to allow customers to identify an email-only profile and merge data from the email-only profile into the identified profile.

## Handling anonymous users

For a use case where you need to create/update a user profile in Braze without having access to an `external_id`, another identifier like an email address or phone number can be passed into Braze's [Export user by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) endpoint to determine if a profile for the user exists within Braze. 

```json
{
 "email_address": "test@braze.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

If a user exists within Braze with that email/phone, their profile will be returned. Otherwise, an empty "users" array will be returned. The benefit of using the export endpoint to determine if a user with that email address already exists is that this will allow you to determine if any anonymous user profiles are associated with the user. For example, an anonymous profile created via the SDK (which will have `braze_id`) or a previously created User Alias profile. 

If the request does not return a user profile, you can choose to either create a User Alias or create an Email-Only user:

### User alias

Use the user track endpoint to create a User Alias, using your chosen identifier as the Alias Name. By including `_update_existing_only` as false within the attribute, event, or purchase object where the new user alias is defined, you can create the alias profile and add attributes, events, and purchases to that profile simultaneously. 

In order for the User Alias to be a sendable profile, you must include the email address in the “email” field, as shown below.

```json
{
   "attributes": [
   {
     "user_alias" : {
       "alias_name" : "test@braze.com",
       "alias_label" : "email"
     },
     "email": "test@braze.com",
     "_update_existing_only": false,
     "string_attribute": "sherman",
     "boolean_attribute_1": true,
     "integer_attribute": 25,
     "array_attribute": ["banana", "apple"]
   }
   ]
}
```

You can later identify and merge this user alias with an `external_id` when one becomes available through our [Identify users](https://www.braze.com/docs/api/endpoints/user_data/post_user_identify/) endpoint. 

### Creating an email-only user

Use the email address as the identifier in the user track endpoint 

```json
{
    "attributes": [
        {
            "email": "test@braze.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}
```
{% alert note %}
This functionality is currently in early access.
{% endalert %}

## Syncing data to user profiles

[User track](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/)
- This is a publicly accessible endpoint that can create and update users in Braze, such as logging attributes to the user profile. As a note, this endpoint has a rate limit of 50K RPM applied at the app group level.
- When using this endpoint, include the `partner` key as shown in our Partner documentation.

[Cloud Data Ingestion](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/#what-is-cloud-data-ingestion)
- Similar to the Track User endpoint, data can be synced to user profiles through Cloud Data Ingestion. When using this tool, attributes, events, and purchases are logged to profiles by setting up and connecting the data warehouse table/view you would like to sync to the desired Braze app group.

[Data points](https://www.braze.com/docs/user_guide/onboarding_with_braze/data_points#data-points)
- Braze has a data point consumption model where data points are incurred per “write” to the user profile regardless of whether the value has changed. For this reason, we recommend that only those attributes that have changed are sent to Braze. 

## Sending audiences of users to braze

[Cohort import sync partner documentation](https://www.braze.com/docs/partners/isv_partners/cohort_import/)<br>
- Audiences of users can be synced to Braze as a cohort using Braze’s Cohort Import API endpoints. Rather than these audiences being stored on the user profile as user attributes, customers can build and target this cohort through a Partner branded filter within our Segmentation tool. This can make finding and targeting a particular segment of users easier and more simple for customers.
- Cohort Import endpoints are not public and are specific to each Partner. For this reason, syncs to the cohort endpoints will not count toward a customer’s app group rate limits. 

[User track](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/)<br>
- This is a publicly accessible endpoint that can be used immediately to create users in Braze by denoting a user in a particular audience through a user attribute! The primary difference between this endpoint and the cohort import endpoint is that audiences sent using this endpoint would be stored on the user profile, whereas the cohort import endpoint would show as a filler in our segmentation tool. It is also worth noting that customers have a rate limit of 50k rpm on this endpoint. 
- When using this endpoint, ensure that you are including the `partner` key as shown in our [Partner documentation](https://www.braze.com/docs/partners/isv_partners/api_partner).

[Data points](https://www.braze.com/docs/user_guide/onboarding_with_braze/data_points#data-points)<br>
- Braze has a data point consumption model where data points are incurred per “write” to the user profile regardless of if the value has changed.
- Data points are incurred by both cohort import and the Track User endpoints.

## Engagement analytics streaming to partner

### Currents

Currents is Braze's near real-time message engagement analytics streaming tool. This will stream user-level data on all sends, deliveries, opens, clicks, etc., for campaigns and Canvases sent from the customer's app group. A couple of things to note: Currents are priced per connector for the customer, so all-new Currents Partners must go through an EA process. We ask that our Partners have five customers as part of the EA before we build the custom-branded UI and publicly make the connector available. 
- [Partner documentation](https://www.braze.com/docs/partners/isv_partners/currents_integration/)
- [Message Engagement Events](https://www.braze.com/docs/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events) - all customers who purchase a Currents connector will have access to these events.
- [User Behavior Events](https://www.braze.com/docs/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events) - not all customers who purchase a Current connector will purchase an "all events" connector that will include these events. 

### Snowflake Data Share

Customers who purchase a Snowflake Data Share connector will automatically have access to both Message Engagement and User Behavior events. When Snowflake Data Share is used as a Partner integration, Braze will provision a share to the Partner’s Snowflake instance on behalf of the customer. As a note, cross-region data share is a higher price-point for our customers, so we ask that Partners who want to integrate with Snowflake the guidance that they need an account in `US-EAST-1` and/or `EU-CENTRAL-1`
- [Partner documentation](https://www.braze.com/docs/partners/isv_partners/currents_integration/)

## Building and triggering campaigns and Canvases

### Creating assets in Braze
Braze offers a number of endpoints that allow customers and Partners to create/update email templates and content blocks within a customer’s app group. These templates and content blocks can, in turn, be used across the customer’s Braze campaigns and Canvases.
- Email Templates
    - [Create template endpoint]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)
    - [Update template endpoint]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/#rate-limit)
- [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) 
    - [Create content block endpoint]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
    - [Update content block endpoint]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)

### API-triggered campaigns and Canvases

Customers can set up campaigns and Canvases to be API-triggered. The API requests to trigger these campaigns can be used to further personalize and segment the campaign by passing in API-trigger properties and audience or recipient parameters. 
- [Triggering campaigns via API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body)
    - Campaigns are singular messages, such as an individual emails.
- [Triggering Canvases via API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#request-body)
    - Canvas is a unified interface where marketers can create campaigns with multiple messages and steps to form a cohesive journey. When triggering a Canvas, you are entering a user into the Canvas flow, where they will continue to receive messaging until they no longer fit the Canvas criteria. 
- [API trigger properties/Canvas entry properties]({{site.baseurl}}/api/objects_filters/trigger_properties_object) 
    - Data that can be dynamically populated into the message at the time of sending.

### API campaigns
When creating API campaigns (different from the API-triggered campaigns referenced above), the Braze dashboard is only used to generate a `campaign_id`, which lets the customer track analytics for campaign reporting. The campaign message itself is defined within the API request. 
- [Send API campaign immediately](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_messages/)
- [Schedule an API campaign](https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/)

### Send IDs
Use Braze's endpoint to generate a send ID which can be used to break down campaign analytics by send. For example, if a `campaign_id` (API campaign) is created per location, a send ID could be generated per send to track how well different messaging is performing for a particular location. 
- [Send IDs](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_create_send_ids/)

## Connected Content

Connected Content can be used within any channel type to make an API request to the specified endpoint at time-of-send and populate what is returned in the response into the message.

Connected Contents' versatility makes this a feature used by many of our customers to insert content that doesn't or can't live in Braze. Some of the more common use cases we see are:
- Templating blog or article content into messages
- Content recommendations
- Product metadata
- Localization and translation

Things to be aware of:
- Braze does not charge for API calls and will not count towards your data point allotment.
- There is a default limit of 1 MB for Connected Content responses. This default limit can be increased upon request. Reach out to your customer success manager for more information.
- Connected Content calls will happen when the message is sent, except for in-app messages, which will make this call when the message is viewed.
- Connected Content calls do not follow redirects.Braze requires that server response time is less than 2 seconds for performance reasons; if the server takes longer than 2 seconds to respond, the content will not be inserted.
- Braze’s systems may make the same Connected Content API call more than once per recipient. That is because Braze may need to make a Connected Content API call to render a message payload, and message payloads can be rendered multiple times per recipient for validation, retry logic, or other internal purposes. 

Refer to these articles to learn more about Connected Content:
- [Making a Connected Content call][1]
- [Aborting Connected Content][2]
- [Connected Content retries][3]

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries
