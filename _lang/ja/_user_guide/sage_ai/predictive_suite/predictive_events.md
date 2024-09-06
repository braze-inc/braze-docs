---
nav_title: イベント予測
article_title: イベント予測
page_order: 6.4
layout: featured
alias: /predictive_purchases/
search_rank: 1
guide_top_header: "イベント予測"
guide_top_text: "どのユーザーが購入のような特定のイベントを行う可能性が高いかを知ることは、成長企業にとって極めて重要な洞察である。それがなければ、どのキャンペーンを作るかどうやって決めるのか？誰が割引やプロモーションを受けるべきか？限られた予算をどこに使うか？Brazeは、マーケティングチームが将来の行動を理解し、エンゲージメントと収益を最大化するキャンペーンにリソースを集中させることを容易にする機械学習モデルであるPredictive Events（旧Predictive Purchases）で、こうした疑問への回答を支援する。"
description: "この記事では、マーケターがイベントを実行する可能性に基づいてユーザーを特定し、メッセージを送る機能を提供するツール、プレディクティブ・イベント（以前はプレディクティブ・パーチェス）を取り上げる。"

guide_featured_title: "トピック"
guide_featured_list:
- name: 予測を立てる
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_events/creating_an_event_prediction/
  image: /assets/img/braze_icons/settings-01.svg
- name: 予測分析
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_events/prediction_analytics/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: ユーザーへのメッセージング
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_events/messaging_users/
  image: /assets/img/braze_icons/arrow-narrow-right.svg

---

## 概要

![予測イベントの仕組み」と題されたグラフィック。左側は、機械学習モデルに取り込まれるユーザーデータを示している。ラベルには、"過去のデータを使って訓練し、ある期間にイベントを実行したユーザーと実行しなかったユーザーの行動を比較する "と書かれている。右側は機械学習の結果で、ユーザーがそのイベントを実行する可能性が最も低いものから最も高いものへとランク付けされている。ラベルには "将来の出来事の可能性を予測し、正確で便利なターゲティングのためにユーザーに可能性スコアを割り当てる "と書かれている。][1]

> Predictive Eventsは、マーケティング担当者がイベントを実行する可能性に基づいてユーザーを特定し、メッセージを送るための強力なツールを提供する。イベント予測を作成すると、Brazeは[勾配ブースティング決定木を](https://en.wikipedia.org/wiki/Gradient_boosting)使用して機械学習モデルを訓練し、過去の活動から学習して将来の活動を予測する。

予測が構築されると、ユーザーは0から100の間で、選択したイベントを実行する可能性を示す[可能性スコアを]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/prediction_analytics/#purchase_score)割り当てられる。スコアが高いほど、ユーザーがそのイベントを実行する可能性が高い。ユーザーはまた、可能性が低い、中程度、高いのカテゴリー別に分類される。

プレディクティブ・イベントの本当の価値は、予測結果を使ってセグメントやキャンペーンを作成することにある。マーケティング担当者は、**予測**ページで直接ターゲットを絞ったキャンペーンを構築し、即座に収益を上げることも、将来のキャンペーンやキャンバスのためにセグメントを保存することもできる。誰を最初にターゲットにするか迷っている？可能性スコアに基づくメッセージング・ユーザーの[戦略的考察を]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/messaging_users/#strategy)読む。

## 予測イベントにアクセスする

**予測」**ページは**「アナリティクス」**セクションにある。完全なアクセスについては、アカウント・マネージャーに連絡すること。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**「** **エンゲージメント**」の下に**「予測」が**ある。
{% endalert %}

この機能を購入する前に、プレビュー・モードで利用できる。これにより、合成データを使ったデモ予測を見ることができるほか、プレビュー予測モデルを一度に1つ作成することもできる。この予測は、実際のユーザーデータに基づいて作成されるが、ユーザーの可能性スコアに従ってメッセージングのターゲットを絞ることはできない。また、作成後に定期的に更新されることもない。

プレビューを使えば、この1つの[予測を]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/prediction_analytics/#prediction_quality)編集して再構築したり、アーカイブして他の予測を作成したりすることもできる[。]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/creating_a_purchase_prediction/#audience)

<br><br>

[1]: {% image_buster /assets/img/how_predictive_events_works.png %}

