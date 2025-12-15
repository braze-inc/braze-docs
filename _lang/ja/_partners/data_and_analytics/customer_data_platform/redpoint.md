---
nav_title: Redpoint
article_title: Redpoint 
description: "Redpoint と Braze の統合により、ファーストパーティデータを使用して Braze ユーザープロファイルを登録および拡充できます。"
alias: /partners/redpoint/
page_type: partner
search_tag: Redpoint
---

# Redpoint

> [Redpoint](https://www.redpointglobal.com) は、完全に統合されたキャンペーンオーケストレーションプラットフォームをマーケターに提供するテクノロジープラットフォームです。Redpoint のセグメンテーション、スケジュール、およびオートメーション機能を活用して、CDP データが Braze にインポートされる方法とタイミングをコントロールします。

_この統合は Redpoint によって管理されます。_

## 統合について

Braze と Redpoint の統合により、Redpoint CDP データに基づいて Braze セグメントを作成できます。Redpoint には、データを Braze に渡すための2種類のモードがあります。 

1. **Braze Onboarding and Upsert** モード:"Upserts" RedpointからBrazeへのユーザープロファイル。これは、データが変更されたときに、ユーザーレコードを登録または更新するために使用されるものです。 
2. **Braze Append** モード:そのユーザーがBrazeにすでに存在する場合は、ユーザープロファイルをアップデートします。 

モードごとにエクスポートテンプレートとアウトバウンドチャネルを設定します。

{% alert note %}
"Upsert"は単語"更新"と"insert."の組合せです。データベーステーブルに新しいレコードが存在しない場合は、そのレコードをデータベーステーブルに挿入するか、存在する場合はレコードを更新する場合に使用されます。基本的に、upsert は、特定のレコードがデータベースに存在するかどうかを確認します。レコードが存在する場合はレコードが更新され、存在しない場合は新しいレコードが挿入されます。
{% endalert %}

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br>これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、インスタンスのBraze URLに依存する。 |
| Redpoint Data Management アーティファクト | Braze 統合は、一連の Redpoint Data Management アーティファクトによりサポートされています。ご使用の Redpoint Data Management バージョンに対応したアーティファクトをリクエストするには、[Redpoint Support](https://support.redpointglobal.com/hc/en-us/restricted?return_to=https%3A%2F%2Fsupport.redpointglobal.com%2Fhc%2Fen-us) にお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## RedpointCDPカスタム属性

次のRedpoint カスタム属性s をBraze ユーザープロファイルに追加できます。

| フィールド               | 説明                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `rpi_cdp_attributes` | Redpoint CDP プロファイル 属性の対象                                                                                  |
| `rpi_audience_outputs`| Redpoint Outbound Delivery Braze チャネルの実行でこのユーザーがターゲットとなるオーディエンス出力タグの配列         |
| `rpi_offers`         | Redpoint Outbound Delivery Braze チャネルの実行でこのユーザーがターゲットとなるオファータグの配列                   |
| `rpi_contact_ids`    | Redpoint Outbound Delivery Braze チャネルの実行でこのユーザーがターゲットとなるオファー履歴連絡先 ID の配列     |
| `rpi_channel_exec_ids`| Redpoint Outbound Delivery Braze チャネルの実行でこのユーザーがターゲットとなるチャネル実行 ID の配列       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/redpoint/rpi_to_braze_custom_attributes.png %}){: style="max-width:75%;"}

## 統合

### ステップ1:テンプレートの設定

#### ステップ 1a: Braze Onboarding and Upsert テンプレートを作成する

Redpointインターアクション(RPI) で、新しいエクスポートテンプレートを作成し、** Braze Onboarding and Upsert** という名前を付けます。このテンプレートでは、Redpoint CDP と Braze ユーザープロファイルの間のコアマッピングと、Braze でユーザープロファイルに追加するカスタム属性を定義します。

Redpoint CDP 属性sを**属性**列にドラッグアンドドロップします。それぞれの**ヘッダー行値**を対応するBraze [ユーザー 属性]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)]に設定します。 

以下のテーブルに、Redpoint CDP 属性と対応するBraze 属性s を示します。

| Redpointアトリビュート | ヘッダ行値 |
|--------------------|------------------|
| PID                | `external_id`    |
| Fist Name          | `first_name`     |
| 姓          | `last_name`      |
| Primary Email      | `email`          |
| 主要国    | `country`        |
| DOB                | `dob`            |
| 性別             | `gender`         |
| Primary City       | `home_city`      |
| Primary Phone      | `phone`          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[**Offer History**] テーブルの [**Offer Name**] 属性を追加します。最後に、Braze にマージするカスタム Redpoint 属性を追加します。たとえば、Education、Income、および Marital Status が属性として追加されている Onboarding and Upsert テンプレートを以下に示します。

![]({% image_buster /assets/img/redpoint/rpi_to_braze_upsert_export_format.png %}){: style="max-width:75%;"}

#### ステップ 1b: Braze追加テンプレートの作成

追加専用操作のための2つ目のエクスポートテンプレートを **Braze Append** という名前で作成します。

このテンプレートには2 つの属性s のみを設定します。**PID**の場合は、**Header Row Value**を`external_id`に設定します。**Output Name**の場合、**Header Row**を`output_name`に設定します。

![`external_id` および Output Name 属性を含むエクスポートテンプレートの例。]({% image_buster /assets/img/redpoint/rpi_to_braze_append_export_format.png %}){: style="max-width:75%;"}

#### ステップ1c:日付形式の設定

両方のエクスポートテンプレートs で、**Options** タブに移動し、**Date Format** を**カスタム書式** の値に設定します。形式を**yyyy-MM-dd**に設定します。

![日付形式がyyyy-MM-dd に設定されているオプションタブ。]({% image_buster /assets/img/redpoint/rpi_to_braze_export_format_config.png %}){: style="max-width:75%;"}

### ステップ2:アウトバウンドチャネルを作成する

RPI で2つの新しいチャネルを作成します。両方のチャネルを [**Outbound Delivery**] に設定します。1つのチャネルに **Braze Onboarding and Upsert** という名前を付け、もう1つのチャネルに **Braze Append** という名前を付けます。

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_general.png %}){: style="max-width:75%;"}

{% alert note %}
Braze への CDP レコードの最初の登録後に、Braze Onboarding and Upsert チャネルを使用する後続の Redpoint Interaction ワークフローが、最初の登録同期以降に変更されたレコードのみを選択するように設計されているかどうかを確認します。
{% endalert %}

### ステップ 3:チャネルの設定s

#### ステップ3a:テンプレートおよびエクスポートパス形式の設定

チャネルの [**Configuration**] 画面の [**General**] タブに移動します。エクスポートテンプレートをそれぞれのチャネルに設定します。 

次に、Redpoint Interaction と Redpoint Data Management の両方がアクセスできる外部コンテンツプロバイダーの場所、ファイル転送プロトコル、または共有ネットワークを指す両方のチャネルで、**エクスポートパス形式**を定義します。 

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_specific.png %}){: style="max-width:75%;"}

両方のチャネルのエクスポートディレクトリ形式は同一であり、`\\[Channel]\\[Offer]\\[Workflow ID]` で終わる必要があります。

![]({% image_buster /assets/img/redpoint/rpi_to_braze_export_directory_setup.png %}){: style="max-width:50%;"}

#### ステップ 3b： 実行後の設定

Channels **Configuration** 画面の**Post Execution** タブに移動します。 

チャネル実行後に**実行後**にチェックを入れ、サービスURLを呼び出します。Redpoint Data Management Web サービスの URL を入力します。このエントリは、Onboarding チャネルと Append チャネルの両方で同一です。

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_post_execution.png %}){: style="max-width:75%;"}

### ステップ 4: Redpoint Data Management で Braze コンポーネントを設定する 

Braze 統合をサポートするための Redpoint Data Management (RPDM) アーティファクトを含むアーカイブには、必要なコンポーネントの詳しい設定手順が記載された README が含まれています。統合を設定するときには以下の点に留意してください。 

#### ステップ4a:Braze REST エンドポイントとベース RPI 出力ディレクトリで RPI to Braze オートメーションを更新する 

Braze関連の成果物をRedpointデータマネージャーにインポートした後、以下の名前のオートメーションを開封する。 **AUTO_Process_RPI_to_Braze**という名前のオートメーションを開き、以下の2つのオートメーション変数をあなたの環境の値で更新する：

* **BRAZE_API_URL**:Braze REST エンドポイント
* **BASE_OUTPUT_DIRECTORY**:Redpoint Interaction と Redpoint Data Management 間の共有出力ディレクトリ

![]({% image_buster /assets/img/redpoint/rpi_to_braze_auto_variables.png %}){: style="max-width:40%;"}

#### ステップ 4b: RPI to Braze append プロジェクトを更新する 

というRedpointデータマネージメントプロジェクトがある。 **PROJ_RPI_to_Braze_Append**という名前のRedpoint Data Managementプロジェクトには、Brazeの`rpi_cdp_attributes` カスタム属性オブジェクトのための、配信エクスポートファイルのスキーマとマッピングが含まれている。 

ファイル入力スキーマとドキュメント挿入ツール **RPI to Braze Document Injector** を、エクスポートファイルテンプレートに定義されている追加のカスタム CDP 属性で更新します。次の例に、education、income、marital_status の追加マッピングを示します。

![]({% image_buster /assets/img/redpoint/rpi_to_braze_doc_injector_mappings.png %}){: style="max-width:40%;"}

## 統合の使用

Outbound Delivery Braze チャネルを Redpoint Interaction ワークフロー内で利用できるようになりました。RPI での選択ルールとオーディエンスの作成、および関連付けられたワークフロースケジュールs とトリガーs の構築については、標準的な方法に従ってください。 

RPI Audience 出力を Braze に同期するには、アウトバウンド配信オファーを作成し、**Braze Onboarding and Upsert** チャネルまたは**Braze Append** チャネルのいずれかに関連付けます。これは、その目的が、Braze で新規レコードを作成またはマージすること、またはレコードが Braze に既に存在する場合にのみキャンペーンデータを追加することのいずれであるかによって異なります。

![]({% image_buster /assets/img/redpoint/rpi_to_braze_rpi_canvas.png %}){: style="max-width:80%;"}

ワークフローが RPI で正常に実行されると、RPI から取得したオーケストレーションおよび CDP データを使用して、Braze でセグメントを作成できるようになります。

![]({% image_buster /assets/img/redpoint/rpi_to_braze_build_braze_segment.png %}){: style="max-width:80%;"}

Redpoint関連のプロパティーは、ユーザープロファイルで表示できます。

![]({% image_buster /assets/img/redpoint/rpi_to_braze_record_example.png %}){: style="max-width:80%;"}


