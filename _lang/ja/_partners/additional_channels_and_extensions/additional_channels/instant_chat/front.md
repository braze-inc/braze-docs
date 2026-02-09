---
nav_title: Front
article_title: Front
description: "BrazeとFrontを統合する方法を学びます"
alias: /partners/front/
page_type: partner
search_tag: Partner

---

# Front

> Front の統合により、各プラットフォームから Braze Data Transformation および Webhook を活用して双方向の会話型 SMS パイプラインを設定できます。

Front からの受信 Webhook には、ライブエージェントが送信したメッセージを含むペイロードが含まれています。リクエストは、Braze のエンドポイントで受け入れられるようにするため、事前に再フォーマットしておく必要があります。Front Data Transformation テンプレートによりペイロードが再フォーマットされ、カスタムイベントが、イベントプロパティとして渡されるメッセージ本文とともに **Outbound SMS Sent** というタイトルのユーザープロファイルに書き込まれます。

Braze で新し変換を設定する前に、[データ変換]({{site.baseurl}}/user_guide/data/data_transformation/overview/)ドキュメントの各ティアのサポートマトリックスを確認することをお勧めします。私たちの無料およびプロのティアは、月ごとのアクティブな変換と受信リクエストの数が異なります。現在のプランがあなたのユースケースをサポートできるか確認してください。

## 前提条件

開始する前に、次のものが必要になります。

| 前提条件             | 説明                                                               |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Front アカウント            | このパートナーシップを利用するには、フロントアカウントが必要です。|
| Braze Data Transformation Webhook URL | [Braze Data Transformation]({{site.baseurl}}/user_guide/data/data_transformation/overview/) は、Front からの受信 Webhook を再フォーマットして、Brazeの /users/track エンドポイントで受け入れられるようにします。|
| フロントREST APIキー         | Front REST API キーを使用して、Braze から Front へのアウトバウンド Webhook リクエストを行います。 |

## ユースケース

- Braze の自動 SMS メッセージングを使用してリード生成プロセスを合理化し、ユーザーの好みを特定し、ライブ販売エージェントがフォローアップして販売を完了できるようにします。
- 自動 SMS 応答とライブチャットサポートによりセールスコンバージョンを促進することで、ショッピングカートを放棄した顧客を再獲得します。

## Front の統合

### ステップ1:データ変換を作成する

まず、Brazeで新しいデータ変換を作成します。次の手順は簡略化されています。完全な手順については、[変換の作成]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation/)を参照してください。

1. Braze で、**データ設定** > **データ変換** に移動し、**変換の作成** を選択します。
2. 「**編集体験**」で「**最初からやり直す**」を選択します。
3. **送信先**で、**POSTを選択します。ユーザー ** を追跡します。
4. 次の変換テンプレートをコピーして貼り付け、次にエンドポイントを保存してアクティブ化します。
    {% raw %}
    ```liquid

    // This is a default template that you can use as a starting point. Feel free to delete this entirely to start from
    // scratch, or to delete specific components as you see fit

    // First, this code defines a variable, "brazecall", to build up a /users/track request
    // Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in
    // desired values in your /users/track request with JS dot notation, such as payload.x.y.z

    let brazecall = {
    "events": [
      {
      "phone": payload.recipients[1].handle,
      "_update_existing_only": true,
      "name": "Outbound SMS Sent",
      "time": new Date().toISOString(),
      "properties": {
        "message_id": payload.id,
        "message_body": payload.body,
        "front_author_username": payload.author.username
      }
      }
    ]
    };

    // After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
    return brazecall;
    ```
    {% endraw %}

    変換は次のようになります。

    ![データ変換の例。]({% image_buster /assets/img/front/data_transformation.png %})

{% alert tip %}
このテンプレートを変更して、特定のニーズに合わせることができます。例えば、プリセットのカスタムイベント名をカスタマイズできます。詳細については、[データ変換の概要]({{site.baseurl}}/user_guide/data/data_transformation/overview/)を参照してください。
{% endalert %}

### ステップ2:アウトバウンドSMSキャンペーンを作成する

次に、Front からの Webhook をリッスンする SMS キャンペーンと、顧客に対するカスタム SMS 応答を作成します。

#### ステップ 2.1:メッセージを作成する

「**メッセージ**」テキストボックスに、次のLiquidコード、およびオプトアウト言語やその他の静的コンテンツを追加します。

{% raw %}
```liquid
{{event_properties.${message_body}}}
```
{% endraw %}

メッセージは次のようになります。

![Liquidコードを使ったメッセージの例。]({% image_buster /assets/img/front/sms_to_braze.png %}){: style="max-width:80%;"}

#### 2.2 配信をスケジュールする

配信タイプには**アクションベースの配信**を選択し、カスタムイベントトリガーには**送信済みSMS**を選択します。

![スケジュール配信」ページ。]({% image_buster /assets/img/front/custom_event_trigger.png %})

{% alert note %}
このカスタムイベントは、ユーザーのプロファイルに書き込むデータ変換です。エージェントメッセージはこのイベントのイベントプロパティとして保存されます。
{% endalert %}

最後に、[**配信コントロール**] で再適格性を有効にします。

![[配信コントロール] で再適格性が有効になっている。]({% image_buster /assets/img/front/braze_reeligibility.png %})

### ステップ 3:カスタムチャネルを作成する

Frontのダッシュボードで、**設定** > **チャネル** > **チャネルを追加** に移動し、**カスタムチャネル** を選択して、新しいBrazeチャネルの名前を入力します。

![フロントダッシュボードのBraze用カスタムチャネル。]({% image_buster /assets/img/front/front_custom_channel.png %})

### ステップ 4: 設定を構成する

アウトバウンド API エンドポイントフィールドに、[以前に作成した](#step-1-set-up-a-data-transformation-in-braze) Data Transformation Webhook URL を入力します。すべてのライブエージェントからの新しいBrazeチャネルの送信メッセージはここに送信されます。このチャネルは、SMSメッセージを転送するためのエンドポイントURLも提供します。Brazeはこれを**受信URL**フィールドに転送します。

このURLをメモしておいてください。後で必要になります。

![Frontに新しく作成されたBrazeチャンネルのチャンネル設定。]({% image_buster /assets/img/front/front_custom_channel2.png %}){: style="max-width:65%;"}

### ステップ 5: インバウンドSMS転送の設定

次に、Brazeで2つの新しいWebhook キャンペーンを作成します。これにより、顧客からのインバウンド SMS を Front の受信トレイに転送できます。

|数値|目的|
|---|---|
|Webhook キャンペーン 1|ライブチャットの会話が要求されていることを Front に通知します。|
|Webhook キャンペーン 2|顧客からインバウンドで送信されたすべての会話型 SMS 応答を Front の受信トレイに転送します。|
{: .reset-td-br-1 .reset-td-br-2 }

#### ステップ 5.1:SMSキーワードカテゴリを作成する

Brazeのダッシュボードで、**オーディエンス**に移動し、**SMSサブスクリプショングループ**を選択して、**カスタムキーワードを追加**を選択します。Frontの専用SMSキーワードカテゴリを作成するには、次のフィールドに記入してください。

|フィールド|説明|
|---|---|
|キーワードカテゴリ|キーワードカテゴリの名前、例えば`FrontSMS1`。|
|キーワード|あなたのカスタムキーワード、例えば`TIMETOMOW`。一般的な言葉を避けて、誤ってトリガーされないようにしてください。念頭に置いてください、キーワードは大文字と小文字を区別しないので、`lawn`は`LAWN`と一致します。|
|返信メッセージ|キーワードが検出されたときに送信されるメッセージ。"A landscaper will contact you shortly"（造園業者からまもなく連絡があります）など。|
{: .reset-td-br-1 .reset-td-br-2 }

![BrazeのSMSキーワードカテゴリーの例。]({% image_buster /assets/img/front/front_keyword.png %}){: style="max-width:65%;"}

#### ステップ 5.2:最初のWebhookキャンペーンを作成する

Brazeのダッシュボードで、以前に作成したURL[を使用して最初のWebhookキャンペーンを作成します](#step-3-configure-the-settings-for-your-new-custom-braze-channel)。

![Brazeで最初に作成すべきWebhookキャンペーンの例。]({% image_buster /assets/img/front/sms_to_front.png %}){: style="max-width:65%;"}

次の内容をリクエストボディに追加してください:

{% raw %}
```liquid
{ 
 "sender": {
  "handle": "{{${phone_number}}}",
  "name": "{{${user_id}}}"
 },
 "body_format": "markdown",
 "metadata": {
  "headers": {
   "first_name": "{{${first_name}}}",
   "last_name": "{{${last_name}}}"
  }
 },
 "body": "{{sms.${inbound_message_body} | default : "no body available" }}"
}
```
{% endraw %}

設定タブで、`Authorization`、`content-type`、および`accept`のリクエストヘッダーを構成します。

![3つの必須ヘッダーを持つリクエスト例。]({% image_buster /assets/img/front/webhook_settings.png %}){: style="max-width:65%;"}

#### ステップ 5.3:最初の配達をスケジュールする

**スケジュール配信**のために、**アクションベースの配信**を選択し、次にトリガータイプとして**SMS受信メッセージの送信**を選択します。また、[以前に設定した](#step-51-create-an-sms-keyword-category) SMS サブスクリプショングループとキーワードカテゴリを追加します。

![最初のWebhookキャンペーンの「配信スケジュール」ページ。]({% image_buster /assets/img/front/front_actionbased_keyword.png %})

[**配信コントロール**] で再適格性を有効にします。

![最初の Webhook キャンペーンの [配信コントロール] で再適格性が選択されている。]({% image_buster /assets/img/front/braze_reeligibility.png %})

#### ステップ 5.4:2番目のWebhookキャンペーンを作成する

2つ目のWebhookキャンペーンは1つ目のキャンペーンと一致するので、[1つ目のキャンペーンを複製し、名前を変更する]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/#duplicating-segments-or-campaigns)ことができる。

#### ステップ 5.5:2 回目の配信をスケジュールする

**スケジュール配信**のために、**アクションベースのトリガー**と**SMSサブスクリプショングループ**を[最初の配信](#step-53-schedule-the-first-delivery)と同じに設定します。しかし、**キーワードカテゴリ**の場合は、**その他**を選択してください。

![2つ目のWebhookキャンペーンの「スケジュールされた配信」ページ。キーワードカテゴリーとして「その他」が選択されている。]({% image_buster /assets/img/front/front_actionbased_other_keyword.png %})

#### ステップ 5.6:オーディエンスフィルターを追加

これで、Webhook キャンペーンが顧客からのインバウンド SMS応答を転送できるようになりました。ライブチャット用のメッセージのみが転送されるようにSMSの応答をフィルタリングするには、**特定のキャンペーンからの最後に受信したメッセージ**セグメンテーションフィルターを**ターゲットオーディエンスステップ**に追加します。

![特定のキャンペーンから最後に受信したメッセージ」を選択したオーディエンスフィルター。]({% image_buster /assets/img/front/front_segment_last_received_message.png %}){: style="max-width:65%;"}

次に、フィルターを設定します：

1. **キャンペーン**のために、以前作成したSMSキャンペーン[を選択します](#step-2-create-an-outbound-sms-campaign)。
2. **オペレーター**の場合、**未満**を選択します。
3. [**時間枠**] については、顧客からの応答がない状態でチャットを開いたままにしておく期間を選択します。

![選択したオーディエンスフィルターの設定。]({% image_buster /assets/img/front/front_target_audience.png %})

## 考慮事項

### 課金セグメント

- BrazeでのSMSメッセージはメッセージSegmentごとに課金されます。何がセグメントを定義し、どのようにメッセージが分割されるかを理解することは、メッセージの請求方法を理解するうえで重要です。詳細については、当社の[ドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/)をご覧ください。
- エージェントの応答が長いと、請求対象セグメントの消費が増加します。

### データポイントを記録する

現在、この統合では、ライブエージェントが Front から SMS を送信するたびに、ユーザープロファイルにカスタムイベントを書き込む必要があります。これは、2、3メッセージで終わるような素早いやりとりには適しているかもしれないが、会話が長くなればなるほど、データポイントの意味合いも大きくなる。Brazeのデータポイントのニュアンスについてご質問があれば、Brazeアカウントマネージャーがお答えします。

### SMSメッセージにリンクを含める

フロントライブチャットからリンクを送信すると、追加のHTMLタグがレンダリングされます。

### フロントから画像ファイルを添付

Brazeから送信されたSMSメッセージでは、Frontの画像ファイルは表示されません。

### オプトアウト 

会話型メッセージでは、あいまいなオプトアウトとして認識される可能性のある言葉 (「stop」など) が含まれるリスクが高くなります。
