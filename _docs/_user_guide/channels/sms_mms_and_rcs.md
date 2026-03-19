---
nav_title: "SMS, MMS, and RCS"
article_title: "SMS, MMS, and RCS"
page_order: 8
page_type: landing
channel:
  - SMS
  - MMS
  - RCS
search_rank: 3
alias: /about_rcs/
description: "This landing page is home to SMS (Short Messaging Service), MMS (Multimedia Messaging Service), and RCS (Rich Communication Services). These services offer a more direct way to reach your users than most other messaging channels, as they utilize their phone number, allowing you to reach them in real-time."
---

# SMS, MMS, and RCS

> SMS (Short Messaging Service), MMS (Multimedia Messaging Service), and RCS (Rich Communication Services) offer a more direct way to reach your users than most other messaging channels, as they utilize phone numbers for real-time reach.
>
> RCS enhances traditional SMS by helping brands deliver messages that are informative and engaging. Supported on Android and iOS, RCS adds high-quality media, interactive buttons, and branded sender profiles in users' pre-installed messaging apps, without requiring a separate app.

Unlike third-party messaging applications, RCS uses the native messaging experience (Apple Messages and Google Messages), so you can reach users where they already spend time and go beyond traditional SMS and MMS with richer, more interactive communication.

SMS remains one of the most widely used channels worldwide—billions of text messages are sent every day—because it is fast, direct, and familiar to customers.

## Prerequisites

SMS, MMS, and RCS availability depends on your Braze package. Contact your account manager or customer success manager to get started.

Before you start, make sure you have the following:

- Short codes, long codes, or Alphanumeric sender IDs configured. For more information, refer to [Sender setup]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/).
- Familiarity with SMS laws and regulations, including TCPA and carrier requirements. For more information, refer to [Laws and regulations]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/).
- Explicit opt-in consent collected from users. For more information, refer to [Collecting user opt-ins]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins/).

## Use cases

| Use case | Explanation |
| --- | --- |
| Appointment reminders | Send timely reminders before scheduled appointments, reducing no-shows and keeping customers informed. |
| Order updates | Notify customers about order confirmations, shipping status, and delivery updates in real time. |
| Two-factor authentication | Deliver one-time verification codes for account login and transaction confirmation. |
| Promotional offers | Reach customers with time-sensitive promotions, flash sales, and personalized discounts directly on their phone. |
| Customer support | Enable two-way conversations to resolve customer inquiries, collect feedback, or confirm service requests. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## SMS, MMS, and RCS compared

- **SMS** delivers text-only messages up to 160 characters (or 70 characters with Unicode). It's universally supported across all mobile devices and carriers.
- **MMS** extends SMS with support for multimedia content, including images, GIFs, and audio. MMS requires carrier and device support.
- **RCS** is the next generation of business messaging, offering rich features such as branded sender profiles, suggested replies, carousels, and read receipts. RCS availability depends on carrier and device support.

### Why use RCS?

RCS (Rich Communication Services) builds on SMS with a richer, more app-like experience in the default messaging app on supported devices. Brands use RCS to:

- Deliver high-resolution images and video instead of only plain text.
- Add suggested replies and actions so customers can respond with one tap.
- Show a verified sender profile with branding so messages are easy to trust.
- Support read receipts and typing indicators where carriers allow it.

RCS is suited to use cases such as transactional updates (shipping, appointments), promotions with rich creative, customer support with quick-reply paths, and onboarding or tutorials that benefit from media and structured actions. For setup and migration from SMS, see [RCS setup]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup/).

## Benefits of using RCS

- **Richer customer experiences:** Combine text, visuals, and interactive elements to boost engagement and support personalized, data-driven campaigns.
- **Trusted, branded interactions:** Use a verified sender ID with your brand assets and industry-aligned privacy practices to reinforce trust.
- **Flexible messaging delivery:** Use SMS fallback when RCS isn't available so you still reach your audience while keeping the experience consistent where RCS is supported.
- **Actionable insights:** Use reporting on key KPIs to optimize campaigns in real time.
- **Omnichannel synergy:** Align RCS with the rest of your marketing stack for consistent cross-channel experiences.

## Example RCS use cases

| Use case | Description |
| --- | --- |
| Interactive product promotions | Combine images or short videos with product details. Use suggested replies (such as "Add to Cart" or "Learn") and openURL actions to drive exploration and conversion in the message. |
| Personalized loyalty and reward updates | Send loyalty updates with high-quality visuals and reward details. Use suggested replies (like "Redeem Now" or "View Offers") and openURL actions to encourage immediate engagement. |
| Secure transaction and account alerts | Send account alerts and transaction notifications with receipt or document images. Use suggested actions (such as "Review Now" or "Contact Support") and openURL links so customers can act quickly. |
| Travel itinerary and booking enhancements | Share itineraries, destination guides, or boarding passes. Use openURL actions for booking changes or schedule updates without leaving the thread. |
| Customer feedback and interactive surveys | Run surveys with rich media and text. Use suggested replies for quick responses and openURL actions for longer forms. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## RCS requirements

| Requirements | Description |
| --- | --- |
| Message credits | Confirm with your Braze account manager that Message Credits are included in your contract. Message Credits let you purchase and allocate messaging volume across channels such as SMS, MMS, RCS, and WhatsApp. |
| Eligible country | Send RCS only to users in a [supported country]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup/#step-1-meet-the-eligibility-criteria). |
| RCS-verified sender | The sender identity users see includes your company name, branding, and a verified badge. Braze helps you apply and register an RCS-verified sender in eligible regions. |
| List of users with phone numbers | Add users and valid phone numbers to Braze before sending. Phone numbers need a country code and proper formatting. For more information, refer to [User phone numbers]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers/). |
| Keywords and responses | Base opt-in, opt-out, and help keywords must have responses before you start messaging. Braze processes default keywords automatically, and you can customize additional keyword responses. For more information, refer to [SMS opt-in and opt-out keywords]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For sender registration, SMS fallback, and subscription groups, also see [RCS setup]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup/).

## RCS terms to know

| Term | Definition |
| --- | --- |
| Subscription group | A group of users subscribed to a specific messaging use case. Each subscription group is tied to one or more brand senders, which can be RCS-verified senders, SMS codes, or both. |
| RCS-verified sender | The sending entity for RCS—what the recipient sees on their device. It includes a company name, caption, visual branding, and a verified badge. |
| SMS fallback | If RCS can't be delivered (for example, limited carrier support), Braze can still attempt delivery over SMS when an SMS code exists in the subscription group. |
| Basic RCS | Text-only messages up to 160 characters, billed as a single message. Used in the global model. |
| Single RCS | Text over 160 characters or any rich elements (such as buttons or media), billed as a single rich message. Used in the global model. |
| Rich | Text-only messages, with or without limited suggestions or buttons, billed per segment (160 UTF-8 bytes). Used in the United States model. |
| Rich Media | Messages that include media or a Rich Card, billed as a single message regardless of length. Used in the United States model. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Next steps

- [Message setup]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/)
- [Create a message]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/)
