---
nav_title: ベストプラクティス
article_title: キャンバスのベストプラクティス
page_order: 1
description: "この記事では、キャンバスとキャンバスフローを使用してユーザージャーニーを作成しカスタマイズする際のベストプラクティスをいくつか紹介します。"
tool: Canvas

---

# キャンバスのベストプラクティス

> この記事では、キャンバスとキャンバスフローを使用してユーザージャーニーを作成しカスタマイズする際のベストプラクティスをいくつか紹介します。

## 目的を特定する

「何を」、「誰が」、「なぜ」を詳しく調べてみましょう。
- ユーザーに何を達成してもらいたいのか?
- リーチしようとしているユーザーは誰か?
- なぜこのキャンバスを作るのか？

## 組み合わせる

[キャンバスコンポーネント]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/)で、ユーザージャーニーの新たな組み合わせを実現しましょう。
- [条件分岐]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/)でユーザーを分割し、異なるワークフローを作成します。
- [遅延]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/)ステップでユーザージャーニーの間隔を空けます。
- キャンバスフローの好きな場所に[スタンドアロンメッセージを]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)追加できる。 

## より充実したメッセージを作成する

より充実したメッセージでユーザーの関心を引きましょう。

- キャンバスをオンボーディングする[アプリ内メッセージ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/)を作成して、第一印象を最大限に活用する。
- プロモーションオファーやプッシュ通知用の[コンテンツカード]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/content-cards_in_canvas/)をキャンバスジャーニーに導入する。

## ユーザージャーニーをテストする

キャンバスメッセージの効果を確認するには、コントロールグループを組み込みます。これにより、キャンバスの印象を理解できます。

- キャンバスの各ステップにユーザージャーニーの識別が可能な名前を付ける。
- ユーザージャーニーで[実験パス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/)コンポーネントを活用し、作成したさまざまなパスにユーザーをランダムに割り当てる。 
- 遅延とメッセージのステップでユーザージャーニーを多様化し、どのパスが最も効果的かを確認する。
- [キャンバス分析]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/)をチェックし、ユーザージャーニーでの各コンポーネントのパフォーマンスを確認する。
- 初回開始後に[キャンバスを編集]({{site.baseurl}}/post-launch_edits/)する。

## キャンバスのスケジュール

{% alert note %}
キャンバスでは、既に過ぎた時刻でスケジュールされた送信を使用することはできません。ただし、キャンペーンがスケジュールされているのとまったく同じ時間 (またはその数秒前) にキャンバスを起動することができます。これにより、キャンバスがスケジュールされたエントリ時刻を逃し、ユーザーがキャンバスにエントリできなくなる可能性があります。スケジュールされた送信時間から数分以内にキャンペーンが編集された場合、すぐにキャンバスを送信することをおすすめします。
{% endalert %}

キャンバスのステップでは、キャンバスをスケジュールする際に次の詳細を考慮します。

- スケジュールの変更は、ステップの受信待ちにまだなっていないユーザーにのみ適用されます。
- ステップの受信を待機していないユーザーに適用されるように変更をスケジュールしない限り、オーディエンスの変更はデフォルトですべてのユーザーに適用されます。
- デプロイ後すぐに配信されるようにスケジュールされているキャンバスを編集し、[**更新**] を選択すると、基本的に送信されます。
