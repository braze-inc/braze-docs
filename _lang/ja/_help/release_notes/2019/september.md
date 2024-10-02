---
nav_title: 9月
page_order: 4
noindex: true
page_type: update
description: "この記事には2019年9月のリリースノートが含まれている。"
---

# 2019年9月

## OneLogin内のBrazeアプリ

顧客は、[OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)内でBrazeを検索して選択するだけで、SPまたはIdP Initiatedログインができるようになる。これは、顧客がOneLogin内にカスタムアプリケーションを追加する必要がないことを意味する。その結果、SAML SSOを立ち上げてから見られるようになった、属性のような特定の設定が事前に入力されるはずである。

## ロクト・カレンダー・パートナーシップ

[Rokt Calendarは]({{site.baseurl}}/partners/additional_channels/calendar/rokt_calendar/)、Brazeの顧客に、パーソナライズされたマーケティングイニシアティブを調整し、パーソナライズされたコンテンツをエンドユーザーのカレンダーに拡張する機能を提供する。こうして、エンドユーザーにとってよりシームレスな体験となり、顧客のサービスに対する愛着がさらに深まる。顧客は...

- Brazeプラットフォーム経由でカレンダーに招待状を送り、「日付を保存」してコミュニケーションを広げる。
- イベントの内容が変更された場合、既存の招待を更新する。

## パスキット・パートナーシップ

[Passkit]({{site.baseurl}}/partners/additional_channels/mobile_wallet/passkit/)で、Braze 顧客 sは携帯ウォレットへのカスタマーエンゲージメントを拡張することができます。彼らは、Brazeの強力なセグメンテーションを使いながら、財布キャンペーンをパーソナライズし、プッシュやアプリ内メッセージなどのチャネルと並行してオーケストレーションすることができる。

## メッセージング・エンドポイント経由でディスパッチID値を返す

メッセージの`dispatch_id` は、以下のメッセージング・エンドポイントのレスポンスに含まれる：
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-via-api-triggered-delivery)
- [`/campaigns/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-immediately-via-api-only)
- [`/messages/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/canvases/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#canvas)
- [`/canvases/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#api-triggered-canvases)

こうすることで、トランザクショナル・メッセージングを利用する顧客は、カレントを介してコールバックをトレースすることができる。

## キャンバスの変更履歴

自分のアカウントで誰がキャンバスに取り組んでいるのか、もっと詳しく知りたいと思ったことはないだろうか？もう不思議ではない！キャンバスの変更履歴にアクセスできるようになった。

![Canvas Changelogs]({% image_buster /assets/img/canvas-changelog1.png %})
![Canvas Changelogs]({% image_buster /assets/img/canvas-changelog2.png %})
