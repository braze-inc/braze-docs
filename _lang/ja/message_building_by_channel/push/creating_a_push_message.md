---
nav_title: "プッシュ・メッセージを作成する"
article_title: プッシュ・キャンペーンを作成する
page_order: 4
page_type: tutorial
description: "このチュートリアルページでは、設定、送信、ターゲティングなど、プッシュメッセージの作成に関わるさまざまなコンポーネントについて説明する。"
channel: push
tool:
  - Campaigns
  
---

# プッシュ・メッセージを作成する

> プッシュ通知は、一刻を争う行動喚起や、しばらくアプリにアクセスしていないユーザーの再エンゲージメントに最適です。成功するプッシュキャンペーンは、ユーザーをコンテンツに直接誘導し、アプリの価値を実証する。プッシュ通知の例については、[ケーススタディを](https://www.braze.com/customers)ご覧いただきたい。

## ステップ 1: メッセージを発信する場所を選ぶ {#create-new-campaign-push}

{% alert tip %}
キャンペーンとキャンバスのどちらを使用すべきでしょうか。キャンペーン s は単一のターゲットメッセージング キャンペーンに適していますが、キャンバスは複数ステップ ユーザーのジャーニーに適しています。
{% endalert %}

{% tabs %}
{% tab Campaign %}
1. [**メッセージング**] > [**キャンペーン**] に進み、[**キャンペーンを作成**] を選択します。
2. 複数のチャネルをターゲットとするキャンペーンの場合は、**Multichannel** を選択します。それ以外の場合は、[**プッシュ通知**] を選択します。それでもわからない場合は、以下の**正規またはマルチチャネルのプッシュキャンペーン**の決定を参照してください。
3. キャンペーンに、明確で意味のある名前を付けます。
4. 必要に応じて、[[チーム]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/)] と [[タグ]({{site.baseurl}}/user_guide/administrative/app_settings/tags/)] を追加します。 

{% alert tip %}
タグを使用すると、キャンペーンを検索してレポートを作成しやすくなります。例えば、[[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/)] を使用する場合、特定のタグでフィルターできます。
{% endalert %}

{: start="5"}
5\.キャンペーンに必要な数だけバリアントを追加して名前を付けます。追加したバリアントごとに、さまざまなプラットフォーム、メッセージタイプ、レイアウトを選択できます。このトピックの詳細については、「[多変量テストと AB テスト]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)」を参照してください。

{% details Deciding between regular or multichannel push campaign %}

モバイル、ウェブ、Kindle、iOS、Androidの組み合わせなど、複数のデバイスやプラットフォームをターゲットにする場合、このステップでの選択が、後のいくつかの機能や設定の可用性に影響する可能性がある。

マルチチャンネルまたはプッシュ通知キャンペーンを作成する前に、以下の決定チャートを参照のこと：

![「キャンペーンタイプを選択するためのフローチャート。まず、複数のデバイスやプラットフォームをターゲットにしているかどうかを決定します。「いいえ」の場合は、「プッシュ通知を選択」につながります。はい」の場合、「どのようなプッシュメッセージのタイプですか」と尋ねられ、選択肢は「標準的なプッシュ」となり、「デバイス固有の設定を使用する必要がありますか」という判断ポイントにつながる。いいえ」の場合は、「プッシュ通知を選択し、クイックプッシュを使用する」につながる。イエスなら、『マルチチャンネルの選択』に進む。どのようなプッシュメッセージのタイプですか」に戻り、答えが「プッシュストーリーまたはインライン画像」であれば、「マルチチャンネルを選択してください」(]({% image_buster /assets/img_archive/flowchart_quickpush.png %}))

**プッシュ通知を**選択し、複数のデバイスとプラットフォームをターゲットに選択すると、自動的にクイックプッシュキャンペーンが作成される。クイックプッシュでは、特定のデバイス固有の設定は利用できない：

- プッシュアクションボタン
- 通知チャネルとグループ
- プッシュ・タイム・トゥ・ライブ（TTL）
- 表示優先度
- サウンド

続行する前に、「[クイックプッシュキャンペーン]({{site.baseurl}}/quick_push)」を参照して、この編集エクスぺリエンスで異なる点を確認してください。

{% enddetails %}

{% alert tip %}
キャンペーン内のすべてのメッセージが類似しているか、同じ内容になる場合は、メッセージを作成してからバリアントを追加します。その後、[**バリアントを追加**] ドロップダウンから [**バリアントをコピー**] を選択できます。
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. キャンバス作成ツールを使用して [[キャンバスを作成]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)] します。
2. キャンバスを設定したら、キャンバスビルダーにステップを追加します。ステップに、明確で意味のある名前を付けます。
3. [[ステップスケジュール]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay)] を選択し、必要に応じて遅延を指定します。
4. 必要に応じて、このステップのオーディエンスをフィルターします。セグメントを指定し、フィルターを追加して、このステップの受信者をさらに絞り込むことができます。後から、メッセージの送信時に、オーディエンスオプションがチェックされます。
5. [[昇進動作]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)] を選択します。
6. メッセージと組み合わせる他のメッセージングチャネルを選択します。

{% endtab %}
{% endtabs %}

## ステップ 2: プッシュプラットフォームを選択する

次に、どのプラットフォームとモバイルデバイスの組み合わせでプッシュを受け取るかを選択します。この選択を使用して、プッシュ通知の配信をアプリの特定のグループに制限します。

これまでの選択によって、いくつかの方法がある：

| 前に選択したもの | options |
| --- | --- | 
| プッシュ通知キャンペーン | 1 つまたは複数のプラットフォームとデバイスを選択します。複数のデバイスやプラットフォームをターゲットに選ぶと、自動的にクイックプッシュキャンペーンが作成される。これにより、1つのエディターで選択したすべてのプラットフォームに対して1つのメッセージを作成するために最適化された編集エクスペリエンスが提供される。この編集エクスペリエンスで何が違うかについては、[クイック・プッシュ・キャンペーンを]({{site.baseurl}}/quick_push)参照のこと。 |
| マルチチャンネル・キャンペーン | [**メッセージングチャネルを追加**] を選択して、プッシュプラットフォームを追加します。プラットフォームの選択はそれぞれのバリアントに特有であるため、プラットフォームごとにメッセージのエンゲージメントをテストしてみることができる。
| キャンバス | メッセージステップで [**\+ その他を追加**] を選択し、プッシュプラットフォームをさらに追加します。マルチチャネルキャンペーンと同様、プラットフォームの選択は、それぞれのバリアントに固有です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ステップ 3: 通知タイプを選択する（iOSとAndroid）

クイックプッシュキャンペーンを作成している場合、通知タイプは自動的に [**標準プッシュ**] に設定され、変更することはできません。

![標準プッシュが選択されている通知タイプの例。]({% image_buster /assets/img_archive/push_2.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

それ以外の場合、iOS と Android では通知タイプを選択します: 

- 標準プッシュ通知
- [プッシュ通知ストーリー]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)
- インライン画像(Androidのみ)

プッシュ・キャンペーンに画像を含めたい場合は、[iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)または[Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)向けのリッチ通知の作成について、以下のガイドを参照のこと。

## ステップ 4: プッシュメッセージを作成する

さて、いよいよプッシュ・メッセージを書く番だ！**Compose**タブでは、メッセージの内容と動作のあらゆる面を編集できる。

![プッシュ通知作成の「作成」タブ。]({% image_buster /assets/img_archive/push_compose.png %})()

[**作成**] タブの内容は、前のステップで選択した通知タイプによって異なりますが、以下のオプションのいずれかを使用できます。

#### 通知チャンネルまたはグループ（iOSおよびAndroid）

プラットフォーム固有の通知オプションの詳細については、[iOS通知オプション]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/)または[Android通知]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_options/)オプションを参照のこと。

#### 言語

**Add Languages**ボタンを使って複数の言語でコピーを追加する。コンテンツを記述する前に言語を選択することをお勧めします。これにより、Liquid 内の適切な場所にテキストを入力することができます。使用可能な言語の完全なリストについては、[サポートされている言語]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported)を参照してください。

右から左に書かれた言語でコピーを追加する場合、右から左に書かれたメッセージの最終的な見た目は、サービスプロバイダーがどのようにそれらをレンダリングするかに大きく左右されることに注意してください。右から左へのメッセージを可能な限り正確に表示するためのベストプラクティスについては、[右から左へのメッセージを作成する]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/)を参照してください。

#### タイトルと本文

{% tabs local %}
{% tab ios %}
メッセージボックスに入力を開始し、左側のプレビューボックスにプレビューが表示されるのを見る。プッシュメッセージはプレーンテキストでフォーマットされなければならない。 

**Title**フィールドを使用してヘッドラインを追加します。プッシュをパーソナライズされターゲットを絞ったものにするには、[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) を含めることができます。
{% endtab %}

{% tab android %}
メッセージボックスに入力を開始し、左側のプレビューボックスにプレビューが表示されるのを見る。プッシュメッセージはプレーンテキストでフォーマットされなければならない。 

プッシュをパーソナライズされターゲットを絞ったものにするには、[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) を含めることができます。

{% alert important %}
Android プッシュメッセージはタイトルなしでは送信**できません**。ただし、代わりに1つのスペースを入力できます。メッセージにスペースが1 つしか含まれていない場合、メッセージはサイレントプッシュ通知として送信されることに注意してください。詳細については、[サイレントプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android)を参照してください。
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
魅力的な文章を作成するためのサポートが必要な場合は、[AI コピーライティングアシスタント]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/)を使用してみてください。商品名や説明を入力すると、AIが人間のようなマーケティングコピーを生成し、メッセージングに使用します。

![プッシュ作成画面の本文フィールドにある「AI コピーライターを起動」ボタン。]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %})({: style="max-width:60%"})
{% endalert %}

#### 画像

サポートされている場合、アプリのアイコンは自動的にプッシュ通知の画像として追加される。また、リッチ通知を送信するオプションもあり、コピー以外のコンテンツを追加することで、プッシュ通知をよりカスタマイズすることができる。

プッシュ通知に画像を使用する際のガイダンスについては、以下の記事を参照のこと：

- [iOS 向けのリッチ通知を作成する]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)
- [Android 向けのリッチ通知を作成する]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)

#### オン・クリック動作

ユーザが**On-Click Behavior**でプッシュ通知の本文を選択した場合の動作を指定します。例えば、顧客にアプリケーションを開くよう促したり、顧客を指定の Web URL にリダイレクトしたり、あるいは[ディープリンク]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/)を使ってアプリケーションの特定のページを開くようにすることも可能です。

ここでは、プッシュ通知の中に、次のようなボタンのプロンプトを設定することもできる：

- 受諾／拒否
- はい／いいえ
- 確認/キャンセル
- もっと見る 

#### 送信オプション

ユーザーが複数のデバイスにアプリをインストールしている場合、デフォルトでは、有効なプッシュトークンが割り当てられたすべてのデバイスにプッシュメッセージが送信される。必要に応じて [**最近使用したデバイス**]を選択することもできます。

![このプッシュをユーザーが最後に使用したデバイスにのみ送信するデバイスオプションのチェックボックス。]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }

この設定には若干のニュアンスがある。このオプションが選択されている場合、Brazeは、iOSとAndroidの両方など、複数のプラットフォームを対象とするキャンペーンを除き、複数送信が発生しないように制限する。ユーザーがiOSとAndroidの両方のデバイスにアプリを入れている場合、両方のプラットフォーム用のプッシュを受け取ることになる。ユーザーが最近使用したデバイスが[プッシュ対応]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#foreground-push-enabled)でない場合、メッセージは送信されない。

iOS の場合、iPad デバイスにのみプッシュ通知を送信したり、iPhone と iPod デバイスにのみ送信するなど、メッセージングをさらに制限することができます。

## ステップ 5: メッセージのプレビューとテスト(オプション)

テストは、おそらく最も重要なステップの 1 つです。完璧なプッシュ・メッセージを作り終えたら、送信する前にテストしてみよう。[**テスト**] タブを選択し、プッシュメッセージのテスト方法のオプションから選択します。[**テスト受信者**] では、コンテンツテストグループまたは個々のユーザーを選択できます。また、**ユーザーとしてメッセージをプレビューを**使用すると、ランダムユーザー、既存ユーザー、カスタムユーザー、多言語ユーザーに対して、あなたのメッセージがモバイルでどのように表示されるかを知ることができる。

## ステップ6: キャンペーンまたはキャンバスの残りの部分を作成する

{% tabs %}
{% tab Campaign %}

プッシュ通知の作成に最適なツールの使い方については、以下のセクションを参照のこと。

#### 配信スケジュールまたはトリガーを選択する

プッシュメッセージは、スケジュールされた時刻、アクション、または API トリガーに基づいて配信することができます。詳細については、[キャンペーンのスケジューリング]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)を参照してください。

アクションベースの配信では、キャンペーンの継続時間と [[サイレント時間]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours)] を設定することもできます。

このステップでは、配信コントロールを指定できます。例えば、ユーザーを[再有効化]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns)してキャンペーンを受信できるようにしたり、[フリークエンシーキャップ]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping)ルールを有効にしたりできます。

#### ターゲットとするユーザーを選択する

次に、セグメントまたはフィルターを選択し、オーディエンスを絞り込んで、[ターゲットのユーザーを設定]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/)する必要があります。そのアプリの近接Segment集団が現在どのように見えるかのプレビューが自動的に与えられます。キャンペーンがターゲットとするチャンネルの詳細なオーディエンス統計は、フッターに表示されます。ユーザー群の何パーセントがターゲットになっているか、およびそのセグメントの生涯価値を確認するには、[**統計をさらに表示する**] を選択します。

{% multi_lang_include target_audiences.md %}

{% details Why does my Total Reachable Users metric not match the sum of all channels? %}

フィルタリングしたオーディエンスのリーチ可能なユーザー合計数を表示した際、個々の列の合計がリーチ可能なユーザー合計数よりも小さい場合があります。このギャップは通常、キャンペーンのセグメントやフィルターに該当するにもかかわらず、プッシュでリーチできないユーザーが多数存在するためである（例えば、有効またはアクティブな[プッシュトークンを持って]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens)いないため）。

{% enddetails %}

![リーチ可能なユーザーの詳細なオーディエンス統計の表。]({% image_buster /assets/img_archive/multi_channel_footer.png %})()

正確なセグメントメンバーシップは常にメッセージが送信される直前に計算されることに注意してください。

また、特定の[購読ステータスを]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)持つユーザー（購読済みでプッシュ配信をオプトインしているユーザーなど）にのみキャンペーンを送信することもできる。

オプションで、セグメント内の指定されたユーザー数に配信を制限したり、キャンペーンが再来したときに同じメッセージを2回受け取ることをユーザーに許可することもできる。

##### Eメールとプッシュによるマルチチャネルキャンペーン

メールチャネルとプッシュ通知チャネルの両方をターゲットにしたマルチチャネルキャンペーンの場合、明示的にオプトインしているユーザーのみがメッセージを受け取るようにキャンペーンを制限することができます (配信登録済みユーザーまたは配信停止済みユーザーを除く)。例えば、次のようにオプトインステータスが異なる 3 人のユーザーがいるとします。

- **ユーザー A** はメールを購読しており、プッシュ通知が有効です。このユーザーはメールを受信しませんが、プッシュ通知は受信します。
- **ユーザー B** はメールにオプトインしていますが、プッシュ通知を有効にしていません。このユーザーはメールを受信しますが、プッシュ通知は受信しません。
- **ユーザー C** はメールにオプトインしており、プッシュ通知が有効です。このユーザーはメールとプッシュ通知の両方を受け取ります。

そのためには、[**オーディエンスの概要**] で、このキャンペーンを「オプトインしたユーザーのみ」に送信するように選択します。このオプションを選択すると、オプトインしたユーザーのみがメールを受信し、Braze は、デフォルトでプッシュ通知が有効になっているユーザーにのみプッシュ通知を送ります。

{% alert important %}
この設定では、**ターゲットオーディエンス**ステップに、オーディエンスを1つのチャネルに制限するフィルターを含めないでください (`Foreground Push Enabled = True` や `Email Subscription = Opted-In` など)。
{% endalert %}

#### コンバージョンイベントを選択する

Braze では、キャンペーンを受信した後、ユーザーが指定のアクションや[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)を実行する頻度を追跡できます。ユーザーが指定したアクションを実行した場合にコンバージョンがカウントされる期間は、最大 30 日間まで設定できます。

{% endtab %}

{% tab Canvas %}

キャンバスコンポーネントが完成していない場合は、残りのセクションを完成させます。キャンバスの残りの部分の構築方法、多変量テストとインテリジェントセレクションの実装方法などの詳細については、キャンバスドキュメントの「[キャンバスを構築する」]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas)ステップを参照のこと。

{% endtab %}
{% endtabs %}

## ステップ 7:レビューと展開 {#review-and-deploy-push}

キャンペーンまたはキャンバスの最後の部分の作成が完了したら、その詳細を確認してください。キャンペーンs の場合、最終頁にあなたが設計したキャンペーンの概要が示されます。関連する詳細をすべて確認し、メッセージをテストしたことをチェックしてから送信し、データが送られてくるのを確認します。

次に、[[プッシュレポート]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/)] をチェックして、プッシュキャンペーンの結果にアクセスする方法を学んでください。プッシュ通知については、メッセージの送信数、配信数、バウンス数、開封数、直接開封数の統計を見ることができる。

