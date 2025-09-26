---
nav_title: Quality rating and messaging limits
article_title: Quality Rating and Messaging Limits 
description: "This reference article covers how Meta influences your quality rating and messaging limits for the WhatsApp channel."
page_type: partner
search_tag: Partner
page_order: 
channel:
  - WhatsApp
---

# Quality rating and messaging limits

> Meta influences your quality rating and [messaging limits](https://developers.facebook.com/docs/whatsapp/messaging-limits) from the moment you start using the WhatsApp channel, and will continue to influence them in response to your WhatsApp usage.

## Definitions

| Word | Definition |
| --- | --- |
| Quality rating | A rating based on the recent messages that your customers have received over the last seven days. This rating is determined by the feedback from your customers, such as the reason to block your phone number and other reporting issues. View Meta's documentation to learn more [about your quality rating](https://www.facebook.com/business/help/896873687365001).|
| Messaging limit | The maximum number of business-initiated conversations you can begin with each of your phone numbers in a rolling 24-hour period. |
{: .reset-td-br-1 .reset-td-br-2 }

## Onboarding  

When a new WhatsApp Business Account is created, Meta uses a variety of factors to determine the initial sending limit. You can find this limit in your WhatsApp Business Manager, and additional details on your Phone Number Insights page. 

View Meta's documentation to learn more about [checking your limit](https://developers.facebook.com/docs/whatsapp/messaging-limits#checking-your-limit) and [phone number requirements](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers).

## Throughput

Meta starts each registered business phone number with a throughput of 80 messages per a second. Upgrades to 1,000 messages per second can happen automatically, or on request. Information. 

View Meta's documentation to learn more about your [throughput](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput).

## Template pacing

Recently created marketing templates and paused marketing templates that become unpaused are potentially subject to pacing. Meta’s pacing selection criteria is primarily driven by your template quality history. When you use a recently created marketing template or recently unpaused marketing template, messages will be sent normally until an unspecified threshold is reached. After this threshold is reached, subsequent messages using that template will be held to allow enough time for customer feedback. 

View Meta's documentation to learn more about [template pacing](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pacing).