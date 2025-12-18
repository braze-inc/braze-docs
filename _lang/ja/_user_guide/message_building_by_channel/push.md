---
nav_title: プッシュ
article_title: プッシュ
page_order: 4
layout: dev_guide
guide_top_header: "プッシュ"
guide_top_text: "プッシュ通知は、モバイルやWebを通じてタイムセンシティブなアクションを呼びかけたり、しばらくアプリに来ていなかったユーザーを再びエンゲージしたりするための、試行錯誤を重ねた方法だ。ユーザーを直接コンテンツに誘導し、アプリケーションの価値を示す。プッシュ通知はユーザーを特定の場所に誘導するのに便利だが、賢く使うべきだ。<br><br> 次の記事を読んだり、当社の[プッシュBrazeラーニングコース](https://学習.Braze.com/メッセージング-チャネルs-push)をチェックアウトしたりして、誰にプッシュを送信できるのか、どのように送信するのか、そしてBrazeが提供する高度なプッシュ機能について学びましょう。プッシュ通知の例については、[顧客ストーリー](https://www.braze.com/customers)をご覧いただきたい。"
description: "このランディングページは、メッセージをプッシュするためのホームです。ここには、プッシュタイプ、プッシュ登録、プッシュイネーブルメント、プッシュのオプトイン促進、プッシュレポートなどに関する記事があります。"
channel:
  - push

guide_featured_title: "よく読まれている記事"
guide_featured_list:
- name: プッシュタイプ
  link: /docs/user_guide/message_building_by_channel/push/types/
  image: /assets/img/braze_icons/list.svg
- name: プッシュ登録
  link: /docs/user_guide/message_building_by_channel/push/push_registration/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: プッシュ有効化とサブスクリプション
  link: /docs/user_guide/message_building_by_channel/push/users_and_subscriptions/
  image: /assets/img/braze_icons/users-01.svg
- name: プッシュメッセージの作成
  link: /docs/user_guide/message_building_by_channel/push/creating_a_push_message/
  image: /assets/img/braze_icons/edit-05.svg

guide_menu_title: "More articles"
guide_menu_list:
- name: 詳細オプション
  link: /docs/user_guide/message_building_by_channel/push/advanced_push_options/
  image: /assets/img/braze_icons/settings-01.svg
- name: プッシュプライマー
  link: /docs/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
  image: /assets/img/braze_icons/phone-02.svg
- name: レポート
  link: /docs/user_guide/message_building_by_channel/push/push_reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Android設定
  link: /docs/user_guide/message_building_by_channel/push/android/
  image: /assets/img/braze_icons/android.svg
- name: iOS オプション
  link: /docs/user_guide/message_building_by_channel/push/ios/
  image: /assets/img/braze_icons/apple.svg
- name: Webプッシュ
  link: /docs/user_guide/message_building_by_channel/push/web/
  image: /assets/img/braze_icons/monitor-01.svg
- name: ベストプラクティス
  link: /docs/user_guide/message_building_by_channel/push/best_practices/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: メッセージのロケール
  link: /docs/locales_in_messages/
  image: /assets/img/braze_icons/translate-01.svg
- name: 一般的なプッシュ・エラー・メッセージ
  link: /docs/user_guide/message_building_by_channel/push/push_error_codes/
  image: /assets/img/braze_icons/alert-triangle.svg
- name: トラブルシューティング
  link: /docs/user_guide/message_building_by_channel/push/troubleshooting/
  image: /assets/img/braze_icons/annotation-question.svg
- name: よくある質問
  link: /docs/user_guide/message_building_by_channel/push/faq/
  image: /assets/img/braze_icons/annotation-question.svg
---

## [![Braze ラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"} ユースケース

![複数の Apple 製品にわたるプッシュ通知メッセージの例。]({% image_buster /assets/img/red-dress.gif %}){: height="400px"} ![iPhoneのホーム画面に表示されるStopwatchのプッシュメッセージの例:「こんにちは。これは iOS プッシュ通知です。」]({% image_buster /assets/img/ios_push.png %}){: height="400px"}

プッシュ通知は、新しいユーザーを引き付け、再エンゲージメントキャンペーンを行うための非常に優れたツールです。一般的なプッシュメッセージユースケースの例を次に示します。

| ユースケース | 説明 |
| -------- | ----------- |
| 初期オンボーディング | ユーザーがアプリの使用に向けて最初のステップ (アカウントの登録など) を実行するまで、アプリの価値は大幅に制限されています。プッシュ通知を使用して、これらの手順を完了してアプリを完全な使用を開始するようにユーザーを促します。 |
| 初回購入 | ユーザーがアプリを快適に使用できるようになったら、プッシュ通知を使用してユーザーをアプリ内購入者にコンバートできます。 |
| 新機能 | プッシュ通知は、離脱ユーザーへの新機能の通知に効果的で、それらのユーザーをアプリに呼び戻す可能性があります。 |
| 時間に敏感なオファー | オファーに時計をチェックすることがある場合、プッシュは、期限切れになるまでにユーザーに知らせるのに便利な方法です。通常、これらのメッセージは高い緊迫感を伝え、最近離脱したユーザーにアプリを思い出してもらう場合に最適です。<br><br> 例えば、御社のアプリがゲームであり、毎日そのゲームをプレイし続けているユーザーにゲーム内通貨ボーナスを提供しているとします。ストリークが壊れてしまう危険性があることをユーザーに知らせることは、ある日数を超えてしまった場合には、合理的なプッシュとなる可能性があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

離脱ユーザーの再エンゲージメントの詳細については、トピックの[迅速な獲得]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users)ページを参照してください。

## プッシュを使用するための前提条件

Braze を使用してプッシュ通知メッセージの作成および送信を行うには、開発者と協力してプッシュ通知を Web サイトまたはアプリに統合する必要があります。詳細なステップについては、プラットフォームごとのインテグレーションガイドを参照してください。

- [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)
- [Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## プッシュプライミング

ユーザーがお客様のメッセージを受信するには、プッシュ通知にオプトインする必要があることに留意してください。つまり、アプリ内メッセージを使用して、お客様がプッシュ通知を送信する理由や、プッシュを有効にすることで得られるメリットを顧客に説明することをお勧めします。このプロセスは、[プッシュプライミング]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)と呼ばれます。

## プッシュメッセージ規定

プッシュメッセージは顧客の携帯電話やブラウザに直接届く押し付けがましいタイプのメッセージングであるため、アプリやサイトを通じてプッシュメッセージを送信するにはガイドラインがある。

### アプリのモバイルプッシュ規定

{% alert important %}
プッシュメッセージは、Apple App Store およびGoogle のPlay Store ポリシーのガイドラインに含まれている必要があります。特に、プッシュメッセージをアドバタイズメント、スパム、プロモーションなどとして使用する場合に使用します。
{% endalert %}

|Apple App Store ポリシー|
|---|
|[3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) 受け入れられません: (i) App Storeに類似したサードパーティ製のアプリ、拡張機能、またはプラグインを表示するためのインターフェイスの作成、または一般的な関心の集合として。| 
|[4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) プッシュ通知は、アプリが機能するために必要ではなく、機密性の高い個人情報や機密情報の送信には使用しないでください。プッシュ通知をキャンペーンやダイレクトマーケティングのために使用することはできません。ただし、そのプッシュ通知を、ユーザーがアプリの UI に表示される同意メッセージを通じて明示的にオプトインすることができ、同時にオプトアウトする手段をアプリに設ける場合を除きます。|
|[4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) ハードウェアやオペレーティングシステムに内蔵されている機能 (プッシュ通知、カメラ、ジャイロスコープなど) または Apple のサービスやテクノロジー (Apple Music へのアクセス、iCloud ストレージ、Screen Time API など) を収益化することは認められません。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

|Google Playストアポリシー|
|---|
|[不正な使用またはシステム機能の模倣](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) 通知や警告などのシステム機能を模倣したり妨害したりするアプリや広告を許可していません。システムレベルの通知は、ユーザーに特別価格を通知する航空会社のアプリや、ユーザーにゲーム内プロモーションを通知するゲームなど、アプリの重要な機能にのみ使用できます。|
{: .reset-td-br-1 role="presentation" }
