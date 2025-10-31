---
nav_title: Stylitics
article_title: Stylitics
description: "This reference article outlines the partnership between Braze and Stylitics, a cloud-based SaaS platform that allows you to enhance your existing email campaigns with engaging and relevant bundled content, creating a personalized customer experience."
alias: /partners/stylitics/
page_type: partner
search_tag: Partner

---

# Stylitics

> [Stylitics](https://stylitics.com/) is a cloud-based SaaS platform for retailers to automate and distribute visual content at scale. Stylitics bundles inspire by contextualizing products, boosting purchase confidence, and increasing engagement, ultimately leading to higher average order value and conversion rates.

_This integration is maintained by Stylitics._

## About the integration

Your Braze and Stylitics integration allows you to enhance your existing email campaigns with engaging and relevant bundled content, creating a personalized customer experience.

![]({% image_buster /assets/img/stylitics.png %}){: style="max-width:60%;"}

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Stylitics account | A [Stylitics](https://stylitics.com/) account is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

The following lists some common triggered email program examples:
- Abandoned cart emails 
- Abandoned browse emails 
- Shipping confirmation emails
- Post-purchase emails 

## Integration

Stylitics provides bundle data for this integration. Your email service provider can create or update the email template to include Stylitics bundles. Stylitics cannot alter the layout or design of the emails. 

1. Integrate the bundle into the email. ESP determines the position and customization.
2. ESP updates trigger email code to include Stylitics content.
3. ESP will test, preview and launch the updates triggered series. 

Stylitics will only be providing the bundle data for the items. Between you and your ESP, you will have user data and can plug in Stylitics bundle data to send to the users.

## Data exchange

The following three approaches allow you to include Stylitics bundles in your triggered emails.

### 1\. API approach (recommended)

You or your ESP can make an API call per item to populate bundle data into your email. Stylitics recommends you use their API to make API calls as it is ready to use immediately.

{% alert note %}
If you run a Stylitics-run A/B test, the `styliticsCID` and `styliticsoverride` parameters must be appended to the PDP URLs of the Stylitics items the user clicks in the email.
<br><br>
For example, {% raw %}`&styliticsoverride=001?styliticsCID=email[clientname]`{% endraw %}
{% endalert %}

### 2\. Flat file approach
You or your ESP can reference an item's bundle data in a flat file to populate bundle data into your email. Stylitics can flatten bundle data into CSV, TXT, or XML format and send it to you daily. They can also help adjust the file format per your ESP's needs. Note that this takes 2-3 weeks to create this file.

#### Requirements:
- **Location**: Stylitics can drop the file on the Stylitics SFTP for you to pick up daily, or you can send them your SFTP credentials to drop the file. 
- **Time**: Stylitics will drop the file in the morning daily. Let them know if there is a specific time in mind you need the file by. 
- **File key**: You and Stylitics need to agree upon what item data string to key the file on so your ESP can reference the data. SKU, `item_group_id`, or `item_number` are commonly used. 

### 3\. Website data extraction approach
Vendors can scrape the front end of your site for Stylitics content and insert bundle data into emails. No additional work from Stylitics is required. 

## Email template best practices 

You and your ESP will create an HTML email template to insert Stylitics data and bundles. Here are some best practices and recommendations. 
- Display 2-4 bundles in the email for the most expensive item or first full-price item the user bought or interacted with 
- Call multiple `item_numbers` and show the first few bundle response 
- Have a fallback option if there are no bundles available for the item 
	- Hide the section where Stylitics bundles live 
	- Show bundles for the next item the user viewed 
- Display bundle images and a list of product titles and thumbnail images to ensure the user has a clear click-through

{% alert note %}
The Stylitics widget JavaScript cannot be inserted into emails as emails do not support JavaScript.
{% endalert %}

## Analytics

Stylitics provides the bundle data for this type of email program. Therefore, we ask for an open data share between you, your ESP, and Stylitics. If possible, we hope to receive the following metrics from you to understand the lift and improve the program:
- Emails sent 
- Emails opened 
- Views and engagements 
- Click through rate 
- Add to bags 
- Purchases

## Next steps 

Contact your Stylitics account manager to coordinate the next steps and timelines for the email program. Some next steps include: 
- Decide which emails you’d like to use
- Connect Stylitics with your ESP to discuss data exchange to decide API option or flat file option 
- Create mockups with your ESP 
- Align on analytics 
- Align on the launch timeline 


