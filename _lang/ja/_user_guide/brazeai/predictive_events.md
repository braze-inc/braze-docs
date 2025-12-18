---
nav_title: 予測イベント
article_title: 予測イベント
description: "この記事では、マーケターがイベントを実行する可能性に基づいてユーザーを識別し、メッセージを送る機能を提供する、Braze Predictive SuiteのツールであるPredictive Events（旧Predictive Purchases）を取り上げる。"
page_order: 2.1
alias: /predictive_purchases/
search_rank: 1
---

# 予測イベント

> 予測イベントは、Braze Predictive Suiteの強力なツールで、イベントを実行する可能性に基づいてユーザーを識別し、メッセージングする。イベント予測を作成すると、Braze は[グラデーションブーストされた意思決定ツリー](https://en.wikipedia.org/wiki/Gradient_boosting) を使用して機械学習モデルをトレーニングし、以前のアクティビティから学習し、将来のアクティビティを予測します。

## 予測イベントについて

予測が作成されると、ユーザーには、選択したイベントを実行する可能性を示す、0 から 100 までの [尤度スコア]({{site.baseurl}}/user_guide/brazeai/predictive_events/prediction_analytics/#purchase_score) が割り当てられます。スコアが高いほど、ユーザーはそのイベントを実行する可能性が高くなります。また、ユーザは低、中、高の尤度カテゴリ別にソートされます。

予測イベントの本当の価値は、予測結果を使ってセグメンテーションやキャンペーンを行うことにある。マーケターは、**Prediction** ページで直接ターゲットを絞ったキャンペーンを構築して、すぐに収益を上げる結果を得たり、将来のキャンペーンやキャンバスのセグメントを保存したりできます。最初にどのユーザーをターゲットに設定すべきかがわからない場合は、[戦略的考慮事項]({{site.baseurl}}/user_guide/brazeai/predictive_events/messaging_users/#strategy)を読み、可能性スコアに基づくユーザーのメッセージングについて学んでください。

![How Predictive Events Works（予測イベントの仕組み）」と題されたグラフィックは、ユーザーデータが機械学習モデルに取り込まれる様子を示している。ラベルは「Train with historical data, compare the behavior of users who did perform the event in a certain period with those who didn't.」です。機械学習の結果が表示されます。ここでは、ユーザーがイベントを実行する可能性が最も低いものから昇順にランク付けされています。ラベルは「Predict likelihood of future events, assign a likelihood score to users for accurate, convenient targeting.」です。]({% image_buster /assets/img/how_predictive_events_works.png %})

## 予測イベントへのアクセス

[**予測**] ページは [**分析**] セクションにあります。フルアクセスが必要な場合、アカウントマネージャーにお問い合わせください。

この機能は、購入前にプレビューモードで使用できます。これにより、合成データを使用してデモ予測を表示したり、一度に1 つのプレビュー予測モデルを作成したりできます。この予測は、実際のユーザーデータに基づいて作成されますが、ユーザーの可能性スコアに従ってメッセージングのターゲットを設定することはできません。また、作成後も定期的に更新されません。

プレビューでは、この1 つの予測を編集して再構築したり、アーカイブしたりして、期待される[予測品質]({{site.baseurl}}/user_guide/brazeai/predictive_events/prediction_analytics/#prediction_quality) of [異なるオーディエンス]({{site.baseurl}}/user_guide/brazeai/predictive_events/creating_an_event_prediction/#audience) をテストし、アナリティクスに精通するように他のユーザを作成することもできます。
