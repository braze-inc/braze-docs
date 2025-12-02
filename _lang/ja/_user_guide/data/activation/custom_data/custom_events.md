---
nav_title: カスタムイベント
article_title: カスタムイベント
page_order: 9
page_type: reference
description: "この記事では、カスタムイベントとプロパティ、セグメンテーション、使用法、キャンバスエントリのプロパティ、関連する分析が表示される場所などについて説明します。"
search_rank: 2
---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}カスタムイベント

> この記事では、カスタムイベントとプロパティ、関連するセグメンテーションフィルタ、キャンバスエントリプロパティ、関連する分析などについて説明します。Braze のイベント全般については、「[イベント]({{site.baseurl}}/user_guide/data/custom_data/events/)」を参照してください。

カスタムイベントとは、ユーザーによって実行されたアクションまたはユーザーに関する更新です。カスタムイベントがログに記録されると、任意の数とタイプのフォローアップキャンペーンをトリガできます。その後、[セグメンテーションフィルタ](#segmentation-filters) を使用して、最近の発生頻度とカスタムイベントの発生頻度に基づいてユーザーをセグメンテーションできます。これにより、カスタムイベントは、アプリケーション内の高価値のユーザーインタラクションの追跡に最適です。

## ユースケース

一般的なカスタムイベントのユースケースをいくつか示します。

- [アクションベースの配信]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) を使用したカスタムイベントに基づくキャンペーンまたはキャンバスのトリガ
- ユーザがカスタムイベントを実行した回数、イベントが最後に発生した時刻、および同様の方法でユーザをセグメント化する
- ダッシュボード[カスタムイベント分析]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-event-analytics) を使用して、各イベントが発生した頻度の集計を表示する
- [ファンネル]({{site.baseurl}}/user_guide/data_and_analytics/reporting/funnel_reports/#step-2-select-events-for-funnel-steps) および[retention]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) レポートを使用した追加の分析の検索
- [永続的なエントリプロパティ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/)を活用し、キャンバスステップで顧客イベントのメタデータをパーソナライゼーションに使用します。
- [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) を使用してより高度な分析を行う
- ユーザーがキャンバスから退出するタイミングを定義する[退出基準の]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria)設定

## カスタムイベントの管理

ダッシュボードでカスタムイベントを管理、作成、またはブロックリストするには、**データ設定** > **カスタムイベント**と移動します。

次のアクションのカスタムイベントの横にあるメニューを選択します。

### ブロックリスト

アクションメニューから個々のカスタムイベントをブロックリストにすることも、最大100のイベントを一括で選択してブロックリストにすることもできる。 

カスタムイベントをブロックする場合:

- そのイベントの将来のデータは収集されません。
- 既存のデータは、そのイベントがブロック解除されない限り使用できません。
- そのイベントはフィルタやグラフには表示されません。

さらに、ブロックされたカスタムイベントが、現在、Braze の他の領域のフィルタまたはトリガによって参照されている場合、それを参照するフィルタまたはトリガのすべてのインスタンスが削除され、アーカイブされることを示す警告モードが表示されます。

### 説明を加える

`Manage Events, Attributes, Purchases` [ユーザー権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)がある場合は、作成後にカスタムイベントに説明を追加できます。カスタムイベントの [**説明を編集**] を選択し、チームへのメモなど好きなものを入力します。

## タグを追加する

"Manage Events, Attributes, Purchases" [user permission]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) がある場合は、作成後にカスタムイベントにタグを追加できます。タグは、イベントのリストをフィルタリングするために使用できます。

### 利用レポートを見る

使用状況レポートには、特定のカスタムイベントを使用しているすべてのキャンバス、キャンペーン、およびセグメントが一覧表示されます。このリストには、Liquid の使用状況は含まれていません。 

複数のカスタムイベントのチェックボックスを選択し、**使用状況レポートの表示**を選択することで、一度に最大100件の使用状況レポートを表示できます。

## データのエクスポート

カスタムイベントのリストをCSV ファイルとしてエクスポートするには、ページ上部の**Export all** ボタンを選択します。CSVファイルが生成され、ダウンロードリンクがEメールで送信されます。

## カスタムイベントのログ記録

カスタムイベントには追加の設定が必要です。各プラットフォームに関するドキュメントについては、以下のリストを参照してください。ここでは、カスタムイベントのログ記録に使用される方法、およびカスタムイベントにプロパティと数量を追加する方法について説明します。

{% details Expand for documentation by platform %}

- [Android と FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=unity)
- [.NET MAUI]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=roku)

{% enddetails %}

## カスタムイベントの保存

カスタムイベントのメタデータ (最初 / 最後の発生日時、合計数、30日間にわたる Y の X) を含む、**ユーザープロファイル**に保存されているすべてのデータは、各プロファイルが[アクティブ]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users)である限り無期限に保持されます。

## セグメンテーションフィルター

次の表に、ユーザーのカスタムイベント別セグメンテーションに使用できるフィルターを示します。

| セグメンテーションオプション | ドロップダウン・フィルター | 入力オプション |
| ---------------------| --------------- | ------------- |
| カスタムイベントが**X回以上**発生したかどうかをチェックする | **より超える** | **数値** |
| カスタムイベントの発生**回数がX回未満か**どうかをチェックする | **より少ない** | **数値** |
| カスタムイベントが**正確にX回**発生したかどうかをチェックする | **一致する** | **数値** |
| カスタムイベントが **日付 X より後**に発生したかどうかをチェックする | **特定の日より後** | **時間** |
| カスタムイベントが**日付 X より前**に発生したかどうかをチェックする | **特定の日より前** | **時間** |
| カスタムイベントが最後に発生したのが**X日以上前か**どうかをチェックする | **より大きい** | **過去の日数**（正の数） |
| カスタムイベントが最後に発生したのが**X日以内か**どうかをチェックする | **未満** | **過去の日数**（正の数） |
| カスタムイベントが**X(Max = 50)回以上**発生したかどうかをチェックする。 | **より後** | 過去**Y日間 (Y = 1,3,7,14,21,30)** |
| カスタムイベントが**X (最大 = 50) 回未満**発生したかどうかを確認する | **より少ない** | 過去 **Y 日間 (Y = 1、3、7、14、21、30)** |
| カスタムイベントが**正確に X (最大 = 50) 回**発生したかどうかを確認する | **一致する** | 過去 **Y 日間 (Y = 1、3、7、14、21、30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 分析

Braze はセグメンテーション用として、カスタムイベントが発生した回数と、各ユーザーの最終実行時刻を記録します。**Analytics**> **カスタムイベントレポート**に移動して、これらの分析を表示します。

ダッシュボードの**Custom Events Report** ページで、各カスタムイベントの発生頻度を集約して表示できます。時系列にオーバーレイされた灰色の線は、キャンペーンが最後に送信された時刻を示します。これは、キャンペーンがカスタムイベントアクティビティにどのような影響を与えたかを表示するのに役立ちます。

![カスタムイベントはカスタムイベントのトレンドを示すダッシュボードの s ページのグラフを数えます]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

**フィルター**を使用して、カスタムイベントを時間、月間平均ユーザー数 (MAU)、セグメント、または KPI 式別に分類することもできます。 

![カスタムイベントグラフフィルターs]({% image_buster /assets/img/custom_events_report_filters.png %}){: style="max-width:40%;"}

{% alert tip %}
[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers) をインクリメントして、カスタムイベントに似たユーザアクションのカウンタを保持します。ただし、カスタム属性データを時系列で表示することはできません。時系列で分析する必要のないユーザーアクションは、この方法を使用して記録する必要があります。
{% endalert %}

### カスタムイベント分析が表示されない理由

カスタムイベントデータを使用して作成されたセグメントでは、作成前の履歴データを表示できません。

## カスタムイベントプロパティ

カスタムイベントプロパティは、イベントの特定の発生を表すカスタムイベントのメタデータまたは属性です。したがって、これらのプロパティを使用して、トリガー条件の絞り込み、メッセージングのパーソナライゼーションの強化、コンバージョンの追跡、生工データのエクスポートによるより高度な分析の生成ができます。

カスタムイベントプロパティはBraze プロファイルに保存されないため、データポイントを記録しません(例外については[データポイントs](#data-points)を参照)。

{% alert important %}
各カスタムイベントまたは購入には、最大 256 個の異なるカスタムイベントプロパティを設定できます。256 個を超えるプロパティを持つカスタムイベントまたは購入がログ記録された場合、最初の 256 個のみが取得されて使用できます。
{% endalert %}

### 必要なフォーマット

プロパティ値は、キーがプロパティ名、値がプロパティ値であるオブジェクトでなければなりません。プロパティ名は、255 文字以下の空でない文字列でなければならず、先頭にドル記号 (`$`) は使用できません。

プロパティ値は、次のデータ型のいずれでもかまいません。

| データ型 | 説明 |
| --- | --- |
| 数値 | [整数](https://en.wikipedia.org/wiki/Integer)または[浮動小数点数として](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| ブール値 | `true`または`false`の値。 |
| 日時 | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)または`yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式の文字列としてフォーマットされる。アレイ内ではサポートされていない。 |
| 文字列 | 255 文字以下。 |
| 配列 | 配列に日時を含めることはできない。 |
| ネストされたオブジェクト | 他のオブジェクトの中にあるオブジェクト。詳細については、この記事の「[階層化オブジェクト](#nested-objects)」のセクションを参照してください。
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

配列またはオブジェクト値を含むイベントプロパティオブジェクトには、最大100 KB のイベントプロパティペイロードを設定できます。

カスタムイベントプロパティのデータ型は変更できますが、データの収集後に[データ型を変更]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/)した場合の影響に注意してください。

### カスタムイベントプロパティの使用

カスタムイベントプロパティを使用して、キャンペーントリガーの絞り込み、コンバージョンの追跡、メッセージングのパーソナライぜーションができます。

#### トリガーメッセージ

カスタムイベントプロパティを使用して、特定のキャンペーンまたはキャンバスの対象をさらに絞り込むことができます。例えば、eコマース・アプリケーションを持っていて、ユーザーがカートを放棄したときにメッセージを送りたい場合、`item price` のカスタムイベントプロパティを追加することで、ターゲットオーディエンスを改善し、キャンペーンのパーソナライゼーションを高めることができる。

![放棄されたカードのカスタムイベントプロパティフィルター。2 つのフィルターs をAND 演算子と組み合わせて、このキャンペーンを100 ～200 ドルのアイテム価格でカードを放棄したユーザーに送信します]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png")

階層化されたカスタムイベントプロパティは[アクションベースの配信]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)でもサポートされています。

![放棄されたカードのカスタムイベントプロパティフィルター。カート内のいずれかの商品価格が 100 ドルを超える場合は、1 つのフィルターが選択されます。]({% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png")

#### メッセージのパーソナライゼーション

カスタムイベントプロパティは、メッセージングテンプレート内でパーソナライゼーションに使用することもできます。トリガーイベントを持つ[アクションベース配信]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)を使用するキャンペーンは、メッセージングパーソナライゼーションのために、そのイベントのカスタムイベントプロパティを使用することができます。

たとえば、ゲームアプリがあり、レベルを完了したユーザーにメッセージを送信する場合、ユーザーがそのレベルを完了するのにかかった時間のために、プロパティを使用してメッセージをさらにパーソナライズできます。この例では、メッセージは[条件付きロジック]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/)を使用して3つの異なるセグメントに対してパーソナライズされています。カスタムイベントプロパティ `time_spent` は、``{% raw %} {{event_properties.${time_spent}}} {% endraw %}`` を呼び出すことでメッセージに含めることができます。

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
ユーザにインターネット接続がない場合、テンプレート化されたカスタムイベントプロパティ(たとえば、{% raw %}``{{event_properties.${time_spent}}}``{% endraw %})を持つトリガされたアプリ内メッセージは失敗し、表示されません。
{% endalert %}

アプリ内メッセージをテンプレート化したアプリ内メッセージとして配信するための Liquid タグの完全なリストについては、[よくある質問]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/faq/#what-are-templated-in-app-messages/)を参照してください。

##### フィルターに関する考慮事項

- **API 呼び出し:**API 呼び出しを行い、かつ「空白」フィルターを使用する場合、呼び出しから除外されたカスタムイベントプロパティは「空白」と見なされます。例えば、`"event_property": ""` を含めた場合、ユーザーは「空白でない」と見なされます。
- **整数:**数値のカスタムイベントプロパティにフィルターを適用するときに、値が非常に大きい場合は、「完全一致」フィルターを使用しないでください。数値が大きすぎると特定の長さに丸められ、フィルターが意図どおりに機能しないことがあります。

#### セグメンテーション

イベントプロパティセグメンテーションを使用して、取得されたカスタムイベントと、それらのイベントに関連付けられたプロパティに基づいて、ターゲットユーザを対象にします。これにより、購入イベントとカスタムイベントでセグメンテーションを行うときのフィルタリングオプションが増えます。

カスタムイベントのイベントプロパティは、それを使用するすべてのセグメントでリアルタイムに更新されます。プロパティの管理は、「**データ設定**」＞「**カスタムイベント**」と進み、関連するカスタムイベントの**「プロパティの管理**」を選択することで行える。特定のセグメントフィルターで使用されるカスタムイベントプロパティの最大遡及履歴は 30 日間です。

##### セグメンテーションのためにイベントプロパティを追加する。

イベントプロパティの再帰性と頻度に基づいてセグメンテーションを作成するには、「カスタムイベントプロパティのセグメンテーションを管理する」[ユーザー権限が]({{site.baseurl}}/user_guide/data/data_points/#viewing-data-point-usage)必要です。

デフォルトでは、1 つのワークスペースにつき 20 個のセグメンテーション可能なイベントプロパティを設定できます。この制限を増やすには、Brazeアカウントマネージャーに連絡する。

セグメンテーションのためにイベントプロパティを追加するには、以下のようにする：

1. カスタムイベントに移動し、[**プロパティを管理**] を選択します。
2. [**セグメンテーションを有効にする]** トグルを選択して、セグメンテーションのイベントプロパティを追加します。セグメンテーションの際に、追加のフィルターオプションにアクセスできる。

イベントプロパティセグメンテーションフィルターには次のようなものがあります。

- 過去 Y 日間に、値 B のプロパティ A を持つカスタムイベントを X 回実行した。
- 過去 Y 日間に、値 B のプロパティ A を持ついずれかの購入を行った。
- 1～30日以内のセグメンテーション機能を追加。

![Abandoned Cart' があり、プロパティが「itmes の数」で、過去30 暦日の1 回より2 回以上の値が設定されているフィルター群。]({% image_buster /assets/img/nested_object3.png %})

特定のイベントプロパティのデータは、カスタマーサクセスマネージャーによって有効にされた後にのみ記録されます。イベントプロパティは、その日付以降にのみ利用可能です。

##### データポイント

サブスクリプションの使用に関して、以下のフィルターでのセグメンテーション用に有効になっているカスタムイベントプロパティは、カスタムイベント自体でカウントされるデータポイントに加えて、すべて個別のデータポイントとしてカウントされます。

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### キャンバスエントリのプロパティとイベントのプロパティ

{% multi_lang_include canvas_entry_event_properties.md %}

### 階層化オブジェクト {#nested-objects}

階層化オブジェクト (他のオブジェクト内にあるオブジェクト) を使用すると、カスタムイベントや購入のプロパティとして階層化された JSON データを送信できます。この階層化されたデータは、メッセージ内のパーソナライズされた情報のテンプレート作成、メッセージ送信のトリガー、およびユーザーのセグメント化に使用できます。

詳細については、[ネストされたオブジェクト]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/)の専用ページを参照してください。

## カスタムイベントプロパティの保存

カスタムイベントプロパティは、ターゲティングの精度を高め、メッセージのパーソナライゼーションの印象を高めるように設計されています。カスタムイベントプロパティは、短期および長期のいずれでも Braze 内に保存できます。

イベントプロパティの値に基づいてセグメント化するには、次の2 つの方法があります。

1. **30 日以内:**Braze サポート担当者は、Braze のセグメント内にある特定のイベントプロパティ値の頻度と新近度に基づいて、イベントプロパティのセグメンテーションができます。セグメント内のイベントプロパティを活用したい場合は、Braze アカウントエグゼクティブまたはカスタマーサクセスマネージャーにお問い合わせください。このオプションは、データの使用に影響を与えます。<br><br>
2. **30 日以内およびそれ以降:**短期と長期の両方のイベントプロパティセグメンテーションに対応する目的で、[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)を使用できます。この機能は、過去2 年間に追跡されたカスタムイベントとイベントプロパティに基づいてユーザーをセグメント化します。このオプションは、データの使用には影響しません。

お客様の特定のニーズに応じた最適なアプローチの推奨事項については、Braze カスタマーサクセスマネージャーにお問い合わせください。

