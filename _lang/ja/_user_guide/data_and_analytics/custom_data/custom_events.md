---
nav_title: カスタムイベント
article_title: カスタムイベント
page_order: 9
page_type: reference
description: "この記事では、カスタムイベントとプロパティ、セグメンテーション、使用法、キャンバスエントリのプロパティ、関連する分析が表示される場所などについて説明します。"
search_rank: 2
---

# [![Braze ラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}カスタムイベント

> この記事では、カスタムイベントとプロパティ、関連するセグメンテーションフィルタ、キャンバスエントリプロパティ、関連する分析などについて説明します。Braze のイベント全般については、「[イベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/events)」を参照してください。

カスタムイベントとは、ユーザーによって実行されたアクションまたはユーザーに関する更新です。カスタムイベントがログに記録されると、任意の数とタイプのフォローアップキャンペーンをトリガできます。その後、[セグメンテーションフィルタ](#segmentation-filters) を使用して、最近の発生頻度とカスタムイベントの発生頻度に基づいてユーザーをセグメンテーションできます。これにより、カスタムイベントは、アプリケーション内の高価値のユーザーインタラクションの追跡に最適です。

## ユースケース

一般的なカスタムイベントのユースケースをいくつか示します。
- [アクションベースの配信]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) を使用したカスタムイベントに基づくキャンペーンまたはキャンバスのトリガ
- ユーザがカスタムイベントを実行した回数、イベントが最後に発生した時刻、および同様の方法でユーザをセグメント化する
- ダッシュボード[カスタムイベント分析]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-event-analytics) を使用して、各イベントが発生した頻度の集計を表示する
- [ファンネル]({{site.baseurl}}/user_guide/data_and_analytics/reporting/funnel_reports/#step-2-select-events-for-funnel-steps) および[retention]({{site.baseurl}}/user_guide/data_and_analytics/reporting/retention_reports/) レポートを使用した追加の分析の検索
- [永続的なエントリプロパティ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/)を活用し、キャンバスステップで顧客イベントのメタデータをパーソナライゼーションに使用します。
- [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents) を使用してより高度な分析を行う
- キャンバスの次のステップに進まない場合を定義するためのキャンバス[例外イベント]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events#canvas-exception-events)の設定

## カスタムイベントの管理

ダッシュボードでカスタムイベントを管理、作成、またはブロックリストするには、**データ設定** > **カスタムイベント**と移動します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、**カスタムイベント**は**設定の管理**にあります。
{% endalert %}

次のアクションのカスタムイベントの横にあるメニューを選択します。

### ブロックリスト

アクションメニューを使用して個別のカスタムイベントをブロックリストすることも、一括で最大10 個のイベントを選択してブロックリストすることもできます。 

カスタムイベントをブロックする場合:

- そのイベントの将来のデータは収集されません。
- 既存のデータは、そのイベントがブロック解除されない限り使用できません。
- そのイベントはフィルタやグラフには表示されません。

さらに、ブロックされたカスタムイベントが、現在、ブレーズの他の領域のフィルタまたはトリガによって参照されている場合、それを参照するフィルタまたはトリガのすべてのインスタンスが削除され、アーカイブされることを示す警告モードが表示されます。

### 説明を加える

`Manage Events, Attributes, Purchases` [ユーザー権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)がある場合は、作成後にカスタムイベントに説明を追加できます。カスタムイベントの [**説明を編集**] を選択し、チームへのメモなど好きなものを入力します。

## タグを追加する

"Manage Events, Attributes, Purchases" [user permission]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) がある場合は、作成後にカスタムイベントにタグを追加できます。タグは、イベントのリストをフィルタリングするために使用できます。 

{% alert important %}
この機能は現在早期アクセス段階です。この早期アクセスへ参加することに興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

### 利用レポートを見る

使用状況レポートには、特定のカスタムイベントを使用しているすべてのキャンバス、キャンペーン、およびセグメントが一覧表示されます。このリストには、Liquid の使用状況は含まれていません。 

複数のカスタムイベントのチェックボックスを選択し、**使用状況レポートの表示**を選択することで、一度に最大10件の使用状況レポートを表示できます。

## データのエクスポート

カスタムイベントのリストをCSV ファイルとしてエクスポートするには、ページ上部の**Export all** ボタンを選択します。CSVファイルが生成され、ダウンロードリンクがEメールで送信される。

{% alert important %}
この機能は現在早期アクセス段階です。この早期アクセスへ参加することに興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## カスタムイベントのログ記録

カスタムイベントには追加の設定が必要です。各プラットフォームに関するドキュメントについては、以下のリストを参照してください。ここでは、カスタムイベントのログ記録に使用される方法、およびカスタムイベントにプロパティと数量を追加する方法について説明します。

{% details プラットフォーム別のドキュメントの拡張 %}

- [Android と FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_custom_events/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_custom_events/)

{% enddetails %}

## カスタムイベントの保存

カスタムイベントのメタデータ (最初 / 最後の発生日時、合計数、30日間にわたる Y の X) を含む、**ユーザープロファイル**に保存されているすべてのデータは、各プロファイルが[アクティブ]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users)である限り無期限に保持されます。

## セグメンテーションフィルター

次の表に、ユーザーのカスタムイベント別セグメンテーションに使用できるフィルターを示します。

| セグメンテーションオプション | ドロップダウン・フィルター | 入力オプション |
| ---------------------| --------------- | ------------- |
| カスタムイベントが**X回以上**発生したかどうかをチェックする | **より大きい** | **数値** |
| カスタムイベントの発生**回数がX回未満か**どうかをチェックする | **未満** | **数値** |
| カスタムイベントが**正確にX回**発生したかどうかをチェックする | **正確に一致** | **数値** |
| カスタムイベントが **日付 X より後**に発生したかどうかをチェックする | **導入後** | **時間** |
| カスタムイベントが**日付 X より前**に発生したかどうかをチェックする | **前** | **時間** |
| カスタムイベントが最後に発生したのが**X日以上前か**どうかをチェックする | **より大きい** | **過去の日数**（正の数） |
| カスタムイベントが最後に発生したのが**X日以内か**どうかをチェックする | **未満** | **過去の日数**（正の数） |
| カスタムイベントが**X(Max = 50)回以上**発生したかどうかをチェックする。 | **より大きい** | 過去**Y日間 (Y = 1,3,7,14,21,30)** |
| カスタムイベントが**X (最大 = 50) 回未満**発生したかどうかを確認する | **未満** | 過去**Y日間 (Y = 1,3,7,14,21,30)** |
| カスタムイベントが**正確に X (最大 = 50) 回**発生したかどうかを確認する | **正確に一致** | 過去**Y日間 (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 分析

Braze はセグメンテーション用として、カスタムイベントが発生した回数と、各ユーザーの最終実行時刻を記録します。**Analytics**> **カスタムイベントレポート**に移動して、これらの分析を表示します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、**カスタムイベント**レポートの下に**データ**があります。
{% endalert %}

ダッシュボードの**Custom Events Report** ページで、各カスタムイベントの発生頻度を集約して表示できます。時系列にオーバーレイされた灰色の線は、キャンペーンが最後に送信された時刻を示します。これは、キャンペーンがカスタムイベントアクティビティにどのような影響を与えたかを表示するのに役立ちます。

![ダッシュボードの [カスタムイベント] ページのカスタムイベント数グラフ (カスタムイベントの傾向を示す)][8]

**フィルター**を使用して、カスタムイベントを時間、月間平均ユーザー数 (MAU)、セグメント、または KPI 式別に分類することもできます。 

![カスタムイベントのグラフフィルター][9]{: style="max-width:40%;"}

{% alert tip %}
[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers) をインクリメントして、カスタムイベントに似たユーザアクションのカウンタを保持します。ただし、カスタム属性データを時系列で表示することはできません。時系列で分析する必要のないユーザーアクションは、この方法を使用して記録する必要があります。
{% endalert %}

### カスタムイベント分析が表示されない理由

カスタムイベントデータを使用して作成されたセグメントでは、作成前の履歴データを表示できません。

## カスタムイベントプロパティ

カスタムイベントプロパティは、イベントの特定の発生を表すカスタムイベントのメタデータまたは属性です。したがって、これらのプロパティを使用して、トリガー条件の絞り込み、メッセージングのパーソナライゼーションの強化、コンバージョンの追跡、生工データのエクスポートによるより高度な分析の生成ができます。

カスタムイベントプロパティはブレーズプロファイルに保存されないため、データポイントを消費しません(例外については[データポイント](#data-points)を参照)。

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
| オブジェクト | オブジェクトは文字列として取り込まれる。 |
| ネストされたオブジェクト | 他のオブジェクトの中にあるオブジェクト。詳細については、この記事の「[階層化オブジェクト](#nested-objects)」のセクションを参照してください。
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

配列またはオブジェクト値を含むイベントプロパティオブジェクトには、最大100 KB のイベントプロパティペイロードを設定できます。

カスタムイベントプロパティのデータ型は変更できますが、データの収集後に[データ型を変更]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/)した場合の影響に注意してください。

### カスタムイベントプロパティの使用

カスタムイベントプロパティを使用して、キャンペーントリガーの絞り込み、コンバージョンの追跡、メッセージングのパーソナライぜーションができます。

#### トリガーメッセージ

カスタムイベントプロパティを使用して、特定のキャンペーンまたはキャンバスの対象をさらに絞り込むことができます。たとえば、eコマースアプリケーションがあり、ユーザがカートを放棄したときにユーザにメッセージを送信する場合は、`cart value` というカスタムイベントプロパティを追加して、ターゲットオーディエンスを向上させ、キャンペーンのパーソナライゼーションを増やすことができます。

![放置カードのカスタムイベントプロパティフィルタ。2つのフィルターをAND演算子で組み合わせ、カート金額が100ドルから200ドルの間にあるカードを放棄したユーザーにこのキャンペーンを送信する。][16]

階層化されたカスタムイベントプロパティは [アクションベースの配信][19] でもサポートされています。

![放置カードのカスタムイベントプロパティフィルタ。カート内のいずれかの商品価格が 100 ドルを超える場合は、1 つのフィルターが選択されます。][20]

#### メッセージのパーソナライゼーション

カスタムイベントプロパティは、メッセージングテンプレート内でパーソナライゼーションに使用することもできます。トリガーイベントを持つ[アクションベースの配信][19] ]を使用するすべてのキャンペーンは、メッセージングパーソナライゼーションのために、そのイベントからカスタムイベントプロパティを使用することができる。

たとえば、ゲームアプリがあり、レベルを完了したユーザーにメッセージを送信する場合、ユーザーがそのレベルを完了するのにかかった時間のために、プロパティを使用してメッセージをさらにパーソナライズできます。この例では、[条件付きロジック][18]]を使って、3つの異なるセグメントに対してメッセージをパーソナライズしている。カスタムイベントプロパティ `time_spent` は、``{% raw %} {{event_properties.${time_spent}}} {% endraw %}`` を呼び出すことでメッセージに含めることができます。

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

カスタムイベントのイベントプロパティは、それを使用するすべてのセグメントでリアルタイムに更新されます。プロパティを管理するには、**Data Settings** > **Custom Events**に移動し、関連付けられたカスタムイベントに対して**Manage Properties**を選択します。特定のセグメントフィルターで使用されるカスタムイベントプロパティの最大遡及履歴は 30 日間です。

{% alert note %}
イベントプロパティの新近性と頻度に基づいてセグメントを作成したい場合は、特定のカスタムイベントプロパティのセグメンテーションを有効にするように、カスタマーサクセスマネージャーに依頼してください。有効にすると、セグメンテーション時に追加のフィルターオプションにアクセスできます。
{% endalert %}

イベントプロパティセグメンテーションフィルターには次のようなものがあります。

- 過去 Y 日間に、値 B のプロパティ A を持つカスタムイベントを X 回実行した。
- 過去 Y 日間に、値 B のプロパティ A を持ついずれかの購入を行った。
- 1、3、7、14、21、30 日以内に、セグメントに加えられる条件を満たした。

![][3]

特定のイベントプロパティのデータは、カスタマーサクセスマネージャーによって有効にされた後にのみ記録されます。イベントプロパティは、その日付以降にのみ利用可能です。

##### データポイント

サブスクリプションの使用に関して、以下のフィルターでのセグメンテーション用に有効になっているカスタムイベントプロパティは、カスタムイベント自体でカウントされるデータポイントに加えて、すべて個別のデータポイントとしてカウントされます。

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### キャンバスエントリのプロパティとイベントプロパティ

キャンバスのユーザージャーニーで `canvas_entry_properties` と `event_properties` を使用できます。詳細と例については、[キャンバスのエントリプロパティとイベントプロパティ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/)を参照してください。

{% tabs local %}
{% tab キャンバスエントリのプロパティ %}

[キャンバスエントリのプロパティ]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)は、アクションベースまたは API でトリガーされるキャンバスにマップするプロパティです。`canvas_entry_properties` オブジェクトのサイズ上限は 50 KB であることに注意してください。

{% alert note %}
特にアプリ内メッセージチャネルでは、以前の早期アクセスの一環として元のエディターで永続的なエントリプロパティを有効にしている場合、キャンバスフローと元のキャンバスエディターでのみ `canvas_entry_properties` を参照できます。
{% endalert %}

キャンバスフローメッセージングでは、いずれのメッセージステップでも `canvas_entry_properties` を Liquid 形式 (``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``) で使用できます。このように使用するには、イベントがカスタムイベントまたは購入イベントでなければならないことに注意してください。 

#### ユースケース

{% raw %}
小売店である RetailApp に対してリクエスト `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}` があるとします。RetailApp では、Liquid `{{canvas_entry_properties.${product_name}}}` を使用して、メッセージに製品名 (shoes) を取り込むことができます。
{% endraw %}

RetailApp は、ユーザーが購入イベントをトリガーした後に、キャンバス内の異なる `product_name` プロパティに対して特定のメッセージをトリガーして送信することもできます。たとえば、次の Liquid をメッセージステップに追加することで、靴を購入したユーザーと別のものを購入したユーザーに異なるメッセージを送ることができます。

{% raw %}
```markdown
{% if  {{canvas_entry_properties.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details 元のキャンバスエディターの拡張 %}

2023 年 2 月 28 日以降、元のエディターを使用したキャンバスの作成や複製はできなくなりました。このセクションは参照のみを目的としています。

元のエディターで作成されたキャンバスの場合、`canvas_entry_properties` はキャンバスの最初のフルステップでのみ参照できます。

{% enddetails %}
{% endtab %}

{% tab イベントのプロパティ %}

{% alert important %}
`event_properties` は先頭のメッセージステップで使用できません。代わりに、`canvas_entry_properties` を使用するか、`event_properties` を含むメッセージステップの**前**に、対応するイベントを含むアクションパスを追加する必要があります。
{% endalert %}

イベントプロパティとは、カスタムイベントと購入に設定したプロパティを指します。これらの `event_properties` は、アクションベースの配信やキャンバスを含むキャンペーンで使用できます。

キャンバスフローでは、カスタムイベントと購入イベントのプロパティを、アクションパスステップに続く任意のメッセージステップで Liquid で使用できます。これらの `event_properties` を参照する場合は、必ず{% raw %} ``{{event_properties.${property_name}}}``{% endraw %} を使用してください。メッセージコンポーネントでこのように使用するには、これらのイベントがカスタムイベントまたは購入イベントである必要があります。

アクションパスに続く最初のメッセージステップでは、そのアクションパスで参照されるイベントに関連する `event_properties` を使用できます。これらの `event_properties` は、ユーザーが実際にアクションを実行した場合 (その他のユーザーグループに移動していない) にのみ使用できます。このアクションパスとメッセージステップの間に、他のステップ (別のアクションパスやメッセージステップではない) があってもかまいません。

{% details 元のキャンバスエディターの拡張 %}

2023 年 2 月 28 日以降、元のエディターを使用したキャンバスの作成や複製はできなくなりました。このセクションは参照のみを目的としています。

元のキャンバスエディターでは、スケジュールされたフルステップで `event_properties` を使用できません。ただし、アクションベースのキャンバスの最初のフルステップでは、フルステップがスケジュールされている場合でも `event_properties` を使用できます。

{% enddetails %}

{% endtab %}
{% endtabs %}

### 階層化オブジェクト {#nested-objects}

階層化オブジェクト (他のオブジェクト内にあるオブジェクト) を使用すると、カスタムイベントや購入のプロパティとして階層化された JSON データを送信できます。この階層化されたデータは、メッセージ内のパーソナライズされた情報のテンプレート作成、メッセージ送信のトリガー、およびユーザーのセグメント化に使用できます。

詳細については、[ネストされたオブジェクト]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/nested_objects/)の専用ページを参照してください。

## カスタムイベントプロパティの保存

カスタムイベントプロパティは、ターゲティングの精度を高め、メッセージのパーソナライゼーションの印象を高めるように設計されています。カスタムイベントプロパティは、短期および長期のいずれでも Braze 内に保存できます。

イベントプロパティの値に基づいてセグメント化するには、次の2 つの方法があります。

1. **30 日以内:**Braze サポート担当者は、Braze のセグメント内にある特定のイベントプロパティ値の頻度と新近度に基づいて、イベントプロパティのセグメンテーションができます。セグメント内のイベントプロパティを活用したい場合は、Braze アカウントエグゼクティブまたはカスタマーサクセスマネージャーにお問い合わせください。このオプションは、データの使用に影響を与えます。<br><br>
2. **30 日以内およびそれ以降:**短期と長期の両方のイベントプロパティセグメンテーションに対応する目的で、[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)を使用できます。この機能は、過去2 年間に追跡されたカスタムイベントとイベントプロパティに基づいてユーザーをセグメント化します。このオプションは、データの使用には影響しません。

お客様の特定のニーズに応じた最適なアプローチの推奨事項については、Braze カスタマーサクセスマネージャーにお問い合わせください。

[1]: {% image_buster /assets/img/nested_object1.png %}
[2]: {% image_buster /assets/img/nested_object2.png %}
[3]: {% image_buster /assets/img/nested_object3.png %}
[4]: {% image_buster /assets/img_archive/nested_event_properties_segmentation.png %}
[5]: {% image_buster /assets/img_archive/nested_event_properties_personalization.png %}
[6]: {% image_buster /assets/img_archive/schema_generation_example.png %}
[8]: {% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[9]: {% image_buster /assets/img/custom_events_report_filters.png %}
[16]: {% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png"
