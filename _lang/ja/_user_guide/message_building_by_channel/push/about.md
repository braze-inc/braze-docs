---
nav_title: "プッシュ通知について"
article_title: プッシュ通知について
page_order: 0
page_type: reference
description: "このリファレンス記事では、プッシュの概要、プッシュメッセージの使用を開始するためのリソース、およびいくつかの規制について説明します。"
channel:
  - Push

---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-push){: style="float:right;width:120px;border:0;" class="noimgborder"}プッシュ通知についてs

> プッシュ通知sは、アクションへの時間に敏感な通話や、しばらくアプリに入ってこなかったユーザーの再参加には素晴らしいです。プッシュキャンペーンが成功すると、ユーザーは直接的にコンテンツに移行し、アプリライセンスの価値を実証します。

ユーザーは、メッセージの受信をプッシュするためにオプトインする必要があることに留意してください。つまり、アプリ内メッセージ s を使用して、プッシュ通知 s を送信する理由や、プッシュを有効にすることでメリットが得られる方法を顧客に説明することができます。このプロセスは、[プッシュプライミング]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/create_push_primer/)と呼ばれます。

![アップル製品にまたがるプッシュメッセージの例。][1]{: height="400px"} ![iPhoneのホーム画面に表示されるStopwatchのプッシュメッセージの例:"こんにちは！これはiOS のPush" です。][2]{: height="400px"}

プッシュ通知 s の他のサンプルを表示するには、\[Case Studies][8]] を参照してください。

## 潜在ユースケースs

プッシュ通知sは、新しいユーザーsを引き付け、再エンゲージメント キャンペーンsを作成するための優れた道具です。一般的なプッシュメッセージユースケースの例を次に示します。

| ユースケース | 説明 |
| -------- | ----------- |
| 初期オンボーディング | ユーザーsがアプリの使用(アカウントの登録など)に向けて最初のステップsをとるまでは、その価値は厳しく制限されます。プッシュ通知 s を使用してユーザー s にこれらのステップ s を完了させ、アプリを完全に使用できるようにします。 |
| 初回購入 | ユーザー s がアプリの使用に適している場合は、プッシュ通知 s を使用して、インアプリの購入者に変換することができます。 |
| 新機能 | プッシュ通知 s は、新しい機能がアプリに呼び戻される可能性があることをユーザーに通知するのに効果的です。 |
| 時間に敏感なオファー | オファーに時計をチェックすることがある場合、プッシュは、期限切れになるまでにユーザーに知らせるのに便利な方法です。一般的に、これらの伝言は切迫感が強く、最近のユーザーにあなたのアプリを思い出させるのに最適です。<br><br> たとえば、アプリがゲームであり、毎日ゲームをプレイするような連続性を維持している場合に、ユーザーにゲーム内通貨ボーナスを提供するとします。ストリークが壊れてしまう危険性があることをユーザーに知らせることは、ある日数を超えてしまった場合には、合理的なプッシュとなる可能性があります。 |
{: .reset-td-br-1 .reset-td-br-2}

失効したユーザー s の再適用の詳細については、トピックスの\[Quick Wins][23] ページを参照してください。

## プッシュを使用するための前提条件

Braze を使用してプッシュメッセージを作成および送信するには、開発者 s を使用してプッシュをWeb サイトまたはアプリに統合する必要があります。詳細なステップについては、プラットフォームごとのインテグレーションガイドを参照してください。

- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/)

## プッシュメッセージ規定

プッシュメッセージは、顧客の電話機またはブラウザーに直接的に送信される侵入型のメッセージングであるため、アプリ s およびサイトを介してプッシュメッセージを送信するための指針があります。

### アプリ向け携帯電話プッシュ規定

{% alert important %}
プッシュメッセージは、Apple App Store およびGoogle のPlay Store ポリシーのガイドラインに含まれている必要があります。特に、プッシュメッセージをアドバタイズメント、スパム、プロモーションなどとして使用する場合に使用します。
{% endalert %}

|Apple App Store ポリシー|
|---|
|\[3.2.2][9] 受け入れられません: (i) サードパーティ製のアプリs、拡張機能、またはプラグインをアプリストアと同様に表示するためのインターフェイスの作成、または一般的な利害関係の収集として。| 
|\[4.5.4][7] プッシュ通知は、アプリが機能するために必要であってはならず、機密性の高い個人情報や機密情報を送信するために使用してはならない。プッシュ通知は、プロモーションや直接マーケティングのために使用してはいけません。ただし、顧客がアプリのUIに表示された同意言語で受信することを明示的に選択し、ユーザーがそのようなメッセージを受信しないようにするためのメソッドをアプリに提供している場合は除きます。|
|[4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) プッシュ通知、カメラ、ジャイロスコープなどのハードウェアまたはオペレーティングシステムが提供する組み込み機能、またはApple Music アクセス、iCloud ストレージ、スクリーンタイムAPI などのApple サービスおよびテクノロジーを収益化できません。|
{: .reset-td-br-1 .reset-td-br-2}

|Google Playストアポリシー|
|---|
|\[システム機能の不正な使用または模倣][10] 通知やワーニングなどのシステム機能を模倣したり妨害したりするアプリsや広告を許可しません。システムレベルの通知は、ユーザーに特殊な取引を通知する航空会社のアプリや、ゲーム内のプロモーションをユーザーに通知するゲームなど、アプリの不可欠な機能にのみ使用できます。|
{: .reset-td-br-1}

[1]: {% image_buster /assets/img/red-dress.gif %}
[2]: {% image_buster /assets/img/ios_push.png %}
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content
[8]: https://www.braze.com/customers
[7]: https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services
[9]: https://developer.apple.com/app-store/review/guidelines/#unacceptable
[10]: https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories
[23]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
