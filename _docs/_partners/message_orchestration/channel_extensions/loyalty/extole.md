---
nav_title: Extole
article_title: Extole
description: "This reference article outlines the partnership between Braze and Extole, a referral marketing company, that allows you to pull customer events and attributes from refer-a-friend and growth programs into Braze"
alias: /partners/extole/
page_type: partner
search_tag: Partner

---

# Extole

> [Extole][1], a SaaS company, is an industry leader in refer-a-friend marketing, helping create and optimize effective referral marketing programs to increase customer acquisition.

With the Braze and Extole integration, you can pull customer events and attributes from Extole refer-a-friend and growth programs into Braze, empowering you to create more personalized marketing campaigns that boost customer acquisition, engagement, and loyalty. You can also dynamically pull Extole content attributes, such as personalized share codes and links, into Braze communications.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Extole account | An Extole account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze test REST API key (optional) | A test API key that can be used for testing purposes if you'd like these requests sent to a separate staging Braze instance. |
| Braze instance | Your Braze instance can be obtained from your Braze onboarding manager or can be found on the [API overview]({{site.baseurl}}/api/basics/#endpoints) page. |
| User identity | The unique identifier for a user in Braze and Extole. This is generally the `external_id`. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

The following use cases showcase a few ways you can leverage Extole's integration with Braze. Work with your Extole implementation and customer success managers to develop an option that fits your company's specific needs.
- Turn every customer into an advocate by including their unique share link in Braze communications.
- Continue the conversation with site visitors by triggering a personalized welcome campaign when they opt-in to receive marketing communications in Extole-powered programs.
- Promote further engagement by triggering a product recommendations campaign when an advocate shares a specific product with a friend.
- Thank advocates for bringing you new, high-quality customers by triggering a "surprise and delight" campaign when they have driven five or more referrals.
- Trigger a refer-a-friend email, push, or SMS campaign during any moment of customer delight, such as a purchase or positive experience with your brand.

## Integration

Complete the following steps to get your integration up and running quickly. Your Extole implementation and customer success managers will support you through this process.

### Step 1: Define event names and attributes 

Any event that Extole tracks can be sent to Braze. Work with your Extole implementation or client success manager to identify the event names and user attributes you'd like to send into Braze or select from the default options in the tables below. Your Extole implementation or client success manager will then map and configure the event names in the Extole dashboard.

#### Event names

| Event name | Description |
| ----------- | ----------- |
| Created Share Link | A share link is created for a customer. |
| Shared | A customer sends a link to their friend(s) via email, SMS, or social channel. |
| Referred Signed Up | A referred customer signs up via email or SMS through the program. |
| Referred Converted | A referred customer completes a purchase. Note that outcome events can be customized for your business.|
| Subscribed | A customer subscribes via email or SMS. |
| Unsubscribed | A customer unsubscribes via email or SMS. |
| Earned Reward | A customer earns a reward. |
{: .reset-td-br-1 .reset-td-br-2}

#### Attribute names

| Attribute name | Description | Example | 
| -------------- | ----- | ------- |
| `external_id` (required) | The unique identifier for the customer, such as a user ID. | User ID |
| `email` | The customer's email address. | jsmith@yourcompany.com |
| `phone_number` | The customer's phone number, including country code. | +15555555555 |
| `share_link` | The customer's personal share link. | refer.yourcompany.com/jsmith |
| `first_name` | The customer's first name. | John |
| `last_name` | The customer's last name. | Smith |
| `city` | The customer's city, spelled out. | Boston |
| `state` | The customer's state, abbreviated. | MA |
| `country` | The customer's country, abbreviated. | US |
| `funnel` | The correct funnel type for the customer. | friend or advocate |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Step 2: Connect to your Braze account 

To start sending data from your Extole programs into Braze, create a new webhook integration in Extole's outbound webhook center.


1. Navigate to **Tech Center > Outbound Webhooks** in your My Extole account and click on the **+ New Integration** button.
2. Enter a key name (i.e., how you'd like to refer to the key in Extole) and select **Webhook** as the key type. 
3. In the partner key ID field, add a value that you will recognize for this credential (e.g., your account ID, email address, or user ID).
4. Select `PASSWORD` from the algorithm drop-down.
5. Add your Braze REST API key to the key field and click **Create Key**.<br><br>![][4]{: style="max-width:80%;"}

Next, work with your Extole success or implementation manager to create a new webhook. They will configure the webhook for you using your newly generated key and Braze instance URL.<br><br>![][5]{: style="max-width:80%;"}

## Customization

### Configure a staging API key for testing

If you only provide one Braze REST API key to Extole, only production events will be sent to Braze. If you also want to send staging or testing events, create another Braze REST API key and configure an additional webhook integration in the Extole dashboard.

### Creating a new user alias

For certain use cases, such as a new email or SMS subscription where Extole does not have an external ID (user ID) for the user, Extole can check for the user's identifier using Braze's [export user by identifier endpoint][2]. If the user exists within Braze, Extole will add and update any profile attributes. If the request does not return a user profile, Extole will instead use the [user track endpoint][3] to create a user alias with the user's email address as the alias name.

## Using this integration

After connecting your Braze account to the Extole dashboard, events will automatically begin flowing from Extole to Braze. A live view of events being sent to Braze can be found in Extole's outbound webhook center for troubleshooting. 

![][6]

Once the events and attributes you have configured are flowing into Braze, you can use the data to generate Braze audiences and campaign segmentation.

[1]: https://www.extole.com
[2]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[3]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/#request-body
[4]: {% image_buster /assets/img/extole/extole-outbound-webhooks.png %}
[5]: {% image_buster /assets/img/extole/extole-add-new-webhook.png %}
[6]: {% image_buster /assets/img/extole/extole-webhook-live-events.png %}