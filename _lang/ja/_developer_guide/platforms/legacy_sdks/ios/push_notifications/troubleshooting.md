---
nav_title: トラブルシューティング
article_title: iOS のプッシュ通知のトラブルシューティング
platform: iOS
page_order: 30
description: "この参照記事では、iOS のプッシュ実装に関する潜在的なトラブルシューティングトピックについて説明します。"
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# {#push-troubleshooting} の トラブルシューティング

## Braze/APNs のワークフローについて

Apple プッシュ通知サービス (APNs) は、iOS および OS X アプリにプッシュ通知を送信するための Apple のインフラです。ユーザーのデバイスに対してプッシュ通知を有効にする方法と、Braze がユーザーにプッシュ通知を送信する方法の簡単な構造を次に示します。

1. プッシュ証明書とプロビジョニングプロファイルを構成します
2. デバイスは　APNs に登録し、Braze にプッシュトークンを提供します
3. Braze プッシュキャンペーンを開始します
4. Braze は無効なトークンを削除します

#### ステップ1:プッシュ証明書とプロビジョニングプロファイルの構成

アプリの開発では、プッシュ通知を有効にするには SSL 証明書を作成する必要があります。この証明書はアプリのビルドに使用されるプロビジョニングプロファイルに含まれ、Braze ダッシュボードにアップロードする必要もあります。証明書を使用すると、、Braze は APNs に対して、あなたに代わってプッシュ通知を送信することが許可されていることを伝えることができます。

[プロビジョニングプロファイル](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html)と証明書には、開発と配布の2つのタイプがあります。混乱を避けるために、配布プロファイルと証明書だけを使用することをお勧めします。開発と配布で異なるプロファイルと証明書を使用することを選択した場合は、ダッシュボードにアップロードされた証明書が現在使用しているプロビジョニングプロファイルと一致することを確認してください。

{% alert warning %}
プッシュ証明書の環境 (開発環境と本番環境) を変更しないでください。プッシュ証明書を間違った環境に変更すると、ユーザーのプッシュトークンが誤って削除され、プッシュで到達できなくなる可能性があります。
{% endalert %}

#### ステップ 2:デバイスは　APNs に登録し、Braze にプッシュトークンを提供します

ユーザーがアプリを開くと、プッシュ通知を受け入れるように求められます。このプロンプトを受け入れると、APNs はその特定のデバイスのプッシュトークンを生成します。iOS SDK は、デフォルトの[自動フラッシュポリシー]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/fine_network_traffic_control/#automatic-request-processing) を使用して、アプリのプッシュトークンを直ちに非同期に送信します。ユーザーにプッシュトークンを関連付けると、［**エンゲージメント**］ タブのユーザープロファイルのダッシュボードに「プッシュ登録済み」と表示され、Braze キャンペーンからプッシュ通知を受け取る資格が得られます。

{% alert note %}
Xcode 14 では、iOS シミュレーター上でリモートプッシュ通知をテストできます。
{% endalert %}

#### ステップ3: Braze プッシュキャンペーンの開始

プッシュキャンペーンが開始されると、Braze は APNs にメッセージの配信リクエストを行います。Braze は、ダッシュボードにアップロードされた SSL プッシュ証明書を使用して認証を行い、提供されたプッシュトークンへのプッシュ通知の送信が許可されていることを確認します。デバイスがオンラインの場合は、キャンペーンが送信された後すぐに通知が受信されます。なお、Braze は通知のデフォルトの APNs [有効期限](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607)を30日に設定していることに注意してください。

#### ステップ4: 無効なトークンを削除する

[APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) が、メッセージを送信しようとしていたプッシュトークンのいずれかが無効であることを通知した場合、それらのトークンは関連付けられたユーザープロファイルから削除されます。

## プッシュエラーログの活用

Braze は、**メッセージアクティビティログ**内のプッシュ通知エラーのログを提供します。このエラーログは、キャンペーンが期待どおりに機能していない理由を特定するのに非常に役立つさまざまな警告を提供します。エラーメッセージをクリックすると、特定のインシデントのトラブルシューティングに役立つ関連ドキュメントにリダイレクトされます。

![エラーログをプッシュして、エラーが発生した時間、アプリ名、チャネル、エラータイプ、およびエラーメッセージを表示します。]({% image_buster /assets/img_archive/message_activity_log.png %})

ここでよく見かけるエラーとしては、[[「プッシュトークンへの登録されていない送信の受信」]](#received-unregistered-sending) など、ユーザー固有の通知があります。

さらに、Braze は ［**エンゲージメント**］ タブのユーザープロファイルにプッシュ通知の変更ログも提供します。この変更ログは、トークンの無効化、プッシュ登録エラー、トークンの新規ユーザーへの移動などのプッシュ登録動作に関するインサイトを提供します。

![]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

## プッシュ登録に関する問題

アプリケーションのプッシュ登録ロジックの検証を追加するには、[プッシュユニットテスト]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests/)を実装します。

#### プッシュ登録プロンプトが表示されない

アプリケーションでプッシュ通知の登録を求めるメッセージが表示されない場合は、プッシュ登録の統合に問題がある可能性があります。[documentation]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration/)に従っており、プッシュ登録が正しく統合されていることを確認してください。コードにブレークポイントを設定して、プッシュ登録コードを確実に実行することもできます。

#### ダッシュボードに「プッシュ登録済み」ユーザーが表示されない

- アプリがプッシュ通知を許可するように求めるメッセージを表示していることを確認します。通常、このプロンプトはアプリを初めて起動したときに表示されますが、他の場所に表示されるようにプログラムすることもできます。表示されるべき場所に表示されない場合は、アプリのプッシュ機能の基本構成に問題がある可能性があります。
  - [push integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration/)の手順が正常に完了したことを確認します。
  - アプリのビルドに使用されたプロビジョニングプロファイルにプッシュの権限が含まれていることを確認します。Apple 開発者アカウントから利用可能なプロビジョニングプロファイルをすべてプルダウンしていることを確認してください。これを確認するには、次の手順を実行します。
    1. Xcodeで、**［環境設定］ > ［アカウント］** に移動します (または、キーボードショートカット [<kbd>Command</kbd>+<kbd>,</kbd>] を使用します）。
    2. 開発者アカウントに使用する Apple ID を選択し、［**詳細を表示**］ をクリックします。
    3. 次のページで、[**<i class="fas fa-redo-alt"></i>更新**] をクリックし、使用可能なすべてのプロビジョニングプロファイルをプルしていることを確認します。
- アプリで[適切に有効なプッシュ機能]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-2-enable-push-capabilities)があることを確認します。
- プッシュプロビジョニングプロファイルがテスト環境と一致することを確認します。ユニバーサル証明書は、開発または実稼働の APNs 環境のいずれかに送信するように Braze ダッシュボードで構成できます。実稼働アプリ用の開発証明書または開発アプリ用の実稼働証明書は動作しません。
- コードにブレークポイントを設定して、`registerPushToken` メソッドを呼び出していることを確認します。
- デバイス上にあり (シミュレーター上ではプッシュが機能しない)、ネットワーク接続が良好であることを確認します。

## デバイスがプッシュ通知を受信しない

#### プッシュ通知の送信後にユーザーが「プッシュ登録」されなくなった

これは、ユーザーが無効なプッシュトークンを持っていたことを示している可能性があります。これにはいくつかの理由が考えられます。

##### ダッシュボードとアプリ証明書が一致していない

ダッシュボードでアップロードしたプッシュ証明書が、アプリのビルドに使用したプロビジョニングプロファイルのものと異なる場合、APNs はトークンを拒否します。別のテスト通知を試みる前に、正しい証明書をアップロードし、アプリで別のセッションを完了していることを確認します。

##### アンインストール数

ユーザーがアプリケーションをアンインストールした場合、プッシュトークンは無効となり、次回の送信時に削除されます。

##### プロビジョニングプロファイルの再生成

最後の手段として、最初からやり直してまったく新しいプロビジョニングプロファイルを作成すると、複数の環境、プロファイル、およびアプリを同時に操作することによって発生する構成エラーを解消できます。iOS アプリのプッシュ通知の設定は「動く部分」が多いので、最初からやり直したほうがいい場合もあります。また、トラブルシューティングを続ける必要がある場合は、問題を切り分けるのに役立ちます。

#### プッシュ通知を送信した後もユーザーが「プッシュ登録」される

##### アプリがフォアグラウンドにある

`UserNotifications` フレームワークを介してプッシュを統合していない iOS バージョンでは、プッシュメッセージの受信時にアプリがフォアグラウンドにある場合、そのメッセージは表示されません。テストメッセージを送信する前に、テストデバイスでアプリをバックグラウンドにする必要があります。

##### テスト通知のスケジュールが正しくない

テストメッセージに設定したスケジュールを確認します。ローカルタイムゾーン配信または[インテリジェントタイミング]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)に設定されている場合、メッセージがまだ受信されていない (または受信時にアプリをフォアグラウンドにしていた) だけかもしれません。

#### テスト対象のアプリに対してユーザーが「プッシュ登録」されていない

テストメッセージを送信しようとしてしている相手のユーザーのプロファイルを確認します。[**エンゲージメント**] タブの下に「プッシュ可能なアプリ」のリストがあるはずです。テストメッセージを送信しようとしているアプリがこのリストにあることを確認します。ユーザーがワークスペース内の任意のアプリのプッシュトークンを持っている場合は「プッシュ登録済み」と表示されるため、誤検知の可能性があります。

以下は、プッシュ登録に問題があるか、プッシュ後にユーザーのトークンが APNs によって無効として Braze に返されたことを示します。

![ユーザの連絡先設定を表示するユーザプロファイル。ここでは、どのアプリがプッシュ通知に登録されているかを確認できます。]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## プッシュメッセージが送信されない

送信されないプッシュ通知のトラブルシューティングについては、「[プッシュ通知のトラブルシューティング]({{site.baseurl}}/user_guide/message_building_by_channel/push/troubleshooting/)」を参照のこと。

## メッセージアクティビティログのエラー

#### プッシュトークン {#received-unregistered-sending} への未登録送信を受信した

- メソッド `[[Appboy sharedInstance] registerPushToken:]` から Braze に送信されているプッシュトークンが有効であることを確認してください。**メッセージアクティビティログ**を見ると、プッシュトークンを確認できます。これは `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6` のようになり、文字と数字が混在する長い文字列になります。プッシュトークンが異なるように見える場合は、Braze にプッシュトークンを送信するための [[コード]]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-4-register-push-tokens-with-braze) を確認してください。
- プッシュプロビジョニングプロファイルがテスト対象の環境と一致することを確認します。ユニバーサル証明書は、開発または実稼働の APNs 環境のいずれかに送信するように Braze ダッシュボードで構成できます。実稼働アプリ用の開発証明書または開発アプリ用の実稼働証明書は動作しません。
 - Braze にアップロードしたプッシュトークンが、プッシュトークンの送信元のアプリのビルドに使用したプロビジョニングプロファイルと一致することを確認します。

#### デバイストークンがトピック用ではない

このエラーは、アプリのプッシュ証明書とバンドル ID が一致しないことを示しています。Brazeにアップロードしたプッシュ証明書が、プッシュトークンの送信元となるアプリのビルドに使用したプロビジョニングプロファイルと一致することを確認します。

#### プッシュトークンへの BadDeviceToken の送信

`BadDeviceToken` は APNs のエラーコードであり、Braze から発信されたものではありません。この応答が返されるには、次のようなさまざまな理由が考えられます。

- アプリは、ダッシュボードにアップロードされた認証情報に対して無効なプッシュトークンを受け取った。
- このワークスペースではプッシュが無効になった。
- ユーザーがプッシュをオプトアウトした。
- アプリがアンインストールされた。
- Apple がプッシュトークンを更新したため、古いトークンが無効になった。
- アプリは本番環境用にビルドされていますが、Braze にアップロードされたプッシュ認証情報は開発環境用に設定されます (または逆の場合もあります)。

## プッシュ配信後の問題

アプリケーションのプッシュ処理の検証を追加するには、[プッシュユニットテスト]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests/) を実装します。

#### プッシュクリックが記録されない {#push-clicks-not-logged}

- これがiOS 10 でのみ発生する場合は、[iOS 10]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling) のプッシュ統合手順に従っていることを確認します。
- Braze では、フォアグラウンドでサイレント受信したプッシュ通知 (`UserNotifications` フレームワーク以前のデフォルトのフォアグラウンドプッシュ動作など) は処理されません。つまり、リンクは開かれず、プッシュクリックは記録されません。アプリケーションが `UserNotifications` フレームワークをまだ統合していない場合、アプリケーション状態が `UIApplicationStateActive` のときに Braze はプッシュ通知を処理しません。アプリが[プッシュ処理メソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling) へのコールを遅延しないようにする必要があります。遅延しない場合、iOS SDK はプッシュ通知をサイレントフォアグラウンドプッシュイベントとして扱い、処理しないことがあります。

#### プッシュクリックからのWebリンクが開かない

iOS 9以降では、ウェブビューで開くにはATS準拠のリンクが必要です。WebリンクがHTTPSを使用していることを確認します。詳細については、[ATS 準拠]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#app-transport-security-ats) の記事を参照してください。

#### プッシュクリックからディープリンクが開かない

ディープリンクを扱うコードのほとんどはプッシュ通知の開封も扱います。まず、プッシュ通知の開封がログに記録されていることを確認します。そうでない場合は、[問題](#push-clicks-not-logged)を修正します(多くの場合、修正によりリンク処理が修正されます)。

開封が記録されている場合は、ディープリンク全般の問題なのか、ディープリンクのプッシュクリック処理の問題なのかを確認してください。そのためには、アプリ内メッセージクリックからのディープリンクが機能するかテストします。

#### 直接開封はほとんどない、または全くない

iOS プッシュ通知を開封したユーザーが1人以上いるにもかかわらず、Braze に_直接開封_のログがほとんど残っていない場合、[SDKの統合]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/)に問題がある可能性があります。テスト送信またはサイレントプッシュ通知については、_Direct Opens_はログに記録されません。

- メッセージが[サイレントプッシュ通知]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/#sending-silent-push-notifications)として送信されていないことを確認します。メッセージがサイレントメッセージと見なされないようにするには、タイトルまたは本文にテキストを含める必要があります。
- [プッシュ統合ガイド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration/)から以下のステップをダブルチェックします。
   - [プッシュを登録する]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns):アプリを起動するたびに、できれば`application:didFinishLaunchingWithOptions:` 内で、ステップ3のコードを実行する必要があります。`UNUserNotificationCenter.current()` のdelegate プロパティは、`UNUserNotificationCenterDelegate` を実装し、`(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` メソッドを含むオブジェクトに割り当てる必要があります。
   - [プッシュ処理を有効にする]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/push_notifications/integration/#step-5-enable-push-handling):`(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` メソッドが実装されていることを確認します。

