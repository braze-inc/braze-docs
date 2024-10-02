---
nav_title: Redpoint
article_title: Redpoint 
description: "BrazeインテグレーションへのRedpointにより、ファーストパーティデータを使用してBraze ユーザープロファイルをオンボードし、拡張することができます。"
alias: /partners/redpoint/
page_type: partner
search_tag: Redpoint
---

# Redpoint

> [Redpoint][2] は、マーケター s に完全に統合されたキャンペーン オーケストレーション プラットフォームを提供するテクノロジプラットフォームです。Redpoint のセグメンテーション、スケジュール、およびオートメーション機能を活用して、CDP データがBraze にインポートされる方法と時期をコントロールします。

BrazeとRedpointインテグレーションを使用すると、RedpointのCDPデータに基づいてBraze Segmentsを作成できます。Redpoint には、Braze にデータを渡すための2 つの方法があります。 

1. **Braze Onboarding and Upsert** モード:"Upserts" RedpointからBrazeへのユーザープロファイル。これは、変更されたユーザーレコードをオンボーディングまたは更新するために使用されることを意図しています。 
2. ** Braze 追加** モード:そのユーザーがBrazeにすでに存在する場合は、ユーザープロファイルをアップデートします。 

エクスポートテンプレートと送信チャネルを設定します。

{% alert note %}
"Upsert"は単語"更新"と"insert."の組合せです。データベーステーブルに新しいレコードが存在しない場合は、そのレコードをデータベーステーブルに挿入するか、存在する場合はレコードを更新する場合に使用されます。基本的に、upsert は、特定のレコードがデータベースに存在するかどうかを確認します。レコードが存在する場合は更新d、存在しない場合は新しいレコードが挿入されます。
{% endalert %}

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| Braze REST API キー | `users.track` 権限を持つBraze REST API キー。<br><br>これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
| Braze REST エンドポイント | [Your REST エンドポイント URL][1].エンドポイントは、インスタンスのBraze URL によって異なります。 |
| Redpoint データマネジメントアーティファクト | Brazeインテグレーションは、Redpoint データマネジメントアーティファクトの集合によってサポートされます。[ Redpoint サポート][3] に連絡して、Redpoint データマネジメントのアーティファクトをリクエストします。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、**デベロッパコンソール**> **API設定**でAPI キーを作成できます。
{% endalert %}

## RedpointCDPカスタム属性

次のRedpoint カスタム属性s をBraze ユーザープロファイルに追加できます。

| フィールド               | 説明                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `rpi_cdp_attributes` | Redpoint CDP プロファイル 属性の対象                                                                                  |
| `rpi_audience_outputs`| ユーザーがRedpoint 送信デリバリーBraze チャネルで実行されるオーディエンスアウトプットタグs の配列         |
| `rpi_offers`         | Redpoint 送信デリバリーBraze チャネルでユーザーがターゲットとなるオファータグの配列                   |
| `rpi_contact_ids`    | ユーザーがRedpoint 送信デリバリーBraze チャネルで実行されるオファー履歴の連絡先ID の配列     |
| `rpi_channel_exec_ids`| Redpoint 送信デリバリーBraze チャネルの実行でユーザーのターゲットとなるチャネル実行ID の配列       |
{: .reset-td-br-1 .reset-td-br-2}

![][4]{: style="max-width:75%;"}

## 統合

### ステップ1:テンプレートの設定

#### ステップ 1a: Braze オンボーディングおよびアップサートテンプレートの作成

Redpointインターアクション(RPI) で、新しいエクスポートテンプレートを作成し、** Braze Onboarding and Upsert** という名前を付けます。このテンプレートでは、Redpoint CDP とBraze ユーザープロファイル の間のコアm アプリを定義し、Braze のユーザープロファイルs に追加する追加のカスタム属性s も定義します。

Redpoint CDP 属性sを**属性**列にドラッグアンドドロップします。それぞれの**ヘッダー行値**を対応するBraze\[ユーザー 属性][17]]に設定します。 

以下のテーブルに、Redpoint CDP 属性と対応するBraze 属性s を示します。

| Redpointアトリビュート | ヘッダ行値 |
|--------------------|------------------|
| PID                | `external_id`    |
| フィッスト名          | `first_name`     |
| 姓          | `last_name`      |
| プライマリメール      | `email`          |
| 主要国    | `country`        |
| DOB                | `dob`            |
| 性別             | `gender`         |
| プライマリ市区町村       | `home_city`      |
| プライマリ電話機      | `phone`          |
{: .reset-td-br-1 .reset-td-br-2}

**Offer History**テーブルの**Offer Name**属性を追加します。最後に、Braze にマージするカスタムRedpoint 属性を追加します。たとえば、次のオンボーディングとアップサートのテンプレートでは、学歴、収入、および配偶者のステータスを追加属性としています。

![][7]{: style="max-width:75%;"}

#### ステップ 1b: Braze追加テンプレートの作成

**Braze アプリ end** という名前のアプリ end-only オペレーションの2 番目のエクスポートテンプレートを作成します。

このテンプレートには2 つの属性s のみを設定します。**PID**の場合は、**Header Row Value**を`external_id`に設定します。**Output Name**の場合、**Header Row**を`output_name`に設定します。

![`external_id` のエクスポートテンプレートの例と属性s を出力します。][8]{: style="max-width:75%;"}

#### ステップ1c:日付形式の設定

両方のエクスポートテンプレートs で、**Options** タブに移動し、**Date Format** を**カスタム書式** の値に設定します。形式を**yyyy-MM-dd**に設定します。

![日付形式がyyyy-MM-dd に設定されているオプションタブ。][16]{: style="max-width:75%;"}

### ステップ2:送信チャネルの作成s

RPIで、2つの新しいチャネルsを作成します。両方のチャネルsを**Outbound Delivery**に設定します。1 つのチャネル** Braze Onboarding and Upsert** と、もう1 つの** Braze Append** に名前を付けます。

![][9]{: style="max-width:75%;"}

{% alert note %}
CDPレコードを最初にオンボーディングしてBrazeした後、最初のオンボーディングの同期以降に変更されたレコードのみを選択するように、Braze オンボーディングおよびアップサートチャネルを使用する後続のRedpointインターアクションワークフローが設計されているかどうかを確認します。
{% endalert %}

### ステップ3:チャネルの設定s

#### ステップ3a:テンプレートおよびエクスポートパス形式の設定

チャネル s **Configuration** 画面の**General** タブに移動します。エクスポートテンプレートをそれぞれのチャネルに設定します。 

次に、共有ネットワーク、ファイル転送プロトコル、または外部コンテンツプロバイダーの場所を指す両方のチャネルで、Redpoint Inter アクション とRedpoint データマネジメントの両方がアクセスできる**エクスポートパス形式** を定義します。 

![][10]{: style="max-width:75%;"}

両方のチャネルs のエクスポートディレクトリ形式は同一であり、`\\[Channel]\\[Offer]\\[Workflow ID]` で終わる必要があります。

![][11]{: style="max-width:50%;"}

#### ステップ3b:実行後の設定

Channels **Configuration** 画面の**Post Execution** タブに移動します。 

チャネル実行後に**実行後**にチェックを入れ、サービスURLを呼び出します。Redpoint データマネジメントウェブサービスURL を入力します。このエントリは、オンボーディングと追加チャネルの両方で同じになります。

![][14]{: style="max-width:75%;"}

### ステップ4:RedpointデータマネジメントでのBrazeコンポーネントの設定 

BrazeインテグレーションをサポートするRedpointデータマネジメント(RPDM)アーティファクトを含むアーカイブには、必要なコンポーネントを設定するための詳細な手順を含むREADME が含まれています。統合を設定するときは、次の詳細に留意してください。 

#### ステップ4a:Braze REST エンドポイントおよび基本RPI出力ディレクトリーを使用してRPIをBraze オートメーションにアップデートする 

Braze関連のアーティファクトをRedpoint データマネジメントにインポートした後、**AUTO_Process_RPI_to_Braze** という名前のオートメーションを開封し、次の2 つのオートメーション変数を環境の値で更新します。

* **BRAZE_API_URL**:Braze REST エンドポイント
* **BASE_OUTPUT_DIRECTORY**:Redpoint Inter アクション とRedpoint Data Management 間の共有出力ディレクトリー

![][5]{: style="max-width:40%;"}

#### ステップ4b:Braze アプリエンドプロジェクトへのRPI のアップデート 

**PROJ_RPI_to_Braze_アプリ end**という名前のRedpointデータマネジメントプロジェクトには、Brazeの`rpi_cdp_attributes`カスタム属性オブジェクトの送信配信エクスポートファイルスキーマとmアプリが含まれています。 

**RPI という名前のファイル入力スキーマとドキュメントインジェクタツールを、エクスポートファイルテンプレートで定義された追加のカスタムCDP 属性でBraze ドキュメントインジェクタ** に更新します。次に、学歴、収入、配偶者のステータスに関する追加のm アプリを示します。

![][6]{: style="max-width:40%;"}

## 統合の使用

送信配信Braze チャネルは、Redpoint Inter アクション ワークフローで活用できるようになりました。RPI での選択ルールとオーディエンスの作成、および関連付けられたワークフロースケジュールs とトリガーs の構築については、標準的な方法に従ってください。 

RPI オーディエンス出力をBraze に同期するには、送信配信オファーを作成し、** Braze Onboarding and Upsert** または** Braze Append** チャネルのいずれかに関連付けます。これは、インテントがBrazeで新規レコードを作成またはマージするかどうか、またはレコードがBrazeにすでに存在する場合はエンドキャンペーンデータのみをアプリするかどうかによって異なります。

![][13]{: style="max-width:80%;"}

ワークフローがRPI で正常に実行されると、RPI からのオーケストレーション およびCDP データソースd を使用して、Braze でSegments を作成できるようになります。

![][12]{: style="max-width:80%;"}

Redpoint関連のプロパティーは、ユーザープロファイルで表示できます。

![][15]{: style="max-width:80%;"}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.redpointglobal.com
[3]: https://support.redpointglobal.com/hc/en-us/restricted?return_to=https%3A%2F%2Fsupport.redpointglobal.com%2Fhc%2Fen-us
[4]: {% image_buster /assets/img/redpoint/rpi_to_braze_custom_attributes.png %}
[5]: {% image_buster /assets/img/redpoint/rpi_to_braze_auto_variables.png %}
[6]: {% image_buster /assets/img/redpoint/rpi_to_braze_doc_injector_mappings.png %}
[7]: {% image_buster /assets/img/redpoint/rpi_to_braze_upsert_export_format.png %}
[8]: {% image_buster /assets/img/redpoint/rpi_to_braze_append_export_format.png %}
[9]: {% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_general.png %}
[10]: {% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_specific.png %}
[11]: {% image_buster /assets/img/redpoint/rpi_to_braze_export_directory_setup.png %}
[12]: {% image_buster /assets/img/redpoint/rpi_to_braze_build_braze_segment.png %}
[13]: {% image_buster /assets/img/redpoint/rpi_to_braze_rpi_canvas.png %}
[14]: {% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_post_execution.png %}
[15]: {% image_buster /assets/img/redpoint/rpi_to_braze_record_example.png %}
[16]: {% image_buster /assets/img/redpoint/rpi_to_braze_export_format_config.png %}
[17]: {{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields
