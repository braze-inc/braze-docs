---
nav_title: メッセージング ユーザー
article_title: メッセージング ユーザー
description: "このリファレンス記事では、Brazeがユーザーメッセージをどのように処理するかについて説明します。"
page_type: reference
channel:
  - WhatsApp
page_order: 5.1
alias: /user_guide/message_building_by_channel/whatsapp/quick_replies/

---

# ユーザー・メッセージ

> WhatsAppは双方向のコミュニケーションチャネルです。ブランドはユーザーにメッセージを送るだけでなく、テンプレート化されたキャンペーンやキャンバスを使って会話に参加することができます。これを行うには、WhatsAppクイック返信やトリガーワードなど、さまざまな方法があります。クイック返信の行動喚起(CTA)は、WhatsAppメッセージへのユーザーのエンゲージメントを促進するための優れた方法です。

## アクションベースのトリガー 

キャンペーンとキャンバスはどちらも、トリガーワードなどのインバウンドWhatsAppメッセージ(ユーザーがWhatsAppにメッセージを送信する)から開始、分岐、およびジャーニーの途中での変更を行うことができます。 

トリガーワードが、ユーザーに期待するものと一致していることを確認します。

**知っておきたいこと:**
\- トリガーワードの各文字は、設定時に大文字にする必要があります。Brazeでは、ユーザーが送信したインバウンドトリガーワードを大文字にする必要はありません。たとえば、「jOin2023」というメッセージを送ると、キャンバスまたはキャンペーンがトリガーされます。
\- エントリースケジュールのアクションベースのトリガーでトリガーワードが指定されていない場合、キャンペーンまたはキャンバスはすべての受信WhatsAppメッセージに対して実行されます。これには、アクティブなキャンペーンとキャンバスでフレーズが一致したメッセージが含まれ、その場合、ユーザーは2つのWhatsAppメッセージを受信します。

{% tabs %}
{% tab Campaign %}

![\]({% image_buster /assets/img/whatsapp/whatsapp27.png %})

![\]({% image_buster /assets/img/whatsapp/whatsapp26.png %})

{% endtab %}
{% tab Canvas %}

![\]({% image_buster /assets/img/whatsapp/whatsapp25.png %})

![\]({% image_buster /assets/img/whatsapp/whatsapp24.png %})
{% endtab %}
{% endtabs %}

## 認識されない応答

インタラクティブなキャンバスで認識されない回答のオプションを含めることをお勧めします。これにより、ユーザーは利用可能なプロンプトが何であるかを理解し、チャネルに対する期待値を設定します。期待値管理は、ライブエージェントチャットを備えたWhatsAppチャネルがある場合に特に役立ちます。
\- アクションステップで、カスタムフィルターフレーズのアクショングループを作成した後、「WhatsAppメッセージを送信する」のアクショングループを追加しますが、[ **メッセージ本文の場所]はチェックしません**。これは、"else" 句と同様に、認識されないユーザーの応答をすべてキャッチします。
\- WhatsAppメッセージでフォローアップし、このチャネルには有人がいないことをユーザーに通知し、必要に応じてサポートチャネルに誘導することをお勧めします。 

## クイック返信 

![コールトゥアクションボタンを表示する電話画面は、クリックされたボタンのテキストに返信します。[11]{: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

クイック返信は、会話内でクリック可能なボタンオプションとして表示されますが、ユーザーがテキストで返信したかのように動作します。Brazeはこれらを受信メッセージとして処理し、クリックされたボタンに基づいて設定された応答を送り返すことができます。ユーザーからの応答を作成およびフィルタリングするときに、「受信WhatsAppメッセージアクション」ステップを使用します。

![テキストと 3 つの行動喚起ボタンを表示する WhatsApp メッセージ。[13]{: style="max-width:50%;"}

### Canvas でのクイック返信エクスペリエンスの構成

#### ステップ 1:CTAの構築

まず、メッセージテンプレート内の [WhatsAppメッセージテンプレートマネージャー](https://business.facebook.com/wa/manage/message-templates/) でクイック返信CTAを作成します。 

![CTAボタンの作成方法を示すWhatsAppメッセージテンプレートマネージャーUIで、ボタンタイプ(カスタム)とボタンテキストを提供します。[12]{: style="max-width:80%;"}

テンプレートがWhatsAppによって送信され、承認されたら、それを使用してBraze内でキャンバスを作成できます。 

{% alert tip %}
メッセージテンプレートで承認を受ける前にキャンバスを作成できます。
{% endalert %}

#### ステップ 2:キャンバスを構築する

次に、作成したテンプレートを含むメッセージステップでキャンバスを構築します。 

![][14]

メッセージ ステップに続くアクション ステップを作成します。このアクション ステップでは、クイック返信オプションごとに 1 つのグループを作成します。

![評価アクションが "whatsapp 受信メッセージを送信する" である Canvas。[15]

クイック返信オプショングループごとに、照合するボタンとして正確なテキストを指定します。キーワードは大文字でなければならないことに注意してください。 

![特定のメッセージ本文を受信したときに送信するようにアクション "whatsapp 受信メッセージを送信する" が設定されているキャンバス ステップ。[16]

クイック返信ではなくテキストでメッセージに返信するユーザーに対してデフォルトの返信が必要な場合は、メッセージ本文が一致しない追加のグループを作成します。

この時点から、通常どおりに Canvas の構築を続けます。

### 応答

ほとんどの場合、応答ごとに応答メッセージが必要になります。クイック返信の範囲外の応答には、キャッチオール オプションを用意することをお勧めします (たとえば、事前に定義されたプロンプトではなく一般的なメッセージで応答する顧客の場合)。たとえば、「申し訳ございません。ご回答に心当たりがありませんでした。サポートの問題については、メッセージを送っ <support channel>てください。

![各行動喚起ボタンの応答を示すキャンバスが構築されています。[18]

Braze Canvas が提供する後続のアクション (応答メッセージ、ユーザープロファイルの更新、Braze-to-Braze Webhook など) を使用できます。 

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
