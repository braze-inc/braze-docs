---
nav_title: 現在のアドビ
article_title: 現在のアドビ
alias: /partners/adobe_for_currents/
description: "このリファレンス記事では、Braze Currents とAdobe のパートナーシップについて説明します。これは、ブランドがAdobe データ(カスタム属性とセグメント)をリアルタイムでBraze に接続してマッピングできるカスタマーデータプラットフォームです。"
page_type: partner
tool: Currents
search_tag: Partner
---

# 現在のアドビ

> [Adobe](https://www.adobe.com/)は、ブランドが自身のAdobeデータ(カスタム属性とセグメント)をリアルタイムでブレーズに接続してマッピングできる顧客データプラットフォームです。

ブレーズとAdobe の統合により、2 つのシステム間の情報の流れをシームレスに制御できます。[Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) を使用すると、データをAdobe に接続して、グローススタック全体で実行可能にすることもできます。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Currents | Adobeにデータを書き戻すには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)を設定する必要があります。 |
| Adobe Experience プラットフォームアカウント | このパートナーシップを活用するには、[Adobe Experience Platform アカウント](https://experience.adobe.com/#/platform/home) が必要です。 |
| コネクタの作成許可 | この統合を使用するには、ストリーミングソース接続を作成するための権限が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:Adobe でのXDM スキーマの作成

1. Adobe Experience Platform で、**Schemas** > select **Create schema** > select **Experience Event** > select **Next**.<br><br>!["Braze Currents Walk-Through"というスキーマのAdobe Schemas ページ。][1]<br><br>
2. スキーマの名前と説明を入力します。 
3. **Composition**パネルで、スキーマ属性を設定します。
- **フィールドグループ**で、**Add**を選択し、**Braze Currents User Event**フィールドグループを追加します。
- [**保存**] を選択します。

スキーマの詳細については、[スキーマの作成](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui)に関するAdobeのドキュメントを参照してください。

### ステップ 2: Adobe Experience プラットフォームへのブレーズの接続

1. Adobe Experience Platform で、**Sources** > **Catalog** > **Marketing automation** に移動します。
2. ろう付け電流は**データ追加**を選択します。
3. [Currentsサンプルファイル](https://github.com/Appboy/currents-examples/blob/master/sample-data/Adobe/adobe_examples.json)をアップロードします。<br><br>![Adobe "データページとクォートを追加します。][2]<br><br>
4. ファイルがアップロードされたら、データセットとマッピング先のスキーマに関する情報など、データフローの詳細を指定します。 
    - ブレーズ電流ソースを初めて接続する場合は、新しいデータセットを作成し、[ステップ1](#step-1-create-an-xdm-schema-in-adobe) で作成したスキーマを使用するようにします。 
    - これが初めてでない場合は、Braze スキーマを参照する既存のデータセットを使用します。
5. データのマッピングを設定し、問題を解決します。
    - スキーマのルートレベルで、`id` のマッピングを`to _braze.appID` から`_id` に変更します。
    - `properties.is_amp` が`_braze.messaging.email.isAMP` にマッピングされていることを確認します。
    - `time` および`timestamp` マッピングを削除し、追加アイコン> **計算フィールド** を選択して、**time * 1000** と入力します。[**保存**] を選択します。
    - 新しいソースフィールドの横にある**ターゲットフィールド**をマッピングし、スキーマのルートレベルの**timestamp**にマッピングします。<br><br>![Adobe "Add data" page with mappings.][3]<br><br>
6. **Validate**を選択して、問題を解決したことを確認します。

{% alert important %}
ろう付けのタイムスタンプは秒単位で表されます。Adobe Experience Platform でタイムスタンプを正確に反映するには、計算項目がミリ秒単位である必要があります。秒をミリ秒に変換するには、**time * 1000** 計算を使用します。
{% endalert %}

{: start="7"}
7. **Next**を選択し、データフローの詳細を確認してから、**Finish**を選択します。<br><br>![Adobe "Add data"マッピングエラーのないページ。][4]

### ステップ 3:認証情報の収集

次のクレジットを収集してBraze に入力すると、Braze はAdobe Experience Platform にデータを送信できます。

| フィールド         |説明                          |
|---------------|-------------------------------------|
| クライアント ID     | Adobe Experience Platform ソースに関連付けられたクライアントID。 |
| クライアントシークレット | Adobe Experience Platform ソースに関連付けられたクライアントシークレット。 |
| テナント ID     | Adobe Experience Platform ソースに関連付けられたテナントID。 |
| サンドボックス名  | Adobe Experience Platform ソースに関連付けられたサンドボックス。   |
| データフロー ID   | Adobe Experience Platform ソースに関連付けられたデータフローID。   |
| ストリーミングエンドポイント  | Adobe Experience Platform ソースに関連付けられたストリーミングエンドポイント。Braze はこれを自動的にバッチストリーミングエンドポイントに変換します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ステップ4:データソースにデータをストリーミングするための現在の設定

1. ブレーズで、**Partner Integrations**> **Data Export**に移動し、**Create New Current**を選択します。 
2. 次の情報を入力します。
    - コネクタの名前
    - コネクタに関する通知の連絡先情報
    - [ステップ3](#step-3-gather-credentials) の認証情報
3. 受信するイベントを選択します。
4. 必要に応じて、フィールドの除外または変換を設定します。
5. **Launch Current**を選択します。

[1]: {% image_buster /assets/img/adobe/currents_sources.png %}
[2]: {% image_buster /assets/img/adobe/currents_add_data.png %}
[3]: {% image_buster /assets/img/adobe/currents_mapping.png %}
[4]: {% image_buster /assets/img/adobe/currents_no_errors.png %}