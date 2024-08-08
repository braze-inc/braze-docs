---
nav_title: 解約予測
article_title: 解約予測
page_order: 6.4
layout: dev_guide
alias: /predictive_churn/
search_rank: 2
guide_top_header: "解約予測"
guide_top_text: "顧客離れは、顧客離職率や顧客損失とも呼ばれ、成長する企業が考慮すべき最も重要な指標の1つです。解約に対処するための適切なツールを持つことは、損失を最小限に抑え、顧客維持を最大化するために重要です。このような解約の可能性があるユーザーをすぐに獲得するために、Brazeは予測解約を提供し、将来の解約を最小限に抑えるためのプロアクティブなアプローチを提供します。"
description: "このランディングページでは、ビジネスにとっての解約の意味と、解約を防ぎたいユーザーを定義できるツールである予測解約について説明します。"

guide_featured_title: "トピック"
guide_featured_list:
- name: Creating A Churn Prediction
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_churn/creating_a_churn_prediction/
  fa_icon: fas fa-cogs
- name: Prediction Analytics
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_churn/prediction_analytics/
  fa_icon: fas fa-chart-bar
- name: Messaging Users
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_churn/messaging_users/
  fa_icon: fas fa-arrow-right
- name: Troubleshooting
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_churn/prediction_faq/
  fa_icon: fas fa-question

---

## 概要

![チャーンの概要には、履歴データを使用したトレーニングによる過去の予測対象ユーザーが含まれます。これは、今日の予測対象者を解約リスクスコアで測定することにより、将来の解約のリスクの予測に貢献します。[1]

> 予測チャーンを使用すると、チャーンがビジネスにとって何を意味するか([チャーンの定義]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn))と、チャーンを防ぐユーザー([予測オーディエンス]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience))を定義できます。予測を作成すると、Brazeは [勾配ブーストデシジョンツリー](https://en.wikipedia.org/wiki/Gradient_boosting) を使用して機械学習モデルをトレーニングし、定義に従って解約したユーザーとしなかった過去のユーザーのアクティビティパターンから学習することで、解約のリスクがあるユーザーを特定します。

予測モデルが構築されると、予測対象ユーザーのユーザーには、定義に従って解約する可能性を示す 0 から 100 までの [解約リスク スコア]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_analytics/#churn_score) が割り当てられます。スコアが高いほど、ユーザーが解約する可能性が高くなります。 

予測対象ユーザーのリスクスコアの更新は、 [選択した頻度]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions)で行うことができます。こうすることで、解約のリスクがあるユーザーに実際に手を差し伸べる前に手を差し伸べ、そもそも解約が起こらないようにすることができます。最大 3 つのアクティブな予測を使用して、予測チャーンを活用して個々のモデルを調整し、最も価値があると見なされるユーザーの特定のセグメント内での離脱を防ぐことができます。

## アクセス予測チャーン

**予測ページ**は、**分析**セクションにあります。フルアクセスについては、アカウントマネージャーにお問い合わせください。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、[**エンゲージメント]** の下に **[予測**] があります。
{% endalert %}

この機能を購入する前は、プレビューモードで利用できます。これにより、合成データを使用してデモのチャーン予測を確認し、ユーザーデータに基づいて一度に1つのチャーン予測モデルを作成できます。このプレビューでは、チャーン リスクに応じてメッセージングのターゲットをユーザーに設定することはできず、作成後に定期的に更新されることはありません。

プレビューでは、1 つの予測を編集して再構築したり、アーカイブして別の予測を作成したりして、さまざまな[定義]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn)の予想される[予測品質]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/)をテストすることもできます。

<br><br>

[1]: {% image_buster /assets/img/churn/churn_overview.png %}
