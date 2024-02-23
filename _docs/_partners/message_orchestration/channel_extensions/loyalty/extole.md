---
nav_title: Extole
article_title: Extole
description: "This article outlines the partnership between Braze and Extole, a referral marketing company, that allows you to pull customer events and attributes from refer-a-friend and growth programs into Braze"
alias: /partners/extole/
page_type: partner
search_tag: Partner

---

# Extole

> [Extole][https://www.extole.com/], a SaaS company, is an industry leader in refer-a-friend marketing, helping create and optimize effective referral marketing programs to increase customer acquisition.

With the Braze and Extole integration, you can pull customer events and attributes from Extole refer-a-friend and growth programs into Braze, empowering you to create more personalized marketing campaigns that boost customer acquisition, engagement, and loyalty. You can also dynamically pull Extole content attributes, such as personalized share codes and links, into Braze communications.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Extole account | An Extole account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions can be created within your Braze Settings > REST API Key > Create New API Key. |
| Braze API URL | Your Braze API URL is specific to your Braze Instance. You can find it [here](https://www.braze.com/docs/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

The following use cases showcase a few ways you can leverage Extole’s integration with Braze. Work with your Extole implementation and customer success managers to develop an option that fits your company’s specific needs.

- Leverage custom events from your referral and engagement programs to trigger a Braze campaign or Canvas
- Create custom segments, dashboards, and reporting using data from your Extole-powered programs
- Automatically unsubscribe or subscribe users to your marketing list in Braze

## Integration

Complete the following steps to quickly get your integration up and running. Your Extole implementation and customer success managers will support you through this process and answer any questions you may have.

### Connect to Your Braze Account

1. Select the Braze integration on the [Partners](https://my.extole.com/partners) page of your My Extole account.
2. Within the Braze integration, hit the Install button to initiate the connection between Extole and Braze.
3. Fill out the required fields, starting with the Braze REST API key. The Braze REST API key can be created in your Braze account and should have the `users.track` option selected. This can be created within your Braze Settings > REST API Key > Create New API Key.
4. Enter your Braze API URL. This URL depends on which instance your Braze account is provisioned to. You can find it [here](https://www.braze.com/docs/api/basics/#endpoints).
5. Add any additional Extole events you'd like to send to Braze beyond the defaults. The default events, event properties, and user attributes are described in the [Extole Events table](https://dev.extole.com/docs/braze#extole-program-events) below.
6. Add any additional Reward states you'd like to send to Braze beyond the default `FULFILLED` state. Refer to the [Extole Rewards table](https://dev.extole.com/docs/braze#extole-rewards) below for a description of all available reward states.
7. Select your Braze External ID key mapping, which is how Extole updates user profiles in Braze. You can map the Braze External ID key to Extole's `email_address` or `partner_user_id` for the user.
8. Complete the connection by saving your settings. Once this is done, Extole events will be able to flow into your Braze account.

### Extole Program Events

Below are the default events, event properties, and user attributes that are sent into Braze. In addition to the default events listed here, you can add any other Extole events to your integration. Please work with your Extole Implementation or Customer Success Manager to identify and add any additional events you would like to send to Braze.

| Event | Description | Default Properties & User Attributes |
| ----------- | ----------- | ----------- |
| `extole_created_share_link` | A participant creates their share link by entering their email in the Extole Share Experience. | Event name  <br>Event time  <br>Partner (Extole)  <br>Email  <br>External ID  <br>Funnel (advocate or friend)  <br>Program  <br>First name  <br>Last name  <br>Share link |
| `extole_shared` | A participant shares their referral link with a friend. | Event name  <br>Event time  <br>Partner (Extole)  <br>Email  <br>External ID  <br>Funnel (advocate or friend)  <br>Program  <br>Share channel  <br>First name  <br>Last name |
| `subscribed` | A participant has opted-in to receive marketing messages. | Email  <br>List type  <br>External ID  <br>Email subscribe (opted in) |
| `unsubscribed` | A participant has opted-out of receiving Extole email communications.| Email  <br>External ID  <br>Subscription state (unsubscribed)  <br>Subscription group ID  <br>List type |
| `outcome` | A participant has converted or completed the desired outcome event configured for the program. | Event name  <br>Event time  <br>Partner (Extole)  <br>Email  <br>External ID  <br>Coupon code  <br>Attributed reward IDs  <br>Partner conversion ID  <br>Value (cart value)  <br>First name  <br>Last name  <br>Share link |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Extole Rewards

By default, Extole will send reward events in the `FULFILLED` state to Braze so that you can trigger reward notifications via a Braze campaign or canvas. See the table below for additional reward states you may be interested in sending from Extole to Braze.

| Reward State | Description | Default Properties & User Attributes |
| ----------- | ----------- | ----------- |
| `FULFILLED` - Default | The reward has been assigned a value (e.g., coupon, gift card, etc.) by an Extole reward supplier. | Event name  <br>Event time  <br>Partner  <br>Email  <br>Face value  <br>Coupon code  <br>Face value type  <br>First name  <br>Last name |
| `EARNED` | A reward has been created and associated with a person. | Event name  <br>Event time  <br>Partner  <br>Email  <br>Face value  <br>Coupon code  <br>Face value type  <br>First name  <br>Last name |
| `SENT` | The reward has been fulfilled and has been sent either via email or on a device to the recipient. | Event name  <br>Event time  <br>Partner  <br>Email  <br>Face value  <br>Coupon code  <br>Face value type  <br>First name  <br>Last name |
| `REDEEMED` | The reward has been used by the recipient, as evidenced in a conversion or  redemption event sent to Extole.| Event name  <br>Event time  <br>Partner  <br>Email  <br>Face value  <br>Coupon code  <br>Face value type  <br>First name  <br>Last name |
| `FAILED` | An issue has prevented the reward from being issued or sent, requiring attention. | Event name  <br>Event time  <br>Partner  <br>Email  <br>Face value  <br>Coupon code  <br>Face value type  <br>First name  <br>Last name |
| `CANCELED` | The reward has been deactivated and will return to inventory. | Event name  <br>Event time  <br>Partner  <br>Email  <br>Face value  <br>Coupon code  <br>Face value type  <br>First name  <br>Last name |
| `REVOKED` | The fulfilled reward has been invalidated. For example, Extole requested a gift card from a supplier and then subsequently determined that the card was sent in error. If the supplier supports revoking the reward, we would request the funds back and the reward would no longer be valid. | Event name  <br>Event time  <br>Partner  <br>Email  <br>Face value  <br>Coupon code  <br>Face value type  <br>First name  <br>Last name |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}


## Customization

### Lookup and Create Users in Braze

For certain use cases, such as a new email or SMS subscription where Extole does not have an external id (user id) for the user, Extole can check for the user's identifier using Braze's Export User by Identifier endpoint. If the user exists within Braze, Extole will add and update any profile attributes. If the request does not return a user profile, Extole will instead use the User Track endpoint to create a User Alias with the user's email address as the Alias Name.

## Using this integration

After connecting your accounts, events will automatically begin flowing from Extole to Braze without any action on your part. A live view of events being sent to Braze can be found in Extole’s Outbound Webhook Center for troubleshooting. 
