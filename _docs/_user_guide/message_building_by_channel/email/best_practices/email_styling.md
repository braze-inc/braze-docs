---
nav_title: Email styling
article_title: Email Styling
page_order: 2
page_type: reference
description: "This article outlines email styling best practices to reference as you build your email campaigns."
channel: email

---

# Email styling

## Address styling

The **Subject Line** is one of the first things that recipients will see upon receiving your message. Keeping it to 6 to 10 words will yield the highest open rates. 

There are also different approaches to creating a good subject line, ranging from asking a question to pique the reader's interest or being more direct, to personalizing it as to engage your clientele. Don't just stick with one subject line, leverage [A/B testing]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing/) to try new ones out and gauge their effectiveness. Subject lines should be no more than 35 characters to display appropriately on mobile.

The "From" field should clearly show who the sender is. Try not to use a person's name or an uncommon abbreviation. Instead, use a recognizable name like your brand name. If using a person's name suits your brand's methods of personalizing email, stay consistent to develop a relationship with the recipient. The "From" name should be no more than 25 characters to display appropriately on mobile.

### No-reply addresses

No-reply email addresses are generally not recommended for multiple reasons as they disengage your readers. Many recipients reply to the email to unsubscribe, so if they are not allowed to do that, the next course of action is more often than not marking the email as spam.

Getting out-of-office replies can actually provide valuable information, increasing open rates and decreasing spam reports (by removing those who don't want to be emailed). On a personal level, a no-reply can appear impersonal to recipients and may turn them away from receiving further emails from your company.

## Preheader text

The preheader text in an email communicates the main point of the message efficiently to catch the reader's interest and encourage opens. Preheader text is also often used by email marketers to provide additional information on an email's contents. A preheader is the preview text displayed immediately after an email subject. In the following example, the preheader is `- Brand. New. Lounge Shorts`.

![Preheader text in a Gmail inbox with the text "Brand. New. Lounge Shorts".]({% image_buster /assets/img_archive/preheader_example.png %})

The amount of visible preheader text is dependent on the user's email client and the length of the email's subject line. Generally, we suggest email preheaders to be between 50 and 100 characters.

Here are some best practices to keep in mind when writing your preheaders:

1. Calls to action come into play after readers have opened your email.
  - Point your readers in the right direction, whether you want them to subscribe, purchase a product or visit your website.
  - Use strong words so that the reader knows exactly what you are asking of them, but make sure it reflects your company's brand voice and that every call to action exhibits some sort of value to the consumer.
  - Preheader should be no more than 85 characters and have some sort of descriptive call to action that supports the subject line.

2. Email and landing sites to which you direct your users to should be mobile optimized:
  - No interstitial boxes
  - Large form-fields
  - Easy navigation
  - Large text
  - Generous white space
  - Short concise body copy
  - Clear calls to action

### Preheader character limits

  |   Mobile Email Client  |  Limit  |
  |:----------------------:|:-------:|
  | iOS Outlook            | 74      |
  | Android Native         | 43      |
  | Android Gmail          | 24      |
  | iOS Native             | 82      |
  | iOS Gmail              | 30      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }

  |  Desktop Email Client  |  Limit  |
  |:----------------------:|:-------:|
  | Apple Mail             | 33      |
  | Outlook '13            | 38      |
  | Outlook for Mac '15   | 53      |
  | Outlook '16            | 50      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }


  |  Webmail Email Client  |  Limit  |
  |:----------------------:|:-------:|
  | AOL Mail               | 81      |
  | Gmail                  | 119     |
  | Outlook.com            | 49      |
  | Office 365             | 40      |
  | Mail.ru                | 64      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Email size

Make sure to limit your email size. Email bodies larger than 102&nbsp;KB are not only extremely taxing on Braze servers, but they're also clipped by Gmail and other email clients. Try to keep the size of your email under 25&nbsp;KB for just text or 60&nbsp;KB with images. We highly encourage you to use our image uploader to host images and to reference these images by the `href`.

|   Text Only   | Text With Images |     Email Width    |
|:-------------:|:----------------:|:------------------:|
| 25&nbsp;KB maximum |   60&nbsp;KB maximum   | 600 pixels maximum |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Text length

Refer to the following table for recommended text lengths.

| Text Specifications | Recommended Properties |
| --- | --- |
| Subject Line Length | 35 characters maximum (for optimal mobile display) (6 to 10 words) |
| Sender Name Length | 25 characters maximum (for optimal mobile display) |
| Preheader Length | 85 characters maximum |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Image size

Refer to the following table for recommended image sizes. Smaller, high-quality images will load faster, so use the smallest asset possible to achieve your desired output.

|     Size    | Header Image Width |  Body Image Width  |   File Types  |
|:-----------:|:------------------:|:------------------:|:-------------:|
| 5&nbsp;MB maximum | 600 pixels maximum | 480 pixels maximum | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Deep linking

A high percentage of emails are read on mobile devices. Using [deep linking]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) is a great practice for engaging with these mobile email recipients. With push notifications and in-app messages, a deep link takes the user directly to a specified destination within an app. 

However, emails don't provide the clarity of knowing whether recipients have the app installed. So, avoiding deep linking helps prevent error messages for these email recipients who do not have the app.

