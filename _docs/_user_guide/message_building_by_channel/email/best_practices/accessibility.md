---
nav_title: Accessibility
article_title: Building Accessible Emails in Braze
page_order: 9
page_type: reference
description: "This article covers best practices regarding building accessible emails in Braze."
channel: email

---

# Building accessible emails in Braze

## Subject lines

Your email subject line is an essential part of communicating your message in a succinct and meaningful fashion. While there isn’t a limit on subject line length, make sure your subject line is descriptive and aligns with your preheader text and email body. Additionally, clearly identify yourself as the sender in a way that is easy for people to recognize.

Avoid using any jargon, technical terms, or abbreviations that may be misunderstood by screenreaders. By being mindful of [character limits for email clients]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#preheader-character-limits), you can avoid truncating your subject line and preheader text. 

Overall, these elements that are a part of the subject line can help increase the likelihood of your email message being opened!

## Email body

When creating accessible and readable emails, keep your content concise. You can leverage headers and body text to elevate your content. When creating an email campaign, maintain a logical structure throughout your email as screenreaders typically read left-to-right.

Avoid using “Click here” to indicate a link. Instead, make your links accessible by providing context, which helps users decide if they want to take any action. You can also use a button to communicate a call to action.

In general, avoid using tables in your content when possible. However, there may be times when you want to use a table purely for email design, not for displaying content. In this case, you can use an HTML attribute `role=”presentation”`, `aria-hidden=”true”` to hide the content from screenreaders.

## Images

Emails include a balance of readable copy and meaningful images. Be sure to describe these images with alternative text (alt text), which is a short description of the image content that screenreaders provide to their users. Avoid setting image dimensions (height and width) as this may cause an abundance of whitespace to appear in your email.

## Design

When designing your email, use high-contrast colors and themes. You can create an [email template]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) to use in your campaigns. This can help improve the readability and legibility of your messages for all of your users. It’s also important to select a legible font that is also spaced appropriately so that letters aren’t too close together. Some email clients may display your content in a default font if your selected font isn’t supported. 

Be sure to [test and preview]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/) your email campaigns on different email clients before sending them! When creating your emails in Braze, you can [check for email errors]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_campaign/#step-3c-check-for-email-errors) on the **Compose** tab of the message workflow.