{% if include.section == "UTM parameters" %}

While link shortening allows you to track your URLs automatically, you can also add UTM parameters to your URLs to track the performance of campaigns in third-party analytics tools, such as Google Analytics.

To add UTM parameters to your URL, do the following:

1. Start with your base URL. This is the URL of the page you want to track (such as `https://www.example.com`).
2. Add a question mark (?) after your base URL.
3. Add each UTM parameter separated by an ampersand (&).

An example is `https://www.example.com?utm_source=newsletter&utm_medium=sms`.

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## Frequently asked questions

### Are the links I receive when test sending real URLs?

If the campaign has been saved as a draft before test sending, yes. Otherwise, it is a placeholder link. Note that the exact URL sent in a launched campaign may differ from the one sent in a test send.

### Can I add UTM parameters to a URL before it is shortened?

Yes. Both static and dynamic parameters can be added. 

### How long do shortened URLs remain valid?

Personalized URLs are valid for two months from the time of URL registration.

### Does the Braze SDK need to be installed in order to shorten links?

No. Link shortening works without any SDK integration.

{% endif %}

{% if include.section == "Custom Domains" %}

## Custom domains

Link shortening also allows you to use your own domain to personalize the look and feel of your shortened URLs, helping portray a consistent brand image. For more information, refer to [Custom domains]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/).

{% endif %}