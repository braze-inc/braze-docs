---
nav_title: AIリキッドアシスタント
article_title: AIリキッドアシスタント
description: "本稿では、Sage AI Liquid Assistant の仕組みと、メッセージング用のLiquid スニペットの生成方法について説明します。"
page_type: reference
page_order: 5
---

# AI Liquidアシスタント

> Sage AI Liquid Assistant は、Sage AI を搭載したチャットアシスタントで、メッセージコンテンツをパーソナライズするために必要なLiquid を生成するのに役立ちます。 

AI Liquid Assistant を使用すると、テンプレート s からLiquid を生成したり、パーソナライズされた Liquid の提案を受信したり、Sage AI を使用して既存のLiquid を最適化したりできます。AI Liquid Assistant には、使用されているLiquid を説明するアノテーションも用意されているため、Liquid について理解を深め、自分で書くことを学ぶことができます。

{% alert important %}
AIリキッドアシスタントは現在、プッシュ型およびSMS型のチャネルを積極的に利用している限られた顧客のためにベータ版に入っている。ベータの検討を希望する場合は、顧客のサクセスマネージャーに連絡するか、この[ポータルカード](https://braze.productboard.com/entity-detail/features/27273918)に関心を示します。
{% endalert %}

## その仕組み

AI Liquid Assistant は、マーケティングのニーズに合わせて効果的なLiquid コードを作成するのに役立ちます。リキッドのシンタックスとマーケター s がリキッドをどのように使っているかの両方についてトレーニングを受け、私たちのAI はパーソナライズされた内容の作り方のニュアンスを理解しています。さらに、AI Liquid Assistant にカスタム属性の名前(`favourite_color` など) とデータ型(ブール値や文字列など) を提供することで、AI Assistant によってメッセージが正確にターゲット設定され、目標と整合性がとれていることが保証されます。

## リキッドコードの生成

AI Liquid Assistant を起動するには、メッセージ作成画面でAI Assistant アイコンを選択します。

![AI アシスタントを持つメッセージコンポーザー。][1]{: style="max-width:50%;"}

[提供されたプロンプト](#provided-prompts)を選択するか、テキストボックスに独自の情報を入力することができます。リキッドコードを生成するには、**コンポーザーの更新**を選択します。

![AI アシスタントウィンドウ。プロンプトが表示されます。][2]{: style="max-width:50%;"}
 
同じプロンプトを使用して別のメッセージを生成するには、**Regenerate**を選択します。メッセージを削除して前のメッセージに戻すには、**更新を元に戻します**を選択します。

### 提供されるプロンプト

AI Liquid Assistant の使用中に、Liquid の使用を開始するためのさまざまなプロンプトが表示されることがあります。プロンプトの一部を以下に示します。

#### アプリ活動を利用する

**アプリアクティビティを使用**プロンプトは、アプリが最後に使用された日時に基づいてさまざまなメッセージを送信するのに役立つリキッドコードを生成します。アシスタントがより多くのキュレートを得ることができるように、フォローアップ質問を受けることがあります。

!["Use アプリ activity"プロンプトの出力例。][3]{: style="max-width:45%;"}

#### カウントダウンの追加

このプロンプトは、イベントhがアプリするまでの時間を示すメッセージを送信するリキッドコードを生成します。イベント日時の詳細をお聞きします。

!["Add countdown"プロンプトの出力例。][4]{: style="max-width:45%;"}

#### インスパイア・ミー

このプロンプトアプリは、メッセージボックスに内容がある場合に表示されます。Liquidでメッセージをパーソナライズするために選択できるオプションのリストが生成されます。 

!["Inspire me"プロンプトの出力例。][5]{: style="max-width:60%;"}

#### リキッドの改良

このプロンプトアプリは、メッセージ作成画面に内容がある場合に有効になります。アシスタントがコードをより効率的に読みやすくする場合に選択します。

![&quot の出力例;Liquid"prompt を改善します。][6]{: style="max-width:45%;"}

## ベータ版でサポートされる属性

| 条件| ナレッジタイプ|
| - | - |
| 液体(`for` ループ、`if` ステートメント、数学、その他を含む) | コーディング|
| 既定および規格のユーザー 属性 s | 属性s |
| 以下のいずれかのデータタイプを持つカスタム属性s: {::nomarkdown}<ul><li>ブール値</li><li>数値</li><li>文字列</li><li>配列</li><li>時刻</li></ul>{:/} | 属性|
| 接続されたコンテンツ| コーディング|
{: .reset-td-br-1 .reset-td-br-2 }

## データはどのように使用されて、OpenAI に送信されるのですか?

メッセージの内容を変更または作成するには、Braze はプロンプト、メッセージ、およびOpenAI のAPI プラットフォームにLiquid AI Assistant に送信されたコンテンツを送信します。Braze から OpenAI に送信されるすべてのクエリは匿名化されます。つまり、提供するコンテンツに一意に識別できる情報を含めない限り、OpenAI はクエリの送信元を特定できません。[OpenAI のAPI プラットフォーム コミットメント](https://openai.com/policies/api-data-usage-policies)に詳述されているように、Braze を介してOpenAI のAPI に送信されるデータは、モデルのトレーニングや改善には使用されず、30 日後に削除されます。[Usage policies](https://openai.com/policies/usage-policies) とその[Sharing & publication policy](https://openai.com/policies/sharing-publication-policy) が含まれている可能性がある、ユーザーに関連するOpenAI のポリシーを遵守してください。Braze は、AI が生成した内容に関していかなる保証も行いません

[1]: {% image_buster /assets/img/ai_liquid/ai_assistant_icon.png %}
[2]: {% image_buster /assets/img/ai_liquid/ai_assistant_window.png %}
[3]: {% image_buster /assets/img/ai_liquid/use_app_activity.png %}
[4]: {% image_buster /assets/img/ai_liquid/add_countdown.png %}
[5]: {% image_buster /assets/img/ai_liquid/inspire_me.png %}
[6]: {% image_buster /assets/img/ai_liquid/improve_my_liquid.png %}