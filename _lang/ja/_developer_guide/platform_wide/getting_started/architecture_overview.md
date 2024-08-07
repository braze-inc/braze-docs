---
nav_title: アーキテクチャの概要
article_title: アーキテクチャの概要
page_order: 3
description: "この記事では、Brazeテクノロジースタックのさまざまな部分と部分について、関連する記事へのリンクとともに説明します。"
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

# 開始:アーキテクチャの概要

> この記事では、Brazeテクノロジースタックのさまざまな部分と部分について、関連する記事へのリンクとともに説明します。 

大まかに言うと、Brazeはデータに関するものです。Brazeプラットフォームは、SDK、REST API、およびパートナー統合により、データを集約して操作できます。 

![ろう付けにはさまざまな層があります。合計で、SDK、API、ダッシュボード、およびパートナー統合で構成されています。これらはそれぞれ、データ インジェスト レイヤー、分類レイヤー、オーケストレーション レイヤー、パーソナライゼーション レイヤー、およびアクション レイヤーの部分に貢献します。アクションレイヤーには、プッシュ、アプリ内メッセージ、接続済みカタログ、Webhook、SMS、メールなど、さまざまなチャネルがあります。[1]{: style="display:block;margin:auto;" }

* [データ インジェスト](#ingestion):Brazeは、さまざまなソースからデータを取り込んでいます。
* [分類](#classification):マーケティングチームは、これらの指標を使用してユーザーベースを動的にセグメント化します。 
* [オーケストレーション](#orchestration)Brazeは、さまざまなオーディエンスセグメントへのメッセージを理想的なタイミングでインテリジェントに調整します。
* [アクション](#action):マーケティングチームはデータに基づいて行動し、SMSやメールなどのさまざまなメッセージングチャネルを通じてコンテンツを作成します。
* [パーソナライゼーション](#personalization):データは、オーディエンスに関するパーソナライズされた情報でリアルタイムに変換されます。 
* [エクスポート](#exporting-data):次に、Brazeは、このメッセージに対するユーザーのエンゲージメントを追跡し、プラットフォームにフィードバックしてループを作成します。このデータは、リアルタイムのレポートと分析を通じて分析情報を得ることができます。

これらすべてが連携して、ユーザーベースとブランドの間のインタラクションを成功させ、目標を達成することができます。Brazeは、これらすべてを、垂直統合スタックと呼ぶもののコンテキストで行います。各レイヤーを 1 つずつ掘り下げてみましょう。

## データ インジェスト {#ingestion}

Brazeは、Snowflake、Kafka、MongoDB、Redisを活用したストリーミングデータアーキテクチャ上に構築されています。多くのソースからのデータは、SDKとAPIを介してBrazeにロードできます。このプラットフォームは、データの入れ子や構造に関係なく、あらゆるデータをリアルタイムで処理できます。Brazeのデータはユーザープロファイルに保存されます。 

{% alert tip %}
Brazeは、ユーザーが匿名である時点から、アプリにログインして認識されるまで、ユーザーのジャーニー全体を通じてデータを追跡できます。Brazeではsと呼ばれる `external_id`ユーザーIDは、ユーザーごとに設定する必要があります。これらは、ユーザーがアプリを開いたときに変更されず、アクセス可能であり、デバイスやプラットフォーム間でユーザーを追跡できるようにする必要があります。ベスト プラクティスについては、 [ユーザー ライフサイクルに関する記事]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/) を参照してください。
{% endalert %}

![Brazeは、APIからバックエンドデータソースを、SDKからフロントエンドデータソースを、Braze Cloud Data Ingestionからデータウェアハウスデータをインポートし、パートナー統合からインポートします。このデータはBraze APIを介してエクスポートされます[3]{: style="display:block;margin:auto;" }

{% alert note %}
この個人中心のユーザープロファイルデータベースにより、リアルタイムでインタラクティブな速度が可能になります。Brazeは、データが到着すると値を事前に計算し、その結果を軽量なドキュメント形式で保存して、高速に検索できるようにします。また、このプラットフォームはこのようにゼロから設計されているため、ほとんどのメッセージングのユースケース、特にコネクテッドコンテンツ、製品カタログ、ネストされた属性などの他のデータコンセプトと組み合わせて理想的です。
{% endalert %}

### Braze API経由のバックエンドデータソース
Brazeは、ユーザーデータベース、オフライントランザクション、データウェアハウスから[REST API][4]を介してデータを引き出すことができます。 

### Braze SDK経由のフロントエンドデータソース
Brazeは、[Braze SDK][5]を介して、ユーザーのデバイスなどのフロントエンドデータソースからファーストパーティデータを自動的に取得します。SDKは、新しい(匿名)ユーザーを処理し、ライフサイクル全体を通じてユーザープロファイルのデータを管理します。 

### パートナー連携：
Brazeには150社以上の技術パートナーがおり、私たちはこれを「Alloys」と呼んでいます。 [相互運用可能なテクノロジーとデータ API] の有意義で堅牢なネットワークを通じて、データ フィードを補完できます。[6] 

### Braze Cloud Data Ingestionによる倉庫への直接接続
[Braze Cloud Data Ingestion][7]により、わずか数分でデータウェアハウスからプラットフォームに顧客データをストリーミングし、関連するユーザー属性、イベント、購入を同期できます。Cloud Data Ingestion インテグレーションは、ネストされた JSON やオブジェクトの配列など、複雑なデータ構造をサポートします。

Cloud Data Ingestion は、Snowflake、Amazon Redshift、Databricks、Google BigQuery のデータを同期できます。

## 分類 {#classification}
分類レイヤーを使用すると、チームは Braze を通過するデータに基づいて、[セグメント][8] と呼ばれるオーディエンスを動的に分類して構築できます。 

{% alert note %}
分類、オーケストレーション、パーソナライゼーションの各レイヤーは、マーケティングチームが作業の多くを行う場所です。これらのレイヤーとのインターフェースは、ほとんどの場合、当社のWebインターフェースであるBrazeダッシュボードを介して行われます。開発者は、これらのレイヤーの設定とカスタマイズを行う役割を担っています。
{% endalert %}

名前、メールアドレス、生年月日、国など、多くの一般的なタイプのユーザー属性は、デフォルトでSDKによって自動的に追跡されます。開発者は、チームと協力して、ユースケースで追跡するのが理にかなっている追加のカスタムデータを定義します。カスタムデータは、ユーザーベースの分類とセグメント化の方法に影響を与えます。このデータ モデルは、実装プロセス中に設定します。 

[自動的に収集されるデータとカスタムデータ][9]の詳細をご覧ください。

## オーケストレーション {#orchestration}
オーケストレーションレイヤーを使用すると、マーケティングチームはユーザーデータと以前のエンゲージメントに基づいてユーザージャーニーを設計できます。この作業は主にダッシュボードインターフェイスを介して行われますが、[APIを介してキャンペーン][10]を開始するオプションもあります。例えば、マーケターがダッシュボードでデザインしたメッセージやキャンペーンをいつ送信するかをバックエンドからBrazeに伝え、バックエンドのロジックに従ってトリガーすることができます。API によってトリガーされるメッセージの例としては、パスワードのリセットや配送の確認などがあります。 

{% alert note %}
APIトリガーキャンペーンは、より高度なトランザクションのユースケースに最適です。これにより、マーケターはキャンペーンコピー、多変量テスト、再適格性ルールをBrazeダッシュボード内で管理しながら、サーバーやシステムからコンテンツの配信をトリガーできます。メッセージをトリガーする API リクエストには、メッセージにリアルタイムでテンプレート化する追加データを含めることもできます。
{% endalert %}


### フィーチャーフラグ
Brazeでは、[feature flags][12]を通じて、選択したユーザーの機能をリモートで有効または無効にすることができます。これにより、マーケターは、まだオーディエンス全体に展開していない機能のメッセージングで、ユーザーベースの適切なセグメントをターゲットにすることができます。しかし、それ以上に、機能フラグを使用して、追加のコードデプロイやアプリストアの更新なしで、本番環境で機能のオンとオフを切り替えることができます。これにより、自信を持って新機能を安全に展開できます。

## パーソナル 化 {#personalization}
パーソナライゼーションレイヤーは、メッセージで動的コンテンツを配信する機能を表します。広く使用されているパーソナライゼーション言語であるLiquidを使用することで、チームは既存のデータを動的に取り込み、各受信者に合わせたメッセージを表示できます。さらに、[接続コンテンツ][11]を使用して、プッシュ通知やメールなど、送信するメッセージにWebサーバーまたはAPI経由でアクセス可能な情報を直接挿入できます。コネクテッドコンテンツはLiquid上に構築され、使い慣れた構文を使用します。

また、この動的コンテンツはプログラム可能であるため、マーケティング担当者は計算値、他のコールからの応答、または製品カタログアイテムを含めることができます。実装時にこれらのシステムをセットアップすると、マーケティングチームは技術チームからのサポートをほとんどまたはまったく受けずにこれを行うことができます。 

## アクション {#action}
アクションレイヤーは、ユーザーへの実際のメッセージングを可能にします。アクションレイヤーの目的は、前述のすべてのレイヤーで利用可能なデータに基づいて、適切なメッセージを適切なユーザーに適切なタイミングで送信することです。メッセージングは、アプリやサイト内(アプリ内メッセージの送信、コンテンツカードカルーセルやバナーなどのグラフィック要素など)またはアプリエクスペリエンスの外部(プッシュ通知やメールの送信など)で行われます。

### メッセージングチャネル
Brazeは、チャネルにとらわれないユーザー中心のデータモデルにより、進化する技術環境に対応するように設計されています。ダッシュボードは、メッセージ配信とトランザクショントリガーを管理します。たとえば、マーケターは、ユーザーがこの場所の近くに設定されたジオフェンスに入ったときに、新しくオープンした店舗の 1 つのクーポンを提供する SMS メッセージをトリガーしたり、お気に入りの番組が新しいシーズンになったことをユーザーにメールで知らせたりすることができます。

[Braze SDK][5]は、プッシュ、アプリ内メッセージ、コンテンツカードなど、追加のメッセージングチャネルを強化します。SDKをアプリやサイトに統合すると、マーケティングチームはBrazeダッシュボードを使用して、サポートされているすべてのメッセージングチャネルでキャンペーンを調整できます。

![][13]

## データのエクスポート
重要なのは、Brazeとのすべてのエンドユーザーとのやり取りが追跡されるため、エンゲージメントとアウトリーチを測定できることです。また、Brazeがこれらすべてのソースからデータを集約すると、さまざまなツールを使用して技術スタックにエクスポートし、ループを閉じることができます。

### Currents
[現在][14] はオプションの Braze アドオンで、スタックの他の宛先に継続的にフィードするきめ細かなストリーミングエクスポートを提供します。Currents は、ユーザーごとのイベントごとの生データフィードで、5 分ごと、または 15,000 イベントごとのいずれか早い方でデータをエクスポートします。Currents のダウンストリーム宛先の例としては、Segment、S3、Redshift、Mixpanel などがあります。 

### Snowflakeデータ共有
Snowflakeの[Secure Data Sharing][15]機能により、Brazeは、一般的なデータプロバイダーとの関係に伴うワークフローの摩擦、障害点、不要なコストを心配することなく、Snowflakeポータル上のデータへの安全なアクセスを提供することができます。すべての共有は、Snowflake独自のサービスレイヤーとメタデータストアを介して行われ、アカウント間で実際にデータがコピーまたは転送されることはありません。共有データはコンシューマーアカウントのストレージを占有しないため、毎月のデータストレージ料金に寄与しないため、これは重要な概念です。コンシューマーに課金されるのは、共有データのクエリに使用されるコンピューティング リソース (つまり、仮想ウェアハウス) に対する料金のみです。

### Braze エクスポート API
Braze APIは、集計分析をプログラムでエクスポートしたり、個々のユーザーデータをエクスポートしたりできる[エンドポイント][16]を提供します。このデータは、任意のサイズのオーディエンスとセグメントに対してエクスポートできます。 

### CSV (英語)
最後に、集計レベルのデータをダッシュボードから直接 [CSV][17] としてダウンロードするオプションがあります。CSVオプションを使用すると、チームメンバーはBrazeからデータを簡単にエクスポートできます。

{% alert tip %}
CSV エクスポートの基本制限は 500,000 行ですが、API にはこの点に関する制限はありません。
{% endalert %}

## すべてをまとめる 
ユーザーの 1 人 (仮に Mel と呼ぶことにします) が、製品に関するお知らせを受け取りました。舞台裏では、Brazeプラットフォームのすべてのレイヤーが連携して、このプロセスがスムーズに進むようにしました。 

Melの情報は、CSVインポートにより、従来の顧客エンゲージメントプラットフォームからBrazeに取り込まれました。統合後、Mel がアプリを操作するたびに、顧客プロファイルにデータが追加されました。 

製品に関するお知らせは、アプリで類似のアイテムを気に入ったすべてのユーザーに送信されました。このデータをカスタムイベントとして定義しました。SDKはこのイベントを追跡し、それに応じてユーザーベースをセグメント化しました。Braze は、このアナウンスを送信するのに最適な時間帯を調整し、メルを好みの名前で呼ぶことでアナウンスをパーソナライズしました。 

メルがお知らせを開くと、メルは新製品をウィッシュリストに追加します。Braze は、彼女がメールを自動的にクリックしたことを追跡します。SDK は、彼女が新製品をウィッシュリストに登録したことを追跡します。ユーザーがあなたのブランドと関わるたびに、あなたとあなたのユーザーはお互いについてより深く知ることができます。

![][18]



[1]: {% image_buster /assets/img/getting-started/braze_listen_understand_act.png %}
[3]: {% image_buster /assets/img/getting-started/import-export.png %}
[4]: {{site.baseurl}}/api/endpoints/user_data
[5]: {{site.baseurl}}/user_guide/getting_started/web_sdk/
[6]: {{site.baseurl}}/partners/home
[7]: {{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion
[8]: {{site.baseurl}}/user_guide/engagement_tools/segments
[9]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/
[10]: {{site.baseurl}}/api/api_campaigns#api-campaigns
[11]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content
[12]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/about/
[13]: {% image_buster /assets/img/getting_started/channels.png %}
[14]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents
[15]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/
[16]: {{site.baseurl}}/api/endpoints/export
[17]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data
[18]: {% image_buster /assets/img/getting-started/putting-it-all-together.png %}
[19]: {{site.baseurl}}/developer_guide/platform_wide/getting_started/integration_overview/
[20]: {{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs