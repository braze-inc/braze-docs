{% if include.section == "Integration Tabs" %}

{% tabs local %}
{% tab standard %}
The standard integration is tailored for Shopify online stores, providing a seamless and straightforward setup process. This option allows you to quickly connect your Shopify store to Braze, empowering you to leverage powerful customer engagement tools without extensive technical expertise. With this integration option, you can sync customer data, automate personalized messaging, and enhance your marketing efforts through comprehensive Braze features.

To use the standard Shopify integration, refer to [Shopify standard integration setup]({{site.baseurl}}/shopify_standard_integration/).
{% endtab %}

{% tab custom %}
The custom integration offers a more flexible and composable solution if you use Shopify Hydrogen or support a headless store. This option empowers you to implement Braze SDKs directly into your Shopify environment, enabling deeper integration and tailored functionalities. Whether you’re looking to create unique customer experiences or optimize specific workflows, the custom integration provides the tools necessary to fully leverage Braze’s capabilities in a headless setup.

To use the custom Shopify integration, refer to [Shopify custom integration setup]({{site.baseurl}}/shopify_custom_integration/).
{% endtab %}
{% endtabs %}

{% endif %}