---
nav_title: Amp for email
article_title: AMP for Email
alias: /amphtml/
page_order: 11
description: "This reference article provides an overview of AMP for Email and common use cases."
channel:
  - email

---

# AMP for email

> With [AMP for email](https://amp.dev/about/email), you can add interactive elements to your emails and elevate your communications with your customers, delivering a full experience directly to your user's inbox. AMP makes this possible through its use of various components that can be used to help build exciting email offerings such as surveys, feedback questionnaires, voting campaigns, reviews, subscription centers, and more. Tools like these can offer opportunities to increase engagement and retention.

## Requirements

Braze is not responsible for users registering with Google or meeting the necessary security requirements. AMP for email is available for SparkPost and SendGrid only.

| Requirement   | Description |
| --------------| ----------- |
| AMP for email turned on | AMP is available for all users. |
| Gmail account enablement | See [Enabling Gmail account](#enabling-gmail-account). |
| Google sender authentication | Gmail [authenticates the sender](https://developers.google.com/gmail/ampemail/security-requirements#sender_authentication) of AMP emails with DKIM, SPF, and DMARC. These must be set up for your account. <br><br>- [Domain Keys Identified Mail](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) (DKIM) <br>- [Sender Policy Framework](https://en.wikipedia.org/wiki/Sender_Policy_Framework)(SPF)<br>- [Domain-based Message Authentication, Reporting, and Conformance](https://en.wikipedia.org/wiki/DMARC)(DMARC)
| AMP email elements | A compelling AMP email includes the strategic use of various components. Refer to the Essentials tab in the [Components](#components) section below. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Supported email clients

Before you can send AMP emails to users, you must register with our email clients. The registration process involves sending a test AMP HTML email to get approved. Approval times vary from client to client. Follow the registration links for more information.

| Client | Registration Link |
| ------ | -------- |
| Gmail | [Google](https://developers.google.com/gmail/ampemail/register) |
| FairEmail | [FairEmail](https://email.faircode.eu/) |
| Yahoo | [Yahoo](https://senders.yahooinc.com/amp/) |
| Mail.ru | [Mail.ru](https://postmaster.mail.ru/amp/) |

For a full list of supported email clients, refer to [AMP documentation](https://amp.dev/support/faq/email-support).

### Enabling Gmail account

Go to your Gmail settings, and select **Enable Dynamic Email** under **General**.

![An example of Gmail settings with the "Enable dynamic email" checkbox selected.]({% image_buster /assets/img/dynamic-content.png %})

## API usage

You can also use AMP for email with our API. If you use any of the Braze [Messaging endpoints]({{site.baseurl}}/api/endpoints/messaging/) to send an email, add `amp_body` as an object specification as shown below.

### Email object specification

```json
{
  "app_id": (required, string) see app identifier above,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <email@address.com>"),
  "reply_to": (optional, valid email address in the format "email@address.com" - defaults to your workspace's default reply to if not set),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "amp_body": (optional, updates the text-amp-html MIME type) the email body in AMP HTML. The MIME (Multipurpose Internet Mail Extensions) type to be referenced is "text/x-amp-html",
  "body": (required unless email_template_id is given, valid HTML),
  "preheader": (optional*, string) Recommended length 50-100 characters,
  "email_template_id": (optional, string) If provided, we will use the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case we will override the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid key-value hash), extra hash - for SendGrid customers, this will be passed to SendGrid as Unique Arguments,
  "headers": (optional, valid key-value hash), hash of custom extensions headers. Currently, only supported for SendGrid customers,
  "should_inline_css": (optional, boolean), whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
  "attachments": (optional, array), array of JSON objects like [{"file_name","url"}] that define the files you need attached. Your file name's extension will be detected automatically from the URL, which should return the appropriate `Content-Type` as a response header,
}
```

## Creating your AMP email

First, build your AMP email using [components](#components). Next, use the [Braze API](#api-usage) to send your message, making sure to include `amp_body` for your AMP HTML.

In addition to the AMP HTML, we require a regular HTML `body` version and suggest a `plaintext_body` version of your AMP email. All AMP emails are sent out multipart, meaning Braze sends out an email that supports HTML, plaintext, and AMP HTML. This becomes useful in the event that your email is sent via a provider who doesn't yet support AMP for email because the email will automatically default to the appropriate version based on the user and their device.

{% alert note %}
When you're building an AMP email, check that you're in the AMP editor as AMP code should not be added to the HTML editor.
{% endalert %}

Refer to these additional resources:

- [AMP tutorial](https://amp.dev/documentation/guides-and-tutorials/start/create_email?format=email)
- [Sample code](https://gist.github.com/CrystalOnScript/988c3f0a2eb406da27e9d9bf13a8bf73) to see how the final product should look. 
- [AMP email components library](https://amp.dev/documentation/components/?format=email/)

### Components

When building the AMP elements, we recommend you check in with your engineering team and include design resources and elements for an extra layer of polish.

{% tabs %}
  {% tab Essentials %}

Each of these elements is required in the body of your AMP email.

| Component | Description | Example |
|---------|--------------|---------|
| Identification <br><br> `⚡4email` or `amp4email`| Identifies your email as an AMP HTML email. | `<!doctype html>` <br> `<html ⚡4email>` <br> `<head>` |
| Load AMP runtime <br><br> `<script>` | Allows AMP to run in your email using JavaScript. | `<script async src="https://cdn.ampproject.org/v0.js"></script>`|
| CSS Boilerplate | Hides content until AMP is loaded. <br> Email providers who support AMP emails enforce security checks that only allow vetted AMP scripts to run in their clients. | `<style amp4email-boilerplate>body{visibility:hidden}</style>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

  {% endtab %}
  {% tab Dynamic %}

Use these components to create dynamic layouts and behaviors in your emails.

| Component | Description | Required Script |
|---------|--------------|---------|
| [Accordion](https://amp.dev/documentation/components/amp-accordion?format=email) <br><br> `amp-accordion`| Allows users to view the content outline and jump to any section. | `<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>` |
| [Forms](https://amp.dev/documentation/components/amp-form?format=email) <br><br> `amp-form`| Create forms to submit input fields in an AMP document. | `<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Any component that requires authenticating the user must use [Google access tokens](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) or [proxy assertion tokens](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}
  {% endtab %}
  {% tab Creative %}

  Get fancy with AMP's components that can help you cater your email to your audience.

| Component | Description | Required Script |
|---------|--------------|---------|
| [Animated Image](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-anim`| Displays an animated image (usually a GIF) managed via runtime. | `<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>` |
| [Carousel](https://amp.dev/documentation/components/amp-carousel?format=email) <br><br> `amp-carousel`| Displays multiple similar pieces of content along a horizontal axis. | `<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>` |
| [Image](https://amp.dev/documentation/components/amp-img?format=email) | A runtime-managed replacement for the HTML `img` tag. <br>  You can also create a [lightbox for your image](https://amp.dev/documentation/components/amp-image-lightbox?format=email). | `<amp-img alt="A view of the sea"` <br> `src="images/sea.jpg"` <br> `width="900"` <br>  `height="675"` <br>  `layout="responsive">`  <br> `</amp-img>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Any component that requires authenticating the user must use [Google access tokens](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) or [proxy assertion tokens](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

  {% endtab %}
  {% tab Other %}

| Component | Description |
|---------|--------------|
| [Data Binding & Expressions](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-bind`| Adds custom stateful interactivity to your AMP pages via data binding and JavaScript-like expressions. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Any component that requires authenticating the user must use [Google access tokens](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) or [proxy assertion tokens](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

{% endtab %}
{% endtabs %}

For a full list of AMP components, check out [AMP documentation](https://amp.dev/documentation/components/?format=email).  

### Use cases

{% tabs local %}
{% tab Interactive Surveys %}

Using the `<amp-form>` component, you can create interactive surveys that can be completed without leaving the email inbox. This can be done by using `<amp-form>` to submit the survey response, and then have your backend supply this aggregate data. 

Some examples include:
* Conference survey email
* Dynamically updating items in the feed
* Article bookmark email

Using this component, users can submit or clear field values. Also, depending on how you set up your email, you can give additional prompts to users, such as whether or not the survey submission was successful, or render the responses from your users showing survey results (such as a voting campaign).

{% endtab %}
{% tab Collapsable Content %}

Expand your content sections using the `<amp-accordion>` component. This component allows you to display collapsible and expandable content sections providing a way for viewers to glance at the content outline and jump to any section. 

If you tend to send long educational articles or personalized recommendations, this provides a way for viewers to glance at the content outline and jump to any section or specific product recommendation to get more details. This can be particularly helpful for mobile users where even a few sentences into a section require scrolling.
{% endtab %}
{% tab Image Heavy Emails %}

If you tend to send emails with many professional photos like retail brands, you can use the `<amp-image-lightbox>` component that allows users to engage with an image that appeals to them. When the user clicks the image, this component displays the image in the center of the message creating a lightbox effect. 

In addition, the `<amp-image-lightbox>` component allows the user to view a detailed image description. You can use the same component for more than one image. For example, if you have multiple images included in your email when the user clicks either image, the image displays in the lightbox.

{% endtab %}
{% tab Font Driven Emails %}

For emails that mostly rely on text copy, the `<amp-fit-text>` component allows you to manage the size and fit of text within a specified area.

Examples include:

- Scaling the text to fit an area
- Scaling the text to fit the area using a maximum font size where you can set the maximum font size
- Truncating the text when content overflows area

{% endtab %}
{% endtabs %}

### Using amp-mustache

Similar to Liquid, AMP supports a scripting language for more advanced use cases. This component is called [`amp-mustache`](https://amp.dev/documentation/components/amp-mustache/?format=email). When including any Mustache markup language, you'll need to wrap it around the [`raw`](https://shopify.github.io/liquid/tags/raw/) tag from Liquid. Note that Liquid and Mustache share syntax styling. 

By wrapping your content around the `raw` tag, the Braze processing engine will ignore any content between the `raw` tags and send out the Mustache variable your team needs.

## Metrics and analytics

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metric</th>
            <th>Details</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Total Opens</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Opens' %} For AMP emails, this is the total opens for the HTML and plaintext versions.</td>
        </tr>
        <tr>
            <td class="no-split">Total Clicks</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Clicks' %} For AMP emails, this is the total clicks in the HTML and plaintext versions.</td>
        </tr>
        <tr>
            <td class="no-split">AMP Opens</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split">AMP Clicks</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}</td>
        </tr>
    </tbody>
</table>

## Testing and troubleshooting

Note that total clicks and unique clicks don't account for any clicks that occur from an AMP message (HTML and plaintext only). AMP-specific clicks are attributed to the *amp_click* metric.

Before you send your AMP email, we recommend that you test according to these [Gmail guidelines](https://developers.google.com/gmail/ampemail/testing-dynamic-email).

For your AMP email to be delivered to any Gmail account, the email must meet the following conditions:

- The AMP for email security requirements must be met.
- The AMP MIME part must contain a valid AMP document.
- The email should include the AMP MIME part before the HTML MIME part.
- The AMP MIME part must be smaller than 100&nbsp;KB.

If none of these conditions are causing the error, reach out to [Support]({{site.baseurl}}/support_contact/).

### Frequently asked questions

#### Should I segment with AMP emails?

We advocate not segmenting to send to all different types of users. This is because we send AMP messages in multipart, having different versions included in the original email. If a user can't see the AMP version, it will default back to HTML. 


