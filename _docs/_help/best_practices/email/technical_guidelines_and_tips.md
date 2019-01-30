---
nav_title: Technical Guidelines & Tips
page_order: 9
---

# Technical Guidelines & Notes

## Email Validation

Braze automatically adjusts inputted email addresses to trim any whitespace.

Email addresses targeted via the Braze servers must be validated per the [RFC 2822][24] standards.  If an email is bounced, Braze automatically unsubscribes the corresponding email address but does not remove the email address from user profiles.

## General Technical Guidelines

- If you would like one email template for both mobile and desktop, keep the width below 500 pixels.
- Use inline style sheets to format your email as CSS or it will not be recognized by Email Service Providers (ESPs).
- Images uploaded to the email template must be less than 5MB and either PNG, JPG, GIF.
- Always use alt-tags for images in case they don't appear in the email (blocked, fail to load, etc.)
- Don't set heights and widths for images as this will cause unnecessary white space in a degraded email.
- Div tags should not be used as most email clients do not support their use. Instead use nested tables.
- Don’t use Javascript because it does not work with any ESP.
- Braze improves load times by using a global CDN to host all email images.

## Disallowed HTML Tags

- The following HTML tags are disallowed as they may potentially let malicious code run in the browser. As a result, end user mail clients often filter emails which contain them.
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

## Email Services {#email-services}

If you need additional support with your email program, we offer recurring and one-time services at an additional cost. For more information reach out to your Account Manager.

### Premium Deliverability Services {#premium-deliverability-services}

We offer two tiers of recurring email support: Premium Deliverability Services and Deliverability Monitoring.

Services Description:

- Audit of historical/current email sending practices with a review of targeting, cadence, and messaging strategies
- Whitelabel configuration and customized IP warming plan created by an email deliverability expert
  - Regular check-in calls during your first month (three times per week for Premium Deliverability and once per week for Deliverability Monitoring)
- Regular call with deliverability expert (twice per month for Premium Deliverability and monthly Deliverability Monitoring) to provide:
  - Monitoring of deliverability performance by domain
  - Recommendations to improve email program performance and results utilizing data and established best practices
- Crisis Triage - in the event of a deliverability issue, like a block or blacklist, our team will help mitigate and remediate

## Enhanced Onboarding {#enhanced-onboarding}

You can also have a deliverability expert help guide the first month of your email onboarding:

- Audit of historical/current email sending practices with a review of targeting, cadence, and messaging strategies
- Whitelabel configuration and customized IP warming plan created by an email deliverability expert
  - Check-in calls three times per week during your first month

[18]: {% image_buster /assets/img_archive/Email_IP_Warming_Sends_Limit_new.png %}
[19]: {{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[20]: {% image_buster /assets/img_archive/Email_Sunset_Policies_new.png %}
[21]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns
[22]: {{ site.baseurl }}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[23]: {{ site.baseurl }}/help/best_practices/spam_regulations/#spam-regulations
[24]: http://tools.ietf.org/html/rfc2822
[25]: {{ site.baseurl }}/help/best_practices/user_onboarding/#user-onboarding
[26]: {% image_buster /assets/img_archive/Livingsocial_email.png %}
[27]: {% image_buster /assets/img_archive/Ideeli_email.png %}
[28]: {% image_buster /assets/img_archive/Restaurant_email.png %}
[29]: {% image_buster /assets/img_archive/Ruelala_email.png %}
[30]: {% image_buster /assets/img_archive/Hailo_social_email.png %}
[31]: {% image_buster /assets/img_archive/Allrecipes_email.png %}
[33]: {% image_buster /assets/img_archive/Multiple_click_tracking_screen_3a.png %}
[34]: {% image_buster /assets/img_archive/Email_HeatMap_new.png %}
[35]: {% image_buster /assets/img_archive/campaign_data_2.png %}
[36]: #deep-linking
[37]: http://googlewebmastercentral.blogspot.com/2015/05/app-deep-linking-with-googl.html
[38]: {{ site.baseurl }}/help/best_practices/email/#unsubscribed-email-addresses
[39]: {{ site.baseurl }}/help/best_practices/email/#bounces--invalid-emails
[40]: {{ site.baseurl }}/help/best_practices/spam_regulations/#spam-regulations
[42]: https://returnpath.com/
[43]: http://www.briteverify.com/
[44]: https://senderscore.org/
[45]: http://www.senderbase.org/
[46]: {{ site.baseurl }}/help/best_practices/email/#email-sunset-policies
[47]: {% image_buster /assets/img_archive/appusage_ipwarming_main.png %}
[48]: {% image_buster /assets/img_archive/campaign_confirmation_ipwarming.png %}
[49]: {% image_buster /assets/img_archive/canvas_ip_warming.png %}
[50]: {% image_buster /assets/img_archive/targeting_campaign_ipwarming.png %}
[60]: {{ site.baseurl }}/help/best_practices/email/#email-sunset-policies
[61]: {% image_buster /assets/img_archive/preheader_example.png %}
[62]: https://www.emailonacid.com/blog/article/email-development/tips-for-coding-email-preheaders
[63]: {% image_buster /assets/img_archive/email_click_results_heatmap.gif %}
[64]: {{ site.baseurl }}/help/best_practices/email/#unsubscribed-email-addresses
[65]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#primary-conversion-event
