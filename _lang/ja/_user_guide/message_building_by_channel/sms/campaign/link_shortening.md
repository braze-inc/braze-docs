---
nav_title: リンク短縮
article_title: リンク短縮
page_order: 5
description: "このリファレンス記事では、SMSメッセージでリンク短縮を有効にする方法と、よくある質問について説明します。"
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
---

# リンク短縮

> リンク短縮とクリックトラッキングにより、SMSメッセージに含まれるURLを自動的に短縮し、クリックスルーレートの分析を収集できます。これにより、ユーザーがSMSキャンペーンにどのようにエンゲージメントしているかを理解するための追加のエンゲージメント指標が提供されます。 

## 概要

リンクの短縮とクリックのトラッキングは、キャンペーンとキャンバスの両方で[メッセージバリアントレベル]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign)で有効にできます。 

URLの長さは、有効になっているトラッキングの種類によって決まります。
- **基本的なトラッキング**はキャンペーンレベルのクリック追跡を可能にします。静的URLの長さは20文字で、ダイナミックなURLの長さは25文字になります。
- **高度なトラッキング**は、キャンペーンレベルおよびユーザーレベルのクリック追跡を可能にします。クリックは、Currentsを通じて送信される[SMSクリックイベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/)も生成します。高度なトラッキングを備えた静的URLは27〜28文字の長さになり、URLをクリックしたユーザーのセグメントを作成することができます。ダイナミックなURLの場合、長さは32〜33文字になります。

リンクは、共有ショートドメイン（`brz.ai`）を使用して短縮されます。例として、URLは次のようになります: `https://brz.ai/8jshX` (基本的、静的) または `https://brz.ai/8jshX/2dj8d` (高度な、ダイナミックな)。詳細については[テスト](#testing)を参照してください。

静的な短縮URLは、作成日から1年間有効です。Liquidパーソナライゼーションを含む短縮URLは2か月間有効です。

{% alert note %}
Sage AIの[インテリジェントチャネルフィルター]({{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_channel/)を使用する予定があり、SMSチャネルを選択可能にしたい場合は、高度なトラッキングおよび[クリックトラッキング]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#click-tracking)を使用してSMSリンクの短縮をオンにしてください。
{% endalert %}

### リンク短縮の有効化

リンク短縮を有効にするには、メッセージ作成画面のリンク短縮トグルが有効になっていることを確認してください。そこから、それぞれのラジアルボタンを選択して、基本的なトラッキングまたは高度なトラッキングを使用するかを選択します。 

![][1]

BrazeがURLを認識するには、それらは_http://_または_https://_で始まる必要があります。URL が認識されると、**プレビュー** ペインがプレースホルダー URL で更新されます。BrazeはURLを短縮した後の長さを見積もりますが、警告が表示され、テストユーザーを選択してメッセージを下書きとして保存するよう促され、より正確な見積もりが得られます。

![][3]

### URL内のLiquidパーソナライゼーション

Brazeコンポーザー内でURLをダイナミックに構築できるため、URLにダイナミックなUTMパラメーターを追加したり、ユーザーにユニークなリンクを送信したりできます（放棄カートや在庫が戻った特定の商品にユーザーを誘導するなど）。

#### サポートされているLiquidパーソナライゼーションタグを使用してURLを作成する

URLは、任意の[サポートされているLiquidパーソナライゼーションタグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)を使用して動的に生成できます。

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

また、カスタム定義されたLiquid変数の短縮もサポートしています。いくつかの例を以下に示します:

#### Liquid変数を使用してURLを作成する

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

#### Liquid変数によってレンダリングされたURLを短縮する

LiquidによってレンダリングされるURLは、APIトリガーのプロパティに含まれているものも短縮されます。例えば、{% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %}が有効なURLを表す場合、SMSメッセージを送信する前にそのURLを短縮して追跡します。 

#### メッセージ/送信でURLを短縮する

リンクの短縮化は、[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)エンドポイントを通じてAPI専用メッセージにも対応しています。基本的または高度なトラッキングを有効にするには、`link_shortening_enabled` または `user_click_tracking_enabled` リクエストパラメータを使用します。

| パラメータ | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| オプション | ブール値 | `link_shortening_enabled`を`true`に設定して、リンクの短縮とキャンペーンレベルのクリックトラッキングを有効にします。トラッキングを使用するには、`campaign_id`と`message_variation_id`が存在している必要があります。|
|`user_click_tracking_enabled`| オプション | ブール値 | `user_click_tracking_enabled`を`true`に設定して、リンクの短縮、キャンペーンレベルおよびユーザーレベルのクリックトラッキングをオンにします。クリックされたURLのユーザーセグメントを作成するために、追跡されたデータを使用できます。トラッキングを使用するには、`campaign_id`と`message_variation_id`が存在している必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

完全なリクエストパラメータのリストについては、[リクエストパラメータ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters)を参照してください。

## テスト

常にメッセージをプレビューおよびテストしてから、キャンペーンまたはキャンバスを開始することをお勧めします。 

**テスト** タブに移動して、プレビューしてSMSを[コンテンツテストグループ]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups)または個々のユーザーに送信します。プレビューは関連するパーソナライゼーションと短縮URLで更新されます。文字数と[課金対象のセグメント]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/)も、レンダリングされたパーソナライゼーションと短縮URLを反映するように更新されます。 

テストメッセージを送信する前に、キャンペーンまたはキャンバスを保存して、メッセージに送信される短縮URLの表現を受け取るようにしてください。キャンペーンまたはキャンバスがテスト送信の前に保存されていない場合、テスト送信にはプレースホルダーURLが含まれます。

{% alert important %}
アクティブなキャンバス内で下書きが作成された場合、短縮URLは生成されません。キャンバス下書きがアクティブになると、実際の短縮URLが生成されます。
{% endalert %}

![][2]

{% alert note %}
Liquidパーソナライゼーションと短縮URLは、ユーザーが選択された後、**テスト**タブにテンプレート化されます。ユーザーが選択されていることを確認して、正確な文字数を取得してください。
{% endalert %}

## クリックトラッキング

リンク短縮が有効になっている場合、SMSおよびMMSのパフォーマンステーブルには、バリアントごとのクリックイベントの数と関連するクリック率を示す**総クリック数**というタイトルの列が含まれます。SMSメトリクスの詳細については、[SMSメッセージパフォーマンス]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/#message-performance)を参照してください。

![][4]

**歴史的パフォーマンス**と**SMS/MMSパフォーマンス**のチャートには、**総クリック数**のオプションも含まれており、クリックイベントの日次時系列が表示されます。クリック数はリダイレクト時（例えば、ユーザーがリンクを訪問したとき）に増加し、ユーザーごとに複数回増加することがあります。

## リターゲティングユーザー

リターゲティングに関するガイダンスについては、[SMSリターゲティング]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links)をご覧ください。

## カスタムドメイン

リンクの短縮は、独自のドメインを使用して短縮URLの外観をパーソナライズし、一貫したブランド画像を表現するのに役立ちます。

{% alert note %}
カスタムドメインの使用を開始したい場合は、Brazeのアカウントマネージャーにお問い合わせください。
{% endalert %}

### ドメイン要件

- ドメインはあなたが取得し、所有し、管理する必要があります。
- この機能に使用されるドメインは一意でなければならず（つまり、あなたのWeb サイトのドメインとは異なる必要があります）、そのドメインはWebコンテンツをホストするために使用することはできません。
  - また、`sms.braze.com`などのユニークなサブドメインを使用することもできます。
- できるだけ短い文字数のドメインを選択することをお勧めします。これにより、URLの長さを最小限に抑えることができます。

#### カスタムドメインの委任

ドメインをBrazeに委任すると、証明書の更新は自動的に行われ、サービスの中断を防ぎます。 

Braze にドメインを委任するには、次の手順に従ってください: 

1. 上記の要件を満たすドメインを顧客成功マネージャーに持ってきてください。Brazeは、ドメインの既存のDNS構成を確認し、次のことを確認します。
- CAAレコードは存在しません OR
- CAAレコード*do*は存在しますが、{% raw %}`<any number> issue "letsencrypt.org"`{% endraw %}または{% raw %}`<anynumber> issuewild "letsencrypt.org"`{% endraw %}のレコードがあります
2. 新しいAレコードを4つ作成し、それぞれのIPに対して1つずつ作成し、それらがドメインリンクホストに存在する唯一のAレコードであることを確認します。
- 151.101.130.133
- 151.101.194.133
- 151.101.2.133
- 151.101.66.133

### カスタムドメインの使用

一度設定すると、カスタムドメインを1つまたは複数のSMSサブスクリプショングループに割り当てることができます。 

![サブスクリプショングループの設定により、リンク短縮ドメインを選択できます。][7]

リンク短縮が有効になっているキャンペーンは、SMSサブスクリプショングループに関連付けられた割り当てドメインを使用します。

![][8]

## よくある質問

### リンク短縮

#### テスト送信時に受け取るリンクは実際のURLですか？

キャンペーンがテスト送信前に下書きとして保存されている場合は、はい。それ以外の場合は、プレースホルダーリンクです。送信されたキャンペーンで送信された正確なURLは、テスト送信で送信されたURLとは異なる場合があることに注意してください。

#### リンクを短縮するためにBraze SDKをインストールする必要がありますか？

いいえ。リンクの短縮は、SDKの統合なしで機能します。

#### 私はどの個々のユーザーがURLをクリックしているかを知っていますか？

そうです。高度なトラッキングがオンになっている場合、[SMSリターゲティングフィルター]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/)やCurrents経由で送信されたSMSクリックイベント（`users.messages.sms.ShortLinkClick`）を活用して、URLをクリックしたユーザーをリターゲティングすることができます。

#### URLを短縮する前にUTMパラメータを追加できますか？

そうです。静的パラメータとダイナミックなパラメータの両方を追加できます。 

#### 短縮URLはどのくらいの期間有効ですか？

静的URLは、URL登録時（最初の送信など）から1年間有効です。

ダイナミックなURは、URL登録時から2か月間有効です。

#### ディープリンクやユニバーサルリンクでリンク短縮は機能しますか？

リンクの短縮は、_http://_ または _https://_ で始まる静的URLを短縮します。ただし、生成されたユニバーサルリンク（BranchやAppsFlyerなどのプロバイダーからのもの）をさらに短縮することはお勧めしません。これにより、これらのツールのアトリビューションやリダイレクトが壊れる可能性があります。

### カスタムドメイン

#### 委任されたドメインは複数のサブスクリプショングループ間で共有できますか？

はい、単一のドメインを複数のサブスクリプショングループで使用できます。そのためには、各サブスクリプショングループが関連付けられるドメインを選択します。

#### 委任されたドメインは複数のワークスペース間で共有できますか？

はい、ドメインは複数のワークスペース内のサブスクリプショングループに関連付けることができます。ワークスペースが同じ会社内に含まれている場合に限ります。

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

