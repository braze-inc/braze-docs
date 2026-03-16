---
nav_title: Troubleshooting
article_title: SSL Troubleshooting
page_order: 5
page_type: reference
description: "This reference article covers troubleshooting tips for SSL."
channel: email
---

# Troubleshooting

> Use these tips to identify common SSL click tracking issues. The troubleshooting guidance is generic because every CDN is unique. For CDN configuration, certificates, or proxy issues with your CDN, we recommend contacting your CDN’s support team, as these configurations take place outside of the Braze ecosystem.

## Key concepts

- **Tracked URL:** Wraps the original HTTPS link in your tracking domain. When a user clicks it, the tracking domain resolves the request and redirects to the final destination. A CDN allows you to track secure (HTTPS) URLs. Without it, users may encounter a "connection is not secure" privacy error.
- **Untracked URL:** Maintains the original URL intact, bypassing the CDN to serve as a control environment.

## Domain registry issues

Run a dig command to confirm you point link tracking at the CDN. In your terminal run `dig CNAME link_tracking_subdomain`. Under `ANSWER SECTION`, it lists where your CNAME points. If it points to the email service provider (SendGrid or SparkPost) and not your CDN, reconfigure your domain registry to point to your CDN.

## CDN issues

If live email links break during setup, you likely pointed DNS toward your CDN before proper configuration. This can appear as a "wrong link" error. Contact your CDN provider and review their documentation to troubleshoot configuration.

## SSL enablement status

If you complete SSL setup and links still appear as HTTP, contact your Braze customer success manager to confirm Braze has enabled SSL. Braze enables SSL only after all setup steps are complete.

## Click tracking issues

Use the following template to test the CDN configuration of your tracking domain, which is the mechanism supporting analytics for links within your emails. Common redirection issues typically result from an improper configuration between the CDN hosting the tracking domain and its associated SSL certificates or DNS CNAME records. These misconfigurations often cause users to receive a "connection is not secure" privacy error or a `404` failure after clicking a tracked email link.

1. Copy and paste the following template into a Braze HTML email campaign.

{% details Click tracking troubleshooting template %}
```html
<!DOCTYPE html>
<html lang="en" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="color-scheme" content="light dark">
    <meta name="supported-color-schemes" content="light dark">
    <title>Click Tracking Test</title>
    <style>
        /* Base Dark Mode (Default) */
        body { 
            margin: 0; 
            padding: 0; 
            background-color: #2b0562; 
            font-family: 'Helvetica Neue', Arial, sans-serif; 
            color: #ffd1e9; 
        }
        
        .email-container { 
            width: 100%; 
            max-width: 600px; 
            margin: 40px auto; 
            background-color: rgba(255, 255, 255, 0.05); 
            border: 1px solid #F3697F; 
            border-radius: 16px; 
            overflow: hidden; 
        }
        
        .header { 
            background: linear-gradient(135deg, #E83F21 0%, #F3697F 100%); 
            padding: 40px 20px 50px 20px; 
            text-align: center; 
        }

        .logo {
            display: block;
            margin: 0 auto 25px auto;
            border: 0;
            outline: none;
            text-decoration: none;
        }
        
        .header h1 { 
            color: #ffffff; 
            margin: 0; 
            font-size: 26px; 
            font-weight: 800; 
            letter-spacing: -0.5px; 
        }
        
        .content { 
            padding: 40px 40px 20px 40px; 
            line-height: 1.8; 
            font-size: 15px; 
        }

        .troubleshoot {
            margin: 0 40px 40px 40px;
            padding: 25px;
            background-color: rgba(253, 167, 216, 0.1);
            border-radius: 12px;
            font-size: 14px;
            border: 1px dashed #F3697F;
        }
        
        .troubleshoot h2 {
            margin-top: 0;
            font-size: 18px;
            color: #ffffff;
        }

        .btn-section { 
            padding: 0 40px 40px 40px; 
            text-align: center; 
        }
        
        .btn { 
            display: inline-block; 
            padding: 16px 32px; 
            border-radius: 12px; 
            font-weight: 700; 
            text-decoration: none; 
            margin: 10px;
            font-size: 14px;
        }
        
        .btn-tracked { 
            background-color: #F3697F; 
            color: #ffffff; 
        }
        
        .btn-untracked { 
            border: 2px solid #FDA7D8; 
            color: #FDA7D8; 
            background-color: transparent;
        }

        .footer { 
            text-align: center; 
            font-size: 12px; 
            color: #FDA7D8; 
            padding-bottom: 40px; 
            opacity: 0.6; 
        }

        /* Light Mode Overrides */
        @media (prefers-color-scheme: light) {
            body { background-color: #F7FCFF !important; color: #2b0562 !important; }
            .email-container { background-color: #ffffff !important; border: 1px solid #FDA7D8 !important; box-shadow: 0 4px 20px rgba(43, 5, 98, 0.1); }
            .content { color: #2b0562 !important; }
            .troubleshoot { background-color: #F7FCFF !important; border-color: #F3697F !important; color: #2b0562 !important; }
            .troubleshoot h2 { color: #E83F21 !important; }
            .btn-untracked { color: #F3697F !important; border-color: #F3697F !important; }
            .footer { color: #2b0562 !important; }
            strong { color: #E83F21 !important; }
        }

        /* Mobile Optimization */
        @media only screen and (max-width: 480px) {
            .btn { display: block !important; margin: 10px 0 !important; width: auto !important; }
            .content, .troubleshoot { padding: 25px !important; }
        }
    </style>
</head>
{%- capture url -%}https://example.com{%- endcapture -%}
<body>
    <center>
        <table class="email-container" role="presentation" width="600" border="0" cellpadding="0" cellspacing="0">
            <tr>
                <td class="header">
                    <img src="https://cdn-staging.braze.com/appboy/communication/assets/image_assets/images/69a9b6976aaa9200763ab224/original.png?1772730007" 
                         width="150" 
                         alt="Logo" 
                         class="logo">
                    <h1>Testing Click Tracking Functionality</h1>
                </td>
            </tr>
            <tr>
                <td class="content">
                    <p>
                        Use this template to test the <strong>CDN configuration</strong> of your tracking domain—the mechanism supporting analytics for links within your emails.
                    </p>
                    <p>
                        A <strong>Tracked URL</strong> wraps the original HTTPS link in your tracking domain. When a user clicks it, the tracking domain resolves the request and redirects to the final destination. A CDN allows you to track secure (HTTPS) URLs; without it, users may encounter a "connection is not secure" privacy error. An <strong>Untracked URL</strong> maintains the original URL intact, bypassing the CDN to serve as a control environment.
                    </p>
                    <p>
                        Common redirection issues typically result from an improper configuration between the CDN hosting the tracking domain and the <strong>associated SSL certificate or DNS CNAME records.</strong>
                    </p>
                    <p>
                        <i style="font-size: 13px;">This template uses "example.com" as the destination URL. To test your own domain, simply replace the URL in the <strong>capture</strong> tag located on line 125.</i>
                    </p>
                </td>
            </tr>
            <tr>
                <td class="btn-section">
                    <a href="{{url}}" class="btn btn-tracked">Tracked URL</a>
                    
                    <a href="{{url}}" 
                       class="btn btn-untracked"
                       clicktracking="off" 
                       data-msys-clicktrack="0" 
                       ses:no-track="true">
                       Untracked URL
                    </a>
                </td>
            </tr>
            <tr>
                <td>
                    <div class="troubleshoot">
                        <h2>Troubleshooting the Test</h2>
                        <ul>
                            <li><strong>Tracked URL Fails / Untracked Works:</strong> This indicates a CDN or SSL certificate issue. Verify that your SSL certificate is valid and correctly bound to your tracking domain.</li>
                            <li><strong>Privacy Error (HTTPS):</strong> Ensure your CDN is configured to handle port 443 traffic and that the certificate matches your tracking CNAME.</li>
                            <li><strong>Both URLs Fail:</strong> Check the destination URL or your internal network firewall settings.</li>
                            <li>For more information, visit: <a href="https://www.braze.com/docs/user_guide/message_building_by_channel/email/email_setup/ssl/#ssl-at-braze">SSL at Braze</a></li>
                        </ul>
                    </div>
                </td>
            </tr>
        </table>
        <div class="footer">
            Braze :: 63 Madison Avenue, 13th Floor :: New York, NY 10016
        </div>
    </center>
</body>
</html>
```
{% enddetails %}

{: start="2"} 
2. Configure your URL. Note that this template uses `example.com` as the default destination. To test your own links and tracking domain, replace the URL in the `capture` tag on line 117. For example, replace `https://example.com` with `https://braze.com/blog`.
3. Send a test email to yourself and select both buttons.
4. Verify that the expected behavior and success criteria are as described in the template.

If your untracked URL works but your tracked URL fails, you may have a configuration gap. To troubleshoot, refer to the documentation for your specific ESP and CDN provider. You can also review the [SSL at Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl) for detailed requirements on certificate provisioning.

| Error code | Troubleshooting | 
| --- | --- | 
| `"Your connection is not private" (NET::ERR_CERT_COMMON_NAME_INVALID)` | Verify that your tracking domain has a valid SSL certificate. |
| `"This site can’t be reached" (DNS_PROBE_FINISHED_NXDOMAIN)` | Check your DNS settings. Ensure your tracking subdomain is configured per your CDN and ESP recommended configuration. |
| `525 / 526 SSL Error` | Check that the SSL setting in your CDN (like Cloudflare) matches your Origin's capability. |
| `404 Not Found` | Check that your CDN is configured to forward the entire URL path to the ESP, rather than just hitting a blank root directory. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
