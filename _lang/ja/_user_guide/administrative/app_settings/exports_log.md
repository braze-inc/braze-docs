---
nav_title: エクスポートログ
article_title: エクスポートログ
page_order: 15
page_type: reference
description: "このページでは、エクスポート・ログについて説明します。エクスポート・ジョブのステータスを表示し、実行中のエクスポートをキャンセルすることができます。"
---

# エクスポートログ

> **Exports Log**ページを使用して、エクスポートジョブのステータスを表示し、Brazeプラットフォームから直接実行中のエクスポートをキャンセルします。<br><br> 現在、エクスポートログはセグメントエクスポートのみをサポートしています。セグメントエクスポートツールの詳細については、[セグメントデータを CSV にエクスポートする]({{site.baseurl}}/user_guide/data/export_braze_data/segment_data_to_csv/)を参照してください。

エクスポートログは、[**設定**] > [**エクスポートログ**] に移動して確認できます。ここでは、前のエクスポート、エクスポートされたセグメントの名前、各エクスポートのステータス、各エクスポートのソース、および各エクスポートが開始および終了した日時を表示できます。 

![エクスポートログと、完成したエクスポートのリスト。][1]

## 保留中のエクスポートのキャンセル

**Exports Log**ページから直接保留中のエクスポートをキャンセルするには、<i class="fas fa-ellipsis-vertical"></i>メニューを選択し、次に**Cancel Export**を選択するか、**Export ID**を選択して、エクスポートのページで**Cancel Export**を選択します。

![エクスポートログには、保留中のエクスポートと、"Cancel Export" オプションが表示されます。][2]

## 特定のエクスポートログの共有

**Export ID**を選択し、**Share Log**を選択して、エクスポートログを共有します。

![ページを共有するためのリンクを含むドロップダウンウィンドウ。][3]{: style="max-width:45%;"}

[1]: {% image_buster /assets/img/export_logs.png %}
[2]: {% image_buster /assets/img/export_logs_cancel.png %}
[3]: {% image_buster /assets/img/export_logs_share.png %}
