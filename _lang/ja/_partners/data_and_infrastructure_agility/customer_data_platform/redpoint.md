---
nav_title: Redpoint
article_title:Redpoint
description:"RedpointとBrazeの統合により、ファーストパーティデータをBrazeユーザープロファイルにオンボーディングし、充実させることができる。"
alias: /partners/redpoint/
page_type: partner
search_tag:Redpoint
---

# Redpoint

> [レッド][2]ポイントは、完全に統合されたキャンペーンオーケストレーションプラットフォームをマーケターに提供するテクノロジープラットフォームである。Redpointのセグメンテーション、スケジュール、オートメーション機能を活用し、CDPデータをBrazeにインポートする方法とタイミングをコントロールする。

BrazeとRedpointの統合により、RedpointのCDPデータに基づいてBrazeのセグメンテーションを作成できる。Redpointには、Brazeにデータを渡すための2つのモードがある： 

1. **オンボーディングとアップサートモード**：ユーザープロファイルをRedpointからBrazeに "Upsert "する。これは、オンボーディングやユーザーデータが変更された場合のユーザー記録の更新に使用されることを意図している。 
2. **Braze Append**モード：ユーザーが既にBrazeに存在する場合、ユーザープロファイルを更新する。 

各モードのエクスポートテンプレートと送信チャネルを設定する。

{% alert note %}
"upsert "は "update "と "insert "を組み合わせた言葉だ。't already exist or update the record if it does exist. Essentially, upsert checks whether a particular record is present in the database. If the record is present, it'、更新されていなければ新しいレコードが挿入される。
{% endalert %}

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br>これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | [RESTエンドポイントのURL][1]。エンドポイントはインスタンスのBraze URLに依存する。 |
| レッドポイント・データ・マネジメントの成果物 | Brazeとの統合は、一連のRedpointデータ管理成果物によってサポートされている。[Redpoint][3]Data Management のバージョンに対応する成果物を要求するには、[Redpoint サポートに][3]連絡すること。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**Developer Console**>**API Settingsで**APIキーを作成できる。
{% endalert %}

## レッドポイントCDPカスタム属性

以下のRedpointカスタム属性をBrazeユーザープロファイルに追加できる。

| フィールド               | 説明                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `rpi_cdp_attributes` | Redpoint CDPプロファイル属性オブジェクト。                                                                                  |
| `rpi_audience_outputs`| Redpoint Outbound Delivery Brazeチャネル実行でユーザーがターゲットとなるオーディエンス出力タグの配列。         |
| `rpi_offers`         | ユーザーがRedpoint Outbound Delivery Brazeチャネル実行のターゲットとなるオファータグの配列。                   |
| `rpi_contact_ids`    | ユーザーがRedpoint Outbound Delivery Brazeチャネル実行のターゲットとなったオファー履歴コンタクトIDの配列。     |
| `rpi_channel_exec_ids`| ユーザーがRedpoint Outbound Delivery Brazeチャネル実行のターゲットとなっているチャネル実行IDの配列。       |
{: .reset-td-br-1 .reset-td-br-2}

![][4]{: style="max-width:75%;"}

## 統合

### ステップ1:テンプレートの設定

#### ステップ 1a: Braze Onboarding and Upsertテンプレートを作成する。

Redpoint Interaction（RPI）で、新しいエクスポートテンプレートを作成し、**Braze Onboarding and Upsertと**名付ける。このテンプレートは、Redpoint CDPとBrazeユーザープロファイル間のコアマッピングを定義し、Brazeのユーザープロファイルに追加したいカスタム属性も定義する。

Redpoint CDPの属性を**アトリビューション**列にドラッグする。**各ヘッダー行の**値を対応するBraze \[ユーザー属性][17] に設定する。 

以下の表は、Redpoint CDP属性と、それに対応するBraze属性の一覧である：

| レッドポイント属性 | ヘッダー行の値 |
|--------------------|------------------|
| ピッド                | `external_id`    |
| 拳の名前          | `first_name`     |
| 姓          | `last_name`      |
| 主要メール      | `email`          |
| 主要国    | `country`        |
| DOBについて                | `dob`            |
| 性別             | `gender`         |
| 市区町村       | `home_city`      |
| 代表電話      | `phone`          |
{: .reset-td-br-1 .reset-td-br-2}

**Offer History**テーブルから**Output Name**属性を追加する。最後に、BrazeにマージしたいカスタムRedpoint属性を追加する。例えば、学歴、収入、婚姻ステータスを追加属性としたオンボーディングとアップサートのテンプレートを以下に示す。

![][7]{: style="max-width:75%;"}

#### ステップ 1b: Braze Appendテンプレートを作成する。

**Braze Appendという**名前の、アペンドのみの操作用の2つ目のエクスポートテンプレートを作成する。

このテンプレートには2つの属性しか設定しない。**PIDについては**、**ヘッダー行の値を** `external_id` と設定する。**出力名には**、**ヘッダー行を** `output_name` と設定する。

![external_id\`とoutput name属性を持つエクスポートテンプレートのサンプル。][8]{: style="max-width:75%;"}

#### ステップ1c：日付フォーマットの設定

どちらのエクスポート・テンプレートでも、**「オプション」**タブに移動し、「**日付フォーマット**」を「**カスタム・フォーマット**」に設定する。フォーマットを**yyyy-MM-ddに**設定する。

![オプションタブで日付の書式がyyyy-MM-ddに設定されている。][16]{: style="max-width:75%;"}

### ステップ2:アウトバウンド・チャネルを作る

RPIで、2つの新しいチャネルを作成する。両方のチャネルを**Outbound Deliveryに**設定する。一方のチャネルを**Braze Onboarding and Upsert**、もう一方を**Braze Appendと**名付ける。

![][9]{: style="max-width:75%;"}

{% alert note %}
CDPレコードをBrazeに最初にオンボーディングした後、BrazeオンボーディングおよびUpsertチャネルを使用する後続のRedpoint Interactionワークフローが、最初のオンボーディング同期以降に変更されたレコードのみを選択するように設計されているかどうかを確認する。
{% endalert %}

### ステップ3:チャネルを設定する

#### ステップ3a：テンプレートとエクスポートパスのフォーマットを設定する

チャネル**設定**画面の**General**タブに移動する。それぞれのチャンネルにエクスポート・テンプレートを設定する。 

次に、Redpoint InteractionとRedpoint Data Managementの両方がアクセス可能な共有ネットワーク、ファイル転送プロトコル、または外部コンテンツプロバイダーの場所をポイントする**Exportパスフォーマットを**両方のチャネルで定義する。 

![][10]{: style="max-width:75%;"}

両チャンネルのエクスポート・ディレクトリのフォーマットは同じで、`\\[Channel]\\[Offer]\\[Workflow ID]` で終わる。

![][11]{: style="max-width:50%;"}

#### ステップ3b：実行後の設定

チャネル**設定**画面の**Post Execution**タブに移動する。 

チャネル実行後にサービスURLを呼び出すには、**Post-execution**チェックボックスをチェックする。Redpoint Data ManagementウェブサービスのURLを入力する。このエントリは、オンボーディングとアペンドの両方のチャネルで同じになる。

![][14]{: style="max-width:75%;"}

### ステップ 4:Redpointデータ管理でBrazeコンポーネントを設定する 

Brazeとの統合をサポートするRedpoint Data Management (RPDM)の成果物を含むアーカイブには、必要なコンポーネントの設定の詳細な説明が記載されたREADMEが含まれている。統合を設定する際には、以下の詳細に留意すること。 

#### ステップ4a：Braze RESTエンドポイントとベースRPI出力ディレクトリを使用して、RPIをBrazeオートメーションに更新する。 

Braze関連のアーティファクトをRedpoint Data Managementにインポートした後、**AUTO_Process_RPI_to_Brazeという**オートメーションを開封し、以下の2つのオートメーション変数を使用環境に応じた値で更新する：

* **BRAZE_API_URL**：Braze RESTエンドポイント
* **BASE_OUTPUT_DIRECTORY**：Redpoint InteractionとRedpoint Data Managementの間で共有される出力ディレクトリ。

![][5]{: style="max-width:40%;"}

#### ステップ4b：RPIからBrazeへの追加プロジェクトの更新 

**PROJ_RPI_to_Braze_Appendという**名前のRedpointデータ管理プロジェクトには、Brazeの`rpi_cdp_attributes` カスタム属性オブジェクトのための送信配信エクスポートファイルスキーマとマッピングが含まれている。 

ファイル入力スキーマと**RPIという**ドキュメントインジェクターツールを**Braze Document Injectorに**更新し、エクスポートファイルテンプレートで定義したカスタムCDP属性を追加する。この例では、学歴、収入、配偶者のステータスを追加マッピングしている：

![][6]{: style="max-width:40%;"}

## 統合を利用する

Outbound Delivery Brazeチャネルは、Redpoint Interactionワークフロー内で活用できるようになった。RPIで選択ルールとオーディエンスを作成し、関連するワークフローのスケジュールとトリガーを構築するための標準的なプラクティスに従う。 

RPIオーディエンス出力のBrazeへの同期を有効にするには、アウトバウンド配信オファーを作成し、**Brazeオンボーディングとアップサート**または**Brazeアペンドチャネルの**いずれかに関連付ける。これは、Brazeに新しいレコードを作成またはマージするのか、Brazeにすでにレコードが存在する場合にのみキャンペーンデータを追加するのかによって異なる。

![][13]{: style="max-width:80%;"}

RPIでワークフローが正常に実行されると、RPIから取得したオーケストレーションデータとCDPデータを使用して、Brazeでセグメンテーションを作成できるようになる。

![][12]{: style="max-width:80%;"}

ユーザープロファイルでレッドポイント関連のプロパティを見ることができる。

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
