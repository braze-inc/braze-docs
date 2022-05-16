---
nav_title: Email Styling
article_title: Email Styling
page_order: 4
page_type: reference
description: "This article outlines email styling best practices to reference as you build your email campaigns."
channel: email

---

# Email styling tips

## Address styling

The **Subject Line** is one of the first things that recipients will see upon receiving your message. Keeping it to 6 to 10 words will yield the highest open rates. 

There are also different approaches to creating a good subject line, ranging from asking a question to pique the reader’s interest or being more direct, to personalizing it as to engage your clientele. Don’t just stick with one subject line, try new ones out and gauge their effectiveness. Subject lines should be no more than 35 characters to display appropriately on mobile.

The "From" field should clearly show who the sender is. Try not to use an unknown person’s name or an uncommon abbreviation, instead try using something recognizable like the company name. If using a person’s name suits your company methods of personalizing email, stay consistent and retain the same “From" name to develop a relationship with the recipient. “From” name should be no more than 25 characters to display appropriately on mobile.

## Body styling

Many users use **Email Previewing** in Gmail or Outlook. These preview areas generally allow for around 300 pixels or 85 characters of content to be shown. It is recommended that the email communicate the main point of the message efficiently within that space, engaging the reader’s interest to encourage opens.

No-reply email addresses are generally not recommended for multiple reasons as they disengage your readers. Many recipients reply to the email to unsubscribe, so if they are not allowed to do that, the next course of action is more often than not marking the email as spam.

Getting out of office replies can actually provide valuable information, increasing open rates and decreasing spam reports (by removing those who don’t want to be emailed). On a personal level, a no-reply can appear impersonal, lazy and arrogant to recipients (suggesting “You aren’t worth my time”), and may turn them off from receiving further email from your company.

Preheader text is often used by email marketers to provide additional information on an email's contents. A preheader is the preview text displayed immediately after an email subject. In the following example, the preheader is `- Brand. New. Lounge Shorts`.

![Preheader text in a Gmail inbox with the text "Brand. New. Lounge Shorts".][61]

The amount of visible preheader text is dependent on the user's email client and the length of the email's subject line. Generally, we suggest email preheaders to be between 50 and 100 characters.

## Preheader character limits

  |   Mobile Email Client  |  Limit  |
  |:----------------------:|:-------:|
  | iOS Outlook            | 74      |
  | Android Native         | 43      |
  | Android Gmail          | 24      |
  | iOS Native             | 82      |
  | iOS Gmail              | 30      |
  {: .reset-td-br-1 .reset-td-br-2}

  |  Desktop Email Client  |  Limit  |
  |:----------------------:|:-------:|
  | Apple Mail             | 33      |
  | Outlook '13            | 38      |
  | Outlook for Mac '15   | 53      |
  | Outlook '16            | 50      |
  {: .reset-td-br-1 .reset-td-br-2}


  |  Webmail Email Client  |  Limit  |
  |:----------------------:|:-------:|
  | AOL Mail               | 81      |
  | Gmail                  | 119     |
  | Outlook.com            | 49      |
  | Office 365             | 40      |
  | Mail.ru                | 64      |
  {: .reset-td-br-1 .reset-td-br-2}

Here are some best practices to keep in mind when writing your preheaders:

1. Calls to action come into play once readers have opened your email.
  - Point your readers in the right direction, whether you want them to subscribe, purchase a product or visit your website.
  - Use strong words so that the reader knows exactly what you are asking of them, but make sure it reflects your company’s brand voice and that every call to action exhibits some sort of value to the consumer.
  - Preheader should be no more than 85 characters and have some sort of descriptive call to action that supports the subject line.

2. Email and landing sites to which you direct your users to should be mobile optimized:
  - No interstitial boxes
  - Large form-fields
  - Easy navigation
  - Large text
  - Generous white space
  - Short concise body copy
  - Clear calls to action

## Email size

Make sure to limit your email size. Email bodies larger than 102KB are not only extremely taxing on Braze and SendGrid's servers, but they are also clipped by Gmail and other email clients. We recommend keeping the size of your email under 25KB for just text or 60KB with images.

If you are receiving this error in the editor, you likely have `base64` encoded images that have been embedded in the email itself. However, this is not the most effective way to send emails with images. We highly encourage you to use Braze's image uploader to host images and to reference these images by the `href`.

|   Text Only   | Text With Images |     Email Width    |
|:-------------:|:----------------:|:------------------:|
| 25KB maximum |   60KB maximum   | 600 pixels maximum |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}


## Text length

Refer to the following table for recommended text lengths:

| **Text Specifications** | **Recommended Properties** |
| --- | --- |
| Subject Line Length | 35 characters maximum (for optimal mobile display) (6 to 10 words) |
| Sender Name Length | 25 characters maximum (for optimal mobile display) |
| Preheader Length | 85 characters maximum |
{: .reset-td-br-1 .reset-td-br-2}

## Image size

Refer to the following table for recommended image sizes. Smaller, high quality images will load faster, so it’s recommended to use the smallest asset possible to achieve your desired output.

|     Size    | Header Image Width |  Body Image Width  |   File Types  |
|:-----------:|:------------------:|:------------------:|:-------------:|
| 5MB maximum | 600 pixels maximum | 480 pixels maximum | PNG, JPG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}


## Deep linking

A high percentage of emails are read on mobile devices. Utilizing deep linking is a great practice for engaging with these mobile email recipients. With push notifications and in-app messages, a deep link takes the user directly to a specified destination within an app. 

Email, on the other hand, gives no way of knowing whether recipients have the app installed. As such, providing a deep link to the app could link to an error message for these recipients who do not have the app.

[25]: {{site.baseurl}}/help/best_practices/user_onboarding/#user-onboarding
[61]: {% image_buster /assets/img_archive/preheader_example.png %}
