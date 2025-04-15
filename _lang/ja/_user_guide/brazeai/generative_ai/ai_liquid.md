---
nav_title: BrazeAI Liquid アシスタント
article_title: BrazeAI Liquid アシスタント
description: "この記事では、AI Liquid アシスタントの仕組みと、それを使用したメッセージング用の Liquid スニペットの生成方法について説明します。"
page_type: reference
page_order: 5
---

# BrazeAI<sup>TM</sup> Liquid アシスタント

> BrazeAI<sup>TM</sup> Liquid アシスタントは BrazeAI<sup>TM</sup> を搭載したチャットアシスタントであり、メッセージコンテンツをパーソナライズするために必要な Liquid を生成する場合に役立ちます。

BrazeAI<sup>TM</sup> Liquid アシスタントを使用すると、テンプレートからの Liquid の生成、パーソナライズされた Liquid の提案の受け取り、および BrazeAI<sup>TM</sup> のサポートを使用した既存の Liquid の最適化ができます。アシスタントには、使用されている Liquid を説明する注釈も用意されているため、Liquid の理解を深めたり、自作方法を学んだりできます。

## サポートされているチャンネル

BrazeAI<sup>TM</sup> Liquid Assistant を使用して以下を作成できます。 
- SMS
- プッシュ通知
- HTMLメールメッセージ
    - アシスタントは、テンプレートではなくメールメッセージで動作し、既に構築されているメールメッセージで最適に動作します。
- Canvases

## 仕組み

BrazeAI<sup>TM</sup> Liquid アシスタントは、お客様のマーケティングニーズに合わせた効果的な Liquid コードの作成を支援するように設計されています。当社の AI は、Liquid の構文、およびマーケターによるメッセージでの Liquid の活用法についてトレーニングされているので、パーソナライズされたコンテンツの作成における微妙な違いを理解しています。さらに、BrazeAI<sup>TM</sup> Liquid アシスタントにカスタム属性名 (「favourite_color」など) とデータ型 (boolean や string など) を指定することで、BrazeAI<sup>TM</sup> Liquid アシスタントにより、正確にメッセージのターゲットが目標に合わされます。さらに、ブランドガイドラインを作成する場合、BrazeAI<sup>TM</sup> Liquid アシスタントはブランドガイドラインを使用して、生成された出力をより適切にカスタマイズたり、コンテンツを自社のブランドボイスにカスタマイズしたりできます。お客様が作成したブランドガイドラインは、お客様自身が使用してコンテンツをパーソナライズするためにのみ使用されます。 

## Liquid コードの生成

BrazeAI<sup>TM</sup>Liquid アシスタントを起動するには、メッセージ作成画面で AI アシスタントアイコンを選択します。

![AI アシスタントを持つメッセージ作成画面。][1]{: style="max-width:50%;"}

[提供されたプロンプト](#provided-prompts)を選択するか、テキストボックスに独自のプロンプトを入力することができます。Liquid コードを生成するには、[**作成ツールを更新**] を選択します。

![プロンプトが表示された AI アシスタントウィンドウ。][2]{: style="max-width:50%;"}
 
同じプロンプトを使用して別のメッセージを生成するには、[**再生成**] を選択します。メッセージを削除して前のメッセージに戻すには、[**更新を元に戻す**] を選択します。

### 提供されるプロンプト

BrazeAI<sup>TM</sup> AI Liquid アシスタントの使用中に、Liquid の使用の開始に役立つさまざまなプロンプトが表示されることがあります。プロンプトの一部を以下に示します。

#### アプリアクティビティを使用

**アプリアクティビティを使用**プロンプトは、アプリが最後に使用された日時に基づいて異なるメッセージを送信するときに役立つ Liquid コードを生成します。アシスタントがより正確な結果を生成できるように、追加の質問を受けることがあります。

![「アプリアクティビティの使用」プロンプトの出力例。][3]{: style="max-width:45%;"}

#### カウントダウンの追加

このプロンプトは、イベントが開始されるまでの時間を含むメッセージを送信する Liquid コードを生成します。イベント日時の詳細を入力するように要求されます。

![「カウントダウンの追加」プロンプトの出力例。][4]{: style="max-width:45%;"}

#### インスピレーションの指定

このプロンプトは、メッセージボックスに内容がある場合に表示されます。Liquid でメッセージをパーソナライズするために選択できるオプションのリストが生成されます。 

![「インスピレーションの指定」プロンプトの出力例。][5]{: style="max-width:45%;"}

#### Liquid を改善

このプロンプトは、メッセージ作成画面に内容がある場合に表示されます。アシスタントでコードをより効率的に読みやすくする場合に選択します。

![「Liquid を改善」プロンプトの出力例。][6]{: style="max-width:45%;"}

## ベータ版でサポートされる属性

| 条件 | ナレッジタイプ |
| - | - |
| Liquid (`for` ループ、`if` ステートメント、数学演算、その他を含む) | コーディング |
| デフォルトおよび標準ユーザー属性 | 属性 |
| 以下のいずれかのデータ型を持つカスタム属性: {::nomarkdown}<ul><li>ブール値</li><li>数値</li><li>文字列</li><li>配列</li><li>時刻</li></ul>{:/} | 属性 |
| コネクテッドコンテンツ | コーディング |
{: .reset-td-br-1 .reset-td-br-2 }

## データはどのように使用されて、OpenAI に送信されるのですか?

メッセージ内容の変更または作成を行うために、Braze ではユーザーが BrazeAI<sup>TM</sup> AI アシスタントに送信したプロンプト、メッセージ、コンテンツ、および / またはブランドガイドライン (ユーザーが作成することを決定した場合) が OpenAI の API プラットフォームに送信されます。Braze から OpenAI に送信されるすべてのクエリは匿名化されます。つまり、提供するコンテンツに一意に識別できる情報を含めない限り、OpenAI はクエリの送信元を特定できません。[OpenAI の API プラットフォームのコミットメント](https://openai.com/policies/api-data-usage-policies)に詳述されているように、Braze 経由で OpenAI の API に送信されたデータは、モデルのトレーニングや改善には使用されず、30 日後に削除されます。お客様に関連する OpenAI のポリシーを必ず遵守してください。これには、OpenAI の[使用ポリシー](https://openai.com/policies/usage-policies)や[共有および公開ポリシー](https://openai.com/policies/sharing-publication-policy)が含まれる場合があります。Braze は AI が生成したコンテンツに関していかなる種類の保証も行いません。

[1]: {% image_buster /assets/img/ai_liquid/ai_assistant_icon.png %}
[2]: {% image_buster /assets/img/ai_liquid/ai_assistant_window.png %}
[3]: {% image_buster /assets/img/ai_liquid/use_app_activity.png %}
[4]: {% image_buster /assets/img/ai_liquid/add_countdown.png %}
[5]: {% image_buster /assets/img/ai_liquid/inspire_me.png %}
[6]: {% image_buster /assets/img/ai_liquid/improve_my_liquid.png %}
