リンク短縮を使用すると、SMSまたはRCSメッセージに含まれるURLを自動的に短縮し、クリックスルー率の分析を収集できます。これにより、追加のエンゲージメント指標が提供され、ユーザーがキャンペーンにどのように関わっているかを理解するのに役立ちます。

リンク短縮は、キャンペーンとキャンバスの両方で[メッセージバリアントレベル]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign)で有効にできます。リンク短縮が有効になると、クリックにより Currents を通じて送信される [SMSクリックイベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)が生成されます。

リンクは共有ショートドメイン（`brz.ai`）またはカスタムリンク短縮ドメインを使用して短縮され、作成日から9週間有効です。URLの例は `https://brz.ai/8jshX2dj` のようになります。

## リンク短縮の使用

リンク短縮を使用するには、メッセージ作成画面のリンク短縮チェックボックスが選択されていることを確認してください。

{% tabs %}
{% tab SMS composer %}

![リンク短縮のチェックボックスが選択されたSMSメッセージ作成画面。]({% image_buster /assets/img/link_shortening/shortening1.png %})

{% endtab %}
{% tab RCS composer %}

![リンク短縮のチェックボックスが選択されたRCSメッセージ作成画面。]({% image_buster /assets/img/link_shortening/shortening1_rcs.png %})

{% endtab %}
{% endtabs %}

Braze は `http://` または `https://` で始まるURLのみを認識します。URLが認識されると、**プレビュー**セクションがプレースホルダーURLで更新されます。Braze は短縮後のメッセージの長さを推定しますが、より正確な推定のためにテストユーザーを選択してメッセージを下書きとして保存するよう警告が表示されます。

![「メッセージ」ボックスに長いURLが入力され、プレビューに生成された短縮リンクが表示されたメッセージ作成画面。]({% image_buster /assets/img/link_shortening/shortening3.png %})

### UTMパラメーターの追加

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## URLでのLiquidパーソナライゼーション

Braze の作成画面内で直接URLをダイナミックに構築できるため、URLにダイナミックなUTMパラメーターを追加したり、ユーザーにユニークなリンクを送信したりできます（放棄カートや在庫が復活した特定の製品にユーザーを誘導するなど）。

### サポートされているLiquidパーソナライゼーションタグを使用したURLの作成

URLは、[サポートされているLiquidパーソナライゼーションタグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)を使用してダイナミックに生成できます。

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

カスタム定義のLiquid変数の短縮もサポートしています。以下にいくつかの例を示します。

### Liquid変数を使用したURLの作成

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Liquid変数によってレンダリングされたURLの短縮

Liquid によってレンダリングされたURL（APIトリガープロパティに含まれるものも含む）を短縮します。例えば、{% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} が有効なURLを表す場合、メッセージを送信する前にそのURLを短縮してトラッキングします。

### `/messages/send` エンドポイントでのURLの短縮

リンク短縮は、[`/messages/send` エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)を通じたAPIのみのメッセージでも有効になります。リクエストパラメーターの完全なリストについては、[リクエストパラメーター]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters)を参照してください。

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| はい | ブール値 | リンク短縮を有効にするには、`link_shortening_enabled` を `true` に設定します。トラッキングを使用するには、`campaign_id` と `message_variation_id` が存在する必要があります。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## テスト

キャンペーンまたはキャンバスを起動する前に、まずメッセージをプレビューしてテストすることがベストプラクティスです。これを行うには、**テスト**タブに移動して、[コンテンツテストグループ]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups)または個々のユーザーにSMSまたはRCSメッセージをプレビューして送信します。

このプレビューは、関連するパーソナライゼーションと短縮URLで更新されます。文字数と[課金対象セグメント]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/)も、レンダリングされたパーソナライゼーションと短縮URLを反映して更新されます。

テストメッセージを送信する前にキャンペーンまたはキャンバスを保存して、メッセージで配信される短縮URLの表現を受け取るようにしてください。テスト送信前にキャンペーンまたはキャンバスが保存されていない場合、テスト送信にはプレースホルダーURLが含まれます。

{% alert important %}
アクティブなキャンバス内で下書きが作成された場合、短縮URLは生成されません。実際の短縮URLは、キャンバスの下書きがアクティブになったときに生成されます。
{% endalert %}

![テスト受信者を選択するフィールドがあるメッセージの「テスト」タブ。]({% image_buster /assets/img/link_shortening/shortening2.png %})

{% alert note %}
Liquidパーソナライゼーションと短縮URLは、ユーザーが選択された後に**テスト**タブでテンプレート化されます。正確な文字数を取得するために、ユーザーが選択されていることを確認してください。
{% endalert %}

## クリックトラッキング

リンク短縮が有効になっている場合、**SMS/MMS/RCSパフォーマンス**テーブルには、バリアントごとのクリックイベント数と関連するクリック率を示す**合計クリック数**という列が含まれます。指標の詳細については、[メッセージパフォーマンス]({{site.baseurl}}/sms_mms_rcs_reporting/)を参照してください。

![SMSおよびMMSパフォーマンス指標テーブル。]({% image_buster /assets/img/link_shortening/shortening4.png %})

**過去のパフォーマンス**および**SMS/MMS/RCSパフォーマンス**テーブルには、**合計クリック数**のオプションも含まれており、クリックイベントの日次時系列が表示されます。クリックはリダイレクト時（ユーザーがリンクにアクセスした場合など）にインクリメントされ、ユーザーごとに複数回インクリメントされる場合があります。

## ユーザーのリターゲティング

リターゲティングに関するガイダンスについては、[リターゲティング]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links)を参照してください。

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### URLをクリックした個々のユーザーを特定できますか？

はい。[SMSリターゲティングフィルター]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/)または Currents によって送信されるSMSクリックイベント（`users.messages.sms.ShortLinkClick`）を使用して、URLをクリックしたユーザーをリターゲティングできます。

### リンク短縮はディープリンクやユニバーサルリンクで機能しますか？

リンク短縮はディープリンクでは機能しません。代わりに、Branch や AppsFlyer などのサードパーティプロバイダーのユニバーサルリンクを短縮できますが、ユーザーに短いリダイレクトや「ちらつき」効果が発生する場合があります。これは、短縮リンクがアプリの起動をサポートするユニバーサルリンクに解決される前に、まずWebを経由してルーティングされるためです。さらに、Braze はユニバーサルリンクの短縮時に発生する可能性のある問題（アトリビューションの破損や予期しないリダイレクトなど）のトラブルシューティングを行うことができません。

{% alert note %}
ユニバーサルリンクでリンク短縮を実装する前に、ユーザーエクスペリエンスをテストして、期待どおりであることを確認してください。
{% endalert %}

### `send_ids` はSMSクリックイベントに関連付けられていますか？

いいえ。ただし、一般的に [Query Builder]({{site.baseurl}}/query_builder/) を使用して、以下のクエリで Currents データをクエリすることにより、`send_ids` をクリックイベントに関連付けることができます。

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id 
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL; 
```