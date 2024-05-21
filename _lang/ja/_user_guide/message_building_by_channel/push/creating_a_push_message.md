---
nav_title: "プッシュメッセージの作成"
article_title: プッシュキャンペーンの作成
page_order: 4
page_type: tutorial
description: "このチュートリアルページでは、設定、送信、ターゲティングなど、プッシュメッセージの作成に関連する様々なコンポーネントについて説明します。"
channel: push
tool:
  - Campaigns
  
---

# プッシュメッセージの作成

> プッシュ通知は、時間的制約のある行動喚起や、しばらくアプリにアクセスしていないユーザーに再度アプローチするのに最適です。プッシュ キャンペーンが成功すると、ユーザーはコンテンツに直接誘導され、アプリの価値が実証されます。

プッシュ通知の例については、[ケーススタディ][8]をご覧ください。

## ステップ 1:メッセージを作成する場所を選択する {#create-new-campaign-push}

メッセージをキャンペーンとキャンバスのどちらで送信すべきか迷っていますか?キャンペーンは単一のシンプルなメッセージングキャンペーンに適しており、キャンバスは複数ステップのユーザージャーニーに適しています。

{% tabs %}
{% tab Campaign %}

**ステップ:**

1. **「メッセージング**」>**「キャンペーン**」に移動し、「**キャンペーンを作成**」をクリックします。
2. 「 **プッシュ通知**」を選択するか、複数のチャネルをターゲットとするキャンペーンの場合は **「マルチチャネルキャンペーン**」を選択します。
3. キャンペーンには、明確で意味のある名前を付けます。
4. 必要に応じて、[チームと]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/)[タグ]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)を追加します。
   * タグを使用すると、キャンペーンを見つけやすくなり、レポートを作成しやすくなります。たとえば、 [レポートビルダー]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)を使用する場合、特定のタグでフィルタリングできます。
5. キャンペーンに必要な数のバリエーションを追加して名前を付けます。追加したバリアントごとに、異なるプラットフォーム、メッセージタイプ、レイアウトを選択できます。このトピックについて詳しくは、 [多変量分析と A/B テスト]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)を参照してください。

{% details Deciding between regular or multichannel push campaign %}

モバイル、ウェブ、Kindle、iOS、Android の任意の組み合わせなど、複数のデバイスやプラットフォームをターゲットにする場合は、このステップでの選択が、後の一部の機能や設定の可用性に影響を与える可能性があります。

マルチチャネルまたはプッシュ通知キャンペーンを作成する前に、次の決定表を参照してください。

!["Flowchart for selecting campaign type. Starts by deciding if you're targeting multiple devices and platforms. If no, it leads to 'Select Push Notification.' If yes, it asks 'What type of push message?' and options are 'Standard push' leading to a decision point 'Do you need to use device-specific settings?' If no, it leads to 'Select Push Notification and use quick push.' If yes, it goes to 'Select Multichannel.' Back to 'What type of push message?', if the answer is 'Push Stories or Inline image,' it directs to 'Select Multichannel."]({% image_buster /assets/img_archive/flowchart_quickpush.png %})

[ **プッシュ通知** ] を選択し、複数のデバイスとプラットフォームをターゲットにすることを選択した場合は、クイックプッシュキャンペーンが自動的に作成されます。クイックプッシュでは、特定のデバイス固有の設定は使用できません。

- プッシュアクションボタン
- 通知チャネルとグループ
- プッシュ TTL
- 表示優先度
- 音

続行する前に、「 [クイックプッシュキャンペーン]({{site.baseurl}}/quick_push) 」を参照して、この編集エクスペリエンスの違いを理解してください。

{% enddetails %}

{% alert tip %}
キャンペーン内のすべてのメッセージが類似しているか、同じ内容になる場合は、パターンを追加する前にメッセージを作成してください。次に、[**バリアントの追加**] ドロップダウンから [**バリアントからコピー**] を選択します。
{% endalert %}

{% endtab %}
{% tab Canvas %}

**ステップ:**

1. Canvas コンポーザーを使用して [Canvas を作成します]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)。
2. キャンバスを設定したら、キャンバスビルダーにステップを追加します。ステップに明確で意味のある名前を付けます。
3. [ステップスケジュール]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay)を選択し、必要に応じて遅延を指定します。
4. 必要に応じて、このステップのオーディエンスをフィルタリングします。セグメントを指定し、フィルターを追加して、このステップの受信者をさらに絞り込みます。後から、メッセージの送信時に、オーディエンスオプションがチェックされます。
5. [進捗動作]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)を選択します。
6. メッセージとペアリングする他のメッセージングチャネルを選択します。

{% endtab %}
{% endtabs %}

## ステップ 2:配信プラットフォームの指定

まず、プッシュを受け取るデバイスとプラットフォームの組み合わせを選択します。この選択を使用して、プッシュ通知の配信を特定のアプリセットに制限します。

これを行うには、以前の選択に応じていくつかの方法があります。

|前の選択 |オプション |
| --- | --- |
|プッシュ通知キャンペーン |1 つ以上のプラットフォームとデバイスを選択します。複数のデバイスやプラットフォームをターゲットにすると、クイックプッシュキャンペーンが自動的に作成されます。これにより、選択したすべてのプラットフォームに対して 1 つのメッセージを 1 つのエディターで作成するために最適化された編集エクスペリエンスが提供されます。「 [クイック プッシュ キャンペーン]({{site.baseurl}}/quick_push) 」を参照して、この編集エクスペリエンスの違いを理解してください。|
|マルチチャネルキャンペーン |「 **メッセージング・チャネルの追加** 」をクリックして、プッシュ・プラットフォームを追加します。プラットフォームの選択は各バリアントに固有であるため、プラットフォームごとにメッセージエンゲージメントをテストできます。
|キャンバス |「メッセージ」ステップで、「 **+さらに追加** 」をクリックしてプッシュ・プラットフォームを追加します。マルチチャネルキャンペーンと同様に、プラットフォームの選択は各バリエーションに固有です。|
{: .reset-td-br-1 .reset-td-br-2}

## ステップ 3:通知の種類を選択 (iOS と Android)

クイックプッシュキャンペーンを作成している場合、通知タイプは自動的に標準プッシュに設定され、変更できません。

![標準プッシュを例に選択した通知タイプ][3]{: style="float:right;max-width:40%;margin-left:15px;"}

それ以外の場合、iOSとAndroidの場合は、通知タイプを選択します。

- 標準プッシュ通知
- [プッシュ通知ストーリー]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)
- インライン画像(Androidのみ)

プッシュキャンペーンに画像を含める場合は、 [iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) または [Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)用のリッチ通知の作成に関する次のガイドを参照してください。

## ステップ 4: プッシュメッセージを作成する

さあ、いよいよプッシュメッセージを書きましょう![ **作成** ] タブでは、メッセージの内容と動作のあらゆる側面を編集できます。

![Compose tab of creating a push notification.]({% image_buster /assets/img_archive/push_compose.png %})

[ **作成** ] タブの内容は、前の手順で選択した通知の種類によって異なりますが、次のオプションのいずれかが含まれる場合があります。

#### 通知チャネルまたはグループ (iOS および Android)

プラットフォーム固有の通知オプションの詳細については、「 [iOS 通知オプション]({{site.baseurl}}/user_guide/message_building_by_channel/push/notification_options_ios/) 」または [「Android 通知オプション]({{site.baseurl}}/user_guide/message_building_by_channel/push/notification_options_android/)」を参照してください。

#### 言語

[ **言語の追加** ] ボタンを使用して、複数の言語でコピーを追加します。コンテンツを書く前に言語を選択し、Liquidのどこにテキストを入力できるようにすることをお勧めします。[利用可能な言語の完全なリスト][18]を参照してください。

#### タイトルと本文

メッセージ ボックスに入力を開始すると、左側のプレビュー ボックスにプレビューが表示されます。プッシュメッセージはプレーンテキストでフォーマットする必要があります。iOS プッシュ通知にヘッドラインを追加するには、「 **タイトル** 」フィールドを使用します。

プッシュをパーソナライズしてターゲットを絞るには、 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)を含めます。

{% alert tip %}
素晴らしいコピーの作成にサポートが必要ですか?[AIコピーライティングアシスタント]({{site.baseurl}}/user_guide/intelligence/ai_copywriting/)を使ってみてください。製品名または説明を入力すると、AIがメッセージングで使用するための人間のようなマーケティングコピーを生成します。

![Launch AI Copywriter button, located in the Body field of the push composer.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

#### 画像

サポートされている場合、アプリアイコンはプッシュ通知の画像として自動的に追加されます。また、リッチ通知を送信するオプションもあり、コピー以外のコンテンツを追加することで、プッシュ通知をさらにカスタマイズできます。

プッシュ通知での画像の使用に関するその他のガイダンスについては、次の記事を参照してください。

- [iOS用のリッチ通知を作成する]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)
- [Android 用のリッチ通知を作成する]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)

#### クリック時動作

ユーザーがプッシュ通知の本文をクリックしたときの動作を **[クリック時の動作**] で指定します。たとえば、顧客にアプリケーションを開くように促したり、指定した Web URL に顧客をリダイレクトしたり、 [ディープ リンク]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/)を使用してアプリケーションの特定のページを開いたりすることができます。

ここでは、プッシュ通知内に次のようなボタンプロンプトを設定することもできます。

- 受諾する / 辞退する
- はい/いいえ
- 確認 / キャンセル
- その他 

#### デバイスオプション

ユーザーが複数のデバイスにアプリをインストールしている場合、デフォルトでは、有効なプッシュトークンが割り当てられたすべてのデバイスにプッシュメッセージが送信されます。必要に応じて、[ **Only send this push to the user's most used device] (このプッシュをユーザーの最近使用したデバイスにのみ送信する)** を選択できます。

![このプッシュをユーザーが最近使用したデバイスにのみ送信するためのデバイスオプションチェックボックス。[9]{: style="max-width:70%;" }

この設定には微妙な違いがあります。このオプションを選択すると、キャンペーンがiOSとAndroidの両方など、複数のプラットフォームをターゲットとしている場合を除き、Brazeは複数の送信を制限します。ユーザーが iOS デバイスと Android デバイスの両方にアプリを持っている場合、ユーザーは両方のプラットフォームのプッシュを受け取ります。ユーザーが最近使用したデバイスが [プッシュ対応]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-enabled)になっていない場合、メッセージは送信されません。

iOSの場合、iPadデバイスにのみプッシュ通知を送信するか、iPhoneおよびiPodデバイスにのみ送信することで、メッセージングをさらに制限できます。

### ステップ4a:メッセージをプレビューしてテストする

![テストプッシュメッセージ][7]{: style="float:right;max-width:30%;margin-left:15px;"}

テストは、間違いなく最も重要なステップの1つです。完璧なプッシュメッセージを作成したら、送信する前にテストします。「 **テスト** 」タブを選択し、「 **ユーザーとしてメッセージをプレビュー」** を使用して、メッセージがモバイルでどのように表示されるかを把握します。[ **テストの送信** ] を使用してテスト プッシュを送信し、メッセージが正しく表示されることを確認します。

## ステップ 5: キャンペーンまたはキャンバスの残りの部分を作成する

{% tabs %}
{% tab Campaign %}

キャンペーンの残りの部分を構築します。プッシュ通知を構築するためのツールの最適な活用方法の詳細については、次のセクションを参照してください。

#### 配信スケジュールまたはトリガーを選択する

プッシュメッセージは、スケジュールされた時間、アクション、またはAPIトリガーに基づいて配信できます。詳しくは、 [キャンペーンのスケジュール設定]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)を参照してください。

アクションベースの配信の場合は、キャンペーンの期間と [待機時間]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours)を設定することもできます。

このステップでは、ユーザーがキャンペーンを受け取る資格 [を再]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) 取得できるようにする方法や、 [フリークエンシー キャップ]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) ルールを有効にする方法など、配信制御を指定することもできます。

#### ターゲットとするユーザーを選択する

次に、セグメントまたはフィルターを選択して [ユーザーをターゲティング]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) し、オーディエンスを絞り込む必要があります。そのおおよそのセグメント母集団が現在どのようになっているかのスナップショットが自動的に提供されます。キャンペーンのターゲットとするチャンネルの詳細なオーディエンス統計情報は、フッターで確認できます。このセグメントのターゲットにされているユーザーベースの割合とライフタイムバリューを確認するには、[ **追加の統計情報を表示**] をクリックします。

{% details Why does my Total Reachable Users metric not match the sum of all channels? %}

絞り込まれたオーディエンスの [Total Reachable Users (到達可能なユーザーの合計)] を表示すると、個々の列の合計が [Total Reachable Users (到達可能なユーザーの合計)] よりも小さいことに気付く場合があります。このギャップは、通常、キャンペーンのセグメントまたはフィルターに適格であるが、プッシュでは到達できないユーザーが多数いるためです(たとえば、有効な [プッシュトークンまたはアクティブなプッシュトークン]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens)を持っていないため)。

{% enddetails %}

![Table of detailed audience statistics for Reachable Users.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

正確なセグメントメンバーシップは、常にメッセージが送信される直前に計算されることに注意してください。

また、特定の [サブスクリプションステータス]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)を持つユーザー(サブスクライブ済みでプッシュをオプトインしているユーザーなど)にのみキャンペーンを送信するように選択することもできます。

必要に応じて、セグメント内の指定した数のユーザーに配信を制限したり、キャンペーンの繰り返し時にユーザーが同じメッセージを 2 回受信できるようにしたりすることもできます。

##### メールとプッシュによるマルチチャネルキャンペーン

メールチャネルとプッシュチャネルの両方をターゲットとするマルチチャネルキャンペーンでは、明示的にオプトインしたユーザー(購読または購読解除したユーザーを除く)のみがメッセージを受信するようにキャンペーンを制限できます。たとえば、オプトインステータスの異なるユーザーが 3 人いるとします。

- **ユーザー A** は電子メールを購読しており、プッシュが有効になっています。このユーザーはメールを受信しませんが、プッシュを受信します。
- **ユーザー B** はメールにオプトインされていますが、プッシュは有効になっていません。このユーザーはメールを受信しますが、プッシュは受信しません。
- **ユーザー C** は電子メールにオプトインされており、プッシュが有効になっています。このユーザーは、メールとプッシュの両方を受信します。

これを行うには、[ **オーディエンスの概要**]で、このキャンペーンを「オプトインしたユーザーのみ」に送信するように選択します。このオプションにより、オプトインしたユーザーのみがメールを受信し、Brazeはデフォルトでプッシュが有効になっているユーザーにのみプッシュを送信します。

{% alert important %}
この設定では、オーディエンスを 1 つのチャネルに制限するフィルターを [ **対象ユーザー** ] ステップに含めないでください( `Push Enabled = True` `Email Subscription = Opted-In`や など)。
{% endalert %}

#### コンバージョン イベントを選択する

Brazeを使用すると、ユーザーがキャンペーンを受け取った後、特定のアクション( [コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/))を実行する頻度を追跡できます。最大 30 日間の期間を指定して、ユーザーが指定したアクションを実行した場合にコンバージョンがカウントされるように設定することもできます。

{% endtab %}

{% tab Canvas %}

まだ行っていない場合は、Canvas コンポーネントの残りのセクションを完了します。Canvas の残りの部分を構築する方法、多変量テストとインテリジェント選択を実装する方法などの詳細については、Canvas ドキュメントの「 [Canvas の構築]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) 」ステップを参照してください。

{% endtab %}
{% endtabs %}

## ステップ 6:確認と展開 {#review-and-deploy-push}

最後のキャンペーンまたはキャンバスの作成が完了したら、その詳細を確認します。キャンペーンの場合、最後のページには、デザインしたキャンペーンの概要が表示されます。関連するすべての詳細を確認し、メッセージをテストしたことを確認してから送信し、データがロールインするのを見てください。

次に、 [プッシュレポート]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) で、プッシュキャンペーンの結果にアクセスする方法を確認してください。プッシュ通知の場合、送信、配信、バウンス、開封、直接開封されたメッセージの数の統計を表示できます。

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
