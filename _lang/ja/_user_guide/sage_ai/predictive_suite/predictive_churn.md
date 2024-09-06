---
nav_title: 解約予測
article_title: 解約予測
page_order: 6.4
layout: dev_guide
alias: /predictive_churn/
search_rank: 2
guide_top_header: "解約予測"
guide_top_text: "顧客離職率や顧客喪失率とも呼ばれる顧客離れは、成長企業にとって最も重要な指標の一つである。解約に対処するための適切なツールを持つことは、損失を最小限に抑え、顧客維持を最大化する上で極めて重要である。Brazeは、このような潜在的なユーザー離脱に先手を打つため、将来のユーザー離脱を最小限に抑えるプロアクティブアプローチを提供するPredictive Churnを提供している。"
description: "このランディングページでは、ビジネスにとっての解約とは何か、解約を防ぎたいユーザーを定義できるツール、Predictive Churnを取り上げる。"

guide_featured_title: "トピック"
guide_featured_list:
- name: 解約予測の作成
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_churn/creating_a_churn_prediction/
  image: /assets/img/braze_icons/settings-01.svg
- name: 予測分析
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_churn/prediction_analytics/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: ユーザーへのメッセージング
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_churn/messaging_users/
  image: /assets/img/braze_icons/arrow-narrow-right.svg
- name: トラブルシューティング
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_churn/prediction_faq/
  image: /assets/img/braze_icons/annotation-question.svg

---

## 概要

![解約の概要。過去のデータを使ったトレーニングによる過去の予測視聴者を含む。これは、今日の予測視聴者を解約リスクスコアで測定することで、将来の解約リスクを予測することに貢献する。][1]

> Predictive Churnでは、ビジネスにとっての解約とは何か[（解約定義]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn)）と、解約を防ぎたいユーザー[（予測対象者]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience)）を定義することができる。予測を作成すると、Brazeは[勾配ブースティング決定木を](https://en.wikipedia.org/wiki/Gradient_boosting)使用して機械学習モデルを訓練し、あなたの定義に従って解約したユーザーと解約しなかった過去のユーザーの活動パターンから学習して、解約リスクのあるユーザーを特定する。

予測モデルが構築されると、予測対象ユーザーには、あなたの定義に従って解約する可能性を示す0から100の間の[解約リスクスコア]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_analytics/#churn_score)が割り当てられます。スコアが高ければ高いほど、ユーザーが解約する可能性は高くなる。 

予測対象者のリスクスコアの更新は、[選択した頻度で]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions)行うことができる。こうすることで、実際に解約される前に、解約リスクのあるユーザーに接触し、解約を未然に防ぐことができる。最大3つのアクティブな予測を使用することで、Predictive Churnを活用して個々のモデルを調整し、最も価値があると思われるユーザーの特定のセグメントにおける解約防止を支援することができる。

## 解約予測にアクセスする

**予測」**ページは**「アナリティクス」**セクションにある。完全なアクセスについては、アカウント・マネージャーに連絡すること。

{% alert note %}
古いナビゲーション を使用している場合は、\[**エンゲージメント**] の下に \[[位置情報]({{site.baseurl}}/navigation)] が表示されます。
{% endalert %}

この機能を購入する前に、プレビュー・モードで利用できる。これにより、合成データを使った解約予測のデモを見ることができ、ユーザーデータに基づいて解約予測モデルを一度に1つ作成することができる。このプレビューでは、解約リスクに応じてユーザーをメッセージングのターゲットにすることはできず、作成後も定期的に更新されることはない。

プレビューを使えば、1つの予測を編集して再構築したり、アーカイブして他の予測を作成し、異なる[定義の]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn) [予測品質を]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/)テストすることもできる。

<br><br>

[1]: {% image_buster /assets/img/churn/churn_overview.png %}
