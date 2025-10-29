{% if include.section == "Integration Tabs" %}

{% tabs local %}
{% tab padrão %}
A integração padrão é feita sob medida para as lojas on-line do Shopify, proporcionando um processo de configuração simples e direto. Essa opção permite que você conecte rapidamente sua loja Shopify ao Braze, possibilitando o engajamento de poderosas ferramentas de engajamento do cliente sem a necessidade de conhecimento técnico extensivo. Com essa opção de integração, você pode sincronizar dados de clientes, automatizar o envio de mensagens personalizadas e aprimorar seus esforços de marketing por meio de recursos abrangentes do Braze.

Para usar a integração padrão do Shopify, consulte [Configuração da integração padrão do Shopify]({{site.baseurl}}/shopify_standard_integration/).
{% endtab %}

{% tab personalizado %}
A integração personalizada oferece uma solução mais flexível e criadora se você usar o Shopify Hydrogen ou suportar uma loja headless. Essa opção lhe permite implementar os SDKs do Braze diretamente em seu ambiente Shopify, ativando uma integração mais profunda e funcionalidades personalizadas. Seja para criar experiências exclusivas para o cliente ou otimizar fluxos de trabalho específicos, a integração personalizada fornece as ferramentas necessárias para aproveitar totalmente os recursos do Braze em uma configuração headless.

Para usar a integração personalizada do Shopify, consulte a [configuração da integração personalizada do Shopify]({{site.baseurl}}/shopify_custom_integration/).
{% endtab %}
{% endtabs %}

{% endif %}

{% if include.section == "Liquid promotion codes with Currents" %}

Você pode combinar [`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/) com [códigos promocionais]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/) para enviar informações sobre códigos promocionais ao Currents. Use a tag `capture` para armazenar o código de promoção em uma variável e, em seguida, faça referência a essa variável em `message_extras`:

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