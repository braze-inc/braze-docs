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

> A secure socket layer (SSL) encrypts a URL with HTTPS, instead of the less secure HTTP. HTTPS in a URL indicates that a valid and trusted SSL or TLS certificate exists, and that the website is safe to visit and isn't a source of dangerous malware.

## Why is SSL important?

While most domains do not require SSL, Braze strongly recommends using SSL for these key reasons.

Securing your website and links with SSL is a common practice even for companies that don't deal directly with sensitive customer information. Users are more trusting of links that are secured with SSL, and the additional layer of authentication helps protect your data.

### Necessary for click and open tracking

At Braze, when we send out emails, we first transform your links using your branded link tracking subdomain to track user clicks and opens. By default, these links will begin with HTTP. This means that users with a browser or extension that restricts non-secure traffic may have difficulty passing through the redirect before landing at the destination URL, even if the URL is secure. This can lead to broken images and inaccurate click and open tracking throughout your emails. For this reason, it is a best practice to apply an SSL layer to the link tracking subdomain to confirm secure redirects in your emails. 

### Browser requirement

SSL protocols are becoming more prevalent today as major browsers like Google Chrome are starting to restrict traffic through non-secure URLs to protect their users. Companies with SSL on their website confirm with these major browsers that their content is trusted, minimizing content viewing issues like broken links and images in their emails.

### HSTS domains requirement 

Regardless of which browsers your users may be accessing your emails from, you must set up SSL if you have an HTTP Strict Transport Security (HSTS) domain and configure a CDN to send the necessary security certificates. Failure to set up SSL will cause both image and web links to break.

## Acquiring an SSL certificate

You can acquire an SSL certificate by using a third party, usually a Content Delivery Network (CDN). A CDN can host the SSL certificate and serve it to the browser any time one of your links is clicked. This is done by redirecting the traffic through the CDN to apply necessary certificates before sending it through to our email partners SendGrid or SparkPost.

To get started with your SSL setup, contact your Braze customer success manager to initiate a full Braze email setup.

After Braze has initiated this setup, follow these steps:
1. Braze will provide DNS records to add to your domain registry.
2. Braze will verify if records have been added to your registry correctly.
3. After this, you'll select a CDN and obtain SSL certificates from a third-party provider. 
4. At this point, you'll set up your CDN. Note that Braze will not be able to help troubleshoot CDN configuration. Contact your CDN provider for any further assistance.
5. Contact your customer success manager to get SSL turned on.

### What is a CDN, and why do I need it?

A content delivery network (CDN) is a platform of servers that help ensure quick load times of high-quality content across multiple mediums while also handling security certificates. 

{% alert important %}
CDN configuration always follows after getting your DNS records validated by Braze. If you have not yet initiated this step, contact your customer success manager for more information on how to get started.
{% endalert %}

At Braze, to do click and open tracking, our delivery partners transform links using a branded subdomain, and the CDN applies the SSL certificate to those newly transformed links. Often, our delivery partners are required to present valid and trusted certificates to your email recipient's browser for links and images to display correctly. Because Braze doesn't request or manage such certificates, this must be set up on your end through a CDN. 

{% alert note %}
If you are unable to or don't wish to use the CDNs listed when setting up SSL for click and open tracking, you may set up a custom SSL configuration. Note that alternate CDNs or custom proxies may result in a more complex and nuanced setup. Refer to the [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) and [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) articles on this topic.
{% endalert %}

#### Additional resources

{% alert important %}
For further assistance with troubleshooting your CDN configuration, you must contact your CDN provider.
{% endalert %}

The following table includes step-by-step guides written by ESP partners on how to configure certain CDNs. While your specific CDN may not be listed, you must make sure your CDN has the ability to apply SSL certificates.

| SendGrid | SparkPost |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Google Cloud Platform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For Amazon SES, refer to [Option 2: Configuring an HTTPS domain](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) and specify the AWS tracking domain by your region based on your Braze cluster:

- **Braze US clusters:** `r.us-east-1.awstrack.me`
- **Braze EU clusters:** `r.eu-central-1.awstrack.me`

{% alert important %}
When configuring your CDN's click-tracking domain, make sure you enable the `X-Forwarded-Host` header. This is used to prevent potential security issues, such as host header attacks. Refer to the CDN documentation or your support team on how to do this, as this varies depending on the CDN.
{% endalert %}

#### Troubleshooting

While CDN configuration, certificates, and proxy issues should be handled with your CDN, here are some general troubleshooting tips to help identify common issues with SSL click tracking setup.

##### Domain registry issues

A dig command can tell you whether you are pointing your link tracking at the CDN. This can be done in your terminal by running `dig CNAME link_tracking_subdomain`. After the command is run, under `ANSWER SECTION`, it should list where your CNAME is pointed to. If it pointed to your chosen email service provider (SendGrid or SparkPost) and not your CDN, try reconfiguring your domain registry to point to your CDN.

##### CDN issues

If your live email links start breaking during setup, this generally means you've pointed your DNS toward your CDN without it being properly configured. This can appear as a "wrong link" error. Contact your CDN provider and review their documentation to help to troubleshoot your CDN configuration.

##### SSL enablement status

If you have completed your SSL setup and your links still appear as HTTP and not HTTPS, contact your Braze customer success manager to make sure SSL has been enabled by Braze. SSL can only be enabled by Braze after all aspects of your SSL setup have been completed.

