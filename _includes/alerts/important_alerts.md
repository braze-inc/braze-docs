{% if include.alert == "Shopify deprecation" %}

{% alert important %}
A [new version of the Shopify integration]({{site.baseurl}}/partners/shopify/#new-shopify-integration) will be released in phases starting in April 2025. The phases will be based on the type of Shopify store and the external ID used to set up the initial integration. <br><br>**The old version of the integration will no longer be available after August 28, 2025. Update to the new version before this date to continue using the integration without any issues.**
{% endalert %}

{% endif %}

{% if include.alert == 'Web push private browsing' %}

{% alert important %}
Private browsing windows do not support web push.
{% endalert %}

{% endif %}

{% if include.alert == 'BCC address billable emails' %}

{% alert important %}
Appending a BCC address to your campaign or Canvas results in doubling your billable emails for the campaign or Canvas component since Braze sends one message to your user and one to your BCC address.
{% endalert %}

{% endif %}

{% if include.alert == 'Android notification priority' %}

{% alert important %}
The Notification Display Priority setting is no longer used on devices running Android O or later. On these devices, set the priority through [notification channel configuration](https://developer.android.com/training/notify-user/channels#importance).
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
The plans to phase out the purchase event will be announced in 2026. The purchase event will eventually be replaced by new [eCommerce recommended events]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/), which will come with enhanced features for segmentation, reporting, analytics, and more. However, the new eCommerce events will not support existing features related to the purchase event, such as Lifetime Value (LTV) or revenue reporting in Canvases or campaigns. For a complete list of features related to purchase events, refer to [Logging purchase events]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation for eCommerce filters' %}

{% alert important %}
The plans to phase out the purchase event will be announced in 2026. The purchase event will eventually be replaced by new [eCommerce recommended events]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/), which will come with enhanced features for segmentation, reporting, analytics, and more. When this happens, segment filters will no longer populate under purchase behavior. For a full list of purchase events, refer to [Logging purchase events]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}

{% endif %}

{% if include.alert == 'S3 file bucket export' %}

{% alert important %}
Export files stored in S3 buckets are automatically deleted after the download link expires (four hours from when the export email is sent, unless otherwise noted).
{% endalert %} 

{% endif %}

{% if include.alert == 'Shopify customer create' %}

{% alert important %}
The Shopify integration supports Shopify customer create and customer update webhooks, which are located in your data configuration settings. When a user profile is created or updated in Shopify, a corresponding user profile in Braze will be created or updated. <br><br>These actions don't trigger custom events in Braze and are solely used to [sync Shopify user data with Braze]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#how-the-integration-works). The data synced includes [custom attributes]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-custom-attributes), [standard attributes]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-standard-attributes), and, if enabled within your configuration, [subscription group states]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#syncing-shopify-email-and-sms-marketing-opt-ins).
{% endalert %}

{% endif %}

{% if include.alert == 'context variable' %}

{% alert important %}
Canvas entry properties are part of Canvas context variables. This means `canvas_entry_properties` is referenced as `context`. Each `context` variable includes a name, data type, and a value that can include Liquid. Currently, `canvas_entry_properties` are backwards compatible. For more details, see [Context]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works) and [Canvas context object]({{site.baseurl}}/api/objects_filters/context_object).
{% endalert %}

{% endif %}

{% if include.alert == 'Braze Agents' %}

{% alert important %}
This partner appears on your **Technology Partners** page only if you have [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/) enabled. For help getting started, contact your customer success manager.
{% endalert %}

{% endif %}

{% if include.alert == 'time filter types' %}

{% alert important %}
**Choosing between "Day of year" and "Time" filter types**: When filtering context variables that contain dates, choose the correct comparison type based on whether the date repeats every year:

- **Use "Day of year"** when the date repeats every year (for example, birthdays, anniversaries, or holidays like Christmas). This comparison type calculates based on the day of the year (1-365/366), ignoring the year component.
- **Use "Time"** when the date is an absolute date that doesn't repeat (for example, contract end dates, appointment dates, or subscription renewal dates). This comparison type calculates based on the full timestamp, including the year.

Using "Day of year" for absolute dates can produce incorrect or unexpected results because the calculation ignores the year component. For example, if you're comparing a future contract end date in April to determine if it's within 63 days, using "Day of year" may incorrectly match dates because it only compares day numbers (119 vs 359) without considering that April is actually 188 days away.

**General guideline**: Does the date repeat every year? **Yes** → Use "Day of year". **No** → Use "Time".
{% endalert %}

{% endif %}

{% if include.alert == 'granular permissions ea' %}

{% alert note %}
Granular permissions is in early access. When migration is planned for your company, your Braze admins will receive emails and in-dashboard banners notifying them of the [granular permission migration]({{site.baseurl}}/granular_permissions_migration/).
{% endalert %}

{% endif %}