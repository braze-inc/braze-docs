{% if include.alert == "Shopify deprecation" %}

{% alert important %}
A [new version of the Shopify integration]({{site.baseurl}}/partners/shopify/#new-shopify-integration) will be released in phases starting in April 2025. The phases will be based on the type of Shopify store and the external ID used to set up the initial integration. <br><br>**The old version of the integration will no longer be available after August 28, 2025. Update to the new version before this date to continue using the integration without any issues.**
{% endalert %}

{% endif %}

{% if include.alert == "Email via SMS" %}

{% alert important %}
Do not send legally required transactional emails to SMS gateways as there's a strong likelihood that those emails will not be delivered.
<br><br>
Although emails you send using a phone number and the provider’s gateway domain (known as an MM3) can result in the email being received as an SMS (text) message, some of our email providers do not support this behavior. For example, if you send an email to a T-Mobile phone number (such as "9999999999@tmomail.net"), your SMS message would be sent to whoever owns that phone number on the T-Mobile network.
<br><br>
Keep in mind that even though these emails may not be delivered to the SMS gateway, they will still count towards your email billing. To avoid sending emails to unsupported gateways, review the [list of unsupported gateway domain names](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads).
{% endalert %}

{% endif %}

{% if include.alert == 'SDK auth' %}

{% alert important %}
For additional security, we recommend adding our [SDK Authentication]({{site.baseurl}}/developer_guide/authentication/) feature to prevent user impersonation.
{% endalert %}

{% endif %}

{% if include.alert == 'Preference Center warning' %}

{% alert important %}
There are certain browsers, such as the Naver Android and iOS apps, that don’t support the Braze preference center. If you anticipate that some of your users use these browsers, consider providing alternative methods for them to manage their email preferences.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation' %}

{% alert important %}
The plans to phase out the purchase event will be announced in late 2025. In the long run, the purchase event will be replaced by new [eCommerce recommended events]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/), which will come with enhanced features for segmentation, reporting, analytics, and more. However, the new eCommerce events will not support existing features related to the purchase event, such as Lifetime Value (LTV) or revenue reporting in Canvases or campaigns. For a complete list of features related to purchase events, refer to [Logging purchase events]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}

{% endif %}

{% if include.alert == 'S3 file bucket export' %}

{% alert important %}
Export files stored in S3 buckets are automatically deleted after the download link expires (four hours from when the export email is sent).
{% endalert %} 

{% endif %}