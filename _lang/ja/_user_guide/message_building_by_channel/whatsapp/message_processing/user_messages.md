---
nav_title: ユーザーへのメッセージング
article_title: ユーザーへのメッセージング
description: "この参考記事では、Brazeがユーザーメッセージをどのように扱うかについて説明している。"
page_type: reference
channel:
  - WhatsApp
page_order: 5.1
alias: /user_guide/message_building_by_channel/whatsapp/quick_replies/

---

# ユーザーメッセージ

> WhatsAppは双方向のコミュニケーションチャネルだ。あなたのブランドはユーザーにメッセージを送ることができるだけでなく、テンプレート化されたキャンペーンやCanvasesを使ってユーザーと会話をすることができる。WhatsAppのクイック返信やトリガーワードなど、様々な方法がある。クイック返信コールトゥアクション (CTA) は、WhatsApp メッセージのユーザーエンゲージメントを促進する優れた方法です。

## アクションベースのトリガー 

キャンペーンとキャンバスはどちらも、トリガーワードなどのインバウンド WhatsApp メッセージ (ユーザーからの WhatsApp メッセージ) から、開始、分岐、および中間ジャーニーの変更を行うことができます。 

トリガー・ワードが、ユーザーから期待されているものと一致していることを確認する。

**知っておくべきこと**
- トリガーワードの各文字は設定時に大文字にする必要があります。Braze では、ユーザーが送信するインバウンドトリガーワードを大文字にする必要はありません。例えば、"jOin2023 "とメッセージを送っても、キャンバスやキャンペーンはトリガーされる。
- エントリスケジュールのアクションベーストリガーにトリガーワードが指定されていない場合、キャンペーンまたはキャンバスはすべてのインバウンドメッセージに対して実行されます。これには、アクティブなキャンペーンやキャンバスでフレーズが一致したメッセージも含まれ、この場合、ユーザーは2通のWhatsAppメッセージを受け取ることになる。

{% tabs %}
{% tab キャンペーン %}

![]({% image_buster /assets/img/whatsapp/whatsapp27.png %})

![]({% image_buster /assets/img/whatsapp/whatsapp26.png %})

{% endtab %}
{% tab キャンバス %}

![]({% image_buster /assets/img/whatsapp/whatsapp25.png %})

![]({% image_buster /assets/img/whatsapp/whatsapp24.png %})
{% endtab %}
{% endtabs %}

## 認識されない応答

インタラクティブ・キャンバスでは、認識できない回答に対するオプションを含めることを推奨する。これは、利用可能なプロンプトが何であるかをユーザーに理解させ、チャネルに対する期待事項を設定するものです。ライブエージェントチャット付きのWhatsAppチャンネルがあれば、期待値管理は特に役立つ。 
- アクションステップで、カスタムフィルターフレーズのアクショングループを作成した後、「WhatsApp メッセージを送信」のための追加のアクショングループを追加しますが、**メッセージ本文の場所はチェックしないでください**。これは、"else "節と同様に、認識できないユーザー・レスポンスをすべてキャッチする。 
- WhatsAppのメッセージで、このチャンネルが有人ではないことをユーザーに伝え、必要であればサポートチャンネルを案内することをお勧めする。 

## クイック返信 

![コール・トゥ・アクションのボタンが表示されている電話画面では、クリックされたボタンのテキストが返信される。][11]{: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

クイック返信は、会話内でクリック可能なボタンオプションとして表示されるが、ユーザーがテキストで返信したかのように動作する。そして、Braze はこれらをインバウンドメッセージとして処理し、クリックされたボタンに基づいて設定済みのレスポンスを送り返すことができます。"インバウンド WhatsApp メッセージアクション "ステップを使用して、ユーザーからの返信を作成し、フィルタリングします。

![WhatsAppメッセージにはテキストと3つの行動喚起ボタンが表示されている。][13]{: style="max-width:50%;"}

### キャンバスでクイック返信エクスペリエンスを設定する

#### ステップ 1: CTA を構築する

まず、[WhatsApp メッセージテンプレートマネージャー](https://business.facebook.com/wa/manage/message-templates/)でメッセージテンプレート内にクイック返信 CTA を設定します。 

![WhatsAppメッセージテンプレートマネージャーのUIでCTAボタンの作成方法、ボタンタイプ(カスタム)、ボタンテキストを確認できる。][12]{: style="max-width:80%;"}

テンプレートが提出され、WhatsAppによって承認されると、そのテンプレートを使ってBraze内でCanvasを構築することができる。 

{% alert tip %}
メッセージテンプレートの承認を受ける前にキャンバスを構築することができる。
{% endalert %}

#### ステップ 2: キャンバスを作成する

次に、作成したテンプレートを含むメッセージ・ステップでキャンバスを構築する。 

![][14]

メッセージステップに続くアクションステップを作成する。このアクションステップでは、クイック返信オプションごとに1つのグループを作成する。

![評価アクションが「whatsappの受信メッセージを送信」であるキャンバス。][15]

各クイック返信オプション・グループに対して、マッチさせるボタンとして正確なテキストを指定する。キーワードは大文字でなければなりません。 

![キャンバスのステップで、「whatsapp受信メッセージを送信する」というアクションが、特定のメッセージ本文を受信したときに送信されるように設定されている。][16]

クイック返信の代わりにテキストで返信するユーザーに対してデフォルトの返信をしたい場合は、メッセージ本文が一致しないグループを追加で作成する。

この時点から、通常通りにキャンバスの設定を続けます。

### 回答

各レスポンスに返信メッセージが欲しい場合がほとんどだろう。クイック返信の範囲外 (あらかじめ決められたプロンプトではなく、一般的なメッセージで返信する顧客の場合など) の返信には、catch-all オプションを使用することをお勧めします。例えば、「申し訳ありません、あなたの返答に気づきませんでした。サポートに関する問題は、<support channel> というメッセージをお送りください。」

![それぞれのコールトゥアクションボタンに対する反応を示すキャンバスが構築された。][18]

レスポンス内のメッセージ、ユーザープロファイルの更新、Braze-to-Braze Webhook など、Braze キャンバスが提供する後続のアクションを使用できることに注意してください。 

[1]: {% image_buster /assets/img/whatsapp/whatsapp24.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp25.png %}
[3]: {% image_buster /assets/img/whatsapp/whatsapp26.png %}
[4]: {% image_buster /assets/img/whatsapp/whatsapp27.png %} 

[11]: {% image_buster /assets/img/whatsapp/whatsapp11.png %}
[12]: {% image_buster /assets/img/whatsapp/whatsapp12.png %}
[13]: {% image_buster /assets/img/whatsapp/whatsapp13.png %}
[14]: {% image_buster /assets/img/whatsapp/whatsapp14.png %}
[15]: {% image_buster /assets/img/whatsapp/whatsapp15.png %}
[16]: {% image_buster /assets/img/whatsapp/whatsapp16.png %}
[17]: {% image_buster /assets/img/whatsapp/whatsapp17.png %}
[18]: {% image_buster /assets/img/whatsapp/whatsapp18.png %}
