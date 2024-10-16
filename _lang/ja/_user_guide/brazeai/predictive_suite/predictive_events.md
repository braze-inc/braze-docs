---
nav_title: 予測イベント
article_title: 予測イベント
page_order: 6.4
layout: featured
alias: /predictive_purchases/
search_rank: 1
guide_top_header: "予測イベント"
guide_top_text: "どのユーザーが特定のイベント(購入のような)を実行する可能性が高いかを知ることは、成長するビジネスにとって極めて重要な洞察です。それがなければ、どのキャンペーンをどのように構築するかを決めるのだろうか。誰が割引とプロモーションを受けるべきですか？限られた予算をどこで使うのか。Braze は、これらの質問にPredictive Events (以前はPredictive Purchases) で回答するのに役立ちます。これは、マーケティングチームが将来の行動を理解しやすくし、エンゲージメントと収益最大化キャンペーンにリソースを集中させる機械学習モデルです。"
description: "この記事では、予測イベント(以前はPredictive Purchases)について説明します。これは、マーケターがイベントを実行する可能性に基づいてユーザーを識別し、メッセージを送る機能を提供するツールです。"

guide_featured_title: "トピック"
guide_featured_list:
- name: 予測の作成
  link: /docs/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/
  image: /assets/img/braze_icons/settings-01.svg
- name: 予測分析
  link: /docs/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: ユーザーへのメッセージング
  link: /docs/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/
  image: /assets/img/braze_icons/arrow-narrow-right.svg

---

## 概要

![「"Predictive Events Works"」というタイトルのグラフィック。左側には、機械学習モデルに組み込まれているユーザデータが表示されます。ラベルは"Train と履歴データを読み取り、特定の期間にイベントを実行したユーザの動作を&quot 以外のユーザと比較します。右側には、機械学習の結果が表示されます。ここでは、ユーザがイベントを実行する可能性が最も低い順位にランク付けされています。ラベルは" Predict likely of future eventsを読み取り、正確で便利なターゲティングのために、ユーザに尤度スコアを割り当てます。][1]

> 予測イベントは、マーケターがイベントを実行する可能性に基づいてユーザーを識別し、メッセージを送るための強力なツールとなります。イベント予測を作成すると、Braze は[グラデーションブーストされた意思決定ツリー](https://en.wikipedia.org/wiki/Gradient_boosting) を使用して機械学習モデルをトレーニングし、以前のアクティビティから学習し、将来のアクティビティを予測します。

予測が作成されると、ユーザーには、選択したイベントを実行する可能性を示す[尤度スコア]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#purchase_score) 0 ～100 が割り当てられます。スコアが高いほど、ユーザーはそのイベントを実行する可能性が高くなります。また、ユーザは低、中、高の尤度カテゴリ別にソートされます。

予測イベントの実際の値は、予測結果を使用してセグメントまたはキャンペーンを作成することです。マーケターは、**Prediction** ページで直接ターゲットを絞ったキャンペーンを構築して、すぐに収益を上げる結果を得たり、将来のキャンペーンやキャンバスのセグメントを保存したりできます。誰が最初にターゲットにするのかわからない?メッセージングユーザの可能性スコアに基づいて、[戦略的考慮事項]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_purchases/messaging_users/#strategy)を読みます。

## アクセス予測イベント

\[**予測**] ページは \[**分析**] セクションにあります。フルアクセスが必要な場合、アカウントマネージャーにお問い合わせください。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、**Predictions**は**Engagement**にあります。
{% endalert %}

この機能を購入する前に、プレビューモードで使用できます。これにより、合成データを使用してデモ予測を表示したり、一度に1 つのプレビュー予測モデルを作成したりできます。この予測は、実際のユーザデータに基づいて作成されますが、ユーザの尤度スコアに従ってメッセージングをターゲットにすることはできません。また、作成後も定期的に更新されません。

プレビューでは、この1 つの予測を編集して再構築したり、アーカイブしたりして、期待される[予測品質]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#prediction_quality) of [異なるオーディエンス]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/#audience) をテストし、アナリティクスに精通するように他のユーザを作成することもできます。

<br><br>

[1]: {% image_buster /assets/img/how_predictive_events_works.png %}

