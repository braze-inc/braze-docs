## Google Tag Manager for Web について {#google-tag-manager}

Google Tag Manager (GTM) を使えば、プロダクションコードのリリースやエンジニアリングリソースを必要とせずに、Web サイトのタグをリモートで追加、削除、編集できます。Braze は Web SDK 用に以下のテンプレートを提供しています。

|タグの種類|ユースケース|
|--------|--------|
| 初期化タグ | このタグにより、サイトのコードを変更することなく、[Web Braze SDK を統合する]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web)ことができます。|
| アクションタグ | このタグで[コンテンツカードの作成]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager)、[ユーザー属性の設定]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web)、[データ収集の管理]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web)ができます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## GTM でカスタムイベントを記録する

GTM の **Custom HTML** タグを使用してカスタムイベントを記録できます。このアプローチでは、GTM の[データレイヤー](https://developers.google.com/tag-platform/tag-manager/datalayer)を使用して、サイトから GTM タグにイベントデータを渡し、Braze Web SDK を呼び出します。

### ステップ 1:データレイヤーにイベントをプッシュする

サイトのコードで、カスタムイベントをトリガーしたい場所でデータレイヤーにイベントをプッシュします。たとえば、ボタンがクリックされたときにカスタムイベントを記録するには、次のようにします。

```html
<button onclick="dataLayer.push({'event': 'my_custom_event'});">Track Event</button>
```

### ステップ 2:GTM でトリガーを作成する

1. GTM コンテナで **Triggers** に移動し、新しいトリガーを作成します。
2. **Trigger Type** を **Custom Event** に設定します。
3. **Event Name** をデータレイヤーにプッシュした値と同じ値（たとえば `my_custom_event`）に設定します。
4. トリガーを発火するタイミングを選択します（たとえば **All Custom Events**）。

### ステップ 3:Custom HTML タグを作成する

1. GTM で **Tags** に移動し、新しいタグを作成します。
2. **Tag Type** を **Custom HTML** に設定します。
3. HTML フィールドに以下を追加します。

    ```html
    <script>
    window.braze.logCustomEvent("my_custom_event");
    </script>
    ```

4. **Triggering** で、ステップ 2 で作成したトリガーを選択します。
5. コンテナを保存して公開します。

イベントプロパティを含めるには、2 番目の引数として渡します。

```html
<script>
window.braze.logCustomEvent("my_custom_event", {"property_key": "property_value"});
</script>
```

## Google の EU ユーザー同意ポリシー

{% alert important %}
Google は、2024年3月6日から施行される[デジタル市場法（DMA）](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)の変更に対応して、[EU ユーザー同意ポリシー](https://www.google.com/about/company/user-consent-policy/)を更新しています。この新しい変更により、広告主は EEA および英国のエンドユーザーに特定の情報を開示し、必要な同意を得る必要があります。詳細については、以下のドキュメントを確認してください。
{% endalert %}

Google の EU ユーザー同意ポリシーの一環として、以下のブール値カスタム属性をユーザープロファイルに記録する必要があります。

- `$google_ad_user_data`
- `$google_ad_personalization`

GTM 統合を使用してこれらを設定する場合、カスタム属性ではカスタム HTML タグを作成する必要があります。以下は、これらの値を（文字列としてではなく）ブール値データタイプとして記録する方法の例です。

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

詳細については、[Google へのオーディエンス同期]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/)を参照してください。