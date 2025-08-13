---
nav_title: 解約予測
article_title: 解約予測
description: "このランディングページでは解約予測というツールについて説明します。これを使用すると、御社にとって解約の意味と、解約を防止する対象のユーザーを定義できます。"
page_order: 2.0
alias: /predictive_churn/
search_rank: 2
---

# 解約予測

> 解約予測を使用して、ビジネスにとっての解約とは何かを定義し、維持するユーザーを特定できます。予測を作成すると、Braze は解約したユーザーと解約しなかったユーザーの両方の過去の行動のパターンを分析してリスクのあるユーザーを認識するように、[勾配ブースティング決定木](https://en.wikipedia.org/wiki/Gradient_boosting)を使用して機械学習モデルをトレーニングします。

{% alert tip %}
詳細については、「[解約の定義]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn)」と「[予測対象ユーザー]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience)」を参照してください。
{% endalert %}

## 解約予測について

予測モデルが作成されると、定義した内容に従って解約の可能性を示す0～100の間の[解約リスクスコア]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/#churn_score)が予測対象ユーザーに割り当てられます。スコアが高いほど、ユーザーが解約する可能性が高くなります。 

予測対象ユーザーのリスクスコアの更新は、[選択した頻度]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions)で実行できます。これにより、実際に解約される前に、解約リスクのあるユーザーにリーチして解約を未然に防ぐことができます。最大 3 つのアクティブな予測を使用することで、解約予測を活用して個々のモデルをカスタマイズし、最も価値があると思われるユーザーからなる特定のセグメントでの解約防止に役立てることができます。

![解約の概要。過去の予測オーディエンスと、履歴データによるトレーニングを含みます。これは、現在の予測対象オーディエンスの解約リスクスコアを測定することにより、将来の解約リスクを予測するために役立ちます。]({% image_buster /assets/img/churn/churn_overview.png %})

## 解約予測へのアクセス

[**予測**] ページは [**分析**] セクションにあります。フルアクセスが必要な場合、アカウントマネージャーにお問い合わせください。

この機能は、購入前にプレビューモードで使用できます。これにより、合成データを使用した解約予測のデモを見ることができ、お客様のユーザーデータに基づいて、解約予測モデルを一度に 1 つ作成できます。このプレビューでは、解約リスクに応じてユーザーをメッセージングのターゲットにすることはできず、作成後に定期的に更新されることもありません。

このプレビューを使用すると、1つの予測を編集して再作成したり、アーカイブして他の予測を作成したりして、さまざまな[定義の]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn)[予測品質]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/)をテストできます。
