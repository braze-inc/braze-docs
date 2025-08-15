---
nav_title: Currents の Azure
article_title: Currents の Azure
alias: /partners/adobe_for_currents/
description: "このリファレンス記事では、Braze Currents と Adobe のパートナーシップについて説明します。Adobe は顧客データプラットフォームであり、ブランドはリアルタイムで Braze に接続し、Adobe データ (カスタム属性とセグメント) を Braze にマッピングできます。"
page_type: partner
tool: Currents
search_tag: Partner
---

# Currents の Azure

> [Adobe](https://www.adobe.com/) は、ブランドが自身の Adobe データ (カスタム属性とセグメント) をリアルタイムで Braze に接続してマッピングできる顧客データプラットフォームです。

Braze と Adobe の統合により、2つのシステム間の情報の流れをシームレスにコントロールすることができます。[Currents]({{site.baseurl}}/user_guide/data/braze_currents/) では、データを Adobe に接続し、グローススタック全体で実用的なデータにすることもできます。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Currents | Adobe にデータを再度エクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) を設定する必要があります。 |
| Adobe Experience プラットフォームアカウント | このパートナーシップを活用するには、[Adobe Experience プラットフォームアカウント](https://experience.adobe.com/#/platform/home)が必要です。 |
| コネクタの作成許可 | この統合を使用するには、ストリーミングソース接続を作成する権限が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:Adobe でのXDM スキーマの作成

1. Adobe Experience プラットフォームで、 [**スキーマ**] > [**スキーマの作成**] > [**Experience Event**] > [**次へ**] の順に選択します。<br><br>!["Braze Currents Walk-Through"というスキーマのAdobe Schemas ページ。][1]<br><br>
2. スキーマの名前と説明を入力します。 
3. **Composition**パネルで、スキーマ属性を設定します。
- **フィールドグループ**で、**Add**を選択し、**Braze Currents User Event**フィールドグループを追加します。
- [**保存**] を選択します。

スキーマの詳細については、[スキーマの作成](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui)に関するAdobeのドキュメントを参照してください。

### ステップ2: Adobe Experience プラットフォームへの Braze の接続

1. Adobe Experience Platform で、**Sources** > **Catalog** > **Marketing automation** に移動します。
2. Braze 電流は**データ追加**を選択します。
3. [Braze Currents サンプルファイル](https://github.com/Appboy/currents-examples/blob/master/sample-data/Adobe/adobe_examples.json)をアップロードします。<br><br>![Adobe「データの追加ページ」][2]<br><br>
4. ファイルがアップロードされたら、データセットとマッピング先のスキーマに関する情報など、データフローの詳細を指定します。 
    - Braze 電流ソースを初めて接続する場合は、新しいデータセットを作成し、[ステップ1](#step-1-create-an-xdm-schema-in-adobe) で作成したスキーマを使用するようにします。 
    - これが初めてでない場合は、Braze スキーマを参照する既存のデータセットを使用します。
5. データのマッピングを設定し、問題を解決します。
    - スキーマのルートレベルで、`id` のマッピングを`to _braze.appID` から`_id` に変更します。
    - `properties.is_amp` が`_braze.messaging.email.isAMP` にマッピングされていることを確認します。
    - `time`と`timestamp`のマッピングを削除し、追加アイコン > [**計算されたフィールドの追加**] を選択して、「**time\*1000**」と入力します。[**保存**] を選択します。
    - 新しいソースフィールドの横にある**ターゲットフィールド**をマッピングし、スキーマのルートレベルの**timestamp**にマッピングします。<br><br>![マッピングを含む Adobe の「データの追加」ページ。][3]<br><br>
6. **Validate**を選択して、問題を解決したことを確認します。

{% alert important %}
Braze のタイムスタンプは秒単位で表されます。Adobe Experience Platform でタイムスタンプを正確に反映するには、計算項目がミリ秒単位である必要があります。秒をミリ秒に変換するには、**time * 1000** 計算を使用します。
{% endalert %}

{: start="7"}
7. **Next**を選択し、データフローの詳細を確認してから、**Finish**を選択します。<br><br>![マッピングエラーのない Adobe の「データの追加」ページ。][4]

### ステップ 3:認証情報の収集

次の認証情報を収集して Braze に入力すると、Braze が Adobe Experience Platform にデータを送信できるようになります。

| フィールド         |説明                          |
|---------------|-------------------------------------|
| クライアント ID     | Adobe Experience Platform ソースに関連付けられたクライアントID。 |
| クライアントシークレット | Adobe Experience Platform ソースに関連付けられたクライアントシークレット。 |
| テナント ID     | Adobe Experience Platform ソースに関連付けられたテナントID。 |
| サンドボックス名  | Adobe Experience Platform ソースに関連付けられたサンドボックス。   |
| データフロー ID   | Adobe Experience Platform ソースに関連付けられたデータフローID。   |
| ストリーミングエンドポイント  | Adobe Experience Platform ソースに関連付けられたストリーミングエンドポイント。Braze はこれを自動的にバッチストリーミングエンドポイントに変換します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ステップ 4: データソースにデータをストリーミングするための現在の設定

1. Braze で、[**パートナー連携**] > [**データエクスポート**] に移動し、[**Current の新規作成**] を選択します。 
2. 次の情報を入力します。
    - コネクタの名前
    - コネクタに関する通知の連絡先情報
    - [ステップ3](#step-3-gather-credentials) の認証情報
3. 受信するイベントを選択します。
4. 必要に応じて、フィールドの除外または変換を設定します。
5. [**Currents を起動**] を選択します。

[1]: {% image_buster /assets/img/adobe/currents_sources.png %}
[2]: {% image_buster /assets/img/adobe/currents_add_data.png %}
[3]: {% image_buster /assets/img/adobe/currents_mapping.png %}
[4]: {% image_buster /assets/img/adobe/currents_no_errors.png %}