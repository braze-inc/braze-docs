{% if include.section == "Integration Tabs" %}

{% tabs local %}
{% tab standard %}
표준 통합은 Shopify 온라인 스토어에 맞춤화되어 있으며, 원활하고 간편한 설정 프로세스를 제공합니다. This option allows you to quickly connect your Shopify store to Braze, empowering you to leverage powerful customer engagement tools without extensive technical expertise. With this integration option, you can sync customer data, automate personalized messaging, and enhance your marketing efforts through comprehensive Braze features.

Shopify 표준 통합을 사용하려면 [Shopify 표준 통합 설정을]({{site.baseurl}}/shopify_standard_integration/) 참조하십시오.
{% endtab %}

{% tab custom %}
The custom integration offers a more flexible and composable solution if you use Shopify Hydrogen or support a headless store. This option empowers you to implement Braze SDKs directly into your Shopify environment, enabling deeper integration and tailored functionalities. 독특한 고객 경험을 창출하거나 특정 워크플로를 최적화하려는 경우, 커스텀 통합은 헤드리스 설정에서 Braze의 기능을 최대한 활용하는 데 필요한 도구를 제공합니다.

Shopify 커스텀 통합을 사용하려면 [Shopify 커스텀 통합 설정을]({{site.baseurl}}/shopify_custom_integration/) 참조하십시오.
{% endtab %}
{% endtabs %}

{% endif %}

{% if include.section == "Liquid promotion codes with Currents" %}

[프로모션 ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/)코드와 [`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/)결합하여 커런츠에 프로모션 코드 정보를 전송할 수 있습니다. 태그를`capture` 사용하여 프로모션 코드를 변수에 저장한 후, 해당 변수를 에서 참조하세요`message_extras`:

{% raw %}
```liquid
{% capture code %}
{% promotion('puttshacktest2') %}
{% endcapture %}
Use {{code}} for an exclusive discount!
{% message_extras :key cardscode :value {{code}} %}
```
{% endraw %}

{% endif %}