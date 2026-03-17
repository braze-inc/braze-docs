{% if include.section == "Integration Tabs" %}

{% tabs local %}
{% tab standard %}
A integração padrão é feita sob medida para lojas online Shopify, proporcionando um processo de configuração simples e direto. Esta opção permite que você conecte rapidamente sua loja Shopify ao Braze, capacitando-o a aproveitar ferramentas poderosas de engajamento de clientes sem necessidade de ampla expertise técnica. Com esta opção de integração, você pode sincronizar dados de clientes, automatizar o envio de mensagens personalizadas e aprimorar seus esforços de marketing por meio de recursos abrangentes do Braze.

Para usar a integração padrão do Shopify, consulte [configuração da integração padrão do Shopify]({{site.baseurl}}/shopify_standard_integration/).
{% endtab %}

{% tab custom %}
A integração personalizada oferece uma solução mais flexível e composta se você usar Shopify Hydrogen ou suportar uma loja headless. Esta opção permite que você implemente os SDKs do Braze diretamente em seu ambiente Shopify, possibilitando uma integração mais profunda e funcionalidades personalizadas. Se você está procurando criar experiências únicas para os clientes ou otimizar fluxos de trabalho específicos, a integração personalizada fornece as ferramentas necessárias para aproveitar totalmente as capacidades do Braze em uma configuração headless.

Para usar a integração personalizada do Shopify, consulte [configuração da integração personalizada do Shopify]({{site.baseurl}}/shopify_custom_integration/).
{% endtab %}
{% endtabs %}

{% endif %}

{% if include.section == "Liquid promotion codes with Currents" %}

Você pode combinar [`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/) com [códigos de promoção]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/) para enviar informações de códigos de promoção para Currents. Use a tag `capture` para armazenar o código de promoção em uma variável, depois faça referência a essa variável em `message_extras`:

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