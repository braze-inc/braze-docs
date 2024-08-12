---
nav_title: 予測イベント
article_title: 予測イベント
page_order: 6.4
layout: featured
alias: /predictive_purchases/
search_rank: 1
guide_top_header: "予測イベント"
guide_top_text: "どのユーザーが購入のような特定のイベントを実行する可能性が高いかを知ることは、成長企業にとって極めて重要なインサイトです。それがなければ、どのキャンペーンを作るかどうやって決めるのか？誰が割引やプロモーションを受けるべきか？限られた予算をどこに使うか？Brazeは、マーケティングチームが将来の行動を理解し、エンゲージメントと収益を最大化するキャンペーンにリソースを集中させることを容易にする機械学習モデルであるPredictive Events（旧Predictive Purchases）で、このような疑問に答えるお手伝いをします。"
description: "この記事では、マーケターがイベントを実行する可能性に基づいてユーザーを特定し、メッセージを送る機能を提供するツール、Predictive Events（旧Predictive Purchases）を取り上げます。"

guide_featured_title: "トピック"
guide_featured_list:
- name: Creating a Prediction
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_events/creating_an_event_prediction/
  fa_icon: fas fa-cogs
- name: Prediction Analytics
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_events/prediction_analytics/
  fa_icon: fas fa-chart-bar
- name: Messaging Users
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_events/messaging_users/
  fa_icon: fas fa-arrow-right

---

## 概要

予測イベントの仕組み」と題されたグラフィック。左側は、機械学習モデルに取り込まれるユーザーデータを示している。ラベルには、"過去のデータでトレーニングし、ある期間にイベントを実行したユーザーと実行しなかったユーザーの行動を比較する "と書かれている。 右側は機械学習の結果で、ユーザーがそのイベントを実行する可能性が低い順にランク付けされている。ラベルには「将来の出来事の可能性を予測し、正確で便利なターゲティングのためにユーザーに可能性スコアを割り当てる」と書かれている][1]。

> Predictive Eventsは、マーケティング担当者がイベントを実行する可能性に基づいてユーザーを特定し、メッセージを送るための強力なツールを提供します。イベント予測を作成すると、Brazeは[勾配ブースティング決定木を](https://en.wikipedia.org/wiki/Gradient_boosting)使用して機械学習モデルを訓練し、過去のアクティビティから学習して将来のアクティビティを予測します。

予測が構築されると、ユーザーは0から100の間で、選択したイベントを実行する可能性を示す[可能性スコアを]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/prediction_analytics/#purchase_score)割り当てられます。スコアが高いほど、ユーザーがそのイベントを実行する可能性が高い。また、ユーザーは、可能性が低い、中程度、高いのカテゴリー別に分類される。

プレディクティブ・イベントの本当の価値は、予測結果を使ってセグメントやキャンペーンを作成することにある。マーケティング担当者は、**予測**ページで直接ターゲットを絞ったキャンペーンを構築し、即座に収益を上げることも、将来のキャンペーンやキャンバスのためにセグメントを保存することもできます。誰を最初にターゲットにするか迷っている？可能性スコアに基づくメッセージング・ユーザーの[戦略的考察を]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/messaging_users/#strategy)お読みください。

## アクセス予測イベント

**予測」**ページは「**アナリティクス」**セクションにあります。完全なアクセスについては、アカウント・マネージャーにお問い合わせください。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)お使いの場合は、**「** **エンゲージメント**」の下に**「予測」が**あります。
{% endalert %}

この機能を購入する前に、プレビューモードで利用することができます。これにより、合成データを使ったデモ予測を見たり、一度に1つのプレビュー予測モデルを作成することができます。この予測は、実際のユーザーデータに基づいて作成されますが、可能性スコアに従ってメッセージングのターゲットをユーザーに絞ることはできません。また、作成後に定期的に更新されることもない。

プレビューでは、この1つの[予測を]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/prediction_analytics/#prediction_quality)編集して再構築したり、アーカイブして他の予測を作成したりすることもできます。

<br><br>

[1]: {% image_buster /assets/img/how_predictive_events_works.png %}

