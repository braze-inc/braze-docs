---
nav_title: 正面
article_title:正面
description:「Front と Braze を統合する方法を学ぼう」
alias: /partners/front/
page_type: partner
search_tag:Partner

---

# 正面

> Frontの統合により、各プラットフォーム Brazeデータトランスフォーメーションとwebhook を活用して、双方向の会話型SMSパイプラインを設定できます。

Front から受信する Webhook には、ライブエージェントから送信されたメッセージを含むペイロードが含まれます。リクエストは Braze のエンドポイントで受け入れられる前に再フォーマットする必要があります。フロントデータ変換テンプレートはペイロードを再フォーマットし、「**Outbound SMS** Sent」というタイトルのユーザープロファイルカスタムイベント書き込みます。メッセージ本文はイベントプロパティとして渡されます。

Braze で新しいトランスフォーメーション設定する前に、[データトランスフォーメーションドキュメントの各階層のサポートマトリックスを確認することをお勧めします]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/overview/)。無料プランとプロプランでは、1 か月あたりのアクティブなトランスフォーメーションと受信リクエストの数が異なります。現在利用しているプランがユースケースをサポートできることを確認してください。

## 前提条件

始める前に、次のものが必要です。

| 前提条件             | 説明                                                               |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| フロントアカウント            | このパートナーシップを利用するには、フロントアカウントが必要です。|
| Braze データ変換ウェブフック URL | [Braze データ変換を使用して]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/overview/)、フロントから受信したWebhook を Braze が受け付けられるように再フォーマットします /users/track endpoint.|
| フロントREST API キー         | フロント REST API キーを使用して、Braze から Front へのアウトバウンドWebhook リクエストを行います。 |

## ユースケース

- Brazeの自動SMSメッセージングを利用してリードジェネレーションプロセスを効率化し、ユーザー好みを特定し、ライブセールスエージェントがフォローアップして販売を成立させられるようにします。
- 自動SMS応答とライブチャットサポートを通じて売上コンバージョンを促進することで、ショッピングカートを放棄した顧客に再び働きかけましょう。

## インテグレーティング・フロント

### ステップ1:データ変換の作成

まず、Braze で新しいデータ変換を作成します。次の手順は簡略化されています。詳細な手順については、「[変換の作成]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation)」を参照してください。

1. **Braze で、**\[データ設定] > \[****データ変換] に移動し、\[変換を作成**] を選択します。**
2. 「**編集エクスペリエンス**」で、「**最初から始める**」を選択します。
3. **「送信先を選択」** で、「**POST:ユーザーを追跡**」を選択します。
4. 次の変換テンプレートをコピーして貼り付け、保存してエンドポイントを有効にします。
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

    変換は次のようになるはずです。

    ![An example data transformation.]({% image_buster /assets/img/front/data_transformation.png %})

{% alert tip %}
このテンプレートは、特定のニーズに合わせて変更できます。たとえば、あらかじめ設定されたカスタムイベント名をカスタマイズできます。詳細については、「[データ変換の概要]({{site.baseurl}}/docs/user_guide/data_and_analytics/data_transformation/overview/)」を参照してください。
{% endalert %}

### ステップ2:アウトバウンド SMS キャンペーンを作成する

次に、FrontからのWebhookと顧客へのカスタムSMS応答を聞くSMSキャンペーンを作成します。

#### ステップ 2.1:メッセージを作成

**メッセージテキストボックスに**、以下のLiquidコードを、オプトアウト言語やその他の静的コンテンツとともに追加します。

{% raw %}
```liquid
{{event_properties.${message_body}}}
```
{% endraw %}

メッセージは次のようになるはずです。

![An example message using Liquid code.]({% image_buster /assets/img/front/sms_to_braze.png %}){: style="max-width:80%;"}

#### 2.2 配送をスケジュールする

配信タイプとして \[**アクションベースの配信**] を選択し、カスタムイベントトリガーとして \[**送信 SMS 送信**] を選択します。

![The "Schedule Delivery" page.]({% image_buster /assets/img/front/custom_event_trigger.png %})

{% alert note %}
このカスタムイベントは、ユーザーのプロファイル書き込むデータ変換です。エージェントメッセージは、このイベントのイベントプロパティとして保存されます。
{% endalert %}

最後に、**配信管理で再資格を有効にします**。

![Re-eligibility enabled under "Delivery Controls."]({% image_buster /assets/img/front/braze_reeligibility.png %})

### ステップ3:カスタムチャネルを作成する

フロントダッシュボードで、\[**設定]** > \[**チャンネル**] > \[**チャンネルを追加**] に移動し、\[**カスタムチャンネル**] を選択して、新しい Braze チャンネルの名前を入力します。

![A custom channel for Braze in the Front dashboard.]({% image_buster /assets/img/front/front_custom_channel.png %})

### ステップ 4:設定を構成する

アウトバウンドAPIエンドポイントフィールドに、[前に作成したデータ変換Webhook](#step-1-set-up-a-data-transformation-in-braze) URLを入力します。新しい Braze チャネルライブエージェントからのすべてのアウトバウンドメッセージはここに送信されます。このチャネルは、Braze が SMS メッセージを転送するためのエンドポイント URL **も受信 URL** フィールドに入力します。

この URL は後で必要になるので、必ず書き留めておいてください。

![The channel settings for the newly created Braze channel in Front.]({% image_buster /assets/img/front/front_custom_channel2.png %}){: style="max-width:65%;"}

### ステップ 5: 受信 SMS 転送の設定

次に、Braze で 2 つの新しい Webhook キャンペーンを作成して、顧客からのインバウンド SMS をフロント受信トレイに転送できるようにします。

|数値|目的|
|---|---|
|ウェブフックキャンペーン 1|ライブチャットでの会話がリクエストされていることをフロントに通知します。|
|ウェブフックキャンペーン 2|顧客から受信したすべての会話型SMS応答をフロント受信トレイに転送します。|
{: .reset-td-br-1 .reset-td-br-2 }

#### ステップ 5.1:SMS キーワードカテゴリの作成

Braze ダッシュボードで \[**オーディエンス**] に移動し、**SMS サブスクリプショングループ**を選択して、\[**カスタムキーワードを追加**] を選択します。Front専用のSMSキーワードカテゴリを作成するには、次のフィールドに入力してください。

|フィールド|説明|
|---|---|
|キーワードカテゴリー|キーワードカテゴリの名前 (など) `FrontSMS1`。|
|キーワード|カスタムキーワード (など) `TIMETOMOW`。偶発的なトリガーを防ぐために、一般的な単語は避けてください。`lawn`キーワードは大文字と小文字を区別しないので、`LAWN`一致することに注意してください。|
|返信メッセージ|キーワードが検出されたときに送信されるメッセージ。たとえば、「造園家からすぐに連絡があります。「|
{: .reset-td-br-1 .reset-td-br-2 }

![An example SMS keyword category in Braze.]({% image_buster /assets/img/front/front_keyword.png %}){: style="max-width:65%;"}

#### ステップ 5.2:初めてのWebhook キャンペーンを作成

Brazeダッシュボードで、[以前に作成したURLを使用して最初のWebhookキャンペーン](#step-3-configure-the-settings-for-your-new-custom-braze-channel)を作成します。

![An example of the first webhook campaign that should be created in Braze.]({% image_buster /assets/img/front/sms_to_front.png %}){: style="max-width:65%;"}

リクエスト本文に以下を追加してください。

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

「設定」タブで、`Authorization``content-type`、`accept`およびリクエストヘッダーを設定します。

![An example request with the three required headers.]({% image_buster /assets/img/front/webhook_settings.png %}){: style="max-width:65%;"}

#### ステップ 5.3:最初の配達をスケジュールする

「**スケジュール配信**」で、「**アクションベースの配信**」を選択し、トリガー**ータイプとして「SMSインバウンドメッセージの送信**」を選択します。また、[以前に設定した](#step-51-create-an-sms-keyword-category) SMS サブスクリプショングループとキーワードカテゴリも追加します。

![The "Schedule Delivery" page for the first webhook campaign.]({% image_buster /assets/img/front/front_actionbased_keyword.png %})

**配送管理で**、再資格を有効にします。

![Re-eligibility selected under "Delivery Controls" for the first webhook campaign.]({% image_buster /assets/img/front/braze_reeligibility.png %})

#### ステップ 5.4:2 つ目のWebhook キャンペーンを作成する

2つ目のWebhookキャンペーンは最初のWebhookキャンペーンと一致するので、[最初のWebhookキャンペーンを複製して名前を変更することができます]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/#duplicating-segments-or-campaigns)。今ならできます。

#### ステップ 5.5:2 回目の配送をスケジュールする

**配信スケジュールでは**、**アクションベースのトリガー****とSMSサブスクリプショングループ**[を最初の配信と同じに設定します](#step-53-schedule-the-first-delivery)。ただし、**キーワードカテゴリには** \[**その他**] を選択してください。

![The "Scheduled Delivery" page for the second webhook campaign, with "Other" chosen as the keyword category.]({% image_buster /assets/img/front/front_actionbased_other_keyword.png %})

#### ステップ 5.6:オーディエンスフィルターを追加する

これで、Webhook キャンペーンで顧客からのインバウンド SMS 応答を転送できるようになりました。ライブチャットのメッセージのみが転送されるように SMS 応答をフィルタリングするには、**ターゲットオーディエンスステップに**「**特定のキャンペーンからの最終受信メッセージ**」セグメンテーションフィルターを追加します。

![An audience filter with "Last Received Message From Specific Campaign" selected.]({% image_buster /assets/img/front/front_segment_last_received_message.png %}){: style="max-width:65%;"}

次に、フィルターを設定します。

1. \[**キャンペーン**] で、[以前に作成した](#step-2-create-an-outbound-sms-campaign) SMS キャンペーンを選択します。
2. \[**演算子**] で \[**未満**] を選択します。
3. **「タイムウィンドウ」** では、顧客からの応答がないままチャット開封ままにする時間を選択します。

![The configuration settings for the selected audience filter.]({% image_buster /assets/img/front/front_target_audience.png %})

## 考慮事項

### 請求対象セグメント

- Braze の SMS メッセージは、メッセージSegment ごとに課金されます。Segment の定義とメッセージの分割方法を理解することは、メッセージに対する請求方法を理解するうえで重要です。詳細については、[ドキュメントをご覧ください]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments)。
- エージェントの応答が長くなると、請求対象セグメントの消費量が増えます。

### データポイント消費

現在、この統合では、ライブエージェントがFrontからSMSを送信するたびに、カスタムイベントユーザープロファイル書き込む必要があります。これは、2、3通のメッセージしか続かないような迅速なやり取りに適しているかもしれませんが、会話が長くなるにつれて、データポイントへの影響も長くなります。Braze に記録されたカスタムイベントごとにデータポイントが消費されます。

### SMS メッセージにリンクを含める

Front ライブチャットからリンクを送信すると、追加の HTML タグでレンダリングされます。

### Front からの画像, 写真ファイルの添付

Frontの画像ファイルは、Brazeから送信されたSMSメッセージには表示されません。

### オプトアウト 

会話形式のメッセージには、「停止」という単語や、あいまいなオプトアウトと認識される類似の言葉が含まれるリスクが高くなります。
