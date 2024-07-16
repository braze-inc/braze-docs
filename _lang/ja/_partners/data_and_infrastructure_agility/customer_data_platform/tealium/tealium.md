---
nav_title: Tealium
article_title:Tealium
page_order:1
alias: /partners/tealium/
description:「この参考記事では、BrazeとTealiumのパートナーシップについて概説しています。Tealiumは、モバイル、ウェブ、代替データを他のサードパーティソースに接続できるようにするユニバーサルデータハブです。「
page_type: partner
search_tag:Partner

---

# Tealium

> [Tealiumは](https://tealium.com/)、EventStream、AudienceStream、iQ Tag Managementで構成されるユニバーサルデータハブおよび顧客データプラットフォームであり、サードパーティのソースからのモバイル、ウェブ、および代替データを接続できます。TealiumをBrazeに接続することで、カスタムイベント、ユーザー属性、購入のデータフローが可能になり、データに基づいてリアルタイムで行動できるようになります。

![Tealiumの概要図は、さまざまなTealium製品とBrazeプラットフォームがどのように連携して、クロスチャネルのキャンペーンをリアルタイムでアクティブ化するかを示しています。][22]{: style="border:0;"}

BrazeとTealiumの統合により、ユーザーを追跡し、データをさまざまなユーザー分析プロバイダーに転送できます。Tealiumでは以下のことが可能になります。
- [TealiumオーディエンスをAudienceStreamとBrazeに同期して]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_audience_stream/)、Brazeのキャンペーンやキャンバスをパーソナライズしたり、セグメントを構築したりすることができます。
- [プラットフォーム間でデータをインポートします](#choose-your-integration-type)。Brazeは、Android、iOS、[ウェブアプリケーション用のサイドバイサイドSDK統合と](#side-by-side-sdk-integration)、イベントデータをレポート[できるあらゆるプラットフォームで使用できるサーバー間統合の両方を提供します](#server-to-server-integration)。<br><br>

{% tabs %}
{% tab EventStream %}
Tealium イベントストリームは、データの中心に位置するデータ収集およびAPIハブです。EventStreamは、セットアップからインストールから、受信したユーザーデータの特定、検証、強化まで、データサプライチェーン全体を処理します。EventStreamは、イベントフィードとコネクタを使用してリアルタイムでアクションを実行します。[イベントストリームを構成する機能は次のとおりです](https://docs.tealium.com/server-side/getting-started/eventstream-api-hub/introduction/)。
- データソース (インストールとデータ収集)
- ライブイベント (リアルタイムデータ検査)
- イベントの仕様と属性 (データレイヤーの要件と検証)
- イベントフィード (フィルターされたイベントタイプ)
- イベントコネクタ (API ハブアクション)

{% endtab %}
{% tab AudienceStream %}

Tealium AudienceStreamは、オムニチャネルの顧客セグメンテーションおよびリアルタイムアクションエンジンです。AudienceStreamは、イベントストリームに流入するデータを取り込み、顧客と貴社のブランドとのエンゲージメント最も重要な属性を表す訪問者プロファイルを作成します。設定手順については、[AudienceStreamの記事を参照してください]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_audience_stream/)。

{% endtab %}
{% tab iQ Tag Management %}
Tealium iQでは、Tealium iQタグ管理UIのタグを使用してアプリ内のコードトリガーすることができます。このタグは、モバイルプラットフォームやウェブプラットフォームからイベントデータを収集、コントロール、配信するため、アプリにBraze固有のコードを追加することなく、ネイティブのBraze実装を構成できます。ユーザーは、iQ Tag ManagementまたはJSON設定ファイル（Tealiumの推奨アプローチ）を使用してモバイルリモートコマンドを統合することを選択できます。Braze Web SDK を使用するユーザーは、Web iQ タグを使用して統合する必要があります。

それぞれの方法の長所と短所について詳しくは、[以下のTealium iQタグマネージャーのセクションを参照してください](#mobile-remote-commands)。
{% endtab %}
{% endtabs %}

{% alert important %}
Tealiumは、バッチコネクタアクションと非バッチコネクタアクションの両方を提供します。リアルタイムリクエストがユースケースにとって重要で、BrazeのAPIレート制限仕様にぶつかる心配がない場合は、非バッチコネクタを使用する必要があります。ご不明な点がございましたら、Braze サポートまたは顧客サクセスマネージャーにお問い合わせください。<br><br>

バッチコネクタの場合、リクエストは次のいずれかのしきい値に達するまでキューに入れられます。<br><br>
- 最大リクエスト数:75
- 最も古いリクエストからの最大時間:10 分
- リクエストの最大サイズ:1 メガバイト

Tealiumは、デフォルトでは同意イベント（サブスクリプション設定）やユーザー削除イベントをバッチ処理しません。
{% endalert %}

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Tealium アカウント | このパートナーシップを利用するには、[サーバー側またはクライアント側にアクセスできるTealiumアカウントが必要です](https://my.tealiumiq.com/)。 | 
| [インストール済みソースライブラリとTealiumソースライブラリ](https://docs.tealium.com/platforms/) | モバイルアプリ、ウェブサイト、バックエンドサーバーなど、Tealiumに送信されるデータの出所。<br><br>Tealiumコネクタを正常にセットアップするには、ライブラリをアプリ、サイト、またはサーバーにインストールする必要があります。 |
| Braze REST と SDKエンドポイント | REST または SDKエンドポイントの URL。エンドポイントは、[インスタンスの Braze URL]({{site.baseurl}}/api/basics/#endpoints) によって異なります。 |
| Braze アプリ識別子キー (サイドバイサイドのみ) | アプリ識別子キー。<br><br>これは **Braze ダッシュボード > 設定の管理 > API キーにあります**。 |
| コードバージョン (サイドバイサイドのみ) | SDK バージョンに対応し、メジャー.minor 形式 (たとえば、3.0.1 ではなく 3.2) である必要があります。コードバージョンは 3.0 以上である必要があります。 |
| REST API キー (サーバー間のみ) | `users.track``users.delete`および権限が付いた Braze REST API キーです。<br><br>これは **Braze ダッシュボード > デベロッパーコンソール > REST API キー > 新しい API キーの作成で作成できます**。|
{: .reset-td-br-1 .reset-td-br-2}

## 統合タイプを選択してください

| 統合 | 詳細 |
| ----------- | ------- |
| [サイド・バイ・サイド](#side-by-side-sdk-integration) | 's SDK to translate events into Braze'Tealiumのネイティブコールを使用しているため、サーバー間の統合よりも詳細な機能にアクセスでき、Brazeをより包括的に使用できます。<br><br>Brazeリモートコマンドを使用する予定の場合、TealiumはすべてのBrazeメソッド（コンテンツカードなど）をサポートしているわけではないことに注意してください。対応するリモートコマンドでマップされていない Braze メソッドを使用するには、ネイティブの Braze コードをコードベースに追加してメソッドを呼び出す必要があります。|
| [サーバー間](#server-to-server-integration) | Tealium からブレイズのREST APIエンドポイントにデータを転送します。<br><br>アプリ内メッセージング、コンテンツカード、プッシュ通知などの Braze UI 機能はサポートしていません。また、デバイスレベルのフィールドなど、この方法では使用できない自動的にキャプチャされたデータもあります。<br><br>これらの機能を使用する場合は、サイドバイサイド統合を検討してください。|
{: .reset-td-br-1 .reset-td-br-2}

## サイドバイサイド SDK 統合

### リモートコマンド

リモートコマンドはティーリアムのiOSおよびAndroidライブラリの機能の1つで、これにより、Tealium SDKから（Brazeサーバーを介して）Brazeに呼び出しを行うことができます。Braze リモートコマンドモジュールは、必要な Braze ライブラリを自動的にインストールおよびビルドし、すべてのメッセージレンダリングと分析トラッキング, 追跡を処理します。Braze モバイルリモートコマンドを使用するには、アプリにTealiumライブラリをインストールする必要があります。

Tealiumでは、Mobile Remote Commandを統合する2つの方法を提供しています。統合タイプ間で機能が失われることはなく、基盤となるネイティブコードは同じです。

| モバイルリモートコマンド方式 | プロ | 短所 |
| --- | --- | --- |
| **リモートコマンドタグ** | Tealium iQ UIを使用して、リモートコマンドに送信されるマッピングとデータを簡単に変更できます。<br><br>これにより、アプリが既にアプリストアに追加された後でも、クライアントアプリ更新しなくても、追加のデータやイベントをサードパーティのSDKに送信アプリ。 | アプリタグ管理モジュールは、非表示のウェブビューを使用してJavaScriptを処理します。 |
| **JSON コンフィギュレーションファイル**<br>([おすすめ](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#how-it-works)) | JSON メソッドを使用すると、アプリに Web ビューを非表示にする必要がなくなり、メモリ消費量が大幅に削減されます。<br><br>JSON ファイルは、お客様のアプリ内でリモートまたはローカルにホストできます。 | 現時点では、これを管理するためのUIがないため、少し手間がかかります。<br><br>Note: Tealiumは、この問題を解決し、iQ Tag管理バージョンと同じレベルの柔軟性をJSONリモートコマンドにもたらす管理UIの追加に取り組んでいます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Braze モバイルリモートコマンドデータマッピングを使用して、デフォルトユーザー属性とカスタム属性を設定し、購入とカスタムイベントを追跡します。対応する Braze メソッドについては、次の表を参照してください。

| リモートコマンド | Braze 法 |
| -------------- | ------------ |
| appendcustomarrayattribute | addToCustomAttributeArrayWithKey()|
| emailnotification | setEmailNotificationSubscriptionType() |
| incrementcustomattribute | incrementCustomAttribute() |
| Initalize | startWithApiKey() |
| logcustomevent | logCustomEvent() |
| logpurchase | logPurchase() |
| pushnotification | setPushNotificationSubscriptionType() |
| removecustomattribute | setCustomAttributeWithKey() |
| setcustomattribute | setCustomAttributeArrayWithKey() |
| setcustomarrayattribute | setCustomAttributeArrayWithKey() |
| setlastknownlocation | setLastKnownLocationWithLatitude() |
| unsetcustomattribute | unsetCustomAttributeWithKey() |
| useralias | addAlias() |
| userattribute | ABKUser() |
| useridentifier | changeUser() |
{: .reset-td-br-1 .reset-td-br-2}

Brazeモバイルリモートコマンドの設定方法の詳細とサポートされている方法の概要については、Tealium開発者ドキュメントをご覧ください。
- [リモートコマンド](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#json-template)
- [リモートコマンドタグ](https://docs.tealium.com/client-side-tags/braze-mobile-remote-command-tag/)

{% alert important %}
Braze モバイルリモートコマンドは、すべての Braze メソッドとメッセージングチャネル (コンテンツカードなど) をサポートしているわけではありません。対応するリモートコマンドでマップされていない Braze メソッドを使用するには、ネイティブの Braze コードをコードベースに追加してメソッドを直接呼び出す必要があります。
{% endalert%}

### Braze Web SDK タグ

Braze Web SDK タグを使用して Braze のWeb SDK をWeb サイトデプロイしてください。[Tealium iQタグ管理により](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)、お客様はTealiumダッシュボードにBrazeをタグとして追加して、訪問者のアクティビティを追跡できます。タグは通常、マーケティング担当者がオンライン広告、メールマーケティング、サイトパーソナライゼーションズの効果を理解するために使用されます。

1. Tealium で、「**iQ」>「タグ」>「+ タグを追加」>「Braze** Web SDK」に移動します。
2. タグ設定ダイアログボックスで、API キー (Braze アプリ識別子キー)、ベース URL (Braze SDKエンドポイント)、および [Braze Web SDK](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) コードバージョンを入力します。また、ログを有効にして Web コンソールに情報を記録して、デバッグを行うこともできます。
3. [読み込むルールダイアログボックスで](https://docs.tealium.com/iq-tag-management/load-rules/about/)、「すべてのページにロード」を選択するか、「**ルールを作成**」を選択して、サイトのこのタグインスタンスをロードするタイミングと場所を決定します。
4. **[データマッピングダイアログボックスで、「マッピングを作成](https://docs.tealium.com/iq-tag-management/data-mappings/about/)****」を選択し、TealiumデータをBrazeにマッピングします**。Braze Web SDK タグの送信先変数は、タグの \[**データマッピング**] タブに組み込まれています。[次の表は](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)、使用可能な送信先カテゴリと各送信先名を示しています。
5. \[**完了**] を選択します。

### サイドバイサイド統合リソース

- iOS リモートコマンド:[ティーリアムのドキュメント、Tealium](https://docs.tealium.com/platforms/remote-commands/integrations/braze/) [GitHub](https://github.com/Tealium/tealium-ios-braze-remote-command) リポジトリ
- Android リモートコマンド:[ティーリアムのドキュメント、Tealium](https://docs.tealium.com/platforms/remote-commands/integrations/braze/) [GitHub](https://github.com/Tealium/tealium-android-braze-remote-command) リポジトリ
- Web SDK タグ:[Tealium ドキュメント](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)

## サーバー間の統合

このインテグレーションは、Tealium からBraze REST APIにデータを転送します。

サーバー間統合では、アプリ内メッセージング、コンテンツカード、プッシュ通知などの Braze UI 機能はサポートされません。この方法では利用できない自動的にキャプチャされたデータ (デバイスレベルのフィールドなど) もあります。

このデータとこれらの機能を使用したい場合は、[サイドバイサイドSDK統合を検討してください]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium/#side-by-side-sdk-integration)。

### ステップ1:ソースをセットアップ

Tealiumでは、最初にコネクタの描画元となる有効なデータソースを設定する必要があります。
1. Tealiumのサイドバーの「**サーバー側**」から、「**ソース」>「データソース」>「+ データソースを追加**」に移動します。
2. 利用可能なカテゴリから目的のプラットフォームを見つけ、ソースに名前を付けます。これは必須フィールドです。<br>![][6]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
3. **イベント仕様オプションから**、[含めたいイベント仕様を選択します](https://docs.tealium.com/server-side/event-specifications/about/)。イベント仕様は、インストールで追跡するイベント名と必須属性を特定するのに役立ちます。これらの仕様は受信イベントに適用されます。<br>![][7]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>時間をかけて、どのデータが自分にとって最も価値があり、どの仕様がユースケースに最も適しているかを考えてください。\[][19]イベント仕様のカスタマイズも可能です。<br>
4. 次のダイアログは「**コードを取得**」ステップに進みます。ここに記載されている基本コードイベントトラッキング, 追跡コード、インストールガイドとして役立ちます。これらの指示をチームと共有したい場合は、付属の PDF をダウンロードしてください。終了したら、\[**保存して続行**] を選択します。<br>
5. これで、保存したソースを表示したり、イベント仕様を追加または削除したりできるようになります。<br>![][18]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>詳細なデータソースビューから、次のアクションを実行できます。
- データソースキーを表示してコピーする
- インストール手順を表示
- 「**コードを取得**」ページに戻る
- イベント仕様の追加または削除
- イベント仕様に関連するライブイベントを表示するにはナビゲートしてください
- そして、もっと...<br>
6. 最後に、ページの上部にある \[**保存/公開**] を選択します。ソースを公開しないと、Braze コネクターの設定時にソースを見つけることができません。

[データソース設定](https://docs.tealium.com/server-side/data-sources/about-data-sources/)と編集の詳細については、「データソース」を参照してください。

### ステップ2:イベントコネクタの作成

コネクタは、Tealiumとデータ送信に使用される他のベンダーとの統合です。これらのコネクタには、パートナーがサポートする API を表すアクションが含まれています。 

1. Tealiumのサイドバーの「**サーバーサイド」から、「イベントストリーム**」>「**イベントコネクター**」に移動します。
2. 青い \[**\+ コネクタを追加**] ボタンを選択して、コネクタマーケットプレイスを確認します。表示される新しいダイアログボックスで、**スポットライト検索を使用してBrazeコネクタを見つけます**。
3. このコネクタを追加するには、**Braze** コネクタータイルをクリックします。クリックすると、接続の概要と、必要な情報、サポートされているアクション、および設定手順のリストが表示されます。設定は、ソース、構成、アクションの 3 つのステップで構成されます。

#### ソース

ソースを設定したら、「**イベントストリーム」>「イベントコネクター」>「+ コネクターを追加」>「Braze」の Braze コネクターページに戻ります**。 

開いたダイアログで、作成したばかりのデータソースを選択し、\[**イベントフィード**] で \[**すべてのイベント**] または \[特定のイベント仕様] を選択します。これは、変更された値のみを Braze に送信するための推奨パスです。\[**続行**] をクリックします。

#### コンフィギュレーション

次に、ページの下部にある \[**コネクタを追加**] を選択します。コネクタに名前を付け、Braze API エンドポイントと Braze REST API キーをここに入力してください。

![][15]{: style="max-width:70%;"}

以前にコネクタを作成したことがある場合は、オプションで利用可能なコネクタリストから既存のコネクタを使用し、鉛筆アイコンを使用してニーズに合わせて変更したり、ゴミ箱アイコンで削除したりできます。 

#### アクション (Action)

次に、コネクタアクションに名前を付け、設定したマッピングに従ってデータを送信するアクションタイプを選択します。ここでは、Brazeの属性、イベント、購入をTealiumの属性、イベント、購入名にマッピングします。

{% alert important %}
入力されたすべてのフィールドが必須というわけではありません。

![] ({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Track User (Batch and Non-Batch) %}

このアクションにより、ユーザー、イベント、購入の属性をすべて1つのアクションで追跡できます。

| パラメーター | 説明 |
| ---------- | ----------- |
| ユーザー ID | このフィールドを使用して、Tealiumユーザー ID フィールドを対応するBrazeフィールドにマップします。1 つ以上のユーザー ID 属性をマップします。複数の ID を指定すると、空白でない最初の値が次の優先順位に基づいて選択されます。外部 ID、Braze ID、エイリアス名、エイリアスラベル<br><br>-プッシュトークンをインポートする場合、外部IDとBraze IDを指定しないでください。<br>-ユーザーエイリアスを指定する場合は、エイリアス名とエイリアスラベルを設定する必要があります。<br><br>詳細については、Braze [`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)をご覧ください。 |
| ユーザー属性 | Braze の既存のユーザープロファイルフィールド名を使用して、Braze ダッシュボードのユーザープロファイル値を更新したり、[独自のカスタムユーザー属性データをユーザープロファイルに追加したりできます]({{site.baseurl}}/api/objects_filters/user_attributes_object/)。<br><br>-デフォルト、ユーザーが存在しない場合は新しいユーザーが作成されます。<br>-「**既存のみ更新**」を設定すると`true`、既存のユーザーのみが更新され、新しいユーザーは作成されません。<br>-Tealiumの属性が空の場合、その属性はnullに変換され、Brazeユーザープロファイルから削除されます。ユーザー属性削除するためにヌル値をBrazeに送信したくない場合は、エンリッチメントを使用する必要があります。 |
| ユーザー属性の変更 | このフィールドを使用して、特定のユーザー属性をインクリメントまたはデクリメントします。<br><br>-整数属性は、正または負の整数でインクリメントできます。<br>-配列属性は、既存の配列に値を追加または削除することで変更できます。 |
| イベント | イベントは、特定のユーザータイムスタンプ時にカスタムイベントを 1 回だけ発生させたことを表します。このフィールドを使用して、Braze [イベントオブジェクト内のようなイベント属性を追跡およびマッピングします]({{site.baseurl}}/api/objects_filters/event_object/)。<br><br>-`Name` イベント属性は、マップされたすべてのイベントに必要です。<br>-`Time` イベント属性は、明示的にマッピングされていない限り、自動的に now に設定されます。<br>-デフォルト、イベントが存在しない場合は新しいイベントが作成されます。設定`Update Existing Only``true`、既存のイベントのみが更新され、新しいイベントは作成されません。<br>-配列タイプの属性をマップして複数のイベントを追加します。配列型の属性は同じ長さでなければなりません。<br>-単一値属性を使用して各イベントに適用できます。 |
| イベントテンプレート | ボディデータで参照されるイベントテンプレートを提供します。テンプレートを使用して、Braze に送信する前にデータを変換できます。詳細については、[Tealiumのテンプレートガイドを参照してください](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)。 |
| イベントテンプレート変数 | イベントテンプレート変数をデータ入力として提供します。詳細については、[Tealiumのテンプレート変数ガイドを参照してください](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)。 |
| 購入 | このフィールドを使用して、Braze [購入オブジェクトにあるようなユーザー]({{site.baseurl}}/api/objects_filters/purchase_object/)購入属性を追跡およびマッピングします。<br><br>-購入属性`Product ID`、`Currency`、`Price`は、マップされたすべての購入に必須です。<br>-Purchase `Time` 属性は、明示的にマッピングされていない限り、自動的に now に設定されます。<br>-デフォルト、新規購入品が存在しない場合は新規購入品が作成されます。設定`Update Existing Only``true`、既存の購入のみが更新され、新しい購入は作成されません。<br>-配列タイプの属性をマップして、複数の購入アイテムを追加します。配列型の属性は同じ長さでなければなりません。<br>-単一値属性を使用でき、各項目に適用されます。|
| 購入テンプレート | テンプレートを使用して、Braze に送信する前にデータを変換できます。<br>-ネストされたオブジェクトのサポートが必要な場合は、購入テンプレートを定義してください。<br>-購入テンプレートが定義されている場合、アクションの購入セクションで設定された設定は無視されます。<br>-詳細については、[Tealiumのテンプレートガイドを参照してください](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)。|
| 購入テンプレート変数 | データ入力として製品テンプレート変数を指定します。詳細については、[Tealiumのテンプレート変数ガイドを参照してください](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)。 |
{: .reset-td-br-1 .reset-td-br-2}

![] ({% image_buster /assets/img/tealium/track_user_example.png %})

{% endtab %}
{% tab Delete User (Non-Batch) %}

このアクションにより、Braze ダッシュボードからユーザーを削除できます。

| パラメーター | 説明 |
| ---------- | ----------- |
| ユーザー ID | このフィールドを使用して、TealiumユーザーIDフィールドを対応するBrazeにマップします。<br><br>-1 つ以上のユーザー ID 属性をマップします。複数の ID を指定すると、空白でない最初の値が次の優先順位に基づいて選択されます。外部 ID、Braze ID、エイリアス名、エイリアスラベル<br>-ユーザーエイリアスを指定する場合、エイリアス名とエイリアスラベルの両方を設定する必要があります。<br><br>詳しくは、Braze [`/users/delete`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)をご覧ください。 |
{: .reset-td-br-1 .reset-td-br-2}

![] ({% image_buster /assets/img/tealium/track_user_delete.png %})

選択したオプションを変更する場合は、\[**編集に戻る**] または \[**完了**] を選択して完了します。

{% endtab %}
{% endtabs %}

\[**続行**] を選択します。

これで、Tealiumホームページのコネクタのリストにコネクタが表示されます。<br>![][13]{: style="max-width:80%;"}

終了したら、**必ずコネクタを保存/公開してください**。設定したアクションは、トリガー接続が満たされたときに実行されるようになりました。 

### ステップ3:お使いの Tealium コネクタをテストしてください

コネクタが起動したら、テストして正しく動作していることを確認する必要があります。これをテストする最も簡単な方法は、**Tealiumトレースツールを使用することです**。Traceを使い始めるには、Tealium Toolsのブラウザ拡張機能を追加していることを確認してください。

1. 新しいトレースを開始するには、サイドバーの \[**サーバー側オプション**] で \[**トレース**] を選択します。\[**開始**] をクリックし、トレース ID をキャプチャします。
2. ブラウザー拡張機能を開き、AudienceStream トレースにトレース ID を入力します。
3. リアルタイムログを調べてください。
4. 「Actions **Triggered」エントリをクリックして展開し、検証するアクションを確認します**。
5. 検証したいアクションを探し、ログステータス。 

Tealiumのトレースツールを参照してください's [Trace documentation][21] for more detailed instructions on implementing Tealium'。

## インテグレーションデモ

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## データポイント超過の可能性

Tealiumを通じてBrazeを統合する際に、誤ってデータオーバーに陥る主な原因は3つあります。

#### 重複データの送信-属性のBrazeデルタのみを送信
Tealium はユーザー属性のBrazeデルタを送信しません。たとえば、's first name, email, and cell phone number, Tealium will send all three attributes to Braze anytime the action is triggered. Tealium won'ユーザーを追跡する EventStream アクションがある場合、何が変更されたか、更新されたかを探して、その情報のみを送信します。<br><br> 
**解決策**:<br>バックエンドをチェックして属性変更されたかどうかを評価し、変更された場合は、Tealiumの関連メソッドを呼び出してユーザープロファイル更新できます。**これは、Brazeを直接統合するユーザーが通常行うことです。**<br>**または**<br> 't store your own version of a user profile in your backend and can'属性が変わるかどうかわからない場合は、AudienceStreamを使用して、
[値が変更されたときにのみユーザー属性を送信するようにエンリッチメントを作成します](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/)。[エンリッチメントルールに関するTealiumのドキュメントを参照してください](https://docs.tealium.com/server-side-connectors/braze-connector/)。

#### 無関係なデータを送信したり、データを不必要に上書きしたりする
同じイベントフィードをターゲットとする複数のEventStreamがある場合、**1つのアクションがトリガーされるたびに、そのコネクタで有効になっているすべてのアクションが自動的に起動します**。**これにより、Brazeでデータが上書きされ、不要なデータポイントが消費される可能性もあります**。<br><br>
**解決策**:<br>個別のイベント仕様またはフィードを設定して、各アクションを追跡します。<br>**または**<br> Tealiumダッシュボードのトグルを使用して、起動させたくないアクション（またはコネクタ）を無効にします。

#### Braze の初期化が早すぎる
Braze Web SDKタグを使用してTealiumと統合したユーザーは、MAUが劇的に増加することがあります。**ページの読み込む時に Braze が初期化されると、ウェブユーザー初めてWeb サイトに移動するたびに Braze は匿名プロファイル作成します。**MAU数を減らすために、ユーザーが「サインイン」や「ビデオ視聴」などの何らかのアクションを完了したときのみユーザー行動を追跡したい場合があります。<br><br>
**解決策**:<br>[読み込むルールを設定して](https://docs.tealium.com/iq-tag-management/load-rules/about/)、サイトのタグが読み込まれるタイミングと場所を正確に決定します。 

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[5]: {% image_buster /assets/img/tealium/braze_connector_marketplace.png %}
[6]: {% image_buster /assets/img/tealium/data_source.png %}
[7]: {% image_buster /assets/img/tealium/event_specs.png %}
[8]: {% image_buster /assets/img/tealium/get_code.png %}
[9]: {% image_buster /assets/img/tealium/summary.png %}
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[13]: {% image_buster /assets/img/tealium/summary_list.png %}
[15]: {% image_buster /assets/img/tealium/create_configuration.png %}
[16]: {% image_buster /assets/img/tealium/connector_summary.png %}
[17]: {% image_buster /assets/img/tealium/save_publish.png %}
[18]: {% image_buster /assets/img/tealium/braze_connection.png %}
[19]: https://docs.tealium.com/iq-tag-management/events/about/
[21]: https://docs.tealium.com/server-side/connectors/trace/about/
[22]: {% image_buster /assets/img/tealium/tealium_overview.png %}
[23]: {% image_buster /assets/img/tealium/remote_mappings.png %}
