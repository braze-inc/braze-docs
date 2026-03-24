---
nav_title: カスタムイベント
article_title: カスタムイベント
page_order: 9
page_type: reference
description: "この記事では、カスタムイベントとプロパティ、セグメンテーション、使用法、キャンバスエントリのプロパティ、関連する分析が表示される場所などについて説明します。"
search_rank: 2
---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}カスタムイベント

> この記事では、カスタムイベントとプロパティ、関連するセグメンテーションフィルター、キャンバスエントリプロパティ、関連する分析などについて説明します。Braze のイベント全般については、「[イベント]({{site.baseurl}}/user_guide/data/custom_data/events/)」を参照してください。

カスタムイベントとは、ユーザーによって実行されたアクションまたはユーザーに関する更新です。カスタムイベントがログに記録されると、任意の数とタイプのフォローアップキャンペーンをトリガーできます。その後、[セグメンテーションフィルター](#segmentation-filters)を使用して、カスタムイベントの発生頻度や最終発生日時に基づいてユーザーをセグメント化できます。これにより、カスタムイベントは、アプリケーション内の高価値のユーザーインタラクションの追跡に最適です。

## ユースケース

一般的なカスタムイベントのユースケースをいくつか示します。

- [アクションベースの配信]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)を使用したカスタムイベントに基づくキャンペーンまたはキャンバスのトリガー
- ユーザーがカスタムイベントを実行した回数、イベントが最後に発生した時刻などに基づくユーザーのセグメント化
- ダッシュボードの[カスタムイベント分析]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-event-analytics)を使用した、各イベントの発生頻度の集計表示
- [ファネル]({{site.baseurl}}/user_guide/data_and_analytics/reporting/funnel_reports/#step-2-select-events-for-funnel-steps)および[リテンション]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/)レポートを使用した追加の分析
- [永続的なエントリプロパティ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/)を活用し、キャンバスステップで顧客イベントのメタデータをパーソナライゼーションに使用
- [Currents]({{site.baseurl}}/user_guide/data/braze_currents/)を使用したより高度な分析の生成
- ユーザーがキャンバスから退出するタイミングを定義する[退出基準]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria)の設定

## カスタムイベントの管理

ダッシュボードでカスタムイベントを管理、作成、またはブロックリストに登録するには、**データ設定** > **カスタムイベント**に移動します。

次のアクションを実行するには、カスタムイベントの横にあるメニューを選択します。

### ブロックリスト

アクションメニューから個々のカスタムイベントをブロックリストに登録することも、最大100件のイベントを一括で選択してブロックリストに登録することもできます。

カスタムイベントをブロックすると、以下のようになります。

- そのイベントの将来のデータは収集されません。
- 既存のデータは、そのイベントのブロックが解除されない限り使用できません。
- そのイベントはフィルターやグラフに表示されません。

さらに、ブロックされたカスタムイベントが現在 Braze の他の領域のフィルターまたはトリガーによって参照されている場合、それを参照するフィルターまたはトリガーのすべてのインスタンスが削除され、アーカイブされることを示す警告モーダルが表示されます。

### 説明の追加

`Manage Events, Attributes, Purchases` [ユーザー権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)がある場合は、作成後にカスタムイベントに説明を追加できます。カスタムイベントの [**説明を編集**] を選択し、チームへのメモなど任意の内容を入力します。

## タグの追加

「Manage Events, Attributes, Purchases」[ユーザー権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)がある場合は、作成後にカスタムイベントにタグを追加できます。タグは、イベントのリストをフィルタリングするために使用できます。

### 使用状況レポートの表示

使用状況レポートには、特定のカスタムイベントを使用しているすべてのキャンバス、キャンペーン、およびセグメントが一覧表示されます。このリストには、Liquid の使用は含まれていません。

複数のカスタムイベントのチェックボックスを選択し、**使用状況レポートの表示**を選択することで、一度に最大100件の使用状況レポートを表示できます。

## データのエクスポート

カスタムイベントのリストをCSVファイルとしてエクスポートするには、ページ上部の**Export all**ボタンを選択します。CSVファイルが生成され、ダウンロードリンクがメールで送信されます。

## カスタムイベントのログ記録

カスタムイベントには追加の設定が必要です。各プラットフォームに関するドキュメントについては、以下のリストを参照してください。ここでは、カスタムイベントのログ記録に使用される方法、およびカスタムイベントにプロパティと数量を追加する方法について説明しています。

{% details プラットフォーム別のドキュメントを展開 %}

- [Android と FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=unity)
- [.NET MAUI（旧称 Xamarin）]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=roku)

{% enddetails %}

## カスタムイベントの保存

カスタムイベントのメタデータ（最初/最後の発生日時、合計数、30日間における X in Y）を含む、**ユーザープロファイル**に保存されているすべてのデータは、各プロファイルが[アクティブ]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users)である限り無期限に保持されます。

## セグメンテーションフィルター

次の表に、カスタムイベントによるユーザーのセグメント化に使用できるフィルターを示します。

| セグメンテーションオプション | ドロップダウンフィルター | 入力オプション |
| ---------------------| --------------- | ------------- |
| カスタムイベントが**X回を超えて**発生したかどうかをチェックする | **MORE THAN** | **NUMBER** |
| カスタムイベントの発生が**X回未満か**どうかをチェックする | **LESS THAN** | **NUMBER** |
| カスタムイベントが**正確にX回**発生したかどうかをチェックする | **EXACTLY** | **NUMBER** |
| カスタムイベントが**日付 X より後**に最後に発生したかどうかをチェックする | **AFTER** | **TIME** |
| カスタムイベントが**日付 X より前**に最後に発生したかどうかをチェックする | **BEFORE** | **TIME** |
| カスタムイベントが最後に発生したのが**X日以上前か**どうかをチェックする | **MORE THAN** | **NUMBER OF DAYS AGO**（正の数） |
| カスタムイベントが最後に発生したのが**X日以内か**どうかをチェックする | **LESS THAN** | **NUMBER OF DAYS AGO**（正の数） |
| カスタムイベントが**X（最大 = 50）回を超えて**発生したかどうかをチェックする | **MORE THAN** | 過去**Y日間（Y = 1,3,7,14,21,30）** |
| カスタムイベントが**X（最大 = 50）回未満**発生したかどうかをチェックする | **LESS THAN** | 過去**Y日間（Y = 1、3、7、14、21、30）** |
| カスタムイベントが**正確にX（最大 = 50）回**発生したかどうかをチェックする | **EXACTLY** | 過去**Y日間（Y = 1、3、7、14、21、30）** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 分析

Braze はセグメンテーション用として、カスタムイベントが発生した回数と、各ユーザーの最終実行時刻を記録します。これらの分析を表示するには、**Analytics** > **カスタムイベントレポート**に移動します。

ダッシュボードの**カスタムイベントレポート**ページで、各カスタムイベントの発生頻度を集約して表示できます。時系列データに重ねて表示されている灰色の線は、キャンペーンが最後に送信された時期を示しています。これは、キャンペーンがカスタムイベントの活動にどう影響したかを確認するのに役立ちます。

![ダッシュボードの [カスタムイベント] ページのカスタムイベント数グラフ（カスタムイベントの傾向を示す）]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

**フィルター**を使用して、カスタムイベントを時間、月間アクティブユーザー数（MAU）、セグメント、または KPI 式別に分類することもできます。

![カスタムイベントのグラフフィルター]({% image_buster /assets/img/custom_events_report_filters.png %}){: style="max-width:40%;"}

{% alert tip %}
[カスタム属性をインクリメント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers)して、カスタムイベントに似たユーザーアクションのカウンターを保持できます。ただし、カスタム属性データを時系列で表示することはできません。時系列で分析する必要のないユーザーアクションは、この方法を使用して記録してください。
{% endalert %}

### カスタムイベント分析が表示されない理由

カスタムイベントデータを使用して作成されたセグメントでは、作成前の過去の履歴データを表示できません。

## カスタムイベントプロパティ

カスタムイベントプロパティは、イベントの特定の発生を表すカスタムイベントのメタデータまたは属性です。これらのプロパティを使用して、トリガー条件の絞り込み、メッセージングのパーソナライゼーションの強化、コンバージョンの追跡、生データのエクスポートによるより高度な分析の生成ができます。

カスタムイベントプロパティは Braze プロファイルに保存されないため、データポイントを消費しません（例外については[データポイント](#data-points)を参照してください）。

{% alert important %}
各カスタムイベントまたは購入には、最大256個の異なるカスタムイベントプロパティを設定できます。256個を超えるプロパティを持つカスタムイベントまたは購入がログ記録された場合、最初の256個のみがキャプチャされて使用可能になります。
{% endalert %}

### 必要なフォーマット

プロパティ値は、キーがプロパティ名、値がプロパティ値であるオブジェクトでなければなりません。プロパティ名は、255文字以下の空でない文字列でなければならず、先頭にドル記号（`$`）は使用できません。

プロパティ値は、次のデータタイプのいずれでもかまいません。

| データタイプ | 説明 |
| --- | --- |
| 数値 | [整数](https://en.wikipedia.org/wiki/Integer)または[浮動小数点数](https://en.wikipedia.org/wiki/Floating-point_arithmetic)として |
| ブール値 | `true`または`false`の値。 |
| 日時 | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)または`yyyy-MM-dd'T'HH:mm:ss:SSSZ`形式の文字列としてフォーマットされます。配列内ではサポートされていません。 |
| 文字列 | 255文字以下。 |
| 配列 | 配列に日時を含めることはできません。 |
| ネストされたオブジェクト | 他のオブジェクトの中にあるオブジェクト。詳細については、この記事の「[ネストされたオブジェクト](#nested-objects)」のセクションを参照してください。
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

配列またはオブジェクト値を含むイベントプロパティオブジェクトには、最大100&nbsp;KBのイベントプロパティペイロードを設定できます。

プロパティ値のデータタイプは、[カスタム属性]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/)の値と同様に検出・処理されますが、2つの重要な違いがあります。

- **文字列から時間への変換:** 認識された時間形式に一致する文字列値は、自動的に日時型に変換されます。これは、一部の文字列値がイベントプロパティにそのまま保存できないことを意味します。
- **型の強制変換なし:** イベントプロパティには自動的な型の強制変換はありません。トリガーフィルターが数値`5`を期待している場合、文字列値`"5"`は一致しません。同じことが Liquid テンプレートと Currents イベントデータにも適用されます。

これらの動作は[購入イベントプロパティ]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#purchase-properties)にも適用されます。

カスタムイベントプロパティのデータタイプは変更できますが、データの収集後に[データタイプを変更]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/)した場合の影響に注意してください。

#### 予約キー

予約キーをイベントのプロパティ名として使用することはできません。`properties`オブジェクトで予約キーを使用すると、「Invalid 'properties' field」というエラーが返されます。

| プロパティ | 予約キー |
| --- | --- |
| カスタムイベント | `time` と `event_name` | 
| 購入イベント | `time`、`product_id`、`quantity`、`event_name`、`price`、`currency` | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### カスタムイベントプロパティの使用

カスタムイベントプロパティを使用して、キャンペーントリガーの絞り込み、コンバージョンの追跡、メッセージングのパーソナライズができます。

#### メッセージのトリガー

カスタムイベントプロパティを使用して、特定のキャンペーンまたはキャンバスのオーディエンスをさらに絞り込むことができます。例えば、eコマースアプリケーションがあり、ユーザーがカートを放棄したときにメッセージを送信したい場合、`item price`のカスタムイベントプロパティを追加することで、ターゲットオーディエンスを改善し、キャンペーンのパーソナライゼーションを高めることができます。

![放棄カートのカスタムイベントプロパティフィルター。2つのフィルターがAND演算子で結合され、商品価格が100ドルから200ドルの商品をカートに入れたまま離脱したユーザーにこのキャンペーンを送信する。]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png")

ネストされたカスタムイベントプロパティは[アクションベースの配信]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)でもサポートされています。

![放棄カートのカスタムイベントプロパティフィルター。カート内のいずれかの商品価格が100ドルを超える場合に、1つのフィルターが選択されます。]({% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png")

#### メッセージのパーソナライズ

カスタムイベントプロパティは、メッセージングテンプレート内でのパーソナライゼーションにも使用できます。トリガーイベントを持つ[アクションベースの配信]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)を使用するキャンペーンでは、そのイベントのカスタムイベントプロパティをメッセージングのパーソナライゼーションに使用できます。

たとえば、ゲームアプリがあり、レベルを完了したユーザーにメッセージを送信する場合、ユーザーがそのレベルを完了するのにかかった時間のプロパティを使用してメッセージをさらにパーソナライズできます。この例では、メッセージは[条件付きロジック]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/)を使用して3つの異なるセグメントに対してパーソナライズされています。カスタムイベントプロパティ`time_spent`は、``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``を呼び出すことでメッセージに含めることができます。

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Incredible work, hero! Are you ready to test your skills against other powerful heroes? Visit the Arena for real-time battles with top players from around the globe.
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Great job, hero! Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Well done, hero! Talk to villagers for tips on how to beat levels faster and unlock more rewards.
{% endif %}
```
{% endraw %}

{% alert warning %}
ユーザーにインターネット接続がない場合、テンプレート化されたカスタムイベントプロパティ（例: {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}）を含むトリガーされたアプリ内メッセージは失敗し、表示されません。
{% endalert %}

アプリ内メッセージをテンプレート化されたアプリ内メッセージとして配信する Liquid タグの完全なリストについては、[よくある質問]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/faq/#what-are-templated-in-app-messages/)を参照してください。

##### フィルターに関する考慮事項

- **API 呼び出し:** API 呼び出しを行い、「is blank」フィルターを使用する場合、呼び出しから除外されたカスタムイベントプロパティは「blank」と見なされます。例えば、`"event_property": ""`を含めた場合、ユーザーは「not blank」と見なされます。
- **整数:** 数値のカスタムイベントプロパティでフィルタリングする際に、値が非常に大きい場合は、「exactly」フィルターを使用しないでください。数値が大きすぎると特定の桁数で丸められ、フィルターが意図どおりに機能しないことがあります。

#### セグメンテーション

イベントプロパティセグメンテーションを使用して、実行されたカスタムイベントとそれらのイベントに関連付けられたプロパティに基づいてユーザーをターゲットにします。これにより、購入イベントとカスタムイベントによるセグメンテーションのフィルタリングオプションが増えます。

カスタムイベントのイベントプロパティは、それを使用するすべてのセグメントでリアルタイムに更新されます。プロパティの管理は、**データ設定** > **カスタムイベント**に移動し、関連するカスタムイベントの**プロパティの管理**を選択することで行えます。特定のセグメントフィルターで使用されるカスタムイベントプロパティの最大遡及期間は30日間です。

##### セグメンテーション用のイベントプロパティの追加

イベントプロパティの最新性と頻度に基づいてセグメントを作成するには、「Edit Custom Event Property Segmentation」[ユーザー権限]({{site.baseurl}}/user_guide/data/data_points/#viewing-data-point-usage)が必要です。

{% multi_lang_include deprecations/user_permissions.md %}

デフォルトでは、1つのワークスペースにつき20個のセグメント化可能なイベントプロパティを設定できます。この制限を増やすには、Braze アカウントマネージャーにお問い合わせください。

セグメンテーション用のイベントプロパティを追加するには、以下の手順を実行します。

1. カスタムイベントに移動し、[**プロパティを管理**] を選択します。
2. [**セグメンテーションを有効にする**] トグルを選択して、セグメンテーション用のイベントプロパティを追加します。セグメンテーションの際に、追加のフィルタリングオプションにアクセスできます。

イベントプロパティセグメンテーションフィルターには次のようなものがあります。

- 過去Y日間に、値Bのプロパティ Aを持つカスタムイベントをX回実行した。
- 過去Y日間に、値BのプロパティAを持ついずれかの購入をX回行った。
- 1～30日以内のセグメント化機能を追加。

![過去30暦日間に、プロパティ「商品数」の値が2である「放棄カート」が1回以上発生したフィルターグループ。]({% image_buster /assets/img/nested_object3.png %})

データは、特定のイベントプロパティを有効にした後にのみ記録されます。また、イベントプロパティは有効にした日付以降のみ利用可能です。

##### データポイント

サブスクリプションの使用に関して、以下のフィルターでセグメンテーション用に有効化されたカスタムイベントプロパティは、カスタムイベント自体でカウントされるデータポイントに加えて、すべて個別のデータポイントとしてカウントされます。

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### キャンバスエントリプロパティとイベントプロパティ

{% multi_lang_include canvas_entry_event_properties.md %}

### ネストされたオブジェクト {#nested-objects}

ネストされたオブジェクト（他のオブジェクト内にあるオブジェクト）を使用すると、カスタムイベントや購入のプロパティとしてネストされた JSON データを送信できます。このネストされたデータは、メッセージ内のパーソナライズされた情報のテンプレート作成、メッセージ送信のトリガー、およびユーザーのセグメント化に使用できます。

詳細については、[ネストされたオブジェクト]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/)の専用ページを参照してください。

## カスタムイベントプロパティの保存

カスタムイベントプロパティは、ターゲティングの精度を高め、メッセージのパーソナライゼーションをさらに向上させるために設計されています。カスタムイベントプロパティは、短期および長期のいずれでも Braze 内に保存できます。

イベントプロパティの値に基づいてセグメント化するには、次の方法があります。

- **30日以内:** Braze のセグメント内で、特定のイベントプロパティ値の頻度と最新性に基づいたイベントプロパティセグメンテーションを利用できます。このオプションはデータ使用量に影響します。<br><br>
- **30日以内およびそれ以降:** 短期と長期の両方のイベントプロパティセグメンテーションに対応するために、[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)を使用できます。この機能は、過去2年間に追跡されたカスタムイベントとイベントプロパティに基づいてユーザーをセグメント化します。このオプションはデータ使用量に影響しません。<br><br>
- **カスタム属性配列を使用したキャンバス:** カスタムイベントでトリガーされるキャンバスを構築して起動します。**ユーザー更新**ステップを設定し、**アイテムを追加**を使用してイベントプロパティをユーザープロファイルのカスタム属性配列に追加します。その後、イベントプロパティフィルターではなく、そのカスタム属性配列のフィルターを使用してユーザーをセグメント化します。このオプションは、カスタム属性配列への各更新がデータポイントを消費するため、データ使用量に影響します。実装の詳細については、[キャンバスのユーザー更新ステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)および[カスタム属性配列]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/#arrays)を参照してください。

お客様の特定のニーズに応じた最適なアプローチについては、Braze カスタマーサクセスマネージャーにお問い合わせください。