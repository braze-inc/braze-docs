---
nav_title: SSL Click-Tracking
page_order: 0
description: ""
---

# SSL Click Tracking Setup Process

Wait for customer to confirm they've updated their CDN to host the SSL certificate for the link domain, and pointed the DNS records away from Sendgrid.net and to their CDN:


Cloudflare - Full DNS Setup




DNS record updates and 



known-working CDN configurations


Origin Domain Name: `sendgrid.net`
Origin Protocol Policy: HTTPS Only
Forward Cookies: All
Forward Query Strings: Yes
Alternate Domain Names (CNAMEs): ablink.subdomain.customer.com
SSL Certificate: Custom SSL Certificate

Create a new CloudFront distribution

Step 1: Go to [Cloudfront](https://console.aws.amazon.com/cloudfront/) and click __Create Distribution__

Step 2: Select __Web__ as your delivery method

Origin Settings
- Origin Domain Name: `sendgrid.net`
- Origin Path: *leave blank*
- Origin ID: `Braze_sendgrid-HSTS-email`
- Minimum Origin SSL Protocol: __TLSv1.2__ only
- Origin Protocol Policy: __HTTPS Only__
- Origin Response Timeout: `30`
- Origin Keep-alive Timeout: `5`
- HTTP Port: `80` *(default)*
- HTTPS Port: `443` *(default)*

Default Cache Behavior
- Origin or Origin Group: __Braze_sendgrid-HSTS-email__
- Viewer Protocol Policy: __HTTP and HTTPS__ *(default)*
- Allowed HTTP Methods: `GET`, `HEAD`, `OPTIONS`, `PUT`, `PATCH` `DELETE`
- Cached HTTP Methods: `GET`, `HEAD`, check __OPTIONS__
- Cache Based on Selected Request Headers: __All__
- Minimum TTL: `0` *(default)*
- Maximum TTL: `31536000` *(default)*
- Default TTL: `86400`
- Forward Cookies: __All__
- Query String Forwarding and Caching: __Forward all, cache based on all__

Distribution Settings

- Log Prefix: *leave blank*
- Delivery Method: __Web__
- Cookie Logging: __Off__ *(default)*
- Distribution Status: __Deployed__
- Price Class: __Use All Edge Locations__
- AWS WAF Web ACL: *leave blank*
- State: __Enabled__
- Alternate Domain Names (CNAMEs): `ablink.subdomain.customer.com`
- SSL Certificate: __Custom SSL Certificate__
- Custom SSL Client Support: __Client that Support Server Name Indication (SNI)__
- Security Policy: __TLSv1.2__
- Supported HTTP Versions: __HTTP/2, HTTP/1.1, HTTP/1.0__ *(default)*
- Enable IPv6: __Enabled__
- Default Root Object: *leave blank*
- Log Bucket: *leave blank*

Step 3: Once the Distribution is deployed, ensure that it can handle links cirrectly over HTTP and HTTPS using an exisitng link

Step 4: Once the distribution is verified, change the DNS entry for the link whitelabels(s) (e.g. ablink.subdomain.customer.com and ablink.info.customer.com) to CNAME to the domain name of the Distribution.

Step 5: Let Braze know you want SSL Clicktracking turned on. Before we can turn this on, we have to ensure:
- The Link Whitelabel is not pointing to sendgrid.net any longer
- The Link Whitelabel domain is terminating in a SSL connection correctly

These are things we will gladly test and diagnose issues but are limited regarding what action we can take to resolve. Once you complete all these steps, please let me know so I can check in my end and enable the SSL Click Tracking.

















