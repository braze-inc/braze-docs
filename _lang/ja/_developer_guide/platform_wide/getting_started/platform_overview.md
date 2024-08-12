---
nav_title: プラットフォームの概要
article_title: プラットフォームの概要
page_order: 1
description: "この記事では、 Braze プラットフォームの基本的な部品と機能について説明します。この記事からのリンクは、必須の Braze ・トピックに接続します。"
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

# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/path/developer){: style="float:right;width:120px;border:0;" class="noimgborder"}はじめに:プラットフォームの概要

> この記事では、 Braze プラットフォームの基本的な部品と機能について説明します。この記事からのリンクは、必須の Braze ・トピックに接続します。

## Brazeとは？

 Braze は顧客エンゲージメントプラットフォームです。つまり、Brazeはユーザーの話を聞き、ユーザーの行動や行動を理解し、それに基づいて行動するのに役立ちます。Braze プラットフォームには、SDK、ダッシュボード、およびREST API の3 つの主要コンポーネントがあります。

マーケターがBrazeのより一般的な概要を探している場合は、代わりにマーケターの[Getting Started section]({{site.baseurl}}/user_guide/getting_started/overview/)をチェックしてください。

![ろう付けはレイヤーが異なります。合計では、SDK、API、ダッシュボード、およびパートナー統合で構成されます。これらはそれぞれ、データ取り込みレイヤー、分類レイヤー、オーケストレーションレイヤー、パーソナライゼーションレイヤー、およびアクションレイヤーの一部を提供します。アクションレイヤには、プッシュ、アプリ内メッセージ、接続カタログ、Webhook、SMS、メールなど、さまざまなチャネルがあります。[17]{: style="max-width:55%;float:right;margin-left:15px;"}

### SDK

[Braze SDKs](#integrating-braze) をモバイルアプリケーションとWeb アプリケーションに統合して、強力なマーケティング、ユーザー管理、分析ツールを提供できます。

簡単に説明すると、完全に統合された場合、SDK は次のようになります。

* \* ユーザーデータを収集し、統合されたユーザープロファイルに同期します
* \* セッションデータ、デバイス情報、プッシュトークンを自動的に収集する
* \* マーケティングエンゲージメントデータとビジネスに固有のカスタムデータを取得します
* 第三者によってテストされたセキュリティと浸透のために設計されているか
* 低バッテリーまたは低速ネットワークデバイス用に最適化されています
* サーバ側のJWT シグネチャをサポートし、セキュリティを強化
* システムへの書き込み専用アクセスがある(ユーザーデータを取得できない)
* \* プッシュ通知、アプリ内メッセージ、コンテンツカード メッセージング チャネルを強化します

### ダッシュボードのユーザーインタフェース

ダッシュボードは、Braze プラットフォームの中心にあるすべてのデータとインタラクションを制御するUI です。マーケティング担当者は、ダッシュボードを使用して自分の仕事を行い、コンテンツを作成します。開発者はダッシュボードを使用して、API キーやプッシュ通知の認証情報など、アプリケーションを統合するための設定を管理します。

開始したばかりの場合、チーム管理者は、ダッシュボード で[users として、Braze にアクセスする必要がある他のすべてのチームメンバーを追加する必要があります。

### REST API

Braze API を使用すると、データをスケールでBraze の内外に移動できます。API を使用して、バックエンド、データウェアハウス、その他の第一および第三者のソースから更新を取り込みます。さらに、API を使用して、ウェブベースのアプリケーションから直接セグメンテーション目的のカスタムイベントを追加します。API を介してメッセージをトリガーおよび送信することができ、テクニカルリソースがキャンペーンの一部として複雑なJSON メタデータを含めることができます。

また、API は、モバイルおよびWeb SDK ではなく、HTTP 経由で直接ユーザが実行したアクションを記録できるWeb サービスも提供します。これは、Webhook と組み合わせて、アクションを追跡し、アプリエクスペリエンス内外のユーザーのアクティビティをトリガーできることを意味します。[API ガイド][2] には、使用可能なBraze API エンドポイントとその使用方法がリストされています。

 Braze の部品や部品の詳細については、こちらをご覧ください。[はじめに: アーキテクチャ概要]({{site.baseurl}}/developer_guide/platform_wide/getting_started/architecture_overview)。

## データ分析とアクション

Brazeに保存されたデータは、Brazeの顧客である限り、セグメンテーション、パーソナライズ、ターゲティングに使用できます。これにより、その情報を非推奨にすることを選択するまで、ユーザープロファイルデータ(セッションアクティビティや購入など) を操作することができます。たとえば、ストリーミングサービスは、サービスの最初の日から各サブスクライバの表示されたコンテンツを追跡し(それが何年も前であったとしても)、そのデータを使用して関連するメッセージングを強化することができます。

![Braze ダッシュボードの「&quot」と呼ばれるセグメント;最近の購入者とクォート; &quot を表示する電話画面の横に並べて表示;Linda&quot の上位推奨; email.][3]{: style="max-width:80%"}

### アプリケーションアナリティクス

Braze ダッシュボードには、アプリケーションで計測するカスタムイベントだけでなく、多数の分析メトリクスに基づいてリアルタイムで更新されるグラフが表示されます。A/Bテスト、カスタムレポートと分析、自動インテリジェンスを使用してキャンペーンを一貫して測定および最適化することで、お客様があなたのスペースで競合他社との関係を維持し、際立たせます。

### ユーザセグメンテーション

セグメンテーションを使用すると、アプリ内の動作、人口統計データなどの強力なフィルタに基づいてユーザーのグループを作成できます。Braze では、アプリ内ユーザアクションを"custom event&quot として定義することもできます。必要なアクションがデフォルトでキャプチャされていない場合です。同じことが、"custom attributes.&quot を介したユーザー特性にも当てはまります。 ユーザーセグメントがダッシュボードに作成されると、ユーザーは定義された基準を満たす(または満たさない)ときにセグメントの内外に移動します。たとえば、アプリ内でお金を使い、2週間以上前にアプリを最後に使用したすべてのユーザーを含むセグメントを作成できます。

データモデルの詳細については、以下を参照してください。[はじめに: Analytics の概要]({{site.baseurl}}/developer_guide/platform_wide/getting_started/architecture_overview)。

## マルチチャネルメッセージング

セグメントを定義した後、Braze メッセージングツールを使用すると、ダイナミックでパーソナライズされた方法でユーザーを操作できます。ろう付けは、チャネルに依存しない、ユーザ中心のデータモデルを用いて設計した。メッセージングは、アプリまたはサイト内(アプリ内メッセージの送信、コンテンツカードのカローセルやバナーなどのグラフィックエレメント)、またはアプリの外部(プッシュ通知やメールの送信など)で行われます。たとえば、マーケターは、前のセクションで定義したサンプルセグメントにプッシュ通知とメールを送信できます。

![アプリまたはウェブサイトの外部または内部を問わず、任意のチャネルでパーソナライズされたメッセージを作成し、トリガーします。][18]{: style="border:none" }

| チャネル                                                                                              | 説明                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [コンテンツカード]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)\* | 顧客を中断することなく、高度なターゲットとダイナミックなアプリ内通知を送信します。|
| [メール]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/) | リッチテキストエディタ、ドラッグアンドドロップエディタ、または既存のHTML テンプレートのいずれかをアップロードしてメールを作成し、リッチHTML メッセージを送信します。|
| [アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) | Braze カスタムビルドのネイティブユーザーインターフェイスを使用して、目立たないアプリ内通知を送信します。|
| [プッシュ]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/) | iOS用Appleプッシュ通知サービス(APNs)またはAndroid用Firebase Cloud Messaging(FCM)を使用して、メッセージングキャンペーンまたはニュースアイテムから自動的にプッシュ通知をトリガします。|
| [SMS/MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/about_sms/)\* | SMS/MMSを使用して、トランザクション通知の送信、プロモーションの共有、リマインダーの送信などを行います。|
| [Web プッシュ]({{site.baseurl}}/user_guide/message_building_by_channel/push/web) | ユーザが現在サイトでアクティブでない場合でも、Web ブラウザ通知を送信します。|
| [Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) | webhooks を使用してアプリ以外のアクションをトリガし、他のシステムやアプリケーションにリアルタイムデータを提供します。|
| [WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/)\* | 人気のピアツーピア・メッセージング・プラットフォームを活用して、ユーザーや顧客と直接接続します。WhatsApp
{: .reset-td-br-1 .reset-td-br-2}

<sup>\*\*アドオン機能として利用できます。*</sup>

### カスタマイズ可能なコンポーネント

{% gallery %}
{{site.baseurl}}/assets/img/getting-started/crawl-example.png <br> すべての Braze コンポーネントは、アクセシブルで、適応性があり、カスタマイズできるように作られています。デフォルトの`BrazeUI` コンポーネントを使用し、ブランドのニーズとユースケースに合わせてカスタマイズすることで、Braze から始めることができます。
{{site.baseurl}}/assets/img/getting-started/walk-example.png <br> デフォルトのオプションを超えるために、カスタムコードを記述して、メッセージチャネルのルックとフィーリングを更新し、ブランドにもっと密接に一致させることができます。これには、コンポーネントのフォントタイプ、フォントサイズ、および色の変更が含まれます。マーケターは、Braze のダッシュボードで直接、オーディエンス、コンテンツ、クリック動作、有効期限をコントロールできます。
{{site.baseurl}}/assets/img/getting-started/run-example.png <br> また、完全なカスタムコンポーネントを作成して、メッセージングの外観、動作、および他のメッセージングチャネルとのやり取りを制御することもできます(たとえば、プッシュ通知に基づいてコンテンツカードをトリガーするなど)。Braze には、Braze ダッシュボードのインプレッション、クリック、および削除などのメトリクスをログに記録するための SDK メソッドが用意されています。各メッセージングチャネルには、これを容易にするための分析記事があります。
{% endgallery %}

<br>
<br>
メッセージングチャネルのカスタマイズの詳細については、以下を参照してください。[はじめに: カスタマイズの概要]({{site.baseurl}}/developer_guide/customization_guides/customization_overview)。

## Braze を統合する

Braze は、迅速かつ簡単に稼働できるように設計されています。数百のブランドの顧客ベース全体で、当社の平均タイムトゥーバリューは6週間です。統合プロセスの詳細については、以下を参照してください。[はじめに: 統合の概要]({{site.baseurl}}/developer_guide/platform_wide/getting_started/integration_overview/)。

さまざまな SDK  Braze ・オファーを探索します。

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
注目の統合 | |   
----------- |---------------- | --------------------
[![Android]({% image_buster /assets/img/android.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) |[<i class="fa-brands fa-apple" style="font-size:60px;vertical-align: middle;"></i>]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview/){: style="max-width:30%;margin-right:15px;border:0"} [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview/) | [<i class="fas fa-globe" style="font-size:60px;vertical-align: middle;"></i>]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/){: style="max-width:30%;margin-right:15px;border:0"} [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)  

すべての統合 | |   
----------- |---------------- | --------------------
[![Cordova Android]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/android/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova Android]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/android/) | [![Cordova iOS]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/ios/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/ios/) | [![Flutter Android and iOS]({% image_buster /assets/img/flutter_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/flutter/flutter_sdk_integration/){: style="max-width:20%;margin-top:5%;border:0" class="noimgborder"}  [Flutter Android および iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/flutter/flutter_sdk_integration/)
[![React Native]({% image_buster /assets/img/reactnative_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/) | [![tvOS]({% image_buster /assets/img/tvos_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/tvos/initial_sdk_setup/){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [tvOS]({{site.baseurl}}/developer_guide/platform_integration_guides/tvos/initial_sdk_setup/) | [![MacOS]({% image_buster /assets/img/macOS_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/macOS/initial_sdk_setup/){: style="max-width:40%;margin-top:15%;border:0" class="noimgborder"}  [MacOS]({{site.baseurl}}/developer_guide/platform_integration_guides/macOS/initial_sdk_setup/)
[![Unity Android]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/android/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Unity Android]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/android/) | [![Unity iOS]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Unity iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/) | [![Xamarin]({% image_buster /assets/img/xamarin.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/){: style="max-width:35%;margin-top:5%;border:0" class="noimgborder"}  [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/)
[![Roku]({% image_buster /assets/img/roku.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/) | [![Unreal Engine]({% image_buster /assets/img/unreal.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unreal_engine/initial_sdk_setup/){: style="max-width:30%;margin-right:15px;border:0" class="noimgborder"}  [Unreal Engine]({{site.baseurl}}/developer_guide/platform_integration_guides/unreal_engine/initial_sdk_setup/)

## ブックマークへのリソース

技術的なリソースとして、あなたはBrazeの多くのナットとボルトに関わるでしょう。ここでは、ドキュメントの外側にブックマークするのに適したリソースを示します。今後も、[ 知っておくべき用語]({{site.baseurl}}/user_guide/getting_started/terms_to_know/) 用語集は、Braze の用語に関する質問がある場合に便利です。

| Resource | What You'll Learn|
|---|---|
| [Braze Public GitHub](https://github.com/braze-inc/) | GitHub リポジトリに詳細な統合情報とサンプルコードがあります。|
| [Android SDK GitHub リポジトリ](https://github.com/braze-inc/braze-android-sdk/)| Android SDK GitHub リポジトリ|
| [Android SDK Reference](https://appboy.github.io/appboy-android-sdk/kdoc/index.html) | Android SDK のクラスドキュメント。|
| [iOS (Swift) SDK GitHub リポジトリ](https://github.com/braze-inc/braze-swift-sdk) | Swift SDK GitHub リポジトリ。|
| [iOS (Swift) SDK リファレンス](https://braze-inc.github.io/braze-swift-sdk/) | iOS SDK のクラスドキュメント。|
| [Web SDK GitHub リポジトリ](https://github.com/braze-inc/braze-web-sdk)| Web SDK GitHub リポジトリ|
| [Web SDK Reference](https://js.appboycdn.com/web-sdk/5.0/doc/modules/braze.html) | iOS SDK のクラスドキュメント|
| [SDK Changelogs]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs) | Braze は、重要な問題および主要なOS アップデートのリリースに加えて、予測可能な月次リリースを持っています。|
| [Braze API Postman Collection](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest) | Postman コレクションをダウンロードします。|
| [Braze System Status Monitor](https://braze.statuspage.io/) | インシデントまたは停止が発生するたびに、ステータスページが更新されます。このページに移動してアラートをサブスクライブします。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}


[1]: {{site.baseurl}}/user_guide/administrative/access_braze
[2]: {{site.baseurl}}/api/home
[3]: {% image_buster /assets/img/getting-started/getting-started-segment.png %}
[4]: {{site.baseurl}}/developer_guide/customization_guides/content_cards
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/push
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/email
[7]:{{site.baseurl}}/user_guide/message_building_by_channel/sms
[8]: {% image_buster /assets/img_archive/UOiOSPush.png %} Example;プッシュダッシュボードとクォート;
[9]: {% image_buster /assets/img_archive/In-App_Modal.png %} "スライドアップの例とクォート;
[10]: {% image_buster /assets/img_archive/EmailTemplateEditor.png %} "メールテンプレートエディタとクォート;
[11]: {{site.baseurl}}/user_guide/message_building_by_channel/whatsapp
[12]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks
[13]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/
[14]: {% image_buster /assets/img_archive/Webhook_Body_Edit.png %}
[15]: {% image_buster /assets/img/whatsapp/whatsapp8.png %}
[16]: {{site.baseurl}}/developer_guide/home
[17]: {% image_buster /assets/img/getting-started/getting-started-vertically-integrated-stack.png %}
[18]: {% image_buster /assets/img/getting-started/messaging-channels.png %}
