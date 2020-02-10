---
nav_title: Technical Guidelines & Tips
page_order: 9
page_type: reference
description: "This reference page covers technical guideslines and tips when dealing with email validation and HTML tags"
channel: Email
---

# Technical Guidelines & Notes

## Email Validation

{% alert important %}
This validation is done for both user email addresses and the from-address of an email message.
{% endalert %}

Braze validates the email address using the following Ruby Gem: https://github.com/afair/email_address.  
The Gem is set to relaxed mode and configured to accept UTF-8 character.

Email Validation looks at both the Local and Host Domain part of an address.
Local part is anything before the @ symbol
Host Domain part is anything after the @ symbol


### Local part Validation Rules
#### Microsoft Domains
If the host domain is has “msn, hotmail, outlook, live” then the following is allowed for the local part

Regex: \A[a-z][\-\w]*(?:\.[\-\w]+)*\z

**Regex explanation:**
1. Local part must start with a character (a-z)
2. Local part can contain any character or number (a-z or 0-9)
3. can contain the following characters (**.**) or (**-**)
4. can not end with a period (**.**)
5. cannot contain two or more consecutive periods (**.**)


##### All other domains
For all other domains, Braze allows the following for the local part

Regex: /\A [\p\{L}\p\{N}_]+ (?: [\.\-\+\'_]+ [\p\{L}\p\{N}_]+ )* \z/x

**Regex explanation:**
1. Local part can contain any letter, number or underscore, including Unicode letters and numbers
2. can contain but may not start or end with the following characters: (**.**) (**-**) (**+**) or (**'**)


### Host part validation Rules
ipv4 or ipv6 addresses are not allowed in the host domain part of the email address

Regex: / [\p{L}\p{N}]+ (?: (?: \-{1,2} | \.) [\p{L}\p{N}]+ )*/x

**Regex explanation:**
1. host domain must start with a alphanumeric character (a-z or 0-9)
2. host domain can only contain one period “.”
3. host domain must end with a top level domain
4. the top level domain is determined by anything after the ‘.’ and can only contain alphanumeric characters (a-z or 0-9)
5. can contain the following characters: (**.**) or (**?**)

{% alert important %}
Unicode is accepted for both the local and host domain part of the email address.
{% endalert %}

If an email is bounced, Braze marks the email as invalid and the subscription status is not changed.


## General Technical Guidelines

- If you would like one email template for both mobile and desktop, keep the width below 500 pixels.
- Use inline style sheets to format your email as CSS or it will not be recognized by Email Service Providers (ESPs).
- Images uploaded to the email template must be less than 5MB and either PNG, JPG, GIF.
- Always use alt-tags for images in case they don't appear in the email (blocked, fail to load, etc.)
- Don't set heights and widths for images as this will cause unnecessary white space in a degraded email.
- Div tags should not be used as most email clients do not support their use. Instead, use nested tables.
- Don’t use Javascript because it does not work with any ESP.
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

[24]: http://tools.ietf.org/html/rfc2822
