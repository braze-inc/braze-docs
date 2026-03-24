---
nav_title: レポートとインサイト
article_title: レポートとインサイト
description: "Braze で BrazeAI Decisioning Studio™ レポートを表示する方法について説明します。これにより、AI を活用した意思決定がキャンペーンにどのような影響を与えるかを理解できます。"
page_order: 3
---

# レポートとインサイト

> Braze で BrazeAI Decisioning Studio™ レポートを表示する方法について説明します。これにより、AI を活用した意思決定がキャンペーンにどのような影響を与えるかを理解できます。パフォーマンス指標からデータの健全性やシステムの変更まで、これらのレポートは結果の理解、問題のトラブルシューティング、そして確信を持った意思決定に役立ちます。

## 前提条件

Braze で Decisioning Studio レポートを表示するには、以下が必要です。

- Braze と BrazeAI Decisioning Studio™ のアクティブな契約があること。 
- カスタマーサクセスマネージャーに連絡して、BrazeAI Decisioning Studio™ を有効にしてもらうこと。
- ライブの BrazeAI Decisioning Studio™ エージェントがあること。

## レポートの表示 {#view}

Braze で Decisioning Studio エージェントの指標を表示するには、**AI Decisioning** > **BrazeAI Decisioning Studio™** に移動し、エージェントを選択します。

![BrazeAI Decisioning Studio™ のレポートホーム画面には、複数のレポートカードを表示するダッシュボードが表示されています。それぞれのカードには、パフォーマンス、インサイト、診断、タイムラインなどのレポートの種類が表示され、それぞれについて簡単な説明とアイコンが表示されています。]( {% image_buster /assets/img/decisioning_studio/reporting_home.png %} )

ここでは、パフォーマンス、インサイト、診断、タイムラインなどのレポートを表示できます。詳しくは、[利用可能なレポート](#available-reports)をご覧ください。

## レポート日付の変更

[レポートを開いた](#view)後に、カレンダードロップダウンから新しい開始日と終了日を選択することで、日付範囲を変更できます。

![BrazeAI Decisioning Studio™ の日付範囲セレクターが、カレンダーのドロップダウンメニューで開いています。カレンダーには、レポートビューをカスタマイズするための選択可能な開始日と終了日が表示されています。]({% image_buster /assets/img/decisioning_studio/reporting_change_date_range.png %}){: style="max-width:50%;"}

デフォルトの開始日を設定したり、常に除外する日付を選択したりすることもできます。除外された日付は、そのエージェントのすべてのレポートからフィルタリングされます。

日付を設定または除外するには、<i class="fa-solid fa-gear"></i>**設定**を選択し、デフォルトの日付を変更するか、必要に応じて日付を除外します。

![BrazeAI Decisioning Studio™ で開いた設定パネルには、デフォルトの開始日を設定するオプションと、レポートから特定の日付を除外するオプションが表示されています。パネルには、「デフォルトの開始日」および「除外日」というラベルの付いた 2 つのセクションが表示されています。「除外日」には、横にチェックボックスが付いたいくつかの日付が表示されています。]({% image_buster /assets/img/decisioning_studio/reporting_set_exclude_dates.png %})

## 利用可能なレポート {#available-reports}

- [パフォーマンス]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/performance/): トリートメントグループとコントロールグループを比較するハイレベルなエージェント指標です。**トレンド**と**ドライバーツリー**のビューがあります。
- [インサイト]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/insights/): アクションバンク内のおすすめオプションがどのように生成されるかを示します。エージェントの設定や SHAP レポートを含みます。
- [診断]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/diagnostics/): アウトバウンドおよびインバウンドのデータ健全性です。おすすめのボリュームやデータフィードの監視を含みます。
- [タイムライン]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/timeline/): 主要なイベント（エージェントの実行、設定変更、ガードレールの更新）をパフォーマンス指標と共に表示する視覚的な記録です。