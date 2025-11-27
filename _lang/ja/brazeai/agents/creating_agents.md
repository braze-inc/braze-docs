---
nav_title: エージェントの作成
article_title: カスタムエージェントの作成
description: "エージェントを作成する方法、開始する前に準備するもの、およびメッセージング、意思決定、データマネジメントをまたいで機能させる方法について説明します。"
alias: /creating-agents/
---

# カスタムエージェントの作成

> カスタムエージェントを作成する方法、始める前に準備するもの、およびメッセージング、意思決定、データマネジメントを横断して機能させる方法について説明します。詳細については、[Brazeエージェント]({{site.baseurl}}/user_guide/brazeai/agents)を参照してください。 

{% alert important %}
Braze代理店は現在ベータ版である。始めるには、顧客のサクセスマネージャーにお問い合わせください。
{% endalert %}

## 前提条件

開始する前に、次のものが必要になります。

- ワークスペース内の**エージェントコンソール** へのアクセス。この項目が表示されない場合は、Braze管理者に問い合わせてください。  
- カスタムAI Agent を作成および編集する権限。 
- エージェントに実行させたい内容のアイデア。Brazeエージェントは、次のアクションに対応できます。  
   - メッセージング件名、見出し、製品内コピー、またはその他のコンテンツを生成します。  
   - **決定:**ビヘイビア、環境設定、またはカスタム属性sに基づいて、キャンバスにユーザーをルーティングします。  
   - データ管理数値の計算、カタログ項目の拡張、またはプロファイル フィールドs のリフレッシュ。  

## 仕組み

エージェントを作成するときは、その目的を定義し、その動作方法にガードレールを設定します。有効になったら、エージェントをBraze にデプロイして、パーソナライズされたの複製を生成したり、リアルタイムで決定したり、s を更新 カタログ フィールドしたりできます。エージェントは、ダッシュボードからいつでも一時停止または更新できます。

## エージェントの作成

カスタムエージェントを作成するには:  

1. Braze ダッシュボードの**Agent Console**> **Agent Management** に移動します。  
2. **エージェントの作成**を選択します。  
3. チームがその目的を理解できるように、名前と説明を入力します。  
4. エージェントが使用する[モデル](#models)を選択します。  

![Braze でカスタムエージェントを作成するためのエージェントコンソールインターフェイス。エージェントの名前と説明を入力し、モデルを選択するためのフィールドs が表示されます。]( {% image_buster /assets/img/ai_agent/create_custom_agent.png %} )

5. エージェントに指示を与えます。ガイダンスについては、[書込み命令](#writing-instructions)を参照してください。
6. [エージェント](#testing-your-agent)の出力をテストし、必要に応じて指示を調整します。
7. 準備ができたら、**Create Agent**を選択してエージェントをアクティブ化します。 

## 次のステップ

これで、エージェントを使用する準備が整いました。詳細については、[エージェントの展開]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)を参照してください。 

## 参考

### モデル

エージェントを設定するときは、レスポンスの生成に使用するモデルを選択します。2 つのオプションがあります。

#### オプション 1: Braze駆動の機種を使用する

これは最も単純なオプションで、追加のセットアップは必要ありません。Braze は、ラージ・ランゲージ・モデル(LLM) をダイレクトに利用できます。このオプションを使用するには、**Auto**を選択します。

{% alert note %}
Braze 電源付きLLM を使用する場合、ベータ期間中に費用は発生しません。呼び出しは1 日あたり50,000 回の実行に制限され、合計で500,000 回の実行になります。詳細については、[制限]({{site.baseurl}}/user_guide/brazeai/agents/#limitations)を参照してください。
{% endalert %}

#### オプション 2: 自分のAPI キーを持ってくる

この機能を使用すると、BrazeアカウントをOpenAI、Anthropic、AWS Bedrock、Google Geminiなどのプロバイダーに接続できます。LLMプロバイダーから独自のAPI キーを取得した場合、費用はBrazeからではなくプロバイダーから直接請求されます。

これを設定するには:
1. **Partner Integrations**> **Technology Partners**に移動し、プロバイダを見つけます。
2. プロバイダーからAPI キーを入力します。
3. [**保存**] を選択します。

その後、エージェントに戻り、モデルを選択できます。

### 命令の記述

指示は、エージェントに指定するルールまたはガイドラインです(システムプロンプト)。これらは、エージェントが実行されるたびにエージェントがどのように動作するかを定義します。システム命令は最大10KB まで可能です。

{% tabs %}
{% tab Best practices %}

プロンプトを開始するための一般的なベストプラクティスを次に示します。

1. 最後を念頭に置いて始めましょう。まず目標を述べよ。
2. モデルにロールまたはペルソナを指定します("You are ...")。
3. クリアコンテキストとコンストレーニングts(オーディエンス、長さ、トーン、形式)を設定します。
4. 構造を確認します("JSON/箇条書きリスト/table...")。
5. 見せろ、言わないで。質の高い例をいくつか挙げてください。
6. 複雑な作業を順序付けられたステップに分割(" ステップ 1...)ステップ 2:
7. 推論を促す("声に出して考えてから、"に答える)。
8. パイロット、検査、および反復。微調整は、大きな品質向上につながります。
9. エッジケースの取り扱い、ガードレールの追加、拒否指示の追加。
10. 再利用と拡大・縮小のために内部機能するものを測定し、文書化する。

ベストプラクティスのプロンプトの詳細については、次のモデルプロバイダのガイドを参照してください。

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [アントロピー](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [ジェミニ](https://support.google.com/a/users/answer/14200040?hl=en)

{% endtab %}
{% tab Examples %}

{% details Simple prompt %}

このサンプルプロンプトは、調査のインプットを受け取り、シンプルなセンチメント解析を出力します。

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative
Always output a single string with just one label.
If any category is missing or unclear, treat it as Neutral.
If sentiment across categories is mixed, return Neutral.

Example Input: “The product works great, but shipping took forever and the cost felt too high.”
Example Output: Neutral
```

{% enddetails %}

{% details Complex prompt %}

このサンプルプロンプトは、ユーザーから調査インプットを受け取り、それを単一のセンチメントラベルに分類します。これにより、ユーザーをさまざまなキャンバスパスにルーティングしたり(正と負のフィードバックなど)、将来のターゲティングのプロファイルにカスタム属性として保存したりすることができます。

{% raw %}
```
You are a customer research AI for a retail brand.  
Input: one open-text survey response from a user.  
Output: A single structured JSON object with:  
- sentiment (Positive, Neutral, Negative)  
- topic (Product, Delivery, Price, Other)  
- action_recommendation (Route: High-priority follow-up | Low-priority follow-up | No action)  

Rules:  
- Always return valid JSON.  
- If the topic is unclear, default to Other.  
- If sentiment is mixed, default to Neutral.  
- If sentiment is Negative and topic = Product or Delivery → action_recommendation = High-priority follow-up.  
- Otherwise, action_recommendation = Low-priority follow-up.  

Example Input:  
"The product works great, but shipping took forever and the cost felt too high."  

Example Output:  
{  
  "sentiment": "Neutral",  
  "topic": "Delivery",  
  "action_recommendation": "High-priority follow-up"  
}  
```
{% endraw %}
{% enddetails %}

{% endtab %}
{% endtabs %}

### ブランド・ガイドライン

エージェントが応答に従うようにするには、[ブランドガイドライン]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) を選択できます。たとえば、エージェントがSMSコピーを生成して、ユーザーがジムのメンバーシップにサインアップするように促す場合、このフィールドを使用して、事前に定義された大胆なモチベーションガイドラインを参照することができます。

### 温度

エージェントを使用してコピーを生成し、ユーザーが携帯アプリにログインできるようにするには、エージェントがよりクリエイティブになり、コンテキスト変数のニュアンスを使用するように、エージェントの温度を高く設定します。エージェントを使用してユーザーセンチメント解析用のコピーを生成する場合は、負の調査レスポンスに対するエージェントの推測を回避するために、低温を設定するアイデアがある場合があります。この設定をテストし、ユーザのシナリオに合わせてエージェントの生成されたコピーを確認することをお勧めします。

{% alert note %}
OpenAI で使用するための温度は現在サポートされていません。
{% endalert %}

### カタログ

代理店のカタログの一覧から選択して、メッセージを参照し、さらにカスタマイズします。

{% alert note %}
現在、エージェントがカタログの目的の列を参照できるようにするには、その列がカタログの少なくとも1つの[選択]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)に存在している必要があります。
{% endalert %}

### 出力形式

**出力形式**フィールドを使用して、フィールドを手動で構造化するか、JSONを使用してエージェントの出力を編成および定義します。 

例えば、あなたのレストランチェーンで直近の食事体験のユーザー フィードバックを集めたいとしましょう。出力形式として**JSONスキーマ**を選択し、次のJSONを挿入して、センチメント変数と推論変数を含むデータオブジェクトを返すことができます。

```json
{
  "type": "object",
  "properties": {
    "sentiment": {
      "type": "string"
    },
    "reasoning": {
      "type": "string"
    }
  },
  "required": [
    "sentiment",
    "reasoning"
  ]
}
```

{% alert note %}
出力形式は現在、Claude AI ではサポートされていません。Anthropic キーを使用している場合は、エージェントプロンプトに手動で構造体を追加することをお勧めします。
{% endalert %}

#### エージェントのテスト  

**Live プレビュー**ペインは、設定エクスペリエンス内でサイドバイサイドパネルとして表示されるエージェントのインスタンスです。これを使用して、エンドユーザーs と同様の方法でエージェントを体験するための更新を作成または作成している間にエージェントをテストすることができます。このステップは、期待通りに動作していることを確認するのに役立ち、実際に動作する前に微調整する機会を提供します。

![カスタムエージェントをテストするための「ライブプレビュー」パネルを表示するエージェントコンソール。インターフェイスには、サンプル入力フィールドとサンプル顧客データ、テスト実行ボタン、エージェント出力が耳にアプリする応答領域が表示されます。]( {% image_buster /assets/img/ai_agent/custom_agent_test.png %} )

1. **サンプル入力**フィールドに、サンプル顧客データまたは顧客応答を入力します。エージェントが処理する実際のシナリオを反映するものを入力します。 
2. [**テストを実行**] を選択します。エージェントは設定に基づいて実行され、その応答が表示されます。テスト実行は、毎日および合計の呼び出し制限にカウントされます。

重要な目で出力を確認します。次の質問について考えてみましょう。

- コピーはブランドに感じられるか。 
- デシジョンロジックルートの顧客は意図したとおりですか? 
- 計算値はキュレートですか? 

何か気分が悪くなった場合は、エージェントの設定を更新して、もう一度テストします。いくつかの異なる入力を実行して、エージェントがシナリオ間でどのように適応するかを確認します。特に、データがない、または無効な応答などのエッジケースです。

#### エージェントの監視

エージェントの**Logs**タブでは、キャンバスとカタログで発生する実際のエージェントコールを監視できます。これには、タイムスタンプ、発信場所、期間、トークン数などが含まれます。入力、出力、およびユーザー IDを表示するには、特定のエージェントコールに対して**View** を選択します。

![エージェント市区町村のトレンドとレコメンドブッキングのログ。これには、エージェントが呼び出された日時と場所が含まれます。詳細パネルには、入力プロンプト、出力レスポンス、および関連するユーザー IDが表示されます。]( {% image_buster /assets/img/ai_agent/agent_logs.png %} )