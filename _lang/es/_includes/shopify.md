{% if include.section == "Integration Tabs" %}

{% tabs local %}
{% tab estándar %}
La integración estándar está adaptada a las tiendas online de Shopify, proporcionando un proceso de configuración sencillo y sin complicaciones. Esta opción te permite conectar rápidamente tu tienda Shopify a Braze, permitiéndote aprovechar potentes herramientas de interacción con los clientes sin necesidad de grandes conocimientos técnicos. Con esta opción de integración, puedes sincronizar los datos de clientes, automatizar la mensajería personalizada y mejorar tus esfuerzos de marketing mediante las completas características de Braze.

Para utilizar la integración estándar de Shopify, consulta [Configuración de la integración estándar de Shopify]({{site.baseurl}}/shopify_standard_integration/).
{% endtab %}

{% tab personalizado %}
La integración personalizada ofrece una solución más flexible y componible si utilizas Shopify Hydrogen o soportas una tienda headless. Esta opción te permite implementar los SDK de Braze directamente en tu entorno de Shopify, habilitando una integración más profunda y funcionalidades a medida. Tanto si quieres crear experiencias del cliente únicas como optimizar flujos de trabajo específicos, la integración personalizada proporciona las herramientas necesarias para aprovechar al máximo las capacidades de Braze en una configuración headless.

Para utilizar la integración personalizada de Shopify, consulta [Configuración de la integración personalizada de Shopify]({{site.baseurl}}/shopify_custom_integration/).
{% endtab %}
{% endtabs %}

{% endif %}

{% if include.section == "Liquid promotion codes with Currents" %}

Puedes combinar [`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/) con [códigos promocionales]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/) para enviar información sobre códigos promocionales a Currents. Utiliza la etiqueta `capture` para almacenar el código promocional en una variable, y luego haz referencia a esa variable en `message_extras`:

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