## Google Tag Manager for Webについて {#google-tag-manager}

Google Tag Manager (GTM)を使えば、プロダクションコードのリリースや開発リソースを必要とせずに、Webサイトのタグをリモートで追加、削除、編集できる。BrazeはWeb SDK用に以下のテンプレートを提供している：

|タグの種類|ユースケース|
|--------|--------|
| 初期化タグ | このタグにより、サイトのコードを変更することなく、[Web Braze SDKを統合する]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web)ことができる。|
| アクションタグ | このタグで[コンテンツカードの作成]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager)、[ユーザー属性の設定]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web)、[データ収集の管理が]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web)できる。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## グーグルのEUユーザー同意ポリシー

{% alert important %}
Googleは、2024年3月6日から施行される[デジタル市場法（DMA）](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)の変更に対応して、[EUユーザー同意ポリシー](https://www.google.com/about/company/user-consent-policy/)を更新しています。この新しい変更により、広告主は EEA および英国のエンドユーザーに特定の情報を開示し、必要な同意を得る必要があります。次のドキュメントを確認して、詳細を学んでください。
{% endalert %}

Google のEU ユーザー同意ポリシーの一部として、次のブール値カスタム属性をユーザープロファイルに記録する必要があります。

- `$google_ad_user_data`
- `$google_ad_personalization`

GTM 統合を使用してこれらを設定する場合、カスタム属性でカスタム HTML タグを作成する必要があります。以下は、これらの値を(文字列としてではなく)ブールデータ型としてログに記録する方法の例です。

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

詳細については、[オーディエンスを Google に同期する]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/)を参照してください。
