---
nav_title: Notify
article_title: Notify
description: "This reference article outlines the partnership between Braze and Notify, a real-time, omnichannel personalization solution that offers personalization across the customer lifecycle. Use Notify with Braze's Connected Content partner to easily drive marketing pressure and orchestrate in omnichannel"
alias: /partners/notify/
page_type: partner
search_tag: Partner
layout: dev_guide

---

<!-- In most cases, the ARTICLE_TITLE will be your company name. If your tool requires several seperate pages on Braze Docs, you can add a relevant page descriptor to your title, such as "MyCompany Analytics." -->
# Notify

<!-- The description starts with a '>' character and contains an introduction to your company, a link to your main site, and a consice overview of your integration. In a following paragraph, highlight the the relationship between your company and Braze and how this partnership helps your customers. -->
> 
Notify is an AI software, connected to CRM's tools, to help drive marketing pressure and orchestrate in omnichannel.
<br><br>
Giving access to exclusives futures such as : individualized perfect timing activation, sleepers awakeness, marketing pressure management, omnichannel orchestration (email, sms, push app, push web, wallet, whatsapp, ...) and carbon footprint reduction.
<br><br>
 We currently work in France and abroad (Europe + USA) with more than 100 brands from different sectors. 

<!-- Most partner integrations will require the following prerequisites. However, you may add additional prerequisites as needed. -->
## Prerequisites

Before you start, you'll need the following:

| Prerequisite          | Description                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
|  Braze REST API key  | A Braze REST API key. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. Don't forget to provision permissions for 'users' and 'campaigns' (endpoint used for Notify integration |
| PARTNER_POST_URL`/users/export/segment| This endpoint is used to fetch segment attached to a campaign                                              |
| PARTNER_POST_URL`/campaigns/trigger/send| This endpoint is used to trigger transactional communications.   
| CNAME configuration | A subdomain has to be created for the tracking pixel that is used within the email so that Notify can track user engagement with messaging to further inform the model. Share the url of the subdomain with Notify once it's created
| Database opt-in export | The client send to notify the campaign and purchase datas​ of the year (12 months). ​This export will be used to train Notify predictive model. <br><br> **Fields:** <br><br> **Email:** A SHA256 hash of the email, converted to lowercase and with any leading or trailing spaces removed.<br><br>**Segment:** The segment information defining the level of activity (active or inactive).<br><br>**Sub-segment:** Any other relevant activity information (client/prospect, purchase activity level, RFM, etc.). 

<!-- Create step-by-step instructions for integrating your tool with Braze. It's important to be concise and only outline the minimum neccesary steps. -->
## Integrating Notify

### Step 1: Campaign creation
Create an [API triggered campaign](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery) in Braze and share the campaign api_identifier with Notify.

### Step 2: Segment creation
Customer will create a segment in Braze and communicate the segmentId attached to the campaign. 

### Step 3: Segment fetching
Notify will fetch with an API call the list of contacts in the segment attached to the campaign.

### Step 4: Notify triggers the campaign
Notify’s AI triggers the Braze campaign to send to users at the time they deem most likely to engage.
             


