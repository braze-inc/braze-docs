---
nav_title: Phrasee
article_title:フレーズ
page_order:1
description:「この参考記事では、BrazeとPhraseeのパートナーシップについて概説しています。Phraseeは、カスタマージャーニー全体にわたって使用される言語を最適化することで顧客体験を向上させることができる、AIと計算言語学のプラットフォームです。Phrasee のディープラーニングエンジンは、学習内容に基づいて新しい言語のテスト、監視、生成を行います。「
page_type: partner
search_tag:Partner

---

# フレーズ

> [Phraseeは][1]、人工知能、計算言語学、顧客中心主義の精神を結集して、ブランドボイスに合わせてカスタマイズされたチャネル全体に、ブランドランゲージを大規模に展開できるよう支援します。

BrazeとPhraseeのパートナーシップにより、顧客ージャーニー全体にわたって使用される言語を最適化することで、顧客体験を向上させることができます。Phrasee のディープラーニングエンジンは、学習内容に基づいてテスト、監視、および新しいコピーの生成を行います。 

[Braze Currentsとコネクテッドコンテンツを使用して購読者のクリックトラッキング, 追跡情報を含めるには、Phraseeの追加Phrasee React統合を確認してください。]({{site.baseurl}}/partners/data_and_infrastructure_agility/ab_testing/phrasee/phrasee_react/)

## 前提条件

| 必要条件 | 説明 |
|---|---|
| フレーズアカウント | このパートナーシップを利用するには [Phrasee アカウントが必要です][3]。 |
| Braze REST API キー | `campaigns`権限のあるBraze REST APIキー。<br><br> これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。 |
| Braze REST エンドポイント  | あなたの REST エンドポイント URL。エンドポイントは、[インスタンスの Braze URL][2] によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合

この統合により、メールやプッシュキャンペーンを Phrasee に統合できます。次の手順は両方について詳細に説明されています。

{% tabs %}
{% tab Email Campaign %}

### メールキャンペーン

#### ステップ1:Phrasee でキャンペーンを設定して、分割テストのバリアントを生成します

Phrasee メールキャンペーンを通常どおり設定します。バリエーションを承認すると、概要ページに移動します。ここで、Brazeキャンペーンに追加するバリエーションをコピーする必要があります。必要に応じて、\[**バリエーションをダウンロード**] ボタンをクリックして、すべてのバリエーションを含むテキストファイルをダウンロードすることもできます。

![A Phrasee campaign showing the available variants.]({% image_buster /assets/img/phrasee/3_phrasee_braze1.png %})

#### ステップ2:Braze メールキャンペーンを作成する

Braze ダッシュボードに移動してメールキャンペーンを作成します。キャンペーンを作成するときに、「**メールキャンペーン**」というタグを追加します。このタグがまだ存在しない場合は、作成してください。

![The Braze email builder emphasizing the email tag that can be added directly under the campaign description field.]({% image_buster /assets/img/phrasee/4_braze_emailtag.png %})

次に、各バリエーションの \[**送信情報を編集**] をクリックして、フレーズバリアントを件名に貼り付けます。PhraseeとBrazeのバリエーションの数が一致していることを確認してください。

各メールを最初から作成し直す必要はありません。最初のバリアントをコピーして、新しいバリアントごとに件名を編集するだけです。

![Option to copy an existing email variant in Braze.]({% image_buster /assets/img/phrasee/5_copy_variant_braze.png %})

#### ステップ3:Braze キャンペーンをスケジュールする

キャンペーンを特定の時間に開始するようにスケジュールします。これは API [`/campaign/trigger/send`とエンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)を使用して行うこともできます。Phrasee にプラグインするには、この時間を知っておく必要があります。

![A scheduled delivery campaign sent at a designated time.]({% image_buster /assets/img/phrasee/6_braze_schedule.png %})

#### ステップ 4:Braze キャンペーンセットアップを完成させましょう

Braze の残りのステップを完了してキャンペーンを設定します。**AB テスト**で、「**優勝バリアントを送信**」を選択します。次に、ウィニングバリアントを送信するまでの待機時間を選択します。

![The A/B testing portion of the campaign showing how the A/B tests and control group will be split. Also shown are settings allowing you to determine the Winning Variant, sending information, and preferences for if the test ends up being statistically insignificant.]({% image_buster /assets/img/phrasee/7_braze_send_winner.png %})

必要に応じてその他の設定を完了し、キャンペーンを保存します。

#### ステップ 5: フレーズ統合入力

Phrasee キャンペーンに戻り、**Braze** インテグレーションボタンをクリックします。

キャンペーンスケジュールウィンドウがポップアップします。ここで、ドロップダウンリストからBrazeキャンペーンを選択します。次に、キャンペーン開始と終了をスケジュールされたしている日付と時刻を選択します。最後に、A/B テストが完了するスケジュールされた送信時間を入力し、詳細を保存します。Braze アカウントのタイムゾーンがキャンペーンンドロップダウンの近くに表示され、お申し込みのたびに時間が一致するようにします。

Braze でキャンペーンを開始してください。Phrasee ではここからキャンペーンを開始できます。キャンペーンテスト結果が出ると、自動的に Phrasee に表示されます。 

![The Phrasee platform showing the schedule campaign window where you can adjust the send settings.]({% image_buster /assets/img/phrasee/8_braze_int_drawer.png %})

{% alert note %}
Phraseeが正しい時間に結果を取得できるように、スケジュールの日付と時刻がBrazeの設定スケジュールされたスケジュールと一致していることを確認してください。
{% endalert %}

{% endtab %}
{% tab Push Campaign %}

### プッシュキャンペーン

#### ステップ1:Phrasee でプッシュキャンペーンを設定して、スプリットテストのバリアントを生成します。

Phrasee メールキャンペーンを通常どおり設定します。バリエーションを承認すると、概要ページに移動します。ここで、Brazeキャンペーンに追加するバリエーションをコピーする必要があります。必要に応じて、\[**バリエーションをダウンロード] ボタンをクリックして、すべてのバリエーションを含む.txtファイルをダウンロードすることもできます**。

![A Phrasee campaign showing the available variants.]({% image_buster /assets/img/phrasee/3_phrasee_braze1.png %})

#### ステップ2:Braze プッシュキャンペーンを設定する

Phraseeの統合により、必要に応じてiOSとAndroidの両方のBrazeプッシュキャンペーンを選択して、1つのPhraseeキャンペーンに統合することができます。この機能を有効にするには、**必ずPush Campaignというタグを付けてください**。これはステップ 4 で必要です。

![The Braze email builder emphasizing the email tag that can be added directly under the campaign description field.]({% image_buster /assets/img/phrasee/9_braze_push_tag.png %})

#### ステップ3:フレーズのバリエーションを Braze にコピー

{% alert important %}
Phrasee がプッシュキャンペーン内のバリアントの結果を自動的に取得するには、バリアントテキストがメッセージ本文に含まれていなければならず、メッセージ本文には含まれていなければなりません。'Title'
{% endalert %}

Phrasee 言語モデルでは、とに分割された 2 行のバリエーションを生成できます。'Title' 'Message'2 行目がメッセージ本文に含まれていることを確認してください。こうすることで、Phrasee はキャンペーン内のバリエーションの結果を自動的に取得できます。

![An example of Phrasee's two-line variant split language model shown in the Braze message composer.]({% image_buster /assets/img/phrasee/10_push_two_lines.png %})

Phrasee **バリアント全体をメッセージ本文に入力して**、結果が Phrasee に正しく取り込まれるようにすることもできます。その場合、テストを正確に行うには、'Title'すべてのバリアントで一定に保つ必要があります。

![An example of what a Phrasee variant may look like if you add the entire variant into the message body.]({% image_buster /assets/img/phrasee/11_push_messagebody.png %})

#### ステップ 4:Braze キャンペーンをスケジュールする

キャンペーンを特定の時間に開始するようにスケジュールします。これは API [`/campaign/trigger/send`とエンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)を使用して行うこともできます。Phrasee にプラグインするには、この時間を知っておく必要があります。

![A scheduled delivery campaign sent at a designated time.]({% image_buster /assets/img/phrasee/6_braze_schedule.png %})

#### ステップ 5: Braze キャンペーンセットアップを完成させましょう

Braze の残りのステップを完了してキャンペーンを設定します。「**AB テスト**」で、「**優勝バリアントを送信**」のボックスにチェックを入れます。次に、ウィニングバリアントを送信するまでの待機時間を選択します。

![The A/B testing portion of a campaign showing how the A/B tests and control group will be split. Also shown are settings allowing you to determine the Winning Variant, sending information, and preferences for if the test ends up being statistically insignificant.]({% image_buster /assets/img/phrasee/7_braze_send_winner.png %})

必要に応じてその他の設定を完了し、キャンペーンを保存します。

#### ステップ 6: フレーズ統合入力

Phrasee キャンペーンに戻り、**Braze** インテグレーションボタンをクリックします。

キャンペーンスケジュールウィンドウがポップアップします。ここで、ドロップダウンリストからBrazeキャンペーンを選択します。次に、キャンペーン開始と終了をスケジュールされたしている日付と時刻を選択します。最後に、A/B テストが完了するスケジュールされた送信時間を入力し、詳細を保存します。Braze アカウントのタイムゾーンがキャンペーンンドロップダウンの近くに表示され、お申し込みのたびに時間が一致するようにします。

Braze でキャンペーンを開始してください。Phrasee ではここからキャンペーンを開始できます。キャンペーンテスト結果が出ると、自動的に Phrasee に表示されます。 

![The Phrasee platform schedule campaign window where you can adjust the send settings.]({% image_buster /assets/img/phrasee/8_braze_int_drawer.png %})

{% alert note %}
Phraseeが正しい時間に結果を取得できるように、スケジュールの日付と時刻がBrazeの設定スケジュールされたスケジュールと一致していることを確認してください。
{% endalert %}

{% endtab %}
{% endtabs %}

[1]: https://phrasee.co/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: mailto:awesome@phrasee.co
[4]: {% image_buster /assets/img/phrasee/1_create_apikey.png %}
[5]: {% image_buster /assets/img/phrasee/2_campaignaccess.png %}
