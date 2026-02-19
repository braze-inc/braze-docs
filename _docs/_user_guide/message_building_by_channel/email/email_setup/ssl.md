---
nav_title: SSL at Braze
article_title: SSL Overview
page_order: 5
page_type: reference
description: "This reference article covers SSL, what's it is used for, and how it's used at Braze."
channel: email

---

# SSL at Braze

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

> A secure socket layer (SSL) encrypts a URL with HTTPS instead of HTTP. HTTPS indicates that a valid and trusted SSL or TLS certificate exists and that the website is safe to visit.

## Why is SSL important?

Most domains do not require SSL, but Braze strongly recommends using SSL for these reasons.

Securing your website and links with SSL is a common practice even for companies that don't deal directly with sensitive customer information. Users are more trusting of links that are secured with SSL, and the additional layer of authentication helps protect your data.

### Necessary for click and open tracking

Braze transforms your links using your branded link tracking subdomain to track clicks and opens. By default these links begin with HTTP. Users with browsers or extensions that restrict non-secure traffic may have difficulty passing through the redirect before the destination URL, even if the URL is secure. This can cause broken images and inaccurate tracking. Apply SSL to the link tracking subdomain to confirm secure redirects.

### Browser requirement

Major browsers such as Google Chrome restrict traffic through non-secure URLs to protect users. Using SSL helps confirm that content is trusted and minimizes issues like broken links and images in emails.

### HSTS domains requirement 

If you have an HTTP Strict Transport Security (HSTS) domain, set up SSL and configure a CDN to send required security certificates. Without SSL, image and web links break.

## Acquiring an SSL certificate

Acquire an SSL certificate through a third party, usually a Content Delivery Network (CDN). A CDN hosts the certificate and serves it to the browser when a user clicks a link by redirecting traffic through the CDN to apply certificates before sending it to SendGrid or SparkPost.

To start SSL setup, contact your Braze customer success manager to initiate a full Braze email setup.

After Braze initiates setup, follow these steps:
1. Braze will provide DNS records to add to your domain registry.
2. Braze will verify if records have been added to your registry correctly.
3. After this, you'll select a CDN and obtain SSL certificates from a third-party provider. 
4. At this point, you'll set up your CDN. Note that Braze will not be able to help troubleshoot CDN configuration. Contact your CDN provider for any further assistance.
5. Contact your customer success manager to get SSL turned on.

### What is a CDN, and why do I need it?

A content delivery network (CDN) is a platform of servers that helps ensure quick load times of content across multiple mediums while also handling security certificates. 

{% alert important %}
CDN configuration always follows after getting your DNS records validated by Braze. If you have not yet initiated this step, contact your customer success manager for more information on how to get started.
{% endalert %}

For click and open tracking, delivery partners transform links using a branded subdomain and the CDN applies the SSL certificate to those transformed links. Partners often must present valid certificates to the recipient's browser for links and images to display correctly. Because Braze doesn't request or manage certificates, you must set this up through a CDN. 

{% alert note %}
If you can't or don't want to use the listed CDNs for SSL click and open tracking, you may set up a custom SSL configuration. Alternate CDNs or custom proxies can result in a more complex setup. Refer to [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) and [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) documentation.
{% endalert %}

#### Additional resources

{% alert important %}
For troubleshooting your CDN configuration, contact your CDN provider.
{% endalert %}

The following table includes step-by-step guides written by ESP partners on how to configure certain CDNs. While your specific CDN may not be listed, you must make sure your CDN has the ability to apply SSL certificates.

| SendGrid | SparkPost |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Google Cloud Platform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For Amazon SES, refer to [Option 2: Configuring an HTTPS domain](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) and specify the AWS tracking domain by region based on your Braze cluster:

- **Braze US clusters:** `r.us-east-1.awstrack.me`
- **Braze EU clusters:** `r.eu-central-1.awstrack.me`

{% alert important %}
When you configure your CDN's click-tracking domain, enable the `X-Forwarded-Host` header to prevent potential security issues such as host header attacks. Refer to CDN documentation or your support team for steps.
{% endalert %}

#### Troubleshooting

While you should handle CDN configuration, certificates, and proxy issues with your CDN, use these tips to identify common SSL click tracking issues.

##### Domain registry issues

Run a dig command to confirm you point link tracking at the CDN. In your terminal run `dig CNAME link_tracking_subdomain`. Under `ANSWER SECTION`, it lists where your CNAME points. If it points to the email service provider (SendGrid or SparkPost) and not your CDN, reconfigure your domain registry to point to your CDN.

##### CDN issues

If live email links break during setup, you likely pointed DNS toward your CDN before proper configuration. This can appear as a "wrong link" error. Contact your CDN provider and review their documentation to troubleshoot configuration.

##### SSL enablement status

If you complete SSL setup and links still appear as HTTP, contact your Braze customer success manager to confirm Braze enabled SSL. Braze enables SSL only after all setup steps are complete.

