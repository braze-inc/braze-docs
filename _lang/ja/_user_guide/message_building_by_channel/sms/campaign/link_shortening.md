---
nav_title: リンク短縮
article_title: リンク短縮
page_order: 5
description: "この参考記事では、SMSメッセージでリンク短縮をオンにする方法と、よくある質問について説明する。"
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
---

# リンク短縮

> このページでは、SMSメッセージでリンク短縮を有効にする方法、短縮リンクをテストする方法、短縮リンクでカスタムドメインを使用する方法などを紹介する。

リンク短縮とクリックトラッキングにより、SMSメッセージに含まれるURLを自動的に短縮し、クリックスルーレートの分析を収集できます。これにより、ユーザーがSMSキャンペーンにどのようにエンゲージメントしているかを理解するための追加のエンゲージメント指標が提供されます。

キャンペーンとキャンバスの両方で、[メッセージバリアントレベルで]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign)リンク短縮とクリック追跡をオンにすることができる。 

URLの長さは、有効になっているトラッキングの種類によって決まる：
- **基本的なトラッキング**はキャンペーンレベルのクリック追跡を可能にします。静的URLの長さは20文字で、ダイナミックなURLの長さは25文字になります。
- **高度なトラッキング**は、キャンペーンレベルおよびユーザーレベルのクリック追跡を可能にします。クリックは、Currentsを通じて送信される[SMSクリックイベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)も生成します。高度なトラッキングを備えた静的URLは27〜28文字の長さになり、URLをクリックしたユーザーのセグメントを作成することができます。ダイナミックなURLの場合、長さは32〜33文字になります。

リンクは、共有ショートドメイン（`brz.ai`）を使用して短縮されます。例として、URLは次のようになります: `https://brz.ai/8jshX` (基本的、静的) または `https://brz.ai/8jshX/2dj8d` (高度な、ダイナミックな)。詳細については[テスト](#testing)を参照してください。

`http://` または`https://` で始まる静的URLはすべて短縮される。静的な短縮URLは、作成日から1年間有効です。Liquidパーソナライゼーションを含む短縮URLは2か月間有効です。

{% alert note %}
BrazeAI<sup>TM</sup>[インテリジェント・チャネル・フィルタ]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/)を使用し、SMS チャネルを選択できるようにする場合は、SMS リンクの短縮と高度なトラッキング、[クリックトラッキング]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#click-tracking)をオンにします。
{% endalert %}

## リンク短縮の使用

リンク短縮を使用するには、メッセージコンポーザーのリンク短縮トグルがオンになっていることを確認します。次に、ベーシックトラッキングまたはアドバンストトラッキングを使用することを選択します。

![メッセージ作成画面にリンク短縮のトグルがついた。][1]

Braze は、`http://` または`https://` で始まるURL のみを認識します。URL が認識されると、**プレビュー** セクションがプレースホルダURL で更新されます。BrazeはURLを短縮した後の長さを見積もりますが、警告が表示され、テストユーザーを選択してメッセージを下書きとして保存するよう促され、より正確な見積もりが得られます。

![[メッセージ] ボックスに長い URL が表示され、プレビューに短縮リンクが生成されたメッセージ作成画面。][3]

### UTMパラメータの追加

{% multi_lang_include click_tracking.md section='UTM parameters' %}

## URL での Liquid パーソナライゼーション

Brazeコンポーザー内でURLをダイナミックに構築できるため、URLにダイナミックなUTMパラメーターを追加したり、ユーザーにユニークなリンクを送信したりできます（放棄カートや在庫が戻った特定の商品にユーザーを誘導するなど）。

### サポートされているLiquidパーソナライゼーションタグを使用してURLを作成する

URLは、任意の[サポートされているLiquidパーソナライゼーションタグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)を使用して動的に生成できます。

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

また、カスタム定義されたLiquid変数の短縮もサポートしています。いくつかの例を以下に示します:

### Liquid変数を使用してURLを作成する

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Liquid変数によってレンダリングされたURLを短縮する

LiquidによってレンダリングされるURLは、APIトリガーのプロパティに含まれているものも短縮されます。例えば、{% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %}が有効なURLを表す場合、SMSメッセージを送信する前にそのURLを短縮して追跡します。 

### /messages/send エンドポイントでのURL の短縮

リンク短縮は、[`/messages/send` endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) を介してAPI 専用メッセージに対してもオンになります。基本的または高度なトラッキングをオンにするには、`link_shortening_enabled` または `user_click_tracking_enabled` リクエストパラメーターを使用します。

| パラメータ | required | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| オプション | ブール値 | `link_shortening_enabled`を`true`に設定して、リンクの短縮とキャンペーンレベルのクリックトラッキングを有効にします。トラッキングを使用するには、`campaign_id` と `message_variation_id` が存在しなければなりません。|
|`user_click_tracking_enabled`| オプション | ブール値 | `user_click_tracking_enabled`を`true`に設定して、リンクの短縮、キャンペーンレベルおよびユーザーレベルのクリックトラッキングをオンにします。クリックされたURLのユーザーセグメントを作成するために、追跡されたデータを使用できます。<br><br> このパラメータを使用するには、`link_shortening_enabled` が`true` であり、`campaign_id` と`message_variation_id` が存在しなければなりません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

完全なリクエストパラメーターのリストについては、「[リクエストパラメーター]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters)」を参照してください。

## テスト

キャンペーンまたはキャンバスを起動する前に、まずメッセージをプレビューしてテストすることをお勧めします。そのためには、**Test**タブをプレビューし、[content test groups]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups)または個々のユーザにSMSを送信します。 

このプレビューは、関連するパーソナライゼーションと短縮されたURL で更新されます。文字数と[課金対象のセグメント]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/)も、レンダリングされたパーソナライゼーションと短縮URLを反映するように更新されます。 

テストメッセージを送信する前に、キャンペーンまたはキャンバスを保存して、メッセージに送信される短縮URLの表現を受け取るようにしてください。テスト送信前にキャンペーンまたはキャンバスが保存されていない場合、テスト送信にはプレースホルダURL が含まれます。

{% alert important %}
アクティブなキャンバス内にドラフトが作成された場合、短縮されたURL は生成されません。キャンバスドラフトがアクティブになると、実際の短縮URL が生成されます。
{% endalert %}

![テスト受信者を選択するためのフィールドがあるメッセージの [テスト] タブ。][2]

{% alert note %}
Liquidパーソナライゼーションと短縮URLは、ユーザーが選択された後、**テスト**タブにテンプレート化されます。ユーザーが選択されていることを確認して、正確な文字数を取得してください。
{% endalert %}

## クリックトラッキング

リンク短縮がオンになっている場合、SMS および MMS のパフォーマンステーブルには、バリアントごとのクリックイベントの数と関連するクリック率を示す**総クリック数**というタイトルの列が含まれます。SMSメトリクスの詳細については、[SMSメッセージパフォーマンス]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/#message-performance)を参照してください。

![SMSとMMSのパフォーマンス・メトリクス表。][4]

**歴史的パフォーマンス**と**SMS/MMSパフォーマンス**のチャートには、**総クリック数**のオプションも含まれており、クリックイベントの日次時系列が表示されます。クリック数はリダイレクト時（例えば、ユーザーがリンクを訪問したとき）に増加し、ユーザーごとに複数回増加することがあります。

## ユーザーのリターゲティング

リターゲティングに関するガイダンスについては、[SMSリターゲティング]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links)をご覧ください。

{% multi_lang_include click_tracking.md section='Custom Domains' %}

{% multi_lang_include click_tracking.md section='Frequently Asked Questions' %}

### URL をクリックしている個々のユーザーを特定することはできますか?

はい。**Advanced Tracking** をオンにすると、Currents 経由で送信される[SMS リターゲティングフィルタ]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/)または SMS クリックイベント(`users.messages.sms.ShortLinkClick`)を利用して、URL をクリックしたユーザーをリターゲティングできます。

### リンク短縮作業は、ディープリンクやユニバーサルリンクと連携していますか?

リンク短縮はディープリンクでは機能しない。BranchやAppsFlyerなどのプロバイダーからユニバーサルリンクを短縮することはできるが、Brazeでは、その際に発生する可能性のある問題（アトリビューションが壊れる、リダイレクトが発生するなど）のトラブルシューティングはできない。

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

