---
nav_title: プラットフォームの概要
article_title: プラットフォームの概要
page_order: 1
description: "この記事では、Brazeプラットフォームの基本的なパーツと機能について説明する。この記事からのリンクは、Brazeの重要なトピックにつながっている。"
platform:
  - iOS
  - Android
  - Web
  - React Native
  - Flutter
  - Cordova
  - Roku
  - Swift
  - Unity
---

# [![Braze Learningコース]](https://learning.braze.com/path/developer)([{% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer){: style="float:right;width:120px;border:0;" class="noimgborder"}はじめに：プラットフォームの概要

> この記事では、Brazeプラットフォームの基本的なパーツと機能について説明する。この記事からのリンクは、Brazeの重要なトピックにつながっている。

## Brazeとは？

Brazeは顧客エンゲージメント・プラットフォームである。これは簡単に言えば、Brazeがユーザーの声に耳を傾け、ユーザーの行動や振る舞いを理解し、それに基づいて行動する手助けをするということだ。Brazeプラットフォームには、SDK、ダッシュボード、REST APIの3つの主要コンポーネントがある。

Brazeのより一般的な概要を知りたいマーケティング担当者は、代わりに[マーケティング担当者向けの「Getting Started」セクションを]({{site.baseurl}}/user_guide/getting_started/overview/)チェックしよう。

![ブレイズにはさまざまな層がある。SDK、API、ダッシュボード、パートナーとの統合で構成されている。これらはそれぞれ、データ取り込みレイヤー、分類レイヤー、オーケストレーションレイヤー、パーソナライゼーションレイヤー、アクションレイヤーの一部を担っている。アクション・レイヤーには、プッシュ、アプリ内メッセージ、コネクテッド・カタログ、ウェブフック、SMS、Eメールなど、さまざまなチャンネルがある。][17]{: style="max-width:55%;float:right;margin-left:15px;"}

### SDK

[BrazeのSDKを](#integrating-braze)モバイルやウェブアプリケーションに統合することで、強力なマーケティング、ユーザー管理、分析ツールを提供することができる。

簡単に言えば、SDKは完全に統合されている：

* ユーザーデータを収集し、統合されたユーザープロファイルに同期する。
* セッションデータ、デバイス情報、プッシュトークンを自動的に収集する
* マーケティング・エンゲージメント・データとお客様のビジネスに特化したカスタム・データを取得する
* セキュリティのために設計され、第三者によって侵入テストが行われている。
* 低バッテリーや低速ネットワークのデバイスに最適化されている
* セキュリティを強化するため、サーバー側のJWT署名をサポートする。
* システムへの書き込み専用アクセス権を持つ（ユーザーデータを取得できない）
* プッシュ通知、アプリ内メッセージ、コンテンツカードのメッセージングチャネルを強化する

### ダッシュボードのユーザー・インターフェース

ダッシュボードは、Brazeプラットフォームの中心にあるすべてのデータとインタラクションを制御するUIである。マーケティング担当者はダッシュボードを使って仕事をし、コンテンツを作成する。開発者はダッシュボードを使い、APIキーやプッシュ通知の認証情報など、アプリを統合するための設定を管理する。

始めたばかりの場合は、チーム管理者が[ダッシュボードで][1]あなた（およびBrazeへのアクセスが必要な他のチームメンバー全員）を[ユーザーとして][1]追加する必要がある。

### REST API

BrazeのAPIを使えば、Brazeからデータを大規模に出し入れすることができる。APIを使用して、バックエンド、データウェアハウス、その他の第一およびサードパーティのソースから更新を取り込む。さらに、APIを使って、ウェブベースのアプリケーションから直接、セグメンテーション目的のカスタムイベントを追加することもできる。APIを通じてメッセージをトリガーしたり送信したりできるので、テクニカル・リソースはキャンペーンの一部として複雑なJSONメタデータを含めることができる。

また、このAPIはウェブサービスも提供しており、モバイルSDKやウェブSDKを介さず、HTTP経由で直接ユーザーのアクションを記録することができる。ウェブフックと組み合わせることで、アプリ体験の内外でユーザーのアクションを追跡し、アクティビティをトリガーすることができる。[APIガイドには][2]、利用可能なBraze APIエンドポイントとその用途が記載されている。

ブレイズの部品やパーツについては、こちらをチェックしてほしい：[はじめに: アーキテクチャの概要]({{site.baseurl}}/developer_guide/platform_wide/getting_started/architecture_overview).

## データ分析と行動

Brazeに保存されたデータは、Brazeの顧客である限り保持され、セグメンテーション、パーソナライゼーション、ターゲティングに使用できる。これにより、あなたがその情報を非推奨にすることを選択するまで、ユーザー・プロファイル・データ（例えば、セッションのアクティビティや購入など）を利用することができる。例えば、ストリーミング・サービスは、各加入者のサービス開始初日から（たとえそれが何年も前のことであっても）視聴したコンテンツを追跡し、そのデータを使って関連するメッセージングを行うことができる。

![Brazeのダッシュボードにある「最近の購入者」というセグメントと、「リンダへの一番のおすすめ」というメールが表示された電話画面が隣り合わせになっている。][3]{: style="max-width:80%"}

### アプリ分析

Brazeのダッシュボードは、多くの分析指標やアプリケーションで設定したカスタムイベントに基づいてリアルタイムで更新されるグラフを表示する。A/Bテスト、カスタムレポート、アナリティクス、自動化されたインテリジェンスにより、キャンペーンを一貫して測定・最適化することで、顧客の関心を維持し、競合他社に差をつけることができる。

### ユーザー・セグメンテーション

セグメンテーションによって、アプリ内での行動や人口統計データなどの強力なフィルターに基づいて、ユーザーのグループを作成することができる。また、Brazeでは、希望するアクションがデフォルトでキャプチャされない場合、任意のアプリ内ユーザーアクションを「カスタムイベント」として定義することができる。同じことが、"カスタム属性 "によるユーザー特性にも当てはまる。ダッシュボード上でユーザーセグメントが作成されると、ユーザーは定義された基準を満たす（または満たさない）ごとにセグメントを出たり入ったりする。例えば、アプリ内でお金を使い、最後にアプリを使ったのが2週間以上前であるすべてのユーザーを含むセグメントを作成することができる。

データモデルについては、こちらをご覧いただきたい：[はじめに: 分析概要]({{site.baseurl}}/developer_guide/platform_wide/getting_started/architecture_overview).

## マルチチャンネル・メッセージング

セグメントを定義した後、Brazeのメッセージングツールを使えば、ダイナミックでパーソナライズされた方法でユーザーに働きかけることができる。Brazeはチャネルにとらわれないユーザー中心のデータモデルで設計されている。メッセージングは、アプリやサイトの内部（アプリ内メッセージの送信や、コンテンツカードのカルーセルやバナーなどのグラフィック要素）で行われることもあれば、アプリの外部（プッシュ通知やEメールの送信など）で行われることもある。例えば、マーケティング担当者は、前のセクションで定義した例のセグメントにプッシュ通知とEメールを送ることができる。

![アプリやウェブサイトの外でも内でも、あらゆるチャネルでパーソナライズされたメッセージを作成し、トリガーする。][18]{: style="border:none" }

| Channel                                                                                              | 説明                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [コンテンツ・カード]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) | 顧客を中断させることなく、高度にターゲット化された動的なアプリ内通知を送信する。 |
| [メールアドレス]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/) | リッチテキストエディタ、ドラッグ＆ドロップエディタ、または既存のHTMLテンプレートをアップロードしてメールを作成し、リッチなHTMLメッセージを送信。 |
| [アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) | Braze特注のネイティブユーザーインターフェースを使用して、控えめなアプリ内通知を送信。 |
| [プッシュ]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/) | iOS用のApple Push Notification Service (APNs)またはAndroid用のFirebase Cloud Messaging (FCM)を使用して、メッセージングキャンペーンやニュースアイテムから自動的にプッシュ通知をトリガーする。 |
| [SMS/MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/about_sms/) | SMS/MMSを使用して、取引通知、プロモーションの共有、リマインダーの送信などを行う。 |
| [Web プッシュ]({{site.baseurl}}/user_guide/message_building_by_channel/push/web) | ユーザーがサイトにアクセスしていなくても、ウェブブラウザーに通知を送る。 |
| [Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) | Webhookを使ってアプリ以外のアクションをトリガーし、他のシステムやアプリケーションにリアルタイムデータを提供する。 |
| [WhatsApp*]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) | 人気のピアツーピア・メッセージング・プラットフォームを活用して、ユーザーや顧客と直接つながる：WhatsAppだ。 |
{: .reset-td-br-1 .reset-td-br-2}

<sup>\*\*アドオン機能として利用できます。*</sup>

### カスタマイズ可能なコンポーネント

{% gallery %}
{{site.baseurl}}/assets/img/getting-started/crawl-example.png<br> すべての Braze コンポーネントは、アクセシブルで、適応性があり、カスタマイズできるように作られています。Brazeを使い始めるには、デフォルトの`BrazeUI` コンポーネントを使用し、ブランドのニーズやユースケースに合わせてカスタマイズする。
{{site.baseurl}}/assets/img/getting-started/walk-example.png<br> デフォルトのオプションを超えるために、カスタムコードを書いて、メッセージチャンネルのルック＆フィールをよりブランドに近いものに更新することができる。これには、コンポーネントのフォント・タイプ、フォント・サイズ、色の変更も含まれる。マーケティング担当者は、Brazeのダッシュボードで直接、オーディエンス、コンテンツ、クリック行動、有効期限をコントロールできる。
{{site.baseurl}}/assets/img/getting-started/run-example.png<br> また、完全にカスタム化したコンポーネントを作成し、メッセージングがどのように見えるか、どのように動作するか、他のメッセージング・チャンネルとどのように相互作用するかをコントロールすることもできる（例えば、プッシュ通知に基づいてコンテンツ・カードをトリガーするなど）。BrazeはSDKメソッドを提供し、Brazeダッシュボードでインプレッション、クリック、退会などの指標を記録できるようにする。各メッセージングチャネルには、これを容易にするための分析記事があります。
{% endgallery %}

<br>
<br>
メッセージング・チャンネルのカスタマイズについては、以下を参照のこと：[始める：カスタマイズの概要]({{site.baseurl}}/developer_guide/customization_guides/customization_overview).

## Braze を統合する

Braze は、迅速かつ簡単に稼働できるように設計されています。数百のブランドの顧客ベース全体で、当社の平均タイムトゥーバリューは6週間です。統合プロセスの詳細については、こちらをご覧いただきたい：[はじめに: 統合の概要]({{site.baseurl}}/developer_guide/platform_wide/getting_started/integration_overview/)。

Brazeが提供するさまざまなSDKを探そう：

<style>
table th:nth-child(1) {
width: 33%;
}
table th:nth-child(2) {
width: 33%;
}
table th:nth-child(3) {
width: 33%;
}
table td {
word-break: break-word;
text-align: center;
}
</style>
注目の統合   |    |   
----------- |---------------- | --------------------
[![アンドロイド]({% image_buster /assets/img/braze_icons/android.svg %})]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [アンドロイド]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) |[![スウィフト]({% image_buster /assets/img/braze_icons/apple.svg %})]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview/){: style="max-width:20%;margin-right:15px;border:0" class="noimgborder"} [スウィフト]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview/) |[![ウェブ]({% image_buster /assets/img/braze_icons/globe-02.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/){: style="max-width:25%;margin-right:15px;border:0" class="noimgborder"} [ウェブ]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)  

すべての統合   |    |   
----------- |---------------- | --------------------
[![Cordova Android]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/android/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [コルドバ・アンドロイド]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/android/) | [![Cordova iOS]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/ios/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [コルドバiOS]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/ios/) | [![Flutter Android and iOS]({% image_buster /assets/img/flutter_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/flutter/flutter_sdk_integration/){: style="max-width:20%;margin-top:5%;border:0" class="noimgborder"}  [Flutter アンドロイドとiOS]({{site.baseurl}}/developer_guide/platform_integration_guides/flutter/flutter_sdk_integration/)
[![リアクト・ネイティブ]({% image_buster /assets/img/reactnative_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [リアクト・ネイティブ]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/) | [![tvOS]({% image_buster /assets/img/tvos_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/tvos/initial_sdk_setup/){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [tvOS]({{site.baseurl}}/developer_guide/platform_integration_guides/tvos/initial_sdk_setup/) | [![MacOS]({% image_buster /assets/img/macOS_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/macOS/initial_sdk_setup/){: style="max-width:40%;margin-top:15%;border:0" class="noimgborder"}  [マックOS]({{site.baseurl}}/developer_guide/platform_integration_guides/macOS/initial_sdk_setup/)
[![Unity Android]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/android/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [ユニティ アンドロイド]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/android/) | [![Unity iOS]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [ユニティ iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/) | [![Xamarin]({% image_buster /assets/img/xamarin.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/){: style="max-width:35%;margin-top:5%;border:0" class="noimgborder"}  [ザマリン]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/)
[![Roku]({% image_buster /assets/img/roku.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [ロク]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/) | [![アンリアル・エンジン]({% image_buster /assets/img/unreal.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unreal_engine/initial_sdk_setup/){: style="max-width:30%;margin-right:15px;border:0" class="noimgborder"}  [アンリアルエンジン]({{site.baseurl}}/developer_guide/platform_integration_guides/unreal_engine/initial_sdk_setup/)

## ブックマークすべきリソース

テクニカル・リソースとして、Brazeの肝心な部分の多くに携わることになる。我々のドキュメント以外でブックマークしておくと良いリソースを紹介しよう。今後、Brazeの用語について質問がある場合は、[用語]({{site.baseurl}}/user_guide/getting_started/terms_to_know/)集を手元に置いておくとよい。

| リソース | 何を学ぶか|
|---|---|
| [BrazeパブリックGitHub](https://github.com/braze-inc/) | 詳細な統合情報とサンプルコードはGitHubリポジトリにある。 |
| [Android SDK GitHubリポジトリ](https://github.com/braze-inc/braze-android-sdk/) | Android SDKのGitHubリポジトリ。 |
| [Android SDKリファレンス](https://appboy.github.io/appboy-android-sdk/kdoc/index.html) | Android SDKのクラス・ドキュメント。 |
| [iOS（Swift）SDKのGitHubリポジトリ](https://github.com/braze-inc/braze-swift-sdk) | Swift SDKのGitHubリポジトリ。 |
| [iOS（Swift）SDKリファレンス](https://braze-inc.github.io/braze-swift-sdk/) | iOS SDKのクラス・ドキュメント。 |
| [ウェブSDK GitHubリポジトリ](https://github.com/braze-inc/braze-web-sdk) | Web SDKのGitHubリポジトリ。 |
| [Web SDKリファレンス](https://js.appboycdn.com/web-sdk/5.0/doc/modules/braze.html) | iOS SDKのクラス・ドキュメント。 |
| [SDK 変更ログ]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs) | Brazeは、クリティカルな問題やOSのメジャーアップデートのためのリリースに加えて、予測可能な毎月のリリースがある。 |
| [ブレイズAPI ポストマン・コレクション](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest) | ポストマン・コレクションはこちらからダウンロードできる。  |
| [ブレイズシステムステータスモニター](https://braze.statuspage.io/) | 私たちのステータス・ページは、事故や障害が発生するたびに更新される。このページでアラートを購読する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}


[1]: {{site.baseurl}}/user_guide/administrative/access_braze
[2]: {{site.baseurl}}/api/home
[3]: {% image_buster /assets/img/getting-started/getting-started-segment.png %}
[4]: {{site.baseurl}}/developer_guide/customization_guides/content_cards
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/push
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/email
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/sms
[8]: {% image_buster /assets/img_archive/UOiOSPush.png %} 「プッシュ・ダッシュボードの例
[9]: {% image_buster /assets/img_archive/In-App_Modal.png %} 「スライドアップの例
[10]: {% image_buster /assets/img_archive/EmailTemplateEditor.png %} 「メールテンプレートエディター
[11]: {{site.baseurl}}/user_guide/message_building_by_channel/whatsapp
[12]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks
[13]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/
[14]: {% image_buster /assets/img_archive/Webhook_Body_Edit.png %}
[15]: {% image_buster /assets/img/whatsapp/whatsapp8.png %}
[16]: {{site.baseurl}}/developer_guide/home
[17]: {% image_buster /assets/img/getting-started/getting-started-vertically-integrated-stack.png %}
[18]: {% image_buster /assets/img/getting-started/messaging-channels.png %}
