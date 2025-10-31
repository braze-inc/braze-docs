---
nav_title: "RCS"
article_title: About Rich Communication Services (RCS)
alias: /about_rcs/
page_type: reference
page_order: 14
description: "This reference article covers general use cases of the RCS channel and requirements needed to get your RCS channel ready for use."
---

# About Rich Communication Services (RCS)

> Rich Communication Services (RCS) enhances traditional SMS by enabling brands to deliver messages that are not only informative but also far more engaging. Now supported on both Android and iOS, RCS brings features like high-quality media, interactive buttons, and branded sender profiles directly into users’ pre-installed messaging apps, eliminating the need to download a separate app.

Unlike third-party messaging applications, RCS leverages the native messaging environment (Apple Messages and Google Messages), allowing you to reach users where they already spend most of their time and go beyond traditional SMS and MMS experiences by enabling richer, more interactive communication with customers. 

## Benefits of using RCS

- **Richer customer experiences:** Deliver richer user experiences by seamlessly integrating text, visuals, and interactive elements—boosting engagement and paving the way for personalized, data-driven campaigns.
- **Trusted, branded interactions:** Achieve trusted, branded interactions through a verified sender ID that not only showcases your brand’s assets but also complies with top industry privacy standards, enhancing customer trust and loyalty.
- **Flexible messaging delivery:** Facilitate flexible, reliable messaging delivery with a seamless SMS fallback that reaches every audience segment, regardless of device capabilities, while preserving a consistent user experience.
- **Actionable insights:** Unlock actionable insights with advanced reporting that tracks critical KPIs, empowering you to optimize campaigns in real time and drive measurable success.
- **Omnichannel synergy:** Seamlessly integrate RCS within your comprehensive marketing strategy to deliver consistent, cross-channel customer experiences, amplifying campaign effectiveness and overall ROI.

## Use cases

| Use case | Description |
| --- | --- |
| Interactive product promotions | Bring product promotions to life by combining engaging images or short videos with detailed product documents. Leverage suggested replies (such as "Add to Cart" or "Learn") and openURL actions to drive immediate product exploration and conversion—all within a rich, in-message experience. |
| Personalized loyalty and reward updates | Deliver personalized loyalty messages enriched with high-quality visuals and reward details. Use suggested replies (like "Redeem Now" or "View Offers") and openURL actions to create an interactive customer journey, making each update visually appealing and tailored to inspire immediate engagement and increased retention. |
| Secure transaction and account alerts | Deliver secure account alerts and transaction notifications by including images of PDF receipts or documents. Suggested actions (such as "Review Now" or "Contact Support") and openURL links enable customers to quickly access more details or initiate security steps, reinforcing both reliability and trust in every interaction. |
| Travel itinerary & booking enhancements | Enhance the travel experience by sending visually rich itineraries, destination guides, or boarding passes. With openURL actions, customers can quickly access booking modifications or real-time updates (such as schedule changes) without leaving the messaging window, facilitating a smooth and engaging travel journey from start to finish. |
| Customer feedback and interactive surveys | Capture actionable feedback by deploying interactive surveys that use a mix of rich media content and text. Integrate suggested replies for quick responses and openURL actions to access more comprehensive survey forms, making it simple for customers to share their opinions, helping marketers refine their strategies based on real-time feedback from across all verticals. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Requirements

| Requirement | Description |
| --- | --- |
| Message credits | Contact your Braze account manager to confirm you’ve purchased Message Credits in your contract. Message Credits is a flexible contract item that allows you to purchase and allocate messaging volume across various channels, such as SMS, MMS, RCS, and WhatsApp. |
| Eligible country | Make sure that you are sending RCS to users in one of Braze’s supported countries: United States, United Kingdom, Germany, Mexico, Sweden, Spain, Singapore, Brazil, France, Italy, Colombia |
| RCS verified sender | The sender that the recipient sees on their device to identify where the message is coming from. An RCS-Verified Sender consists of a company name, visual branding, and a verified badge. <br><br> Braze will help you apply and register for an RCS-verified sender in eligible regions. You’ll need to provide your Braze representative with some basic information. |
| List of users with phone numbers | Before you can start sending messages, you must add users to your account. Additionally, you must know the approximate size of your audience. Users and phone numbers can be added to Braze through several different methods. Phone numbers must be formatted as a 10-digit number, as well as a country area code. To learn more, refer to [User phone numbers]({{site.baseurl}}/user_phone_numbers/). |
| Keywords and responses | All base keywords must have responses attributed to them before you can begin messaging. Braze will process opt-in, opt-out, and help keywords automatically. Customization options and additional keyword-response configurations are available. To learn more, refer to [Opt-in and opt-out keywords]({{site.baseurl}}/optin_optout/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Terms to know

| Term | Definition |
|----|----|
| Subscription group | A group of users who are subscribed to a specific messaging use case. Each subscription group is tied to one or more brand "senders," which can be RCS verified senders, SMS codes, or both. For example, if you plan to send both transactional and promotional RCS messages, you might choose to set up two subscription groups with separate RCS-verified senders in your Braze dashboard. |
| RCS-verified sender | The sending entity of an RCS message, or what the recipient of the RCS message sees on their device to identify where the message is coming from. RCS-verified senders contain a company name, caption, visual branding, and a verified badge. After you provide the necessary RCS sender registration information to Braze, we take care of registration and subscription group setup. |
| SMS fallback | If a message is unable to be delivered with RCS (for example, lack of carrier support in the region), Braze will still attempt to deliver the message through SMS when an SMS code exists within the subscription group. |
| Basic RCS | Text-only messages up to 160 characters. Billed as a single message. <br><br> This category is only used in the global model. |
| Single RCS | Text-only messages that are over 160 characters **or** include any rich elements, like buttons or media. <br><br>This category is only used in the global model. |
| Rich | Text-only messages, with or without limited suggestions or buttons. Billed per segment (160 UTF-8 bytes). For example, a message with 161 characters of plain text is two segments. <br><br> This category is only used in the United States model. |
| Rich Media | Messages that include a media file (image, video) or a Rich Card. Billed as a single message, regardless of message length. <br><br> This category is only used in the United States model. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
