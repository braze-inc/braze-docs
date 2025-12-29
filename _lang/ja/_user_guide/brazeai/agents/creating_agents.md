---
nav_title: エージェントを作る
article_title: カスタムエージェントを作成する
description: "エージェントの作成方法、始める前に準備すべきこと、メッセージング、意思決定、データ管理にわたってエージェントを活用する方法を学習する。"
alias: /creating-agents/
---

# カスタムエージェントを作成する

> カスタムエージェントの作成方法、始める前に準備すべきこと、メッセージング、意思決定、データ管理にわたってエージェントを活用する方法を学習する。一般的な情報については、[Braze Agentsを]({{site.baseurl}}/user_guide/brazeai/agents)参照のこと。 

{% alert important %}
Braze Currentsは現在ベータ版である。まずはカスタマー・サクセス・マネージャーにご相談を。
{% endalert %}

## 前提条件

開始する前に、次のものが必要になります。

- ワークスペース内の**エージェントコンソールに**アクセスする。このオプションが表示されない場合は、Brazeの管理者に確認すること。  
- カスタムAIエージェントの作成・編集権限。 
- 代理人に何を成し遂げてほしいかのアイデア。Braze Agentsは以下のアクションをサポートできる：  
   - **メッセージングだ：**件名、見出し、製品内コピー、その他のコンテンツを作成する。  
   - **決断する：**行動、好み、またはカスタム属性に基づいてキャンバスでユーザーをルーティングする。  
   - **データマネージャー：**値の計算、カタログエントリの充実、プロファイルフィールドの更新を行う。  

## 仕組み

エージェントを作成するとき、その目的を定義し、どのように振る舞うべきかのガードレールを設定する。本番稼動後、エージェントはパーソナライズされたコピーの生成、リアルタイムの意思決定、カタログフィールドの更新のためにBrazeに配備することができる。エージェントの一時停止や更新はダッシュボードからいつでもできる。

## エージェントを作成する

カスタムエージェントを作成する：  

1. ダッシュボードの**Agent Console**>**Agent Managementに**進む。  
2. **エージェントの作成**」を選択する。  
3. チームがその目的を理解できるように、名前と説明を入力する。  
4. エージェントが使用する[モデルを](#models)選択する。  

![Brazeでカスタムエージェントを作成するためのエージェントコンソールインターフェイス。画面には、エージェント名と説明を入力し、モデルを選択するフィールドが表示される。]( {% image_buster /assets/img/ai_agent/create_custom_agent.png %} )

5. 代理人に指示を出す。[ライティングの手引きを](#writing-instructions)参照すること。
6. [エージェントの](#testing-your-agent)出力を[テスト](#testing-your-agent)し、必要に応じて指示を調整する。
7. 準備ができたら、**Create Agentを**選択してエージェントをアクティブにする。 

## 次のステップ

これでエージェントを使用する準備が整った！詳細は[エージェントのデプロイを]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)参照のこと。 

## 参考

### モデル

エージェントを設定する際、レスポンスを生成するために使用するモデルを選択する。選択肢は2つある：

#### オプション 1: Braze搭載モデルを使用する

これは最もシンプルなオプションで、余分なセットアップは必要ない。Brazeは大規模言語モデル（LLM）に直接アクセスできる。このオプションを使用するには、**Autoを**選択する。

{% alert note %}
Brazeが提供するLLMを利用する場合、ベータ期間中の費用は一切かからない。招集は1日5万回、合計50万回に制限されている。詳細は「[制限事項]({{site.baseurl}}/user_guide/brazeai/agents/#limitations)」を参照のこと。
{% endalert %}

#### オプション 2: APIキーを持参する

このオプションを使えば、BrazeアカウントをOpenAI、Anthropic、AWS Bedrock、Google Geminiなどのプロバイダーに接続できる。LLMプロバイダーからAPIキーを持参する場合、費用はBrazeからではなく、プロバイダーを通して直接請求される。

これを設定する：
1. **パートナー連携**＞**テクノロジー・パートナーと**進み、プロバイダーを探す。
2. プロバイダーからのAPIキーを入力する。
3. [**保存**] を選択します。

その後、エージェントに戻り、モデルを選択することができる。

### 指示書を書く

指示とは、あなたがエージェント（システム・プロンプト）に与えるルールやガイドラインのことである。これらは、エージェントが実行されるたびにどのように振る舞うべきかを定義する。システム命令は最大10KBである。

{% tabs %}
{% tab Best practices %}

プロンプティングを始めるための一般的なベストプラクティスを紹介しよう：

1. 終わりを念頭に置いてスタートする。まず目標を述べる。
2. モデルに役割やペルソナを与える（「あなたは...です」）。
3. 明確な文脈と制約（オーディエンス、長さ、トーン、フォーマット）を設定する。
4. 構造を求める（「JSON/箇条書きリスト/テーブルを返す...」）。
5. 見せて、教えるな。質の高い例をいくつか挙げる。
6. 複雑な仕事を順序立てたステップに分ける（「ステップ1...ステップ2..."）。
7. 推論を奨励する（「声に出して考えてから答えよ」）。
8. 試験し、検査し、反復する。小さな微調整が大きな品質向上につながる。
9. エッジケースを処理し、ガードレールを追加し、拒否指示を追加する。
10. 再利用とスケーリングのために、内部で何がうまくいっているかを測定し、ドキュメント化する。

プロンプティングのベストプラクティスの詳細については、以下のモデルプロバイダーのガイドを参照のこと：

- [オープンAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [アンソロピック](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [ジェミニ](https://support.google.com/a/users/answer/14200040?hl=en)

{% endtab %}
{% tab Examples %}

{% details Simple prompt %}

このプロンプトの例では、アンケートを入力し、簡単なセンチメント分析を出力する：

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

このプロンプトの例では、ユーザーからのアンケート入力を受け取り、それを1つのセンチメントラベルに分類する。その結果は、ユーザーを異なるキャンバスのパス（肯定的なフィードバックと否定的なフィードバックなど）に誘導したり、将来のターゲティングのために、センチメントをプロフィール上のカスタム属性として保存するために使用することができる。

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

エージェントの[レスポンシブ・ガイドラインを]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines)選択することができる。例えば、ユーザーにジムの会員登録を促すSMSコピーをエージェントに生成させたい場合、このフィールドを使って、事前に定義した太字でやる気を起こさせるガイドラインを参照することができる。

### 温度

ユーザーがモバイルアプリにログインすることを促すコピーを生成するためにエージェントを使うことが目的であれば、エージェントがよりクリエイティブになり、コンテキスト変数のニュアンスを利用できるように、エージェントの温度を高く設定することができる。ユーザーのセンチメント分析用のコピーを生成するためにエージェントを使用している場合、ネガティブなアンケート回答に対するエージェントの推測を避けるために、温度を低く設定するのが理想的かもしれない。この設定をテストし、あなたのシナリオに合うようにエージェントが生成したコピーを見直すことをお勧めする。

{% alert note %}
現在、温度はOpenAIではサポートされていない。
{% endalert %}

### カタログ

エージェントが参照するカタログのリストから選択し、メッセージをさらにパーソナライズさせる。

{% alert note %}
現在、エージェントがカタログの希望する列を参照できるようにするには、その列がカタログの少なくとも1つの[選択に]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)存在しなければならない。
{% endalert %}

### 出力フォーマット

手動でフィールドを構造化するか、JSON を使用することによって、エージェントの出力を整理し定義するために、**出力形式**フィールドを使用する。 

例えば、あなたのレストラン・チェーンで最近食事をしたユーザーのフィードバックを集めたいとしよう。出力形式として**JSONスキーマを**選択し、以下のJSONを挿入することで、センチメント変数と推論変数を含むデータオブジェクトを返すことができる。

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
出力フォーマットは現在クロードAIではサポートされていない。Anthropicキーを使用している場合は、エージェントのプロンプトに手動で構造を追加することを推奨する。
{% endalert %}

#### エージェントをテストする  

**ライブプレビューペインは**、コンフィギュレーションエクスペリエンス内でサイドバイサイドパネルとして表示されるエージェントのインスタンスである。エージェントの作成中や更新中のテストに使用し、エンドユーザーと同じように体験することができる。このステップを踏むことで、期待通りの動作が確認でき、本番前に微調整をするチャンスが得られる。

![カスタムエージェントをテストするためのライブプレビューペインを示すエージェントコンソール。インターフェイスには、顧客データの例が表示されるサンプル入力フィールド、テスト実行ボタン、エージェント出力が表示されるレスポンシブエリアが表示される。]( {% image_buster /assets/img/ai_agent/custom_agent_test.png %} )

1. **サンプル入力**フィールドには、顧客データや顧客のレスポンシブなど、エージェントが扱う実際のシナリオを反映したものを入力する。 
2. **Run testを**選択する。エージェントはあなたの設定に基づいて実行し、そのレスポンスを表示する。テストの実行は、1日および総招集回数制限にカウントされる。

批判的な目でアウトプットを見直す。次の質問を考えてみよう：

- コピーはブランドにふさわしいか？ 
- 意思決定ロジックは意図した通りに顧客をルーティングしているか？ 
- 計算値は正確か？ 

何かおかしいと感じたら、エージェントの設定を更新し、再度テストする。いくつかの異なる入力を実行し、エージェントがシナリオ間でどのように適応するか、特にデータなしや無効なレスポンスのようなエッジケースを確認する。

#### エージェントを監視する

エージェントの**ログ**タブでは、キャンバスとカタログで発生した実際のエージェントコールを監視することができる。これには、タイムスタンプ、通話場所、通話時間、トークン数などの情報が含まれる。入力、出力、ユーザーIDを見るには、特定のエージェント・コールの**[表示]**を選択する。

![エージェントの市区町村のトレンドとレコメンデーション予約のログ。詳細パネルには、入力プロンプト、出力レスポンス、関連するユーザーIDが表示される。]( {% image_buster /assets/img/ai_agent/agent_logs.png %} )