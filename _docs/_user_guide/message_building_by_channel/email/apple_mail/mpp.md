---
nav_title: Apple Mail Privacy Protection
article_title: Apple Mail Privacy Protection for iOS 15
page_order: 1
description: "This reference article covers the Apple Mail Privacy Protection privacy update, who will be affected by it, and some next steps to prepare for the feature."
channel:
  - email

---

# Apple's Mail Privacy Protection

## What is Apple's Mail Privacy Protection update?

Apple's Mail Privacy Protection (MPP) is a privacy update that is available for users of the Apple Mail app on iOS 15, iPadOS 15, macOS Monterey, and watchOS 8, released mid-September 2021. For users who opt-in to MPP (which we predict most users will do), emails will now be preloaded using proxy servers, caching images and hindering the ability to leverage tracking pixels for metrics like [open tracking]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel). 

Brands should expect MPP to result in issues regarding email deliverability metrics and issues with pre-existing campaigns and Canvases that trigger based on these metrics. To understand the impact in email deliverability, refer to [Email Reporting]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/).

### Who will this affect?

Any recipient using the native Apple Mail app on:

- iOS 15
- iPadOS 15
- macOS Monterey
- watchOS 8

This applies to all users who have connected their mail account to the Apple Mail app and have opted into the security feature, regardless of email service (Gmail, Outlook, Yahoo, AOL, etc.). This impact is not constrained to subscribers who receive mail at Apple/iCloud/me.com email addresses.

{% alert important %}
While these updates to email deliverability are significant, MPP doesn't fundamentally change any of the rules that govern email and deliverability. Instead, it will impact how we benchmark success and what email tools and functionalities can be used going forward.
{% endalert %} 

## How to prepare for MPP?

Time is of the essence for brands who are just beginning to think about how they respond to MPP and its potential impact on their email marketing and overall customer engagement efforts. We recommend users do the following:

- Assess the risk that MPP poses to their marketing efforts
- Put together a targeted MPP response plan that addresses automation adjustments on the Braze platform, strengthens deliverability best practices, and develops a broader set of metrics to measure performance.
- Implement that response plan as soon as they can

For an in-depth overview of how to prepare for Apple's Mail Privacy Protection, check out our [blog post](https://www.braze.com/resources/articles/apple-mail-privacy-protection-how-to-prepare). 
