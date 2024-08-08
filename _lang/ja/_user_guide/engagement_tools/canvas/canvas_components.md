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
  - name: Message Step
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/message_step/
    fa_icon: fas fa-comment-alt
  - name: Delay Step
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/delay_step/
    fa_icon: fas fa-stopwatch
  - name: Decision Split Step
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/decision_split/
    fa_icon: fas fa-random
  - name: Audience Paths Step
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/audience_paths/
    fa_icon: fa fa-users 
  - name: Action Paths Step  
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/action_paths/
    fa_icon: fa fa-bolt
  - name: Experiment Paths Step
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/experiment_step/
    fa_icon: fas fa-columns
  - name: User Update Step
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/user_update/
    fa_icon: fas fa-user-check
  - name: Feature Flags in Canvas
    link: /docs/developer_guide/platform_wide/feature_flags/canvas/
    fa_icon: fas fa-project-diagram
  - name: Canvas Audience Sync
    link: /docs/partners/canvas_steps/
    fa_icon: fa-solid fa-rotate
---

## キャンバスコンポーネントについて

キャンバスコンポーネントを使用すると、新しいユーザージャーニーを開拓してプロセスを改善し、オーディエンスへの働きかけの効果を高めることができます。

{% alert important %}
2023 年 2 月 28 日以降、元のキャンバスエクスペリエンスを使用したキャンバスの作成や複製ができなくなりました。Braze では、元のキャンバスエクスペリエンスを使用しているお客様に、キャンバスフローへの移行をお勧めしています。これは、キャンバスの構築と管理をより良く行う目的で改良された編集エクスペリエンスです。「[キャンバスからキャンバスフローへの複製]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/)」を参照してください。
{% endalert %}

### ユーザージャーニーのカスタマイズ

[アクションパス][1]を使用すると、アクションや購入などのエンゲージメントイベントに基づいてユーザージャーニーを分岐させることができます。オーディエンスをフィルタリングしでターゲティングしたい場合、[オーディエンスパス][2]を利用すると、オーディエンスの条件に基づいてユーザーをさまざまなキャンバスパスに誘導できるため、ユーザーのターゲット設定が簡単になります。

[条件分岐][3]のコンポーネントは、単純な「はい / いいえ」のロジックを使用して、アクションやユーザー属性に基づいて、ユーザージャーニーに相互に排他的な 2 つのパスを作成します。これは、ユーザーグループの特定とターゲット設定に役立ちます。

[延期期間][4]コンポーネントを使うと、キャンバス内の 1 つのステップを延期することができます。キャンバスのこのスタンドアロンの延期期間ステップは、特定の時刻にユーザーにメッセージを伝えるのに最適です。さらに、延期期間コンポーネントを使用すると、オーディエンスがコンポーネントの条件を満たすまでの時間を長くできるので、オーディエンスへの働きかけを増やすこともできます。 

### テスト
ユーザージャーニーを作成するときは、最も効果的なキャンバスパスもテストすることをお勧めします。[実験パス][5]を使用すると、任意のステップで複数のキャンバスパスをテストできます。 

### 統合 
貴社ブランドのファーストパーティユーザーデータとの同期をご希望の場合には、[Facebook][6] と [Google][7] で利用できるオーディエンス同期オプションをご活用ください。<br><br>

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths
[3]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split
[4]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step
[5]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step
[6]: {{site.baseurl}}/partners/canvas_steps/facebook_audience_sync
[7]: {{site.baseurl}}/partners/canvas_steps/google_audience_sync