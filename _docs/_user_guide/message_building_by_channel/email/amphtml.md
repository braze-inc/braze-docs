---
nav_title: AMP for Email
article_title: AMP for Email
alias: /amphtml/
page_order: 9
description: "This reference article provides an overview of AMP for Email and common use cases."
channel:
  - email

---

# AMP for email

> With [AMP for Email](https://amp.dev/about/email), you can add interactive elements to your emails and elevate your communications with your customers, delivering a full experience directly to your user's inbox. 

AMP makes this possible through its use of various components that can be used to help build exciting in email offerings such as surveys, feedback questionnaires, voting campaigns, reviews, subscription centers, and more! Tools like these offer significant opportunities to increase engagement and retention. 

{% alert important %}
AMP for Email is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

## Requirements

Braze is not responsible for the customer registering with Google or meeting the necessary security requirements.

| Requirement   | Description |
| --------------| ----------- |
| AMP for Email Turned On | AMP is available for everyone. Please reach out to your Customer Success Manager and they can work with our product team to enable this feature for you. |
| Gmail Account Enablement | See [Enabling Gmail Account](#enabling-gmail-account) Below. |
| Google Sender Authentication | Gmail authenticates the sender of AMP emails with DKIM, SPF, and DMARC. These must be set up for your account, learn more [here](https://developers.google.com/gmail/ampemail/security-requirements#sender_authentication). <br><br>- [Domain Keys Identified Mail](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) (DKIM) <br>- [Sender Policy Framework](https://en.wikipedia.org/wiki/Sender_Policy_Framework)(SPF)<br>- [Domain-based Message Authentication, Reporting, and Conformance](https://en.wikipedia.org/wiki/DMARC)(DMARC)
| AMP Email Elements | A compelling AMP Email includes the strategic use of various components.<br>Check out the Essentials tab in the [Components](#components) section below. |
{: .reset-td-br-1 .reset-td-br-2}

### Supported clients

Before you can send AMP Emails to users, you must register with our clients. The registration process involves sending a test AMPHTML email to get approved. Approval times vary client to client. Follow the register links for more information.

| Client | Register Link |
| ------ | -------- |
| Gmail | [Google](https://developers.google.com/gmail/ampemail/register) |
| FairEmail | [FairEmail](https://email.faircode.eu/) |
| Yahoo | [Yahoo](https://senders.yahooinc.com/amp/) |
| Mail.ru | [Mail.ru](https://postmaster.mail.ru/amp/) |

For a full list of supported platforms, visit the [AMP documentation](https://amp.dev/support/faq/email-support). 

### Enabling Gmail account

Go into your Gmail Settings, and under General, check the `Enable Dynamic Email` box.

![Dynamic Content][1]

## API usage

You can utilize AMP for Email using our API. When you use any of [our Messaging Endpoints]({{site.baseurl}}/api/endpoints/messaging/) to send an email, add `amp_body` as an object specification, as shown below.

### Email object specification

```json
{
  "app_id": (required, string) see App Identifier above,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <email@address.com>"),
  "reply_to": (optional, valid email address in the format "email@address.com" - defaults to your app group's default reply to if not set),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "amp_body": (optional, updates the text-amp-html MIME type) the email body in AMPHTML. The MIME (Multipurpose Internet Mail Extensions) type to be referenced is "text/x-amp-html".
  "body": (required unless email_template_id is given, valid HTML),
  "preheader": (optional*, string) Recommended length 50-100 characters.
  "email_template_id": (optional, string) If provided, we will use the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case we will override the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid Key-Value Hash), extra hash - for SendGrid customers, this will be passed to SendGrid as Unique Arguments,
  "headers": (optional, valid Key-Value Hash), hash of custom extensions headers. Currently, only supported for SendGrid customers,
  "should_inline_css": (optional, boolean), whether to inline css on the body. If not provided, falls back to the default css inlining value for the App Group,
  "attachments": (optional, array), array of json objects like [{"file_name","url"}] that define the files you need attached. Your file name's extension will be detected automatically from the URL, which should return the appropriate `Content-Type` as a response header,
}
```

## Writing your AMP email

Construct your AMP email using the [components](#components) below, check out our [example use cases](#example-use-cases), and then use [our API](#api-usage) to send your message! Be sure to use `amp_body` for your AMP HTML! 

You can also check out: 
- [AMP's tutorial](https://amp.dev/documentation/guides-and-tutorials/start/create_email?format=email)
- [Sample code](https://gist.github.com/CrystalOnScript/988c3f0a2eb406da27e9d9bf13a8bf73) to see how the final product should look. 
- [AMP's full email components library](https://amp.dev/documentation/components/?format=email/)

<br>
In addition to the AMPHTML, we __require__ a regular HTML `body` version and suggest a `plaintext_body` version of your AMP email. All AMP Emails are sent out multi-part, meaning Braze sends out an email that supports HTML, Plaintext, and AMPHTML. This becomes useful in the event that your email is sent via a provider who does not yet support AMP for Email, automatically defaulting to the appropriate version based on the user and their device.

### Components

{% tabs %}
  {% tab Essentials %}

These are what makes an AMPHTML Email... AMP'ed! Each of these elements is required in the body of your AMP email.

| Component | What It Does | Example |
|---------|--------------|---------|
| Identification <br><br> `⚡4email` or `amp4email`| Identifies your email as an AMPHTML email. | `<!doctype html>` <br> `<html ⚡4email>` <br> `<head>` |
| Load AMP runtime <br><br> `<script>` | Allows AMP to fun within your email using JavaScript. | `<script async src="https://cdn.ampproject.org/v0.js"></script>`|
| CSS Boilerplate | Hides content until AMP is loaded. <br> Email providers who support AMP emails enforce fierce security checks that only allow vetted AMP scripts to run in their clients| `<style amp4email-boilerplate>body{visibility:hidden}</style>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

  {% endtab %}
  {% tab Dynamic %}

Want to see something cool? Oh wait - that's your email. Use these components to create dynamic layouts and behaviors in your emails.

| Component | What It Does | Required Script |
|---------|--------------|---------|
| [Accordion](https://amp.dev/documentation/components/amp-accordion?format=email) <br><br> `amp-accordion`| Lets your users glance at the content outline and jump to any section. | `<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>` |
| [Forms](https://amp.dev/documentation/components/amp-form?format=email) <br><br> `amp-form`| Create forms to submit input fields in an AMP document. | `<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
Any component that requires authenticating the user must use [Google Access Tokens](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) or [Proxy Assertion Tokens](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}
  {% endtab %}
  {% tab Creative %}

  Get fancy with AMP's components that help you cater more to the eye of the beholder.

| Component | What It Does | Required Script |
|---------|--------------|---------|
| [Animated Image](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-anim`| Display an animated image (usually a GIF) managed via runtime. | `<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>` |
| [Carousel](https://amp.dev/documentation/components/amp-carousel?format=email) <br><br> `amp-carousel`| Display multiple similar pieces of content along a horizontal axis. | `<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>` |
| [Image](https://amp.dev/documentation/components/amp-img?format=email) | A runtime-managed replacement for the HTML `img` tag. <br>  You can also create a [lightbox for your image](https://amp.dev/documentation/components/amp-image-lightbox?format=email). | `<amp-img alt="A view of the sea"` <br> `src="images/sea.jpg"` <br> `width="900"` <br>  `height="675"` <br>  `layout="responsive">`  <br> `</amp-img>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
Any component that requires authenticating the user must use [Google Access Tokens](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) or [Proxy Assertion Tokens](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

  {% endtab %}
  {% tab Other %}

  There's more to the world than those other tabs. Here are some other fun components you should check out.

| Component | What It Does |
|---------|--------------|
| [Data Binding & Expressions](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-bind`| Adds custom stateful interactivity to your AMP pages via data binding and JS-like expressions. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
Any component that requires authenticating the user must use [Google Access Tokens](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) or [Proxy Assertion Tokens](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

{% endtab %}
{% endtabs %}

For a full list of AMP Components, check out the [AMP Documentation](https://amp.dev/documentation/components/?format=email).  

### Example use cases
Below you will find a couple of example use cases for the various components discussed above.

{% tabs local %}
{% tab Interactive Surveys %}
__Interactive Surveys__

Idea: Using the `<amp-form>` component, you can create interactive surveys that can be completed without leaving the email inbox. This can be done by using `<amp-form>` to submit the survey response, and then have your backend supply this aggregate data. 

Some Examples:
* Conference Survey Email
* Dynamically Updating Items in the Feed
* Article bookmark Email

Using this component, users can submit or clear field values. Also, depending on how you set up your email, you can do things like give additional prompts to users such as whether or not the survey submission was successful, or even render the responses from your users showing results of the survey if it makes sense. (i.e a voting campaign)

{% endtab %}
{% tab Collapsable Content %}
__Collapsable Content__

Idea: Expand your content sections using the `<amp-accordion>` component. This component allows you to display collapsible and expandable content sections providing a way for viewers to glance at the content outline and jump to any section. 

If you tend to send long educational articles or personalized recommendations, it provides a way for viewers to glance at the content outline and jump to any section or specific recommended product to get more details. This is also helpful for mobile devices where even a couple of sentences into a section requires scrolling. Effective use reduces scrolling needs on mobile devices.
{% endtab %}
{% tab Image Heavy Emails %}
__Image Heavy Emails__

Idea: If you tend to send emails with a lot of professional photos like retail brands, you can use the `<amp-image-lightbox>` component that allows users to engage with an image that appeals to them. When the user clicks the image, this component displays the image in the center of the message creating a lightbox effect. 

In addition, the `<amp-image-lightbox>`  component allows the user to zoom, pan, or show a more detailed image description. You can use the same component for more than one image. For example, if you have multiple images included in your email when the user clicks either image, the image displays in the lightbox.
{% endtab %}
{% tab Font Driven Emails %}
__Font Driven Emails__

Idea: For emails that mostly rely on text copy, the `<amp-fit-text>` component allows you to manage the size and fit of text within a specified area.

Some examples:
  * Having the text to scale to fit the area
  * Having text scale to fit the area using a maximum font size where you can set the maximum font size. 
  * Having text truncate when content overflows area
{% endtab %}
{% endtabs%}

### Using amp-mustache

Similar to Liquid, AMP supports a scripting language for more advanced use cases.  This component is called [amp-mustache](https://amp.dev/documentation/components/amp-mustache/?format=email).  When including any Mustache mark-up language you will need to wrap it around the [raw](https://shopify.github.io/liquid/tags/raw/) tag from Liquid.  Unfortunately Liquid (the markup language used here at Braze) and Mustache share syntax styling. 

By wrapping your content around the Raw tag, the Braze processing engine will correctly ignore any content between the raw tags and send out the Mustache variable your team needs.

## Metrics and analytics

| Metric | Details |
|---|---|
| Total Opens | Total opens for the HTML and plaintext versions of your AMP Email. |
| Total Clicks | Total clicks in the HTML and plaintext versions of your AMP Email. |
| AMP Opens | Total count for opens in your AMP HTML Email, cumulative count of the HTML, plaintext, and AMPHTML versions of the email. |
| AMP Clicks | Total count for clicks in your AMP HTML Email, cumulative count of the HTML, plaintext, and AMPHTML versions of the email. |
{: .reset-td-br-1 .reset-td-br-2}  

## Testing and troubleshooting

Please note that total clicks and unique clicks do not account for any click that happened from an AMP message (HTML and Plaintext only). AMP specific clicks are attributed to the `amp_click` metric.

Before you send your AMP email, we recommend that you test according to [Gmail's guidelines here](https://developers.google.com/gmail/ampemail/testing-dynamic-email).

For your AMP email to be delivered to any Gmail account, the email must meet the following conditions:
- The AMP for Email security requirements must be met (see table above).
- The AMP MIME part must contain a valid AMP document.
- The email should include the AMP MIME part before the HTML MIME part.
- The AMP MIME part must be smaller than 100KB.

If none of these conditions are causing the error, reach out to [support][support].

### Frequently Asked Questions

{% details Should I segment with AMP Emails? %}
We advocate not segmenting to send to all different types of users. This is because we send AMP messages in multipart, having different versions included in the original email. If you customer can't see the AMP version, it will default back to HTML. 
{% enddetails %}

{% details Any tips as I build out my AMP Emails? %}
Lean on your engineering as much as possible to build out the AMP elements. Once the elements are set up, we encourage you to include whatever design resources and elements you have to add an extra layer of polish. Showcasing some of the things AMP can do in email can be pretty compelling in terms of getting your engineering team to prioritize this.
{% enddetails %}

[1]: {% image_buster /assets/img/dynamic-content.png %} "Dynamic Content"
[support]: {{site.baseurl}}/support_contact/
