---
nav_title: Extole
article_title: Extole
page_order: 1

description: "With the integration between Extole and Braze, you can pull valuable customer insights from your refer-a-friend and growth programs into Braze, empowering you to create more personalized marketing campaigns that boost customer acquisition, engagement, and loyalty."
alias: /partners/extole/

page_type: partner
search_tag: Partner
hidden: true

---

# Extole

Marketers use Extole to turn their customers into a primary vehicle for acquisition, awareness, and activation. With Extole’s SaaS platform and experts, marketers rapidly launch programs such as refer-a-friend, influencer, and challenges, personalized to important behavioral segments. Customer-Led Growth drives revenue and generates a significant and unique source of first-party data.

With the integration between Extole and Braze, you can pull valuable customer insights from your refer-a-friend and growth programs into Braze, empowering you to create more personalized marketing campaigns that boost customer acquisition, engagement, and loyalty. You can also dynamically pull Extole content attributes, such as personalized share codes and links, into Braze communications to turn every customer into a brand advocate.

[Learn more about Extole][1].

## Prerequisites

The table below lists the prerequisites you need to complete this partnership integration.

| Requirement | Description |
| ----------- | ----------- |
| Extole Account | An Extole account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST test API key (optional) | A test API key that can be used for testing purposes if you’d like these requests sent to a separate staging Braze instance. |
| Braze Instance | Your Braze instance can be obtained from your Braze onboarding manager or can be found on the API overview page. |
| User Identity | The unique identifier for a user in Braze and Extole. This is generally the external_id. |

## Use cases

The following use cases exemplify just a few of the ways you can leverage Extole's integration with Braze. Work with your implementation and customer success managers to develop an option that fits your company's specific needs.
- Turn every customer into an advocate by including their unique share link in all Braze communications. A personal share link is how an advocate shares your brand with their friends, family, and followers. These Extole-generated links also attribute activity from an advocate's network back to the advocate. Include a customer's personal link in any communications you have with them so that they're just a copy-and-paste away from continuing to share your brand.
- Make opting in to receive marketing communications in Extole-powered programs more meaningful for customers by triggering a personalized welcome campaign.
- Promote further engagement by triggering a product recommendations campaign when an advocate shares a specific product with a friend.
- Thank advocates for bringing you new, high-quality customers by triggering a surprise and delight campaign when they have driven five or more referrals. 
- When a customer converts, capitalize on the excitement by triggering a refer-a-friend email, push, or SMS campaign.

## Integration

Complete the following steps to quickly get your integration up and running. Your Extole implementation and customer success managers will support you through this process and answer any questions you may have.

### Step 1: Define event names and attributes 

Any event that Extole tracks can be sent to Braze. Please work with your implementation or client success manager to identify the event names and user attributes that you’d like Extole to send into Braze, or select from the default options in the tables below. Your Extole implementation or client success manager will then map and configure the event names in the Extole dashboard for you.

| Event Name | Description |
| ----------- | ----------- |
| Created Share Link | A share link is created for a customer. |
| Shared | A customer sends a link to their friend(s) via email, SMS, or social channel. |
| Referred Signed Up | A referred customer signs up via email or SMS through the program. |
| Referred Converted | A referred customer completes a purchase.<br><br> Note: Outcome events can be customized for your business.|
| Subscribed | A customer subscribes via email or SMS. |
| Unsubscribed | A customer unsubscribes via email or SMS. |
| Earned Reward | A customer earns a reward. |

| Attribute Name | Value |
| ----------- | ----------- |
| external_id (required) | The unique identifier for the customer, such as a user ID |
| email | The customer's email address<br>Ex. "jsmith@yourcompany.com" |
| phone_number | The customer's phone number, including country code<br>Ex. "+15555555555" |
| share_link | The customer’s personal share link<br>Ex. "refer.yourcompany.com/jsmith" |
| first_name | The customer's first name<br>Ex. "John" |
| last_name | The customer's last name<br>Ex. "Smith" |
| city | The customer's city, spelled out<br>Ex. "Boston" |
| state | The customer's state, abbreviated<br>Ex. "MA" |
| country | The customer's country, abbreviated<br>Ex. "US" |
| funnel | The correct funnel type for the customer<br>Ex. "friend" and/or "advocate" |

### Step 2: Connect to your Braze account 

To start sending data from your Extole programs into your Braze account, you’ll need to create a new webhook integration in Extole’s Outbound Webhook Center.
1. Navigate to Tech Center > Outbound Webhooks in the Extole dashboard and select + New Integration.
2. Enter a name for the Key and select “Webhook” as the Key Type. 
3. Add your Braze REST API key to the Partner Key ID, select HTTP_BASIC as the algorithm, and click “Create Key.”

![extole-outbound-webhooks][4]

Work with your client success or implementation manager to create a new webhook. They will configure the webhook for you using your newly generated key and Braze instance URL. 

![extole-add-new-webhook][5]

## Customization

### Configure a staging API key for testing

If you only provide one Braze REST API key to Extole, only production events will be sent from Extole to Braze. If you also want to send staging / testing events, create another Braze REST API key and configure an additional webhook integration in the Extole dashboard.

### Creating a new User Alias

For certain use cases, such as a new email or SMS subscription where Extole does not have an external id (user id) for the user, Extole can check for the user's identifier using Braze's [Export User by Identifier endpoint][2]. If the user exists within Braze, Extole will add and update any profile attributes. If the request does not return a user profile, Extole will instead use the [User Track endpoint][3] to create a User Alias with the user's email address as the Alias Name.

## Using this integration

After connecting your Braze account in the Extole dashboard, events will automatically begin flowing from Extole to Braze without any action on your part. A live view of events being sent to Braze can be found in Extole’s Outbound Webhook Center for troubleshooting. 

![extole-webhook-live-events][6]

Once the events and attributes you and your integration or customer success manager have configured are flowing into Braze, you can use the data to generate Braze audiences and campaign segmentation.

[1]: https://www.extole.com
[2]: https://www.braze.com/docs/api/endpoints/export/user_data/post_users_identifier/
[3]: https://www.braze.com/docs/api/endpoints/user_data/post_user_track/#request-body
[4]: {% image_buster /assets/img/extole/extole-outbound-webhooks.png %}
[5]: {% image_buster /assets/img/extole/extole-add-new-webhook.png %}
[6]: {% image_buster /assets/img/extole/extole-webhook-live-events.png %}
