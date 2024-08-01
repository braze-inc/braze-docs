---
nav_title: 9月
page_order: 4
noindex: true
page_type: update
description: "この記事には2019年9月のリリースノートが含まれている。"
---

# 2019年9月

## OneLogin内のBrazeアプリ

顧客は、[OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)内でBrazeを検索して選択するだけで、サービスプロバイダーやIdP Initiatedログインができるようになる。これは、顧客がOneLogin内にカスタムアプリケーションを追加する必要がないことを意味する。その結果、SAML SSOを立ち上げてから見られるようになった、属性などの特定の設定が事前に入力されるはずである。

## Roktカレンダー・パートナーシップ

[Rokt Calendarは]({{site.baseurl}}/partners/additional_channels/calendar/rokt_calendar/)、パーソナライズされたマーケティングイニシアティブを調整し、パーソナライズされたコンテンツをエンドユーザーのカレンダーに拡張する機能をBraze顧客に提供する。こうして、エンドユーザーにとってよりシームレスなエクスペリエンスとなり、カスタマーエクスペリエンスのスティッキネスをさらに発展させることができる。顧客は...

- Brazeプラットフォームを通じてカレンダーに招待状を送り、「日付を保存」してコミュニケーションを広げる。
- イベントの内容が変更された場合、既存の招待を更新する。

## パスキット・パートナーシップ

[Passkitによって]({{site.baseurl}}/partners/additional_channels/mobile_wallet/passkit/)、Brazeの顧客はカスタマーエンゲージメントをモバイルウォレットに拡大することができる。Brazeの強力なセグメンテーションを使いながらパーソナライズされたウォレットキャンペーンを行い、プッシュやアプリ内メッセージなどのチャネルと並行してオーケストレーションを行うことができる。

## メッセージングエンドポイント経由でディスパッチID値を返す

メッセージの`dispatch_id` は、以下のメッセージングエンドポイントのレスポンスに含まれる：
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-via-api-triggered-delivery)
- [`/campaigns/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-immediately-via-api-only)
- [`/messages/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/canvases/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#canvas)
- [`/canvases/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#api-triggered-canvases)

こうすることで、トランザクショナル・メッセージングを利用する顧客は、カレントを経由してコールバックをトレースすることができる。

## キャンバスの変更履歴

自分のアカウントで誰がキャンバスに取り組んでいるのか、もっと詳しく知りたいと思ったことはないだろうか？もう不思議ではない！キャンバスの変更履歴にアクセスできるようになった。

![キャンバス変更履歴]({% image_buster /assets/img/canvas-changelog1.png %})
![キャンバス変更履歴]({% image_buster /assets/img/canvas-changelog2.png %})
