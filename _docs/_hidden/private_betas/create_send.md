---
nav_title: Canvas Delay Step
permalink: "/create_send/"
---

## Create and Send or Update and Send Via API Triggered Delivery

### Use Cases

When user information is sent to Braze via the users/track endpoint, it will occasionally take a few seconds for the user to be created in Braze's system or for the data to propagate to the user's profile. When requests are made to Braze's user track endpoint and Braze's messaging endpoints at around the same time, Braze cannot guarantee that the request to the user track endpoint will be processed before the request to the messaging endpoint. This can result in race conditions that impact messaging - for example a user may not yet have been created in Braze's system when a request to the campaigns/trigger/send endpoint is processed, resulting in the user not receiving an api-triggered push campaign. 

In certain cases, you'll want to guarantee that a user has been created or that new data has propagated to a user's profile before a message is sent to a user. 

For example, you might want to send an order confirmation to a customer that just registered. Because the user's email information is not yet in Braze, you'll want to make sure that Braze processes the user's email address before the order confirmation campaign is sent to them. 

Another example is ensuring that user attributes needed for campaign segmentation are processed before the campaign is sent. You might have a segment on your api triggered campaign that references an attribute value like gender, which is provided by the user during the registration process. If the attribute isn't updated on the user's profile before the campaign segmentation is evaluated, the user will not get the campaign. 

In order to guarantee that: 

- Users are created before a request to the campaigns/trigger/send endpoint is processed
- User attributes are updated before a request to the campaign/trigger/send endpoint is processed

You can leverage the attribute object in the campaigns/trigger/send endpoint. Attributes that are included in this object will be processed before Braze begins to send the campaign. If the ```send_to_existing_only``` flag is set to false, and an external_user_id or user_alias does not exist in Braze's database, Braze will create a user profile for the external_user_id or user_alias and process the associated attributes to the user profile before Braze begins to send the campaign. 

### Sending Messages via API Triggered Delivery

API Triggered Delivery allows you to house message content inside of the Braze dashboard, while dictating when a message is sent, and to whom via your API. Please see this section of [Braze Academy for further details][39].

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/campaigns/trigger/send`
US-02 | `https://rest.iad-02.braze.com/campaigns/trigger/send`
US-03 | `https://rest.iad-03.braze.com/campaigns/trigger/send`
US-04 | `https://rest.iad-04.braze.com/campaigns/trigger/send`
US-06 | `https://rest.iad-06.braze.com/campaigns/trigger/send`
EU-01 | `https://rest.fra-01.braze.eu/campaigns/trigger/send`

##### Campaigns

```json
POST https://YOUR_REST_API_URL/campaigns/trigger/send
Content-Type: application/json
{
  "api_key": (required, string) see App Group REST API Key,
  "campaign_id": (required, string) see Campaign Identifier,
  "send_id": (optional, string) see Send Identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to entire segment targeted by the campaign) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External Id of user to receive message,
      "trigger_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with trigger_properties above),
      // When "send_to_existing_only" is true Braze will only send the message to existing users. When "send_to_existing_only" is false and a user with the given id does not exist, Braze will create a user with that id and attributes before sending the message. 
"send_to_existing_only": (optional, boolean) defaults to true,
     // When "send_to_existing_only" is set to true attributes will only be created or updated for existing users 
"attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent. Note that existing values will be overwritten. 
    },
    ...
  ]
}
```
For more information on the "broadcast" flag, see [Broadcast][1].

[1]: {{ site.baseurl }}/api/endpoints/messaging/#broadcast