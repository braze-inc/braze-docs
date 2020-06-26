---
nav_title: SSL Click-Tracking
page_order: 0
description: "A fundamental part of SSL click-tracking for users who have HSTS, is getting a CDN configured to send the necessary security certificates required."
---

# SSL Click Tracking - CDN Configuration

> A fundamental part of getting SSL click-tracking up and working for clients with an HTTP Strict Transport Security (HSTS) policy enabled, is getting a CDN setup to deal with the necessary security certificates required to ensure links and images work as they should. 

Content Delivery Networks are a great mechanism that you can use to serve up content very quickly and easily across multiple mediums as well as handle security certificates for you. Below we have outlined and linked out to relevant resources and configurations to help make this process easy. 

__Content Delivery Networks__<br>
&#45; [CloudFront](#cloudfront)<br>
&#45; [Cloudflare](#cloudflare)<br>
&#45; [KeyCDN](#keycdn)<br>
&#45; [Fastly](#fastly)

{% alert note %}
If you can't or don't want to use Content Delivery Networks when setting up SSL for click and open tracking, then you can set up custom SSL configuration. Documentation regarding this can be found [here](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/).
{% endalert %}

## CloudFront {#cloudfront}

### Step 1: Create a Distribution

Go to [Cloudfront](https://console.aws.amazon.com/cloudfront/) and click __Create Distribution__. Select __Web__ as your delivery method. *Please note* you will also have to do this set up for each of the link white labels.

### Step 2: Configure your Distribution

__Set Origin Settings__
- Origin Domain Name: `sendgrid.net`
- Origin Path: *leave blank*
- Origin ID: `Braze_sendgrid-HSTS-email`
- Minimum Origin SSL Protocol: __TLSv1.2__ only
- Origin Protocol Policy: __HTTPS Only__
- Origin Response Timeout: `30`
- Origin Keep-alive Timeout: `5`
- HTTP Port: `80` *(default)*
- HTTPS Port: `443` *(default)*

__Set Default Cache Behavior__
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

__Distribution Settings__
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

### Step 3: Test your Distribution

Once the Distribution is deployed, ensure that it can handle links correctly over HTTP and HTTPS using an existing link.

### Step 4: Update your DNS

Once the distribution is verified, change the DNS entry for the link white labels(s) (e.g. __ablink.subdomain.customer.com__ and __ablink.info.customer.com__) to CNAME to the domain name of the Distribution.

### Step 5: Next Steps

Now that you have configured CloudFront, reach out to your CSM or Braze account manager and let them know you want SSL click-tracking turned on. They will also help test that your configuration is set up correctly.

## Cloudflare {#cloudflare}

### Step 1: Set Crypto Settings

You must first purchase an SSL certificate that matches the exact link branding record for each subdomain, for example, __ablink.m.level-ex.com__, __ablink.x.level-ex.com__. A wildcard certificate that only covers one level of a subdomain  (&#42;__.level-ex.com__) will cause links to break. 

![Crytpo Settings][1]{: style="max-width:70%"}

### Step 2: Purchase SSL Certificates

Clients can purchase the "Dedicated SSL with Custom Hostnames" option.

![SSL Certificates][2]{: style="max-width:70%"}

The ablink subdomain record will be added as custom hostnames.

![Link Branding][3]{: style="max-width:80%"}

### Step 3: Set Up Page Rules

Confirm that __SSL is set to Full__ and Page Rules are turned __ON__ for each URL.

![Page Rules][4]{: style="max-width:70%"}

### Step 4: Update DNS Settings

Lastly, you must reach out to your CSM or Braze Account Manager to have them generate Email Link Whitelabels. They will then provide you with information similar to the chart found below for each of your subdomains and corresponding CNAMES. These CNAMES will be used to configure your DNS in Cloudflare.

![DNS Settings][5]{: style="max-width:70%"}

Next, point all link branding records for each subdomain to sendgrid.net (there should be 2 CNAME records per each subdomain). Make sure the HTTP proxy is enabled, i.e. the cloud icon is orange. 

In the "Name" field, ensure you are only posting the portion of the CNAME before your domain. For example, if your CNAME is `ablink.x.level-ex.com`, you would only post `ablink.x`.

![DNS][6]{: style="max-width:90%"}

### Next steps 

Now that you have configured Cloudflare, reach out to your CSM or Braze account manager to get them to test your setup. 

## KeyCDN {#keycdn}

Please follow [Sendgrid's KeyCDN CDN Documentation](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly) for guidance on how to configure your CDN using KeyCDN.

## Fastly {#fastly}

Please follow [Sendgrid's Fastly CDN Documentation](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly) for guidance on how to configure your CDN using Fastly.


[1]: {% image_buster /assets/img/SSL/SSL_certificate.png %}
[2]: {% image_buster /assets/img/SSL/custom_hostname.png %}
[3]: {% image_buster /assets/img/SSL/crypto_settings.png %}
[4]: {% image_buster /assets/img/SSL/page_rules.png %}
[5]: {% image_buster /assets/img/SSL/DNS_settings.png %}
[6]: {% image_buster /assets/img/SSL/DNS.png %}
