リンク短縮とクリックトラッキングを使用すると、SMS または RCS メッセージに含まれる URL を自動的に短縮し、クリックスルー率の分析を収集できます。これにより、追加のエンゲージメント指標が提供され、ユーザーがキャンペーンにどのように関わっているかを理解するのに役立ちます。

リンク短縮とクリックトラッキングは、キャンペーンとキャンバスの両方で[メッセージバリアントレベル]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign)で有効にできます。

URL の長さは、有効にしたトラッキングの種類によって決まります。
- **基本トラッキング**は、キャンペーンレベルのクリックトラッキングを有効にします。静的 URL の長さは20文字、パーソナライズ済み URL の長さは25文字になります。
- **高度なトラッキング**は、キャンペーンレベルおよびユーザーレベルのクリックトラッキングを有効にし、クリックに基づくセグメンテーションやリターゲティング機能の使用を可能にします。クリックは Currents を通じて送信される [SMS クリックイベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)も生成します。高度なトラッキングを使用した静的 URL の長さは27〜28文字になり、URL をクリックしたユーザーのセグメントを作成できます。パーソナライズ済み URL の長さは32〜33文字になります。

リンクは、共有短縮ドメイン（`brz.ai`）またはカスタムリンク短縮ドメインを使用して短縮されます。URL の例は次のようになります：`https://brz.ai/8jshX`（基本、静的）または `https://brz.ai/p/8jshX/2dj8d`（高度、パーソナライズ済み）。詳細については[テスト](#testing)を参照してください。

`http://` または `https://` で始まる静的 URL はすべて短縮されます。静的短縮 URL は作成日から1年間有効です。Liquid パーソナライゼーションを含む短縮 URL は2か月間有効です。

{% alert note %}
BrazeAI<sup>TM</sup> [インテリジェントチャネルフィルター]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/)を使用する予定で、SMS および RCS チャネルを選択可能にしたい場合は、高度なトラッキングを使用したリンク短縮を有効にしてください。
{% endalert %}

## リンク短縮の使用

リンク短縮を使用するには、メッセージ作成画面のリンク短縮トグルが有効になっていることを確認してください。次に、基本トラッキングまたは高度なトラッキングのいずれかを選択します。

![リンク短縮のトグルがあるメッセージ作成画面。]({% image_buster /assets/img/link_shortening/legacy/temp_shortening1.png %})

Braze は `http://` または `https://` で始まる URL のみを認識します。URL が認識されると、**プレビュー**セクションがプレースホルダー URL で更新されます。Braze は短縮後の URL の長さを推定しますが、より正確な推定を得るためにテストユーザーを選択してメッセージを下書きとして保存するよう警告が表示されます。

![「メッセージ」ボックスに長い URL があり、プレビューに生成された短縮リンクが表示されたメッセージ作成画面。]({% image_buster /assets/img/link_shortening/legacy/temp_shortening3.png %})

### UTM パラメーターの追加

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## URL での Liquid パーソナライゼーション

Braze の作成画面内で URL を動的に構築できるため、URL にダイナミックな UTM パラメーターを追加したり、ユーザーにユニークなリンクを送信したりできます（放棄カートや在庫が復活した特定の製品にユーザーを誘導するなど）。

### サポートされている Liquid パーソナライゼーションタグを使用した URL の作成

URL は、[サポートされている Liquid パーソナライゼーションタグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)を使用して動的に生成できます。

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

カスタム定義の Liquid 変数の短縮もサポートしています。以下にいくつかの例を示します。

### Liquid 変数を使用した URL の作成

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Liquid 変数によってレンダリングされた URL の短縮

Liquid によってレンダリングされた URL は、API トリガープロパティに含まれるものも含めて短縮されます。たとえば、{% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} が有効な URL を表す場合、メッセージを送信する前にその URL を短縮してトラッキングします。

### `/messages/send` エンドポイントでの URL 短縮

リンク短縮は、[`/messages/send` エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)を通じた API のみのメッセージでも有効にできます。基本トラッキングまたは高度なトラッキングも有効にするには、`link_shortening_enabled` または `user_click_tracking_enabled` リクエストパラメーターを使用します。

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| オプション | ブール値 | `link_shortening_enabled` を `true` に設定すると、リンク短縮とキャンペーンレベルのクリックトラッキングが有効になります。トラッキングを使用するには、`campaign_id` と `message_variation_id` が必要です。|
|`user_click_tracking_enabled`| オプション | ブール値 | `user_click_tracking_enabled` を `true` に設定すると、リンク短縮、キャンペーンレベルおよびユーザーレベルのクリックトラッキングが有効になります。トラッキングデータを使用して、URL をクリックしたユーザーのセグメントを作成できます。<br><br> このパラメーターを使用するには、`link_shortening_enabled` が `true` であり、`campaign_id` と `message_variation_id` が必要です。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

リクエストパラメーターの完全なリストについては、[リクエストパラメーター]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters)を参照してください。

## テスト

キャンペーンまたはキャンバスを起動する前に、まずメッセージをプレビューしてテストすることがベストプラクティスです。これを行うには、**テスト**タブに移動して、[コンテンツテストグループ]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups)または個々のユーザーに SMS または RCS メッセージをプレビューして送信します。

このプレビューは、関連するパーソナライゼーションと短縮 URL で更新されます。文字数と[課金対象セグメント]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/)も、レンダリングされたパーソナライゼーションと短縮 URL を反映して更新されます。

テストメッセージを送信する前にキャンペーンまたはキャンバスを保存して、メッセージで配信される短縮 URL の表現を受け取るようにしてください。テスト送信前にキャンペーンまたはキャンバスが保存されていない場合、テスト送信にはプレースホルダー URL が含まれます。

キャンバスが「短縮 SMS リンクをクリック」フィルターに表示されるには、短縮リンクを含むキャンバスステップでも高度なトラッキングが有効になっている必要があります。これにより、ユーザーレベルのクリックトラッキングが可能になります。短縮リンクが基本トラッキングで設定されている場合、SMS 短縮リンクのクリックイベントをフィルタリングするオプションは利用できません。

{% alert important %}
アクティブなキャンバス内で下書きが作成された場合、短縮 URL は生成されません。実際の短縮 URL は、キャンバスの下書きがアクティブになったときに生成されます。
{% endalert %}

![テスト受信者を選択するフィールドがあるメッセージの「テスト」タブ。]({% image_buster /assets/img/link_shortening/legacy/temp_shortening2.png %})

{% alert note %}
Liquid パーソナライゼーションと短縮 URL は、ユーザーが選択された後に**テスト**タブでテンプレート化されます。正確な文字数を取得するために、ユーザーが選択されていることを確認してください。
{% endalert %}

## クリックトラッキング

リンク短縮が有効になっている場合、**SMS/MMS/RCS パフォーマンス**テーブルには**合計クリック数**という列が含まれ、バリアントごとのクリックイベント数と関連するクリック率が表示されます。指標の詳細については、[メッセージパフォーマンス]({{site.baseurl}}/sms_mms_rcs_reporting/)を参照してください。

![SMS および MMS パフォーマンス指標テーブル。]({% image_buster /assets/img/link_shortening/shortening4.png %})

**過去のパフォーマンス**テーブルと **SMS/MMS/RCS パフォーマンス**テーブルにも**合計クリック数**のオプションがあり、クリックイベントの日次時系列が表示されます。クリックはリダイレクト時（ユーザーがリンクにアクセスしたときなど）にカウントされ、ユーザーごとに複数回カウントされる場合があります。

## ユーザーのリターゲティング

リターゲティングに関するガイダンスについては、[リターゲティング]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links)を参照してください。

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### URL をクリックした個々のユーザーを特定できますか？

はい。**高度なトラッキング**が有効になっている場合、[SMS リターゲティングフィルター]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/)または Currents によって送信される SMS クリックイベント（`users.messages.sms.ShortLinkClick`）を活用して、URL をクリックしたユーザーをリターゲティングできます。

### リンク短縮はディープリンクやユニバーサルリンクで機能しますか？

リンク短縮はディープリンクでは機能しません。代わりに、Branch や AppsFlyer などのサードパーティプロバイダーのユニバーサルリンクを短縮できますが、ユーザーに短いリダイレクトや「ちらつき」効果が発生する場合があります。これは、短縮リンクがアプリの起動をサポートするユニバーサルリンクに解決される前に、まず Web を経由してルーティングされるためです。さらに、Braze はユニバーサルリンクの短縮時に発生する可能性のある問題（アトリビューションの破損や予期しないリダイレクトなど）のトラブルシューティングを行うことができません。

{% alert note %}
ユニバーサルリンクでリンク短縮を実装する前に、ユーザーエクスペリエンスをテストして、期待どおりであることを確認してください。
{% endalert %}

### `send_ids` は SMS クリックイベントに関連付けられていますか？

いいえ。ただし、高度なトラッキングが有効になっている場合、[クエリビルダー]({{site.baseurl}}/query_builder/)を使用して、次のクエリで Currents データをクエリすることにより、一般的に `send_ids` をクリックイベントに関連付けることができます。

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id 
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL; 
```