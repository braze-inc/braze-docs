---
nav_title: Digioh
article_title: Digioh
description: "このリファレンス記事では、Braze と Digioh のパートナーシップについて説明します。Digioh は、Braze のキャンペーンを通じて真のエンゲージメントを促進するポップアップ、フォーム、アンケート、およにコミュニケーションユーザー設定センターを簡単に作成できるアンケートプラットフォームです。"
alias: /partners/digioh/
page_type: partner
search_tag: Partner

---

# Digioh

> [Digioh](https://www.digioh.com/) は、リストの拡大、ファーストパーティデータの取り込み、Braze キャンペーンでのデータの利用を支援します。

_この統合は Digioh によって管理されます。_

## 統合について

Braze と Digioh の統合により、柔軟性の高いドラッグ＆ドロップビルダーを使用して、顧客とつながるためのブランドらしさのあるフォーム、ポップアップ、パフォーマンスセンター、ランディングページ、アンケートを作成できます。Digioh は、統合の設定を支援し、最初のキャンペーンを作成、設計、開始できるようにします。

![「Digioh で柔軟製の高いメールとコミュニケーションのユーザー設定センターを作成する」][5]{: style="border:0"}

## 前提条件

| 必要条件 | 説明 |
|---|---|
|Digioh アカウント | このパートナーシップを活用するには、[Digioh アカウント](https://www.digioh.com/)が必要です。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze API`/users/track/` エンドポイント | `/users/track/` の詳細が付加された REST エンドポイント URL。エンドポイントは[インスタンスの Braze URL][6] に応じて異なります。<br><br>たとえば、REST API エンドポイントが `https://rest.iad-01.braze.com` の場合、`/users/track/` エンドポイントは `https://rest.iad-01.braze.com/users/track/` になります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 統合 

Digioh を統合するには、まず Braze コネクターを設定する必要があります。完了したら、ライトボックス（ウィジェット）に統合を適用する必要がある。[Digioh](https://help.digioh.com/knowledgebase/digioh-integration-basics/) にアクセスして、統合の基礎についてお読みください。

### ステップ1:Digioh 統合を作成する 

Digioh で [**Integration**] タブをクリックし、次に[**New Integration**] ボタンをクリックします。[**Integration**] ドロップダウンから [**Braze**] を選択し、統合に名前を付けます。 

!["ドロップダウンから正しい統合を選択する"][2]{: style="max-width:50%;"}

次に、Braze REST API キーとBraze API `/users/track/` エンドポイントを入力します。 

最後に、マップフィールドセクションを使って、Eメールと名前以外のカスタムフィールドをマッピングする。次のコード・スニペットは、ペイロードの例を示している。完了したら、[**Create Integration**] を選択します。

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

### ステップ2:Digioh ライトボックスを作成する

Digioh [デザインエディター](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/)を使用してライトボックス (ウィジェット) を作成します。<br>
デザインエディターを活用する方法のギャラリーを見ることに興味がある？Digioh の[テーマギャラリー](https://www.digioh.com/theme-gallery)をご覧ください。

### ステップ3:統合を適用する

この統合を Digioh [ライトボックス](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/)に適用するには、[**Boxes**] ページに移動し、[**Integrations**] カラムの [**Add**] または [**Edit**] リンクを選択します。これはエディターの**Integration**セクションからも追加できる。

![「統合をライトボックスに追加する][3]{: style="max-width:90%"}

ここで [**Add Integration**] を選択し、目的の統合を選択して [**Save**] をクリックします。Digioh は、キャプチャしたリードをリアルタイムで Braze に渡します。


[2]: {% image_buster /assets/img/digioh/2.png %}
[3]: {% image_buster /assets/img/digioh/3.png %}
[4]: {% image_buster /assets/img/digioh/4.png %}
[5]: {% image_buster /assets/img/digioh/pref_pop_examples.png %}
[6]: {{site.baseurl}}/api/basics/#endpoints