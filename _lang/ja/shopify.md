{% if include.section == "Integration Tabs" %}

{% tabs local %}
{% tab standard %}
標準的な統合は Shopify オンラインストアに合わせて調整されており、シームレスで簡単なセットアッププロセスを提供します。このオプションを使用すると、Shopify ストアを Braze にすばやく接続でき、専門知識がなくても強力なカスタマーエンゲージメントツールを活用することができます。この統合オプションを使用すると、顧客データの同期、パーソナライズされたメッセージングの自動化、包括的な Braze の機能によるマーケティングの強化が可能になります。

通常のShopify積分を使用する場合は、[Shopifyスタンダード積分設定]({{site.baseurl}}/shopify_standard_integration/)を参照してください。
{% endtab %}

{% tab custom %}
カスタム統合は、Shopify Hydrogen を使用している場合やヘッドレスストアをサポートしている場合に、柔軟性が高く構成機能に優れたソリューションを提供します。このオプションは、Shopify 環境に直接 Braze SDK を実装して、詳細な統合と機能のカスタマイズを使用できるようにします。独自のカスタマーエクスペリエンスの提供を望む場合も、特定のワークフローを最適化する場合も、カスタム統合では、ヘッドレス設定で Braze の機能をフルに活用するために必要なツールが提供されます。

カスタムShopifyインテグレーションを使用するには、[Shopifyカスタムインテグレーションセットアップ]({{site.baseurl}}/shopify_custom_integration/)を参照してください。
{% endtab %}
{% endtabs %}

{% endif %}

{% if include.section == "Liquid promotion codes with Currents" %}

[`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/)と[プロモーションコードs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/)を組み合わせて、プロモーションコードをCurrentsに送信できます。`capture` タグを使用して昇格コードを変数に保存し、その変数を`message_extras` で参照します。

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