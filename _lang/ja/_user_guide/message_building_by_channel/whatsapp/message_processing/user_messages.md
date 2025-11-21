---
nav_title: メッセージング・ユーザー
article_title: ユーザーへのメッセージング
description: "この参考記事では、Brazeがユーザーメッセージをどのように扱うかについて説明している。"
page_type: reference
channel:
  - WhatsApp
page_order: 5.1
alias: /whatsapp_quick_replies/

---

# ユーザーメッセージ

> WhatsAppは双方向のコミュニケーションチャネルだ。あなたのブランドはユーザーにメッセージを送ることができるだけでなく、テンプレート化されたキャンペーンやCanvasesを使ってユーザーと会話をすることができる。これには、WhatsAppのクイック返信、リストメッセージ、トリガワードなど、さまざまな方法があります。Quick Reply and list message calls-to-action (CTA) は、WhatsApp メッセージングへのユーザーの関与を促す素晴らしい方法です。

## アクションベースのトリガー 

キャンペーンとキャンバスはどちらも、トリガーワードなどのインバウンド WhatsApp メッセージ (ユーザーからの WhatsApp メッセージ) から、開始、分岐、および中間ジャーニーの変更を行うことができます。 

トリガー・ワードが、ユーザーから期待されているものと一致していることを確認する。

**知っておくべきこと**
- トリガーワードの各文字は設定時に大文字にする必要があります。Braze では、ユーザーが送信するインバウンドトリガーワードを大文字にする必要はありません。例えば、"jOin2023 "とメッセージを送っても、キャンバスやキャンペーンはトリガーされる。
- エントリスケジュールのアクションベーストリガーにトリガーワードが指定されていない場合、キャンペーンまたはキャンバスはすべてのインバウンドメッセージに対して実行されます。これには、アクティブなキャンペーンやキャンバスでフレーズが一致したメッセージも含まれ、この場合、ユーザーは2通のWhatsAppメッセージを受け取ることになる。

{% tabs %}
{% tab Campaign %}

![アクションベースのキャンペーンスケジュールオプション。]({% image_buster /assets/img/whatsapp/whatsapp27.png %})

{% endtab %}
{% tab Canvas %}

![アクションベースのキャンバススケジュールオプション。]({% image_buster /assets/img/whatsapp/whatsapp25.png %})

{% endtab %}
{% endtabs %}

## 認識されない応答

インタラクティブ・キャンバスでは、認識できない回答に対するオプションを含めることを推奨する。これは、利用可能なプロンプトが何であるかをユーザーに理解させ、チャネルに対する期待事項を設定するものです。ライブエージェントチャット付きのWhatsAppチャンネルがあれば、期待値管理は特に役立つ。 
- アクションステップで、カスタムフィルターフレーズのアクショングループを作成した後、「WhatsApp メッセージを送信」のための追加のアクショングループを追加しますが、**メッセージ本文の場所はチェックしないでください**。これは、"else "節と同様に、認識できないユーザー・レスポンスをすべてキャッチする。 
- WhatsAppのメッセージで、このチャンネルが有人ではないことをユーザーに伝え、必要であればサポートチャンネルを案内することをお勧めする。 

## クイック返信 

![コールトゥアクションボタンが表示されている電話画面では、クリックされたボタンのテキストが返信される。]({% image_buster /assets/img/whatsapp/whatsapp11.png %}){: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

クイック返信は、会話内でクリック可能なボタンオプションとして表示されるが、ユーザーがテキストで返信したかのように動作する。そして、Braze はこれらをインバウンドメッセージとして処理し、クリックされたボタンに基づいて設定済みのレスポンスを送り返すことができます。"インバウンド WhatsApp メッセージアクション "ステップを使用して、ユーザーからの返信を作成し、フィルタリングします。

![WhatsAppメッセージにテキストと3つのアクションボタンが表示されている。]({% image_buster /assets/img/whatsapp/whatsapp13.png %}){: style="max-width:50%;"}

### キャンバスでのクイック返信エクスペリエンスの設定

#### ステップ 1: CTA を構築する

まず、[WhatsApp メッセージテンプレートマネージャー](https://business.facebook.com/wa/manage/message-templates/)でメッセージテンプレート内にクイック返信 CTA を設定します。 

![WhatsApp メッセージテンプレートマネージャーのUIでCTAボタンの作成方法、ボタンタイプ(カスタム)、ボタンテキストを確認できる。]({% image_buster /assets/img/whatsapp/whatsapp12.png %}){: style="max-width:80%;"}

テンプレートが提出され、WhatsAppによって承認されると、そのテンプレートを使ってBraze内でCanvasを構築することができる。 

{% alert tip %}
メッセージテンプレートの承認を受ける前にキャンバスを構築することができる。
{% endalert %}

#### ステップ 2: キャンバスを作成する

次に、作成したテンプレートを含むメッセージ・ステップでキャンバスを構築する。 

![WhatsAppのステップメッセージ作成画面にクイック返信テンプレートが追加された。]({% image_buster /assets/img/whatsapp/whatsapp14.png %})

メッセージステップに続くアクションステップを作成する。このアクションステップでは、クイック返信オプションごとに1つのグループを作成する。

![評価アクションが「WhatsApp受信メッセージを送信」であるキャンバス。]({% image_buster /assets/img/whatsapp/whatsapp15.png %})

各クイック返信オプション・グループに対して、マッチさせるボタンとして正確なテキストを指定する。キーワードは大文字でなければなりません。 

![WhatsApp受信メッセージを送信する」というアクションが、特定のメッセージボディを受信したときに送信されるように設定されたキャンバスステップ。]({% image_buster /assets/img/whatsapp/whatsapp16.png %})

クイック返信の代わりにテキストで返信するユーザーに対してデフォルトの返信をしたい場合は、メッセージ本文が一致しないグループを追加で作成する。

この時点から、通常通りにキャンバスの設定を続けます。

### 回答

各レスポンスに返信メッセージが欲しい場合がほとんどだろう。クイック返信の範囲外 (あらかじめ決められたプロンプトではなく、一般的なメッセージで返信する顧客の場合など) の返信には、catch-all オプションを使用することをお勧めします。例えば、「申し訳ありません、あなたの返答に気づきませんでした。サポートに関する問題は、<support channel> というメッセージをお送りください。」

![各コールトゥアクションボタンのレスポンスを示すキャンバスを作成した。]({% image_buster /assets/img/whatsapp/whatsapp18.png %})

レスポンス内のメッセージ、ユーザープロファイルの更新、Braze-to-Braze Webhook など、Braze キャンバスが提供する後続のアクションを使用できることに注意してください。 

## リストメッセージ

リストメッセージは、クリック可能なオプションのリストとともに本文メッセージとして表示されます。各リストには複数のセクションを含めることができ、各リストには最大10 行を含めることができます。

![WhatsAppリストメッセージの例。]({% image_buster /assets/img/whatsapp/list_message_example.png %}){: style="max-width:40%;"}

### キャンバスでのリストメッセージエクスペリエンスの設定

#### ステップ 1: 既存のアクションベースのキャンバスを作成または編集する

ユーザーメッセージに応答する必要があるため、アクションベースのキャンバスにはWhatsAppリストメッセージのみを追加できます。

#### ステップ 2: WhatsApp メッセージステップの作成

WhatsApp [メッセージステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)を追加し、**リストメッセージ**の応答メッセージレイアウトを選択します。

![WhatsAppレスポンシブメッセージの種類を選択できる。]({% image_buster /assets/img/whatsapp/list_message_option.png %}){: style="max-width:70%;"}

ユーザーがリストを表示するために選択する**リストボタン**名を追加します。次に、**List content** のフィールドを使用してリストを作成します。

- **セクション:**最大10 個のセクションを追加して、リスト項目をグループ化および整理します。たとえば、衣料品小売業者は、セクションを使用して季節スタイル(春、夏、秋、冬など)または衣料品(トップ、ボトム、シューズなど)別に整理することができます。
- **行:**すべてのセクションに、最大10 の行またはリスト項目を追加します。
- **行の説明(オプション):**すべての行(リスト項目) にオプションの説明を追加します。

![リストの内容」セクションは、2つのセクションといくつかの行と行の説明で埋め尽くされた。]({% image_buster /assets/img/whatsapp/list_content.png %}){: style="max-width:60%;"}

セクションと行の順序を変更するには、名前の横にあるアイコンを選択してドラッグします。

![リストセクションを新しい場所にドラッグする。]({% image_buster /assets/img/whatsapp/drag_list_order.png %}){: style="max-width:60%;"}

キャンバス作成画面に戻り、リスト応答ごとにグループを持つメッセージステップの後に[アクションパス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)を追加します。各グループ内で次のようにします。

1. **Sent inbound WhatsApp subscription group** にトリガを追加し、それぞれのWhatsApp サブスクリプションググループを選択します。
2. [**メッセージ本文の場所**] チェックボックスをオンにします。
3. 1つの行 (またはリスト項目) の内容を指定します。

![服のスタイル別にグループ分けされたアクションパスのコンポーザー。]({% image_buster /assets/img/whatsapp/action_path_list_message.png %})

キャンバスの作成を続行します。

### 長い説明のためのアクションパスの作成

行の説明がある場合は、[**次に部分一致 (正規表現も使用可)**] を使用して行を指定する必要があります。たとえば、説明"ankle boots"のお気に入りのペアに適合する新しいスタイルを指定する場合、[regex]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)を"ankle boots"とともに使用できます。

![WhatsAppのトリガーが "Matches regex "のフィルターを使用して、"ankle boots "を含むレスポンシブメッセージをキャプチャした。]({% image_buster /assets/img/whatsapp/regex_list_message.png %})

## 応答メッセージに関する考慮事項

応答メッセージは、ユーザのメッセージを受信してから24時間以内に送信する必要があります。優れたエクスペリエンスを実現できるように、Braze はメッセージロジックをチェックして、応答メッセージのブロックを解除するアップストリームのインバウンドユーザーメッセージがあることを確認します。 

次のイベントは、応答メッセージのブロックを解除します。 

- インバウンドメッセージ 
  - [**WhatsApp インバウンドメッセージを送信**] トリガーが設定された[アクションベースのエントリ]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)または[アクションパス]({{site.baseurl}}/action_paths/)。

![トリガー「WhatsApp受信メッセージを送信」を持つアクションベースのエントリステップ。]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message_trigger.png %})

- [API トリガーエントリ]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)
- インバウンド製品メッセージ 
  - [`ecommerce.cart_updated`]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/?tab=ecommerce.cart_updated#types-of-ecommerce-recommended-events) イベント

![実行されたカスタムイベントをトリガーとするアクションパス`ecommerce.cart_updated`.]({% image_buster /assets/img/whatsapp/ecommerce_cart_updated.png %})

