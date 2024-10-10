---
nav_title: BrazeAIリキッドアシスタント
article_title: BrazeAIリキッドアシスタント
description: "この記事では、AI Liquid Assistant の仕組みと、メッセージング用のLiquid スニペットを生成するためのAI Liquid Assistant の使用方法について説明します。"
page_type: reference
page_order: 5
---

# BrazeAI<sup>TM</sup> 液体アシスタント

> BrazeAI<sup>TM</sup> Liquid Assistant は、BrazeAI<sup>TM</sup> を搭載したチャットアシスタントで、メッセージコンテンツをパーソナライズするために必要なLiquid の生成に役立ちます。SMS メッセージの作成、プッシュ通知、HTML メールキャンペーン、およびキャンバスの作成時に使用できます。メールチャネルの場合、アシスタントはテンプレートではなくメールメッセージで動作し、既に構築されているメールメッセージで最適に動作します。

BrazeAI<sup>TM</sup> Liquid Assistant を使用すると、テンプレートからLiquid を生成したり、パーソナライズされたLiquid の提案を受信したり、BrazeAI<sup>TM</sup> をサポートして既存のLiquid を最適化したりすることができます。アシスタントには、使用されている液体を説明するアノテーションも用意されているため、Liquid についての理解を深め、自分で書くことを学ぶことができます。

## その仕組み

BrazeAI<sup>TM</sup> Liquid Assistant は、お客様のマーケティングニーズに合わせた効果的なLiquid コードの作成を支援するよう設計されています。リキッドのシンタックスと、マーケターがリキッドをどのようにメッセージに活用するかの両方についてトレーニングを受け、私たちのAIはパーソナライズされたコンテンツを作り上げるニュアンスを理解しています。さらに、BrazeAI<sup>TM</sup> Liquid Assistant にカスタム属性名("favourite_color" など) とデータ型(boolean やstring など) を指定することで、BrazeAI<sup>TM</sup> Liquid Assistant を使用することで、メッセージが正確にターゲット設定され、目標に合わせて調整されます。さらに、ブランド・ガイドラインを作成する場合、BrazeAI<sup>TM</sup>Liquid Assistantは、ブランド・ガイドラインを使用して、生成された出力をより適切にカスタマイズし、コンテンツを自社のブランド・ボイスにカスタマイズすることができる。あなたが作成したブランドガイドラインは、あなた自身の使用のためにコンテンツをパーソナライズするためにのみ使用されます。 

## Liquid コードの生成

BrazeAI<sup>TM</sup>Liquid assistantを起動するには、メッセージコンポーザーでAI assistantアイコンを選択します。

![AI アシスタントを持つメッセージ作成画面。][1]{: style="max-width:50%;"}

[提供されたプロンプト](#provided-prompts)を選択するか、テキストボックスに独自の情報を入力することができます。Liquid コードを生成するには、\[**作成ツールを更新**] を選択します。

![プロンプトが表示された AI アシスタントウィンドウ。][2]{: style="max-width:50%;"}
 
同じプロンプトを使用して別のメッセージを生成するには、**Regenerate**を選択します。メッセージを削除して前のメッセージに戻すには、**Undo update** を選択します。

### 提供されるプロンプト

BrazeAI<sup>TM</sup> Liquid Assistant の使用中に、Liquid の使用を開始するためのさまざまなプロンプトが表示されることがあります。プロンプトの一部を以下に示します。

#### アプリアクティビティを使用

**Use app activity** プロンプトは、アプリが最後に使用された日時に基づいて異なるメッセージを送信するのに役立つLiquid コードを生成します。アシスタントがより正確な結果を得ることができるように、フォローアップの質問を受けることがあります。

![「アプリアクティビティの使用」プロンプトの出力例。][3]{: style="max-width:45%;"}

#### カウントダウンの追加

このプロンプトは、イベントが開始されるまでの時間を含むメッセージを送信する Liquid コードを生成します。イベント日時の詳細を入力するように要求されます。

!["Add countdown"プロンプトの出力例。][4]{: style="max-width:45%;"}

#### インスピレーションの指定

このプロンプトは、メッセージボックスに内容がある場合に表示されます。Liquidでメッセージをパーソナライズするために選択できるオプションのリストが生成されます。 

!["Inspire me"プロンプトの出力例。][5]{: style="max-width:45%;"}

#### Liquid を改善

このプロンプトは、メッセージ作成画面に内容がある場合に表示されます。アシスタントがコードをより効率的に読みやすくする場合に選択します。

![「Liquid を改善」プロンプトの出力例。][6]{: style="max-width:45%;"}

## ベータでサポートされる属性

| 条件 | ナレッジタイプ |
| - | - |
| 液体(`for` ループ、`if` ステートメント、数学、その他を含む) | コーディング|
| デフォルトおよび標準ユーザー属性| 属性|
| 以下のいずれかのデータ型を持つカスタム属性: {::nomarkdown}<ul><li>ブール値</li><li>数値</li><li>文字列</li><li>配列</li><li>時刻</li></ul>{:/} | 属性 |
| 接続されたコンテンツ| コーディング|
{: .reset-td-br-1 .reset-td-br-2 }

## データはどのように使用されて、OpenAI に送信されるのですか?

メッセージコンテンツを変更または作成するために、Braze は、BrazeAI<sup>TM</sup> AI アシスタントに送信されたプロンプト、メッセージコンテンツ、ブランドガイドライン(作成する場合) をOpenAI のAPI プラットフォームに送信します。Braze から OpenAI に送信されるすべてのクエリは匿名化されます。つまり、提供するコンテンツに一意に識別できる情報を含めない限り、OpenAI はクエリの送信元を特定できません。[OpenAIのAPIプラットフォームコミットメント](https://openai.com/policies/api-data-usage-policies)に詳述されているように、Braze経由でOpenAIのAPIに送信されるデータは、モデルのトレーニングや改良には使用されず、30日後に削除されます。[Usage policies](https://openai.com/policies/usage-policies) とその[Sharing & publication policy](https://openai.com/policies/sharing-publication-policy) を含む、OpenAI の関連ポリシーを遵守してください。Braze は AI が生成したコンテンツに関していかなる種類の保証も行いません。

[1]: {% image_buster /assets/img/ai_liquid/ai_assistant_icon.png %}
[2]: {% image_buster /assets/img/ai_liquid/ai_assistant_window.png %}
[3]: {% image_buster /assets/img/ai_liquid/use_app_activity.png %}
[4]: {% image_buster /assets/img/ai_liquid/add_countdown.png %}
[5]: {% image_buster /assets/img/ai_liquid/inspire_me.png %}
[6]: {% image_buster /assets/img/ai_liquid/improve_my_liquid.png %}
