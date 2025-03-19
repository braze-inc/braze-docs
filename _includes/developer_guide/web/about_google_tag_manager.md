## About Google Tag Manager

[Google Tag Manager](https://support.google.com/tagmanager/answer/6103696) lets you remotely add, remove, and edit tags on your website without requiring a production code release or engineering resources.

There are two Google Tag Manager templates built by Braze, the [Initialization Tag](#web_initialization-tag) and the [Actions Tag](#web_actions-tag). Both tags can be added to your workspace from [Google's community gallery](https://tagmanager.google.com/gallery/#/?filter=braze) or by searching for Braze when adding a new tag from the Community Templates.

![image of gallery search]({% image_buster /assets/img/web-gtm/gtm-community-gallery-search.png %})

## Google's updated EU User Consent Policy

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

For more information, refer to [Audience Sync to Google]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/).