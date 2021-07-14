---
nav_title: SSL Overview
page_order: 9

page_type: reference
description: "This reference article covers SSL, what's its used for, and how it's used at Braze."
channel: email
---

# SSL at Braze

{% include video.html id="4FUPxkIq2xc" align="right" %}

A Secure Socket Layer (SSL) encrypts a URL with HTTPS instead of the less secure HTTP. URLs with HTTPS indicate that an SSL or TLS certificate that is valid and trusted exists, and that the site is safe to visit and not a scam or the source of dangerous malware.

SSL protocols are becoming more prevalent today as major browsers like Chrome are starting to restrict traffic through non-secure URLs to protect their users. Companies with SSL on their website ensure to these major browsers that their content is trusted, and that issues viewing content on their browsers will not arise. 

In Braze email, we transfer your links using your branded link tracking subdomain to track your user's clicks. By default, these links will begin with HTTP. This means that by default, users with a browser or extension that restricts non-secure traffic may have difficulty passing through the redirect before landing at the destination URL, even if the URL is secure. For this reason, it is a best practice to apply an SSL layer to the link tracking subdomain to ensure secure redirects in your emails. 

Aquiring an SSL certificate can be done by utilizing a third-party, usually a Content Delivery Network, or "CDN". A CDN can host the SSL certificate and serve it to the browser anytime one of your links are clicked. This is done by redirecting the traffic through the CDN before sending it through to our email partners Sendgrid or Sparkpost.

Ready to get started with your SSL setup? View our next SSL article [here]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ssl/ssl_clicktracking/). 