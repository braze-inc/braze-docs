---
nav_title: デジオー
article_title: デジオー
description: "この参考記事では、BrazeとDigiohのパートナーシップについて概説している。Digiohは、Brazeのキャンペーンを通じて真のエンゲージメントを促進するポップアップ、フォーム、アンケート、コミュニケーションプレファレンスセンターを簡単に作成できるアンケートプラットフォームである。"
alias: /partners/digioh/
page_type: partner
search_tag: Partner

---

# デジオー

> [Digiohは](https://www.digioh.com/)、リストを増やし、ファーストパーティデータを取得し、そのデータをBrazeのキャンペーンに活用することを支援する。

BrazeとDigiohの統合により、柔軟なドラッグ＆ドロップビルダーを使用して、顧客とつながるオンブランドのフォーム、ポップアップ、パフォーマンスセンター、ランディングページ、アンケートを作成することができる。Digiohは、統合セットアップを支援し、あなたのために最初のキャンペーンを構築し、設計し、起動する。

!["Digiohで柔軟な電子メールとコミュニケーションのプリファレンスセンターを作る"][5]{: style="border:0"}

## 前提条件

| 必要条件 | 説明 |
|---|---|
|デジオーアカウント | このパートナーシップを利用するには、[デジオのアカウントが](https://www.digioh.com/)必要である。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze API`/users/track/` エンドポイント | あなたのRESTエンドポイントのURLに、`/users/track/` の詳細が付加されている。エンドポイントは、\[インスタンスのBraze URL][6] に依存する。<br><br>例えば、REST API のエンドポイントが`https://rest.iad-01.braze.com` の場合、`/users/track/` のエンドポイントは`https://rest.iad-01.braze.com/users/track/` となる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合 

Digiohを統合するには、まずBrazeコネクタを設定する必要がある。完了したら、ライトボックス（ウィジェット）に統合を適用する必要がある。統合の基本についてもっと読むには、[Digiohを](https://help.digioh.com/knowledgebase/digioh-integration-basics/)ご覧いただきたい。

### ステップ1:デジオーの統合を作成する 

Digiohで、**Integrations**タブをクリックし、**New Integration**ボタンをクリックする。**Integration（統合）**ドロップダウンから**Brazeを**選択し、統合に名前を付ける。 

!["ドロップダウンから正しい統合を選択する"][2]{: style="max-width:50%;"}

次に、Braze REST APIキーとBraze API`/users/track/` エンドポイントを入力する。 

最後に、マップフィールドセクションを使って、Eメールと名前以外のカスタムフィールドをマッピングする。次のコード・スニペットは、ペイロードの例を示している。完了したら、**Create Integrationを**選択する。

```json
{
    "attributes" : [
         {
           "external_id": "[EMAIL_MD5]",
           "email" : "[EMAIL]"
         }
     ]
}
```

### ステップ2:デジオのライトボックスを作成する

デジオの[デザインエディターを使って](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/)ライトボックス（ウィジェット）を作る。<br>
デザインエディターを活用する方法のギャラリーを見ることに興味がある？デジオの[テーマギャラリーを](https://www.digioh.com/theme-gallery)見る。

### ステップ3:統合を適用する

この統合をDigioh[ライト](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/)ボックスに適用するには、**Boxes**ページに移動し、**Integrations**列の**Add**または**Edit**リンクを選択する。これはエディターの**Integration**セクションからも追加できる。

![「統合をライトボックスに追加する][3]{: style="max-width:90%"}

ここで、**Add Integrationを**選択し、希望のインテグレーションを選択し、**Save**する。DigiohはリアルタイムでBrazeにリードを渡す。

[2]: {% image_buster /assets/img/digioh/2.png %}
[3]: {% image_buster /assets/img/digioh/3.png %}
[4]: {% image_buster /assets/img/digioh/4.png %}
[5]: {% image_buster /assets/img/digioh/pref_pop_examples.png %}
[6]: {{site.baseurl}}/api/basics/#endpoints