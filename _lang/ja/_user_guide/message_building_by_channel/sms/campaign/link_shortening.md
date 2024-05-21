---
nav_title: リンク短縮
article_title: リンク短縮
page_order: 5
description: "このリファレンス記事では、SMSメッセージとよくある質問でリンクの短縮を有効にする方法について説明します。"
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
---

# リンク短縮

> リンクの短縮とクリックの追跡により、SMSメッセージに含まれるURLを自動的に短縮し、クリックスルーレート分析を収集することができます。これにより、ユーザーがSMSキャンペーンにどのように関与しているかを理解するための追加のエンゲージメントメトリクスが提供されます。 

## 概要

リンクの短縮とクリックの追跡は、キャンペーンとキャンバスの両方で[message variant-level]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) で有効にできます。 

URL の長さは、有効になっているトラッキングのタイプによって決まります。
- **基本トラッキング**はキャンペーンレベルのクリックトラッキングを有効にします。基本リンクの長さは20 ～21 文字です。
- **高度なトラッキング** は、キャンペーンレベルおよびユーザーレベルのクリックトラッキングを有効にします。高度なトラッキング機能を備えたリンクは最大7 文字長くなり、URL をクリックしたユーザのセグメントを作成できます。詳細リンクの長さは27 ～28 文字です。

共有ショートドメイン(`brz.ai`)を使用してリンクを短縮します。URL の例は、`https://brz.ai/8jshX` (basic) または`https://brz.ai/8jshX/2dj8d` (advanced) のようになります。詳細については、[テスト](#testing)を参照してください。

短縮されたURL は、作成日から1 年間有効です。

{% alert note %}
Sage AI [インテリジェント・チャネル・フィルタ]({{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_channel/)を使用し、SMSチャネルを選択可能にする場合は、高度なトラッキングと[クリックトラッキング]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#click-tracking)によるSMSリンク短縮をオンにします。
{% endalert %}

### リンク短縮の有効化

リンク短縮を有効にするには、メッセージコンポーザーのリンク短縮トグルが有効になっていることを確認します。そこから、それぞれのラジアルボタンを選択して、「基本」または「詳細」のどちらを使用するかを選択します。 

![][1]

ブレーズがURL を認識するには、_http://_ または_https://_ で始まる必要があります。URL が認識されると、**プレビュー** ペインがプレースホルダURL で更新されます。Braze は短縮後のURL の長さを見積もりますが、警告が表示され、テストユーザを選択し、メッセージを下書きとして保存して、より正確な見積もりを得るよう求められます。

![][3]

## テスト

キャンペーンまたはキャンバスを起動する前に、メッセージをプレビューしてテストすることをお勧めします。 

**Test** タブに移動してプレビューし、[content test groups]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) または個々のユーザにSMS を送信します。プレビューは、関連するパーソナライゼーションと短縮されたURL で更新されます。文字数と[課金可能なセグメント]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/) も更新され、レンダリングされたパーソナライゼーションと短縮されたURL が反映されます。 

メッセージで送信される短縮URL を受信するテストメッセージを送信する前に、必ずキャンペーンまたはキャンバスを保存してください。テスト送信前にキャンペーンまたはキャンバスが保存されていない場合、テスト送信にはプレースホルダURL が含まれます。

{% alert important %}
アクティブなキャンバス内にドラフトが作成された場合、短縮されたURL は生成されません。実際に短縮されたURL は、キャンバスドラフトがアクティブになったときに生成されます。
{% endalert %}

![][2]

{% alert note %}
流動的なパーソナライゼーションと短縮されたURL は、ユーザが選択された後、**Test** タブにテンプレート化されます。ユーザーが正確な文字数を受け取るように選択されていることを確認します。
{% endalert %}

## クリック追跡

リンク短縮が有効になっている場合、SMS とMMS のパフォーマンステーブルには、**Total Clicks** というタイトルの列があり、バリアントごとのクリックイベント数と関連するクリック率が表示されます。SMSメトリクスの詳細については、[SMSメッセージパフォーマンス]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/#message-performance)を参照してください。

![][4]

Historical Performance and SMS Overview チャートには、**Total Clicks**のオプションも含まれており、クリックイベントの毎日の時系列が表示されます。

## ユーザーのターゲット変更

リターゲットのガイダンスについては、[SMS リターゲット]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links) をご覧ください。

## カスタムドメイン

また、リンクの短縮により、独自のドメインを使用して、短縮されたURLの外観や感覚をパーソナライズすることができ、一貫したブランドイメージを表現するのに役立ちます。

{% alert note %}
カスタムドメインの使用開始に関心がある場合は、Braze アカウントマネージャにお問い合わせください。
{% endalert %}

### ドメイン要件

- ドメインは、お客様が調達し、所有し、管理しなければなりません。
- この機能に使用するドメインは一意である必要があり(つまり、ウェブサイトドメインとは異なる)、ドメインを使用してウェブコンテンツをホストすることはできません。
  - また、`sms.braze.com` などの一意のサブドメインを使用することもできます。
- URL の長さを最小限に抑えるため、できるだけ文字数の少ないドメインを選択することをお勧めします。

### カスタムドメインの使用

設定すると、カスタムドメインを1 つまたは複数のSMS サブスクリプショングループに割り当てることができます。 

![リンク短縮ドメインを選択できるサブスクリプショングループ設定][7]

リンク短縮を有効にして送信されたキャンペーンは、SMSサブスクリプショングループに関連付けられている割り当てられたドメインを使用します。

![][8]

## よくある質問

### リンク短縮

#### 短縮されたURLはどのくらいの期間ですか?

短縮されたURL の長さは20 ～21 文字です。

#### Link Shortening は、Liquid を含むURL と連携しますか?

いいえ。現在は、静的URL のみが短縮されています。

#### テスト送信時に受信するリンクは実際のURL ですか?

キャンペーンがテスト送信前にドラフトとして保存されている場合は、はい!それ以外の場合は、プレースホルダリンクです。起動されたキャンペーンで送信された正確なURL は、テスト送信で送信されたURL とは異なる場合があることに注意してください。

#### リンクを短くするために、Braze SDK をインストールする必要がありますか?

No, Link Shortening はSDK 統合なしで動作します。

#### URLをクリックしている個々のユーザーを知っていますか?

はい。Advanced Tracking をオンにすると、Currents 経由で送信される[SMS ターゲット変更フィルタ]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting#trigger-messages-as-users-receive-sms) またはSMS クリックイベント(`users.messages.sms.ShortLinkClick`) を利用して、URL をクリックしたユーザーを再ターゲットできます。

#### 短縮される前に、URL にUTM パラメータを追加できますか?

はい任意の静的URL パラメータを追加できます。 

#### 短縮されたURLはどのくらい有効ですか?

URL登録(初回送信など)から1年間 

#### リンク短縮は、ディープリンクまたはユニバーサルリンクと連携しますか?

リンクの短縮は、_http://_ または_https://_ で始まる静的URL を短縮します。ただし、生成されたユニバーサルリンク(Branch やAppsflyer などのプロバイダからの) をさらに短縮することはお勧めしません。これにより、これらのツールの属性やリダイレクトが壊れる可能性があるためです。

### カスタムドメイン

#### 委任されたドメインは複数のサブスクリプショングループ間で共有できますか?
はい。1 つのドメインを複数のサブスクリプショングループで使用できます。これを行うには、関連付けるサブスクリプショングループごとにドメインを選択します。

#### 委任されたドメインは複数のワークスペース間で共有できますか?
はい。ドメインは複数のワークスペースのサブスクリプショングループに関連付けることができます。ワークスペースが同じ会社内に含まれていることを前提とします。

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

