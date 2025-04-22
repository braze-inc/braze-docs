---
nav_title: 解約予測
article_title: 解約予測
page_order: 6.4
layout: dev_guide
alias: /predictive_churn/
search_rank: 2
guide_top_header: "解約予測"
guide_top_text: "顧客解約は、顧客離れやクライアント喪失とも呼ばれ、成長する企業にとって考慮すべき最重要指標の 1 つです。解約を最小限に抑え、カスタマーリテンションを最大限に伸ばすためには、解約に対処する適切なツールが不可欠です。このような解約の可能性があるユーザーに先手を打つため、Braze には将来のユーザー解約を最小限に抑える積極的なアプローチを提供する「解約予測」という機能が用意されています。"
description: "このランディングページでは解約予測というツールについて説明します。これを使用すると、御社にとって解約の意味と、解約を防止する対象のユーザーを定義できます。"

guide_featured_title: "トピック"
guide_featured_list:
- name: 解約予測の作成
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

![解約の概要。過去の予測オーディエンスと、履歴データによるトレーニングを含みます。これは、現在の予測対象オーディエンスの解約リスクスコアを測定することにより、将来の解約リスクを予測するために役立ちます。][1]

> 解約予測では、御社にとって解約が意味するもの ([解約の定義]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn)) と、解約を防止する対象のユーザー ([予測対象ユーザー]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience)) を定義できます。お客様が予測を作成すると、Braze は[勾配ブースト決定木](https://en.wikipedia.org/wiki/Gradient_boosting)を使用して機械学習モデルをトレーニングし、お客様の定義に従って過去に解約したユーザーと解約しなかったユーザーのアクティビティパターンから学習させて、解約リスクのあるユーザーを特定します。

予測モデルが作成されると、定義した内容に従って解約の可能性を示す 0 ～ 100 の間の[解約リスクスコア]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/#churn_score)が予測対象ユーザーに割り当てられます。スコアが高いほど、ユーザーが解約する可能性が高くなります。 

予測対象ユーザーのリスクスコアの更新は、[選択した頻度]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions)で実行できます。これにより、実際に解約される前に、解約リスクのあるユーザーにリーチして解約を未然に防ぐことができます。最大 3 つのアクティブな予測を使用することで、解約予測を活用して個々のモデルをカスタマイズし、最も価値があると思われるユーザーからなる特定のセグメントでの解約防止に役立てることができます。

## 解約予測へのアクセス

[**予測**] ページは [**分析**] セクションにあります。フルアクセスが必要な場合、アカウントマネージャーにお問い合わせください。

この機能は、購入前にプレビューモードで使用できます。これにより、合成データを使用した解約予測のデモを見ることができ、お客様のユーザーデータに基づいて、解約予測モデルを一度に 1 つ作成できます。このプレビューでは、解約リスクに応じてユーザーをメッセージングのターゲットにすることはできず、作成後に定期的に更新されることもありません。

このプレビューを使用すると、1つの予測を編集して再作成したり、アーカイブして他の予測を作成したりして、さまざまな[定義の]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn)[予測品質]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/)をテストできます。

<br><br>

[1]: {% image_buster /assets/img/churn/churn_overview.png %}
