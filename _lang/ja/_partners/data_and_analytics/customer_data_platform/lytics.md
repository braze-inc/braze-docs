---
nav_title: Lytics
article_title: Lytics
description: "このリファレンス記事では、Braze と Lytics の統合について説明します。Lytics は、マーケター、アナリスト、技術者向けのエンタープライズ顧客データプラットフォームです。この統合により、ブランドは Lytics のデータを Braze に直接同期およびマッピングできます。"
alias: /partners/lytics/
page_type: partner
search_tag: Partner
---

# Lytics

> [Lytics](https://www.lytics.com/) は、顧客中心の次世代ビジネスに最適な顧客データプラットフォーム (CDP) です。Lytics Decision Engine、Conductor、Cloud Connectの各ソリューションは、マーケティング担当者とデータチームに、プライバシーに準拠した方法で、アイデンティティ解決、オーケストレーション、キャンペーン最適化をリアルタイムで実行する機会を提供する。

_この統合は Lytics によって管理されます。_

## 統合について

Braze と Lytics の統合により、顧客を一元的に把握できるため、強力なパーソナライゼーションが可能になり、ネクストベストアクションオーケストレーションと意思決定を使用して最適化されたキャンペーンを推進できます。

この統合により、ブランドは以下のことができるようになります。

- Lytics から直接 Braze にオーディエンスをエクスポートする
- BrazeのキャンペーンやCanvasesのイベントをリアルタイムでLyticsに送信し、パーソナライズされたキャンペーンやリッチなユーザープロファイルを構築する。

## ユースケース

Braze を Lytics に接続して、メール、SMS、プッシュアクティビティを[インポート](#importing-data-from-braze-to-lytics)し、Lytics のユーザープロファイルを充実させます。Braze と Lytics を併用することで、Lytics のクロスチャネル、行動主導型のオーディエンスを[エクスポート](#integration)し、ファーストパーティデータを使用して高度にパーソナライズされた Braze カスタマージャーニーを構築することもできます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Lyticsアカウント | この統合を活用するには、Lytics アカウントが必要です。 |
| Lyticsアカウント番号 | ウェブフックのエンドポイントURLを設定するには、Lyticsのアカウント番号が必要である。 |
| Lytics APIトークン | データマネージャー権限を持つLytics REST APIトークン。<br><br> これは、Lyticsダッシュボード内の**「アカウント設定コンソール**」＞「**アクセストークン**」＞「**新しいトークンの作成**」から作成できる。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| ブレイズインスタンス | お客様の [Braze インスタンス]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)。不明な場合は、Brazeのオンボーディング・マネージャーに問い合わせること。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

このセクションでは、LyticsのデータをBrazeにエクスポートする方法を説明する。

### ステップ1:認証を作成する

Lyticsで、ナビゲーションバーの [**Data**] コンソール内の [**Authorization**] ダッシュボードに移動します。[**Create New Authorization**] を選択し、**Braze** を検索して選択します。

表示される**Configure Authorization**プロンプトで、ラベルと説明を入力し、REST APIキーとBrazeインスタンスを入力する。完了したら [**Complete**] を選択します。

![]({% image_buster /assets/img/lytics/braze_authorization.png %}){: style="max-width:80%;"}

### ステップ 2:新しい仕事を作る

Lytics で、ナビゲーションバーの [**Data**] コンソール内の[**Jobs**] ダッシュボードに移動します。[**Create New Job**] を選択し、**Braze** を検索して選択します。 表示される [**Select Job Type**] プロンプトで [**Export Audience**] を選択します。

![]({% image_buster /assets/img/lytics/braze_jobtype.png %}){: style="max-width:80%;"}

次に、**Select Authorization**オプションの中から認証を選択する。

![]({% image_buster /assets/img/lytics/braze_jobauth.png %}){: style="max-width:80%;"}

### ステップ 3:ジョブを設定する

**Configure Job**プロンプト内で、ラベルとオプションの説明を入力する。次に [**Braze External User ID Field**] の入力から、Braze 外部ユーザー ID (`braze_id`) を含む Lytics のフィールドを選択します。次は最も重要なステップです。Braze にエクスポートするオーディエンスを選択します。

![]({% image_buster /assets/img/lytics/braze_job.png %}){: style="max-width:80%;"}

最後に、"**Existing Users**"チェックボックスで好ましいオプションを選択する。このボックスをオンのままにすると、選択した Lytics オーディエンスにすでに存在しているユーザーが追加されます。オフにすると、ワークフロー開始後にオーディエンスに追加される時点またはオーディエンスから外される時点でのみ、ユーザーが Braze にエクスポートされます。

{% alert note %}
このボックスをチェックすることで、選択したオーディエンスのすべての既存ユーザーがBrazeにプッシュされる。Brazeの料金にデータポイントが含まれている場合は、データポイントの使用量を適宜モニターすること。
{% endalert %}

完了したら [**完了**] をクリックしてエクスポートを開始し、保存します。

![]({% image_buster /assets/img/lytics/braze_backfill.png %}){: style="max-width:80%;"}

エクスポートジョブの設定が完了したら、Lytics はネイティブ統合を介して、選択されたオーディエンスを Braze に送信します。以下は、Braze に送信されるオーディエンスの JSON 構造を示すサンプルオーディエンスです。

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

オーディエンスのエクスポートに含まれ、Braze にまだ存在していない `external_id` に対し、Braze で新しいユーザーが作成されます。 

## BrazeからLyticsにデータをインポートする

Braze から Lytics へのオーディエンスデータのインポートは、以下の方法で行うことができます。

- [Webhook を使用する](#using-webhooks)
- [CSVファイルから](#from-a-csv-file)

### Webhook を使用する

#### ステップ1:Lytics API トークンを作成する

アカウント名を選択して左下にある Lytics Account Menu に移動し、ドロップダウンメニューから [**Access Tokens**] を選択します。次に [**Create API Token**] を選択します。

![]({% image_buster /assets/img/lytics/create_token.png %}){: style="max-width:80%;"}

名前、オプションの説明、トークンの有効期限を入力する。次に API 権限の [**Data Manager**] スコープをオンに切り替え、[**Generate Token**] をクリックします。トークンをコピーし、安全な場所に保管する。

![]({% image_buster /assets/img/lytics/data_manager.png %}){: style="max-width:80%;"}

#### ステップ 2:LyticsのウェブフックURLを設定する

Lytics Webhook URL は、Braze から Lytics API にメッセージを送信するために Braze によって使用されます。このメッセージは、Lytics でキャンペーンをパーソナライズする場合や、Lytics の顧客プロファイルを充実させる場合に使用できます。以下の2つのパラメータは、LyticsウェブフックURL内に追加する必要がある：

- Lyticsアカウント番号
- Lytics APIトークン

ウェブフックのURLを以下のように設定する：

```
https://api.lytics.io/c/<ACCOUNT-NUMBER>/braze_users?key=<LYTICS-API-TOKEN>
```

`<ACCOUNT-NUMBER>` をアカウント番号に置き換え、`<LYTICS-API-TOKEN>` を Lytics API トークンに置き換えます。

#### ステップ3:BrazeでWebhookを作成する 

Braze で新しい [Webhook キャンペーン]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)を作成します。**Webhook URL**フィールドにLyticsのWebhook URLを追加する。

リクエストタイプ (HTTP `POST` メソッド) を定義し、残りの Webhook の詳細を設定したら、Webhook をテストおよびデプロイできます。以下は、BrazeでWebhookを設定した後のPOSTリクエスト本文のサンプルである：

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

#### ステップ1:認証を作成する

Lyticsで、ナビゲーションバーの [**Data**] コンソール内の [**Authorization**] ダッシュボードに移動します。[**Create New Authorization**] を選択し、[**Custom Integrations**] を検索して選択します。

ビジネス要件とセキュリティ要件に基づいて、使用する SFTP 認証タイプを選択します。SFTP経由でLyticsにファイルをインポートする場合、以下の認証タイプがサポートされている：

- クライアントSFTPサーバー認証
- PGP秘密鍵によるクライアントSFTPサーバー認証
- Lytics マネージド SFTP サーバー認証

公開鍵SFTP認証は、SFTPエクスポート専用である。

![]({% image_buster /assets/img/lytics/authorization_method.png %}){: style="max-width:80%;"}

表示された**Configure Authorization**プロンプトで、ラベルと説明を入力し、残りの構成要件を完了する。完了したら [**Complete**] をクリックします。

#### ステップ2:セグメントデータをCSVにエクスポートする

Braze で [**オーディエンス**] > [**セグメント**] に移動します。エクスポートするセグメントを見つけ、[<i class="fas fa-gear" aria-label="設定"></i>] を選択し、次に [**ユーザーデータを CSV 形式でエクスポート**] を選択します。1つのセグメントで最大50万ユーザーをエクスポートできます。詳細については、「[CSV へのセグメントデータのエクスポート]({{site.baseurl}}/user_guide/data/export_braze_data/segment_data_to_csv/)」を参照してください。

#### ステップ3:CSVインポートジョブを設定する

Lytics で、ナビゲーションバーの [**Data**] コンソール内の[**Jobs**] ダッシュボードに移動します。[**Create New Job**] を選択し、[**Custom Integrations**] を検索して選択します。

次にジョブタイプを選択します。Braze の CSV ファイルを Lytics にインポートするには、ジョブタイプとして [**Import CSV**] を選択します。

![]({% image_buster /assets/img/lytics/configure_job.png %}){: style="max-width:80%;"}

最後に、仕事のラベルと任意の説明を入力し、その他の必要な詳細を設定する。[**Complete**] をクリックして、ジョブを開始し、保存します。







