---
nav_title: エージェント
article_title: エージェントステップ
alias: /agent_step/
page_order: 0.2
page_type: reference
description: "このリファレンス記事では、キャンバスでエージェントステップを使用してコンテンツを生成したり、リアルタイムでインテリジェントな意思決定を行う方法について説明します。"
tool: Canvas
---

# エージェントステップ  

> Agent ステップを使用すると、AI を活用したデシジョンとコンテンツ生成をキャンバスワークフローに直接追加できます。詳細については、[Brazeエージェント]({{site.baseurl}}/user_guide/brazeai/agents/)を参照してください。 

<<<<<<< HEAD
![キャンバスユーザー旅行のエージェントステップ。]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}
=======
\![キャンバスユーザー旅行のエージェントステップ。]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}
>>>>>>> main

## 仕組み

ユーザーがキャンバスのエージェントステップに到達すると、Brazeは設定したインプットデータ(フルコンテキストまたは選択したフィールド)を選択したエージェントに送信します。次に、エージェントはそのモデルと命令を使用して入力を処理し、出力を返します。その出力は、ステップで定義した出力変数に保存されます。

次に、この変数を2 つの主な方法で使用できます。

- **決定:**ルートユーザーは、エージェントのレスポンスに基づいて、さまざまなキャンバスパスを停止します。たとえば、リードスコアリングエージェントは1 ～10 の数値を返す場合があります。このスコアを使用して、ユーザーのメッセージングを続行するか、ジャーニーから削除するかを決定できます。
- **パーソナライゼーション:**エージェントの応答をメッセージに直接挿入します。例えば、エージェントは、顧客 フィードバックを分析し、顧客の意見を参照し、再ソリューションを示唆するem パスのエティックフォローアップメールを生成することができます。

## エージェントステップの作成

### ステップ 1: ステップを追加する

サイドバーから**Agent**コンポーネントをドラッグアンドドロップするか、ステップの下部にある<i class="fas fa-plus-circle"></i>プラスボタンを選択し、**Agent**を選択します。  

### ステップ 2: エージェントの選択  

このステップでデータを処理するエージェントを選択します。既存のエージェントを選択するか、このステップから直接的に新しいエージェントを作成します。セットアップガイダンスについては、[カスタムエージェントの作成]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)を参照してください。

### ステップ 3: 出力変数の定義

エージェント出力は"output variables&quot と呼ばれ、[context variable]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-types) に格納され、簡単にアクセスできます。出力変数を定義するには

1. 変数に名前を付けます。
2. データタイプを選択します。 

エージェント出力は、文字列、数値、またはブール値として保存できます。これにより、キャンバス内のテキストパーソナライゼーションと条件付きロジックの両方に柔軟性を持たせることができます。各タイプの一般的な使用方法を次に示します。

| データタイプ | 一般的な用途 |
| --- | --- |
| string | メッセージパーソナライゼーション(件名、コピー、レスポンス) |
| 数値 | スコアリング、しきい値、[ Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) でのルーティング |
| ブール値 | [Decision Splits]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split)のYes/No分岐 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

定義すると、コンテキスト変数と同じテンプレート構文を使用して、キャンバス全体で出力変数を使用できます。**Context Variable** Segment フィルターを使用するか、またはLiquid: {% raw %}`{{context.${response_variable_name}}}` {% endraw %} を使用してエージェントレスポンスをテンプレートします。

### ステップ 4: エージェントに提供するコンテキストを決定する  

エージェントが実行時に受信するデータを決定する必要があります。以下のオプションがあります。  

- **すべてのキャンバスコンテキストを含める:**使用可能なすべてのキャンバスコンテキスト変数([Canvas エントリプロパティ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)など)と、コンテキストステップs で指定された他のコンテキストを渡します。  
- **値を指定します。**ユーザーの名や好きなカラーなど、選択したプロパティーのみを渡します。このオプションを選択すると、エージェントはここで割り当てた値にのみアクセスできます。**Key**ごとに、具体的なユーザープロファイル フィールドまたはコンテキスト変数を定義する[Liquid タグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags)を入力します。  

{% alert note %}
Brazeは、最初の10Kバイトのコンテンツのみをエージェントに渡します。合計値が10KB を超える値を指定すると、切り捨てられます。費用を節約するために、キャンバスのBraze Agent は、同一のインプットのLLM レスポンスに短時間のキャッシュを使用します。すべてのキャンバスコンテキストを含めると、キャッシュされた結果が使用できない可能性が高くなり、LLM コストが増加する可能性があります。
{% endalert %}

## エラー処理  

- 接続されたモデルがレート制限 エラーを返す場合、Brazeは指数バックオフで最大5 回再試行します。  
- 他の理由(不正なAPI キーなど)でエージェントが失敗した場合、出力変数は`null` に設定されます。  
- 応答は、繰り返しの呼び出しを減らすために、同じ入力に対してキャッシュされます。  

## 分析  

エージェントステップの実行方法を追跡するには、次のメトリクスを参照してください。  

| 指標 | 説明 |
| --- | --- |
| _入力済み_ | ユーザーがエージェントステップに入った回数。 |
| _次のステップに進む_ | エージェントステップを通過した後、フロー内の次回のステップに進むユーザーの数。 |
| _終了済みのキャンバス_ | エージェントステップを通過した後にキャンバスを終了したユーザーの数。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 関連記事  

- [Braze代理店の概況]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [カスタムエージェントの作成]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [エージェントのデプロイ]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  