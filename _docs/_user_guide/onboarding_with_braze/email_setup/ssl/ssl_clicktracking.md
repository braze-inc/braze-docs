---
nav_title: SSL Click Tracking
article_title: SSL Click Tracking
page_order: 9
page_type: reference
description: "This reference article covers SSL click-tracking, best practices, and how to get started."
channel: email

---

# SSL click tracking

A Secured Socket Layer (SSL) encrypts a URL with HTTPS instead of the less secure HTTP. Customers at Braze can set up their links and domains to apply SSL certificates. These certificates, similar to SPM and DKIM for email authentication, are insurances that links in your emails are sending your users to reputable locations, and not malicious websites. While not required, SSL certificates are quickly becoming the standard and are strongly recommended to ensure links and images display properly.

## How do i get started?
1. You must reach out to a COM or CSM to initiate a full Braze email setup.
2. Braze will provide DNS records to add to your domain registry.
3. Braze will verify if records have been added to your registry correctly.
4. You will then select a CDN and obtain SSL certificates from a third-party provider. 
5. You will set up your CDN. Please note that Braze will not be able to help troubleshoot CDN configuration. Please reach out to your CDN provider for help.
6. Lastly, reach out to your COM or CSM to get SSL turned on.

## What is a cdn, and why do i need it?

A Content Delivery Network (CDN) is a platform of servers that help ensure quick load times of high-quality content across multiple mediums while also handling security certificates. 

At Braze, to do click and open tracking, our delivery partners transform links using a branded subdomain, and the CDN applies the SSL certificate to those newly transformed links. Often, our delivery partners are required to present valid and trusted certificates to your email recipient's browser for links and images to display correctly. Because Braze cannot request or manage such certificates, this must be set up on your end through a CDN. 

Below we have outlined and linked out to relevant CDN partner resources to help make this process easy. 

{% alert important %}
Please note that CDN configuration always follows after getting your DNS records validated by Braze. If you have not yet initiated this step, reach out to your COM or CSM for more information on how to get started.
{% endalert %}

{% alert note %}
If you are unable or do not wish to use the CDNs listed above when setting up SSL for click and open tracking, you may set up a custom SSL configuration. Note that alternate CDNs or custom proxies may result in a more complex and nuanced setup. Check out the [Sendgrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) and [Sparkpost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) documentation on this topic.
{% endalert %}

### CDN resources

Listed below are step-by-step guides written by Sendgrid and Sparkpost on how to configure certain CDNs. While your specific CDN may not be listed below, you must make sure your CDN has the ability to apply SSL certificates.

{% alert important %}
Braze will be unable to help you troubleshoot your CDN configuration. You must reach out to your CDN provider to help troubleshoot your CDN configuration.
{% endalert %}

| Sendgrid Step-By-Step Guides | Sparkpost Step-By-Step Guides |
| -------- | --------- |
| [AWS Cloudfront](https://sendgrid.com/docs/ui/sending-email/universal-links/#setting-up-universal-links-using-cloudfront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#aws-create)<br>[CloudFlare](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Cloudfront](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/)<br>[Fastly](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Google Cloud Platform](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#gcp-create)<br>[Microsoft Azure](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#azure-create) |

### CDN troubleshooting

While CDN configuration, certificates, and proxy issues should be handled with your selected CDN, we offer some basic troubleshooting tips to identify where your SSL click tracking setup may be failing.

{% tabs %}
{% tab Domain Registry %}

#### Check for domain registry issues

A dig command can tell you whether you are pointing your link tracking at the CDN. This can be done through the terminal by running `dig CNAME link_tracking_subdomain`.

Once the command is run, under `ANSWER SECTION` it should list where your CNAME is pointed to. If it pointed to your chosen email service provider (Sendgrid or Sparkpost) and not your CDN, you must reconfigure your domain registry to point to your CDN.

{% endtab %}
{% tab CDN %}

#### Check for cdn issues

If your live email links start breaking during setup, this often means you've pointed your DNS toward your CDN without it being properly configured. This often comes up as a "Wrong Link" error.

Please reach out to your CDN provider and review their documentation to help to troubleshoot your CDN configuration.

{% endtab %}
{% tab HTTP Messages Persisting %}

#### Check if ssl is enabled by braze

If you have completed your SSL setup and are still seeing your links come up as HTTP and not HTTPS, reach out to your Braze COM or CSM and make sure SSL has been enabled by Braze. SSL can only be enabled by Braze once all aspects of your SSL setup have been completed.

{% endtab %}
{% endtabs %}