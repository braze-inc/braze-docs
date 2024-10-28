---
nav_title: 解約予測
article_title: 解約予測
page_order: 6.4
layout: dev_guide
alias: /predictive_churn/
search_rank: 2
guide_top_header: "解約予測"
guide_top_text: "顧客解約は、顧客回転率や顧客喪失とも呼ばれ、成長する企業にとって最も重要な指標の 1 つです。解約を最小限に抑え、カスタマーリテンションを最大限に引き出すためには、解約に対処する適切なツールが不可欠です。Braze には、このような潜在的なユーザー離脱に先手を打つため、将来のユーザー離脱を最小限に抑えるプロアクティブアプローチを提供する「解約予測」という機能が用意されています。"
description: "このランディングページでは解約予測について説明します。これは、貴社にとって解約予測の意味と、解約予測を防止したいユーザーを定義するためのツールです。"

guide_featured_title: "トピック"
guide_featured_list:
- name: 解約予測を立てる
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/
  image: /assets/img/braze_icons/settings-01.svg
- name: 予測分析
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: ユーザーへのメッセージング
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/
  image: /assets/img/braze_icons/arrow-narrow-right.svg
- name: トラブルシューティング
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/prediction_faq/
  image: /assets/img/braze_icons/annotation-question.svg

---

## 概要

![解約の概要。過去のデータによるトレーニングで過去の予測対象ユーザーを含む。これは、解約リスクスコアを用いて現在の予測オーディエンスを測定することにより、将来の解約リスクを予測するのに役立ちます。][1]

> 解約予測では、ビジネスにとって解約が意味するもの ([解約の定義]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn)) と、解約を防ぎたいユーザー ([予測対象ユーザー]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience)) を定義することができます。予測を作成すると、Brazeは[勾配ブースティング決定木を](https://en.wikipedia.org/wiki/Gradient_boosting)使用して機械学習モデルをトレーニングし、あなたの定義に従って解約したユーザーとしなかった過去のユーザーの活動パターンから学習して、解約リスクのあるユーザーを識別する。

予測モデルが構築されると、定義した内容に従って解約の可能性を示す 0 ～ 100 の間の[解約リスクスコア]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/#churn_score)が予測対象ユーザーに割り当てられます。スコアが高いほど、ユーザーが解約する可能性が高くなる。 

予測対象ユーザーのリスクスコアの更新は、[選択した頻度]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions)で行うことができます。こうすることで、実際に解約される前に、解約リスクのあるユーザーにリーチし、解約を未然に防ぐことができます。最大3つのアクティブユーザー予測を使用することで、Predictive Churnを活用して個々のモデルをカスタマイズし、最も価値があると思われるユーザーの特定のセグメンテーションにおける解約防止を支援することができる。

## 解約予測にアクセスする

\[**予測**] ページは \[**分析**] セクションにあります。フルアクセスが必要な場合、アカウントマネージャーにお問い合わせください。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**「** **エンゲージメント**」の下に**「予測」が**ある。
{% endalert %}

この機能を購入する前に、プレビュー・モードで利用できる。これにより、合成データを使った解約予測のデモを見ることができ、ユーザーデータに基づいて解約予測モデルを一度に1つ作成することができる。このプレビューでは、解約リスクに応じてユーザーをメッセージングのターゲットにすることはできず、作成後に定期的に更新されることもありません。

プレビューを使えば、1つの予測を編集して再構築したり、アーカイブして他の予測を作成し、異なる[定義の]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn) [予測品質を]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/)テストすることもできる。

<br><br>

[1]: {% image_buster /assets/img/churn/churn_overview.png %}
