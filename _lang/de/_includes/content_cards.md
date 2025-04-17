{% tabs %}
{% tab Android %}
Standardmäßig bietet das native [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk) keine Unterstützung für animierte GIFs für Content Cards. Sie können jedoch eine Bildbibliothek eines Drittanbieters verwenden, um stattdessen GIFs anzuzeigen. Weitere Informationen finden Sie unter [Android Content Cards: GIFs]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs/?sdktab=android).
{% endtab %}

{% tab iOS %}
Standardmäßig bietet das [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) keine Unterstützung für animierte GIFs für Content Cards. Sie können jedoch Ihre eigene Ansicht oder eine Ansicht eines Drittanbieters in eine Instanz von [`GIFViewProvider`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/gifviewprovider). Eine vollständige Anleitung finden Sie unter [Tutorial: GIF-Unterstützung für Swift Content Cards](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support/).
{% endtab %}
{% endtabs %}
