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

With the integration between Extole and Braze, you can pull valuable customer insights from your refer-a-friend and growth programs into Braze, empowering you to create more personalized marketing campaigns that boost customer acquisition, engagement, and loyalty. You can also dynamically pull content attributes, such as personalized share codes and links, into Braze communications to turn every customer into a brand advocate.

[Learn more about Extole][1].

## Prerequisites

The table below lists the prerequisites you need to complete this partnership integration.

| Requirement | Description |
| ----------- | ----------- |
| Extole Account | An Extole account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST test API key (optional) | A test API key that can be used for testing purposes if you’d like these requests sent to separate a staging Braze instance. |
| Braze Instance | Your Braze instance can be obtained from your Braze onboarding manager or can be found on the API overview page. |
| User Identity | The unique identifier for a user in Braze and Extole. This is generally the external_id. |

## Use cases

Discover typical use cases for an integration between Extole and Braze.
- Turn every customer into an advocate by including their unique share link in all Braze communications.
- Trigger a personalized welcome campaign when a customer opts in to receive marketing communications in an Extole-powered program.
- Trigger a product recommendations campaign when an advocate shares a specific product with a friend.
- Trigger a surprise and delight campaign when an advocate has driven five or more referrals. 
- Trigger a refer a friend email, push, or SMS campaign when a customer converts.

## Integration

### Step 1: Define event names and attributes 

Any event that Extole tracks can be sent to Braze. Please work with your implementation or client success manager to identify the event names and user attributes that you’d like for Extole to send into Braze, or select from the default options in the tables below. Your Extole implementation or client success manager will then map and configure the event names in the Extole dashboard for you.

| Event Name | Description |
| ----------- | ----------- |
| Created Share Link | A share link is created for a customer. |
| Shared | A customer sends a link to their friend(s) via email, SMS, or social channel. |
| Signed Up | A customer signs up via email or SMS through the program. |
| Converted | A customer completes a purchase. |
| Subscribed | A customer subscribes via email or SMS. |
| Unsubscribed | A customer unsubscribes via email or SMS. |
| Earned Reward | A customer earns a reward. |

| Attribute Name | Value |
| ----------- | ----------- |
| external_id (required) | The unique identifier for the customer, such as a user ID |
| email | The customer's email address<br><br>"jsmith@yourcompany.com" |
| phone_number | The customer's phone number, including country code<br><br>"+15555555555" |
| share_link | The customer’s personal share link<br><br>"refer.yourcompany.com/jsmith" |
| first_name | The customer's first name<br><br>"John" |
| last_name | The customer's last name<br><br>"Smith" |
| city | The customer's city, spelled out<br><br>"Boston" |
| state | The customer's state, abbreviated<br><br>"MA" |
| country | The customer's country, abbreviated<br><br>"US" |
| funnel | The correct funnel type for the customer<br><br>"friend" and/or "advocate" |

### Step 2: Connect to your Braze account 

To start sending data from your Extole programs into your Braze account, you’ll need to create a new webhook integration in Extole’s Outbound Webhook Center.
1. Navigate to Tech Center > Outbound Webhooks in the Extole dashboard and select Create New Integration.
2. Enter a name for the Key and select “Webhook” as the Key Type. 
3. Add your Braze REST API key to the Partner Key ID, select HTTP_BASIC as the algorithm, and click “Create Key.”

![extole-outbound-webhooks][2]

Work with your client success or implementation manager to create a new webhook. They will configure the webhook for you using your newly generated key and Braze instance URL. 

![extole-add-new-webhook][3]

## Customization

### Configure a staging API key for testing

If you only provide one Braze REST API key to Extole, only production events will be sent from Extole to Braze. If you also want to send staging / testing events, create another Braze REST API key and configure an additional webhook integration in the Extole dashboard.

## Using this integration

After connecting your Braze account in the Extole dashboard, events will automatically begin flowing from Extole to Braze without any action on your part. A live view of events being sent to Braze can be found in Extole’s Outbound Webhook Center for troubleshooting. 

![extole-add-new-webhook][3]

Once the events and attributes you and your integration or customer success manager have configured are flowing into Braze, you can use the data to generate Braze audiences and campaign segmentation.

[1]: https://www.extole.com
[2]: {% image_buster /assets/img/extole/extole-outbound-webhooks.png %}
[3]: {% image_buster /assets/img/extole/extole-create-new-webhook.png %}
