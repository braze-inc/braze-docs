---
nav_title: キャンバスのコンポーネント
article_title: キャンバスのコンポーネント
page_order: 2
alias: "/user_guide/engagement_tools/canvas/canvas_components/about/"
layout: dev_guide
guide_top_header: "キャンバスのコンポーネント"
guide_top_text: "キャンバスのコンポーネントを使ってキャンバスジャーニーをさらに充実させることができます。キャンバスコンポーネントを使用すると、キャンバスの有効性を判断するプロセスを簡略化できます。これにより、必要以上に多くの手順を 1 つの手順に置き換えることができます。キャンバスのコンポーネントは、キャンバスブランチでのパーソナライズされたユーザージャーニーを指しています。"

page_type: landing
description: "このランディングページには、より高度なキャンバスの作成に役立つキャンバスコンポーネントに関する記事がまとめられています。これらのコンポーネントには、メッセージステップ、延期期間ステップ、条件分岐ステップなどがあります。"
tool: Canvas

guide_featured_title: "セクションの記事"
guide_featured_list:
  - name: メッセージ ステップ
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/message_step/
    image: /assets/img/braze_icons/message-square-02.svg
  - name: 遅延 ステップ
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/delay_step/
    image: /assets/img/braze_icons/clock-stopwatch.svg
  - name: 条件分岐ステップ
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/decision_split/
    image: /assets/img/braze_icons/dataflow-04.svg
  - name: オーディエンス パス ステップ
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/audience_paths/
    image: /assets/img/braze_icons/users-01.svg 
  - name: アクション パス ステップ  
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/action_paths/
    image: /assets/img/braze_icons/zap.svg
  - name: 実験パスステップ
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/experiment_step/
    image: /assets/img/braze_icons/columns-01.svg
  - name: ユーザー 更新 ステップ
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/user_update/
    image: /assets/img/braze_icons/user-check-01.svg
  - name: キャンバスのフィーチャーフラグ
    link: /docs/developer_guide/feature_flags/canvas/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: キャンバスオーディエンスの同期
    link: /docs/partners/canvas_audience_sync/
    image: /assets/img/braze_icons/refresh-ccw-02.svg
---

## キャンバスコンポーネントについて

キャンバスコンポーネントを使用すると、新しいユーザージャーニーを開拓してプロセスを改善し、オーディエンスへの働きかけの効果を高めることができます。

### ユーザージャーニーのカスタマイズ

![条件分岐ステップの後に遅延ステップとメッセージステップが続くキャンバスユーザー体験の例]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %})({: style="float:right;max-width:55%;margin-left:15px;"})

[アクションパス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths)を使用すると、アクションや購入などのエンゲージメントイベントに基づいてユーザージャーニーを分岐させることができます。オーディエンスをフィルタリングしでターゲティングしたい場合、[オーディエンスパス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths)を利用すると、オーディエンスの条件に基づいてユーザーをさまざまなキャンバスパスに誘導できるため、ユーザーのターゲット設定が簡単になります。

[条件分岐]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split)のコンポーネントは、単純な「はい / いいえ」のロジックを使用して、アクションやユーザー属性に基づいて、ユーザージャーニーに相互に排他的な 2 つのパスを作成します。これは、ユーザーグループの特定とターゲット設定に役立ちます。

[延期期間]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step)コンポーネントを使うと、キャンバス内の 1 つのステップを延期することができます。キャンバスのこのスタンドアロンの延期期間ステップは、特定の時刻にユーザーにメッセージを伝えるのに最適です。さらに、延期期間コンポーネントを使用すると、オーディエンスがコンポーネントの条件を満たすまでの時間を長くできるので、オーディエンスへの働きかけを増やすこともできます。

### テスト

ユーザージャーニーを作成するときは、最も効果的なキャンバスパスもテストすることをお勧めします。[実験パス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step)を使用すると、任意のステップで複数のキャンバスパスをテストできます。ステップ間の接続をハイレベルのプレビューとして使用することもできます。オレンジ色の接続は、直前のステップがユーザーを次のステップに進ませることを示します。

### 統合

貴社ブランドのファーストパーティユーザーデータとの同期をご希望の場合には、[Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) と [Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) で利用できるオーディエンス同期オプションをご活用ください。

