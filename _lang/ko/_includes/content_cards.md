{% tabs %}
{% tab Android %}
기본적으로 기본 [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk)는 콘텐츠 카드에 애니메이션 GIF를 지원하지 않지만, 타사 이미지 라이브러리를 사용하여 GIF를 대신 표시할 수 있습니다. 자세한 내용은 [Android 콘텐츠 카드를 참조하세요: GIF]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/GIFs/).
{% endtab %}

{% tab iOS %}
기본적으로 [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk)는 콘텐츠 카드에 애니메이션 GIF 지원을 제공하지 않지만, 인스턴스의 [`GIFViewProvider`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/gifviewprovider)에서 자체 보기 또는 타사 보기를 래핑할 수 있습니다. 전체 안내는 [튜토리얼을 참조하세요: Swift 콘텐츠 카드에 대한 GIF 지원](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support/).
{% endtab %}
{% endtabs %}
