---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 7
alias: /operator/
toc_headers: h2
description: "BrazeAI Operator<sup>TM</sup>へのアクセス方法と使用方法について説明します。これはBrazeダッシュボードに組み込まれたAI搭載のアシスタントで、その機能やベストプラクティスを紹介します。"
---

# BrazeAI Operator

> BrazeAI Operator<sup>TM</sup>は、ダッシュボードに組み込まれたAI搭載のアシスタントです。Operatorは、質問への回答、セットアップの手順案内、問題のトラブルシューティング、アイデアのブレインストーミングなど、さまざまな作業をサポートします。

## Operatorにアクセスする

Brazeダッシュボードの任意のページからOperatorを開きます。  

1. ユーザープロファイルの横にある**BrazeAI Operator<sup>TM</sup>**を選択します。

![ユーザープロファイルの横にあるBrazeAI Operatorアイコン。]({% image_buster /assets/img/operator/operator_icon.png %})

{:start="2"}
2. 画面の右側にOperatorチャットパネルが開きます。

![Operatorチャットパネル。]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
パネルを最大化して読みやすくしたり、最小化して作業中もOperatorを利用可能な状態に保つことができます。  
{% endalert %} 

## Operatorを使用する

自然言語を使って、達成したいことを説明します。プロンプトは、シンプルな質問から複雑なリクエストまで対応できます。

- **シンプル：** Liquidが正しくレンダリングされないのはなぜですか？
- **複雑：** メッセージの`abort_message`タグに、中止の原因となったユーザー属性を含めるにはどうすればよいですか？

Operatorは、ステップバイステップの手順、Brazeドキュメントへのリンク、わかりやすい説明を提供できます。明確で具体的な質問をすることで、より有益な回答が得られます。Operatorは[GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2)を使用しており、強力な推論能力を備え、複雑なマルチステップのタスクに適しています。 

## ベストプラクティス

Operatorを検索エンジンではなく会話として扱いましょう。短く自然なプロンプトが最も効果的です。

- **具体的に：**「キャンバスについて教えてください」ではなく、「キャンバスでアクションパスをどのように使用しますか？」と聞いてみましょう。  
- **フォローアップの質問をする：** 最初の回答がニーズに合わない場合は、明確化や追加の詳細を求めましょう。
- **ページ認識コンテキストを活用する：** OperatorはBraze内での現在の位置を理解します。最も正確な結果を得るために、関連するページを表示しながらOperatorを開きましょう。

## 体験をカスタマイズする

### ブランドガイドラインを適用する

Operatorのクエリにブランドガイドラインをコンテキストとして追加することで、ブランドの声、トーン、パーソナリティに合った回答を得ることができます。Operatorはワークスペースで設定されたブランドガイドラインを使用するため、コピーの提案や機能の説明時に一貫したメッセージングを確保できます。

ブランドガイドラインを設定するには、**設定** > **ブランドガイドライン**に移動します。詳細については、[ブランドガイドライン]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/)を参照してください。

![Operatorチャットパネルでのブランドガイドラインの選択。]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### ページ認識コンテキストを活用する

Operatorは、Braze内での現在の位置を自動的に理解し、そのコンテキストに基づいて回答を調整します。たとえば、キャンバスの作成中にOperatorを開くと、ワークフローのどこにいるかを説明しなくても、関連するステップを提案したり、キャンバス機能についてのガイダンスを提供したりできます。

このコンテキスト認識により、「キャンバスワークフローに遅延ステップを追加するにはどうすればよいですか？」ではなく、「遅延を追加するにはどうすればよいですか？」のように、より短く自然な質問ができます。

## Operatorの回答を活用する

### 推奨プロンプトから始める

Operatorを開くと、一般的なタスクと現在のページに基づいて推奨プロンプトが表示されます。すぐに始めるにはプロンプトを選択するか、独自の質問を入力します。

### Operatorの思考プロセスを理解する

Operatorは、**Reasoned**とラベル付けされた折りたたみ可能なセクションに推論ステップを表示します。ドロップダウンを選択してこれらのセクションを展開し、Operatorがどのように回答を導き出したかを確認できます。提案の背後にあるロジックを理解したり、アプローチを検証したりする際に役立ちます。

![Operatorの回答内の折りたたまれた「Reasoned」ドロップダウン。]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Operatorでアクションを実行する

Operatorは、フォームフィールドの入力、設定の更新、コンテンツの生成など、Brazeダッシュボードで直接変更を提案・実行できます。提案された変更はそれぞれアクションカードとして表示され、適用前に確認・承認できます。この仕組みの詳細については、[アクションの確認]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/)を参照してください。

## セッションを管理する

### 回答を停止する

Operatorが回答を生成している間、**Send**ボタンは**Stop**ボタンに変わります。質問を言い換えたい場合や、回答が意図しない方向に進んでいる場合は、**Stop**を選択して回答を早期に終了できます。

### 履歴をクリアする

最初からやり直したい場合や、会話から機密情報を削除したい場合は、**チャット履歴をクリア**を選択します。これにより、現在のすべてのコンテンツが削除され、会話のコンテキストがリセットされます。

### フィードバックを提供する

各回答の下部にある、サムズアップまたはサムズダウンボタンを使って、素早くフィードバックを提供できます。フィードバックは、Operatorの回答を継続的に改善するのに役立ちます。

## データプライバシーとセキュリティ

### HIPAAコンプライアンス

AI Operatorは、現在OpenAIのZero Data Retentionポリシーの対象外であるマルチターン会話テクノロジーを使用しています。AI OperatorはOpenAIのModified Abuse Monitoringデータリテンションポリシーを使用していますが、AI OperatorはBrazeとOpenAI間のBusiness Associate Agreement（BAA）の対象外です。ユーザーは、AI OperatorにBrazeに保存されているProtected Health Information（PHI）へのアクセスを要求したり、PHIをこの機能に送信したりしないでください。

### サブプロセッサまたはサードパーティプロバイダーとしてのモデルプロバイダー

Brazeサービス（「Braze提供のLLM」）を通じてBrazeが提供するLLMプロバイダーとの統合を使用する場合、当該Braze提供のLLMのプロバイダーは、お客様とBraze間のData Processing Addendum（DPA）の条件に従い、Brazeのサブプロセッサとして機能します。BrazeAI Operator<sup>TM</sup>はOpenAIと統合されています。

### OpenAIでのデータの使用方法

OpenAIを活用するBrazeAI機能を通じてAI出力（「Output」）を生成するために、Brazeは特定の情報（「Input」）をOpenAIに送信します。Inputは、プロンプト、ダッシュボードに表示されるコンテンツ、およびクエリに関連するワークスペースデータで構成されます。[OpenAIのAPIプラットフォームコミットメント](https://openai.com/enterprise-privacy/)に基づき、Brazeを介してOpenAIのAPIに送信されるデータは、OpenAIモデルのトレーニングや改善には使用されません。お客様とBrazeの間では、Outputはお客様の知的財産です。Brazeは、当該Outputに関する著作権の所有権を主張しません。Brazeは、Outputを含むAI生成コンテンツに関して、いかなる種類の保証も行いません。

## 次のステップ

- [アクションの確認]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/)：Operatorが提案した変更を確認・承認する方法を学びます
- [サポートチケットの提出]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets/)：Operatorから直接サポートチケットを提出します
- [トラブルシューティング]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/)：一般的な問題とソリューションを参照します