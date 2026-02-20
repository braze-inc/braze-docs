---
nav_title: Snowplow
article_title: Snowplow
description: "この参考記事では、BrazeとデータインフラプラットフォームであるSnowplowのパートナーシップについて概説しており、SnowplowのEvent Forwardingを使用して、SnowplowのイベントをリアルタイムでBrazeに転送することができる。"
alias: /partners/snowplow/
page_type: partner
search_tag: Partner

---

# Snowplow

> [Snowplowは](https://snowplowanalytics.com)、リッチで高品質な低遅延データ収集のためのスケーラブルなプラットフォームである。Snowplowは、企業向けに高品質で完全な行動データを収集するように設計されている。

_この統合は Snowplow によって管理されます。_

## 統合について

BrazeとSnowplowの統合により、Snowplowのイベント転送ソリューションを使って、SnowplowのイベントをリアルタイムでBrazeに転送することができる。この統合により、柔軟性とコントロールを提供しながら、Brazeにイベントを送信することができる。具体的にはこうだ：
- Brazeに送信する前に、イベントにフィルターをかけて変換する。
- SnowplowのイベントデータをBrazeのユーザー属性、カスタムイベント、購入にマッピング。
- 転送を選択するまで、すべてのデータをプライベート・クラウドに保持する。
- 既存のSnowplowクラウドアカウント内にソリューションを自分で展開する。 

Snowplowの[イベント転送は](https://docs.snowplow.io/docs/destinations/forwarding-events/)、Snowplowの顧客が利用できる有料のアドオン機能である。このアドオンなしでBrazeにイベントを転送するには、Snowplowの[Googleタグマネージャーサーバーサイド](https://docs.snowplow.io/docs/destinations/forwarding-events/google-tag-manager-server-side/)統合を使用する。

Snowplowの豊富な顧客行動データを活用して、Brazeで強力な顧客中心インタラクションを促進し、パーソナライズされたメッセージをリアルタイムで配信する。

## 前提条件

| 必要条件             | 説明                                                                                                                                                                                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Snowplow パイプライン       | スノープラウのパイプラインを稼働させる必要がある。                                                                                                                                                                                                                                          |
| 除雪コンソールへのアクセス | イベントフォワーダーを設定するには、Snowplow Consoleにアクセスする必要がある。                                                                                                                                                                                                                                |
| Braze REST API キー      | 以下の権限を持つBraze REST APIキー：`users.track` `users.alias.new`,`users.identify`,`users.export.ids`,`users.merge`,`users.external_ids.rename`, および`users.alias.update` 。<br><br> ダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze REST エンドポイント     | [あなたのRESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントはインスタンスの Braze URL に応じて異なります。                                                                                                                                     |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

### パーソナライズされた、アクションベースの配信
Snowplow がデフォルトで収集する多数のリッチなイベントのいずれかを使用するか、カスタムイベントを定義して、ビジネスに適したより細かなカスタマージャーニーを形成します。Snowplowの豊富な行動データを活用して顧客ファネルを設計し、マーケティングおよび製品チームの価値を引き出し、Brazeを通じてコンバージョンと製品使用を最大化するのに役立てます。

### ダイナミックなセグメンテーション
Snowplowの高品質な行動データに基づいてBrazeでダイナミックなオーディエンスを作成する:ユーザーが製品、アプリ、またはWebサイトでアクションを実行すると、Snowplowが収集するリアルタイムの行動データを活用して、Brazeの関連セグメントにユーザーを自動的に追加または削除できます。

## 統合

### ステップ1:Snowplow Consoleで送信先を設定する

イベント・フォワーダーを作成する：

1. Snowplow Consoleで、**Destinationsに**移動し、**Create new destinationを**選択する。
2. 接続を設定する際、接続タイプに**Brazeを**選択する。
3. Braze APIキーとREST APIエンドポイントを入力する。
4. 接続を保存する。

### ステップ2:イベント・フォワーダーを設定する

フォワーダーを設定する際、転送するSnowplowイベントを選択し、Brazeオブジェクトタイプにマッピングすることができる：

1. **[ユーザー属性]({{site.baseurl}}/api/objects_filters/user_attributes_object)**:ユーザープロファイルデータとカスタムユーザープロパティを更新する。
2. **[カスタムイベント]({{site.baseurl}}/api/objects_filters/event_object)**:ユーザーのアクションや行動を送信する。
3. **[購入品目]({{site.baseurl}}/api/objects_filters/purchase_object)**:商品詳細の取引データを送信する。

オブジェクトタイプごとに、フィールドマッピングを設定して、SnowplowイベントデータをBrazeフィールドにマッピングする方法を指定できる。詳細なセットアップ手順とフィールドマッピング設定については、Snowplowの[Creating forwardersドキュメントを](https://docs.snowplow.io/docs/destinations/forwarding-events/creating-forwarders/)参照のこと。

### ステップ 3:統合を検証する

Brazeアカウントで以下のページをチェックし、イベントがBrazeに届いていることを確認する：

1. **クエリー・ビルダー**Brazeで、「**Analytics**>**Query Builder**」に移動する。スノープラウから転送されたデータをプレビューするために、以下のテーブルにクエリーを書くことができる：`USER_BEHAVIORS_CUSTOMEVENT_SHARED` と`USERS_BEHAVIORS_PURCHASE_SHARED` 。
2. **API利用ダッシュボード**：Brazeの**「設定**」>「**APIと識別子**」で、API使用量の時系列チャートを見ることができる。Snowplowが使用しているAPIキーに特化してフィルターをかけ、成功と失敗の両方を見ることができる。

## カスタムプロパティを送信する

標準フィールド以外にもカスタムプロパティを送信できる。その構造は、どのBrazeオブジェクトタイプを使用しているかによって異なる：

- **ユーザー属性で**ある：トップレベルフィールドとして追加する（例えば、`subscription_tier` 、`loyalty_points` ）。
- **イベントのプロパティ**：`properties` オブジェクトの下にネストする（例えば、`properties.plan_type`,`properties.feature_flag` ）。
- **プロパティを購入する**：`properties` オブジェクトの下にネストする（例えば、`properties.color`,`properties.size` ）。

スペースを含むプロパティ名には、ブラケット表記を使用する（例えば、`["account type"]` や`properties["campaign source"]` ）。

サポートされるデータタイプ、プロパティ命名要件、ペイロードサイズ制限の詳細については、[イベントオブジェクトのドキュメントを]({{site.baseurl}}/api/objects_filters/event_object)参照のこと。

## 制限事項

**レート制限：**Brazeは、Track Users APIのレート制限を3秒ごとに3,000APIコールとしている。Snowplowはイベントフォワーダーのバッチ処理をサポートしていないため、このAPIレート制限はイベントレート制限としても機能する。入力スループットが3秒間に3,000イベントを超えると、レイテンシーが増大する可能性がある。
