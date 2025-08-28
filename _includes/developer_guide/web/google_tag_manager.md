## About Google Tag Manager for Web {#google-tag-manager}

Google Tag Manager (GTM) lets you remotely add, remove, and edit tags on your website without requiring a production code release or engineering resources. Braze offers the following templates for the Web SDK:

|Tag Type|Use Case|
|--------|--------|
| Initialization tag | This tag lets you [integrate the Web Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web) without needing to modify your site’s code.|
| Action tag | This tag lets you [create Content Cards]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager), [set user attributes]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web), and [manage data collection]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Google's EU User Consent Policy

{% alert important %}
Google is updating their [EU User Consent Policy](https://www.google.com/about/company/user-consent-policy/) in response to changes to the [Digital Markets Act (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), which is in effect as of March 6, 2024. This new change requires advertisers to disclose certain information to their EEA and UK end users, as well as obtain necessary consents from them. Review the following documentation to learn more.
{% endalert %}

As part of Google's EU User Consent Policy, the following boolean custom attributes need to be logged to user profiles:

- `$google_ad_user_data`
- `$google_ad_personalization`

If setting these via the GTM integration, custom attributes require creating a custom HTML tag. The following is an example of how to log these values as boolean data types (not as strings):

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

For more information, refer to [Audience Sync to Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/).
