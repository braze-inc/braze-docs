---
nav_title: 統合の概要
article_title: 統合の概要
page_order: 2
description: "本論文は、オンボーディングプロセスの基本的な概要を提供する。"
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

# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}はじめに:統合の概要

> 本論文は、オンボーディングプロセスの基本的な概要を提供する。

!["time to value."][27]を中心とした、4つのサークル(発見、統合、品質保証、維持)の正式図{: style="max-width:50%;float:right;margin-left:15px;border:none;"} 

テクニカルリソースとして、Braze をテクノロジースタックに統合することで、チームに権限を与えます。オンボーディングは大きく4つのステップに分かれています。
* [検出と計画](#discovery):チームと協力して、スコープを調整し、データとキャンペーンの構造を計画し、適切なワークスペース構造を作成します。
* [統合](#integration):SDKとAPIを統合し、メッセージングチャネルを有効にし、データのインポートとエクスポートを設定して、プランで実行します。
* [品質保証](#qa):Braze プラットフォームとアプリまたはサイト間のデータおよびメッセージのループが期待どおりに機能していることを確認します。
* [メンテナンス](#maintenance):Braze からマーケティングチームに渡った後は、すべてがスムーズに実行され続けることを確認し続けます。

<br>
{% alert tip %}
すべての組織には明確なニーズがあることを認識しており、Braze はお客様固有の要件に合わせてカスタマイズできる多様なカスタマイズオプションに対応するよう構築されています。統合時間は、ユースケースによって異なります。
{% endalert %}

## 発見・計画 {#discovery}
このフェーズでは、チームと協力してオンボーディングタスクをスコープ化し、すべてのステークホルダーが共通の目標に沿っていることを確認します。 

チームは、ユースケースのエンドツーエンドの計画を実行し、すべてのものが期待どおりに構築され、そのために使用可能な正しいデータがあることを確認します。このフェーズには、プロジェクトリード、CRMリード、フロントエンドおよびバックエンドエンジニアリング、製品オーナー、マーケターが含まれます。 

検出と計画のフェーズには、平均で約6週間かかります。エンジニアリングリーダーは、このフェーズで1週間に2～4時間を費やすことが期待できます。製品を使用する開発者は、検出および計画段階で1週間に10～20時間をBrazeに費やすことができます。 

{% alert tip %}
御社のオンボーディング期間中、Brazeは技術概要セッションを主催します。これらのセッションにはエンジニアが参加することを強くお勧めします。テクニカル概要セッションでは、プラットフォームアーキテクチャのスケーラビリティについて話し合いを行い、サイズの企業が同様のユースケースでこれまでどのように成功してきたかについての実用的な例を見ることができます。
{% endalert %}

![メール、ショッピングカート、画像、地理位置情報など、チャネルごとのアイコン][28]{: style="max-width:40%;float:right;margin-left:15px;"} 

### キャンペーン企画

CRMチームは、近い将来に起動するメッセージングユースケースを計画します。これには以下が含まれます。
* [チャネル][1](例:プッシュ通知またはアプリ内メッセージ)
* [配信方法][2](スケジュール配信やアクションベース配信など)
* [ターゲットオーディエンス][3]
* [成功メトリクス][4]

たとえば、新しい顧客キャンペーンは、毎日午前10時に、昨日の最初のセッションを記録した顧客のセグメントに送信されるメールです。変換イベント(成功メトリクス)は、セッションのログ記録です。

<br>
{% alert important %}
キャンペーン計画ステップが完了するまで統合を開始できません。このステップでは、統合フェーズ中にどの部品および Braze の部品を構成する必要があるかを決定します。
{% endalert %}

### データ要件の作成
次に、CRMチームは、計画したキャンペーンを起動するために必要なデータを定義し、データ要件を作成します。 

Braze SDK が統合されると、名前、メール、生年月日、国など、一般的なユーザー属性の多くが自動的に追跡されます。その他のタイプのデータは、カスタムデータとして定義する必要があります。

開発者は、チームと協力して、追跡に役立つ追加のカスタムデータを定義します。カスタム・データは、ユーザー・ベースがどのように分類され、セグメント化されるかに影響します。グローススタック全体にイベント分類を設定し、データが Braze の内外に移動するときにシステムと互換性があるようにデータを構造化します。

{% alert tip %}
ツール間でデータ命名法の一貫性を保ちます。たとえば、データウェアハウスは"purchase limited time offer"を特定の方法で記録できます。このフォーマットに合わせるために、Braze のカスタムイベントが必要かどうかを決定する必要があります。
{% endalert %}

[自動的に収集されたデータとカスタムデータ][5] について詳しく説明します。

### カスタマイズ計画
希望するカスタマイズについてマーケターに話してみましょう。たとえば、デフォルトのろう付けコンテンツカードを実装しますか?あなたのブランドガイドラインに合わせて、彼らの外観や感覚を少し微調整したいですか?コンポーネントの完全に新しいUI を開発し、その分析をBraze で追跡しますか?カスタマイズのレベルに応じて、スコープのレベルが異なります。詳細については、[カスタマイズの概要][6]を参照してください。

### ダッシュボードアクセスの取得
Braze ダッシュボードはWeb UI インタフェースです。マーケティング担当者は、ダッシュボードを使用して自分の仕事を行い、コンテンツを作成します。開発者はダッシュボードを使用して、API キーやプッシュ通知の認証情報など、アプリケーションを統合するための設定を管理します。

チーム管理者は、ダッシュボード上のユーザとして、ユーザ(およびBraze へのアクセスが必要な他のすべてのチームメンバー) を追加する必要があります。

### ワークスペースとAPI キー
チーム管理者は、異なる[ワークスペース]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/)も作成します。ワークスペースは、ユーザー、セグメント、API キーなどのデータを1 つの場所にグループ化します。ベストプラクティスとして、同じアプリやよく似たアプリの異なるバージョンのみを1つのワークスペースにまとめることをお勧めします。 

重要な点として、ワークスペースは、複数のプラットフォーム(iOS やAndroid など) のAPI キーを提供します。相関API キーを使用して、SDK データを特定のワークスペースに関連付けます。ワークスペースに移動して、各アプリのAPI キーにアクセスします。各API キーに、スコープした作業を実行するための正しい権限があることを確認します。詳細については、[APIプロビジョニング記事][7]を参照してください。

{% alert important %}
開発と実稼働のために異なる環境を設定することが重要です。テスト環境を設定すると、オンボーディングとQA 中に実際の費用を消費することができなくなります。テスト環境を作成するには、テストワークスペースを設定し、そのAPI キーを使用して、本番ワークスペースにテストデータを入力しないようにします。
{% endalert %}  


## 統合 {#integration}
![データソースからユーザーデバイスへの情報の流れを表す抽象ピラミッドグラフ][29]{: style="max-width:45%;float:right;margin-left:15px;"} 

Braze はiOS アプリ、Android アプリ、Web アプリなどをサポートしています。React Native やUnity などのクロスプラットフォームラッパーSDK を使用することもできます。通常、顧客は1～6週間の間、どこでも統合されている。多くの顧客は、技術スキルと帯域幅の幅に応じて、1人のエンジニアだけとBrazeを統合しています。それは、あなたの特定の統合範囲と、あなたのチームがBrazeプロジェクトにどれだけの時間を費やしているかに完全に依存します。 

以下に詳しい開発者が必要になります。
\* アプリまたはサイトのネイティブレイヤでの作業
\* REST APIに打撃を与えるプロセスの作成
\* 統合テスト
\* JSON Web トークン認証
\* 一般的なデータ管理スキル
\* DNS レコードの設定

### CDP統合パートナー
Braze Onboardingは、顧客データプラットフォーム(CDP)とも統合パートナーとして統合する機会として多くの顧客が利用している。Braze はデータ追跡と分析を提供し、CDP は追加のデータルーティングとオーケストレーションを提供します。Braze は、[mParticle]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle/) や[Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/) など、多くのCDP とシームレスに統合できます。 

CDP との並列統合を実行する場合は、CDP のSDK からのコールをBraze SDK にマッピングします。基本的には、以下の操作を行います。
* `changeUser` ([Android][11], [iOS][12], [web][13]) への呼び出しをマップし、属性を設定します。
* `requestImmediateDataFlush` ([Android][14]、[iOS][15]、[web][16]) へのデータフラッシュ呼び出しをマップします。
\* カスタムイベントまたは購入を記録します。

選択したプラットフォームに応じて、選択したBraze SDK とCDP の統合例を使用できます。詳細については、[CDPテクノロジーパートナーのリスト][8]を参照してください。 

###  Braze SDKの統合 
Braze SDK には、ユーザーデータを収集して統合されたユーザープロファイルに同期することと、プッシュ通知、アプリ内メッセージ、コンテンツカードなどのメッセージングチャネルに電力を供給することの2 つの重要な機能が用意されています。 

{% alert tip %}
アプリまたはサイトと完全に統合すると、Braze SDK は完全に実現されたレベルのマーケティングの高度化を実現します。Braze SDK の統合を延期すると、ドキュメントに記載されている機能の一部が使用できなくなります。
{% endalert %}

SDK インプリメンテーションでは、次の操作を実行します。
\* サポートする各プラットフォームのSDK 統合コードを記述します。
\* 各プラットフォームのメッセージングチャネルを有効化し、メール、SMS、プッシュ通知、およびその他のチャネルで、Braze SDK が顧客とのやり取りからデータを追跡できるようにします。
\* 計画された[UI コンポーネントカスタマイズ][6] を作成します(たとえば、カスタムコンテンツカード)。完全にカスタムのコンテンツの場合、SDK の自動データ収集では新しいコンポーネントが認識されないため、分析をログに記録する必要があります。この実装は、デフォルトのコンポーネントでパターン化できます。


###  Braze API の使用
Braze を使用すると、REST API を使用してさまざまなタスクをさまざまな時点で実行できます。ろう付けAPI は、以下の場合に役立ちます。
1. 履歴データのインポート
2. Braze でトリガーされない継続的な更新。たとえば、ユーザープロファイルはアプリにログインせずにVIP にアップグレードされるため、API はこの情報をBraze に通信する必要があります。

[Braze API の使用を開始します。][9]

{% alert important %}
API の使用中は、リクエストをバッチ処理し、デルタ値のみを送信するようにしてください。Braze は、送信されるすべての属性を再書き込みします。値が変更されていない場合は、カスタム属性を更新しないでください。
{% endalert %}

### 製品分析のセットアップ
ろう付けはすべてデータに関するものである。 Braze 内のデータは、ユーザープロファイルに保存されます。 

データポイントは、"any" any&quotではなく、マーケターに適したデータを確実に取り込むための構造です。データをバキュームアップすることができます。[データポイント][10]について理解しておきます。

### レガシーユーザーデータの移行
Braze [/users/track endpoint][17] を使用して、Braze の外部に記録された履歴データを移行できます。一般的にインポートされるデータの例には、プッシュトークンおよび過去の購入が含まれます。このエンドポイントは、1回限りのインポートまたは定期的なバッチ更新に使用できます。 

また、ユーザーをインポートし、ワンタイム[CSV アップロード][18] を介して顧客属性値をダッシュボードに更新することもできます。CSV のアップロードはマーケターにとって役立ちますが、REST API を使用すると柔軟性が向上します。

### セッショントラッキングの設定
Braze SDK は、"open session"および"close session"データポイントを生成します。また、Braze SDK は定期的にデータをフラッシュします。セッショントラッキングのデフォルト値については、これらのリンクを参照してください。これらのリンクはすべてカスタマイズできます([Android][19]、[iOS][20]、[web][21])。

### カスタムイベント、属性、および購入イベントの追跡
チームと調整し、カスタムイベント、ユーザー属性、購入イベントなど、計画されたデータスキーマを設定します。[カスタムデータスキーム][22] はダッシュボードを使用して入力され、SDK 統合時に実装するものと正確に一致する必要があります。

{% alert tip %}
`external_id`s in Braze と呼ばれるユーザID は、すべての既知のユーザに設定する必要があります。これらは、ユーザーがアプリを開いたときに変更されず、アクセス可能である必要があります。これにより、デバイスとプラットフォーム間でユーザーを追跡できます。ベストプラクティスについては、[User lifecycle]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/)の記事を参照してください。
{% endalert %}

### その他のツール
ユースケースに応じて、他に設定が必要なツールがある場合があります。たとえば、[geofences][24] のようなツールを設定して、ユーザのストーリーを実現する必要がある場合があります。本質的な統合手順を完了した後に、これらの追加ツールを設定する能力を持つ顧客が最も成功していることがわかりました。

## 品質保証 {#qa}
統合を実行すると、設定しているすべての機能が期待どおりに動作していることを確認するための品質保証が提供されます。このQAは、データ取り込みとメッセージチャネルの2つの一般的なカテゴリに分類される。

{% alert important %}
QAを開始する前に、本番環境とテスト環境が設定されていることを確認してください。
{% endalert %}

| **QA データ取り込み**|**QA メッセージ**|
|---------------------------|---------------------------------------------------------------|
| データの取り込み、保存、およびエクスポートの方法をQA にします。| メッセージがユーザーに正しく送信され、すべてがすばらしく見えることを確認します。|
| データが正しく保存されていることを確認するためのテストを実行します。| ユーザのセグメントを作成します。|
| セッションデータが、Braze 内の目的のワークスペースに正しく割り当てられていることを確認します。| キャンペーンとキャンバスを正常に起動します。|
| セッションの開始と終了が記録されていることを確認します。| 正しいユーザーセグメントに正しいキャンペーンが表示されていることを確認します。|
| ユーザープロファイルに対してユーザー属性情報が正しく記録されていることを確認します。| プッシュトークンが正しく登録されていることを確認します。|
| カスタムデータがユーザープロファイルに対して正しく記録されていることをテストします。| プッシュトークンが正しく削除されていることを確認します。|
| 匿名ユーザープロファイルを作成します。| プッシュキャンペーンがデバイスに正しく送信されているかどうかをテストし、エンゲージメントが記録されます。|
| `changeUser()` メソッドが呼び出されたときに、匿名ユーザープロファイルが既知のユーザープロファイルになることを確認します。| アプリ内メッセージが配信され、メトリックがログに記録されることをテストします。|
|                           | コンテンツカードが配信され、メトリックがログに記録されるかどうかをテストします。|
|                           | 接続されたコンテンツ(AccuWeather など)を容易にします。|
|                           | すべてのメッセージチャネル統合が適切に連携していることを確認します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}



### マーケターに Braze を渡す
プラットフォームまたはサイトを統合したら、マーケティングチームを関与させてプラットフォームの所有権をそれらに渡すことができます。このプロセスは、すべての企業で異なりますが、次のようなことが考えられます。
\* 複合体[液体ロジック][25]
* [電子メールIPウォーミング][26]を促進するヘルプ
\* 追跡されるデータの種類を他の利害関係者に理解させる

### 将来に向けて発展させる
コードベースを継承し、最初の開発者が何を考えていたのか手がかりがなかったことはありますか?悪いことに、あなたはコードを書いて、完全に理解し、1年後にそれに戻ってきたとき、完全に困惑したと感じたことがありますか? 

Braze に乗船する際、データ、ユーザープロファイル、どのような統合が適用範囲内であったか、また適用範囲外であったか、カスタマイズがどのように機能するべきか、さらには、あなたの心の中に新鮮さを感じ、それゆえに明白であることを、あなたが総合的に判断します。あなたのチームがBrazeを拡張したい場合、または他の技術リソースがあなたのBrazeプロジェクトに割り当てられた場合、この情報は不明瞭になります。

技術概要セッションで学習した情報を確定するためのリソースを作成します。このリソースは、チームに参加した新しい開発者を迅速に乗船させるのに役立ちます(または、現在のBraze 実装を拡張する必要がある場合に、自分自身へのリマインダーとして役立ちます)。 

## メンテナンス {#maintenance}
マーケターに引き継いだ後も、メンテナンスのためのリソースとしての役割を果たし続けます。Braze SDK に影響を与える可能性のあるiOS およびAndroid のアップデートに注意を払い、サードパーティベンダーが最新であることを確認します。 

Braze プラットフォームへの更新は、Braze [GitHub][23] で追跡します。場合によっては、管理者がBraze から緊急アップデートやバグ修正に関するメールを直接受け取ることもあります。 




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