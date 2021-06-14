---
nav_title: AMP for Email
alias: /amphtml/
hidden: true
---

# AMP for Email

With [AMP for Email](https://amp.dev/about/email), you can add interactive elements to your emails and elevate your communications with your customers to a whole new level.

## Requirements

Braze is not responsible for the customer registering with Google or meeting the necessary security requirements.

Requirement   | Description
--------------| -----------
Gmail Account Enablement | [See below.](#enabling-gmail-account)
Google Sender Authentication | Gmail authenticates the sender of AMP emails with [Domain Keys Identified Mail](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail), [Sender Policy Framework](https://en.wikipedia.org/wiki/Sender_Policy_Framework), and [Domain-based Message Authentication, Reporting, and Conformance](https://en.wikipedia.org/wiki/DMARC). <br> Learn more [here](https://developers.google.com/gmail/ampemail/security-requirements#sender_authentication).
AMP Email Elements | Check out the Essentials tab in the [Components](#components) section below. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
At this time, only Gmail provides support for AMP for Email. [Register with Google here](https://developers.google.com/gmail/ampemail/register).
{% endalert %}

### Enabling Gmail Account

Go into your Gmail Settings and select `Enable Dynamic Content`.

![Dynamic Content][1]

## API Usage

You can utilize AMP for Email using our API. When you use any of [our Messaging Endpoints]({{site.baseurl}}/api/endpoints/messaging/) to send an email, add `amp_body` as an object specification, as shown below.

### Email Object Specification

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

## Writing Your AMP Email

Construct your AMP email using the [components](#components) below, then use [our API](#api-usage) to send. Be sure to use `amp_body` for your AMP HTML! You can also check out [AMP's tutorial](https://amp.dev/documentation/guides-and-tutorials/start/create_email?format=email) or [sample code](https://gist.github.com/CrystalOnScript/988c3f0a2eb406da27e9d9bf13a8bf73) to see how the final product should look. You can also checkout AMP's [full email components library here](https://amp.dev/documentation/components/?format=email/).

When you write your email for our API, we __require__ a regular HTML `body` version and suggest a `plaintext_body` version of your AMP email, in the event that your email is sent via a provider who does not yet support AMP for Email.

### Components

{% tabs %}
  {% tab Essentials %}

These are what makes an AMPHTML Email... AMP'ed! Each of these elements are required in the body of your AMP email.

| Component | What It Does | Example |
|---------|--------------|---------|
| Identification <br> `⚡4email` or `amp4email`| Identifies your email as an AMPHTML email. | `<!doctype html>` <br> `<html ⚡4email>` <br> `<head>` |
| Load AMP runtime <br> `<script>` | Allows AMP to fun within your email using JavaScript. | `<script async src="https://cdn.ampproject.org/v0.js"></script>`|
| CSS Boilerplate | Hides content until AMP is loaded. <br> Email providers who support AMP emails enforce fierce security checks that only allow vetted AMP scripts to run in their clients| `<style amp4email-boilerplate>body{visibility:hidden}</style>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

  {% endtab %}
  {% tab Dynamic %}

Want to see something cool? Oh wait - that's your email. Use these components to create dynamic layouts and behaviors in your emails.

| Component | What It Does | Required Script |
|---------|--------------|---------|
| [Accordion](https://amp.dev/documentation/components/amp-accordion?format=email) <br> `amp-accordion`| Lets your users glance at the content outline and jump to any section. | `<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>` |
| [Forms](https://amp.dev/documentation/components/amp-form?format=email) <br> `amp-form`| Create forms to submit input fields in an AMP document. | `<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
Any component that requires authenticating the user must use [Google Access Tokens](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) or [Proxy Assertion Tokens](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}
  {% endtab %}
  {% tab Creative %}

  Get fancy with AMP's components that help you cater more to the eye of the beholder.

| Component | What It Does | Required Script |
|---------|--------------|---------|
| [Animated Image](https://amp.dev/documentation/components/amp-anim?format=email) <br> `amp-anim`| Display an animated image (usually a GIF) managed via runtime. | `<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>` |
| [Carousel](https://amp.dev/documentation/components/amp-carousel?format=email) <br> `amp-carousel`| Display multiple similar pieces of content along a horizontal axis. | `<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>` |
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
| [Data Binding & Expressions](https://amp.dev/documentation/components/amp-anim?format=email) <br> `amp-bind`| Adds custom stateful interactivity to your AMP pages via data binding and JS-like expressions. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
Any component that requires authenticating the user must use [Google Access Tokens](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) or [Proxy Assertion Tokens](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

  {% endtab %}
{% endtabs %}

### Using amp-mustache

Similar to Liquid, AMP supports a scripting language for more advanced use cases.  This component is called [amp-mustache](https://amp.dev/documentation/components/amp-mustache/?format=email).  When including any Mustache mark-up language you will need to wrap it around the [raw](https://shopify.github.io/liquid/tags/raw/) tag from Liquid.  Unfortunately Liquid (the markup language used here at Braze) and Mustache share syntax styling. 

By wrapping your content around the Raw tag, the Braze processing engine will correctly ignore any content between the raw tags and send out the Mustache variable your team needs.


### Metrics and Analytics

| Metric | Details |
|---|---|
| Total Opens | Total opens for the HTML and plaintext versions of your AMP Email. |
| Total Clicks | Total clicks in the HTML and plaintext versions of your AMP Email. |
| AMP Opens | Total count for opens in your AMP HTML Email, cumulative count of the HTML, plaintext, and AMPHTML versions of the email. |
| AMP Clicks | Total count for clicks in your AMP HTML Email, cumulative count of the HTML, plaintext, and AMPHTML versions of the email. |
{: .reset-td-br-1 .reset-td-br-2}  

- Please note that total clicks and unique clicks do not account for any click that happened from an AMP message (HTML and Plaintext only). AMP specific clicks are attributed to the `amp_click` metric.

### Testing & Troubleshooting

Before your send your AMP email, we recommend that you test according to [Gmail's guidelines here](https://developers.google.com/gmail/ampemail/testing-dynamic-email).

For your AMP email to be delivered to any Gmail account, the email must meet the following conditions:
- The AMP for Email security requirements must be met (see table above).
- The AMP MIME part must contain a valid AMP document.
- The email should include the AMP MIME part before the HTML MIME part.
- The AMP MIME part must be smaller than 100KB.

If none of these conditions are causing error, reach out to [support][support].

 [1]: {% image_buster /assets/img/dynamic-content.png %} "Dynamic Content"
 [support]: {{site.baseurl}}/support_contact/
