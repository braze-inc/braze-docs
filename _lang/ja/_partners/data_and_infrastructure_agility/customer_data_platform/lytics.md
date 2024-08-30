---
nav_title: Lytics
article_title: Lytics
description: "この参考記事は、BrazeとLyticsの統合をカバーしている。Lyticsは、マーケティング担当者、アナリスト、技術者のための企業向け顧客データプラットフォームである。この統合により、ブランドはLyticsのデータをBrazeに直接同期し、マッピングすることができる。"
alias: /partners/lytics/
page_type: partner
search_tag: Partner
---

# Lytics

> [Lyticsは][1]、顧客中心の次世代ビジネスに選ばれる顧客データプラットフォーム（CDP）である。Lytics Decision Engine、Conductor、Cloud Connectの各ソリューションは、マーケティング担当者とデータチームに、プライバシーに準拠した方法で、アイデンティティ解決、オーケストレーション、キャンペーン最適化をリアルタイムで実行する機会を提供する。

BrazeとLyticsの統合は、顧客の統一されたビューを提供し、強力なパーソナライゼーションを可能にし、次善のアクションオーケストレーションと決定を用いて最適化されたキャンペーンを推進する。

この統合により、ブランドは以下のことが可能になる：

- Lyticsから直接Brazeにオーディエンスをエクスポートする
- BrazeのキャンペーンやCanvasesのイベントをリアルタイムでLyticsに送信し、パーソナライズされたキャンペーンやリッチなユーザープロファイルを構築する。

## ユースケース

BrazeをLyticsに接続して、電子メール、SMS、プッシュのアクティビティを[インポート](#importing-data-from-braze-to-lytics)し、Lyticsのユーザープロファイルを充実させる。BrazeとLyticsを一緒に使えば、Lyticsのクロスチャネル、行動主導型オーディエンスを[エクスポートして](#integration)、ファーストパーティデータを使って高度にパーソナライズされたBrazeカスタマージャーニーを構築することもできる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Lyticsアカウント | この統合を利用するには、Lyticsのアカウントが必要である。 |
| Lyticsアカウント番号 | ウェブフックのエンドポイントURLを設定するには、Lyticsのアカウント番号が必要である。 |
| Lytics APIトークン | データマネージャー権限を持つLytics REST APIトークン。<br><br> これは、Lyticsダッシュボード内の**「アカウント設定コンソール**」＞「**アクセストークン**」＞「**新しいトークンの作成**」から作成できる。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| ブレイズインスタンス | [ブレイズのインスタンス]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)だ。不明な場合は、Brazeのオンボーディング・マネージャーに問い合わせること。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

このセクションでは、LyticsのデータをBrazeにエクスポートする方法を説明する。

### ステップ1:認可を作成する

Lyticsで、ナビゲーションバーの**データ・**コンソール内の**認可**ダッシュボードに移動する。**Create New Authorizationを**選択し、**Brazeを**検索して選択する。

表示される**Configure Authorization**プロンプトで、ラベルと説明を入力し、REST APIキーとBrazeインスタンスを入力する。終了したら**Completeを**選択する。

![][2]{: style="max-width:80%;"}

### ステップ2:新しい仕事を作る

Lyticsで、ナビゲーションバーの**データ**コンソール内の**ジョブダッシュボードに**移動する。**Create New Jobを**選択し、**Brazeを**検索して選択する。 表示される**Select Job Type**プロンプトで、**Export Audienceを**選択する。

![][3]{: style="max-width:80%;"}

次に、**Select Authorization**オプションの中から認証を選択する。

![][4]{: style="max-width:80%;"}

### ステップ3:ジョブを設定する

**Configure Job**プロンプト内で、ラベルとオプションの説明を入力する。次に、**Braze External User ID Field**入力から、Braze外部ユーザーID（`braze_id` ）を含むLyticsのフィールドを選択する。次のステップが最も重要で、Brazeにエクスポートするオーディエンスを選択する。

![][5]{: style="max-width:80%;"}

最後に、"**Existing Users**"チェックボックスで好ましいオプションを選択する。このボックスにチェックを入れたままにしておくと、選択したLyticsオーディエンスにすでに存在しているユーザーを追加する。チェックを外すと、ワークフロー開始後にオーディエンスに入室または退室するときのみ、ユーザーがBrazeにエクスポートされる。

{% alert note %}
このボックスをチェックすることで、選択したオーディエンスのすべての既存ユーザーがBrazeにプッシュされる。この結果、最初の同期では、視聴者1人につきユーザー1人分のデータポイントが発生することになる。
{% endalert %}

**完了**したら**Completeを**クリックしてエクスポートを開始し、保存する。

![][6]{: style="max-width:80%;"}

エクスポートジョブが設定されると、Lyticsはネイティブ統合を通じて、選択されたオーディエンスをBrazeに送信する。以下は、Brazeに送信されたオーディエンスのJSON構造を示すサンプルオーディエンスである。

```json
{
    "lytics_to_braze_audience": [{
            "external_id": "ABC124ID",
            "lytics_segments": {
                "add": [
                    "lytics_all",
                    "lytics_new"
                ]
            }
        },
        {
            "external_id": "XYZ234ID",
            "lytics_segments": {
                "add": [
                    "lytics_known"
                ],
                "remove": [
                    "lytics_new"
                ]
            }
        }
    ]
}
```

オーディエンスエクスポートに含まれる、Brazeにまだ存在しない`external_id` 、Brazeに新しいユーザーが作成される。 

## BrazeからLyticsにデータをインポートする

BrazeからLyticsへのオーディエンスデータのインポートは、以下の方法で行うことができる：

- [ウェブフックを使う](#using-webhooks)
- [CSVファイルから](#from-a-csv-file)

### ウェブフックを使う

#### ステップ1:Lytics API トークンを作成する

左下にあるLyticsアカウントメニューに移動し、アカウント名を選択し、ドロップダウンメニューから**Access Tokensを**選択する。次に、**Create API Tokenを**選択する。

![][7]{: style="max-width:80%;"}

名前、オプションの説明、トークンの有効期限を入力する。次に、**Data Managerの**スコープをAPI Permissionsに切り替え、**Generate Tokenを**クリックする。トークンをコピーし、安全な場所に保管する。

![][8]{: style="max-width:80%;"}

#### ステップ2:LyticsのウェブフックURLを設定する

Lytics webhook URLは、BrazeからLytics APIにメッセージを送信するためにBrazeによって使用される。このメッセージは、Lyticsでキャンペーンをパーソナライズしたり、Lyticsの顧客プロファイルを充実させたりするために使用できる。以下の2つのパラメータは、LyticsウェブフックURL内に追加する必要がある：

- Lyticsアカウント番号
- Lytics APIトークン

ウェブフックのURLを以下のように設定する：

```
https://api.lytics.io/c/<ACCOUNT-NUMBER>/braze_users?key=<LYTICS-API-TOKEN>
```

`<ACCOUNT-NUMBER>` をあなたのアカウント番号に、`<LYTICS-API-TOKEN>` をあなたの Lytics API トークンに置き換える。

#### ステップ3:BrazeでWebhookを作成する 

Brazeで、新しい[Webhookキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成する。**Webhook URL**フィールドにLyticsのWebhook URLを追加する。

リクエストタイプ（HTTP`POST` メソッド）を定義し、残りのウェブフックの詳細を設定したら、ウェブフックのテストとデプロイの準備は完了だ。以下は、BrazeでWebhookを設定した後のPOSTリクエスト本文のサンプルである：

```json
{
  "city": "AnyTown",
  "country": "United States",
  "first_name": "John",
  "gender": "male",
  "language": "English",
  "last_name": "Smith",
  "date_of_birth": "19820101",
  "phone_number": "5551231234",
  "time_zone": "GMT+7",
  "twitter_handle": "johnsmith",
  "email": "john.smith@email.com",
  "braze_id": "xxxxxx" 
}
```

### CSVファイルから

このセクションでは、BrazeのユーザーデータをセグメントからLyticsにインポートする方法を説明する。

#### ステップ1:認可を作成する

Lyticsで、ナビゲーションバーの**データ・**コンソール内の**認可**ダッシュボードに移動する。**Create New Authorizationを**選択し、**Custom Integrationsを**検索して選択する。

ビジネス要件とセキュリティ要件に基づいて、SFTP認証の優先タイプを選択する。SFTP経由でLyticsにファイルをインポートする場合、以下の認証タイプがサポートされている：

- クライアントSFTPサーバー認証
- PGP秘密鍵によるクライアントSFTPサーバー認証
- Lytics マネージド SFTP サーバー認証

公開鍵SFTP認証は、SFTPエクスポート専用である。

![][9]{: style="max-width:80%;"}

表示された**Configure Authorization**プロンプトで、ラベルと説明を入力し、残りの構成要件を完了する。完了したら**Completeを**クリックする。

#### ステップ2:セグメントデータをCSVにエクスポートする

Brazeで、**Audience**>**Segmentsに**移動する。エクスポートしたいセグメントを探し、以下を選択する。 <i class="fas fa-gear" aria-label="設定"></i>を選択し、次に**CSV Export User Dataを**選択する。セグメントで最大50万ユーザーをエクスポートできる。詳しくは、[セグメントデータをCSVにエクスポートするを]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv)参照のこと。

#### ステップ3:CSVインポートジョブを設定する

Lyticsで、ナビゲーションバーの**データ**コンソール内の**ジョブダッシュボードに**移動する。**Create New Jobを**選択し、**Custom Integrationsを**検索して選択する。

次に、ジョブ・タイプを選択する。BrazeのCSVファイルをLyticsにインポートするには、ジョブタイプとして**CSVインポートを**選択する。

![][10]{: style="max-width:80%;"}

最後に、仕事のラベルと任意の説明を入力し、その他の必要な詳細を設定する。**Completeを**クリックしてジョブを開始し、保存する。

[1]: https://www.lytics.com/
[2]: {% image_buster /assets/img/lytics/braze_authorization.png %}
[3]: {% image_buster /assets/img/lytics/braze_jobtype.png %}
[4]: {% image_buster /assets/img/lytics/braze_jobauth.png %}
[5]: {% image_buster /assets/img/lytics/braze_job.png %}
[6]: {% image_buster /assets/img/lytics/braze_backfill.png %}
[7]: {% image_buster /assets/img/lytics/create_token.png %}
[8]: {% image_buster /assets/img/lytics/data_manager.png %}
[9]: {% image_buster /assets/img/lytics/authorization_method.png %}
[10]: {% image_buster /assets/img/lytics/configure_job.png %}





