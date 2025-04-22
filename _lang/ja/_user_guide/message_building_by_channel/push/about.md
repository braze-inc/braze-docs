---
nav_title: "プッシュ通知について"
article_title: プッシュ通知について
page_order: 0
page_type: reference
description: "このリファレンス記事では、プッシュ通知の概要、プッシュ通知メッセージの使用を開始するためのリソース、およびいくつかの規制について説明します。"
channel:
  - Push

---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-push){: style="float:right;width:120px;border:0;" class="noimgborder"}プッシュ通知についてs

> プッシュ通知は、時間的な制約のあるアクションの呼びかけや、しばらくアプリを使用していないユーザーの再獲得において、非常に優れています。プッシュ通知のキャンペーンが成功すると、ユーザーを直接コンテンツに移動し、アプリケーションの価値を提示します。

ユーザーがお客様のメッセージを受信するには、プッシュ通知にオプトインする必要があることに留意してください。つまり、アプリ内メッセージを使用して、お客様がプッシュ通知を送信する理由や、プッシュを有効にすることで得られるメリットを顧客に説明することをお勧めします。このプロセスは、[プッシュプライミング]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)と呼ばれます。

![複数の Apple 製品にわたるプッシュ通知メッセージの例。][1]{: height="400px"} ![iPhoneのホーム画面に表示されるStopwatchのプッシュメッセージの例:「こんにちは。これは iOS プッシュ通知です。」][2]{: height="400px"}

プッシュ通知のその他の例については、[ケーススタディ][8]をご覧ください。

## 潜在ユースケースs

プッシュ通知は、新しいユーザーを引き付け、再エンゲージメントキャンペーンを行うための非常に優れたツールです。一般的なプッシュメッセージユースケースの例を次に示します。

| ユースケース | 説明 |
| -------- | ----------- |
| 初期オンボーディング | ユーザーがアプリの使用に向けて最初のステップ (アカウントの登録など) を実行するまで、アプリの価値は大幅に制限されています。プッシュ通知を使用して、これらの手順を完了してアプリを完全な使用を開始するようにユーザーを促します。 |
| 初回購入 | ユーザーがアプリを快適に使用できるようになったら、プッシュ通知を使用してユーザーをアプリ内購入者にコンバートできます。 |
| 新機能 | プッシュ通知は、離脱ユーザーへの新機能の通知に効果的で、それらのユーザーをアプリに呼び戻す可能性があります。 |
| 時間に敏感なオファー | オファーに時計をチェックすることがある場合、プッシュは、期限切れになるまでにユーザーに知らせるのに便利な方法です。通常、これらのメッセージは高い緊迫感を伝え、最近離脱したユーザーにアプリを思い出してもらう場合に最適です。<br><br> 例えば、御社のアプリがゲームであり、毎日そのゲームをプレイし続けているユーザーにゲーム内通貨ボーナスを提供しているとします。ストリークが壊れてしまう危険性があることをユーザーに知らせることは、ある日数を超えてしまった場合には、合理的なプッシュとなる可能性があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

離脱ユーザーの再エンゲージメントの詳細については、トピックの[迅速な獲得][23]ページを参照してください。

## プッシュを使用するための前提条件

Braze を使用してプッシュ通知メッセージの作成および送信を行うには、開発者と協力してプッシュ通知を Web サイトまたはアプリに統合する必要があります。詳細なステップについては、プラットフォームごとのインテグレーションガイドを参照してください。

- [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)
- [Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## プッシュメッセージ規定

プッシュメッセージは、顧客の電話機またはブラウザーに直接的に送信される侵入型のメッセージングであるため、アプリ s およびサイトを介してプッシュメッセージを送信するための指針があります。

### アプリのモバイルプッシュ規定

{% alert important %}
プッシュメッセージは、Apple App Store およびGoogle のPlay Store ポリシーのガイドラインに含まれている必要があります。特に、プッシュメッセージをアドバタイズメント、スパム、プロモーションなどとして使用する場合に使用します。
{% endalert %}

|Apple App Store ポリシー|
|---|
|[3.2.2][9] 受け入れられません: (i) サードパーティ製のアプリs、拡張機能、またはプラグインをアプリストアと同様に表示するためのインターフェイスの作成、または一般的な利害関係の収集として。| 
|[4.5.4][7] アプリが機能するためにプッシュ通知を必須とすることはできません。また、プッシュ通知を個人情報や秘密情報を送信するために使用することは許可されません。プッシュ通知をキャンペーンやダイレクトマーケティングのために使用することはできません。ただし、そのプッシュ通知を、ユーザーがアプリの UI に表示される同意メッセージを通じて明示的にオプトインすることができ、同時にオプトアウトする手段をアプリに設ける場合を除きます。|
|[4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) ハードウェアやオペレーティングシステムに内蔵されている機能 (プッシュ通知、カメラ、ジャイロスコープなど) または Apple のサービスやテクノロジー (Apple Music へのアクセス、iCloud ストレージ、Screen Time API など) を収益化することは認められません。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

|Google Playストアポリシー|
|---|
|[システム機能の不正な使用または模倣][10] 通知やワーニングなどのシステム機能を模倣したり妨害したりするアプリsや広告を許可しません。システムレベルの通知は、ユーザーに特別価格を通知する航空会社のアプリや、ユーザーにゲーム内プロモーションを通知するゲームなど、アプリの重要な機能にのみ使用できます。|
{: .reset-td-br-1 role="presentation" }

[1]: {% image_buster /assets/img/red-dress.gif %}
[2]: {% image_buster /assets/img/ios_push.png %}
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content
[8]: https://www.braze.com/customers
[7]: https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services
[9]: https://developer.apple.com/app-store/review/guidelines/#unacceptable
[10]: https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories
[23]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
