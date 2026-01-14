---
nav_title: Meta resources
article_title: Meta Resources
page_order: 12
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

## WhatsApp product updates

### April 2025: Pause of marketing messages to US phone numbers
*Last Updated August 2025*

Meta will pause the delivery of all marketing template messages to WhatsApp users who have a United States phone number (a number composed of a `+1` dialing code and a US area code). There is no current scheduled date when this pause will be lifted. 

Any attempts to send a template to a WhatsApp user with a US phone number will result in the error `131049`.

### March 2025: Per-user marketing template message limits
*Last Updated August 2025*

Meta will limit the number of marketing template messages a user can receive across all businesses in a given period of time, starting with messages that are less likely to be read. 

One exception is, if a person responds to a marketing message, it will start a 24-hour customer service window. Marketing messages sent within this window will not count towards a person’s limit.

The specific limit varies by user, depending on their engagement level. Learn more about WhatsApp's per-user marketing template message limits [here](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits). 

### January 2025: WhatsApp pausing marketing message sending to US users starting April 1
*Last Updated January 2025*

WhatsApp will pause marketing message sending to US users (people with US phone numbers) starting April 1, 2025. [Utility, service, authentication](https://developers.facebook.com/docs/whatsapp/pricing/), and [response messages]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) will still be allowed in the US. 

Marketing message sending (plus all other message types) to all other countries or regions is still allowed and will not be affected.

Meta informed us that they are making this update to maintain the health of the WhatsApp ecosystem in the US, where WhatsApp is fast growing, but still at an earlier stage (for example, marketing messages see lower engagement than other regions). They will continue to evaluate when the US market is ready to resume marketing messages.

Marketing message delivery to phone numbers with US area codes will be rejected by WhatsApp and return an error code of 131049. 

### November 2024: Changes to WhatsApp Opt-in policy
*Last Updated January 2025*

Meta recently updated their [opt-in policy](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Instead of requiring channel-specific consent, businesses can now message users on the platform if:

1. The person has given their phone number.
2. The person provided opt-in permission for general messaging, not just WhatsApp. 

Businesses still need to comply with all local laws and follow the below requirements when obtaining opt-in:

- Businesses must clearly state that a person is opting in to receive communication from the business
- Businesses must clearly state the business name that a person is opting in to receive messages from
- Businesses must comply with applicable law

Although WhatsApp has loosened their policy, Braze still recommends collecting opt-in specific to the WhatsApp channel in order to foster the best customer experience and engagement rates. As always, check with your legal team to see what makes sense for your brand.

### November 2024: Updates to the per-user marketing template limit for people in the US, ahead of the holiday season
*Last Updated December 2024*

Since Meta has rolled out the per-user marketing template limit, Meta has seen significant improvements in user read rates and sentiment.
 
Beginning now, ahead of the holiday season, people in the US will receive fewer new marketing conversations. Meta expects this change to create more engaged audiences, which ultimately leads to better outcomes for businesses. This may result in lower delivery rates for your business if you send marketing messages to US phone numbers, which can be monitored with the error code `131049` through Braze Currents and the Message Activity Log.

Businesses in the US can still deliver marketing messages in other geographies, and there is no impact to utility, authentication or service messages, or marketing template messages sent within a user-initiated conversation window (for example, a click-to-WhatsApp ad or product carousel or coupon template that is sent as part of a conversation). 

### November 2024: WhatsApp expanding quality-based account enforcements to include read rates
*Last Updated December 2024*

WhatsApp is continuously investing in new ways to help businesses create quality experiences for their customers, such as reducing spam-like behavior on their platform. 

On November 22, WhatsApp began to expand their existing account-level quality enforcements on WhatsApp business accounts (WABAs) with extremely low read rates. This change will roll out globally.

When an account's read rate drops significantly (for example, the majority of messages sent by the account are unread), messaging blocks will be enforced on the account. The severity of the block will increase if there are consistently low read rates at scale. 

If the account's read rate is extremely low, the following actions will be taken:

- The account will be blocked from sending business-initiated messages. They can still respond to customer-initiated messages. This initial block is a "soft lock" and may be acknowledged by selecting the acknowledge button in Account Quality to begin messaging again.
- If read rate continues to drop or remains low after the soft lock, businesses may face a gradual increase in enforcement actions (for example, a few days of messaging restrictions).
- Businesses will have to wait for the enforced limit to begin messaging again. If the read rate continues to remain low after repeat soft locks, the account will eventually be offboarded.

#### How to stay updated on these warnings and enforcements

Similar to existing platform enforcement, businesses will be notified about these actions and can acknowledge them by using the Account Quality page in the WhatsApp Business Manager. Confirm that you have the correct contact details listed in the WhatsApp Business Manager for all necessary administrators, as the enforcement notification emails will be sent based on that information.

Notifications about severe spam violations will be:

- Surfaced in the WhatsApp Business Manager Notifications Center
- Displayed in a banner in the WhatsApp Manager
- Sent as an email to all administrators set in the WhatsApp Business Manager

### May 2024: Cloud API going live in Türkiye
*Last Updated May 2024*

Meta now provides Cloud API businesses access to Türkiye for business messaging. Previously, WhatsApp Cloud API was available for businesses in Turkey to use, but WhatsApp users with Turkish numbers were not able to send or receive messages sent via Cloud API. 

Meta always makes it clear to users when they are chatting with a business hosted by Meta, and all users are required to accept the relevant WhatsApp Terms of Service and Privacy Policy to proceed with business messaging. The 2021 Terms of Service and Privacy Policy update in Turkey had been paused, but is now rolling out. It does not change Meta’s commitment to privacy–personal conversations continue to be protected by end-to-end encryption meaning only you and the intended recipient can see them. The update enables Turkish users to access optional business features if they choose to do so and provides more transparency about how WhatsApp works.  
 
Cloud API businesses can now initiate conversations with WhatsApp users with Turkish numbers, which will now return a webhook as a “sent” conversation, instead of today’s error code 131026.

For a business message to be “delivered” or “read” requires the user accepting the WhatsApp terms. A business will not be charged unless the message is delivered.

Users that receive or try to send a message to a Cloud API business will be shown an in-app notification about the terms update which makes clear they cannot message a Cloud API business until they’ve accepted the WhatsApp update. In addition, users that register or re-register the app on their phone, will be prompted to accept the WhatsApp update.

When a user accepts the update they will see the existing Cloud API system message notice when they chat with a Cloud API Business.

### May 2024: Per-user marketing template message limits
*Last Updated May 2024*

Meta is rolling out new approaches to maintain high-quality user experiences and maximize marketing template message engagement on the WhatsApp platform. Beginning May 23, 2024, they will be limiting the number of marketing template messages that each individual user can receive from all businesses they interact with during a given time period, starting with a small number of conversations that are less likely to be read. Note that the limit is determined based on the number of marketing template messages that person has already received from any business, and is not related to your brand specifically. However, this may affect the deliverability of your marketing template messages.

The limit only applies to marketing template messages that would normally open a new marketing conversation. If a marketing conversation is already open between your brand and a WhatsApp user, marketing template messages sent to the user will not be affected.

If a marketing template message is not delivered to a given user due to the limit, Cloud API will return error code 131026. Note, however, that these error codes cover a wide range of issues that can result in non-delivery of a message, and for privacy reasons, Meta will not disclose if in fact the message was not delivered due to the limit. Refer to Cloud API's [Troubleshooting document](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) for descriptions of non-delivery reasons and what you can do to determine their underlying cause.

If you do receive one of these error codes and suspect it is due to the limit, avoid immediately resending the template message, as it will only result in another error response. 

For more information on this deliverability update, including details on monitoring your deliverability and other best practices for marketing messaging on WhatsApp, refer to our recent [blog post](https://www.braze.com/resources/articles/meta-introduces-deliverability-updates-for-whatsapp?utm_campaign=fy25-q2-global-customer-customer-meta-deliverability-updates-for-whatsapp&utm_medium=email-cdb&utm_source=braze&utm_content=blog-meta-deliverability-updates-for-wa-blog).

### April 2024: Template pacing for utility templates
*Last Updated April 2024*

Last year, WhatsApp introduced template pacing for marketing messages as a new way to help businesses improve the engagement of their templates and create valuable user experiences. Beginning April 30, they're expanding template pacing to utility messages. If a utility template for an account gets paused due to user feedback, they will pace the new utility templates that are created for the next seven days.

### April 2024: Read rates will affect quality rating for marketing templates 
*Last Updated March 2024*

WhatsApp is testing new approaches, starting with consumers in India, to create more valuable experiences and maximize engagement with businesses’ marketing conversations. This may include limiting the number of marketing conversations a person receives from any business in a given period, starting with a small number of conversations that are less likely to be read. Braze will get an error code if a message is not delivered.

WhatsApp will start considering read rates as part of our quality rating for marketing templates, alongside traditional metrics like blocks and reports. WhatsApp may temporarily pause marketing message campaigns with low read rates, giving businesses time to iterate on the templates with the lowest engagement before scaling volume beginning on April 1, 2024. 

### February 2024: Marketing Conversations Experimentation
*Last Updated February 2024*

Starting February 6th, 2024, WhatsApp is testing new approaches, starting with consumers in India, to create more valuable experiences and maximize customer engagement with your brand’s marketing conversations. This may include limiting the number of marketing conversations a user receives from your brand in a given period, starting with a small number of conversations that are less likely to be read.

### October 2023: Template Pacing 
*Last Updated October 2023*

Starting October 12th, 2023, WhatsApp is introducing a concept called “template pacing” for marketing messages. Instead of sending your message to your entire campaign audience simultaneously, “template pacing” initially delivers the message to a smaller subset of users to gather real-time feedback from campaign recipients before sending the remaining messages. 

The “pace limit” (the initial subset of messages sent) is variable depending on the template. Following the initial send, WhatsApp will hold the remaining messages for a maximum of 30 minutes. During this holding period, they assess the quality of the template based on customer feedback. If the feedback is positive, indicative of a high-quality template, they deliver the remaining messages. If the feedback is negative, they drop the remaining undelivered messages, preventing further negative feedback from a larger portion of your customers and helping you avoid potential quality enforcement issues (such as phone number quality rating impacts). 

Note that WhatsApp uses the same system for assessing template quality in template pacing as they do for template pausing. So, messages undelivered during template pacing (due to low-quality templates) are the same ones that would have been paused on a larger scale. 

Ultimately, this update provides you with a quicker feedback loop (30 minutes versus hours or days with template pausing), so you can adjust your templates and provide a better customer experience.

**If you have any further questions about this update, contact your Meta partner representative.**

### June 2023: Messaging Experimentation 
*Last Updated June 2023*

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
