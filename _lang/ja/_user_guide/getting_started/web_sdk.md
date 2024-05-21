---
nav_title: SDK の概要 
article_title: SDK の概要 
page_order: 9
page_type: reference
description: "この参考記事では Braze SDK の基本情報について説明します。"
---

# SDK の概要 

> Braze SDK を使用すると、Web サイトやアプリを通じてセッション データの収集、ユーザーの識別、購入やカスタムイベントの記録が簡単になります。SDK を使用して、アプリ内メッセージやプッシュ通知を Braze ダッシュボードから直接送信することでユーザーとやり取りすることもできます。

Braze SDK を簡単に説明すると、次のとおりです。
\* ユーザーデータを収集し、統合されたユーザープロファイルに同期します
\* マーケティングエンゲージメントデータとビジネスに固有のカスタムデータを取得します
\* プッシュ通知、アプリ内メッセージ、コンテンツカード メッセージング チャネルを強化します

## SDK とは何ですか?
ソフトウェア開発キット (SDK) は、新しい機能をサポートするためにデジタルアプリケーションに追加できる、既成のツール (小さなコードのブロック) のセットです。Braze SDK は、アプリまたはサイトとの間で情報を送受信するために使用されます。ユーザープロファイルの作成、カスタムイベントのログ記録、プッシュ通知のトリガーなど、最初から重要な機能を提供するように設計されています。 

この機能は Braze ではデフォルトで提供されるため、開発者はコアビジネスに専念できます。SDK がなければ、すべての Braze クライアントは、データ処理、セグメンテーションロジック、配​​信オプション、匿名ユーザーの処理、キャンペーン分析などのためのすべてのインフラストラクチャとツールを完全にゼロから作成する必要があります。これは、SDK を組み込むために1時間ほど要するよりも、はるかに時間がかかり、はるかに面倒です。

## 実装

SDK をアプリまたはサイトに組み込むには、そのアプリケーションを動作させる、より大きなコードベース全体に SDK のコードを追加する必要があります。これは、お客様のエンジニアリングチームが関与し、本質的にアプリを結び付けて、情報とアクションがアプリ間で流れるようにすることを意味します。ただし、開発者が関与しているにもかかわらず、SDK は軽量でユーザーフレンドリーに統合できるように設計されています。 

時間を節約し、スムーズな統合を実現するために、お客様とエンジニアリングチームがカスタムイベント、カスタム属性、SDK を同時に設定することをお勧めします。マーケティングチームとエンジニアリングチームが一緒に検討する必要があるステップについて詳しくは、[実装に関する記事][4]をご覧ください。 

## データの集約

Braze SDK はユーザーレベルで膨大な量のデータを自動的にキャプチャし、アプリとユーザーベースの主要な指標を簡単に確認できるようにします。類似したアプリをダッシュ​​ボード上の1つのワークスペースにグループ化します。たとえば、アプリの iOS バージョンと Android バージョンを同じワークスペースにグループ化すると、両方のプラットフォームのユーザーから収集されたデータを確認できるようになります。これにより、Web チャネルとモバイルチャネル全体でユーザーをより完全に把握できるようになります。詳細については、[ホームページ][3]の記事を参照してください。

## アプリ内メッセージング

SDK を使用すると、アプリ内メッセージを簡単に作成して送信し、ユーザーと直接やり取りすることができます。キャンペーン戦略に基づいて、スライドアップ、モーダル、または全画面メッセージの送信を選択できます。アプリ内メッセージの作成の詳細については、[アプリ内メッセージの作成][8] に関するページを参照してください。

![Web ブラウザー上でプッシュ通知が表示される][11]{: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## プッシュ通知

プッシュ通知は、ユーザーと関わるためのもう1つの優れたオプションであり、時間的制約のある行動喚起を処理する場合に特に便利です。モバイルプッシュ通知はユーザーのデバイスに表示され、Web プッシュ通知はサイトが開いていないときでも表示されます。プッシュ通知の使用方法の詳細については、[プッシュ通知の記事][5]を参照してください。

Web サイトまたはアプリのユーザーは、プッシュ通知を受け取るようにオプトインする必要があります。詳細については、[プッシュプライミング][13] を参照してください。 

## セグメンテーションと配信ルール

デフォルトでは、アプリ内メッセージを含むキャンペーンは、そのワークスペース内のアプリのすべてのバージョンに送信されます。たとえば、メッセージは Web ユーザーとモバイルユーザーの両方に送信されます。アプリ内メッセージを Web またはモバイルのみに送信するには、それに応じてキャンペーンをセグメント化する必要があります。これは Braze SDK を通じてデフォルトでサポートされています。 

セグメントの **[使用するアプリ]** セクションで Web サイトのアプリアイコンのみを選択することで、Web ユーザーのセグメントを作成できます。

![Web アプリが選択されたセグメントの詳細ページ][10]

これにより、インテリジェントな方法でユーザーの行動に基づいてユーザーをターゲットにすることができます。Web ユーザーをターゲットにしてモバイルアプリのダウンロードを奨励したい場合は、このセグメントをターゲットユーザーとして作成します。Web メッセージではなくモバイルアプリ内メッセージを含むメッセージングキャンペーンを送信したい場合は、セグメント内の Web サイトのアイコンのチェックを外します。

## Braze にはどのような統合がありますか?
Braze は、多くのプラットフォーム (Web、Android、iOS、Flutter、React Native など) 向けに SDK のバージョンを提供していますが、それらはすべて基本的に同じように動作します。したがって、たとえば「Web SDK」という記述があれば、それは単に Web サイト用の Braze SDK のバージョンです。

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

[3]: {{site.baseurl}}/user_guide/data_and_analytics/your_analytics_dashboards/understanding_your_app_usage_data/
[4]: {{site.baseurl}}/user_guide/onboarding_with_braze/integration/#the-technical-side-of-the-integration-process
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/push/about/
[7]: {% image_buster /assets/img_archive/app_group_list.png %}
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[10]: {% image_buster /assets/img_archive/web-users-segment.png %}
[11]: {% image_buster /assets/img_archive/web_push_macbook.png %}
[13]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/
