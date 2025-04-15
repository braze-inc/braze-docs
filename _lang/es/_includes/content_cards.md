{% tabs %}
{% tab Android %}
Por defecto, el [SDK nativo para Android de Braze](https://github.com/braze-inc/braze-android-sdk) no proporciona soporte GIF animado para las tarjetas de contenido; sin embargo, puedes utilizar una biblioteca de imágenes de terceros para mostrar GIF en su lugar. Para más información, consulta [Tarjetas de contenido Android: GIFs]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/GIFs/).
{% endtab %}

{% tab iOS %}
Por defecto, el [SDK de Braze Swift](https://github.com/braze-inc/braze-swift-sdk) no proporciona soporte GIF animado para tarjetas de contenido; sin embargo, puedes envolver tu propia vista o la de un tercero en una instancia de [`GIFViewProvider`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/gifviewprovider). Para un recorrido completo, consulta [Tutorial: Soporte GIF para tarjetas de contenido Swift](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support/).
{% endtab %}
{% endtabs %}
