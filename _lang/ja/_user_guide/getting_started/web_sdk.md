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
* ユーザーデータを収集し、統合されたユーザープロファイルに同期する。
* マーケティング・エンゲージメント・データとお客様のビジネスに特化したカスタム・データを取得する
* プッシュ通知、アプリ内メッセージ、コンテンツカードのメッセージングチャネルを強化する

## SDK とは何ですか?
ソフトウェア開発キット (SDK) は、新しい機能をサポートするためにデジタルアプリケーションに追加できる、既成のツール (小さなコードのブロック) のセットです。Braze SDK は、アプリまたはサイトとの間で情報を送受信するために使用されます。ユーザープロファイルの作成、カスタムイベントのログ記録、プッシュ通知のトリガーなど、最初から重要な機能を提供するように設計されています。 

この機能は Braze ではデフォルトで提供されるため、開発者はコアビジネスに専念できます。SDK がなければ、すべての Braze クライアントは、データ処理、セグメンテーションロジック、配​​信オプション、匿名ユーザーの処理、キャンペーン分析などのためのすべてのインフラストラクチャとツールを完全にゼロから作成する必要があります。これは、SDK を組み込むために1時間ほど要するよりも、はるかに時間がかかり、はるかに面倒です。

## 実装

SDK をアプリまたはサイトに組み込むには、そのアプリケーションを動作させる、より大きなコードベース全体に SDK のコードを追加する必要があります。これは、お客様のエンジニアリングチームが関与し、本質的にアプリを結び付けて、情報とアクションがアプリ間で流れるようにすることを意味します。ただし、開発者が関与しているにもかかわらず、SDK は軽量でユーザーフレンドリーに統合できるように設計されています。 

時間を節約し、スムーズな統合を実現するために、お客様とエンジニアリングチームがカスタムイベント、カスタム属性、SDK を同時に設定することをお勧めします。マーケティングチームとエンジニアリングチームが一緒に検討する必要があるステップについて詳しくは、[実装に関する記事]({{site.baseurl}}/user_guide/getting_started/integration/)をご覧ください。 

## データの集約

Braze SDK はユーザーレベルで膨大な量のデータを自動的にキャプチャし、アプリとユーザーベースの主要な指標を簡単に確認できるようにします。類似したアプリをダッシュ​​ボード上の1つのワークスペースにグループ化します。たとえば、アプリの iOS バージョンと Android バージョンを同じワークスペースにグループ化すると、両方のプラットフォームのユーザーから収集されたデータを確認できるようになります。これにより、Web チャネルとモバイルチャネル全体でユーザーをより完全に把握できるようになります。詳細については、[ホームページ]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/)の記事を参照してください。

## アプリ内メッセージング

SDK を使用すると、アプリ内メッセージを簡単に作成して送信し、ユーザーと直接やり取りすることができます。キャンペーン戦略に基づいて、スライドアップ、モーダル、または全画面メッセージの送信を選択できます。アプリ内メッセージの作成の詳細については、[アプリ内メッセージの作成]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/)に関するページを参照してください。

![Web ブラウザーに表示されるプッシュ]({% image_buster /assets/img_archive/web_push_macbook.png %}){: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## プッシュ通知

プッシュ通知は、ユーザーと関わるためのもう1つの優れたオプションであり、時間的制約のある行動喚起を処理する場合に特に便利です。モバイルプッシュ通知はユーザーのデバイスに表示され、Web プッシュ通知はサイトが開いていないときでも表示されます。プッシュ通知の使用方法の詳細については、[プッシュ通知の記事]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)を参照してください。

Web サイトまたはアプリのユーザーは、プッシュ通知を受け取るようにオプトインする必要があります。詳細については、[プッシュプライミング]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)を参照してください。 

## セグメンテーションと配信ルール

デフォルトでは、アプリ内メッセージを含むキャンペーンは、そのワークスペース内のアプリのすべてのバージョンに送信されます。たとえば、メッセージは Web ユーザーとモバイルユーザーの両方に送信されます。アプリ内メッセージを Web またはモバイルのみに送信するには、それに応じてキャンペーンをセグメント化する必要があります。これは Braze SDK を通じてデフォルトでサポートされています。 

**特定のアプリからのユーザー**を**ターゲットにしたアプリと Web サイト**を設定して Ｗｅｂ ユーザーのセグメントを作成し、**特定のアプリ**の Web サイトのみを選択できます。

![Web アプリが強調表示されている [セグメントの詳細]ページ]({% image_buster /assets/img_archive/web-users-segment.png %}){:style="max-width:60%"}

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
注目の統合   |    |   
----------- |---------------- | --------------------
[![Android]({% image_buster /assets/img/braze_icons/android.svg %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) |[![iOS]({% image_buster /assets/img/braze_icons/apple.svg %})]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift){: style="max-width:20%;margin-right:15px;border:0" class="noimgborder"} [iOS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) |[![ウェブ]({% image_buster /assets/img/braze_icons/globe-02.png %})]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web){: style="max-width:25%;margin-right:15px;border:0" class="noimgborder"} [ウェブ]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)  

すべての統合   |    |   
----------- |---------------- | --------------------
[![Cordova Android]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=android){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=android) | [![Cordova iOS]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=ios){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=ios) | [![Flutter の Android および iOS]({% image_buster /assets/img/flutter_icon.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=flutter){: style="max-width:20%;margin-top:5%;border:0" class="noimgborder"}  [Flutter の Android および iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=flutter)
[![React Native]({% image_buster /assets/img/reactnative_icon.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [React Native]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native) | [![tvOS]({% image_buster /assets/img/tvos_icon.png %})]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/tvos/initial_sdk_setup/){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [tvOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/tvos/initial_sdk_setup/) | [![MacOS]({% image_buster /assets/img/macOS_icon.png %})]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/macOS/initial_sdk_setup/){: style="max-width:40%;margin-top:15%;border:0" class="noimgborder"}  [MacOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/macOS/initial_sdk_setup/)
[![Unity Android]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [ユニティ アンドロイド]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity) | [![Unity iOS]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [ユニティ iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity) | [![Xamarin]({% image_buster /assets/img/xamarin.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=xamarin){: style="max-width:35%;margin-top:5%;border:0" class="noimgborder"}  [Xamarin]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=xamarin) 
[![Roku]({% image_buster /assets/img/roku.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=roku){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [Roku]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=roku) | [![Unreal Engine]({% image_buster /assets/img/unreal.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unreal%20engine){: style="max-width:30%;margin-right:15px;border:0" class="noimgborder"}  [Unreal Engine]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unreal%20engine)

