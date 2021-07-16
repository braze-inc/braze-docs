---
nav_title: SSL Overview
page_order: 9

page_type: reference
description: "This reference article covers SSL, what's it is used for, and how it's used at Braze."
channel: email
---

# SSL at Braze
<!---
{% include video.html id="" align="right" %}
-->

> A Secure Socket Layer (SSL) encrypts a URL with HTTPS instead of the less secure HTTP. URLs with HTTPS indicate that an SSL or TLS certificate that is valid and trusted exists and that the site is safe to visit and not a scam or the source of dangerous malware.

## Why is SSL Important?

While most domains do not require SSL, these are the reasons we strongly recommend SSL to our users:
1. __Required by some Major Browsers__: SSL protocols are becoming more prevalent today as major browsers like Google Chrome are starting to restrict traffic through non-secure URLs to protect their users. Companies with SSL on their website ensure to these major browsers that their content is trusted, minimizing content viewing issues like broken links and images in their emails.<br><br>
2. __Neccesary for Click and Open Tracking__: At Braze, when we send out emails, we first transform your links using your branded link tracking subdomain to track user clicks and opens. By default, these links will begin with HTTP. This means that users with a browser or extension that restricts non-secure traffic may have difficulty passing through the redirect before landing at the destination URL, even if the URL is secure. This can lead to broken images and inaccurate click and open tracking throughout your emails. For this reason, it is a best practice to apply an SSL layer to the link tracking subdomain to ensure secure redirects in your emails. <br><br>
3. __HSTS Domains Require SSL__: Regardless of which browsers your users may be accessing your emails from, you must set up SSL if you have an HTTP Strict Transport Security (HSTS) domain and configure a CDN to send the necessary security certificates. Failure to set up SSL will cause both image and web links to break.<br><br>
4. __General Best Practice__: Securing your website and links with SSL is a common practice even for companies that don't deal directly with sensitive customer information. Users are more trusting of links that are secured with SSL, and the additional layer of authentication helps protect your data.

## Acquiring an SSL Certificate

Acquiring an SSL certificate can be done by utilizing a third party, usually a Content Delivery Network (CDN). A CDN can host the SSL certificate and serve it to the browser any time one of your links is clicked. This is done by redirecting the traffic through the CDN to apply necessary certificates before sending it through to our email partners Sendgrid or Sparkpost.

Ready to get started with your SSL setup? View our next SSL article [here]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ssl/ssl_clicktracking/). 