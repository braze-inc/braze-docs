---
nav_title: Email Guidelines & Tips
article_title: Email Guidelines & Tips
page_order: 1
page_type: reference
description: "This article covers content-specific, styling, and technical tips and tricks for various email use cases."
channel: email

---

# Email Guidelines & Tips

> This article covers technical, styling, and content-specific tips and tricks for various email use cases and topics.

## Technical Guidelines

### General

- If you would like one email template for both mobile and desktop, keep the width below 500 pixels.
- Use inline style sheets to format your email as CSS or it will not be recognized by Email Service Providers (ESPs).
- Images uploaded to the email template must be less than 5MB and either PNG, JPG, GIF.
- Always use alt-tags for images in case they don't appear in the email (blocked, fail to load, etc.)
- Don't set heights and widths for images as this will cause unnecessary white space in a degraded email.
- Div tags should not be used as most email clients do not support their use. Instead, use nested tables.
- Don’t use JavaScript because it does not work with any ESP.
- Braze improves load times by using a global CDN to host all email images.

### Email Validation

Braze automatically adjusts inputted email addresses to trim any whitespace. Email addresses targeted via the Braze servers must be validated per the [RFC 2822][24] standards.
In addition to these standards, Braze does not accept certain characters (noted below) and recognizes them as invalid.

If an email is bounced, Braze marks the email as invalid and the subscription status is not changed.
{% details Unaccepted characters outside of RFC Standards %}
- *
- /
- ?
- !
- $
- #
- %
- &#94;
- &
- (
- )
- {
- }
- [
- ]
- ~
- ,
{% enddetails %}

### Disallowed HTML Tags

The following HTML tags are disallowed as they may potentially let malicious code run in the browser. As a result, end-user mail clients often filter emails that contain them.
- `<!doctype>`
- `<applet>`
- `<bgsound>`
- `<embed>`
- `<frameset>`
- `<iframe>`
- `<ilayer>`
- `<layer>`
- `<link>`
- `<meta>`
- `<object>`
- `<script>`
- `<title>`
- `<xml>`
- `<svg>`

The following HTML attributes are disallowed as well:

- `<animationend>`
- `<animationiteration>`
- `<animationstart>`
- `<data-bind>`
- `<fscommand>`
- `<onabort>`
- `<onabort>`
- `<onactivate>`
- `<onafterprint>`
- `<onafterupdate>`
- `<onbeforeactivate>`
- `<onbeforecopy>`
- `<onbeforecut>`
- `<onbeforedeactivate>`
- `<onbeforeeditfocus>`
- `<onbeforepaste>`
- `<onbeforeprint>`
- `<onbeforeunload>`
- `<onbeforeupdate>`
- `<onbegin>`
- `<onblur>`
- `<onbounce>`
- `<oncanplay>`
- `<oncanplaythrough>`
- `<oncellchange>`
- `<onchange>`
- `<onclick>`
- `<oncontextmenu>`
- `<oncontrolselect>`
- `<oncopy>`
- `<oncut>`
- `<ondataavailable>`
- `<ondatasetchanged>`
- `<ondatasetcomplete>`
- `<ondblclick>`
- `<ondeactivate>`
- `<ondrag>`
- `<ondragdrop>`
- `<ondragend>`
- `<ondragenter>`
- `<ondragleave>`
- `<ondragover>`
- `<ondragstart>`
- `<ondrop>`
- `<ondurationchange>`
- `<onemptied>`
- `<onend>`
- `<onended>`
- `<onerror>`
- `<onerror>`
- `<onerrorupdate>`
- `<onfilterchange>`
- `<onfinish>`
- `<onfocus>`
- `<onfocusin>`
- `<onfocusout>`
- `<onhashchange>`
- `<onhelp>`
- `<oninput>`
- `<oninvalid>`
- `<onkeydown>`
- `<onkeypress>`
- `<onkeyup>`
- `<onlayoutcomplete>`
- `<onload>`
- `<onloadeddata>`
- `<onloadedmetadata>`
- `<onloadstart>`
- `<onlosecapture>`
- `<onmediacomplete>`
- `<onmediaerror>`
- `<onmessage>`
- `<onmousedown>`
- `<onmouseenter>`
- `<onmouseleave>`
- `<onmousemove>`
- `<onmouseout>`
- `<onmouseover>`
- `<onmouseup>`
- `<onmousewheel>`
- `<onmove>`
- `<onmoveend>`
- `<onmovestart>`
- `<onoffline>`
- `<ononline>`
- `<onopen>`
- `<onoutofsync>`
- `<onpagehide>`
- `<onpageshow>`
- `<onpaste>`
- `<onpause>`
- `<onplay>`
- `<onplaying>`
- `<onpopstate>`
- `<onprogress>`
- `<onpropertychange>`
- `<onratechange>`
- `<onreadystatechange>`
- `<onredo>`
- `<onrepeat>`
- `<onreset>`
- `<onresize>`
- `<onresizeend>`
- `<onresizestart>`
- `<onresume>`
- `<onreverse>`
- `<onrowdelete>`
- `<onrowexit>`
- `<onrowinserted>`
- `<onrowsenter>`
- `<onscroll>`
- `<onsearch>`
- `<onseek>`
- `<onseeked>`
- `<onseeking>`
- `<onselect>`
- `<onselectionchange>`
- `<onselectstart>`
- `<onshow>`
- `<onstalled>`
- `<onstart>`
- `<onstop>`
- `<onstorage>`
- `<onsubmit>`
- `<onsuspend>`
- `<onsyncrestored>`
- `<ontimeerror>`
- `<ontimeupdate>`
- `<ontoggle>`
- `<ontouchcancel>`
- `<ontouchend>`
- `<ontouchmove>`
- `<ontouchstart>`
- `<ontrackchange>`
- `<onundo>`
- `<onunload>`
- `<onurlflip>`
- `<onvolumechange>`
- `<onwaiting>`
- `<onwheel>`
- `<seeksegmenttime>`
- `<transitionend>`

### Implementing 'ALT' Tags

Since spam filters watch for both an HTML and a plain text version of a message, utilizing plain text alternatives is a great way to lower your spam score. In addition, ALT texts can serve to complement and in some cases stand in lieu of images included in your email body that may have been filtered out by a user's email provider.

### Setting From and Reply-To Addresses

When setting your "From" addresses, make sure your "From" email domain, matches your sending domain (i.e. `marketing.yourdomain.com`), failure to do this may result in SPF and DKIM misalignment. All reply-to emails can be set to your root domain. 

## Styling Tips

### Address Styling

- The **Subject Line** is one of the first things that recipients will see upon receiving your message.
  - Keeping it to 6 to 10 words will yield the highest open rates.
  - There are also different approaches to creating a good subject line, ranging from asking a question to pique the reader’s interest or being more direct, to personalizing it as to engage your clientele.
  - Don’t just stick with one subject line, try new ones out and gauge their effectiveness.
  - Subject line should be no more than 35 characters to display appropriately on mobile.

- The **“From Field”** should clearly show who the sender is.
  - Try not to use an unknown person’s name or an uncommon abbreviation, instead try using something recognizable like the company name.
  - If using a person’s name suits your company methods of personalizing email, stay consistent and retain the same “From Name” to develop a relationship with the recipient.
  -  “From” name should be no more than 25 characters to display appropriately on mobile.

### Body Styling

- Many users use **Email Previewing**, either in Gmail or Outlook.
  - These preview areas generally allow for around 300 pixels or 85 characters of content to be shown.
  - It is recommended that the email communicate the main point of the message efficiently within that space, engaging the reader’s interest to encourage opens.

- **No-reply** email addresses are generally not recommended for multiple reasons as they disengage your readers.
  - Many recipients reply to the email to unsubscribe, so if they are not allowed to do that, the next course of action is more often than not marking the email as spam.
  - Getting out of office replies can actually provide valuable information, increasing open rates and decreasing spam reports (by removing those who don’t want to be emailed).
  - On a personal level, a no-reply can appear impersonal, lazy and arrogant to recipients (suggesting “You aren’t worth my time”), and may turn them off from receiving further email from your company.

- **Preheader Text** is often used by email marketers to provide additional information on an email's contents.
  - A preheader is the preview text displayed immediately after an email subject. In the example below, the preheader is `- Brand. New. Lounge Shorts`.

![Preheader Example][61]

  - The amount of visible preheader text is dependent on the User's email client and the length of the email's subject line. Generally, we suggest email preheaders to be between 50 and 100 characters.

### Preheader Character Limits

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


  Source: [Email on Acid][62]


- **Call to actions** come into play once readers have opened your email.
  - Point your readers in the right direction, whether you want them to subscribe, purchase a product or visit your website.
  - Use strong words so that the reader knows exactly what you are asking of them, but make sure it reflects your company’s brand voice and that every call to action exhibits some sort of value to the consumer.
  - Pre-header should be no more than 85 characters and have some sort of descriptive call to action that supports the subject line.

- **Email and landing sites** to which you direct your users to should be mobile optimized:
  - No interstitial boxes
  - Large form-fields
  - Easy navigation
  - Large text
  - "Finger Friendly"
  - Generous white space
  - Short concise body copy
  - Clear calls to action

### Email Size

|   Text Only   | Text With Images |     Email Width    |
|:-------------:|:----------------:|:------------------:|
| 25KB maximum |   60KB maximum   | 600 pixels maximum |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Make sure to limit your **Body Size**: Large E-Mail bodies (larger than 102kb) are not only extremely taxing on Braze and SendGrid's servers, but are also clipped by Gmail and other E-Mail clients. We recommend keeping the size of your email under 25kb for just text, or 60kb with images.

If you are receiving this error in the editor, you likely have base64 encoded images that have been embedded in the email itself. This is not an effective way to send emails with images. We highly encourage you to use Braze's image uploader to host images and to reference these images by href.

### Text Length

**Text Specifications** | **Recommended Properties**
--- | ---
Subject Line Length | 35 characters maximum (for optimal mobile display) (6 to 10 words)
Sender Name Length | 25 characters maximum (for optimal mobile display)
Pre-Header Length | 85 characters maximum
{: .reset-td-br-1 .reset-td-br-2}

### Image Size

|     Size    | Header Image Width |  Body Image Width  |   File Types  |
|:-----------:|:------------------:|:------------------:|:-------------:|
| 5MB maximum | 600 pixels maximum | 480 pixels maximum | PNG, JPG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

Smaller, high quality images will load faster, so it’s recommended to use the smallest asset possible to achieve your desired output.

### Deep Linking

A high percentage of emails are read on mobile devices. Utilizing deep linking is a great practice for engaging with these mobile email recipients. With push notifications and in-app messages, a deep link takes the user directly to a specified destination within an app. Email, on the other hand, gives no way of knowing whether recipients have the app installed. As such, providing a deep link to the app could link to an error message for these recipients who do not have the app.

## Content-Specific Tips & Tricks

### Onboarding

- Provide tips to help users get started.
- Showcase only the most essential features - too much information can be overwhelming and potentially confusing if the user is still unfamiliar with your app.
- Provide links to your documentation and let users know how they can get support.
- Try to always send a welcome email after a user signs up. Below is an example from LivingSocial that contains simple but clear calls to action and lets users know about a deal:

![LivingSocial email][26]{: style="max-width:70%;"}

### Sales and Promotional

- Within seconds of opening your email, users should know the value of the promotion (what the discounts are and what is on sale) and how long the offer lasts.
- Provide graphics to illustrate any products that you're promoting.
- Keep your copy concise and simple so that it doesn't clutter your email and distract users from the essential content.
- Make your call to action clear and give recipients an easy way to immediately participate in the promotion.
- If you're recommending certain products, try to present them as curated, personal suggestions that the user may like.
- Use social proof to promote your products. Show users any items their friends have liked or purchased.
- If you're promoting a limited time offer, be sure to let users know! Ideeli does a great job at conveying urgency in this email:

![Ideeli email][27]{: style="max-width:70%;"}

### Transactional

- If the user just made an in-app purchase, you should thank them and provide any tips that can help them make the most of that purchase.
- If the user just made an out-of-app purchase, provide them with shipping confirmation and a way to ask questions about their shipment.
- Asking users to give feedback after a purchase is a good way to solicit input without being pushy. Because you've just provided users with a service, they may be more likely to share their thoughts. Here's an example of an email from Restaurant.com:

![Restaurant email][28]{: style="max-width:80%;"}

### Retention

- Keep your tone friendly.
- This may be your last chance to win users back, so be sure to include content that showcases your app's value.
- If the user has been relatively inactive since installing, offer helpful hints for getting started.
- For social apps, keep users updated on their friends' activities.
- Offer discounts or any other incentives that may bring users back.
- Try to make your message personal to show the user that he is still valued. Rue La La, for instance, frames its retention email as a note from its CEO:

![Ruelala email][29]{: style="max-width:80%;"}

### Social

- Email can help you build up a social fanbase by directing recipients toward your Facebook, Twitter, Instagram, Pinterest, Youtube channel, etc.
- Include links to your social media accounts within the email to make it easy for users to connect.
- Make it fun! Try running a photo contest, promoting a hashtag, or having a giveaway. Below is an email from Hailo that offers a reward for participating in photo challenges:

![Hailo social email][30]{: style="max-width:70%;"}

### Updates

- Send updates of new or improved features to all of your users.
- Updating users on new features is also a re-engagement tool because it reminds lapsing users of your app's value.
- If your feature requires an explanation or demo, include a link in the message. Here's an example by Allrecipes.com:

![Allrecipes email][31]{: style="max-width:70%;"}


[25]: {{site.baseurl}}/help/best_practices/user_onboarding/#user-onboarding
[26]: {% image_buster /assets/img_archive/Livingsocial_email.png %}
[27]: {% image_buster /assets/img_archive/Ideeli_email.png %}
[28]: {% image_buster /assets/img_archive/Restaurant_email.png %}
[29]: {% image_buster /assets/img_archive/Ruelala_email.png %}
[30]: {% image_buster /assets/img_archive/Hailo_social_email.png %}
[31]: {% image_buster /assets/img_archive/Allrecipes_email.png %}


[24]: http://tools.ietf.org/html/rfc2822
[61]: {% image_buster /assets/img_archive/preheader_example.png %}
[62]: https://www.emailonacid.com/blog/article/email-marketing/preview-vs-preheader-text-how-long-should-preheader-text-be/