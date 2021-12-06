---
nav_title: Taxi for Email
article_title: Taxi for Email
alias: /partners/taxi_for_email
description: "This article outlines the partnership between Braze and Taxi for Email, an online email marketing tool that allows Braze customers to create intelligent email templates using their drag and drop interface and simple yet powerful syntax."
page_type: partner
search_tag: Partner

---

# Taxi for Email

[Taxi for Email](http://taxiforemail.com/) is an online email marketing tool that offers an intuitive drag-and-drop visual email editor. Taxi encourage teams to easily collaborate on email campaigns, allowing copywriters and editors the access and resources they need to build emails, all without code.

The Braze and Taxi integration leverages Taxi's simple yet powerful syntax to create and export intelligent email templates to Braze. 

## Prerequisites

| Requirement | Description |
| ------------| ----------- |
| Taxi for Email account | A Taxi for Email account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API Key with full **Templates** permissions. <br><br> This can be created within the __Braze Dashboard -> Developer Console -> REST API Key -> Create New API Key__ |
| Braze endpoint | Your Braze [endpoint]({{site.baseurl}}/api/basics/#endpoints) aligns with your Braze dashboard URL.<br><br> For example, if your dashboard URL is `https://dashboard-03.braze.com`, your endpoint will be `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Integration

### Step 1: Create a Taxi email template

Create a Taxi template on the Taxi platform. Once created, navigate to your **Organization Settings** and select the **ESP Connectors** tab.

### Step 2: Create Braze connector

1. In the dialogue that appears, click the **Add New** button and select **Braze** from the drop-down. 
2. Click **Braze** to edit the Braze connector settings.
3. Enter your Braze endpoint and your Braze API key.

Your connector field will turn green once details with correct permissions are provided. If this field is not green, check that your fields align with the requirements listed above. 

## Usage

Find your uploaded Taxi template in your Braze account's **Templates & Media > Email Templates** section. You can now use this email template to start sending engaging email messages to your customers!

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
