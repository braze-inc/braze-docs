---
nav_title: Optimizely
article_title: Optimizely
page_order: 2
description: "このリファレンス記事では、Braze と Optimizely のパートナーシップの概要を説明します。これにより、Braze の顧客セグメント、イベント、および Currents イベントを Optimizely データプラットフォームに同期できます。"
alias: /partners/optimizely/
page_type: partner
search_tag: Partner
---

# Optimizely

> [Optimizely](https://www.optimizely.com/) は、デジタル製品やマーケティングキャンペーンのための実験やコンテンツ管理ツールを提供する、主要なデジタルエクスペリエンスプラットフォームです。

Braze と Optimizely の統合は、双方向の統合であり、次のことが可能です。

- Braze の顧客セグメントとイベントを Optimizely Data Platform (ODP) に毎晩同期して、Optimizely の顧客プロファイル、レポート、およびセグメンテーションを強化します。
- Braze Currents イベントをBraze からOptimizely のレポートツールに送信します。
- ODP 顧客データとイベントをBraze に同期すると、Braze 顧客データが強化され、ODP の顧客イベントに基づいてBraze メッセージングがトリガーされます。

## 前提条件

| 必要条件                     | 説明 |
|----------------------------------|-------------|
| Optimizely データプラットフォームアカウント | このパートナーシップを活用するには、Optimizely Data Platform(ODP)アカウントが必要です。 |
| Braze REST API キー               | 以下の権限を持つBraze REST APIキーs: `users.track`、`users.export.segments`、`segments.list`、`campaigns.trigger.send`、および `canvas.trigger.send`。 |
| Currents                         | データをOptimizely に書き戻すには、アカウントにBraze Currents を設定する必要があります。 |
| URLとトークンの最適化         | これは、Optimizelyダッシュボードに移動し、取り込みURLとトークンをコピーすることで取得できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ 1: 統合を設定する

1. Optimizely Data Platform (ODP) の **App Directory** で、**Braze** アプリを選択し、[**アプリをインストール**] を選択します。
2. [**設定**] タブに移動します。[**Authorization**] セクションで、以下を実行します。
    1. Braze **REST API キー**を入力します。
    2. Braze **Instance URL** を選択します。
    2. [**API キーを確認**] を選択します。
3. Braze で、**[Currents]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents/)** に移動します。
4. [**Currents の新規作成**] > [**カスタム Currents エクスポート**] の順に選択します。
5. ODPで提供されるエンドポイントとトークンを使用して現在を設定します。これは、Braze イベントと ODP との同期に必要です。 

![Optimizely 認証]({% image_buster /assets/img/optimizely/image1_authorization.png %})

{:start="6"}
6. ODP で、[**セグメント**] セクションを展開し、[**同期するセグメント**] リストから特定のセグメントを選択するか、[**すべての顧客をインポート**] を選択してすべてのセグメントを同期します。
7. Braze とODP の間で必要な[フィールドマッピング](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/29918568615949-Integrate-Braze%23h_01J6Z1P53JVDBFZ758Q78CK1QB&sa=D&source=editors&ust=1733948158380300&usg=AOvVaw3WSAND5ie3LCVuSxUlLanR) を追加します。
8. [**保存**] を選択します。

![Optimizely と Braze のセグメント同期。]({% image_buster /assets/img/optimizely/image2_syncsegment.png %})

{% alert tip %}
Braze 顧客プロファイルをインポートするには、セグメントを選択する必要があります。セグメントを選択しない場合、統合でカスタマプロファイルはインポートされません。
{% endalert %}

### ステップ2: データフィールドをマップする

統合には、Braze と ODP 間のデフォルトのデータフィールドマッピングがあります。たとえば、Braze の [**メール**] フィールドは、ODP の [**Last Seen Email**] フィールドにマッピングされます。

![Optimizely と Braze のセグメントマッピングフィールド。]({% image_buster /assets/img/optimizely/image3_emailmapfield.png %})

#### 追加フィールドのマッピング (オプション)

ODP にマッピングする追加のデータフィールドが Braze にある場合は、ODP で以下の手順を実行します。

1. アプリの [**Segments**] セクションで、[**Braze User Data Fields**] ドロップダウンリストから Braze フィールドを選択します。
2. [**ODP Customer Fields**] ドロップダウンリストから ODP フィールドを選択します。
3. [**Save Field Map**] を選択します。

![Optimizely と Braze のセグメント保存フィールドマッピング]({% image_buster /assets/img/optimizely/image4_mapfields.png %})

#### 不要なフィールドマッピングの削除 (オプション)

不要なデータフィールドマッピングを削除することもできます。ODP で次の手順を実行します。

1. アプリの [**Segments**] セクションで、[**Field Map**] ドロップダウンリストから削除するフィールドマッピングを選択します。
2. [**Delete Field Map**] を選択します。

![Optimizely と Braze のセグメント削除フィールドマップ]({% image_buster /assets/img/optimizely/image5_deletephonefield.png %})

### ステップ 3:Optimizely Data Platform (ODP) から Braze へのデータの同期

統合を設定した後、ODP でアクティベーションを設定して、ODP カスタマーデータをBraze に同期できます。

1. [**Activation**] > [**Engage**] に進み、[**Create New Campaign**] を選択します。
2. [**Behavioral**] を選択して、自動定期同期を設定します。
3. [**最初から作成**] を選択し、Braze に同期するデータを表すアクティベーションの名前を入力します (**Braze データ同期** など)。
4. **登録** セクションでは、セグメントに一致する顧客のデータを同期したり、イベントをトリガする顧客のデータを同期したりできます(顧客がメールを開いたODP 登録時など)。
   - **セグメントに一致する顧客:**必要なセグメントを選択し、[**Next**] を選択します。<br><br>![Optimizely のセグメント選択]({% image_buster /assets/img/optimizely/image6_segment.png %})
   - **イベントをトリガーする顧客:**[**フィルター**] ドロップダウンリストを展開し、Braze へのこのデータ同期のトリガーとして使用する ODP イベントを選択します。次に、[**Automation Rules**] を展開し、必要に応じて調整します。<br><br>![Optimizely トリガーイベント]({% image_buster /assets/img/optimizely/image7_trigger.png %})
5. [**Touchpoints**] を展開し、[**Touchpoint 1**] の編集を選択して、[**Braze**} を選択します。
6. [**Targeting**] セクションを展開し、[**Target Identifier**] を選択します。
7. [**Configure**] セクションで、[**Add Users To**] に次のオプションのいずれかを選択します。
    - **キャンペーン:**Braze で特定のキャンペーンに顧客を追加します。このオプションを選択した後、Braze キャンペーンを選択する必要があります。
    - **キャンバス：**Braze で特定のキャンバスに顧客を追加します。このオプションを選択した後、Braze キャンペーンを選択する必要があります。
    - **プロファイル更新のみ:**Braze の顧客プロファイルのみを更新します。
8. (オプション) Braze に同期する [**追加フィールド数**] を選択します (最大 20)。  
    次に、追加フィールドのドロップダウンリストと入力フィールドごとに、次の項目を選択します。
    - 各 [**Field #**] ドロップダウンリストで、入力する Braze フィールドを選択します。 
    - 対応する [**Field # Value**] ごとに、選択した Braze フィールドに送信する ODP フィールドを入力します。たとえば、**Company Name** を[**Field #**] ドロップダウンリストで選択した場合は、対応する [**Field # Value**] に `{{customer.company_name}}` と入力します。
9. [**保存**] を選択し、パンくずリストのアクティベーション名を選択します。
10. 登録に [**Customers that match a segment**] を選択した場合は、[**Touchpoints**] セクションで [**Select start time and schedule**] を選択します。
11. 次の設定を行います。
    - **Recurring or Continuous:**[**Recurring**] を選択します。
    - **Start Date:**データを Braze に送信する日付を入力します。
    - **End:**デフォルトは **Never** です。特定の日付に Braze データの同期を終了する場合は、ここで設定します。
    - **Repeats:****Daily** に設定します。
    - **Repeat Every** - **1 day** に設定します。
    - **Timing:**データを Braze に送信する日付を入力します。
    - **Time Zone:**このデータを送信するタイムゾーンを選択します。
12. [**Apply**]、[**Save**]、[**Go Live**] を選択します。同期は、指定した開始日時 (またはトリガーイベントの発生時) に開始されます。

## トラブルシューティング

### イベントの検査

データが ODP から Braze に正しく同期されていることを確認するために、ODP でイベントを検査できます。

1. ODP で、[**Account Settings**] > [**Event Inspector**] と移動します。
2. [**インスペクターを開始**] を選択します。
3. インスペクタでデータが利用可能な場合、**Refresh** の横に数字が表示されます。データを表示する場合に選択します。
4. ODP と Braze が相互に送信する生データが表示されます。**View Details**を選択すると、その生データのフォーマットされたバージョンが表示されます。
5. Braze からODP に戻されるデータフィールドは、`_braze` で始まります。

### アクティビティログの確認

各データ同期は、[ODP アクティビティログ](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/4407268804365-Use-the-Activity-Log&sa=D&source=editors&ust=1733948158385124&usg=AOvVaw2tMOxzcTKfL0-oYLT4IMpP) にも記録されます。

1. [**アカウント設定**] > [**アクティビティログ**] に移動します。
2. **Braze** でカテゴリをフィルタリングします。
3. [**詳細を表示**] を選択すると、一致数を含むログの詳細がフォーマットされた形式で表示されます。

