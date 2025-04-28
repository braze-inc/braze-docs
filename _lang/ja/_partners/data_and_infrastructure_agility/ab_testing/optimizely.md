---
nav_title: 最適化
article_title: 最適化
page_order: 2
description: "このリファレンス記事では、ブレーズと最適化のパートナーシップの概要を説明します。これにより、ブレーズの顧客セグメント、イベント、および現在のイベントを最適化データプラットフォームに同期できます。"
alias: /partners/optimizely/
page_type: partner
search_tag: Partner
---

# 最適化

> [Optimizely](https://www.optimizely.com/)は、デジタル製品やマーケティングキャンペーンのための実験やコンテンツ管理ツールを提供する、主要なデジタルエクスペリエンスプラットフォームです。

ろう付けと最適化の統合は、次のことを可能にする2 方向の統合です。

- 顧客のセグメントとイベントを、Optimize Data Platform (ODP) の夜間に同期して、顧客プロファイル、レポート、およびセグメンテーションを最適化します。
- Braze Currents イベントをBraze からOptimizely のレポートツールに送信します。
- ODP 顧客データとイベントをBraze に同期すると、Braze 顧客データが強化され、ODP の顧客イベントに基づいてBraze メッセージングがトリガーされます。

## 前提条件

| 必要条件                     | 説明 |
|----------------------------------|-------------|
| データプラットフォームアカウントの最適化 | このパートナーシップを活用するには、Optimizely Data Platform(ODP)アカウントが必要です。 |
| Braze REST API キー               | 次の権限を持つRaze REST API キー。`users.track`、`users.export.segments`、`segments.list`、`campaigns.trigger.send`、`canvas.trigger.send`。 |
| Currents                         | データをOptimizely に書き戻すには、アカウントにBraze Currents を設定する必要があります。 |
| URLとトークンの最適化         | これは、Optimizelyダッシュボードに移動し、取り込みURLとトークンをコピーすることで取得できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:統合を設定する

1. Optimizely Data Platform(ODP)の**App Directory**で、**Braze**アプリを選択し、**Install App**を選択します。
2. **Settings**タブに移動します。**Authorization** セクションで、以下を実行します。
    1. Braze **REST API Key** と入力します。
    2. Braze **インスタンスURL**を選択します。
    2. **Verify API Key**を選択します。
3. ブレーズで、**[Currents]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents/)**に移動します。
4. **Create New Current** > **Custom Currents Export**を選択します。
5. ODPで提供されるエンドポイントとトークンを使用して現在を設定します。これは、ブレーズイベントをODP に同期するために必要です。 

![最適な許可。][1]

{:start="6"}
6. ODP で、**Segments** セクションを展開し、**Segments to Sync** リストから特定のセグメントを選択するか、**Import All Customers** を選択してすべてのセグメントを同期します。
7. Braze とODP の間に必要な[フィールドマッピング](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/29918568615949-Integrate-Braze%23h_01J6Z1P53JVDBFZ758Q78CK1QB&sa=D&source=editors&ust=1733948158380300&usg=AOvVaw3WSAND5ie3LCVuSxUlLanR) を追加します。
8. [**保存**] を選択します。

![セグメント同期を最適化する。][2]

{% alert tip %}
ブレーズ顧客プロファイルをインポートするには、セグメントを選択する必要があります。セグメントを選択しない場合、統合ではカスタマプロファイルはインポートされません。
{% endalert %}

### ステップ2:マップデータフィールド

統合には、Braze とODP 間のデフォルトのデータフィールドマッピングがあります。たとえば、Braze の**Email** フィールドは、ODP の**Last Seen Email** フィールドにマッピングされます。

![セグメントマップフィールドを最適化およびブレーズする。][3]

#### 追加フィールドのマップ(オプション)

ODP にマッピングする追加のデータフィールドがBraze にある場合は、ODP で以下の手順を実行します。

1. アプリの**Segments** セクションで、**Braze User Data Fields** ドロップダウンリストからBraze フィールドを選択します。
2. **ODPカスタマーフィールド**ドロップダウンリストからODPフィールドを選択します。
3. **Save Field Map**を選択します。

![セグメント保存フィールドマップの最適なろう付け][4]

#### 必須でないフィールドマッピングの削除(オプション)

必要のないデータフィールドマッピングを削除することもできます。ODP で次の手順を実行します。

1. アプリの**Segments** セクションで、**Field Map** ドロップダウンリストから削除するフィールドマッピングを選択します。
2. **Delete Field Map**を選択します。

![セグメント削除フィールドマップの最適なろう付け][5]

### ステップ 3:Optimizely Data Platform(ODP)からブレーズへのデータの同期

統合を設定した後、ODP でアクティベーションを設定して、ODP カスタマーデータをBraze に同期できます。

1. **Activation**> **Engage**に進み、**Create New Campaign**を選択します。
2. **Behavioral**を選択して、自動化された定期的な同期を設定します。
3. **Create From Scratch**を選択し、Brazeに同期するデータを表すアクティベーションの名前を入力します(**Braze Data Sync**など)。
4. **登録** セクションでは、セグメントに一致する顧客のデータを同期したり、イベントをトリガする顧客のデータを同期したりできます(顧客がメールを開いたODP 登録時など)。
   - **セグメントに一致する顧客:**希望するセグメントを選択し、**Next**を選択します。<br><br>![セグメントの最適選択][6]
   - **イベントをトリガする顧客:****Filter** ドロップダウンリストを展開し、このデータ同期のトリガとして使用するODP イベントを選択します。次に、**Automation Rules**を展開し、必要に応じて調整します。<br><br>![最適なトリガイベント][7]
5. **タッチポイント**を展開し、**タッチポイント1**の編集を選択し、**ブライズ**を選択します。
6. **Targeting**セクションを展開し、**Target Identifier**を選択します。
7. **Configure** セクションで、**Add Users To** に対して次のオプションのいずれかを選択します。
    - **キャンペーン:**Braze で特定のキャンペーンに顧客を追加します。このオプションを選択した後、ブレーズキャンペーンを選択する必要があります。
    - **キャンバス：**Braze で特定のキャンバスに顧客を追加します。このオプションを選択した後、ブレーズキャンバスを選択する必要があります。
    - **プロファイル更新のみ:**ブレーズの顧客プロファイルのみを更新します。
8. (オプション)ブレーズに同期する**追加フィールド数**を選択します(最大20)。  
    次に、追加フィールドのドロップダウンリストと入力フィールドごとに、次の項目を選択します。
    - 各**Field #** ドロップダウンリストで、入力するBraze フィールドを選択します。 
    - それぞれの対応する**Field # Value** に、選択したろう付けフィールドに送信するODP フィールドを入力します。たとえば、**Company Name** を**Field #** ドロップダウンリストから選択した場合は、対応する**Field # Value** に`{{customer.company_name}}` と入力します。
9. **Save**を選択し、ブレッドクラム証跡でアクティベーション名を選択します。
10. 登録に**セグメント**に一致する顧客を選択した場合は、****タッチポイント**セクションで開始時刻とスケジュール**を選択します。
11. 次の設定を行います。
    - **繰り返しまたは連続:****Recurring**を選択します。
    - **開始日:**データをろう付けに送信する日付を入力します。
    - **終了:**デフォルトは**Never** です。特定の日付でブレーズデータの同期を終了する場合は、ここで設定します。
    - **繰り返し:****Daily**に設定します。
    - **Repeat Every** - **1 日** に設定します。
    - **タイミング:**データをろう付けに送信する時間を入力します。
    - **タイムゾーン:**このデータを送信するタイムゾーンを選択します。
12. **Apply**、**Save**、**Go Live**を選択します。同期は、指定した開始日時(またはトリガイベントが発生したとき)に開始されます。

## トラブルシューティング

### イベントの検査

データがODP からブレーズに正しく同期されていることを確認するために、ODP でイベントを検査できます。

1. ODP で、**アカウント設定** > **イベントインスペクタ** に移動します。
2. **Start Inspector**を選択します。
3. インスペクタでデータが利用可能な場合、**Refresh** の横に数字が表示されます。データを表示する場合に選択します。
4. ODPとろう付けが前後に送る生データが表示されます。**View Details**を選択すると、その生データのフォーマットされたバージョンが表示されます。
5. Braze からODP に返されるデータフィールドは、`_braze` で始まります。

### アクティビティログの確認

各データ同期は、[ODP アクティビティログ](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/4407268804365-Use-the-Activity-Log&sa=D&source=editors&ust=1733948158385124&usg=AOvVaw2tMOxzcTKfL0-oYLT4IMpP) にも記録されます。

1. **Account Settings** > **Activity Log**に移動します。
2. **ブレーズ**でカテゴリをフィルタリングします。
3. 一致の数を含むログの詳細のフォーマットされたビューに対して、**View Details** を選択します。

[1]: {% image_buster /assets/img/optimizely/image1_authorization.png %}
[2]: {% image_buster /assets/img/optimizely/image2_syncsegment.png %}
[3]: {% image_buster /assets/img/optimizely/image3_emailmapfield.png %}
[4]: {% image_buster /assets/img/optimizely/image4_mapfields.png %}
[5]: {% image_buster /assets/img/optimizely/image5_deletephonefield.png %}
[6]: {% image_buster /assets/img/optimizely/image6_segment.png %}
[7]: {% image_buster /assets/img/optimizely/image7_trigger.png %} 