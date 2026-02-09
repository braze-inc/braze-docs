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

# [![Braze ラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer){: style="float:right;width:120px;border:0;" class="noimgborder"} はじめに：プラットフォームの概要

> この記事では、Brazeプラットフォームの基本的なパーツと機能について説明する。この記事からのリンクは、Brazeの重要なトピックにつながっている。 

{% alert tip %}
これらの記事とともに、無料の[開発者学習パス](https://learning.braze.com/path/developer)コースをチェックしよう。
{% endalert %}

## Brazeとは？

Braze はカスタマーエンゲージメントプラットフォームです。ユーザーデータを取り込み、ユーザーのアクションや行動を表面化し、それに基づいて行動できるようにする。プラットフォームには、SDK、ダッシュボード、REST APIの3つの主要コンポーネントがある。

Brazeのより一般的な概要を知りたいマーケティング担当者は、代わりに[マーケティング担当者向けの「Getting Started」セクションを]({{site.baseurl}}/user_guide/getting_started/overview/)チェックしよう。

![Braze にはさまざまなレイヤーがあります。全体として、SDK、API、ダッシュボード、およびパートナー連携から構成されています。これらはそれぞれ、データインジェストレイヤー、分類レイヤー、オーケストレーションレイヤー、パーソナライゼーションレイヤー、およびアクションレイヤーの一部を構成します。アクションレイヤーには、プッシュ、アプリ内メッセージ、コネクテッドカタログ、Webhook、SMS、メールなど、さまざまなチャネルがあります。]({% image_buster /assets/img/getting-started/getting-started-vertically-integrated-stack.png %}){: style="max-width:55%;float:right;margin-left:15px;"}

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

始めたばかりの場合は、チーム管理者がダッシュボードであなた（およびBrazeへのアクセスが必要な他のチームメンバー全員）を[ユーザーとして]({{site.baseurl}}/user_guide/administrative/access_braze)追加する必要がある。

### REST API

Braze API を使えば、Braze からデータを大規模に出し入れすることができます。API を使用して、バックエンド、データウェアハウス、その他のファーストパーティソースおよびサードパーティソースから更新を取り込みます。さらに、APIを使って、ウェブベースのアプリケーションから直接、セグメンテーション目的のカスタムイベントを追加することもできる。APIを通じてメッセージをトリガーしたり送信したりできるので、テクニカル・リソースはキャンペーンの一部として複雑なJSONメタデータを含めることができる。

また、この API は、モバイルおよび Web SDK 経由ではなく、HTTP 経由で直接ユーザーが実行したアクションを記録できる Web サービスも提供します。webhook と組み合わせることで、アプリ体験の内外でユーザーのアクションを追跡し、アクティビティをトリガーできます。[APIガイドには]({{site.baseurl}}/api/home)、利用可能なBraze APIエンドポイントとその用途が記載されている。

Braze の構成要素については、以下を確認してください。[はじめに: アーキテクチャの概要]({{site.baseurl}}/developer_guide/getting_started/architecture_overview/).

## データ分析と行動

Braze に保存されたデータは、Braze の顧客である限り保持され、セグメンテーション、パーソナライゼーション、およびターゲティングのために保持され、使用できます。これにより、その情報を非推奨にすることを選択するまで、ユーザープロファイルデータ (たとえば、セッションアクティビティや購入) に対して操作を行うことができます。例えば、ストリーミングサービスは、各サブスクライバーがサービス利用開始日から (それが何年も前であっても) 視聴したコンテンツを追跡し、そのデータを使用して関連するメッセージングを強化できます。

![Brazeのダッシュボードにある「最近の購入者」というセグメントと、「リンダへの一番のおすすめ」というメールが表示された電話画面が隣り合わせになっている。]({% image_buster /assets/img/getting-started/getting-started-segment.png %}){: style="max-width:80%"}

### アプリ分析

Brazeのダッシュボードには、分析指標やあなたが設定したカスタムイベントに基づいてリアルタイムで更新されるグラフが表示される。ABテスト、カスタムレポート、分析、自動インテリジェンスを使用した一貫した測定と最適化は、カスタマーエンゲージメントと差別化をサポートする。

### ユーザー・セグメンテーション

セグメンテーションを利用することで、アプリ内での行動やユーザー層データなどの強力なフィルターに基づいて、ユーザーのグループを作成することができます。また、Brazeでは、希望するアクションがデフォルトでキャプチャされない場合、任意のアプリ内ユーザーアクションを「カスタムイベント」として定義することができる。同じことが、"カスタム属性 "によるユーザー特性にも当てはまる。ダッシュボード上でユーザーセグメントが作成されると、ユーザーは定義された基準を満たす（または満たさない）ごとにセグメントを出たり入ったりする。例えば、アプリ内でお金を使い、最後にアプリを使ったのが2週間以上前であるすべてのユーザーを含むセグメントを作成することができる。

データモデルについては、こちらをご覧いただきたい：[はじめに: 分析の概要]({{site.baseurl}}/developer_guide/getting_started/architecture_overview/)。

## マルチチャンネル・メッセージング

セグメントを定義した後、Brazeのメッセージングツールを使えば、ダイナミックでパーソナライズされた方法でユーザーに働きかけることができる。Brazeはチャネルにとらわれないユーザー中心のデータモデルで設計されている。メッセージングは、アプリやサイトの内部（アプリ内メッセージの送信や、コンテンツカードのカルーセルやバナーなどのグラフィック要素）で行われることもあれば、アプリの外部（プッシュ通知やEメールの送信など）で行われることもある。例えば、マーケティング担当者は、前のセクションで定義した例のセグメントにプッシュ通知とEメールを送ることができる。

![アプリやウェブサイトの外でも内でも、あらゆるチャネルでパーソナライズされたメッセージを作成し、トリガーする。]({% image_buster /assets/img/getting-started/messaging-channels.png %}){: style="border:none" }

| Channel                                                                                              | 説明                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [コンテンツカード]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) | 顧客の作業を中断することなく、高度にターゲットを絞った動的なアプリ内通知を送信します。 |
| [メールアドレス]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/) | リッチテキストエディタ、ドラッグ＆ドロップエディタ、または既存のHTMLテンプレートをアップロードしてメールを作成し、リッチなHTMLメッセージを送信。 |
| [アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) | Braze が独自に構築したネイティブユーザーインターフェイスを使用して、控えめなアプリ内通知を送信します。 |
| [プッシュ]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/) | iOS 用の Apple Push Notification Service (APNs) または Android 用のFirebase Cloud Messaging (FCM) を使用して、メッセージングキャンペーンまたはニュースアイテムから自動的にプッシュ通知をトリガーします。 |
| [SMS、MMS、および RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs)* | SMS、MMS、またはRCSを使用して、取引通知、プロモーションの共有、リマインダーの送信などを行う。 |
| [Web プッシュ]({{site.baseurl}}/user_guide/message_building_by_channel/push/web) | ユーザーが現在サイトでアクティブでない場合でも、Web ブラウザー通知を送信します。 |
| [Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) | Webhookを使ってアプリ以外のアクションをトリガーし、他のシステムやアプリケーションにリアルタイムデータを提供する。 |
| [WhatsApp*]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) | 広く普及しているピアツーピアメッセージングプラットフォームを活用して、ユーザーや顧客と直接つながります。WhatsApp。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<sup>\*\*アドオン機能として利用できます。*</sup>

### カスタマイズ可能なコンポーネント

{% gallery %}
{{site.baseurl}}/assets/img/getting-started/crawl-example.png<br> すべての Braze コンポーネントは、アクセシブルで、適応性があり、カスタマイズできるように作られています。Braze を使い始めるには、デフォルトの `BrazeUI` コンポーネントを使用し、ブランドのニーズやユースケースに合わせてカスタマイズします。
{{site.baseurl}}/assets/img/getting-started/walk-example.png<br> デフォルトのオプションを超えるために、カスタムコードを書いて、メッセージチャンネルのルック＆フィールをよりブランドに近いものに更新することができる。これには、コンポーネントのフォントタイプ、フォントサイズ、色の変更も含まれます。マーケティング担当者は、Brazeのダッシュボードで直接、オーディエンス、コンテンツ、クリック行動、有効期限をコントロールできる。
{{site.baseurl}}/assets/img/getting-started/run-example.png<br> また、完全にカスタムのコンポーネントを作成して、メッセージングの外観、動作、および他のメッセージングチャネルとの連携方法 (プッシュ通知に基づいてコンテンツカードをトリガーするなど) をコントロールすることもできます。Braze には SDK メソッドが用意されており、Braze ダッシュボードでのインプレッション数、クリック数、閉じた回数などのメトリクスを記録できます。各メッセージングチャネルには、これを容易にするための分析記事があります。
{% endgallery %}

<br>
<br>

## Braze を統合する

Brazeは迅速に統合できるように設計されている。顧客ベースでは平均6週間である。統合プロセスの詳細については、[はじめにを参照のこと：統合の概要]({{site.baseurl}}/developer_guide/getting_started/integration_overview/)。

## ブックマークすべきリソース

テクニカル・リソースとして、Brazeの肝心な部分の多くに携わることになる。ドキュメント以外でブックマークしておくとよいリソースを以下に紹介します。今後、Brazeの用語について質問がある場合は、[用語]({{site.baseurl}}/user_guide/getting_started/terms_to_know/)集を手元に置いておくとよい。

| リソース | 学べる内容|
|---|---|
| [SDKをデバッグする]({{site.baseurl}}/developer_guide/sdk_integration/debugging) | 統合をトラブルシューティングする際には、SDK デバッグツールが役に立ちます。必ず手元に置いておきましょう。 |
| [Braze Public GitHub](https://github.com/braze-inc/) | 統合に関する詳細な情報とサンプルコードについては、GitHub リポジトリを参照してください。 |
| [Android SDK GitHubリポジトリ](https://github.com/braze-inc/braze-android-sdk/) | Android SDKのGitHubリポジトリ。 |
| [Android SDK リファレンス](https://appboy.github.io/appboy-android-sdk/kdoc/index.html) | Android SDKのクラス・ドキュメント。 |
| [iOS（Swift）SDKのGitHubリポジトリ](https://github.com/braze-inc/braze-swift-sdk) | Swift SDKのGitHubリポジトリ。 |
| [iOS (Swift) SDK リファレンス](https://braze-inc.github.io/braze-swift-sdk/) | iOS SDKのクラス・ドキュメント。 |
| [ウェブSDK GitHubリポジトリ](https://github.com/braze-inc/braze-web-sdk) | Web SDKのGitHubリポジトリ。 |
| [Web SDK リファレンス](https://js.appboycdn.com/web-sdk/5.0/doc/modules/braze.html) | iOS SDKのクラス・ドキュメント。 |
| [SDK 変更ログ]({{site.baseurl}}/developer_guide/changelogs) | Braze は、重要な問題や主要な OS 更新のリリースに加えて、予測可能な毎月のリリースを提供しています。 |
| [Braze API Postman Collection](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest) | Postman collection はこちらからダウンロードできます。  |
| [Braze System Status Monitor](https://braze.statuspage.io/) | 私たちのステータス・ページは、事故や障害が発生するたびに更新される。アラートをサブスクライブするには、このページに移動します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

