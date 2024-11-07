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

# [![Braze ラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer){: style="float:right;width:120px;border:0;" class="noimgborder"}はじめに：プラットフォームの概要

> この記事では、Brazeプラットフォームの基本的なパーツと機能について説明する。この記事からのリンクは、Brazeの重要なトピックにつながっている。

## Brazeとは？

Braze はカスタマーエンゲージメントプラットフォームです。これは簡単に言えば、Brazeがユーザーの声に耳を傾け、ユーザーの行動や振る舞いを理解し、それに基づいて行動する手助けをするということだ。Braze プラットフォームには、SDK、ダッシュボード、REST API の3つの主要コンポーネントがあります。

Brazeのより一般的な概要を知りたいマーケティング担当者は、代わりに[マーケティング担当者向けの「Getting Started」セクションを]({{site.baseurl}}/user_guide/getting_started/overview/)チェックしよう。

![Braze にはさまざまなレイヤーがあります。全体として、SDK、API、ダッシュボード、およびパートナー連携から構成されています。これらはそれぞれ、データ取り込みレイヤー、分類レイヤー、オーケストレーションレイヤー、パーソナライゼーションレイヤー、アクションレイヤーの一部を担っています。アクションレイヤーには、プッシュ、アプリ内メッセージ、コネクテッドカタログ、Webhook、SMS、メールなど、さまざまなチャネルがあります。][17]{: style="max-width:55%;float:right;margin-left:15px;"}

### SDK

[Braze SDK](#integrating-braze) をモバイルアプリケーションおよび Web アプリケーションに統合して、強力なマーケティング、ユーザー管理、および分析ツールを提供できます。

つまり、完全に統合されると、SDK は次を行います。

* ユーザーデータを収集し、統合されたユーザープロファイルに同期する。
* セッションデータ、デバイス情報、プッシュトークンを自動的に収集する
* マーケティング・エンゲージメント・データとお客様のビジネスに特化したカスタム・データを取得する
* サードパーティによってセキュリティと侵入のテストが行われるように設計されている
* 低バッテリーや低速ネットワークのデバイスに最適化されている
* セキュリティを強化するため、サーバー側のJWT署名をサポートする。
* システムへの書き込み専用アクセス権を持つ (ユーザーデータを取得できない)
* プッシュ通知、アプリ内メッセージ、コンテンツカードのメッセージングチャネルを強化する

### ダッシュボードのユーザー・インターフェース

ダッシュボードは、Brazeプラットフォームの中心にあるすべてのデータとインタラクションを制御するUIである。マーケティング担当者はダッシュボードを使って仕事をし、コンテンツを作成する。開発者はダッシュボードを使い、APIキーやプッシュ通知の認証情報など、アプリを統合するための設定を管理する。

始めたばかりの場合は、チーム管理者が[ダッシュボードで][1]あなた（およびBrazeへのアクセスが必要な他のチームメンバー全員）を[ユーザーとして][1]追加する必要がある。

### REST API

Braze API を使えば、Braze からデータを大規模に出し入れすることができます。API を使用して、バックエンド、データウェアハウス、その他のファーストパーティソースおよびサードパーティソースから更新を取り込みます。さらに、APIを使って、ウェブベースのアプリケーションから直接、セグメンテーション目的のカスタムイベントを追加することもできる。APIを通じてメッセージをトリガーしたり送信したりできるので、テクニカル・リソースはキャンペーンの一部として複雑なJSONメタデータを含めることができる。

また、この API は、モバイルおよび Web SDK 経由ではなく、HTTP 経由で直接ユーザーが実行したアクションを記録できる Web サービスも提供します。webhook と組み合わせることで、アプリ体験の内外でユーザーのアクションを追跡し、アクティビティをトリガーできます。[APIガイドには][2]、利用可能なBraze APIエンドポイントとその用途が記載されている。

Braze の構成要素については、以下を確認してください。[はじめに: アーキテクチャの概要]({{site.baseurl}}/developer_guide/platform_wide/getting_started/architecture_overview).

## データ分析と行動

Braze に保存されたデータは、Braze の顧客である限り保持され、セグメンテーション、パーソナライゼーション、およびターゲティングのために保持され、使用できます。これにより、その情報を非推奨にすることを選択するまで、ユーザープロファイルデータ (たとえば、セッションアクティビティや購入) に対して操作を行うことができます。例えば、ストリーミングサービスは、各サブスクライバーがサービス利用開始日から (それが何年も前であっても) 視聴したコンテンツを追跡し、そのデータを使用して関連するメッセージングを強化できます。

![Brazeのダッシュボードにある「最近の購入者」というセグメントと、「リンダへの一番のおすすめ」というメールが表示された電話画面が隣り合わせになっている。][3]{: style="max-width:80%"}

### アプリ分析

Brazeのダッシュボードは、多くの分析指標やアプリケーションで設定したカスタムイベントに基づいてリアルタイムで更新されるグラフを表示する。AB テスト、カスタムレポートおよび分析、自動化されたインテリジェンスを使用してキャンペーンを一貫して測定および最適化することで、顧客のエンゲージメントを維持し、競合他社に差をつけることができます。

### ユーザー・セグメンテーション

セグメンテーションを利用することで、アプリ内での行動やユーザー層データなどの強力なフィルターに基づいて、ユーザーのグループを作成することができます。また、Brazeでは、希望するアクションがデフォルトでキャプチャされない場合、任意のアプリ内ユーザーアクションを「カスタムイベント」として定義することができる。同じことが、"カスタム属性 "によるユーザー特性にも当てはまる。ダッシュボード上でユーザーセグメントが作成されると、ユーザーは定義された基準を満たす（または満たさない）ごとにセグメントを出たり入ったりする。例えば、アプリ内でお金を使い、最後にアプリを使ったのが2週間以上前であるすべてのユーザーを含むセグメントを作成することができる。

データモデルについては、こちらをご覧いただきたい：[はじめに: 分析の概要]({{site.baseurl}}/developer_guide/platform_wide/getting_started/architecture_overview)。

## マルチチャンネル・メッセージング

セグメントを定義した後、Brazeのメッセージングツールを使えば、ダイナミックでパーソナライズされた方法でユーザーに働きかけることができる。Brazeはチャネルにとらわれないユーザー中心のデータモデルで設計されている。メッセージングは、アプリやサイトの内部（アプリ内メッセージの送信や、コンテンツカードのカルーセルやバナーなどのグラフィック要素）で行われることもあれば、アプリの外部（プッシュ通知やEメールの送信など）で行われることもある。例えば、マーケティング担当者は、前のセクションで定義した例のセグメントにプッシュ通知とEメールを送ることができる。

![アプリやウェブサイトの外でも内でも、あらゆるチャネルでパーソナライズされたメッセージを作成し、トリガーする。][18]{: style="border:none" }

| Channel                                                                                              | 説明                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [コンテンツカード]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) | 顧客の作業を中断することなく、高度にターゲットを絞った動的なアプリ内通知を送信します。 |
| [メールアドレス]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/) | リッチテキストエディタ、ドラッグ＆ドロップエディタ、または既存のHTMLテンプレートをアップロードしてメールを作成し、リッチなHTMLメッセージを送信。 |
| [アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) | Braze が独自に構築したネイティブユーザーインターフェイスを使用して、控えめなアプリ内通知を送信します。 |
| [プッシュ]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/) | iOS 用の Apple Push Notification Service (APNs) または Android 用のFirebase Cloud Messaging (FCM) を使用して、メッセージングキャンペーンまたはニュースアイテムから自動的にプッシュ通知をトリガーします。 |
| [SMS/MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/about_sms/) | SMS/MMS を使用して、トランザクション通知、プロモーションの共有、リマインダーの送信などを行います。 |
| [Web プッシュ]({{site.baseurl}}/user_guide/message_building_by_channel/push/web) | ユーザーが現在サイトでアクティブでない場合でも、Web ブラウザー通知を送信します。 |
| [Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) | Webhookを使ってアプリ以外のアクションをトリガーし、他のシステムやアプリケーションにリアルタイムデータを提供する。 |
| [WhatsApp*]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) | 広く普及しているピアツーピアメッセージングプラットフォームを活用して、ユーザーや顧客と直接つながります。WhatsApp。 |
{: .reset-td-br-1 .reset-td-br-2}

<sup>\*\*アドオン機能として利用できます。*</sup>

### カスタマイズ可能なコンポーネント

{% gallery %}
{{site.baseurl}}/assets/img/getting-started/crawl-example.png <br> すべての Braze コンポーネントは、アクセシブルで、適応性があり、カスタマイズできるように作られています。Braze を使い始めるには、デフォルトの `BrazeUI` コンポーネントを使用し、ブランドのニーズやユースケースに合わせてカスタマイズします。
{{site.baseurl}}/assets/img/getting-started/walk-example.png <br> デフォルトのオプションを超えるために、カスタムコードを書いて、メッセージチャンネルのルック＆フィールをよりブランドに近いものに更新することができる。これには、コンポーネントのフォントタイプ、フォントサイズ、色の変更も含まれます。マーケティング担当者は、Brazeのダッシュボードで直接、オーディエンス、コンテンツ、クリック行動、有効期限をコントロールできる。
{{site.baseurl}}/assets/img/getting-started/run-example.png <br> また、完全にカスタムのコンポーネントを作成して、メッセージングの外観、動作、および他のメッセージングチャネルとの連携方法 (プッシュ通知に基づいてコンテンツカードをトリガーするなど) をコントロールすることもできます。Braze には SDK メソッドが用意されており、Braze ダッシュボードでのインプレッション数、クリック数、閉じた回数などのメトリクスを記録できます。各メッセージングチャネルには、これを容易にするための分析記事があります。
{% endgallery %}

<br>
<br>
メッセージングチャネルのカスタマイズの詳細については、以下を参照してください： [はじめにカスタマイズの概要]({{site.baseurl}}/developer_guide/customization_guides/customization_overview).

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
[![Android]({% image_buster /assets/img/braze_icons/android.svg %})]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) |[![Swift]({% image_buster /assets/img/braze_icons/apple.svg %})]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview/){: style="max-width:20%;margin-right:15px;border:0" class="noimgborder"} [Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview/) |[![ウェブ]({% image_buster /assets/img/braze_icons/globe-02.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/){: style="max-width:25%;margin-right:15px;border:0" class="noimgborder"} [ウェブ]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)  

すべての統合   |    |   
----------- |---------------- | --------------------
[![Cordova Android]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/android/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova Android]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/android/) | [![Cordova iOS]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/ios/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/ios/) | [![Flutter Android and iOS]({% image_buster /assets/img/flutter_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/flutter/flutter_sdk_integration/){: style="max-width:20%;margin-top:5%;border:0" class="noimgborder"}  [Flutter Android and iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/flutter/flutter_sdk_integration/)
[![React Native]({% image_buster /assets/img/reactnative_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/) | [![tvOS]({% image_buster /assets/img/tvos_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/tvos/initial_sdk_setup/){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [tvOS]({{site.baseurl}}/developer_guide/platform_integration_guides/tvos/initial_sdk_setup/) | [![MacOS]({% image_buster /assets/img/macOS_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/macOS/initial_sdk_setup/){: style="max-width:40%;margin-top:15%;border:0" class="noimgborder"}  [MacOS]({{site.baseurl}}/developer_guide/platform_integration_guides/macOS/initial_sdk_setup/)
[![Unity Android]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/android/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [ユニティ アンドロイド]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/android/) | [![Unity iOS]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [ユニティ iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/) | [![Xamarin]({% image_buster /assets/img/xamarin.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/){: style="max-width:35%;margin-top:5%;border:0" class="noimgborder"}  [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/)
[![Roku]({% image_buster /assets/img/roku.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/) | [![Unreal Engine]({% image_buster /assets/img/unreal.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unreal_engine/initial_sdk_setup/){: style="max-width:30%;margin-right:15px;border:0" class="noimgborder"}  [Unreal Engine]({{site.baseurl}}/developer_guide/platform_integration_guides/unreal_engine/initial_sdk_setup/)

## ブックマークすべきリソース

テクニカル・リソースとして、Brazeの肝心な部分の多くに携わることになる。ドキュメント以外でブックマークしておくとよいリソースを以下に紹介します。今後、Brazeの用語について質問がある場合は、[用語]({{site.baseurl}}/user_guide/getting_started/terms_to_know/)集を手元に置いておくとよい。

| リソース | 学べる内容|
|---|---|
| [Braze Public GitHub](https://github.com/braze-inc/) | 統合に関する詳細な情報とサンプルコードについては、GitHub リポジトリを参照してください。 |
| [Android SDK GitHubリポジトリ](https://github.com/braze-inc/braze-android-sdk/) | Android SDKのGitHubリポジトリ。 |
| [Android SDK リファレンス](https://appboy.github.io/appboy-android-sdk/kdoc/index.html) | Android SDKのクラス・ドキュメント。 |
| [iOS（Swift）SDKのGitHubリポジトリ](https://github.com/braze-inc/braze-swift-sdk) | Swift SDKのGitHubリポジトリ。 |
| [iOS (Swift) SDK リファレンス](https://braze-inc.github.io/braze-swift-sdk/) | iOS SDKのクラス・ドキュメント。 |
| [ウェブSDK GitHubリポジトリ](https://github.com/braze-inc/braze-web-sdk) | Web SDKのGitHubリポジトリ。 |
| [Web SDK リファレンス](https://js.appboycdn.com/web-sdk/5.0/doc/modules/braze.html) | iOS SDKのクラス・ドキュメント。 |
| [SDK 変更ログ]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs) | Braze は、重要な問題や主要な OS 更新のリリースに加えて、予測可能な毎月のリリースを提供しています。 |
| [Braze API Postman Collection](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest) | Postman collection はこちらからダウンロードできます。  |
| [Braze System Status Monitor](https://braze.statuspage.io/) | 私たちのステータス・ページは、事故や障害が発生するたびに更新される。アラートをサブスクライブするには、このページに移動します。 |
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
