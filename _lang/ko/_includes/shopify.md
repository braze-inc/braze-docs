{% if include.section == "Integration Tabs" %}

{% tabs local %}
{% tab 표준 %}
표준 통합은 Shopify 온라인 스토어에 맞게 조정되어 원활하고 간단한 설정 프로세스를 제공합니다. This option allows you to quickly connect your Shopify store to Braze, empowering you to leverage powerful customer engagement tools without extensive technical expertise. With this integration option, you can sync customer data, automate personalized messaging, and enhance your marketing efforts through comprehensive Braze features.

표준 Shopify 통합을 사용하려면 [Shopify 표준 통합 설정을]({{site.baseurl}}/shopify_standard_integration/) 참조하십시오.
{% endtab %}

{% tab 커스텀 %}
The custom integration offers a more flexible and composable solution if you use Shopify Hydrogen or support a headless store. This option empowers you to implement Braze SDKs directly into your Shopify environment, enabling deeper integration and tailored functionalities. 고유한 고객 경험을 만들거나 특정 워크플로를 최적화하려는 경우 커스텀 통합을 통해 헤드리스 설정에서 Braze의 기능을 최대한 활용하는 데 필요한 도구를 제공합니다.

커스텀 Shopify 통합을 사용하려면 [Shopify 커스텀 통합 설정을]({{site.baseurl}}/shopify_custom_integration/) 참조하십시오.
{% endtab %}
{% endtabs %}

{% endif %}

{% if include.section == "Liquid promotion codes with Currents" %}

프로모션 코드와 결합하여 [`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/) 를 [프로모션 코드]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/) 와 결합하여 프로모션 코드 정보를 커런츠에 전송할 수 있습니다. `capture` 태그를 사용하여 프로모션 코드를 변수에 저장한 다음 `message_extras` 에서 해당 변수를 참조합니다:

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