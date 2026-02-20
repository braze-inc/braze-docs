## About Google Tag Manager for Web {#google-tag-manager}

Google Tag Manager (GTM) lets you remotely add, remove, and edit tags on your website without requiring a production code release or engineering resources. Braze offers the following templates for the Web SDK:

|Tag Type|Use Case|
|--------|--------|
| Initialization tag | This tag lets you [integrate the Web Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web) without needing to modify your site’s code.|
| Action tag | This tag lets you [create Content Cards]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager), [set user attributes]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web), and [manage data collection]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Logging custom events with GTM

You can log custom events using a **Custom HTML** tag in GTM. This approach uses the GTM [data layer](https://developers.google.com/tag-platform/tag-manager/datalayer) to pass event data from your site to a GTM tag that calls the Braze SDK.

### Step 1: Push the event to the data layer

In your site's code, push an event to the data layer wherever you want to trigger the custom event. For example, to log a custom event when a button is clicked:

```html
<button onclick="dataLayer.push({'event': 'my_custom_event'});">Track Event</button>
```

### Step 2: Create a trigger in GTM

1. In your GTM container, go to **Triggers** and create a new trigger.
2. Set the **Trigger Type** to **Custom Event**.
3. Set the **Event Name** to the same value you pushed to the data layer (for example, `my_custom_event`).
4. Choose when the trigger should fire (for example, **All Custom Events**).

### Step 3: Create a Custom HTML tag

1. In GTM, go to **Tags** and create a new tag.
2. Set the **Tag Type** to **Custom HTML**.
3. In the HTML field, add the following:

    ```html
    <script>
    window.braze.logCustomEvent("my_custom_event");
    </script>
    ```

4. Under **Triggering**, select the trigger you created in step 2.
5. Save and publish your container.

To include event properties, pass them as the second argument:

```html
<script>
window.braze.logCustomEvent("my_custom_event", {"property_key": "property_value"});
</script>
```

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
