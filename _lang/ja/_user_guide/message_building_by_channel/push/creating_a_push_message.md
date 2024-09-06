---
nav_title: "プッシュメッセージを作成する"
article_title: プッシュ・キャンペーンを作成する
page_order: 4
page_type: tutorial
description: "このチュートリアルページでは、設定、送信、ターゲティングなど、プッシュメッセージの作成に関わるさまざまなコンポーネントについて説明する。"
channel: push
tool:
  - Campaigns
  
---

# プッシュ・メッセージを作成する

> プッシュ通知は、一刻を争う行動喚起や、しばらくアプリにアクセスしていないユーザーの再エンゲージメントに最適だ。成功するプッシュキャンペーンは、ユーザーをコンテンツに直接誘導し、アプリの価値を実証する。

プッシュ通知の事例をご覧になりたい方は、\[ケーススタディ][8] をご覧いただきたい。

## ステップ 1:メッセージを発信する場所を選ぶ {#create-new-campaign-push}

メッセージは、キャンペーンとキャンバスのどちらを使用して配信すべきでしょうか。キャンペーンは単一のシンプルなメッセージングキャンペーンに適していますが、キャンバスはマルチステップのユーザーのジャーニーに適しています。

{% tabs %}
{% tab キャンペーン %}

**ステップ:**

1. **Messaging**>**Campaignsに**進み、**Create Campaignを**クリックする。
2. **プッシュ通知」を**選択するか、複数のチャネルを対象とするキャンペーンの場合は「**マルチチャネルキャンペーン**」を選択する。
3. キャンペーンに、明確で意味のある名前を付けます。
4. 必要に応じて、\[[チーム]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/)] と \[[タグ]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)] を追加します。
   * タグを使用すると、キャンペーンを検索してレポートを作成しやすくなります。例えば、\[[レポートビルダー]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)] を使用する場合、特定のタグでフィルターできます。
5. キャンペーンに必要な数だけバリアントを追加して名前を付けます。追加したバリアントごとに、さまざまなプラットフォーム、メッセージタイプ、レイアウトを選択できます。このトピックの詳細については、「[多変量テストと AB テスト]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)」を参照してください。

{% details 通常キャンペーンかマルチチャネルプッシュキャンペーンかを決める %}

モバイル、ウェブ、Kindle、iOS、Androidの組み合わせなど、複数のデバイスやプラットフォームをターゲットにする場合、このステップでの選択が、後のいくつかの機能や設定の可用性に影響する可能性がある。

マルチチャンネルまたはプッシュ通知キャンペーンを作成する前に、以下の決定チャートを参照のこと：

![「キャンペーンタイプを選択するためのフローチャート。複数のデバイスやプラットフォームをターゲットにしているかどうかを決めることから始める。いいえ」の場合は、「プッシュ通知を選択」につながる。はい」の場合、「どのようなプッシュメッセージのタイプですか」と尋ねられ、選択肢は「標準的なプッシュ」となり、「デバイス固有の設定を使用する必要がありますか」という判断ポイントにつながる。いいえ」の場合は、「プッシュ通知を選択し、クイックプッシュを使用する」につながる。イエスなら、『マルチチャンネルの選択』に進む。どのようなプッシュメッセージのタイプですか」に戻り、答えが「プッシュストーリーまたはインライン画像」であれば、「マルチチャンネルを選択してください」]({% image_buster /assets/img_archive/flowchart_quickpush.png %})

**プッシュ通知を**選択し、複数のデバイスとプラットフォームをターゲットに選択すると、自動的にクイックプッシュキャンペーンが作成される。クイックプッシュでは、特定のデバイス固有の設定は利用できない：

- アクションボタンを押す
- 通知チャネルとグループ
- プッシュ・タイム・トゥ・ライブ（TTL）
- 表示優先度
- サウンド

[クイック・プッシュ・キャンペーンを]({{site.baseurl}}/quick_push)参照して、この編集体験で何が違うのかを理解してから次に進もう。

{% enddetails %}

{% alert tip %}
キャンペーン内のすべてのメッセージが類似しているか、同じ内容になる場合は、メッセージを作成してからバリアントを追加します。その後、\[**バリアントを追加**] ドロップダウンから \[**バリアントをコピー**] を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

**ステップ:**

1. キャンバス作成ツールを使用して \[[キャンバスを作成]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)] します。
2. キャンバスを設定したら、キャンバスビルダーにステップを追加します。ステップに、明確で意味のある名前を付けます。
3. \[[ステップスケジュール]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay)] を選択し、必要に応じて遅延を指定します。
4. このステップでは、必要に応じて聴衆をフィルタリングする。セグメントを指定し、フィルターを追加して、このステップの受信者をさらに絞り込むことができます。後から、メッセージの送信時に、オーディエンスオプションがチェックされます。
5. \[[昇進動作]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)] を選択します。
6. メッセージと組み合わせる他のメッセージングチャネルを選択します。

{% endtab %}
{% endtabs %}

## ステップ 2:配信プラットフォームを指定する

まず、どのデバイスとプラットフォームの組み合わせでプッシュを受け取るかを選択する。プッシュ通知の配信を特定のアプリに限定するには、この選択を使用する。

これまでの選択によって、いくつかの方法がある：

| 前選考 | options |
| --- | --- | 
| プッシュ通知キャンペーン | 1つまたは複数のプラットフォームとデバイスを選択する。複数のデバイスやプラットフォームをターゲットに選ぶと、自動的にクイックプッシュキャンペーンが作成される。これにより、1つのエディターで選択したすべてのプラットフォームに対して1つのメッセージを作成するために最適化された編集エクスペリエンスが提供される。この編集エクスペリエンスで何が違うかについては、[クイック・プッシュ・キャンペーンを]({{site.baseurl}}/quick_push)参照のこと。 |
| マルチチャンネル・キャンペーン | **Add Messaging Channelを**クリックして、プッシュ・プラットフォームを追加する。プラットフォームの選択はそれぞれのバリアントに特有であるため、プラットフォームごとにメッセージのエンゲージメントをテストしてみることができる。
| キャンバス | メッセージ・ステップで、**「+ Add more**」をクリックし、プッシュ・プラットフォームを追加する。マルチチャネルキャンペーンと同様、プラットフォームの選択は、それぞれのバリアントに特化している。 |
{: .reset-td-br-1 .reset-td-br-2}

## ステップ 3:通知タイプを選択する（iOSとAndroid）

クイックプッシュキャンペーンを作成している場合、通知タイプは自動的に標準プッシュに設定され、変更することはできない。

![通知タイプは、例として標準プッシュが選択されている。][3]{: style="float:right;max-width:40%;margin-left:15px;"}

iOSとAndroidの場合は、通知タイプを選択する：

- スタンダード・プッシュ
- [プッシュ通知ストーリー]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)
- インライン画像（Androidのみ）

プッシュ・キャンペーンに画像を含めたい場合は、[iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)または[Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)向けのリッチ通知の作成について、以下のガイドを参照のこと。

## ステップ 4:プッシュメッセージを作成する

さて、いよいよプッシュ・メッセージを書く番だ！**Compose**タブでは、メッセージの内容と動作のあらゆる面を編集できる。

![] （{% image_buster /assets/img_archive/push_compose.png %} ）。

**Compose "**タブの内容は、前のステップで選択した通知タイプによって異なるが、以下のオプションのいずれかを含むことができる：

#### 通知チャンネルまたはグループ（iOSおよびAndroid）

プラットフォーム固有の通知オプションの詳細については、[iOS通知オプション]({{site.baseurl}}/user_guide/message_building_by_channel/push/notification_options_ios/)または[Android通知]({{site.baseurl}}/user_guide/message_building_by_channel/push/notification_options_android/)オプションを参照のこと。

#### 言語

**Add Languages**ボタンを使って複数の言語でコピーを追加する。コンテンツを書く前に言語を選択することをお勧めする。私たちの\[利用可能な言語の完全なリストを参照してください][18] 。

#### タイトルと本文

メッセージボックスに入力を開始し、左側のプレビューボックスにプレビューが表示されるのを見る。プッシュメッセージはプレーンテキストでフォーマットされなければならない。iOSのプッシュ通知に見出しを追加するには、**「タイトル」**フィールドを使う。

あなたのプッシュをパーソナライズされ、ターゲットを絞ったものにするために、[リキッドを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)含めることができる。

{% alert tip %}
素晴らしいコピーの作成にお困りですか？[AIコピーライティング・アシスタントを使って]({{site.baseurl}}/user_guide/intelligence/ai_copywriting/)みよう。商品名や説明を入力すると、AIが人間のようなマーケティングコピーを生成し、メッセージングに使用する。

![プッシュコンポーザーのボディ欄にある「AIコピーライター」ボタンを起動する。]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

#### イメージ

サポートされている場合、アプリのアイコンは自動的にプッシュ通知の画像として追加される。また、リッチ通知を送信するオプションもあり、コピー以外のコンテンツを追加することで、プッシュ通知をよりカスタマイズすることができる。

プッシュ通知に画像を使用する際のガイダンスについては、以下の記事を参照のこと：

- [iOS用のリッチな通知を作成する]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)
- [Android向けにリッチな通知を作成する]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)

#### オン・クリック動作

**On-Click Behaviorで**、ユーザーがプッシュ通知の本文をクリックしたときの動作を指定する。例えば、顧客にアプリケーションを開くよう促したり、顧客を指定のウェブURLにリダイレクトさせたり、あるいは[ディープリンクを使って]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/)アプリケーションの特定のページを開くこともできる。

ここでは、プッシュ通知の中に、次のようなボタンのプロンプトを設定することもできる：

- 受諾／拒否
- はい／いいえ
- 確認/キャンセル
- もっと見る 

#### デバイス・オプション

ユーザーが複数のデバイスにアプリをインストールしている場合、デフォルトでは、有効なプッシュトークンが割り当てられたすべてのデバイスにプッシュメッセージが送信される。必要であれば、**このプッシュをユーザーの最近使用したデバイスにのみ送信する**ように選択することもできる。

![デバイスオプションのチェックボックスで、このプッシュをユーザーの最近使用したデバイスにのみ送信する。][9]{: style="max-width:70%;" }

この設定には若干のニュアンスがある。このオプションが選択されている場合、Brazeは、iOSとAndroidの両方など、複数のプラットフォームを対象とするキャンペーンを除き、複数送信が発生しないように制限する。ユーザーがiOSとAndroidの両方のデバイスにアプリを入れている場合、両方のプラットフォーム用のプッシュを受け取ることになる。ユーザーが最近使用したデバイスが[プッシュ対応]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-enabled)でない場合、メッセージは送信されない。

iOSの場合、iPadデバイスにのみプッシュ通知を送信したり、iPhoneとiPodデバイスにのみ送信するなど、メッセージングをさらに制限することができる。

### ステップ4a：メッセージをプレビューしてテストする

![テスト・プッシュ・メッセージ][7]{: style="float:right;max-width:30%;margin-left:15px;"}

テストは、間違いなく最も重要なステップのひとつである。完璧なプッシュ・メッセージを作り終えたら、送信する前にテストしてみよう。**Test "**タブを選択し、"**Preview Message as User**"を使用して、メッセージがモバイルでどのように表示されるかを確認する。**Send Testを使って**テストプッシュを送信し、メッセージが正しく表示されることを確認する。

## ステップ 5: キャンペーンまたはキャンバスの残りの部分を作成する

{% tabs %}
{% tab キャンペーン %}

プッシュ通知の作成に最適なツールの使い方については、以下のセクションを参照のこと。

#### 配信スケジュールまたはトリガーを選択する

プッシュメッセージは、スケジュールされた時間、アクション、またはAPIトリガーに基づいて配信することができる。詳しくは、[キャンペーンのスケジューリングを]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)参照のこと。

アクションベースの配信では、キャンペーンの継続時間と \[[サイレント時間]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours)] を設定することもできます。

このステップでは、ユーザーがキャンペーンを受信する[再資格を]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns)得ることを許可したり、[頻度の上限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping)ルールを有効にしたりするなど、配信コントロールを指定することもできる。

#### ターゲットとするユーザーを選択する

次に、セグメントやフィルターを選択することで、[ユーザーを絞り込む]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/)必要がある。セグメントのおおよその人数について現在の状態を示すスナップショットが自動的に表示されます。キャンペーンがターゲットとするチャンネルの詳細なオーディエンス統計は、フッターで見ることができる。ユーザーベースの何パーセントがターゲットになっているか、またそのセグメントのライフタイムバリューを見るには、**「追加統計情報を表示**」をクリックする。

{% details リーチャブル・ユーザーの合計が全チャンネルの合計と一致しないのはなぜか？ %}

フィルタリングしたオーディエンスの合計到達可能ユーザーを表示すると、個々の列の合計が合計到達可能ユーザーよりも小さいことに気づくかもしれない。このギャップは通常、キャンペーンのセグメントやフィルターに該当するにもかかわらず、プッシュでリーチできないユーザーが多数存在するためである（例えば、有効またはアクティブな[プッシュトークンを持って]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens)いないため）。

{% enddetails %}

![]({% image_buster /assets/img_archive/multi_channel_footer.png %}) リーチャブル・ユーザーの詳細な視聴者統計の表。

正確なセグメントメンバーシップは常にメッセージが送信される直前に計算されることに注意してください。

また、特定の[購読ステータスを]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)持つユーザー（購読済みでプッシュ配信をオプトインしているユーザーなど）にのみキャンペーンを送信することもできる。

オプションで、セグメント内の指定されたユーザー数に配信を制限したり、キャンペーンが再来したときに同じメッセージを2回受け取ることをユーザーに許可することもできる。

##### Eメールとプッシュによるマルチチャネルキャンペーン

Eメールとプッシュチャネルの両方をターゲットにしたマルチチャネルキャンペーンの場合、明示的にオプトインしているユーザーのみがメッセージを受信するようにキャンペーンを制限したい場合がある（購読または購読解除したユーザーを除く）。例えば、オプトインのステータスが異なる3人のユーザーがいるとする：

- **ユーザー A** はメールを購読しており、プッシュ通知が有効です。このユーザーはメールを受信しませんが、プッシュ通知は受信します。
- **ユーザー B** はメールにオプトインしていますが、プッシュ通知を有効にしていません。このユーザーはメールを受信しますが、プッシュ通知は受信しません。
- **ユーザー C** はメールにオプトインしており、プッシュ通知が有効です。このユーザーはメールとプッシュ通知の両方を受け取ります。

そのためには、**「オーディエンス・サマリー**」で、このキャンペーンを「オプトインしたユーザーのみ」に送信することを選択する。このオプションを選択すると、オプトインしたユーザーのみがメールを受信し、Braze は、デフォルトでプッシュ通知が有効になっているユーザーにのみプッシュ通知を送ります。

{% alert important %}
この構成では、**Target Users**ステップに、オーディエンスを単一のチャネルに限定するフィルタ（例えば、`Push Enabled = True` や`Email Subscription = Opted-In` ）を含めない。
{% endalert %}

#### コンバージョンイベントを選択する

Braze では、キャンペーンを受信した後、ユーザーが指定のアクションや[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/)を実行する頻度を追跡できます。ユーザーが指定したアクションを実行した場合にコンバージョンがカウントされる期間は、最大 30 日間まで設定できます。

{% endtab %}

{% tab キャンバス %}

まだやっていない場合は、キャンバス・コンポーネントの残りのセクションを完成させる。キャンバスの残りの部分の構築方法、多変量テストとインテリジェントセレクションの実装方法などの詳細については、キャンバスドキュメントの「[キャンバスを構築する」]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas)ステップを参照のこと。

{% endtab %}
{% endtabs %}

## ステップ 6:レビューと配備 {#review-and-deploy-push}

キャンペーンやキャンバスの最後の構築が終わったら、その詳細を確認する。キャンペーンの場合、最終ページには、あなたがデザインしたキャンペーンの概要が表示される。関連する詳細をすべて確認し、メッセージをテストしたことを確認してから送信し、データが送られてくるのを見る！

次に、[プッシュレポート]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/)をチェックして、プッシュキャンペーンの結果にアクセスする方法を学びましょう。プッシュ通知については、メッセージの送信数、配信数、バウンス数、開封数、直接開封数の統計を見ることができる。

[1]: {% image_buster /assets/img_archive/new_campaign_push.png %}
[2]: {% image_buster /assets/img_archive/push_1.png %}
[3]: {% image_buster /assets/img_archive/push_2.png %}
[4]: {% image_buster /assets/img_archive/schedule.png %}
[5]: {% image_buster /assets/img_archive/confirmation_page.png %}
[6]: {% image_buster /assets/img_archive/push-results-statistics.png %}
[7]: {% image_buster /assets/img_archive/push_3.png %}
[8]: https://www.braze.com/customers
[9]: {% image_buster /assets/img_archive/push_recent_device.png %}
[15]: {% image_buster /assets/img_archive/conversion_event_selection.png %}
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[24]: {% image_buster /assets/img_archive/multi_channel_footer.png %}
[25]: {% image_buster /assets/img_archive/target_segmenter.png %} 
