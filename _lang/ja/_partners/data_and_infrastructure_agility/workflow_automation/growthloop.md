---
nav_title: GrowthLoop
article_title: GrowthLoop
description: "この参考記事では、BrazeとGrowthLoopの提携について概説している。GrowthLoopは、データウェアハウスから顧客データを直接セグメント化してBrazeに送信できるプラットフォームである。"
alias: /partners/growthloop/
page_type: partner
search_tag: Partner

---

# GrowthLoop

> [GrowthLoop](https://growthloop.com/) は、クラウドデータウェアハウスから Braze やその他のチャネルへの顧客データを活性化するマーケティング チームを支援します。クラウドデータウェアハウスからマーケティングプログラムを自動化、スケーリング、測定し、データを一元管理します。

_この統合は GrowthLoop によって管理されます。_

## 統合について

Braze と GrowthLoop の統合により、データウェアハウスから直接顧客データをセグメント化して Braze に送信できます。これにより、ユーザーは Braze の豊富な機能セットを、信頼できる唯一の情報源とともに最適化できます。顧客セグメンテーションとアクティベーションのためのマーケティング活動を合理化し、Brazeに送られたターゲットキャンペーンのセグメンテーション、ローンチ、テスト、結果測定にかかる時間を短縮する。

## 前提条件 

| 必要条件 | 説明 |
| ----------- | ----------- |
| GrowthLoop の growth アカウントまたは enterprise アカウント | このパートナーシップを利用するには、GrowthLoopのアカウントが必要である。 |
| Braze Rest APIキー | すべての権限を持つBraze REST APIキー。<br><br>これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | REST エンドポイントのURL。エンドポイントはインスタンスの [Braze URL][2] に応じて異なります。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## ユースケース

データウェアハウスから Braze に顧客リストを送信し、ワンクリックでメールキャンペーンやプッシュ通知キャンペーンのターゲット設定を行い、常に同期を維持できます。

- サインアップアクティベーションに基づくEメール - サインアップフローから外れたユーザーをアクティブユーザーに変えるためにEメールを送る。
- あらゆるユーザーの行動に基づいたメール - "カートに入れる "など、ユーザーの行動に基づいてメールを送信する。
- 解約顧客へのEメール - オファーのあるEメールで、解約した顧客に再度アプローチする。

## 統合

### GrowthLoopでBraze接続を設定する

GrowthLoop の Segmentation Platform にサインインしたら、左サイドバーの [**Destinations**] タブを開き、右上の [**New Destination**] をクリックします。

Braze が見つかるまでスクロールし、[**Add Braze**] をクリックします。

宛先への接続を設定するポップアップが表示される。

- **Destination name**:これは宛先に指定される名前であり、今後アプリでこの宛先はこの名前で参照されます。
- **同期周波数**：[Daily] または [Hourly] を選択します。これにより、GrowthLoop がオーディエンスを Braze にエクスポートする頻度が制御されます。
- **APIキー**：要件で作成した、必要な権限を持つ API キー。
- **API URL**:要件で定義されているURL

[**Create**] をクリックします。これで最初のオーディエンスを Braze にエクスポートできます。GrowthLoop でオーディエンスを作成するには、[オーディエンスの作成](https://www.growthloop.com/help-center-articles/create-an-audience)を参照してください。

### エクスポート後の作業

顧客リストがエクスポートされたら、GrowthLoop が15分ごとに最新の顧客リストを生成して Braze に送信します。

同時に GrowthLoop は、条件を満たさなくなったユーザーをオーディエンスから削除し、新たに条件を満たしているユーザーをオーディエンスに追加します。 

Braze はユーザーを照合し、ユーザーが GrowthLoop のオーディエンスに含まれていることを示すフラグを作成します。

Braze でキャンペーンを作成するときに、その GrowthLoop オーディエンスから顧客を選択できます。 

## トラブルシューティング

追加情報やサポートについては、GrowthLoopチーム（solutions@growthloop.com ）までお問い合わせを。


[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
