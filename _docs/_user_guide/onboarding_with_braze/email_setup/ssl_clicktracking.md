---
nav_title: SSL Click Tracking
page_order: 9
description: "A fundamental part of SSL click-tracking for users who have HSTS, is getting a CDN configured to send the necessary security certificates required."
---

# SSL Click Tracking - CDN Configuration

> At Braze, email delivery is handled by our delivery partners that support open and click reporting within the Braze dashboard. To perform this tracking over SSL, the delivery partner is required to present a valid trusted certificate to your email recipient's browser. Braze is unable to request or manage such certificates, so this must be set up on your end through a CDN. <br><br>CDN configuration commonly follows after getting your DNS records validated by Braze. If you have not yet initiated this step, reach out to your COM or CSM for more information on how to get started.

Content Delivery Networks are a great mechanism that you can use to serve up content very quickly and easily across multiple mediums as well as handle security certificates for you. Below we have outlined and linked out to relevant CDN partner configurations and resources to help make this process easy. 

__Content Delivery Networks - Partners__<br>
&#45; [AWS CloudFront](#cloudfront): Sendgrid and Sparkpost<br>
&#45; [Cloudflare](#cloudflare): Sendgrid and Sparkpost<br>
&#45; [Fastly](#fastly): Sendgrid and Sparkpost<br>
&#45; [KeyCDN](#keycdn): Sendgrid<br>

{% alert note %}
If you are unable or do not wish to use the Content Delivery Network Partners listed above when setting up SSL for click and open tracking, you may set up a custom SSL configuration. Note that alternate CDNs or custom proxies may result in a more complex and nuanced setup. Check out the [Sendgrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) and [Sparkpost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) documentation on this topic.
{% endalert %}

## AWS CloudFront - Sendgrid and Sparkpost {#cloudfront}

{% tabs %}
{% tab Sendgrid %}

#### Step 1: Set Up your Server Certificate

Either upload an existing certificate using the [AWS command-line tool](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html#UploadSignedCert) or approve a new certificate through your [Certificate Manager service](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) that is valid for your link whitelabel(s). e.g. __ablink.subdomain.customer.com/link.subdomain.customer.com__ and another certificate for __ablink.info.customer.com/link.subdomain.customer.com__. 

#### Step 2: Create a Distribution

Go to [Cloudfront](https://console.aws.amazon.com/cloudfront/) and click __Create Distribution__. Select __Web__ as your delivery method. *Please note* you will also have to do this set up for each of the link white labels. However, it is possible to use a single distribution (see photos below) for all link white labels, as long as the SSL certificate attached to this distribution covers all subdomains.

![Single Distribution]({% image_buster /assets/img/SSL/single_distribution.png %})

#### Step 3: Configure your Distribution

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
- Cache and Origin Request Settings: __Use legacy cache settings__
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
- Alternate Domain Names (CNAMEs): `ablink.subdomain.customer.com` or `link.subdomain.customer.com`
- SSL Certificate: __Custom SSL Certificate__
- Custom SSL Client Support: __Client that Support Server Name Indication (SNI)__
- Security Policy: __TLSv1.2__
- Supported HTTP Versions: __HTTP/2, HTTP/1.1, HTTP/1.0__ *(default)*
- Enable IPv6: __Enabled__
- Default Root Object: *leave blank*
- Log Bucket: *leave blank*

#### Step 4: Test your Distribution

Once the Distribution is deployed, ensure that it can handle links correctly over HTTP and HTTPS using an existing link.

#### Step 5: Update your DNS

Once the distribution is verified, change the DNS entry for the link white labels(s) (e.g. __ablink.subdomain.customer.com/link.subdomain.customer.com__ and __ablink.info.customer.com/link.subdomain.customer.com__) to CNAME to the domain name of the Distribution.

#### Step 6: Next Steps

Now that you have configured CloudFront, reach out to your COM or CSM and let them know you want SSL click-tracking turned on. They will also help test that your configuration is set up correctly.

{% endtab %}
{% tab Sparkpost %}

Please follow [Sparkpost's CloudFront CDN Documentation](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/) for guidance on how to configure your CDN using CloudFront.

{% endtab %}
{% endtabs %}

## Cloudflare - Sendgrid and Sparkpost {#cloudflare}

{% tabs %}
{% tab Sendgrid %}
#### Step 1: Set Crypto Settings

You must first purchase an SSL certificate that matches the exact link branding record for each subdomain, for example, __ablink.m.example.com__, __ablink.x.example.com__. A wildcard certificate that only covers one level of a subdomain  (&#42;__.level-ex.com__) will cause links to break. 

![Crytpo Settings]({% image_buster /assets/img/SSL/SSL_certificate.png %}){: style="max-width:70%"}

#### Step 2: Purchase SSL Certificates

Clients can purchase the "Dedicated SSL with Custom Hostnames" option. Ensure that the Certificate purchased is an "Edge Certificate". For more information on Cloudflare's different certificates [please see here](https://support.cloudflare.com/hc/en-us/articles/228009108-Managing-Dedicated-SSL-Certificates).

![SSL Certificates]({% image_buster /assets/img/SSL/custom_hostname.png %}){: style="max-width:70%"}

The ablink subdomain record will be added as custom hostnames.

![Link Branding]({% image_buster /assets/img/SSL/crypto_settings.png %}){: style="max-width:80%"}

Make sure the HTTP proxy is enabled, i.e. the cloud icon is orange. 

#### Step 3: Set Up Page Rules

Confirm that __SSL is set to Full__ and Page Rules are turned __ON__ for each URL.

![Page Rules]({% image_buster /assets/img/SSL/page_rules.png %}){: style="max-width:70%"}

#### Step 4: Update DNS Settings

Make sure to point all link branding records for each subdomain to sendgrid.net (there should be 2 CNAME records per each subdomain).

In the "Name" field, ensure you are only posting the portion of the CNAME before your domain. For example, if your CNAME is `ablink.x.example.com`, you would only post `ablink.x`.

![DNS]({% image_buster /assets/img/SSL/crypto_settings.png %}){: style="max-width:90%"}

#### Next steps 

Now that you have configured Cloudflare, reach out to your COM or CSM to get them to test your setup. 

{% endtab %}
{% tab Sparkpost %}
#### Step 1: Navigate to the DNS Tab

From your Cloudflare account, navigate to the __DNS Tab__ in the Cloudflare Dashboard.

#### Step 2: Add your Domain 

Add a domain and then add the following Cloudflare NS records:
```
NS    aron.ns.cloudflare.com
NS    peyton.ns.cloudflare.com
```
These values can be found under the __DNS Tab__ in the Cloudflare Dashboard. Checkout the Sparkpost [documentation](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare) on how to use the command line to confirm your NS records have been updated. 

#### Step 3: Set up Page Rules

Configure the appropriate page rule settings for the domain. In the __Page Rules Tab__, perform the following instructions:
1. __Create a page rule__: Navigate to the __Page Rule Tab__, selecting __Create Page Rule__
2. __Enter your domain in this format__: track.yourdomain.com/*
3. __Add in redirects__ (if necessary): Add a Setting -> Forwarding URL (you may need to specify a 301 redirect option)
4. __Configure your destination URL__: Your URL will look something like this: `https://<CNAME_VALUE>/$1`. Replace `<CNAME_VALUE>` with the value displayed in the tracking domains section of the SparkPost Dashboard. Note that this varies per region. For SparkPost US, this would be spgo.io; for SparkPost EU, this would be eu.spgo.io; for PMTA+Signals, refer to your user guide.
5. __Save and Deploy__ (turn page rule __ON__)

#### Step 4: Verify SSL Settings

Cloudflare has Universal SSL for all accounts, but it’s good to ensure that setting on the page rule is "SSL". This is required for how Cloudflare will validate the certificate on the origin.

More information on SSL options for Cloudflare can be found [here](https://support.cloudflare.com/hc/en-us/articles/200170416).

#### Step 5: Add a CNAME Entry into DNS for your Tracking Domain

The value in the record doesn’t matter; the record simply needs to exist. For example, if your tracking domain is `track.example.com`, a CNAME value of `example.com` is sufficient. Without a record to reference, the page rule never gets triggered, and the proper redirect will not occur. Please note the typical time it takes to propagate new CNAME records is often around five to ten minutes but can be longer depending on your DNS provider.

#### Step 6: Reach out to Braze to Update Tracking Domain API

Please reach out to a COM or CSM to complete this step for you. 

#### Step 7: Run Test Verification

Navigate to the Tracking Domains section in the UI and click the orange "test" verification link. At this point, the process is complete. For detailed instructions and additional resources, check out Sparkpost's CDN documentation [here](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare). 

{% endtab %}
{% endtabs %}

## KeyCDN - Sendgrid {#keycdn}

Please follow [Sendgrid's KeyCDN CDN Documentation](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) for guidance on how to configure your CDN using KeyCDN.

## Fastly - Sendgrid and Sparkpost {#fastly} 

{% tabs %}
{% tab Sendgrid %}

Please follow [Sendgrid's Fastly CDN Documentation](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly) for guidance on how to configure your CDN using Fastly.

{% endtab %}
{% tab Sparkpost%}

Please follow [Sparkpost's Fastly CDN Documentation](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly) for guidance on how to configure your CDN using Fastly.

{% endtab %}
{% endtabs %}


[1]: {% image_buster /assets/img/SSL/SSL_certificate.png %}
[2]: {% image_buster /assets/img/SSL/custom_hostname.png %}
[3]: {% image_buster /assets/img/SSL/crypto_settings.png %}
[4]: {% image_buster /assets/img/SSL/page_rules.png %}
