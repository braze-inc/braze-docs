---
nav_title: GrowthLoop
article_title: GrowthLoop
description: "この参考記事では、BrazeとGrowthLoopの提携について概説している。GrowthLoopは、データウェアハウスから顧客データを直接セグメント化してBrazeに送信できるプラットフォームである。"
alias: /partners/growthloop/
page_type: partner
search_tag: Partner

---

# GrowthLoop

> [GrowthLoopは](https://growthloop.com/)、マーケティングチームが顧客データをクラウドデータウェアハウスからBrazeやその他のチャネルに有効化するのを支援する。クラウドデータウェアハウスからマーケティングプログラムを自動化、拡張、測定し、データを一元管理する。

BrazeとGrowthLoopの統合により、データウェアハウスから直接顧客データをセグメント化し、Brazeに送信することができる。顧客セグメンテーションとアクティベーションのためのマーケティング活動を合理化し、Brazeに送られたターゲットキャンペーンのセグメンテーション、ローンチ、テスト、結果測定にかかる時間を短縮する。

## 前提条件 

| 必要条件 | 説明 |
| ----------- | ----------- |
| GrowthLoop グロースアカウントまたはエンタープライズアカウント | このパートナーシップを利用するには、GrowthLoopのアカウントが必要である。 |
| Braze Rest APIキー | すべての権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは、[インスタンスのBraze URLに][2]依存する。|
{: .reset-td-br-1 .reset-td-br-2} 

## ユースケース

データウェアハウスからBrazeに顧客リストを送信し、Eメールやプッシュ通知キャンペーンをワンクリックでターゲティング。

- サインアップアクティベーションに基づくEメール - サインアップフローから外れたユーザーをアクティブユーザーに変えるためにEメールを送る。
- あらゆるユーザーの行動に基づいたメール - "カートに入れる "など、ユーザーの行動に基づいてメールを送信する。
- 解約顧客へのEメール - オファーのあるEメールで、解約した顧客に再度アプローチする。

## 統合

### GrowthLoopでBraze接続を設定する

GrowthLoop の Segmentation Platform にサインインしたら、左サイドバーの**Destinations**タブを開き、右上の**New Destination**をクリックする。

Brazeが見つかるまでスクロールし、**Add Brazeを**クリックする。

宛先への接続を設定するポップアップが表示される。

- **デスティネーション名である**：これが、今後アプリ内で目的地がどのように命名され、どのように参照されるかである。
- **同期周波数**：GrowthLoopがオーディエンスをBrazeにエクスポートする頻度をコントロールする。
- **APIキー**：要件で作成したAPIキーに必要な権限を付与する。
- **APIのURL**：要件で定義されているURL

**Createを**クリックすると、最初のオーディエンスをBrazeにエクスポートできる！GrowthLoopでオーディエンスを作成するには、[Create an Audienceを](https://www.growthloop.com/help-center-articles/create-an-audience)参照のこと。

### ポストの輸出

顧客リストがエクスポートされると、15分毎にGrowthLoopが顧客リストの更新版を生成し、Brazeに送信する。

同時に、GrowthLoopは、もはや適格でないユーザーをオーディエンスから削除し、新たに適格なユーザーをオーディエンスに追加する。 

Brazeはユーザーをマッチングし、GrowthLoopのオーディエンスの一員であることを示すフラグを作成する。

Brazeでキャンペーンを作成する際、GrowthLoopのオーディエンスから顧客を選択することができる。 

## トラブルシューティング

追加情報やサポートについては、GrowthLoopチーム（solutions@growthloop.com ）までお問い合わせを。

[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
