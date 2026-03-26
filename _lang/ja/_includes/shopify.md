{% if include.section == "Integration Tabs" %}

{% tabs local %}
{% tab standard %}
標準の統合はShopifyオンラインストア向けに設計されており、シームレスに簡単な設定プロセスを提供する。このオプションを使用すると、Shopify ストアを Braze にすばやく接続でき、専門知識がなくても強力なカスタマーエンゲージメントツールを活用することができます。この統合オプションを使用すると、顧客データの同期、パーソナライズされたメッセージングの自動化、包括的な Braze の機能によるマーケティングの強化が可能になります。

標準のShopify連携を使用するには、[Shopify標準連携の設定]({{site.baseurl}}/shopify_standard_integration/)を参照すること。
{% endtab %}

{% tab custom %}
カスタム統合は、Shopify Hydrogen を使用している場合やヘッドレスストアをサポートしている場合に、柔軟性が高く構成機能に優れたソリューションを提供します。このオプションは、Shopify 環境に直接 Braze SDK を実装して、詳細な統合と機能のカスタマイズを使用できるようにします。独自のカスタマーエクスペリエンスを創出したい場合でも、特定のワークフローを最適化したい場合でも、カスタム統合はヘッドレス環境においてBrazeの機能を最大限に活用するために必要なツールを提供する。

カスタムShopify連携を使用するには、[Shopifyカスタム連携の設定]({{site.baseurl}}/shopify_custom_integration/)を参照せよ。
{% endtab %}
{% endtabs %}

{% endif %}

{% if include.section == "Liquid promotion codes with Currents" %}

[プロモーションコード]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/)と[`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/)組み合わせることで、プロモーションコード情報をCurrentsに送信できる。プロモーションコードを変数に保存するには  タグ`capture`を使う。その後、その変数を`message_extras`  で参照する。

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