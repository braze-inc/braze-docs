---
nav_title: Digioh
article_title:デジオー
description:この記事では、BrazeとDigiohのパートナーシップについて説明します。Digiohは、ポップアップ、フォーム、アンケート、コミュニケーションの好みセンターを簡単に作成できる調査プラットフォームで、Brazeキャンペーンを通じて実際のエンゲージメントを促進します。
alias: /partners/digioh/
page_type: partner
search_tag:Partner

---

# デジオー

> [Digioh](https://www.digioh.com/) は、リストの拡大、ファーストパーティデータの取得、およびBrazeキャンペーンでのデータ活用を支援します。

BrazeとDigiohの統合により、柔軟なドラッグアンドドロップビルダーを使用して、ブランドに合ったフォーム、ポップアップ、パフォーマンスセンター、ランディングページ、およびアンケートを作成し、顧客とつながることができます。Digiohは、統合の設定を支援し、最初のキャンペーンを構築、設計、開始するのを手伝います。

![「Digiohで柔軟なメールおよびコミュニケーションの設定センターを作成する」][5]{: style="border:0"}

## 前提条件

| 要件 | 説明 |
|---|---|
|ディジオアカウント | このパートナーシップを利用するには、[Digiohアカウント](https://www.digioh.com/)が必要です。 |
| Braze REST API キー | `users.track` の権限を持つ Braze REST API キー。<br><br> これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze API `/users/track/` エンドポイント | あなたのRESTエンドポイントURLに`/users/track/`の詳細が追加されています。エンドポイントは、インスタンスのBraze URL][6]に依存します。<br><br>例えば、REST APIエンドポイントが`https://rest.iad-01.braze.com`の場合、`/users/track/`エンドポイントは`https://rest.iad-01.braze.com/users/track/`になります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合 

Digiohを統合するには、まずBrazeコネクタを構成する必要があります。完了したら、統合をライトボックス（ウィジェット）に適用する必要があります。[Digioh](https://help.digioh.com/knowledgebase/digioh-integration-basics/)について詳しく読むには、[Digioh](https://help.digioh.com/knowledgebase/digioh-integration-basics/)を訪れてください。

### ステップ1:Digioh統合を作成する 

Digiohで、**統合**タブをクリックし、**新しい統合**ボタンをクリックします。**ブラゼ** ドロップダウンから **インテグレーション** を選択し、インテグレーションに名前を付けます。 

![ドロップダウンから正しい統合を選択してください][2]{: style="max-width:50%;"}

次に、Braze REST APIキーとBraze API `/users/track/`エンドポイントを入力します。 

最後に、メールと名前以外のカスタムフィールドをマップするには、マップフィールドセクションを使用します。次のコードスニペットは、ペイロードの例を示しています。完了したら、**統合の作成**を選択します。

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

### ステップ2:Digiohのライトボックスを作成する

Digioh [デザインエディタ](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/) を使用して、ライトボックス（ウィジェット）を作成します。<br>
デザインエディターを活用する方法のギャラリーに興味がありますか？Digiohの[テーマギャラリー](https://www.digioh.com/theme-gallery)を訪問してください。

### ステップ3:統合を適用

この統合をDigioh [ライトボックス](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/)に適用するには、**ボックス**ページに移動し、**統合**列の**追加**または**編集**リンクを選択します。これは、エディターの**統合**セクションから追加することもできます。

![「ライトボックスに統合を追加する」][3]{: style="max-width:90%"}

ここで、**統合を追加**を選択し、希望する統合を選択して、**保存**します。Digiohは、キャプチャしたリードをリアルタイムでBrazeに渡します。

[2]: {% image_buster /assets/img/digioh/2.png %}
[3]: {% image_buster /assets/img/digioh/3.png %}
[4]: {% image_buster /assets/img/digioh/4.png %}
[5]: {% image_buster /assets/img/digioh/pref_pop_examples.png %}
[6]: {{site.baseurl}}/api/basics/#endpoints