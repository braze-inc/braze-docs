---
nav_title: Technical Guidelines & Tips
page_order: 9
page_type: reference
description: "This reference page covers technical guideslines and tips when dealing with email validation and HTML tags"
channel: Email
---

# Technical Guidelines & Notes

## Email Validation

Braze automatically adjusts inputted email addresses to trim any whitespace.

Email addresses targeted via the Braze servers must be validated per the [RFC 2822][24] standards.<br>
__In addition to these standards__, Braze does not accept certain characters (noted below) and recognizes them as invalid. 

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

## General Technical Guidelines

- If you would like one email template for both mobile and desktop, keep the width below 500 pixels.
- Use inline style sheets to format your email as CSS or it will not be recognized by Email Service Providers (ESPs).
- Images uploaded to the email template must be less than 5MB and either PNG, JPG, GIF.
- Always use alt-tags for images in case they don't appear in the email (blocked, fail to load, etc.)
- Don't set heights and widths for images as this will cause unnecessary white space in a degraded email.
- Div tags should not be used as most email clients do not support their use. Instead, use nested tables.
- Don’t use JavaScript because it does not work with any ESP.
- Braze improves load times by using a global CDN to host all email images.

## Disallowed HTML Tags

- The following HTML tags are disallowed as they may potentially let malicious code run in the browser. As a result, end-user mail clients often filter emails that contain them.
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

- The following HTML attributes are disallowed as well:
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

## Implementing 'ALT' Tags

Since spam filters watch for both an HTML and a plain text version of a message, utilizing plain text alternatives is a great way to lower your spam score. In addition, ALT texts can serve to complement and in some cases stand in lieu of images included in your email body that may have been filtered out by a user's email provider.

## Setting From and Reply-To Addresses

When setting your "From" addresses, make sure your "From" email domain, matches your sending domain (i.e. marketing.yourdomain.com), failure to do this may result in SPF and DKIM misalignment. All reply-to emails can be set to your root domain. 

[24]: http://tools.ietf.org/html/rfc2822
