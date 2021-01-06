---
nav_title: Zapier
alias: /partners/zapier/
---
# Zapier Integration

[Zapier][1] is an automation web tool that allows you to share data between web apps, and then use that information to automate actions. You can use the Braze platform's API endpoints and [webhooks][3] to connect with third-party applications—such as Google Workplace, Slack, Salesforce, etc—and automate a variety of actions.


In the Zapier example below, we'll be sending information from Wordpress to Braze using a POST webhook. We'll then use that information to create a Braze campaign. 


### Step 1: Add WordPress as a Trigger and select New Post after you connect your account:

Using Zapier's terminology, a "zap"  is an automated workflow that connects your apps and services together. The first part of any zap is to designate a trigger. Once your zap is enabled, whenever your trigger is detected, Zapier will automatically perform its respective actions.

Using our Wordpress example, we'll set up our trigger as a published Wordpress post.

![zapier1] [5]

![zapier2] [6]

### Step 3: Add an Action “Webhook”:

The second part of any zap is the action. When your zap is enabled and your trigger is detected, the action will automatically occur. 

Using the same example, our action will send a POST request as a JSON to a Braze endpoint. 

![zapier3] [7]

### Step 4: Choose Post as the Type:

![zapier4] [8]

### Step 5: Setup Braze Post:

URL : `https://rest.iad-01.braze.com/campaigns/trigger/send`

Payload Type : JSON

Data : `trigger_properties__name`, `api_key`, `campaign_id`
These data fields are key value pairs that will for the data portion of the request.

![zapier5] [10]

>  The above is an example for customers on the `US-01` instance. If you are not on this instance please refer to our [API documentation][66] to see which endpoint to make requests to.

## Step 6: Create a Braze Campaign:

![zapier6] [12]

Once you've successfully set up your zap, you can now use that information you're being sent to customize your campaign and send off any messages. You can also use trigger_properties with Liquid to filter what or if the message is sent.

[1]: https://zapier.com/
[2]: https://ifttt.com/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/scheduling_your_campaign/#setting-up-an-api-triggered-campaign
[5]:{% image_buster /assets/img_archive/zapier1.png %}
[6]:{% image_buster /assets/img_archive/zapier2.png %}
[7]:{% image_buster /assets/img_archive/zapier3.png %}
[8]:{% image_buster /assets/img_archive/zapier4.png %}
[10]:{% image_buster /assets/img_archive/zapier5.png %}
[11]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/scheduling_your_campaign/#api-triggered-campaigns-server-triggered-campaigns
[12]:{% image_buster /assets/img_archive/zapier6.png %}
[66]: {{site.baseurl}}/developer_guide/rest_api/messaging/#sending-messages-via-api-triggered-delivery
