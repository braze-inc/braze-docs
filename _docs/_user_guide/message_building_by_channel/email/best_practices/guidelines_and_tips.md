---
nav_title: Email guidelines
article_title: Email Guidelines
page_order: 1
page_type: reference
description: "This article covers general tips and tricks to keep in mind as you build email campaigns for various use cases and topics."
channel: email

---

# Email guidelines

> As you build your email campaign, it's important to keep in mind how your email messaging is received across your various users and email service providers (ESPs). 

Here are some quick tips to keep in mind while building your content:

- When formatting your email, use inline style sheets as CSS.
- To use one email template for both mobile and desktop versions, keep the width under 500 pixels.
- Images must be under 5&nbsp;MB. We recommend using PNG, JPEG, or GIF for maximum compatibility. Avoid SVG and WebP, as many major email clients do not yet support them.
- Don't set heights and widths for images as this can cause unnecessary white space in a degraded email.
- `div` tags should not be used as most email clients do not support their use. Instead, use nested tables.
- Avoid using JavaScript because it does not work with any ESP.
- Braze improves load times by using a global CDN to host all email images.

### Implementing alternative text

Since spam filters watch for both an HTML and a plain text version of a message, utilizing plain text alternatives is a great way to lower your spam score. In addition, alternative text `(alt="")` can serve to complement and in some cases stand in lieu of images included in your email body that may have been filtered out by a user's email provider. Screen readers announce alt text to explain images, so this is an opportunity to use plain language to provide key information about an image.

### Email validation

{% alert important %}
Validation is used for dashboard email addresses, end-user email addresses (your customers), and from and reply-to addresses done of an email message.
{% endalert %}

Email validation happens when a user's email address is updated or is being imported into Braze by the API, CSV upload, SDK, or modified in the dashboard. Note that your email addresses cannot include whitespaces, and if sent using the API, whitespaces can result in a `400` error.

Email addresses targeted via the Braze servers must be validated per [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822) standards, Braze does not accept certain characters and recognizes them as invalid. If an email is bounced, Braze marks the email as invalid and the subscription status is not changed. 

For information about disallowed characters and email validation rules, see [Email validation]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/#how-it-works).

### Setting from and reply-to addresses

When setting your "from" addresses, make sure your "from" email domain matches your sending domain (such as `marketing.yourdomain.com`). Failure to do this may result in SPF and DKIM misalignment. All reply-to emails can be set to your root domain.

{% alert note %}
Unicode encoding is not supported in "from" addresses.
{% endalert %}

### Checking HTML details

Keep in mind that some HTML tags and attributes are not allowed as they may potentially let malicious code run in the browser.

Check out the following lists for HTML tags and attributes that aren't allowed in your emails:
{% details Expand for disallowed HTML tags %}
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
{% enddetails %}

{% details Expand for disallowed HTML attributes %}
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
{% enddetails %}



