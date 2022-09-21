update shopify video


shopify.md

### Supported Shopify custom attributes
{% tabs local %}
{% tab Shopify Custom Attributes %}
| Attribute Name | Description |
| --- | --- |
| `shopify_accepts_marketing` | This custom attribute corresponds to the email marketing opt-in status that is captured on the checkout page. |
| `shopify_sms_consent` | This custom attribute corresponds to the SMS marketing opt-in status that is captured on the checkout page. |
| `shopify_tags`  | This attribute corresponds to the [customer tags](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types) set by Shopify admins. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Example Payload %}
{% subtabs local %}
{% subtab Shopify SMS Consent %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "shopify_sms_consent": {
        "state": "subscribed",
        "opt_in_level": "single_opt_in",
        "collected_from": "other"
      }
    }
  ]
}
```
{% endsubtab %}
{% subtab Shopify Accepts Marketing (Email) %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "shopify_accepts_marketing": true
    }
  ]
}
```
{% endsubtab %}
{% subtab Shopify Tags %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "shopify_tags": "VIP_customer"
    }
  ]
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Supported Shopify standard attributes

- Email
- First Name
- Last Name
- Phone
- City
- Country

{% alert note %}
Braze will only update supported Shopify custom attributes and Braze standard attributes if there is a difference in data from the existing user profile. For example, if the inbound Shopify data contains a first name of Bob and Bob already exists as a first name on the Braze user profile, Braze will not trigger an update, and the customer will not be charged a data point.
{% endalert %}


[22]: {% image_buster /assets/img/Shopify/shopify_segmentation2.png %}
[23]: {% image_buster /assets/img/Shopify/shopify_segmentation3.png %}
[24]: {% image_buster /assets/img/Shopify/shopify_segmentation4.png %}   