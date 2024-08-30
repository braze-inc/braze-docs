---
nav_title: 統合の概要
article_title: 統合の概要
page_order: 2
description: "この記事では、オンボーディング・プロセスの基本的な概要を説明する。"
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

# [![Braze Learningコース]](https://learning.braze.com/sdk-integration-basics)([{% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}はじめに：統合の概要

> この記事では、オンボーディング・プロセスの基本的な概要を説明する。

![発見、統合、品質保証、保守という4つの円のベン図は、"価値実現までの時間 "を中心に描かれている。][27]{: style="max-width:50%;float:right;margin-left:15px;border:none;"} 

技術的なリソースとして、Brazeを技術スタックに統合することで、チームに力を与えることができる。オンボーディングは大きく4つのステップに分けられる：
* [忖度と計画](#discovery)：チームと協力して、スコープを調整し、データとキャンペーンの構造を計画し、適切なワークスペース構造を作成する。 
* [統合](#integration)だ：SDKとAPIを統合し、メッセージング・チャンネルを有効にし、データのインポートとエクスポートを設定することで、計画を実行する。 
* [品質保証](#qa)：Brazeプラットフォームとお客様のアプリまたはサイト間のデータとメッセージングのループが期待通りに機能していることを確認する。
* [メンテナンス](#maintenance)だ：Brazeをマーケティング・チームに引き継いだ後も、すべてがスムーズに進むようにする。

<br>
{% alert tip %}
すべての組織には明確なニーズがあることを認識しており、Braze はお客様固有の要件に合わせてカスタマイズできる多様なカスタマイズオプションに対応するよう構築されています。統合にかかる時間は、ユースケースによって異なる。
{% endalert %}

## 発見と計画 {#discovery}
このフェーズでは、チームと協力してオンボーディング・タスクの範囲を決め、すべての利害関係者が共通のゴールで足並みを揃えるようにする。 

あなたのチームは、ユースケースのエンド・ツー・エンド・プランニングを行い、すべてが期待通りに構築され、そのために適切なデータが利用できることを確認する。このフェーズには、プロジェクトリード、CRMリード、フロントエンドとバックエンドのエンジニアリング、プロダクトオーナー、マーケターが含まれる。 

ディスカバリーとプランニングの段階には、平均して約6週間かかる。エンジニアリング・リードは、この段階で週に2〜4時間を費やすと予想される。この製品に携わる開発者は、発見と計画の段階では、週に10〜20時間をBrazeに費やすと予想される。 

{% alert tip %}
御社のオンボーディング期間中、Brazeは技術概要セッションを開催する。エンジニアにはこれらのセッションに参加することを強く推奨する。技術概要セッションでは、プラットフォーム・アーキテクチャのスケーラビリティについて話し合ったり、同規模の企業が同様のユースケースで過去にどのように成功したかという実践的な事例を見たりすることができる。
{% endalert %}

![Eメール、ショッピングカート、画像、ジオロケーションなど、さまざまなチャンネル用のアイコンがある。][28]{: style="max-width:40%;float:right;margin-left:15px;"} 

### キャンペーン計画

CRMチームは、近い将来に立ち上げるメッセージングのユースケースを計画する。これには以下が含まれる：
* [チャンネル][1]（例えば、プッシュ通知やアプリ内メッセージなど）
* [配信方法][2]（例えば、定期配信やアクションベースの配信など）
* [対象読者][3]
* [成功の指標][4]

例えば、新規顧客キャンペーンは、毎日午前10時に、昨日最初のセッションを記録した顧客のセグメントにEメールを送信する。コンバージョンイベント（成功指標）はセッションを記録している。

<br>
{% alert important %}
キャンペーンの計画段階が完了するまで、統合を開始することはできない。このステップでは、統合フェーズでBrazeのどの部品や部分を構成する必要があるかを決定する。
{% endalert %}

### データ要件を作成する
次に、CRMチームは、計画したキャンペーンを実施するために必要なデータを定義し、データ要件を作成する。 

名前、Eメール、生年月日、国など、多くの一般的なユーザー属性は、Braze SDKが統合された後に自動的に追跡される。その他のタイプのデータは、カスタムデータとして定義する必要がある。

開発者として、あなたはチームと協力して、追跡することが意味のある追加的なカスタムデータを定義する。カスタム・データは、ユーザー・ベースがどのように分類され、セグメンテーションされるかに影響する。成長スタック全体でイベント分類法を設定し、データを構造化して、Brazeに出入りする際のシステムとの互換性を確保する。

{% alert tip %}
ツール間でデータの命名法を統一する。例えば、データウェアハウスは「期間限定オファーの購入」を特定の方法で記録するかもしれない。このフォーマットに合わせてBrazeのカスタムイベントが必要かどうかを決める必要がある。
{% endalert %}

[自動収集されたデータとカスタム・データについての][5]詳細はこちら。

### カスタマイズの計画
マーケティング担当者に、希望するカスタマイズについて相談する。例えば、デフォルトのBraze Content Cardsを実装したいか？ブランド・ガイドラインに合うように、ルック＆フィールを少し調整したいのか？コンポーネントのために全く新しいUIを開発し、Brazeにその分析を追跡させたいか？カスタマイズのレベルが異なれば、必要な範囲も異なる。詳細は[カスタマイズの概要を][6]参照のこと。

### ダッシュボードにアクセスする
Brazeダッシュボードは、私たちのウェブUIインターフェイスである。マーケティング担当者はダッシュボードを使って仕事をし、コンテンツを作成する。開発者はダッシュボードを使い、APIキーやプッシュ通知の認証情報など、アプリを統合するための設定を管理する。

チーム管理者は、ダッシュボードであなた（およびBrazeへのアクセスが必要な他のチームメンバー全員）をユーザーとして追加する必要がある。

### ワークスペースとAPIキー
チーム管理者はまた、さまざまな[ワークスペースを]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/)作成する。ワークスペースは、ユーザー、セグメント、APIキーなどのデータを1つの場所にグループ化する。ベストプラクティスとして、同じアプリやよく似たアプリの異なるバージョンのみを1つのワークスペースにまとめることをお勧めします。 

重要なのは、ワークスペースが複数のプラットフォーム（iOSやAndroidなど）用のAPIキーを提供することだ。SDKデータを特定のワークスペースに関連付けるには、相関APIキーを使用する。ワークスペースに移動し、各アプリのAPIキーにアクセスする。各APIキーが、スコープした作業を実行するための正しい権限を持っていることを確認する。詳細は[APIプロビジョニングの記事を][7]参照のこと。

{% alert important %}
開発用と本番用で異なる環境を設定することが重要だ。テスト環境を設定することで、オンボーディングやQAで実際にお金を使うことを防ぐことができる。テスト環境を作成するには、テスト用ワークスペースをセットアップし、本番用ワークスペースにテスト用データを入力しないように、必ずそのAPIキーを使用すること。
{% endalert %}  


## 統合 {#integration}
![データソースからユーザー機器への情報の流れを表す抽象的なピラミッド図形。][29]{: style="max-width:45%;float:right;margin-left:15px;"} 

BrazeはiOSアプリ、Androidアプリ、ウェブアプリなどをサポートしている。また、React NativeやUnityのようなクロスプラットフォームのラッパーSDKを使うこともできる。通常、1週間から6週間で統合される。多くの顧客は、技術的スキルと帯域幅の広さに応じて、1人のエンジニアだけでBrazeを統合している。具体的な統合範囲と、チームがBrazeプロジェクトにどれだけの時間を割くかに完全に依存する。 

そのためには、この分野に精通した開発者が必要だ：
* アプリやサイトのネイティブレイヤーで作業する
* REST APIにヒットするプロセスを作成する
* 統合テスト 
* JSONウェブトークン認証
* 一般的なデータ管理スキル
* DNSレコードを設定する

### CDP統合パートナー
多くの顧客は、Brazeのオンボーディングを、統合パートナーとして顧客データプラットフォーム（CDP）とも統合する機会として利用している。Brazeはデータの追跡と分析を提供し、CDPはさらにデータのルーティングとオーケストレーションを提供できる。Brazeは、[mParticleや]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle/) [Segmentなど]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/)多くのCDPとシームレスに統合できる。 

CDPとサイドバイサイドの統合を行う場合は、CDPのSDKからの呼び出しをBraze SDKにマッピングする。基本的には、そうなるだろう：
* `changeUser` [（Android][11]、[iOS][12]、[Web][13]）への識別コールをマップし、属性を設定する。
* `requestImmediateDataFlush` [（Android][14]、[iOS][15]、[ウェブ][16]）への地図データフラッシュコール。
* カスタムイベントや購入を記録する。

選択したプラットフォームによっては、Braze SDKと選択したCDPの間の統合例が利用できるかもしれない。詳細は[CDPテクノロジー・パートナーのリストを][8]参照のこと。 

### Braze SDKの統合 
Braze SDKは、2つの重要な機能を提供する。それは、ユーザーデータを収集し、統合されたユーザープロファイルに同期することと、プッシュ通知、アプリ内メッセージ、コンテンツカードなどのメッセージングチャネルを強化することである。 

{% alert tip %}
アプリやサイトと完全に統合されたBraze SDKは、完全に実現されたレベルの高度なマーケティングを提供する。Braze SDKの統合を延期すると、ドキュメントに記載されている機能の一部が利用できなくなる。
{% endalert %}

SDKの実装では、以下のことを行う：
* サポートしたいプラットフォームごとにSDK統合コードを書く。
* 各プラットフォームのメッセージングチャネルを有効にし、Braze SDKがEメール、SMS、プッシュ通知、その他のチャネルにわたる顧客とのインタラクションのデータを追跡するようにする。
* 予定されている[UIコンポーネントのカスタマイズ][6]（例えば、カスタムコンテンツカード[）を][6]作成する。完全にカスタム化されたコンテンツの場合、SDKの自動データ収集では新しいコンポーネントを認識できないため、アナリティクスのログを取る必要がある。この実装は、我々のデフォルト・コンポーネントでパターン化することができる。


### Braze APIを使用する
Brazeを使用している間、さまざまな場面でさまざまなタスクにREST APIを使用することになる。Braze APIは次のような用途に役立つ： 
1. 過去のデータをインポートする
2. Brazeではトリガーされない継続的なアップデート。例えば、アプリにログインせずにユーザープロファイルをVIPにアップグレードする場合、APIはこの情報をBrazeに伝える必要がある。

[Braze APIを][9]使い始める[。][9]

{% alert important %}
APIを使用する際は、リクエストをバッチ処理し、デルタ値のみを送信するようにしてほしい。ブレイズは送信されたすべての属性を書き直す。カスタム属性の値が変更されていない場合は更新しない。
{% endalert %}

### 製品分析を設定する
ブレイズはデータがすべてだ。Brazeのデータはユーザープロファイルに保存される。 

データポイントとは、マーケティング担当者にとって適切なデータを確実に取得するための仕組みであり、単に「どんな」データでも集めればいいというものではない。[データポイントに][10]慣れ親しむ。

### レガシーユーザーデータの移行
Brazeの[/users/trackエンドポイントを][17]使用して、Brazeの外部で記録された履歴データを移行できる。よくインポートされるデータの例としては、プッシュトークンや過去の購入履歴などがある。このエンドポイントは、単発のインポートや定期的なバッチ更新に使用できる。 

また、ダッシュボードに[CSVを][18]一度だけ[アップロードする][18]ことで、ユーザーをインポートし、顧客の属性値を更新することもできる。CSVのアップロードはマーケティング担当者にとって便利だが、REST APIを使えばより柔軟に対応できる。

### セッショントラッキングを設定する
Braze SDKは、「オープンセッション」と「クローズセッション」のデータポイントを生成する。また、Braze SDKは定期的にデータをフラッシュする。セッショントラッキングのデフォルト値については、以下のリンクを参照のこと[（Android][19]、[iOS][20]、[ウェブ][21][）][19]。

### カスタムイベント、属性、購入イベントを追跡する
カスタムイベント、ユーザー属性、購入イベントなど、計画したデータスキーマを設定するためにチームと調整する。[カスタム・データ・スキームは][22]ダッシュボードを使用して入力され、SDK統合中に実装したものと完全に一致しなければならない。

{% alert tip %}
Brazeでは`external_id`sと呼ばれるユーザーIDは、すべての既知のユーザーに設定されるべきである。これらの情報は不変であるべきで、ユーザーがアプリを開いたときにアクセスできるようにし、デバイスやプラットフォームを超えてユーザーを追跡できるようにする。ベストプラクティスについては、[ユーザーライフサイクルの]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/)記事を参照のこと。
{% endalert %}

### その他のツール
あなたのユースケースに基づき、セットアップする必要がある他のツールがあるかもしれない。例えば、ユーザーストーリーを実現するために、[ジオフェンスの][24]ようなツールを設定する必要があるかもしれない。私たちは、重要な統合ステップを完了した後に、これらの追加ツールをセットアップする能力を持つ顧客が最も成功していることを発見した。

## 品質保証 {#qa}
統合を実行する際には、設定したすべてが期待通りに機能していることを確認するため、品質保証を行う。このQAは、データ・インジェストとメッセージ・チャネルの2つに大別される。

{% alert important %}
QAを始める前に、本番環境とテスト環境がセットアップされていることを確認する。
{% endalert %}

| **QAデータの取り込み**  | **QAメッセージング**                                              |
|---------------------------|---------------------------------------------------------------|
| データのインジェスト、保存、エクスポートの方法について品質保証を行う。 | メッセージがユーザーに正しく送信され、すべてが素晴らしく見えることを確認できるだろう。 |
| データが正しく保存されていることを確認するためにテストを実行する。 | ユーザーのセグメントを作成する。 |
| セッションデータがBraze内の意図したワークスペースに正しく帰属していることを確認する。 | キャンペーンとキャンバスを成功させる。 |
| セッションの開始と終了が記録されていることを確認する。 | 正しいキャンペーンが正しいユーザーセグメントに表示されていることを確認する。 |
| ユーザー属性情報がユーザープロファイルに対して正しく記録されていることを確認する。 | プッシュトークンが正しく登録されていることを確認する。 |
| ユーザープロファイルに対してカスタムデータが正しく記録されていることをテストする。 | プッシュトークンが正しく取り除かれていることを確認する。 |
| 匿名ユーザープロファイルを作成する。 | プッシュキャンペーンがデバイスに正しく送信され、エンゲージメントが記録されているかテストする。 |
| `changeUser()` 、匿名ユーザー・プロファイルが既知のユーザー・プロファイルになることを確認する。 | アプリ内メッセージが配信され、メトリクスが記録されることをテストする。 |
|                           | コンテンツカードが配信され、メトリクスが記録されていることをテストする。 |
|                           | コネクテッド・コンテンツを促進する（例えば、AccuWeather）。 |
|                           | すべてのメッセージチャネルの統合が正しく機能していることを確認する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}



### ブレーズをマーケティング担当者に引き継ぐ
プラットフォームやサイトを統合したら、マーケティングチームを巻き込み、プラットフォームの所有権を彼らに渡したい。このプロセスは企業によって異なるが、以下のようなものがある：
* 複雑な[リキッドロジックを][25]構成する
* [電子メールのIPウォーミングアップを][26]容易にする
* 他の利害関係者に追跡されるデータの種類を理解させる

### 未来のために開発する
コードベースを受け継いだが、最初の開発者が何を考えていたのか全く分からなかったことはないだろうか？さらに悪いことに、コードを書いて完全に理解したのに、1年後にそのコードに戻ってきたときに、まったく不可解に感じたことはないだろうか？ 

Brazeのオンボーディング時には、データ、ユーザープロファイル、どのような統合が範囲内か範囲外か、カスタマイズがどのように機能することになっているかなどに関して、あなたが下した決断の積み重ねが新鮮に感じられ、それゆえに明白になる。あなたのチームがBrazeを拡張したいとき、または他の技術リソースがあなたのBrazeプロジェクトに割り当てられたとき、この情報は不明瞭になる。

技術概要セッションで学んだ情報を定着させるためのリソースを作成する。このリソースは、あなたのチームに加わる新しい開発者をオンボードする時間を短縮するのに役立つ（あるいは、現在のBrazeの実装を拡張する必要があるときに、自分自身へのリマインダーとして役立つ）。 

## メンテナンス {#maintenance}
マーケティング担当者に引き継がれた後も、あなたはメンテナンスのためのリソースとしての役割を果たすことになる。Braze SDKに影響を与える可能性のあるiOSとAndroidのアップデートに注意を払い、サードパーティーベンダーが最新であることを確認する。 

Braze[GitHubを通じて][23]Brazeプラットフォームのアップデートを追跡する。時折、緊急アップデートやバグフィックスに関するメールがBrazeから管理者に直接届くこともある。 




[1]: {{site.baseurl}}/user_guide/message_building_by_channel
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types
[3]: {{site.baseurl}}/user_guide/engagement_tools/segments
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events
[5]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/
[6]: {{site.baseurl}}/developer_guide/customization_guides/customization_overview
[7]: {{site.baseurl}}/api/basics/#rest-api-key
[8]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform
[9]: {{site.baseurl}}/api/basics
[10]: {{site.baseurl}}/user_guide/data_and_analytics/data_points
[11]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html
[12]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)/
[13]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser
[14]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-immediate-data-flush.html?query=abstract%20fun%20requestImmediateDataFlush()
[15]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/requestimmediatedataflush()
[16]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestimmediatedataflush
[17]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[18]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#importing-a-csv
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/
[20]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_sessions/
[21]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/
[22]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[23]: https://github.com/braze-inc/
[24]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences#about-locations-and-geofences/
[25]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid#about-liquid
[26]: {{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/
[27]: {% image_buster /assets/img/getting-started/getting-started-integrate-flower.png %}
[28]: {% image_buster /assets/img/getting-started/data-graphic-2.png %}
[29]: {% image_buster /assets/img/getting-started/data-graphic.png %}  