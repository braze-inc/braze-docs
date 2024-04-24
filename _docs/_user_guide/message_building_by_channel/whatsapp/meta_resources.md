---
nav_title: Meta Resources
article_title: Meta Resources
page_order: 81
description: "This article provides helpful Meta documentation, information, and resources to improve your understanding of the WhatsApp integration."
page_type: reference
channel:
  - WhatsApp

---

# Meta resources

## Meta documentation

Review the following Meta documentation for guidance with display names, phone numbers, and more.

- [Display name guidance](https://www.facebook.com/business/help/757569725593362) 
- [Enabling Meta Insights](https://www.facebook.com/business/help/218116047387456)
- [Phone Number Requirements](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)
- [Messaging Limits](https://developers.facebook.com/docs/whatsapp/messaging-limits)
- [Quality Rating](https://www.facebook.com/business/help/896873687365001)

## WhatsApp Product Updates

### April 2024: Template pacing for utility templates
*Last Updated April 2024*

Last year, WhatsApp introduced template pacing for marketing messages as a new way to help businesses improve the engagement of their templates and create valuable user experiences. Beginning April 30, they're expanding template pacing to utility messages. If a utility template for an account gets paused due to user feedback, they will pace the new utility templates that are created for the next seven days.

### April 2024: Read rates will affect quality rating for marketing templates 
*Last Updated March 2024*

WhatsApp is testing new approaches, starting with consumers in India, to create more valuable experiences and maximize engagement with businesses’ marketing conversations. This may include limiting the number of marketing conversations a person receives from any business in a given period, starting with a small number of conversations that are less likely to be read. Braze will get an error code if a message is not delivered.

WhatsApp will start considering read rates as part of our quality rating for marketing templates, alongside traditional metrics like blocks and reports. WhatsApp may temporarily pause marketing message campaigns with low read rates, giving businesses time to iterate on the templates with the lowest engagement before scaling volume beginning on April 1, 2024. 

### February 2024: Marketing Conversations Experimentation

Starting February 6th, 2024, WhatsApp is testing new approaches, starting with consumers in India, to create more valuable experiences and maximize customer engagement with your brand’s marketing conversations. This may include limiting the number of marketing conversations a user receives from your brand in a given period, starting with a small number of conversations that are less likely to be read.

### October 2023: Template Pacing 

Starting October 12th, 2023, WhatsApp is introducing a concept called “template pacing” for marketing messages. Instead of sending your message to your entire campaign audience simultaneously, “template pacing” initially delivers the message to a smaller subset of users to gather real-time feedback from campaign recipients before sending the remaining messages. 

The “pace limit” (the initial subset of messages sent) is variable depending on the template. Following the initial send, WhatsApp will hold the remaining messages for a maximum of 30 minutes. During this holding period, they assess the quality of the template based on customer feedback. If the feedback is positive, indicative of a high-quality template, they deliver the remaining messages. If the feedback is negative, they drop the remaining undelivered messages, preventing further negative feedback from a larger portion of your customers and helping you avoid potential quality enforcement issues (such as phone number quality rating impacts). 

Note that WhatsApp uses the same system for assessing template quality in template pacing as they do for template pausing. So, messages undelivered during template pacing (due to low-quality templates) are the same ones that would have been paused on a larger scale. 

Ultimately, this update provides you with a quicker feedback loop (30 minutes versus hours or days with template pausing), so you can adjust your templates and provide a better customer experience.

**If you have any further questions about this update, please reach out to your Meta partner representative.**

### June 2023: Messaging Experimentation 

Starting June 14, 2023, Meta is introducing new experimentation practices to the WhatsApp platform in order to assess how marketing messages impact consumer experience and engagement. This experiment may affect your marketing messages sent on the WhatsApp Business API with Braze.

Meta intends to continue such experimentation on the WhatsApp platform. Please see [Meta’s documentation](https://developers.facebook.com/docs/whatsapp/on-premises/guides/experiments?content_id=86oue5PtwEgcBJl) for more information.

**WhatsApp experimentation affects marketing messages only.** This experiment has the potential to impact the delivery of marketing template messages. Utility and authentication templates will continue to be delivered without any experimentation impact.

In the experiment, Meta randomly chooses approximately 1% of WhatsApp consumers as participants. If chosen, Meta will not deliver marketing message templates to these consumers unless one of the following is true:

- If a consumer has replied to you in the last 24 hours;
- If an existing marketing conversation is open; or
- If a WhatsApp Ad was clicked on by the consumer in the last 72 hours.

## Frequently asked questions {#faq}

### How will I know if my marketing message was impacted by Meta's experiment?

If a message isn’t delivered due to the experiment, a specific error code will be surfaced under Activity Log and within Currents. The message will also be counted as a failure and incorporated into your WhatsApp Failures metrics across all reporting within the Braze dashboard. You will not be charged for these messages.

This 130472 error code will state “User’s number is part of an experiment.” Please see [Meta’s documentation](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes?content_id=8SJRLBEjYGvXO9k) for more information on WhatsApp Cloud API error codes.

### Can I opt out of Meta's experiment?

No, Meta does not permit any experiment opt-outs. All WhatsApp Business API providers and users are subject to this Meta experiment.

### Can I try to resend a template later?

There is no fixed time for this experiment. As such, a consumer may continue to be subject to the experiment.

### What can I do if my marketing messages are not delivered due to Meta's experiment?

We recommend using other Braze channels, such as email, SMS, push notifications, or in-app messages to send a message with similar content to your intended users.
