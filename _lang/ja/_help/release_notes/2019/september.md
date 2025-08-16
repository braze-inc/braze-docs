---
nav_title: 9月
page_order: 4
noindex: true
page_type: update
description: "この記事には2019年9月のリリースノートが含まれている。"
---

# 2019年9月

## OneLogin内のBrazeアプリ

[OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/) 内で Braze を検索し、サービスプロバイダーまたは IdP 開始ログイン用に選択できるようになります。これは、顧客がOneLogin内にカスタムアプリケーションを追加する必要がないことを意味する。その結果、SAML SSO の起動後に表示された属性などの特定の設定が事前入力されます。

## ロクト・カレンダー・パートナーシップ

[Rokt Calendarは]({{site.baseurl}}/partners/home/)、Brazeの顧客に、パーソナライズされたマーケティングイニシアティブを調整し、パーソナライズされたコンテンツをエンドユーザーのカレンダーに拡張する機能を提供する。これにより、エンドユーザーのエクスペリエンスがよりシームレスになり、お客様のサービスのスティッキネスがさらに向上します。以下を実行できるようになります。

- Brazeプラットフォーム経由でカレンダーに招待状を送り、「日付を保存」してコミュニケーションを広げる。
- イベントの内容が変更された場合、既存の招待を更新する。

## Passkit パートナーシップ

[Passkit]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/mobile_wallet/passkit/) により、Braze のお客様はカスタマーエンゲージメントをモバイルウォレットに拡張できます。Braze の強力なセグメンテーションを利用しながらウォレットキャンペーンをパーソナライズし、プッシュやアプリ内メッセージなどのチャネルとのオーケストレーションを実現できます。

## メッセージングエンドポイント経由でのディスパッチ ID 値の返却

メッセージの`dispatch_id` は、以下のメッセージング・エンドポイントのレスポンスに含まれる：
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-via-api-triggered-delivery)
- [`/campaigns/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-immediately-via-api-only)
- [`/messages/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/canvases/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#canvas)
- [`/canvases/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#api-triggered-canvases)

これにより、トランザクションメッセージングを使用するお客様は、Currents を介してコールバックをトレースできます。

## キャンバスの変更履歴

自分のアカウントで誰がキャンバスに取り組んでいるのか、もっと詳しく知りたいと思ったことはないだろうか？もうその必要はありません。キャンバス変更ログにアクセスできるようになりました。

![キャンバス変更ログ]({% image_buster /assets/img/canvas-changelog1.png %})
![キャンバス変更ログ]({% image_buster /assets/img/canvas-changelog2.png %})
