---
nav_title: Zapier
alias: /partners/zapier/
---
# Zapier Integration

[Zapier] [1] is an automation tool that links software services together, similar to [IFTTT] [2] (if this then that) for enterprise software. Utilizing [Webhooks] [3] and [API Triggered Campaigns] [4], Braze can integrate with Zapier

### Step 1: Add Wordpress as a Trigger and select New Post after you connect your account:

![zapier1] [5]

### Step 2: When Post Status is Published:

![zapier2] [6]

### Step 3: Add an Action “Webhook”:

![zapier3] [7]

### Step 4: Choose Post as the Type:

![zapier4] [8]

### Step 5: Setup Braze Post:

URL : `https://rest.iad-01.braze.com/campaigns/trigger/send`

Payload Type : JSON

Data : `trigger_properties__name`, `api_key`, `campaign_id`

![zapier5] [10]

>  The above is an example for customers on the `US-01` instance. If you are not on this instance please refer to our [API documentation][66] to see which endpoint to make requests to.

## Step 6: Create Braze Campaign:

![zapier6] [12]

You can also use trigger_properties with Liquid to filter what or if the message is sent.

[1]: https://zapier.com/
[2]: https://ifttt.com/
[3]: {{ site.baseurl }}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook
[4]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/scheduling_your_campaign/#setting-up-an-api-triggered-campaign
[5]:{% image_buster /assets/img_archive/zapier1.png %}
[6]:{% image_buster /assets/img_archive/zapier2.png %}
[7]:{% image_buster /assets/img_archive/zapier3.png %}
[8]:{% image_buster /assets/img_archive/zapier4.png %}
[10]:{% image_buster /assets/img_archive/zapier5.png %}
[11]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/scheduling_your_campaign/#api-triggered-campaigns-server-triggered-campaigns
[12]:{% image_buster /assets/img_archive/zapier6.png %}
[66]: {{ site.baseurl }}/developer_guide/rest_api/messaging/#sending-messages-via-api-triggered-delivery
