---
nav_title: 予測イベント
article_title: 予測イベント
page_order: 6.4
layout: featured
alias: /predictive_purchases/
search_rank: 1
guide_top_header: "予測イベント"
guide_top_text: "どのユーザーが特定のイベント (購入など) を実行する可能性が高いかを知ることは、ビジネスの成長にとって極めて重要なインサイトです。それがなければ、どのキャンペーンをどのように構築するかを決めるのだろうか。割引とプロモーションをどのユーザーに送信すべきか。限られた予算をどこで使うのか。Braze は、これらの質問に回答する支援をするために「予測イベント」 (旧称「購入予測」) を使用します。これは、エンゲージメントと収益最大化キャンペーンにリソースを集中させることができるよう、マーケティングチームが将来の行動を理解しやすくする機械学習モデルです。"
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

![How Predictive Events Works（予測イベントの仕組み）」と題されたグラフィックは、ユーザーデータが機械学習モデルに取り込まれる様子を示している。ラベルは「Train with historical data, compare the behavior of users who did perform the event in a certain period with those who didn't.」です。機械学習の結果が表示されます。ここでは、ユーザーがイベントを実行する可能性が最も低いものから昇順にランク付けされています。ラベルは「Predict likelihood of future events, assign a likelihood score to users for accurate, convenient targeting.」です。][1]

> 予測イベントは、マーケターが、イベントを実行する可能性に基づいてユーザーを特定し、メッセージを送るための強力なツールとなります。イベント予測を作成すると、Braze は[グラデーションブーストされた意思決定ツリー](https://en.wikipedia.org/wiki/Gradient_boosting) を使用して機械学習モデルをトレーニングし、以前のアクティビティから学習し、将来のアクティビティを予測します。

予測が作成されると、ユーザーには、選択したイベントを実行する可能性を示す[尤度スコア]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#purchase_score) 0 ～100 が割り当てられます。スコアが高いほど、ユーザーはそのイベントを実行する可能性が高くなります。また、ユーザは低、中、高の尤度カテゴリ別にソートされます。

予測イベントの本当の価値は、予測結果を使ってセグメンテーションやキャンペーンを行うことにある。マーケターは、**Prediction** ページで直接ターゲットを絞ったキャンペーンを構築して、すぐに収益を上げる結果を得たり、将来のキャンペーンやキャンバスのセグメントを保存したりできます。最初にどのユーザーをターゲットに設定すべきかがわからない場合は、[戦略的考慮事項]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/#strategy)を読み、可能性スコアに基づくユーザーのメッセージングについて学んでください。

## アクセス予測イベント

[**予測**] ページは [**分析**] セクションにあります。フルアクセスが必要な場合、アカウントマネージャーにお問い合わせください。

この機能を購入する前に、プレビューモードで使用できます。これにより、合成データを使用してデモ予測を表示したり、一度に1 つのプレビュー予測モデルを作成したりできます。この予測は、実際のユーザーデータに基づいて作成されますが、ユーザーの可能性スコアに従ってメッセージングのターゲットを設定することはできません。また、作成後も定期的に更新されません。

プレビューでは、この1 つの予測を編集して再構築したり、アーカイブしたりして、期待される[予測品質]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#prediction_quality) of [異なるオーディエンス]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/#audience) をテストし、アナリティクスに精通するように他のユーザを作成することもできます。

<br><br>

[1]: {% image_buster /assets/img/how_predictive_events_works.png %}

