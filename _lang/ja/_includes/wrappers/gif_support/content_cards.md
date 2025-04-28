{% tabs %}
{% tab Android %}
デフォルトでは、ネイティブの [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk) はコンテンツカードのアニメーション GIF をサポートしていません。ただし、代わりにサードパーティの画像ライブラリを使用して GIF を表示できます。詳しくは、[Androidコンテンツカードを参照のこと：GIF]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs/?sdktab=android).
{% endtab %}

{% tab iOS %}
デフォルトでは、[Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) はコンテンツカードのアニメーション GIF をサポートしていません。ただし、独自のビューまたはサードパーティのビューを [`GIFViewProvider`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/gifviewprovider) のインスタンスにラップできます。完全なチュートリアルについては、[チュートリアル：SwiftコンテンツカードのGIFサポート](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support/).
{% endtab %}
{% endtabs %}
