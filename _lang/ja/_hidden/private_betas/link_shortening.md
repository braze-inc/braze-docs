---
nav_title: "リンク短縮"
permalink: "/updated_link_shortening/"
hidden: true
---

# リンク短縮

> リンク短縮とクリックトラッキングにより、SMSメッセージに含まれるURLを自動的に短縮し、クリックスルー率分析を収集できます。これにより、ユーザーがSMSキャンペーンにどのように関わっているかを理解するのに役立つ追加のエンゲージメント指標が得られます。 

## 概要

リンク短縮とクリックトラッキングは、[キャンペーンとキャンバスの両方でメッセージバリアントレベルで有効にできます]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign)。 

URL の長さは、有効になっているトラッキングの種類によって決まります。
-**ベーシックトラッキングでは、キャンペーンレベルのクリックトラッキングが可能になります**。静的 URL の長さは 20 文字で、動的 URL の長さは 25 文字です。
-**高度なトラッキングにより、キャンペーンレベルとユーザーレベルのクリックトラッキングが可能になります**。アドバンストラッキング機能付きの静的 URL の長さは 27 ～ 28 文字で、URL をクリックしたユーザーのセグメントを作成できます。ダイナミック URL の場合、長さは 32 ～ 33 文字です。

リンクは共有ショートドメイン (`brz.ai`) を使用して短縮されます。URL の例は、`https://brz.ai/8jshX` (基本、静的) または `https://brz.ai/8jshX/2dj8d` (詳細、動的) のようになります。詳細については、「[テスト](#testing)」を参照してください。

静的短縮 URL は、作成日から 1 年間有効です。Liquidパーソナライゼーションを含む短縮URLは2か月間有効です。

{% alert important %}
動的URLの短縮とトラッキングは現在早期アクセス中です。早期アクセスへの参加に興味がある場合は、Braze アカウントマネージャーにお問い合わせください。
{% endalert %}

{% alert note %}
Sage AI [インテリジェントチャネルフィルタを使用する予定で、SMS チャネルを選択できるようにしたい場合は]({{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_channel/)、[アドバンスドトラッキングとクリックトラッキングによる]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#click-tracking) SMS リンク短縮機能を有効にしてください。
{% endalert %}

### リンク短縮を有効にする

リンク短縮を有効にするには、メッセージコンポーザーのリンク短縮トグルが有効になっていることを確認してください。そこから、それぞれのラジアルボタンを選択して、ベーシックトラッキングとアドバンストラッキングのどちらを使用するかを選択します。 

![][1]

Braze が URL を認識するには、URL が _http://または _https:_//_で始まる必要があります。URL が認識されると、**プレビューペインがプレースホルダー** URL で更新されます。Braze は短縮後に URL の長さを推定しますが、より正確な見積もりを行うために、テストユーザーを選択し、メッセージをドラフトとして保存するよう求める警告が表示されます。

![][3]

### URL でのリキッドパーソナライゼーション

Braze Composer 内で直接 URL を動的に作成できるため、URL に動的 UTM パラメータを追加したり、ユーザー固有のリンク (放棄されたカートや再入荷した特定の商品にユーザーを誘導するなど) を送信したりできます。

#### サポートされているLiquidパーソナライゼーションタグを含むURLを作成する

URL は、[サポートされている任意の Liquid パーソナライゼーションタグを使用して動的に生成できます]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)。

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

また、カスタム定義のLiquid変数の短縮もサポートしています。いくつかの例を以下に示します。

#### リキッド変数を使用して URL を作成する

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

#### Liquid 変数によってレンダリングされる URL を短くする

LiquidによってレンダリングされるURLは、APIトリガープロパティに含まれるURLも含めて短縮されます。たとえば、{% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %}が有効なURLを表している場合、SMSメッセージを送信する前にそのURLを短縮して追跡します。 

#### 内の URL を短縮 /messages/send

リンク短縮は、エンドポイント経由の API のみのメッセージでも有効になっています。[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)ベーシックトラッキングまたはアドバンスドトラッキングも有効にするには、`link_shortening_enabled``user_click_tracking_enabled`またはリクエストパラメータを使用します。

| パラメーター | 必須 | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `link_shortening_enabled` | オプション | Boolean | `link_shortening_enabled` `true` に設定すると、リンクの短縮とキャンペーンレベルのクリックトラッキングが有効になります。トラッキングを使用するには、`campaign_id``message_variation_id`とが必要です。|
| `user_click_tracking_enabled` | オプション | Boolean | `user_click_tracking_enabled` `true` に設定すると、リンクの短縮と、キャンペーンレベルおよびユーザーレベルのクリックトラッキングが有効になります。追跡データを使用して、URL をクリックしたユーザーのセグメントを作成できます。トラッキングを使用するには、`campaign_id``message_variation_id`とが必要です。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

リクエストパラメータの完全なリストについては、[リクエストパラメータをご覧ください]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters)。

## テスト

キャンペーンやキャンバスを立ち上げる前に、メッセージをプレビューしてテストすることを常にお勧めします。 

「**テスト**」タブに移動して、SMS をプレビューし、[コンテンツテストグループまたは個々のユーザーに送信します]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups)。プレビューが更新され、関連するカスタマイズと短縮された URL が表示されます。レンダリングされたパーソナライゼーションと短縮URLを反映して、[文字数と請求対象セグメントも更新されます]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/)。 

メッセージで送信される短縮URLの表現を受け取るには、テストメッセージを送信する前にキャンペーンまたはキャンバスを保存してください。テスト送信の前にキャンペーンまたはキャンバスを保存しない場合、テスト送信にはプレースホルダー URL が含まれます。

{% alert important %}
アクティブなキャンバス内で下書きを作成した場合、短縮 URL は生成されません。実際の短縮URLは、Canvasドラフトがアクティブになったときに生成されます。
{% endalert %}

![][2]

{% alert note %}
Liquid パーソナライゼーションと短縮URLは、ユーザーを選択すると、「**テスト**」タブにテンプレート化されます。正確な文字数を受け取るユーザーが選択されていることを確認してください。
{% endalert %}

## クリック追跡

リンク短縮機能を有効にすると、SMSとMMSのパフォーマンステーブルに「**合計クリック数」というタイトルの列が表示されます。この列には、バリアントごとのクリックイベントの数と関連するクリック率が表示されます**。SMS メトリックの詳細については、「[SMS メッセージのパフォーマンス]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/#message-performance)」を参照してください。

![][4]

**履歴パフォーマンスグラフと** **SMS/MMS パフォーマンスグラフには**、**合計クリック数のオプションもあり、クリックイベントの日次時系列が表示されます**。

## ユーザーのリターゲティング

リターゲティングのガイダンスについては、[SMSリターゲティングをご覧ください]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links)。

## カスタムドメイン

リンク短縮機能では、独自のドメインを使用して短縮URLの外観をパーソナライズすることもでき、一貫したブランドイメージを表現するのに役立ちます。

{% alert note %}
カスタムドメインの使用に興味がある場合は、Braze アカウントマネージャーにお問い合わせください。
{% endalert %}

### ドメイン要件

- ドメインはお客様が調達、所有、管理する必要があります。
- この機能に使用するドメインは一意である必要があり（つまり、ウェブサイトのドメインとは異なる）、そのドメインを使用してウェブコンテンツをホストすることはできません。
  - など`sms.braze.com`、独自のサブドメインを使用することもできます。
- URL の長さを最小限に抑えるため、できるだけ文字数の少ないドメインを選択することをおすすめします。

### カスタムドメインを使用する

設定が完了すると、カスタムドメインを 1 つまたは複数の SMS 購読グループに割り当てることができます。 

![サブスクリプションは、リンク短縮ドメインを選択できる設定をグループ化します。] [7]

リンク短縮を有効にして送信されたキャンペーンは、SMS購読グループに関連付けられている割り当てられたドメインを使用します。

![][8]

## よくある質問

### リンク短縮

#### 実際の URL をテスト送信したときに受信したリンクは?

テスト送信前にキャンペーンが下書きとして保存されていれば、はい。それ以外の場合は、プレースホルダーリンクです。開始したキャンペーンで送信される正確なURLは、テスト送信で送信されたURLとは異なる場合があることに注意してください。

#### リンクを短縮するにはBraze SDKをインストールする必要がありますか？

いいえ。リンク短縮は SDK を統合しなくても機能します。

#### どのユーザーが特定のURLをクリックしているのかわかりますか？

はい。アドバンストトラッキングを有効にすると、[SMSリターゲティングフィルターまたはCurrents経由で送信されたSMSクリックイベント（）`users.messages.sms.ShortLinkClick`を利用して、URLをクリックしたユーザーをリターゲティングできます]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting#trigger-messages-as-users-receive-sms)。

#### URL が短縮される前に UTM パラメータを URL に追加できますか?

はい。静的パラメーターと動的パラメーターの両方を追加できます。 

#### 短縮URLはどのくらいの期間有効ですか？

静的 URL は、URL 登録 (初回送信など) から 1 年間有効です。

ダイナミック URL は URL 登録から 2 か月間有効です。

#### リンク短縮機能はディープリンクでもユニバーサルリンクでも使えますか？

リンクを短縮すると、_http://または _https_://_で始まる静的 URL はすべて短縮されます。ただし、（BranchやAppsflyerなどのプロバイダーからの）生成されたユニバーサルリンクをさらに短縮することは、これらのツールの帰属またはリダイレクトを損なう可能性があるため、お勧めしません。

### カスタムドメイン

#### 委任されたドメインを複数のサブスクリプショングループで共有できますか？

はい。1 つのドメインを複数のサブスクリプショングループで使用できます。そのためには、関連付ける必要がある各サブスクリプショングループのドメインを選択します。

#### 委任されたドメインを複数のワークスペースで共有できますか？

はい。ワークスペースが同じ会社内にあることを前提として、ドメインを複数のワークスペースのサブスクリプショングループに関連付けることができます。

[1]: {% image_buster /assets/img/link_shortening/shortening1.png %}
[2]: {% image_buster /assets/img/link_shortening/shortening2.png %}
[3]: {% image_buster /assets/img/link_shortening/shortening3.png %}
[4]: {% image_buster /assets/img/link_shortening/shortening4.png %}
[5]: {% image_buster /assets/img/sms/retargeting5.png %}
[6]: {% image_buster /assets/img/sms/retargeting4.png %}
[7]: {% image_buster /assets/img/custom_domain.png %}
[8]: {% image_buster /assets/img/custom_domain2.png %}
[11]: {% image_buster /assets/img/sms/link_shortening10.png %}
[13]: {% image_buster /assets/img/link_shortening/shortening3.png %}   

