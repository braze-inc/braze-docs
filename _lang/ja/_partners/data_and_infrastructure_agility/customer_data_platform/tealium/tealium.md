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

> [Tealium](https://tealium.com/) は、EventStream、AudienceStream、およびiQ Tag Management で構成されるユニバーサルデータハブおよび顧客データプラットフォームで、サードパーティのソースからモバイル、ウェブ、および代替データを接続できます。Tealium と Braze を接続すると、カスタムイベント s、ユーザー 属性、および購入のデータフローが可能になり、リアルタイムでデータを操作できるようになります。

![さまざまなTealiumプロダクトとBraze プラットフォームを組み合わせてリアルタイムでクロスチャネルの キャンペーンs を有効にする方法を示すTealium図です。][22]{: style="border:0;"}

BrazeとTealiumインテグレーションを使用すると、ユーザーを追跡し、さまざまなユーザー 分析プロバイダーにデータをルーティングできます。Tealiumでは次の操作ができます。
- Tealium オーディエンス s を[オーディエンスStream]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_audience_stream/) と同期し、Braze キャンペーンとキャンバスのパーソナライズまたはSegments の構築に使用するためにBrazeします。
- [プラットフォーム間のデータインポート](#choose-your-integration-type)。Braze は、Android、iOS、およびWeb アプリの各アプリケーションに[並列](#side-by-side-sdk-integration)SDKインテグレーションと、イベントデータにレポートできる任意のプラットフォーム内で使用できる[server-to-server](#server-to-server-integration)インテグレーションの両方を提供します。<br><br>

{% tabs %}
{% tab EventStream %}
Tealium EventStream は、データセンターに配置されるデータ収集およびAPI ハブです。EventStream は、セットアップとインストールから、受信ユーザーデータの識別、検証、および拡張まで、データサプライチェーン全体を処理します。EventStream は、イベントフィードs およびコネクターでリアルタイムのアクションを実行します。以下は、[EventStream](https://docs.tealium.com/server-side/getting-started/eventstream-api-hub/introduction/)を構成する機能です。
- データソース(設置とデータ収集)
- ライブイベント(リアルタイムデータ検査)
- イベント仕様と属性s(データレイヤー要件と検証)
- イベントフィードs (フィルターのイベントタイプ)
- イベントコネクター(API ハブアクションs)

{% endtab %}
{% tab オーディエンスストリーム %}

Tealium AudienceStreamはオムニチャネル 顧客 セグメンテーションでリアルタイムのアクションエンジンです。AudienceStream は、EventStream に流れるデータを取得し、ブランドとの顧客のエンゲージメントの最も大切な属性を表すビジタープロファイルs を作成します。設定ステップについては、[AudienceStream]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_audience_stream/)を参照してください。

{% endtab %}
{% tab iQタグ管理 %}
Tealium iQ では、トリガー コードをアプリ s で使用することができます。これには、Tealium iQ タグマネジメントユーザーインターフェイスのタグを使用します。このタグでは、モバイルおよびウェブプラットフォームs からイベントデータを収集、コントロール、配信します。これにより、アプリs にBraze固有のコードを追加することなく、ネイティブのBraze インプリメンテーションを設定できます。ユーザは、iQ タグ管理またはJSON 設定ファイルを介してモバイルリモートコマンドを統合することができます(推奨Tealium アプリ到達)。Braze Web SDKを使用するユーザは、Web iQ タグを使用して統合する必要があります。

各メソッドの長所と短所について詳しくは、以下の[ Tealium iQ タグ マネージャー](#mobile-remote-commands) を参照してください。
{% endtab %}
{% endtabs %}

{% alert important %}
Tealium は、バッチコネクタと非バッチコネクタの両方のアクションを提供します。ユースケースにとってリアルタイムのリクエストが大切で、BrazeのAPI レート制限スペックを打つ心配がない場合は、非バッチコネクターを使用する必要があります。不明な点がある場合は、Brazeサポートまたは顧客のサクセスマネージャーにお問い合わせください。<br><br>

バッチ・コネクターの場合、要求は、以下のいずれかのしきい値が満たされるまでキューに入れられます。<br><br>
- 最大リクエスト数:75
- 最も古いリクエストからの最大時間:10分
- 要求の最大サイズ1 MB

Tealium では、同意イベント(サブスクリプション環境設定)またはユーザー削除イベントはデフォルトで一括処理されません。
{% endalert %}

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| Tealium勘定 | この提携を進めるには、サーバーおよび/またはクライアントサイドアクセスを持つ[Tealiumアカウント](https://my.tealiumiq.com/)が必要です。 | 
| インストール元とTealium元[ライブラリ](https://docs.tealium.com/platforms/) | モバイルアプリs、Web サイトs、バックエンドサーバなど、Tealiumに送信されるデータの送信元。<br><br>Tealiumコネクターを正しく設定するには、ライブラリーをアプリ、現場、またはサーバーにインストールする必要があります。 |
| Braze RESTとSDKエンドポイント | RESTまたはSDKエンドポイント。エンドポイントは、インスタンス の[ Braze URL によって異なります。 |
| Braze アプリ 識別子鍵(横並びのみ) | アプリ 識別子ボタン。<br><br>これは、** Braze Dashboard > Manage Settings > API Key** にあります。 |
| コードバージョン(並列のみ) | SDK 版に対応し、major.minor 形式である必要があります(3.0.1 ではなく3.2 など)。コード版は、3.0以上にしてください。 |
| REST API キー(サーバ間のみ) | `users.track` および`users.delete` 権限を持つBraze REST API キー。<br><br>これは、** Braze Dashboard > Developer Console > REST API Key > Create New API Key** 内で作成できます。|
{: .reset-td-br-1 .reset-td-br-2}

## 統合タイプを選択する

| 統合 | 詳細 |
| ----------- | ------- |
| [横並び](#side-by-side-sdk-integration) | Tealium のSDKを使用して、イベントをBrazeのネイティブコールに変換し、サーバー間の統合よりも深い機能とBrazeの包括的な使用を可能にします。<br><br>Brazeのリモートコマンドを使用する場合は、TealiumがすべてのBraze方法(コンテンツカードなど)に対応しているわけではないことに注意してください。対応するリモートコマンドでアプリされていないBrazeメソッドを使用するには、ネイティブBraze コードをコードベースに追加してメソッドを呼び出す必要があります。|
| [サーバ間](#server-to-server-integration) | Tealium からBraze のREST API エンドポイントに転送します。<br><br>アプリ メッセージング内、コンテンツカード、プッシュ通知などのBrazeのユーザーインターフェイス機能には対応していません。また、このメソッドでは使用できない、デバイスレベルのフィールドs などの自動的にキャプチャされるデータもあります。<br><br>これらの機能を使用する場合は、並列統合を検討してください。|
{: .reset-td-br-1 .reset-td-br-2}

## サイドバイサイドSDKインテグレーション

### リモートコマンド

リモートコマンドは、Tealium iOS およびAndroid ライブラリの機能であり、Braze Server からBraze へTealium SDKからの呼び出しを可能にします。Braze リモートコマンドモジュールは、必要なBrazeライブラリを自動的にインストールして構築し、すべてのメッセージレンダリングと分析 "トラッキングを処理します。Braze モバイルリモートコマンドを使用するには、アプリs にインストールされているTealium ライブラリが必要です。

Tealium には、モバイルリモートコマンドを統合する2 つの方法があります。統合タイプ間で機能が失われることはなく、基礎となるネイティブコードは同じです。

| モバイルリモートコマンド方式 | 利点 | 連結 |
| --- | --- | --- |
| **リモート指令タグ** | Tealium iQ UI を使用して、リモートコマンドに送信されるm アプリの内容やデータを簡単に変更できます。<br><br>これにより、アプリがすでにアプリストアに入った後、クライアントがアプリを更新する必要なく、追加のデータまたはイベントをサードパーティSDKに送信できます。 | アプリのタグマネジメントモジュールは、非表示のWeb ビューに依存してJavaScript を処理します。 |
| **JSON構成ファイル**<br>([推奨](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#how-it-works)) | JSONメソッドを使用すると、アプリで非表示のWebビューを使用する必要がなくなり、メモリー使用量が大幅に削減されます。<br><br>JSON ファイルは、顧客のアプリ内でリモートまたはローカルにホストできます。 | 現時点では、これを管理するUIがないため、少し手間がかかります。<br><br>注:Tealiumは、この問題を解決し、iQタグマネジメントバージョンと同じレベルの柔軟性をJSONリモートコマンドにもたらすマネジメントUIの追加に取り組んでいます |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Braze モバイルリモートコマンドデータm アプリ ings を使用して、デフォルト ユーザー 属性s とカスタム属性s を設定し、購買とカスタムイベントs を追跡します。対応するBraze方法については、次の表を参照してください。

| リモートコマンド | Braze法 |
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

Braze モバイルリモートコマンドの設定方法の詳細と、サポートされている方法の概要については、Tealium 開発者 ドキュメントを参照してください。
- [リモートコマンド](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#json-template)
- [リモート指令タグ](https://docs.tealium.com/client-side-tags/braze-mobile-remote-command-tag/)

{% alert important %}
Brazeのモバイルリモートコマンドは、すべてのBraze方法やメッセージング チャネル(コンテンツカードなど)に対応しているわけではありません。対応するリモートコマンドでアプリされていないBrazeメソッドを使用するには、ネイティブBraze コードをコードベースに追加して、そのメソッドを直接的に呼び出す必要があります。
{% endalert%}

### Braze Web SDK タグ

Braze Web SDKタグを使用して、BrazeのWeb SDKをWeb サイトにデプロイします。[ Tealium iQ タグ Management](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/) では、顧客 s がビジターのアクティビティを追跡するタグとしてBrazeをTealium ダッシュボード内に追加できます。通常、タグは、オンライン広告、メール マーケティング、およびサイトパーソナライゼーションの有効性を理解するためにマーケターs によって使用されます。

1. Tealium で、**iQ > Tags > + Add Tag > Braze Web SDK** に移動します。
2. Tag Configuration ダイアログボックスで、API Key (Braze アプリ 識別子鍵)、Base URL (Braze SDKエンドポイント)、および[Braze Web SDK コードバージョン](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) を入力します。また、ログを有効にして、デバッグ目的で Web Console に情報を記録することもできます。
3. [ 読み込む Rules](https://docs.tealium.com/iq-tag-management/load-rules/about/) ダイアログボックスで、" All Pages&quot を読み込むするか、**Create Rule** を選択して、いつ、どこでこのタグのインスタンスをサイトに読み込むするかを決定します。
4. **[Data Mアプリings](https://docs.tealium.com/iq-tag-management/data-mappings/about/)**ダイアログボックスで、**Create Mアプリings**を選択してTealiumデータをBrazeにマッピングします。Braze Web SDK タグの送信先は、タグの**Data Mアプリing**タブに組み込まれています。[以下のテーブル](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)は、使用可能な送信先カテゴリを一覧表示し、それぞれの送信先の名前を説明します。
5. **Finish**を選択します。

### サイドバイサイドの統合リソース

- iOS リモートコマンド:[Tealium ドキュメント](https://docs.tealium.com/platforms/remote-commands/integrations/braze/),[Tealium GitHub リポジトリ](https://github.com/Tealium/tealium-ios-braze-remote-command)
- Androidリモートコマンド:[Tealium ドキュメント](https://docs.tealium.com/platforms/remote-commands/integrations/braze/),[Tealium GitHub リポジトリ](https://github.com/Tealium/tealium-android-braze-remote-command)
- Web SDK タグ:[Tealium ドキュメント](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)

## サーバー間統合

このインテグレーションでは、Tealium からBraze REST にデータが転送されます。

サーバー間統合では、アプリ メッセージング、コンテンツカード、またはプッシュ通知などのBraze UI 機能は使用できません。また、このメソッドでは使用できない、自動的にキャプチャされるデータ(デバイスレベルのフィールドなど) もあります。

このデータとこれらの機能を使用する場合は、[並列]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium/#side-by-side-sdk-integration)SDKインテグレーションを検討してください。

### ステップ1:ソースの設定

Tealiumでは、まずコネクターの有効なデータソースを設定する必要があります。
1. **Server-Side** のTealiumのサイドバーから、**Sources > Data Sources > + Add Data Source** に移動します。
2. 使用可能なカテゴリ内で目的のプラットフォームを見つけ、送信元に名前を付けます。これは必須のフィールドです。<br>![][6]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
3. **Event Specifications**オプションから、含める[イベント仕様](https://docs.tealium.com/server-side/event-specifications/about/)を選択します。イベントの指定は、イベントの名前とインストールで追跡するために必要な属性を特定するのに役立ちます。これらの指定は、アプリ受信事象に依存します。<br>![][7]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>あなたにとって最も価値のあるデータと、あなたのユースケースにとって最もアプリ適切と思われる仕様について、少し時間をかけて考えてみましょう。\[カスタムイベント仕様][19]も利用可能です。]<br>
4. 次に、**Get Code**ステップに進みます。ここに記載されている基本コードと行動"トラッキング コードは、インストールガイドとして機能します。これらの指示を共有したい場合は、提供されたPDF を読み込むします。**Save & Continue**を選択します。<br>
5. 保存したソースを表示したり、イベントスペックを追加または削除したりできます。<br>![][18]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>詳細なデータソースビューから、次のアクションを実行できます。
- データソース鍵の表示と複製
- インストール手順の表示
- **Get Code**ページに戻る
- イベント仕様の追加または削除
- イベント仕様に関連するライブイベントを表示するために移動します
- さらに・・・<br>
6. 最後に、ページの上部にある**Save / Publish**を選択します。送信元を公開しないと、Braze コネクターの設定時に見つかりません。

データソースの設定と編集の詳細については、[データソース s](https://docs.tealium.com/server-side/data-sources/about-data-sources/)を参照してください。

### ステップ2:イベント・コネクターの作成

コネクターは、Tealiumと、データ通信に使用される別のベンダーとの間のインテグレーションです。これらのコネクターには、パートナーがサポートするAPI を表すアクションが含まれています。 

1. **Server-Side** のTealiumのサイドバーから、**EventStream > Event Connectors** に移動します。
2. 青色の**\+ Add Connector** ボタンを選択して、コネクター市場を調べます。アプリが耳にする新しいダイアログボックスで、スポットライト検索を使用して**Braze** コネクターを見つけます。
3. このコネクターを追加するには、**Braze**コネクタータイルを選択します。クリックすると、接続の概要と、必要な情報、サポートされるアクション、および設定手順の一覧が表示されます。構成は、送信元、構成、およびアクションの3 つのステップで構成されます。

#### ソース

ソースが設定されたら、**EventStream > Event Connectors > + Add Connector > Braze** のBraze コネクターページに戻ります。 

開封が作成したデータソースを選択し、**Event Feed**で**All Events**または特定のイベント仕様を選択して、変更された値のみをBrazeに送信する推奨パスを選択します。**Continue**をクリックします。

#### 構成

次に、ページの下部で**Add Connector** を選択します。コネクターに名前を付け、Braze API エンドポイントとBraze REST API キーを指定します。

![][15]{: style="max-width:70%;"}

以前にコネクタを作成した場合は、オプションとして、使用可能なコネクタリストから既存のコネクタを使用し、必要に応じて鉛筆アイコンで修正するか、ごみ箱アイコンで削除できます。 

#### アクション (Action)

次に、コネクター・アクションに名前を付け、構成するmアプリに従って送信するアクションの種類を選択します。ここでは、Braze 属性s、行動、および購入をTealium 属性、行動、および購入の名前にマッピングします。

{% alert important %}
提供されるすべてのフィールドが必要なわけではありません。

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs ローカル %}
{% tab トラックユーザー(バッチおよび非バッチ) %}

このアクションでは、1つのアクションでユーザー、行動、購買属性をすべて追跡できます。

| パラメータ | 説明 |
| ---------- | ----------- |
| ユーザー ID | このフィールドを使用して、Tealium ユーザー ID フィールドを同等のBrazeにマップします。1 つ以上のユーザー ID 属性をマップします。複数のID が指定されている場合、最初の非ブランク値は、次の優先順位に基づいて選択されます。外部ID、Braze ID、別名、および別名ラベル。<br><br>\- プッシュトークンs をインポートする場合は、外部ID とBraze ID を指定しないでください。<br>\- ユーザー別名を指定する場合は、別名と別名を設定する必要があります。<br><br>詳細については、Braze[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) を参照してください。 |
| ユーザ属性 | Braze のユーザープロファイル フィールドネームを使用してBraze ダッシュボードに更新 ユーザープロファイルするか、独自のカスタム[ユーザー 属性]({{site.baseurl}}/api/objects_filters/user_attributes_object/) をユーザープロファイルs に追加します。<br><br>\- デフォルトでは、新しいユーザーs は存在しない場合に作成されます。<br>\- 設定では、** 更新 Existing Only** to `true` で、存在するユーザーs のみが更新d になり、新しいユーザーは作成されません。<br>\- Tealium 属性が空の場合は、NULL に変換され、Braze ユーザープロファイルから削除されます。ヌル値をBrazeに送信してユーザー 属性を削除しない場合は、エンリッチメントを使用する必要があります。 |
| ユーザー 属性の変更s | このフィールドを使用して、特定のユーザー 属性を増減します<br><br>\- 整数属性s は正または負の整数でインクリメントできます。<br>\- 配列属性s は、既存の配列に数値を追加または削除することで修正できます。 |
| イベント | イベントは、タイムスタンプでの特定のユーザーによるカスタムイベントの単一オカレンスを表します。このフィールドを使用して、Braze[event object]({{site.baseurl}}/api/objects_filters/event_object/) のようなイベント属性s を追跡およびマップします。<br><br>\- イベント属性`Name` は、m アプリの各イベントに必要です。<br>\- イベント属性`Time` は、明示的にm がアプリしない限り、自動的に現在に設定されます。<br>\- デフォルトでは、新しいイベントは存在しない場合に作成されます。設定では、`Update Existing Only` から`true` までは、既存のイベントのみが更新d になり、新しいイベントは作成されません。<br>\- 配列型属性s をマップして、複数のイベントを追加します。配列型の属性s は等しい長さでなければなりません。<br>\- 単一の属性s を使用し、それぞれの事象にアプリを置くことができます。 |
| 事象テンプレート | ボディデータで参照するイベントテンプレートを指定します。テンプレートを使用してデータを変換してから、Brazeに送信できます。詳細については、Tealiumの[テンプレートガイド](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)を参照してください。 |
| 事象テンプレート | データインプットとして事象テンプレートを提供する。詳細については、Tealiumの[テンプレート変数ガイド](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)を参照してください。 |
| 購入 | このフィールドを使用して、Braze[purchase object]({{site.baseurl}}/api/objects_filters/purchase_object/) のようにユーザーの購買属性s を追跡およびマップします。<br><br>\- 購入属性s `Product ID`、`Currency`、および`Price` は、購入するm アプリごとに必要です。<br>\- 購入属性`Time` は、明示的にm がアプリされない限り、自動的に現在に設定されます。<br>\- デフォルトでは、新規購入は存在しない場合に作成されます。設定では、`Update Existing Only` から`true` までは、既購入分のみが更新 d となり、新規購入分は作成されません。<br>\- 配列型属性s をマップして、複数の購入アイテムを追加します。配列型の属性s は等しい長さでなければなりません。<br>\- 1つの数値属性sを使うことができ、それぞれの項目にアプリします。|
| 購買テンプレート | テンプレートを使用して、Brazeに送信する前にデータを変換できます。<br>\- ネストされたオブジェクトサポートが必要な場合は、購入テンプレートを定義します。<br>\- 購入テンプレートが定義されている場合、アクションの購入セクションで設定された設定は無視されます。<br>\- 詳細については、Tealiumの[テンプレートガイド](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)を参照してください。|
| 購買テンプレート変数 | 商品テンプレートの項目を入力します。詳細については、Tealiumの[テンプレート変数ガイド](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2}

![]({% image_buster /assets/img/tealium/track_user_example.png %})

{% endtab %}
{% tab ユーザーの削除(非バッチ) %}

このアクションでは、Braze ダッシュボードからユーザーs を消去できます。

| パラメータ | 説明 |
| ---------- | ----------- |
| ユーザー ID | このフィールドを使用して、TealiumのユーザID フィールドをBraze同等のものにマップします。<br><br>\- 1 つ以上のユーザー ID 属性をマップします。複数のID が指定されている場合、最初の非ブランク値は、次の優先順位に基づいて選択されます。外部ID、Braze ID、別名、および別名ラベル。<br>\- ユーザー別名を指定する場合は、別名と別名ラベルの両方を設定する必要があります。<br><br>詳細については、Braze[`/users/delete` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2}

![]({% image_buster /assets/img/tealium/track_user_delete.png %})

選択したオプションを変更する場合は、**Back** を選択して編集するか、**Finish** を選択して完了します。

{% endtab %}
{% endtabs %}

**Continue**を選択します。

コネクターがTealiumのホームページのコネクターの一覧に表示されるようになりました。<br>![][13]{: style="max-width:80%;"}

終了したら、必ず**Save / Publish**コネクタを使用してください。設定したアクションは、トリガーコネクションが満たされると起動します。 

### ステップ3:Tealiumコネクターのテスト

コネクタが起動して実行されたら、正しく動作することをテストする必要があります。これを検証する最も簡単な方法は、Tealium**トレースツール**を使用することです。トレースの使用を開始するには、Tealium ツールブラウザ拡張を追加したことを確認します。

1. 新しいトレースを開始するには、**Server-Side** オプションの下のサイドバーで**Trace** を選択します。**Start**をクリックし、Trace ID をキャプチャします。
2. ブラウザ拡張を開き、AudienceStream Trace にTrace ID を入力します。
3. リアルタイムログを調べます。
4. **アクション s Triggered** エントリをクリックして、検証するアクションを確認します。
5. 検証するアクションを探して、ログステータスを表示します。 

Tealium のトレースツールの実装に関する詳細な手順については、Tealium の\[トレースドキュメント][21] を参照してください。

## 統合デモ

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 潜在データポイント 超過料金s

Tealium を介してBrazeを統合するときに、誤ってデータ超過料金s を操作する可能性がある主な方法は3 つあります。

#### 重複データの送信- Brazeの属性の差分のみを送信します
Tealium は、ユーザー 属性s のBrazeの差分を送信しません。たとえば、EventStream アクションでユーザーの名、メール、および携帯電話番号を追跡している場合、アクションがトリガーされると、Tealium は3 つの属性すべてをBraze に送信します。Tealiumは、変更されたものや更新されたものを探し、その情報のみを送信しません。<br><br> 
**解決策**:<br>バックエンドを確認して、属性が変更されているかどうかを評価し、変更されている場合は、Tealium の関連メソッドを呼び出してユーザープロファイルを更新できます。**これは、Brazeを直接的に統合するユーザーが通常行うことである。**<br>**または**<br> 自分のバージョンのユーザープロファイルをバックエンドに保存せず、属性が変更されたかどうかを判断できない場合は、AudienceStream を使用できます
[エンリッチメントを作成](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/) 値が変更されたときにのみユーザー 属性s を送信します。[エンリッチメントルール](https://docs.tealium.com/server-side-connectors/braze-connector/)に関するTealiumのドキュメントを参照してください。

#### 無関係なデータの送信またはデータの不必要な上書き
同じイベントフィードをターゲットとする複数のEventStreams がある場合、そのコネクタ で有効になっているすべてのアクションは、1 つのアクションがトリガーされるたびに自動的に起動されます。**これにより、Brazeでデータが上書きされ、不必要なデータポイントを消費することもあります。**<br><br>
**解決策**:<br>それぞれのアクションを追跡するために、個別のイベント指定またはフィードを設定します。<br>**または**<br> Tealium ダッシュボードのトグルを使用して、起動しないアクション(またはコネクター)を無効にします。

#### Brazeの初期化が早すぎる
Braze Web SDK タグ を使用してTealium と統合すると、MAU が大幅に増えることがあります。**Braze がページ読み込むで初期化されている場合、Web ユーザーが初めてWeb サイトに移動するたびに、Braze によって匿名プロファイルが作成されます。**ユーザーが"Signed In"または"Watched Video"など、いくつかのアクションを完了したときにのみ、MAU数を減らすためにユーザーの挙動を追跡することを望む人もいるかもしれません。<br><br>
**解決策**:<br>[ 読み込む規則](https://docs.tealium.com/iq-tag-management/load-rules/about/) を設定して、タグ 読み込むがいつどこにあるかを正確に判断します。 

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
