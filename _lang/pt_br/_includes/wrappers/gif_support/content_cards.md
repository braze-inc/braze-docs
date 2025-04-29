{% tabs %}
{% tab Android %}
Por padrão, o [SDK nativo da Braze para Android](https://github.com/braze-inc/braze-android-sdk) não oferece suporte a GIFs animados para cartões de conteúdo; no entanto, você pode usar uma biblioteca de imagens de terceiros para exibir GIFs. Para saber mais, consulte [Cartões de conteúdo do Android: GIFs]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs/?sdktab=android).
{% endtab %}

{% tab iOS %}
Por padrão, o [SDK do Braze Swift](https://github.com/braze-inc/braze-swift-sdk) não oferece suporte a GIFs animados para cartões de conteúdo; no entanto, você pode envolver sua própria visualização ou uma visualização de terceiros em uma instância de [`GIFViewProvider`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/gifviewprovider). Para obter um passo a passo completo, consulte [Tutorial: Suporte a GIFs para cartões de conteúdo Swift](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support/).
{% endtab %}
{% endtabs %}
