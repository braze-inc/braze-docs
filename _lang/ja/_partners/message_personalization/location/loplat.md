---
nav_title: loplat
article_title: loplat
description:"この参考記事では、Brazeとオフラインの位置情報マーケティングプラットフォームであるloplatとの提携について概説している。"位置情報のコンテキストを追加することで、プロキシミティマーケティングキャンペーンを実施することができる。
alias: /partners/loplat/
page_type: partner
search_tag:Partner

---

# ロプラット

> [Loplatは][1]オフラインの位置情報プラットフォームをリードしている。loplat SDKを使って、来店者数をスマートに増やし、店頭での購買を促すマーケティングキャンペーンを実施しよう。キャンペーン終了後も、フットフォール分析を通じて店舗のパフォーマンスを測定することができる。

Brazeとloplatの統合により、loplatの位置情報サービス（店舗POIとカスタムジオフェンス）を使って、ジオコンテクストに応じたマーケティングキャンペーンをトリガーしたり、オフラインセグメンテーションを使ってカスタムイベントを作成したりすることができる。ユーザーがloplat Xで設定したターゲットロケーションにアクセスすると、キャンペーンとロケーション情報が即座にBrazeに送信される。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| ロプラXアカウント | この統合を利用するには、loplat Xアカウントが必要である。<br><br>[support@loplat.com][3]にメールでloplat Xアカウントをリクエストする。 |
| loplat SDK | loplat SDKはユーザー' store visits, processes location events, and distinguishes whether users are staying at a place or moving. You can use loplat SDK to analyze your store'の足跡を認識し、ユーザーが店舗に入店した際にプッシュメッセージを送信する。<br><br>SDKはAndroidとiOSでのみ利用可能である。 |
| Braze REST API キー | 以下の権限を持つBraze REST APIキー：<br>- `users.track`<br>- `campaigns.trigger.send`<br>- `campaigns.list`<br>- `canvas.trigger.send`<br>- `canvas.list`<br><br>これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

loplatが提供するカスタムイベントの位置情報は、キャンペーンで次のようなユースケースを実現するために使用することができる：

- [免税プロモーション警報][2]
    - 空港の搭乗ゲート付近にいるユーザーに免税店の割引クーポンを送る。
- 電気自動車（EV）充電ステーション位置のプッシュ
    - EV充電ステーションの周辺にジオフェンスを設定し、ユーザーがステーションの近くに来たら通知して充電を促す。

## 統合

### ステップ1:SDKを統合する

loplat[\- Brazeインテグレーション][4]ドキュメントに記載されているステップを使用して、アプリにloplat SDKとBraze SDKを統合する。

### ステップ2:Brazeとloplat Xのダッシュボードを同期し、キャンペーンを作成する。

ダッシュボードで新しいAPIキーを作成する。APIキーをコピーし、loplat Xダッシュボードの**設定 > API設定に**貼り付ける。詳細は[loplat Xユーザーガイドを](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e?pvs=25)参照のこと。

#### API トリガー配信

1. **APIトリガー配信**で送信するBrazeキャンペーンまたはキャンバスを作成し、キャンペーンIDをコピーする。
2. すべてのステップが完了したら、Brazeでキャンペーンを開始する。
3. loplat Xの[ユーザーガイドに従って][5]キャンペーンを作成する。
4. **キャンペーンメッセージ設定の**下にBrazeキャンペーンIDを貼り付け、キャンペーンを開始する。

![][7]

#### アクションベースの配信

この統合により、ジオフェンス情報、地域、ブランド名、店舗名を送信することで、ロケーション条件を適用することができる。さらに、作成したカスタムイベントでセグメンテーションを追加したり、コンバージョンを割り当てることもできる。
1. loplat X[ユーザーガイドに従って][6]loplat Xキャンペーンを作成する。
2. **キャンペーンメッセージ**設定でカスタムイベントを追加し、キャンペーンを開始する。
3. Brazeダッシュボードにアクセスし、**アクションベース配信で**送信するキャンペーンまたはキャンバスを作成する。
4. loplat Xで作成したカスタムイベントを選択し、ロケーショントリガーアクションを設定する。

![][8]

[1]: https://www.loplat.com/
[2]: https://www.loplat.com/loplat-x#usecase
[3]: mailto:support@loplat.com
[4]: https://developers.loplat.com/braze/
[5]: https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#2ed232c885014f19b1870b9fca4230fb
[6]: https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#f898aa55ef74440aba76dd9a0e3e7598
[7]: {% image_buster /assets/img/loplat/loplat_api_triggered_delivery.png %}
[8]: {% image_buster /assets/img/loplat/loplat_action_based_delivery.png %}