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

> WhatsAppは双方向のコミュニケーションチャネルだ。あなたのブランドはユーザーにメッセージを送ることができるだけでなく、テンプレート化されたキャンペーンやCanvasesを使ってユーザーと会話をすることができる。WhatsAppのクイック返信やトリガーワードなど、様々な方法がある。クイック返信コールトゥアクション(CTA)はWhatsAppメッセージのユーザーエンゲージメントを促進する優れた方法。

## アクションベースのトリガー 

キャンペーンもキャンバスも、WhatsAppのインバウンドメッセージ（ユーザーがあなたのWhatsAppにメッセージを送ること）をトリガーワードとして、開始、分岐、途中変更を行うことができる。 

トリガー・ワードが、ユーザーから期待されているものと一致していることを確認する。

**知っておくべきこと**
- トリガー・ワードの各文字は大文字で構成されなければならない。Brazeは、ユーザーが送信するインバウンドのトリガーワードを大文字にする必要はない。例えば、"jOin2023 "とメッセージを送っても、キャンバスやキャンペーンはトリガーされる。
- エントリースケジュールのアクションベーストリガーにトリガーワードが指定されていない場合、キャンペーンまたはキャンバスは全てのインバウンドメッセージに対して実行される。これには、アクティブなキャンペーンやキャンバスでフレーズが一致したメッセージも含まれ、この場合、ユーザーは2通のWhatsAppメッセージを受け取ることになる。

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

インタラクティブ・キャンバスでは、認識できない回答に対するオプションを含めることを推奨する。これは、利用可能なプロンプトが何であるかをユーザーに理解させ、チャンネルに対する期待値を設定するものである。ライブエージェントチャット付きのWhatsAppチャンネルがあれば、期待値管理は特に役立つ。 
- アクションステップで、カスタムフィルターフレーズのアクショングループを作成した後、「WhatsAppメッセージを送信」のための追加のアクショングループを追加しますが、**メッセージ本文を確認しないでください**。これは、"else "節と同様に、認識できないユーザー・レスポンスをすべてキャッチする。 
- WhatsAppのメッセージで、このチャンネルが有人ではないことをユーザーに伝え、必要であればサポートチャンネルを案内することをお勧めする。 

## 迅速な回答 

![コール・トゥ・アクションのボタンが表示されている電話画面では、クリックされたボタンのテキストが返信される。][11]{: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

クイック返信は、会話内でクリック可能なボタンオプションとして表示されるが、ユーザーがテキストで返信したかのように動作する。そして、Brazeはこれらをインバウンドメッセージとして処理し、クリックされたボタンに基づいたセットレスポンスを送り返すことができる。WhatsAppメッセージ受信アクション "ステップを使用して、ユーザーからの返信を作成し、フィルタリングする。

![WhatsAppメッセージにはテキストと3つの行動喚起ボタンが表示されている。][13]{: style="max-width:50%;"}

### キャンバスでクイックリプライの経験を設定する

#### ステップ 1:CTAを構築する

まず、[WhatsAppメッセージテンプレートマネージャーで](https://business.facebook.com/wa/manage/message-templates/)メッセージテンプレート内にクイックリプライCTAを作成する。 

![WhatsAppメッセージテンプレートマネージャーのUIでCTAボタンの作成方法、ボタンタイプ(カスタム)、ボタンテキストを確認できる。][12]{: style="max-width:80%;"}

テンプレートが提出され、WhatsAppによって承認されると、そのテンプレートを使ってBraze内でCanvasを構築することができる。 

{% alert tip %}
メッセージテンプレートの承認を受ける前にキャンバスを構築することができる。
{% endalert %}

#### ステップ 2:キャンバスを作成する

次に、作成したテンプレートを含むメッセージ・ステップでキャンバスを構築する。 

![][14]

メッセージステップに続くアクションステップを作成する。このアクションステップでは、クイック返信オプションごとに1つのグループを作成する。

![評価アクションが「whatsappの受信メッセージを送信」であるキャンバス。][15]

各クイック返信オプション・グループに対して、マッチさせるボタンとして正確なテキストを指定する。キーワードは大文字でなければならない。 

![キャンバスのステップで、「whatsapp受信メッセージを送信する」というアクションが、特定のメッセージ本文を受信したときに送信されるように設定されている。][16]

クイック返信の代わりにテキストで返信するユーザーに対してデフォルトの返信をしたい場合は、メッセージ本文が一致しないグループを追加で作成する。

この時点から、通常通りにキャンバスを作り続ける。

### 回答

各レスポンスに返信メッセージが欲しい場合がほとんどだろう。私たちは、クイック返信の範囲外の回答（たとえば、あらかじめ決められたプロンプトではなく、一般的なメッセージで回答する顧客など）のために、キャッチオールオプションを用意することを推奨する。例えば、「申し訳ありません、あなたの返答に気づきませんでした。サポートに関する問題は、<support channel> 。"

![それぞれのコールトゥアクションボタンに対する反応を示すキャンバスが構築された。][18]

応答メッセージ、ユーザープロファイルの更新、Braze-to-Brazeウェブフックなど、Braze Canvasが提供する後続のアクションを使用できることに注意すること。 

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
