---
nav_title: 参考
article_title: 代理店照会
description: "Braze Agentsの主な詳細を参照のこと。"
page_order: 3
---

# 代理店照会

> カスタムエージェントを作成する際、指示や出力スキーマのような重要な設定については、この記事を参照のこと。紹介は[Braze Agentsを]({{site.baseurl}}/user_guide/brazeai/agents/)参照のこと。

{% alert important %}
Braze Currentsは現在ベータ版である。まずはカスタマー・サクセス・マネージャーにご相談を。
{% endalert %}

## モデル

エージェントを設定する際、レスポンスを生成するために使用するモデルを選択することができる。Brazeを搭載したモデルを使うか、APIキーを持参するかの2つの選択肢がある。

{% alert important %}
Brazeを搭載した**Auto**モデルは、思考能力がカタログ検索やユーザーセグメンテーションのメンバーシップなどのタスクを実行するのに十分なモデルに最適化されている。他のモデルを使用する場合は、使用するモデルがユースケースでうまく機能するかどうかをテストすることをお勧めする。スピードや能力の異なるモデルに対して、異なる詳細レベルやステップ・バイ・ステップの考え方を与えるために、[インストラクションを](#writing-instructions)調整する必要があるかもしれない。
{% endalert %}

### オプション 1: Braze搭載モデルを使用する

これは最もシンプルなオプションで、余分なセットアップは必要ない。Brazeは大規模言語モデル（LLM）に直接アクセスできる。このオプションを使用するには、ジェミニ・モデルを使用する**Autoを**選択する。

### オプション 2: APIキーを持参する

このオプションを使えば、BrazeアカウントをOpenAI、Anthropic、AWS Bedrock、Google Geminiなどのプロバイダーに接続できる。LLMプロバイダーから自分のAPIキーを持参する場合、トークンの費用はBrazeではなく、プロバイダーを通して直接請求される。

{% alert important %}
レガシー・モデルは数カ月後に製造中止や非推奨となる可能性があるため、定期的に最新モデルをテストすることをお勧めする。
{% endalert %}

これを設定する：

1. **パートナー連携**＞**テクノロジー・パートナーと**進み、プロバイダーを探す。
2. プロバイダーからのAPIキーを入力する。
3. [**保存**] を選択します。

その後、エージェントに戻り、モデルを選択することができる。

{% alert important %}
お客様がBrazeが提供するLLMを使用する場合、当該モデルのプロバイダーは、お客様とBrazeとの間のデータ処理追加条項（DPA）の条件に従い、Brazeのサブプロセッサーとして行動する。APIキーの持参を選択した場合、LLMサブスクリプションのプロバイダーは、お客様とBraze間の契約においてサードパーティプロバイダーとみなされる。  
{% endalert %}

## 指示書を書く

指示とは、あなたがエージェント（システム・プロンプト）に与えるルールやガイドラインのことである。これらは、エージェントが実行されるたびにどのように振る舞うべきかを定義する。システム命令は最大25KBである。

プロンプティングを始めるための一般的なベストプラクティスを紹介しよう：

1. 終わりを念頭に置いてスタートする。まず目標を述べる。
2. モデルに役割やペルソナを与える（「あなたは...です」）。
3. 明確な文脈と制約（オーディエンス、長さ、トーン、フォーマット）を設定する。
4. 構造を求める（「JSON/箇条書きリスト/テーブルを返す...」）。
5. 見せて、教えるな。質の高い例をいくつか挙げる。
6. 複雑な仕事を順序立てたステップに分ける（「ステップ1...ステップ2..."）。
7. 推論を促す（「内部でステップを考え、簡潔に最終的な答えを出す」、あるいは「決定を簡潔に説明する」）。
8. 試験し、検査し、反復する。小さな微調整が大きな品質向上につながる。
9. エッジケースを処理し、ガードレールを追加し、拒否指示を追加する。
10. 再利用とスケーリングのために、内部で何がうまくいっているかを測定し、ドキュメント化する。

エージェントが解析できないレスポンスを受信した場合のキャッチオールレスポンスとして、デフォルトを含めることも推奨する。このエラー処理により、エージェントは未知の結果変数があることを知らせることができる。例えば、エージェントに "肯定的 "か "否定的 "かの感情値だけを求めるのではなく、判断できない場合は "不明 "を返すように求める。

### シンプルなプロンプト

このプロンプトの例では、アンケートを入力し、簡単なセンチメント分析を出力する：

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative.
Always output a single string with just one label.
If any category is missing or unclear, treat it as Neutral.
If sentiment across categories is mixed, return Neutral.

Example Input: “The product works great, but shipping took forever and the cost felt too high.”
Example Output: Neutral
```

### コンプレックス・プロンプト 

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

プロンプティングのベストプラクティスの詳細については、以下のモデルプロバイダーのガイドを参照のこと：

- [オープンAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [アンソロピック](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [ジェミニ](https://support.google.com/a/users/answer/14200040?hl=en)

### Liquid の使用

エージェントの指示にパーソナライズ[されたLiquidを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid)含めることで、レスポンスにパーソナライゼーションを加えることができる。エージェントが取得するLiquid変数を正確に指定し、プロンプトのコンテキストに含めることができる。例えば、"名 "を明示的に書く代わりに、Liquidのスニペット{% raw %}`{{${first_name}}}`{% endraw %} ：

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

**エージェントコンソールの** **ログ**セクションで、Liquid からレンダリングされた値を理解するために、エージェントの入力と出力の詳細を確認することができる。

![Liquidを持つエージェントの詳細。]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:65%;"}

## カタログとフィールド

エージェントが参照する特定のカタログを選択し、関連する場合は、エージェントがユーザー以外のデータや製品を理解するために必要なコンテキストを与える。エージェントは、トークンの使用を最小限にするため、ツールを使って関連するアイテムだけを見つけ、それをLLMに送る。

![レストラン "カタログと"Loyalty_Program" 列がエージェントの検索対象として選択されている。]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:85%;"}

## セグメンテーション・コンテキスト

キャンバスでエージェントを使用する際に、各ユーザーのセグメンテーションメンバーシップを相互参照するために、エージェントに最大3つのセグメントを選択することができる。例えば、エージェントが "ロイヤルティユーザー "のセグメントメンバーシップを選択していて、そのエージェントがキャンバスで使用されているとしよう。ユーザーがエージェントのステップに入ると、エージェントは、各ユーザーがエージェントコンソールで指定した各セグメンテーションのメンバーかどうかを相互参照し、各ユーザーのメンバーシップ（または非メンバー）をLLMのコンテキストとして使用することができる。

![ロイヤルティユーザー」のセグメンテーションがエージェント会員アクセスに選択された。]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:85%;"}

## ブランド・ガイドライン

エージェントの[レスポンシブ・ガイドラインを]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines)選択することができる。例えば、ユーザーにジムの会員登録を促すSMSコピーをエージェントに生成させたい場合、このフィールドを使って、事前に定義した太字でやる気を起こさせるガイドラインを参照することができる。

## 温度

ユーザーがモバイルアプリにログインすることを促すコピーを生成するためにエージェントを使うことが目的であれば、エージェントがよりクリエイティブになり、コンテキスト変数のニュアンスを利用できるように、エージェントの温度を高く設定することができる。センチメントスコアの生成にエージェントを使用している場合は、ネガティブなアンケート回答に対するエージェントの推測を避けるため、温度を低めに設定するのが理想的かもしれない。この設定をテストし、あなたのシナリオに合うようにエージェントが生成する出力を確認することをお勧めする。

{% alert note %}
現在、温度はOpenAIではサポートされていない。
{% endalert %}