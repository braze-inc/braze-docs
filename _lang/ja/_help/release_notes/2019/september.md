---
nav_title: 9 月
page_order: 4
noindex: true
page_type: update
description: "この記事には、2019 年 9 月のリリース ノートが含まれています。"
---

# 2019年9月発売

## OneLogin内のBrazeアプリ

お客様は、 [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/) 内でBrazeを検索して選択するだけで、SPまたはIdP Initiatedログインを行うことができます。つまり、お客様はOneLogin内にカスタムアプリケーションを追加する必要がありません。その結果、SAML SSOの起動以降に登場した属性などの特定の設定が事前に入力されます。

## Roktカレンダーのパートナーシップ

[Rokt Calendar]({{site.baseurl}}/partners/additional_channels/calendar/rokt_calendar/) は、Brazeの顧客向けにパーソナライズされたマーケティングイニシアチブを調整し、パーソナライズされたコンテンツをエンドユーザーのカレンダーに拡張する機能を提供します。したがって、エンドユーザーにとってよりシームレスなエクスペリエンスを実現し、お客様のサービスとの粘着性をさらに高めます。お客様は次のことができるようになります...

- Brazeプラットフォームを介してカレンダーの招待状を送信して「日付を保存」し、コミュニケーションを拡張します
- イベントの内容が変更された場合は、既存の招待を更新します。

## Passkitとのパートナーシップ

[Passkit]({{site.baseurl}}/partners/additional_channels/mobile_wallet/passkit/)を利用することで、Brazeの顧客は顧客エンゲージメントをモバイルウォレットに拡大することができます。Brazeの強力なセグメンテーションを使用しながら、ウォレットキャンペーンをパーソナライズし、プッシュやアプリ内メッセージなどのチャネルと連携して調整することができます。

## メッセージング エンドポイント経由で返されるディスパッチ ID 値

メッセージは `dispatch_id` 、次のメッセージング エンドポイント応答に含まれます。
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-via-api-triggered-delivery)
- [`/campaigns/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-immediately-via-api-only)
- [`/messages/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/canvases/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#canvas)
- [`/canvases/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#api-triggered-canvases)

これにより、トランザクション メッセージングを使用するお客様は、Currents を通じてコールを追跡できます。

## キャンバスの変更履歴

アカウントで誰がキャンバスで作業しているかの詳細について、さらに疑問に思いましたか?もう不思議に思う必要はありません!キャンバスの変更ログにアクセスできるようになりました。

![Canvas Changelogs]({% image_buster /assets/img/canvas-changelog1.png %})
![Canvas Changelogs]({% image_buster /assets/img/canvas-changelog2.png %})
