---
nav_title: AIコピーライティング・アシスタント
article_title: AIコピーライティング・アシスタント
page_order: 4
description: "この参考記事では、OpenAIのGPTコピー生成ツールに簡単な商品名や説明を渡すことで、メッセージングに使用する人間のようなマーケティングコピーを生成する機能、AIコピーライティングアシスタントについて説明します。"
---

# AIコピーライティング・アシスタント

> AIコピーライティングアシスタントは、OpenAIが所有するサードパーティプロバイダのGPTコピー生成ツールに簡単な製品名や説明を渡し、メッセージングに使用する人間のようなマーケティングコピーを生成します。この機能は、Brazeダッシュボードのほとんどのメッセージ作成者でデフォルトで利用可能です。

## ステップ:

AIコピーライティングアシスタントを使用してコピーを生成するには、以下の手順に従ってください：

1. メッセージ作成ツールから、<i class="fa-solid fa-wand-magic-sparkles"></i> **Launch AI Copywriter** を選択します。
   * アプリ内メッセージのドラッグアンドドロップエディターで、テキストブロックを選択して <i class="fa-solid fa-wand-magic-sparkles" title="AIコピーライター"></i>を選択します。
2. 入力フィールドに製品名または説明を入力します。
3. 出力言語を選択します。これは入力言語とは異なる場合がある。
4. 利用可能なオプションからメッセージトーンを選択します。これにより、生成されるコピーのスタイルが決まる。
5. おおよその出力長を選択する。 
6. **コピーを作成**」をクリックする。

応答はOpenAIから取得され、あなたに提供されます。自由に実験し、心ゆくまでバリエーションを試してほしい。 

AIコピーライティングアシスタントモーダル：「マーケティングを次のレベルに引き上げたいとお考えですか？Brazeマーケティングオートメーションはあなたのためのソリューションです！当社の強力なツールを使えば、マーケティングキャンペーンの作成、送信、追跡を簡単に行うことができます。では、なぜ待つのか？今すぐ申し込んで、結果をご自身でお確かめください！"][1]。{: style="max-width:70%;"}

私たちが裏で行うのは、GPTに指示して、ご希望のフォーマットで商品名や商品説明のクリエイティブ広告を生成してもらうことだけです。それ以外のカスタマイズは行わない。あとはGPTのマジックだ！ 

{% alert important %}
OpenAIの[コンテンツポリシーに](https://beta.openai.com/docs/usage-guidelines/content-policy)違反する不快な内容の回答はフィルタリングで除外します。
{% endalert %}

## GPTとは？

[GPTは](https://openai.com/product/gpt-4)、人工知能を搭載したOpenAIの最先端の自然言語生成ツールです。テキスト生成、補完、分類など、さまざまな自然言語タスクを実行できる。Brazeのダッシュボードに接続することで、作業中に直接コピーをインスパイアし、多様化させることができます。

## 私のデータはどのように使用され、OpenAIに送信されるのですか？

コピーを生成するために、BrazeはOpenAIにクエリーを送信します。BrazeからOpenAIに送信されるクエリはすべて匿名化されます。つまり、お客様が提供する入力に個人を特定できる情報が含まれていない限り、OpenAIはそのクエリが誰から送信されたものかを特定することはできません。[OpenAIのポリシー](https://openai.com/policies/api-data-usage-policies)により、Braze経由でOpenAIのAPIに送信されたデータは、モデルのトレーニングや改良には使用されず、30日後に削除されます。お客様とBrazeの間で、GPTを使用して生成されたコンテンツは、お客様の知的財産です。Brazeは、かかるコンテンツの著作権所有権を主張せず、AIが生成したコンテンツに関していかなる保証も行いません。

## その他のAIツール

メディアライブラリから[AIを使って画像を生成]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#generate-ai)することもできる。これは、自然言語による記述からリアルな画像やアートを作成できるオープンエイのAIシステム、DALL-E 2を活用している。

[1]: {% image_buster /assets/img/ai_copywriter/gpt3.png %} 「GPT3
