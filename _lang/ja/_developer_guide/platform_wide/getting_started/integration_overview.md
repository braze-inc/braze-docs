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

# [![Braze ラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}はじめに：統合の概要

> この記事では、オンボーディング・プロセスの基本的な概要を説明する。

![発見、統合、品質保証、保守という4つの円のベン図は、"価値実現までの時間 "を中心に描かれている。][27]{: style="max-width:50%;float:right;margin-left:15px;border:none;"} 

技術リソースとして、Braze を技術スタックに統合することで、チームを強化できます。オンボーディングは大きく4つのステップに分けられる：
* [発見と計画](#discovery)：チームと協力して、スコープを調整し、データとキャンペーンの構造を計画し、適切なワークスペース構造を作成する。 
* [統合](#integration)：SDK と API を統合し、メッセージングチャネルを有効にし、データのインポートとエクスポートを設定することで、計画を実行します。 
* [品質保証](#qa)：Brazeプラットフォームとお客様のアプリまたはサイト間のデータとメッセージングのループが期待通りに機能していることを確認する。
* [メンテナンス](#maintenance)：Braze をマーケティングチームに引き渡した後も、すべてがスムーズに実行されるよう引き続き確認します。

<br>
{% alert tip %}
すべての組織には明確なニーズがあることを認識しており、Braze はお客様固有の要件に合わせてカスタマイズできる多様なカスタマイズオプションに対応するよう構築されています。統合にかかる時間は、ユースケースによって異なる。
{% endalert %}

## 発見と計画 {#discovery}
このフェーズでは、チームと協力してオンボーディングタスクの範囲を設定し、すべての利害関係者が共通の目的に向けて足並みが揃っていることを確認します。 

あなたのチームは、ユースケースのエンド・ツー・エンド・プランニングを行い、すべてが期待通りに構築され、そのために適切なデータが利用できることを確認する。このフェーズには、プロジェクトリード、CRMリード、フロントエンドとバックエンドのエンジニアリング、プロダクトオーナー、マーケターが含まれる。 

ディスカバリーとプランニングの段階には、平均して約6週間かかる。このフェーズでは、開発リードは週に2～4時間を費やすことが予想されます。この製品に携わる開発者は、発見と計画の段階では、週に10〜20時間をBrazeに費やすと予想される。 

{% alert tip %}
御社のオンボーディング期間中、Braze は技術概要セッションを開催します。エンジニアにはこれらのセッションに参加することを強く推奨する。技術概要セッションでは、プラットフォーム・アーキテクチャのスケーラビリティについて話し合ったり、同規模の企業が同様のユースケースで過去にどのように成功したかという実践的な事例を見たりすることができる。
{% endalert %}

![メール、ショッピングカート、画像、ジオロケーションなど、さまざまなチャネル用のアイコン。][28]{: style="max-width:40%;float:right;margin-left:15px;"} 

### キャンペーン計画

CRM チームは、近い将来に立ち上げるメッセージングのユースケースを計画します。これには以下が含まれます：
* [チャンネル][1]（例えば、プッシュ通知やアプリ内メッセージなど）
* [配信方法][2](例えば、スケジュールされた配信やアクションベースの配信など)
* [ターゲットオーディエンス][3]
* [成功の指標][4]

例えば、新規顧客キャンペーンは、毎日午前10時に昨日最初のセッションを記録した顧客のセグメントにメールを送信します。コンバージョンイベント（成功指標）はセッションを記録している。

<br>
{% alert important %}
キャンペーンの計画ステップが完了するまで、統合を開始することはできません。このステップでは、統合フェーズで構成する必要がある Braze の構成要素を決定します。
{% endalert %}

### データ要件を作成する
次に、CRMチームは、計画したキャンペーンを実施するために必要なデータを定義し、データ要件を作成する。 

名前、メール、生年月日、国など、多くの一般的なユーザー属性は、Braze SDK が統合された後に自動的に追跡されます。その他のタイプのデータは、カスタムデータとして定義する必要がある。

開発者として、チームと協力して、追跡する価値のある追加のカスタムデータを定義します。カスタムデータは、ユーザーベースがどのように分類され、セグメント化されるかに影響します。成長スタック全体でイベント分類法を設定し、データを構造化して、Brazeに出入りする際のシステムとの互換性を確保する。

{% alert tip %}
ツール間でデータの命名法を統一する。例えば、データウェアハウスは「期間限定オファーの購入」を特定の方法で記録する場合があります。このフォーマットに合わせてBrazeのカスタムイベントが必要かどうかを決める必要がある。
{% endalert %}

[自動収集されたデータとカスタムデータ][5]の詳細を参照してください。

### カスタマイズの計画
マーケティング担当者に、希望するカスタマイズについて相談する。例えば、デフォルトのBraze Content Cardsを実装したいか？ブランド・ガイドラインに合うように、ルック＆フィールを少し調整したいのか？コンポーネントのために全く新しいUIを開発し、Brazeにその分析を追跡させたいか？カスタマイズのレベルが異なれば、必要な範囲も異なる。詳細は[カスタマイズの概要を][6]参照のこと。

### ダッシュボードにアクセスする
Brazeダッシュボードは、私たちのウェブUIインターフェイスである。マーケティング担当者はダッシュボードを使って仕事をし、コンテンツを作成する。開発者はダッシュボードを使い、APIキーやプッシュ通知の認証情報など、アプリを統合するための設定を管理する。

チーム管理者は、ダッシュボードであなた（およびBrazeへのアクセスが必要な他のチームメンバー全員）をユーザーとして追加する必要がある。

### ワークスペースとAPIキー
チーム管理者はまた、さまざまな[ワークスペース]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/)を作成します。ワークスペースは、ユーザー、セグメント、APIキーなどのデータを1つの場所にグループ化する。ベストプラクティスとして、同じアプリやよく似たアプリの異なるバージョンのみを1つのワークスペースにまとめることをお勧めします。 

重要なのは、ワークスペースが複数のプラットフォーム（iOSやAndroidなど）用のAPIキーを提供することだ。SDKデータを特定のワークスペースに関連付けるには、相関APIキーを使用する。ワークスペースに移動し、各アプリのAPIキーにアクセスする。各APIキーが、スコープした作業を実行するための正しい権限を持っていることを確認する。詳細は [API プロビジョニングの記事][7]を参照してください。

{% alert important %}
開発用と本番用で異なる環境を設定することが重要だ。テスト環境を設定することで、オンボーディングやQAで実際にお金を使うことを防ぐことができる。テスト環境を作成するには、テスト用ワークスペースをセットアップし、本番用ワークスペースにテスト用データを入力しないように、必ずそのAPIキーを使用すること。
{% endalert %}  


## 統合 {#integration}
![データソースからユーザー機器への情報の流れを表す抽象的なピラミッド図形。][29]{: style="max-width:45%;float:right;margin-left:15px;"} 

BrazeはiOSアプリ、Androidアプリ、ウェブアプリなどをサポートしている。また、React Native や Unity のようなクロスプラットフォームのラッパー SDK を使うこともできます。通常、顧客は1～6週間で統合されます。多くの顧客は、技術スキルと帯域幅の広さにもよりますが、たった1人のエンジニアで Braze を統合しています。これは、具体的な統合の範囲と、チームが Braze のプロジェクトに費やす時間に完全に依存します。 

そのためには、この分野に精通した開発者が必要だ：
* アプリやサイトのネイティブレイヤーで作業する
* REST APIにヒットするプロセスを作成する
* 統合テスト 
* JSONウェブトークン認証
* 一般的なデータ管理スキル
* DNS レコードを設定する

### CDP統合パートナー
多くの顧客は、Braze のオンボーディングを、統合パートナーとして顧客データプラットフォーム (CDP) とも統合する機会として利用しています。Braze はデータの追跡と分析を提供し、顧客データプラットフォームは追加のデータルーティングとオーケストレーションを提供できます。Braze は、[mParticle]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle/) や [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/) など多くの顧客データプラットフォームとシームレスに統合できます。 

顧客データプラットフォームとサイドバイサイドの統合を行う場合は、顧客データプラットフォームの SDK からの呼び出しを Braze SDK にマッピングします。基本的に、次を実行します。
* 識別呼び出しを `changeUser` ([Android][11]、[iOS][12]、[web][13]) にマップし、属性を設定します。
* データフラッシュ呼び出しを `requestImmediateDataFlush` ([Android][14]、[iOS][15]、[web][16]) にマッピングします。
* カスタムイベントや購入を記録する。

選択したプラットフォームによっては、Braze SDK と選択した CDP の間の統合例を利用できる可能性があります。詳細は[CDPテクノロジー・パートナーのリストを][8]参照のこと。 

### Braze SDKの統合 
Braze SDKは、2つの重要な機能を提供する。それは、ユーザーデータを収集し、統合されたユーザープロファイルに同期することと、プッシュ通知、アプリ内メッセージ、コンテンツカードなどのメッセージングチャネルを強化することである。 

{% alert tip %}
Braze SDK は、アプリやサイトと完全に統合されると、完全に実現されたレベルの高度なマーケティングを提供します。Braze SDK の統合を延期すると、ドキュメントに記載されている機能の一部が利用できなくなります。
{% endalert %}

SDKの実装では、以下のことを行う：
* サポートしたいプラットフォームごとにSDK統合コードを書く。
* 各プラットフォームのメッセージングチャネルを有効にし、Braze SDKがEメール、SMS、プッシュ通知、その他のチャネルにわたる顧客とのインタラクションのデータを追跡するようにする。
* 予定されている [UI コンポーネントのカスタマイズ][6] (例えば、カスタムコンテンツカード) を作成します。完全にカスタム化されたコンテンツの場合、SDK の自動データ収集では新しいコンポーネントを認識できないため、分析のログを取る必要があります。この実装は、当社のデフォルトのコンポーネントでパターン化することができます。


### Braze APIを使用する
Brazeを使用している間、さまざまな場面でさまざまなタスクにREST APIを使用することになる。Braze APIは次のような用途に役立つ： 
1. 過去のデータをインポートする
2. Brazeではトリガーされない継続的なアップデート。例えば、アプリにログインせずにユーザープロファイルをVIPにアップグレードする場合、APIはこの情報をBrazeに伝える必要がある。

[Braze API][9] の使用を開始する。

{% alert important %}
APIを使用する際は、リクエストをバッチ処理し、デルタ値のみを送信するようにしてほしい。Braze は送信されたすべての属性を書き直します。カスタム属性の値が変更されていない場合は更新しない。
{% endalert %}

### 製品分析を設定する
Braze はデータがすべてです。Brazeのデータはユーザープロファイルに保存される。 

データポイントとは、マーケティング担当者にとって適切なデータを確実に取得するための仕組みであり、単に「どんな」データでも集めればいいというものではない。[データポイント][10]に慣れましょう。

### レガシーユーザーデータの移行
Braze の [/users/track エンドポイント][17]を使用して、Braze の外部で記録された履歴データを移行できます。よくインポートされるデータの例としては、プッシュトークンや過去の購入履歴などがある。このエンドポイントは、単発のインポートや定期的なバッチ更新に使用できる。 

また、ダッシュボードに一度だけ [CSV をアップロードする][18]ことで、ユーザーをインポートし、顧客の属性値を更新することもできます。CSVのアップロードはマーケティング担当者にとって便利だが、REST APIを使えばより柔軟に対応できる。

### セッショントラッキングを設定する
Braze SDKは、「オープンセッション」と「クローズセッション」のデータポイントを生成する。また、Braze SDK は定期的にデータをフラッシュします。セッショントラッキングのデフォルト値 (いずれもカスタマイズ可能) については、以下のリンクを参照してください ([Android][19]、[iOS][20]、[web][21])。

### カスタムイベント、属性、購入イベントを追跡する
カスタムイベント、ユーザー属性、購入イベントなど、計画したデータスキーマを設定するためにチームと調整する。[カスタムデータスキーム][22]はダッシュボードを使用して入力され、SDK 統合中に実装したものと完全に一致しなければなりません。

{% alert tip %}
ユーザー ID (Braze では `external_id` と呼ばれます) は、既知のすべてのユーザに対して設定する必要があります。これらの情報は不変であるべきで、ユーザーがアプリを開いたときにアクセスできるようにし、デバイスやプラットフォームを超えてユーザーを追跡できるようにする。ベストプラクティスについては、[ユーザーライフサイクルの]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/)記事を参照のこと。
{% endalert %}

### その他のツール
ユースケースによっては、他にも設定が必要なツールがある可能性があります。例えば、ユーザーストーリーを実現するために、[ジオフェンスの][24]ようなツールを設定する必要がある場合があります。重要な統合ステップを完了した後に、これらの追加ツールをセットアップできる顧客が最も成功していることが明らかになっています。

## 品質保証 {#qa}
統合を実行する際には、設定したすべてが期待通りに機能していることを確認するため、品質保証を行う。この QA は、データインジェストとメッセージチャネルの2つに大別されます。

{% alert important %}
QA を始める前に、本番環境とテスト環境がセットアップされていることを確認してください。
{% endalert %}

| **QA データの取り込み**  | **QA メッセージング**                                              |
|---------------------------|---------------------------------------------------------------|
| データのインジェスト、保存、エクスポートの方法について品質保証を行います。 | メッセージがユーザーに正しく送信され、すべてが素晴らしく見えることを確認できるだろう。 |
| データが正しく保存されていることを確認するためにテストを実行する。 | ユーザーのセグメントを作成する。 |
| セッションデータがBraze内の意図したワークスペースに正しく帰属していることを確認する。 | キャンペーンとキャンバスを正常に起動します。 |
| セッションの開始と終了が記録されていることを確認する。 | 正しいキャンペーンが正しいユーザーセグメントに表示されていることを確認する。 |
| ユーザー属性情報がユーザープロファイルに対して正しく記録されていることを確認する。 | プッシュトークンが正しく登録されていることを確認する。 |
| ユーザープロファイルに対してカスタムデータが正しく記録されていることをテストする。 | プッシュトークンが正しく取り除かれていることを確認する。 |
| 匿名ユーザープロファイルを作成する。 | プッシュキャンペーンがデバイスに正しく送信され、エンゲージメントが記録されているかテストする。 |
| `changeUser()` メソッドが呼び出されたときに、匿名ユーザープロファイルが既知のユーザープロファイルになることを確認します。 | アプリ内メッセージが配信され、メトリクスが記録されることをテストする。 |
|                           | コンテンツカードが配信され、メトリクスが記録されていることをテストする。 |
|                           | コネクテッド・コンテンツを促進する（例えば、AccuWeather）。 |
|                           | すべてのメッセージチャネルの統合が正しく機能していることを確認する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}



### Braze をマーケターに引き継ぐ
プラットフォームやサイトを統合したら、マーケティングチームを関与させて、彼らにプラットフォームの所有権を渡しましょう。このプロセスは企業によって異なるが、以下のようなものがある：
* 複雑な [Liquid ロジック][25]を構成する
* [メールの IP ウォームアップ][26]を容易にする
* 他の利害関係者に追跡されるデータの種類を理解させる

### 未来のために開発する
コードベースを受け継いだが、最初の開発者が何を考えていたのか全く分からなかったことはないだろうか？さらに悪いことに、コードを書いて完全に理解したのに、1年後にそのコードに戻ってきたときに、まったく不可解に感じたことはないだろうか？ 

Braze のオンボーディング時には、データ、ユーザープロファイル、対象となる統合と対象外の統合、カスタマイズの動作方法などに関して下した決断の積み重ねが新鮮に感じられ、それゆえに明白なものとなります。あなたのチームがBrazeを拡張したいとき、または他の技術リソースがあなたのBrazeプロジェクトに割り当てられたとき、この情報は不明瞭になる。

技術概要セッションで学んだ情報を定着させるためのリソースを作成する。このリソースは、あなたのチームに加わる新しい開発者をオンボードする時間を短縮するのに役立つ（あるいは、現在のBrazeの実装を拡張する必要があるときに、自分自身へのリマインダーとして役立つ）。 

## メンテナンス {#maintenance}
マーケターに引き継がれた後も、あなたはメンテナンスのためのリソースとしての役割を果たすことになります。Braze SDKに影響を与える可能性のあるiOSとAndroidのアップデートに注意を払い、サードパーティーベンダーが最新であることを確認する。 

Braze [GitHub][23] を使用して、Braze プラットフォームへの更新を追跡します。時折、緊急アップデートやバグフィックスに関するメールがBrazeから管理者に直接届くこともある。 




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