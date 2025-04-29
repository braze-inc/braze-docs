{% tabs %}
{% tab Android %}
By default, the native [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk) does not provide animated GIF support for Content Cards&#8212;however, you can use a third-party image library to display GIFs instead. For more information, see [Android Content Cards: GIFs]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs/?sdktab=android).
{% endtab %}

{% tab iOS %}
By default, the [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) does not provide animated GIF support for Content Cards&#8212;however, you can wrap your own view or a third-party view in an instance of [`GIFViewProvider`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/gifviewprovider). For a full walkthrough, see [Tutorial: GIF Support for Swift Content Cards](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support/).
{% endtab %}
{% endtabs %}
