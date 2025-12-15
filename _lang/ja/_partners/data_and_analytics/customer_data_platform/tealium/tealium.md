---
nav_title: Tealium
article_title: Tealium
page_order: 1
alias: /partners/tealium/
description: "このリファレンス記事では、Braze とTealium の提携について概説します。これは、モバイル、ウェブ、および代替データを他のサードパーティのソースに接続できるユニバーサルデータハブです。"
page_type: partner
search_tag: Partner

---

# Tealium

> [Tealium](https://tealium.com/) は、EventStream、AudienceStream、および iQ Tag Management で構成されるユニバーサルデータハブおよびカスタマーデータプラットフォームであり、サードパーティのソースのモバイルデータ、Web データ、および代替データを接続できます。Tealium を Braze と接続することで、カスタムイベント、ユーザー属性、購入のデータフローが実現し、リアルタイムでデータを操作できるようになります。

![さまざまな Tealium 製品と Braze プラットフォームがどのように連携してクロスチャネルキャンペーンをリアルタイムでアクティブにするかを示す Teralium の概要図。]({% image_buster /assets/img/tealium/tealium_overview.png %}){: style="border:0;"}

BrazeとTealiumインテグレーションを使用すると、ユーザーを追跡し、さまざまなユーザー 分析プロバイダーにデータをルーティングできます。Tealiumでは次の操作ができます。
- [AudienceStream]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_audience_stream/)で Tealium オーディエンスを Braze に同期し、Braze キャンペーンとキャンバスのパーソナライズ、またはセグメントの作成に使用できるようにします。
- [プラットフォーム間でデータをインポートします](#choose-your-integration-type)。Braze は、Android、iOS、およびWeb アプリの各アプリケーションに[並列](#side-by-side-sdk-integration)SDKインテグレーションと、イベントデータにレポートできる任意のプラットフォーム内で使用できる[server-to-server](#server-to-server-integration)インテグレーションの両方を提供します。<br><br>

{% tabs %}
{% tab EventStream %}
Tealium EventStream は、データの中央に位置するデータ収集および API ハブです。EventStream は、セットアップとインストールから、受信ユーザーデータの識別、検証、および拡張まで、データサプライチェーン全体を処理します。EventStream は、イベントフィードとコネクターを使用してリアルタイムアクションを実行します。以下は、[EventStream](https://docs.tealium.com/server-side/getting-started/eventstream-api-hub/introduction/)を構成する機能です。
- データソース (インストールおよびデータ収集)
- ライブイベント(リアルタイムデータ検査)
- イベント仕様と属性s(データレイヤー要件と検証)
- イベントフィード (フィルタリングされたイベントタイプ)
- イベントコネクター(API ハブアクションs)

{% endtab %}
{% tab AudienceStream %}

Tealium AudienceStreamはオムニチャネル 顧客 セグメンテーションでリアルタイムのアクションエンジンです。AudienceStream は EventStream に流入するデータを取得し、ブランドのカスタマーエンゲージメントの最も重要な属性を表す訪問者プロファイルを作成します。設定ステップについては、[AudienceStream]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_audience_stream/)を参照してください。

{% endtab %}
{% tab iQ Tag Management %}
Tealium iQ では、Tealium iQ Tag Management UI でタグを使用してアプリでコードをトリガーできます。このタグにより、モバイルおよび Web プラットフォームからイベントデータが収集、制御、および配信されます。これにより、アプリケーションに Braze 固有のコードを追加することなく、ネイティブの Braze 実装を設定できます。ユーザーは、iQ Tag Management または JSON 設定ファイルを使用してモバイルリモートコマンドを統合できます (Tealium アプローチが推奨されます)。Braze Web SDK を使用するユーザーは、Web iQ タグを使用して統合を行う必要があります。

各メソッドの長所と短所について詳しくは、以下の[ Tealium iQ タグ マネージャー](#mobile-remote-commands) を参照してください。
{% endtab %}
{% endtabs %}

{% alert important %}
Tealium は、バッチと非バッチの両方のコネクターアクションを提供します。非バッチコネクターは、リアルタイムリクエストがユースケースにとって重要であり、Braze の API レート制限指定に達する懸念がない場合にのみ使用してください。不明な点がある場合は、Brazeサポートまたは顧客のサクセスマネージャーにお問い合わせください。<br><br>

バッチ・コネクターの場合、要求は、以下のいずれかのしきい値が満たされるまでキューに入れられます。<br><br>
- 最大リクエスト数:75
- 最も古いリクエストからの最大経過時間:10分
- 要求の最大サイズ1 MB

Tealium は、デフォルトでは同意イベント (サブスクリプション設定) またはユーザー削除イベントをバッチ処理しません。
{% endalert %}

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Tealium アカウント | この提携を進めるには、サーバーおよび/またはクライアントサイドアクセスを持つ[Tealiumアカウント](https://my.tealiumiq.com/)が必要です。 | 
| インストールされたソースと Tealium ソースの[ライブラリ](https://docs.tealium.com/platforms/) | モバイルアプリ、Web サイト、バックエンドサーバーなど、Tealium に送信されるデータの提供元。<br><br>適切な Tealium コネクターを設定できるようにするには、ライブラリをアプリ、サイト、サーバーにインストールしておく必要があります。 |
| Braze RESTとSDKエンドポイント | REST または SDK エンドポイントの URL。エンドポイントはインスタンスの [Braze URL]({{site.baseurl}}/api/basics/#endpoints) に応じて異なります。 |
| Braze アプリ 識別子鍵(横並びのみ) | アプリ識別子キー。<br><br>これは、**Braze ダッシュボード > [設定の管理] > [API キー]** で確認できます。 |
| コードバージョン(並列のみ) | SDK バージョンに対応し、major.minor 形式である必要があります (3.0.1ではなく3.2など)。コードバージョンは3.0以上である必要があります。 |
| REST API キー(サーバ間のみ) | `users.track` および`users.delete` 権限を持つBraze REST API キー。<br><br>これは **Brazeダッシュボード > [開発者コンソール] > [REST API キー] > [新しい API キーを作成]** で作成できます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合タイプを選択する

| 統合 | 詳細 |
| ----------- | ------- |
| [サイドバイサイド](#side-by-side-sdk-integration) | Tealium の SDK を使用して、イベントを Braze のネイティブ呼び出しに変換します。これにより、サーバー間統合よりも高度な機能にアクセスでき、Braze をより包括的に使用できるようになります。<br><br>Brazeのリモートコマンドを使用する場合は、TealiumがすべてのBraze方法(コンテンツカードなど)に対応しているわけではないことに注意してください。対応するリモートコマンドにマッピングされていない Braze メソッドを使用するには、ネイティブ Braze コードをコードベースに追加してメソッドを呼び出す必要があります。|
| [サーバー間](#server-to-server-integration) | Tealium から Braze REST API エンドポイントにデータを転送します。<br><br>アプリ メッセージング内、コンテンツカード、プッシュ通知などのBrazeのユーザーインターフェイス機能には対応していません。また、この方法では利用できないデバイスレベルのフィールドなど、自動的に取得されるデータも存在します。<br><br>これらの機能を使用する場合は、並列統合を検討してください。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## サイドバイサイドの SDK 統合

### リモートコマンド

リモートコマンドは、Tealium iOS および Android ライブラリの機能であり、Tealium SDK から Braze サーバーを介して Braze への呼び出しを実行できるようにします。Braze リモートコマンドモジュールは、必要な Braze ライブラリを自動的にインストールおよびビルドし、すべてのメッセージレンダリングと分析トラッキングを処理します。Braze モバイルリモートコマンドを使用するには、アプリs にインストールされているTealium ライブラリが必要です。

Tealium には、モバイルリモートコマンドを統合する2 つの方法があります。統合タイプ間で機能が失われることはなく、基礎となるネイティブコードは同じです。

| モバイルリモートコマンド方式 | 長所 | 短所 |
| --- | --- | --- |
| **リモートコマンドタグ** | Tealium iQ UI を使用して、リモートコマンドに送信されるデータとマッピングを簡単に変更できます。<br><br>これにより、アプリがすでにアプリストアに入った後、クライアントがアプリを更新する必要なく、追加のデータまたはイベントをサードパーティSDKに送信できます。 | アプリのタグマネジメントモジュールは、非表示のWeb ビューに依存してJavaScript を処理します。 |
| **JSON構成ファイル**<br>([推奨](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#how-it-works)) | JSONメソッドを使用すると、アプリで非表示のWebビューを使用する必要がなくなり、メモリー使用量が大幅に削減されます。<br><br>JSON ファイルは、顧客のアプリ内でリモートまたはローカルにホストできます。 | 現時点では、これを管理するUIがないため、少し手間がかかります。<br><br>注:Tealium は、この問題を解決し、iQ Tag Management バージョンと同じレベルの柔軟性を JSON リモートコマンドに取り入れる Management UIの追加に取り組んでいます |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Braze モバイルリモートコマンドのデータマッピングを使用して、デフォルトのユーザー属性とカスタム属性を設定し、購入とカスタムイベントを追跡します。対応するBraze方法については、次の表を参照してください。

| リモートコマンド | Braze のメソッド |
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
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze モバイルリモートコマンドの設定方法の詳細と、サポートされている方法の概要については、Tealium 開発者 ドキュメントを参照してください。
- [リモートコマンド](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#json-template)
- [リモートコマンドタグ](https://docs.tealium.com/client-side-tags/braze-mobile-remote-command-tag/)

{% alert important %}
Braze モバイルリモートコマンドは、すべての Braze メソッドとメッセージングチャネルをサポートしているわけではありません (コンテンツカードなど)。対応するリモートコマンドにマッピングされていない Braze メソッドを使用するには、ネイティブ Braze コードをコードベースに追加してメソッドを直接呼び出す必要があります。
{% endalert%}

### Braze Web SDK タグ

Web サイトに Braze Web SDK をデプロイするには、Braze Web SDK タグを使用します。[Tealium iQ Tag Management](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/) により、顧客は訪問者のアクティビティを追跡するために Tealium ダッシュボード内でタグとして Braze を追加できます。タグは一般的に、オンライン広告、メールマーケティング、およびサイトのパーソナライゼーションの効果を理解する目的でマーケターにより使用されます。

1. Tealium で **[iQ] > [Tags] > [+ Add Tag] > [Braze Web SDK]** に移動します。
2. [Tag Configuration] ダイアログボックスで、API キー (Braze アプリ識別子キー)、ベース URL (Braze SDK エンドポイント)、および[Braze Web SDK コードバージョン](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) を入力します。また、ロギングを有効にして、デバッグ目的で Web コンソールに情報を記録することもできます。
3. [[Load Rules](https://docs.tealium.com/iq-tag-management/load-rules/about/)] ダイアログボックスで [Load on All Pages] を選択するか、または [**Create Rule**] を選択して、サイトでこのタグのインスタンスをいつどこに読み込むかを決定します。
4. **[Data Mアプリings](https://docs.tealium.com/iq-tag-management/data-mappings/about/)**ダイアログボックスで、**Create Mアプリings**を選択してTealiumデータをBrazeにマッピングします。Braze Web SDK タグの宛先変数は、タグの [**Data Mapping**] タブに組み込まれています。[これらの表](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)に、使用可能な宛先カテゴリと、それぞれの宛先名の説明が示されています。
5. [**Finish**] を選択します。

### サイドバイサイド統合のリソース

- iOS リモートコマンド:[Tealium ドキュメント](https://docs.tealium.com/platforms/remote-commands/integrations/braze/),[Tealium GitHub リポジトリ](https://github.com/Tealium/tealium-ios-braze-remote-command)
- Androidリモートコマンド:[Tealium ドキュメント](https://docs.tealium.com/platforms/remote-commands/integrations/braze/),[Tealium GitHub リポジトリ](https://github.com/Tealium/tealium-android-braze-remote-command)
- Web SDK タグ:[Tealium ドキュメント](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)

## サーバー間統合

この統合により、Tealium から Braze REST API にデータが転送されます。

サーバー間統合では、アプリ内メッセージング、コンテンツカード、プッシュ通知などの Braze UI 機能はサポートされていません。また、このメソッドでは使用できない、自動的にキャプチャされるデータ(デバイスレベルのフィールドなど) もあります。

このデータとこれらの機能を使用する場合は、[並列]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium/#side-by-side-sdk-integration)SDKインテグレーションを検討してください。

### ステップ1: ソースを設定する

Tealium では最初に、コネクターの取得元となる有効なデータソースを設定する必要があります。
1. Tealium のサイドバーの [**Server-Side**] から **[Sources] > [Data Sources] > [+ Add Data Source]** に移動します。
2. 使用可能なカテゴリ内で目的のプラットフォームを見つけ、ソースに名前を付けます。これは必須フィールドです。<br>![]({% image_buster /assets/img/tealium/data_source.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
3. **Event Specifications**オプションから、含める[イベント仕様](https://docs.tealium.com/server-side/event-specifications/about/)を選択します。イベント仕様は、インストールで追跡するイベント名と必須属性を特定するのに役立ちます。これらの仕様は受信イベントに適用されます。<br>![]({% image_buster /assets/img/tealium/event_specs.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>どのデータがあなたにとって最も価値があるのか、どの仕様があなたのユースケースに最も適しているのか、時間をかけて考えてみよう。[カスタムイベント仕様](https://docs.tealium.com/iq-tag-management/events/about/)も可能です。<br>
4. 次に、**Get Code**ステップに進みます。ここで提供されるベースコードとイベント追跡コードは、インストールガイドとして機能します。これらの指示を共有したい場合は、提供されたPDF を読み込むします。終了したら**Save& Continueを**選択する。<br>
5. これで、保存したソースを表示し、イベント仕様を追加または削除することができます。<br>![]({% image_buster /assets/img/tealium/braze_connection.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>詳細なデータソースビューから、次のアクションを実行できます。
- データソース鍵の表示と複製
- インストール手順を表示する
- **Get Code**ページに戻る
- イベント仕様の追加または削除
- イベント仕様に関連するライブイベントを表示するために移動します
- その他<br>
6. 最後に、ページの上部にある**Save / Publish**を選択します。ソースを公開しないと、Braze コネクターの設定時にソースを見つけることができません。

データソースの設定と編集の詳細な手順については、[データソース](https://docs.tealium.com/server-side/data-sources/about-data-sources/)を参照してください。

### ステップ2:イベントコネクターを作成する

コネクターとは、Tealium と他のベンダーの間でデータを伝送するために使用される統合です。これらのコネクターには、パートナーがサポートするAPI を表すアクションが含まれています。 

1. Tealium のサイドバーの [**Server-Side**] から **[EventStream] > [Event Connectors]** に移動します。
2. 青色の [**＋Add Connector**] ボタンを選択して、コネクターマーケットプレースを参照します。アプリが耳にする新しいダイアログボックスで、スポットライト検索を使用して**Braze** コネクターを見つけます。
3. このコネクターを追加するには、**Braze**コネクタータイルを選択します。クリックすると、接続の概要と、必要な情報、サポートされるアクション、および設定手順の一覧が表示されます。この設定は、ソース、設定、アクションの3つのステップで構成されています。

#### ソース

ソースの設定が完了したら、[**EventStream**] > [**Event Connectors**] > [**\+ Add Connector**] > [**Braze**] の Braze コネクタページに戻ります。 

作成したデータソースを選択し、**Event Feed**で**All Events**または特定のイベント仕様を選択して、変更された値のみをBrazeに送信する推奨パスを選択します。**Continue**を選択します。

#### 構成

次に、ページの下部で**Add Connector** を選択します。コネクターに名前を付け、Braze エンドポイントと Braze REST API キーを指定します。

![]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

以前にコネクターを作成したことがある場合は、利用可能なコネクターのリストにある既存のコネクターを使用し、鉛筆アイコンでニーズに合わせて変更するか、ゴミ箱アイコンでコネクターを削除することができます。 

#### アクション (Action)

次に、コネクターアクションに名前を付け、設定するマッピングに従ってデータを送信するアクションタイプを選択します。ここでは、Braze の属性、イベント、および購入をTealium の属性、イベント、および購入名にマッピングします。

{% alert important %}
提供されるすべてのフィールドが必要なわけではありません。

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Track User - Batch and Non-Batch %}

このアクションを使用すると、ユーザー、イベント、購入属性をすべて1回のアクションで追跡できます。

| パラメータ | 説明 |
| ---------- | ----------- |
| ユーザー ID | このフィールドを使用して、Tealium のユーザー ID フィールドを Braze の対応するフィールドにマッピングします。1 つ以上のユーザー ID 属性をマップします。複数のID が指定されている場合、最初の非ブランク値は、次の優先順位に基づいて選択されます。External ID、Braze ID、エイリアス名、エイリアスラベル。<br><br>\- プッシュトークンs をインポートする場合は、外部ID とBraze ID を指定しないでください。<br>\- ユーザーエイリアスを指定する場合、エイリアス名とエイリアスラベルの両方を設定する必要があります。<br><br>詳細については、Braze[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) を参照してください。 |
| ユーザ属性 | 既存の Braze のユーザープロファイルのフィールド名を使用して、Braze ダッシュボードのユーザープロファイル値を更新するか、独自のカスタム[ユーザー属性]({{site.baseurl}}/api/objects_filters/user_attributes_object/)データをユーザープロファイルに追加します。<br><br>\- デフォルトでは、新規ユーザーが存在しない場合は作成されます。<br>\- 設定では、** 更新 Existing Only** to `true` で、存在するユーザーs のみが更新d になり、新しいユーザーは作成されません。<br>\- Tealium 属性が空の場合、その属性は NULL に変換され、Braze ユーザープロファイルから削除されます。ユーザー属性を削除する目的で Braze に NULL 値を送信すべきでない場合は、エンリッチメントを使用してください。 |
| ユーザー属性の変更 | このフィールドを使用して、特定のユーザー 属性を増減します<br><br>\- 整数属性は、正の整数または負の整数でインクリメントできます。<br>\- 配列属性s は、既存の配列に数値を追加または削除することで修正できます。 |
| イベント | イベントは、タイムスタンプの時点で特定のユーザーによりカスタムイベントが 1回発生したことを表します。このフィールドは、Braze [イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object/)の属性と同様にイベント属性を追跡、マッピングする場合に使用します。<br><br>\- イベント属性 `Name` は、マッピングされたすべてのイベントで必要です。<br>\- イベント属性 `Time` は、明示的にマッピングされていない限り、自動的に現時点の時刻に設定されます。<br>\- デフォルトでは、新しいイベントは存在しない場合に作成されます。`Update Existing Only` を`true` に設定すると、既存のイベントのみが更新され、新規のイベントは作成されません。<br>\- 配列型属性s をマップして、複数のイベントを追加します。配列型の属性s は等しい長さでなければなりません。<br>\- 単一値属性を使用できます。単一値属性は各イベントに適用できます。 |
| イベントテンプレート | ボディデータで参照するイベントテンプレートを指定します。テンプレートを使用してデータを変換してから、Brazeに送信できます。詳細については、Tealiumの[テンプレートガイド](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)を参照してください。 |
| イベントテンプレート変数 | イベントテンプレート変数をデータ入力として指定します。詳細については、Tealiumの[テンプレート変数ガイド](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)を参照してください。 |
| 購入 | このフィールドは、Braze [購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)の属性と同様に購入属性を追跡、マッピングする場合に使用します。<br><br>\- 購入属性 `Product ID`、`Currency`、`Price` は、マッピングされたすべての購入に必要です。<br>\- 購入属性 `Time` は、明示的にマッピングされていない限り、自動的に現時点の時刻に設定されます。<br>\- デフォルトでは、新規購入が存在しない場合は作成されます。`Update Existing Only` を`true` に設定すると、既存の購入のみが更新され、新規購入は作成されません。<br>\- 配列型属性s をマップして、複数の購入アイテムを追加します。配列型の属性s は等しい長さでなければなりません。<br>\- 単一値属性を使用できます。単一値属性は各アイテムに適用されます。|
| 購買テンプレート | テンプレートを使用して、Brazeに送信する前にデータを変換できます。<br>\- ネストされたオブジェクトサポートが必要な場合は、購入テンプレートを定義します。<br>\- 購入テンプレートを定義すると、アクションの購入セクションで設定された設定は無視されます。<br>\- 詳細については、Tealiumの[テンプレートガイド](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)を参照してください。|
| 購買テンプレート変数 | 商品テンプレートの項目を入力します。詳細については、Tealiumの[テンプレート変数ガイド](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_example.png %})

{% endtab %}
{% tab Delete User - Non-Batch %}

このアクションでは、Braze ダッシュボードからユーザーを削除できます。

| パラメータ | 説明 |
| ---------- | ----------- |
| ユーザー ID | このフィールドを使用して、Tealium のユーザー ID フィールドを Braze の対応するフィールドにマッピングします。<br><br>\- 1 つ以上のユーザー ID 属性をマップします。複数のID が指定されている場合、最初の非ブランク値は、次の優先順位に基づいて選択されます。External ID、Braze ID、エイリアス名、エイリアスラベル。<br>\- ユーザーエイリアスを指定する場合、エイリアス名とエイリアスラベルの両方を設定する必要があります。<br><br>詳細については、Braze[`/users/delete` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_delete.png %})

選択したオプションを変更する場合は、**Back** を選択して編集するか、**Finish** を選択して完了します。

{% endtab %}
{% endtabs %}

**Continue**を選択します。

コネクターが Tealium ホームページのコネクターリストに表示されます。<br>![]({% image_buster /assets/img/tealium/summary_list.png %}){: style="max-width:80%;"}

完了したら、コネクタの [**保存 / 公開**] を選択してください。設定したアクションは、トリガー接続が満たされたときに実行されます。 

### ステップ3:Tealium コネクターをテストする

コネクターが稼動したら、正常に動作していることを確認するため、コネクターをテストする必要があります。これを検証する最も簡単な方法は、Tealium**トレースツール**を使用することです。Trace の使用を開始するには、Tealium Tools ブラウザー拡張機能が追加されていることを確認します。

1. 新しいトレースを開始するには、サイドバーの [**Server-Side**] のオプションから [**Trace**] を選択します。[**開始**] を選択し、トレース ID をキャプチャします。
2. ブラウザー拡張機能を開き、AudienceStream Trace にトレース ID を入力します。
3. リアルタイムログを調べます。
4. **Actions Triggered**エントリを選択して展開し、検証したいアクションをチェックする。
5. 検証するアクションを探して、ログステータスを表示します。 

Tealium の [Trace ツールの詳しい実装手順については、Tealium の [Trace ドキュメント](https://docs.tealium.com/server-side/connectors/trace/about/)を参照してください。

## 統合デモ

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 潜在データポイント 超過料金s

Tealiumを通じてBrazeを統合する際に、誤って不必要なデータポイントを記録してしまう可能性がある主な方法は3つある：

#### 重複データの送信- Brazeの属性の差分のみを送信します

Tealium はユーザー属性の Braze 差分を送信しません。たとえば、EventStream アクションでユーザーの名、メール、および携帯電話番号を追跡している場合、このアクションがトリガーされると、Tealium は3つの属性すべてを Braze に送信します。Tealium は、変更された内容や更新された内容を探してその情報のみを送信することはありません。

**解決策**:<br>バックエンドを確認して、属性が変更されているかどうかを評価し、変更されている場合は、Tealium の関連メソッドを呼び出してユーザープロファイルを更新できます。**これは、Braze を直接統合するユーザーが通常行う作業です。**<br>**または**<br> 自分自身のユーザープロファイルをバックエンドに保存しておらず、属性が変更されたかどうかを判断できない場合は、AudienceStream を使用して
[エンリッチメントを作成](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/) 値が変更されたときにのみユーザー 属性s を送信します。[エンリッチメントルール](https://docs.tealium.com/server-side-connectors/braze-connector/)に関する Tealium のドキュメントを参照してください。

#### 無関係なデータの送信またはデータの不必要な上書き

同じイベントフィードをターゲットとする複数のEventStreamsがある場合、**そのコネクタに対してイネーブルメントされたすべてのアクションは**、単一のアクションがトリガーされるたびに自動的に発火する。その結果、Brazeでデータが上書きされ、不必要なデータポイントが記録される可能性もある。

**解決策**:<br>それぞれのアクションを追跡するために、個別のイベント指定またはフィードを設定します。<br>**または**<br> Tealium ダッシュボードのトグルを使用して、起動しないアクション (またはコネクター) を無効にします。

#### Brazeの初期化が早すぎる

Braze Web SDK タグを使用して Tealium と統合するユーザーの場合、MAU が大幅に増加する可能性があります。**Braze がページ読み込むで初期化されている場合、Web ユーザーが初めてWeb サイトに移動するたびに、Braze によって匿名プロファイルが作成されます。**ユーザーが"Signed In"または"Watched Video"など、いくつかのアクションを完了したときにのみ、MAU数を減らすためにユーザーの挙動を追跡することを望む人もいるかもしれません。

**解決策**:<br>[ 読み込む規則](https://docs.tealium.com/iq-tag-management/load-rules/about/) を設定して、タグ 読み込むがいつどこにあるかを正確に判断します。 

