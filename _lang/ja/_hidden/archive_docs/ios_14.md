---
nav_title: iOS 14 アップグレードガイド
article_title: iOS 14 SDK アップグレードガイド
page_order: 7
platform: iOS
description: "このリファレンス記事では、iOS 14 SDK のアップデート、ジオフェンス、ロケーションターゲティング、IDFA などの変更点を強調表示します。"
hidden: true
permalink: "/ios_14/"

---

# iOS 14 SDKアップグレードガイド

このガイドでは、iOS 14 で導入されたBraze関連の変更点と、Braze iOS SDK 統合に必要なアップグレード手順について説明します。

新しいiOS 14 アップデートの完全なリストについては、Apple の[iOS 14 ページ](https://www.apple.com/ios/ios-14/) を参照してください。

{% alert tip %}
iOS 14.5 では、**IDFA** コレクションと[特定のデータ共有](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track) には、新しい[AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency) Framework パーミッションプロンプト([Learn More](#idfa)) が必要です。
{% endalert %}

#### iOS 14 の変更点の概要

- iOS 14 / Xcode 12をターゲットとするアプリは、[公式iOS 14リリース][1]を使用する必要があります。
- 新しい_おおよその場所_権限を選択したユーザーの[がiOS][4]でサポートされなくなりました。
- "Last Known Location"ターゲティング機能を使用するには、_おおよそのロケーション_権限との互換性のために、Braze iOS SDK v3.26.1+へのアップグレードが必要です。Xcode 12 を使用している場合は、少なくともv3.27.0 にアップグレードする必要があります。
- iOS 14.5 以降、IDFA コレクションおよび[特定のデータ共有][5] には、新しい[AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency) Framework パーミッションプロンプトが必要です。
- "Ad Tracking Enabled"フィールドを使用してキャンペーンターゲティングまたはアナリティクスを行う場合は、Xcode 12にアップグレードし、新しいAppTrackingTransparencyフレームワークを使用してユーザのオプトインステータスを報告する必要があります。

## アップグレードの概要

<style>
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2) {
    min-width:230px;
}
table td {
    word-break: break-word;
}
</style>

|アプリが使用する場合:|アップグレードの推奨事項|説明|
|------|--------|---|
|Xcode 12|**iOS SDK v3.27 以降へのアップグレード**|Xcode 12 を使用するお客様は、互換性のためにv3.27.0+ を使用する必要があります。iOS 14 の互換性に関する問題や質問が発生した場合は、新しい[GitHub の問題][2].|を開きます。
最近使った場所| **iOS SDK v3.26.1以降へのアップグレード**|最新の場所のターゲット機能を使用し、Xcode 11をまだ使用している場合は、新しい_おおよその場所_機能をサポートする少なくともiOS SDK v3.26.1にアップグレードする必要があります。iOS 14 _および_にユーザーがApproximate Locationを選択した場合、古いSDKではロケーションを確実に収集できません。<br><br>アプリがiOS 14をターゲットにしない場合でも、ユーザーはiOS 14にアップグレードして、新しい位置精度オプションの使用を開始することができます。iOS SDK v3.26.1+ にアップグレードしないアプリは、ユーザーがiOS 14 デバイスで_おおよそのロケーション_ を提供すると、ロケーション属性を確実に収集できなくなります。|
|IDFA Ad Tracking ID|**Xcode 12およびiOS SDK v3.27へのアップグレードが必要な場合があります**|2021年に、アップルがIDFAの収集の許可プロンプトを要求し始めることがあります。その際、アプリはXcode 12 にアップグレードし、IDFA の収集を継続するために新しい`AppTrackingTransparency` フレームワークを使用する必要があります。IDFA をBraze SDK に渡す場合は、その時点でv3.27.0+ にもアップグレードする必要があります。<br><br>新しいiOS 14 API を使用しないアプリはIDFA を収集できず、代わりにApple が2021年にこの変更を実施し始めた後に空白のID (`00000000-0000-0000-0000-000000000000`) を収集します。これがアプリに適用されるかどうかの詳細については、[IDFAの詳細](#idfa).|を参照してください。


## iOS 14の動作の変更

### おおよその位置許可

![Precise Location]({% image_buster /assets/img/ios/ios14-approximate-location.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

#### 概要

ロケーション権限をリクエストするとき、ユーザは_正確なロケーション_ (以前の動作)、または新しい_おおよそのロケーション_を提供する選択肢があります。おおよその位置は、正確な座標の代わりに、ユーザが位置するより大きな半径を返します。

#### ジオフェンス  {#geofences}

新しい_おおよその場所_権限を選択したユーザーの[がiOS][4]でサポートされなくなりました。Braze SDK の統合には更新は必要ありませんが、ジオフェンスに依存するキャンペーンでは、[ロケーションベースのマーケティング戦略](https://www.braze.com/blog/geofencing-geo-targeting-beaconing-when-to-use/) を調整する必要がある場合があります。

#### 立地目標 {#location-tracking}

_おおよそのロケーション_が付与されたときに、ユーザーの_最新の既知のロケーション_を引き続き収集するには、アプリは少なくともBraze iOS SDK のv3.26.1 にアップグレードする必要があります。場所の精度が低下することに留意してください。私たちのテストによれば、12,000メートル(7マイル以上)まで上昇しています。Braze ダッシュボードで_最新の既知のロケーション_ ターゲットオプションを使用する場合は、新しい_およそのロケーション_ を考慮してロケーションの半径を増やしてください(半径1.6km あたり1 マイル以上を推奨します)。

Braze iOS SDK を少なくともv3.26.1 にアップグレードしないアプリは、iOS 14 デバイスで_おおよそのロケーション_ が付与された場合、ロケーショントラッキングを使用できなくなります。

すでにロケーションアクセスを許可されているユーザーは、アップグレード後も引き続き_正確なロケーション_ を提供します。

Xcode 12 を使用している場合は、少なくともv3.27.0 にアップグレードする必要があります。

おおよその場所の詳細については、Appleの[What's New In Location](https://developer.apple.com/videos/play/wwdc2020/10660/) WWWDCビデオを参照してください。

### IDFAとアプリのトラッキングの透明性 {#idfa}

#### 概要

IDFA (Identifier for Advertisers) は、クロスデバイストラッキングのための広告および属性パートナーと共に使用するためにApple が提供する識別子で、個人のApple ID に関連付けられています。

iOS 14.5 以降、IDFA の明示的なユーザ同意を収集するには、新しい権限プロンプト(新しい`AppTrackingTransparency` フレームワークによって起動される) を表示する必要があります。この許可プロンプトは、" 他社が所有するアプリやウェブサイト間で追跡します。ユーザーに場所を要求するように促すのと同じように、要求されます。

ユーザーがプロンプトを受け入れない場合、またはXcode 12 の`AppTrackingTransparency` フレームワークにアップグレードしない場合、空のIDFA 値(`00000000-0000-0000-0000-000000000000`) が返され、アプリはユーザーに再度プロンプトを出すことができません。

{% alert important %}
これらのIDFAアップデートは、エンドユーザーがデバイスをiOS 14.5にアップグレードした後に有効になります。IDFA を収集する場合は、アプリで新しい`AppTransparencyFramework` とXcode 12 が使用されていることを確認します。
{% endalert %}

#### ろう付けIDFAコレクションの変更
![IDFA]({% image_buster /assets/img/ios/ios14-idfa.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

1. Brazeは引き続き、アプリがユーザーのIDFA値_から_のBraze SDKを提供できるようにします。

2. オプションの自動IDFA コレクションで条件付きでコンパイルする`ABK_ENABLE_IDFA_COLLECTION` コンパイルマクロは、iOS 14 では機能しなくなり、3.27.0 で削除されました。 

3. "Ad Tracking Enabled"フィールドを使用してキャンペーンターゲティングまたはアナリティクスを行う場合は、Xcode 12にアップグレードし、新しいAppTrackingTransparencyフレームワークを使用してユーザのオプトインステータスを報告する必要があります。この変更の理由は、iOS 14 では、古い[`advertisingTrackingEnabled`](https://developer.apple.com/documentation/adsupport/asidentifiermanager/1614148-advertisingtrackingenabled) フィールドが常にNo を返すためです。

4. アプリケーションでBraze外部ID としてIDFA またはIDFV を使用している場合は、UUID を優先してこれらのID から移行することを強くお勧めします。外部ID の移行の詳細については、[外部ID 移行API エンドポイント]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/) を参照してください。

Apple の[プライバシーアップデート](https://developer.apple.com/app-store/user-privacy-and-data-use/) と新しい[App Tracking Transparency framework](https://developer.apple.com/documentation/apptrackingtransparency) について詳しく説明します。

### プッシュ認証 {#push-provisional-auth}

{% alert important %}
iOS 14には、暫定プッシュ認証への変更は含まれていません。iOS 14 の以前のベータ版では、Apple は以前の動作に戻した変更を導入しました。
{% endalert %}

## iOS 14の新機能

### アプリのプライバシーとデータ収集の概要 {#app-privacy}

2020年12月8日以降、App Storeへのすべての提出には、[Appleの新しいApp Privacy standards](https://developer.apple.com/app-store/app-privacy-details/)に従うための追加ステップが必要です。

#### アップル社の開発者向けポータルアンケート

On the _Apple Developer Portal_:
\* アプリまたはサードパーティのパートナーがどのようにデータを収集するかを説明するアンケートに記入するよう求められます。
  \* アンケートは、App Storeの最新リリースで常に最新の状態になることが期待されます。
  \* アンケートは、新しいアプリの投稿がなくても更新される場合があります。
\* アプリのプライバシーポリシーURL にリンクを貼り付ける必要があります。

アンケートに記入する際には、法務チームに相談し、以下の項目についてのBrazeの使用が、あなたの開示要件にどのように影響するかを検討してください。

#### ろう付けデフォルトデータ収集
**識別子** \- 匿名デバイス識別子は、常にBraze SDK によって収集されます。これは現在、デバイスIDFV(ベンダーの識別子)に設定されています。

**使用状況データ** \- これには、製品の相互作用を測定するために使用するイベントまたは属性コレクションと同様に、Braze のセッションデータを含めることができます。

#### オプションのデータ収集
オプションで、Braze を使用して収集するデータ:

**ロケーション** \- おおよそのロケーションと正確なロケーションの両方を、オプションでBraze SDK で収集することができます。これらの機能はデフォルトで無効になっています。

**Contact Info** -これには、ユーザのID に関連するイベントと属性を含めることができます。

**購入** \- これには、ユーザに代わってログオンしたイベントや購入を含めることができます。

{% alert important %}
これは完全なリストではないことに注意してください。App Privacy Questionnaireの他のカテゴリーに適用されるBrazeのユーザーに関する他の情報を手動で収集する場合は、それらも開示する必要があります。
{% endalert %}

この機能の詳細については、[Appleのプライバシーとデータ使用](https://developer.apple.com/app-store/user-privacy-and-data-use/)を参照してください。

[1]: https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.27.0
[2]: https://github.com/Appboy/appboy-ios-sdk/issues
[4]: https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization
[5]: https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track
