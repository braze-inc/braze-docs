---
nav_title: SSL Click Tracking
page_order: 9
description: "A fundamental part of SSL click-tracking for users who have HSTS, is getting a CDN configured to send the necessary security certificates required."
---

# SSL Click Tracking

## What is SSL?

A Secured Socket Layer (SSL) encrypts a URL with HTTPS instead of the less secure HTTP. Customers at Braze can set up their links and domains to apply SSL certificates. These certificates, similiar to SPM and DKIM for email authentication, are insurances that the links in your emails are sending your users to reputable locations, and not malicious websites. While not required, SSL certificates are quickly becoming the standard and are not only recommended to ensure links and images display properly for all your customers, but they are also required if you would like to take advantage of valuable email analytics like user open and click tracking.

## Why We Recommend SSL

While SSL is not required, the reasons we recommend SSL to our clients are two-fold:
1. __Required by some browsers__<br>HTTPS links have a certified SSL link certificates attached to it, making it more secure for your users. Authentications like this are quickly becoming the standard with big-name browsers like Google Chrome now requiring it. This means that newer versions of Chrome can no longer access HTTP links without the necessary SSL layer. <br><br>
2. __Click and open tracking are only available through the use of SSL__<br> Not only does this allow you to see valuable email analytics in the braze dashboard, but it also ensures your links and images will appear as you intend them to. This is because without SSL, your email service provider (ESP) will transform your link to include click tracking, and then send it off to your user, but because this link has not been verified to be using SSL, your browser may cause your links (both image and web links) to break.

## How do I get Started?
1. Clients must first complete a full Braze email setup.
2. Take the given DNS records from Braze and add them to your domain registry
3. Braze verifies added to domain correctly.
4. User selects CDN and obtains SSL certificates from a chosen third party (if needed)
5. User Sets up CDN. Please note that Braze will not be able to help troubleshoot CDN configuration. Please reach out to your CDN provider for help.
6. Reach out to your COM or CSM to get SSL turned on.

## What is a CDN?

At Braze, email delivery is handled by our delivery partners that support open and click reporting within the Braze dashboard. To perform this tracking over SSL, the delivery partner is required to present a valid trusted certificate to your email recipient's browser. Braze is unable to request or manage such certificates, so this must be set up on your end through a CDN.

CDNs are a great mechanism that you can use to serve up content very quickly and easily across multiple mediums as well as handle security certificates for you. Below we have outlined and linked out to relevant CDN partner resources to help make this process easy. 

{% alert important %}
CDN configuration commonly follows after getting your DNS records validated by Braze. If you have not yet initiated this step, reach out to your COM or CSM for more information on how to get started.
{% endalert %}

### CDN Resources

Listed below are step-by-step guides written by Sendgrid and Sparkpost on how to configure certain CDNs. While your specific CDN may not be listed below, you must make sure your CDN has the ability to apply SSL certificates. It is also important to note that __Braze will be unable to help you troubleshoot your CDN configuration__. You must reach out to your CDN provider to help troubleshoot your CDN configuration.

| Sendgrid Step-By-Step Guides | Sparkpost Step-By-Step Guides |
| -------- | --------- |
| [AWS Cloudfront](https://sendgrid.com/docs/ui/sending-email/universal-links/#setting-up-universal-links-using-cloudfront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#aws-create)<br>[Clouflare](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Cloudfront](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/)<br>[Fastly](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Google Cloud Platform](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#gcp-create)<br>[Microsoft Azure](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#azure-create) |

{% alert note %}
If you are unable or do not wish to use the CDNs listed above when setting up SSL for click and open tracking, you may set up a custom SSL configuration. Note that alternate CDNs or custom proxies may result in a more complex and nuanced setup. Check out the [Sendgrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) and [Sparkpost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) documentation on this topic.
{% endalert %}

### CDN Troubleshooting

While CDN configuration, certificates, and proxy issues should be handled with your selected CDN, we do offer some basic troubleshooting tips to identify where your SSL click tracking setup may be failing.

{% tabs %}
{% tab Domain Registry %}

### Check for Domain Registry Issues

A dig command can tell you whether you are pointing your link tracking at the CDN. This can be done through the terminal by running `dig CNAME link_tracking_subdomain`.

Once the command is run, under `ANSWER SECTION` it should list where your CNAME is pointed to. If it pointed to your chosen email service provider (Sendgrid or Sparkpost) and not your CDN, you must reconfigure your domain registry to point to your CDN.

{% endtab %}
{% tab CDN %}

### Check for CDN Issues

If your live email links start breaking during setup, this often means you've pointed your DNS toward your CDN without it being properly configured. This often comes up as a "Wrong Link" error.

Please reach out to your CDN provider and review their documentation to help to troubleshoot your CDN configuration.

{% endtab %}
{% tab HTTP Messages Persisting %}

#### Check if SSL is Enabled by Braze

If you have completed your SSL setup and are still seeing your links come up as HTTP and not HTTPS, reach out to your Braze COM or CSM and make sure SSL has been enabled by Braze. SSL can only be enabled by Braze once all aspects of your SSL setup have been completed.

{% endtab %}
{% endtabs %}