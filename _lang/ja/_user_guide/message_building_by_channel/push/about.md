---
nav_title: "プッシュ通知について"
article_title: プッシュ通知について
page_order: 0
page_type: reference
description: "このリファレンス記事では、プッシュの概要を説明し、プッシュメッセージの使用を開始するためのリソースを提供し、いくつかの規制について説明します。"
channel:
  - Push

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/messaging-channels-push){: style="float:right;width:120px;border:0;" class="noimgborder"}プッシュ通知について

> プッシュ通知は、時間的制約のある行動喚起や、しばらくアプリにアクセスしていないユーザーに再度アプローチするのに最適です。プッシュキャンペーンが成功すると、ユーザーはコンテンツに直接誘導され、アプリケーションの価値が実証されます。

ユーザーがメッセージを受信するにはプッシュをオプトインする必要があるため、アプリ内メッセージを使用して、プッシュ通知を送信する理由と、プッシュを有効にすることでどのようなメリットがあるかを顧客に説明することをお勧めします。このプロセスは [プッシュプライミング]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/create_push_primer/)と呼ばれます。

![Apple製品全体のプッシュメッセージの例][1]{: height="400px"}  ![iPhoneのホーム画面のストップウォッチからのプッシュメッセージの例:こんにちはこれはiOSプッシュです。[2]{: height="400px"}

プッシュ通知のその他の例については、[ケーススタディ][8]をご覧ください。

## 想定されるユースケース

プッシュ通知は、新規ユーザーを引き付け、リエンゲージメントキャンペーンを行うための優れたツールです。ここでは、一般的なプッシュメッセージの使用例をいくつか紹介します。

|ユースケース |解説 |
| -------- | ----------- |
|初期オンボーディング |ユーザーがアプリを使用するための最初の手順 (アカウントの登録など) を実行するまで、その価値は大幅に制限されます。プッシュ通知を使用して、ユーザーがアプリを完全に使い始めることができるように、これらの手順を完了するように促します。|
|初回購入 |ユーザーがアプリを使いこなせるようになったら、プッシュ通知を使ってアプリをアプリ内購入に変えることができます。|
|新機能 |プッシュ通知は、離脱したユーザーに、アプリに呼び戻す可能性のある新機能について通知するのに効果的です。 |
|時間的制約のあるオファー |オファーの時計が刻々と進んでいる場合、有効期限が切れる前にユーザーに知らせるには、プッシュが最適な方法である場合があります。これらのメッセージは一般的に緊急性が高く、最近休眠したユーザーにアプリを思い出させるのに最適です。<br><br> たとえば、アプリがゲームであり、ユーザーが毎日ゲームを連続してプレイしている場合に、ゲーム内通貨ボーナスを提供するとします。そのストリークが破られる危険性があることをユーザーに警告することは、特定の日数を超えた場合に合理的なプッシュになる可能性があります。|
{: .reset-td-br-1 .reset-td-br-2}

休眠ユーザーの再エンゲージの詳細については、このトピックの [クイックウィン][23] ページを参照してください。

## プッシュを使用するための前提条件

Brazeを使用してプッシュメッセージを作成して送信する前に、開発者と協力してプッシュをWebサイトまたはアプリに統合する必要があります。詳細な手順については、各プラットフォームの統合ガイドを参照してください。

- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/)

## プッシュメッセージ規制

プッシュメッセージは、顧客の携帯電話やブラウザに直接送信される煩わしいタイプのメッセージであるため、アプリやサイトを介してプッシュメッセージを送信するためのガイドラインがあります。

### アプリのモバイルプッシュ規制

{% alert important %}
プッシュメッセージは、Apple App StoreおよびGoogleのPlayストアポリシーのガイドライン(特に、プッシュメッセージを広告、スパム、プロモーションなどとして使用することに関するガイドライン)に準拠している必要があります。
{% endalert %}

|Apple App Storeポリシー|
|---|
|[4.5.4][7] プッシュ通知は、アプリが機能するために必要であってはならず、広告、プロモーション、ダイレクトマーケティングの目的で使用したり、機密性の高い個人情報や機密情報を送信したりしないでください。
|[3.2.2][9] (i) App Storeに類似した、または一般的なコレクションとして、サードパーティのアプリ、拡張機能、またはプラグインを表示するためのインターフェイスを作成すること。(ii)プッシュ通知、カメラ、ジャイロスコープなど、ハードウェアまたはオペレーティングシステムによって提供される組み込み機能を収益化すること。またはAppleのサービス(Apple MusicアクセスやiCloudストレージなど)|
{: .reset-td-br-1 .reset-td-br-2}

|Google Play ストア ポリシー|
|---|
|[システム機能の不正使用または模倣][10] 通知や警告など、システムの機能を模倣したり妨害したりするアプリや広告は許可されません。システムレベルの通知は、ユーザーに特別セールを通知する航空会社アプリや、ゲーム内プロモーションをユーザーに通知するゲームなど、アプリの不可欠な機能にのみ使用できます。|
{: .reset-td-br-1}

[1]: {% image_buster /assets/img/red-dress.gif %}
[2]: {% image_buster /assets/img/ios_push.png %}
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content
[8]: https://www.braze.com/customers
[7]: https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services
[9]: https://developer.apple.com/app-store/review/guidelines/#unacceptable
[10]: https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories
[23]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
