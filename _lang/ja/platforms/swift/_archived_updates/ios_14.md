---
nav_title: iOS 14アップグレードガイド
article_title: iOS 14 SDKアップグレードガイド
page_order: 7
platform: iOS
description: "この参考記事では、iOS 14 SDKのアップデートを取り上げ、ジオフェンス、ロケーション・ターゲティング、IDFAなどの変更点を紹介している。"
hidden: true
noindex: true
---

# iOS 14 SDKアップグレードガイド

> このガイドでは、iOS 14で導入されたBraze関連の変更と、Braze iOS SDK統合に必要なアップグレード手順について説明する。iOS 14 の新しい更新の完全なリストについては、Apple の[iOS 14 ページ](https://www.apple.com/ios/ios-14/)を参照してください。

{% alert tip %}
iOS 14.5以降、**IDFAの**収集と[特定のデータ共有には](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track)、新しい[AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency)フレームワークの許可プロンプトが必要になる[（詳細はこちら）](#idfa)。
{% endalert %}

#### iOS 14の変更点のまとめ

- iOS 14 / Xcode 12 を対象とするアプリは、[公式 iOS 14 リリース](https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.27.0)を使用する必要があります。
- iOS では、新しい「_おおよその位置情報」_パーミッションを選択したユーザーのジオフェンスは[サポートされなくなった](https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization)。
- Last Known Location」ターゲティング機能の使用には、_おおよその位置情報_許可との互換性のため、Braze iOS SDK v3.26.1+へのアップグレードが必要。Xcode 12 を使っている場合は、v3.27.0 以降にアップグレードする必要があります。
- iOS 14.5以降、IDFAの収集と[特定のデータ共有には](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track)、新しい[AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency)フレームワークの許可プロンプトが必要となる。
- キャンペーンターゲティングやアナリティクスのために "Ad Tracking Enabled "フィールドを使用する場合、Xcode 12にアップグレードし、ユーザーのオプトインステータスを報告するために新しいAppTrackingTransparencyフレームワークを使用する必要がある。

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

|あなたのアプリが使用する場合：|アップグレードの推奨|説明|
|------|--------|---|
|Xcode 12|**iOS SDK v3.27以降にアップグレードする。**|Xcode 12 を使用している顧客は、互換性を確保するために v3.27.0 以降を使用する必要があります。iOS 14 の互換性に関連する問題や質問が生じた場合は、新しい [GitHub issue](https://github.com/Appboy/appboy-ios-sdk/issues) を開いてください。|
|最新の位置情報| **iOS SDK v3.26.1以降にアップグレードする。**|最新の位置情報ターゲティング機能を使用し、まだ Xcode 11 を使用している場合は、新しい_おおよそのロケーション_機能をサポートする iOS SDK v3.26.1 以降にアップグレードする必要があります。古いSDKは、ユーザーがiOS 14にアップグレード_し、_"おおよその位置 "を選択した場合、確実に位置情報を収集することができない。<br><br>あなたのアプリがiOS 14をターゲットにしていなくても、ユーザーがiOS 14にアップグレードし、新しい位置情報精度オプションを使い始めるかもしれない。iOS SDK v3.26.1+にアップグレードしていないアプリは、iOS 14デバイスでユーザーが_おおよその位置情報を_提供した場合、位置情報を確実に収集することができない。|
|IDFA広告トラッキングID| **Xcode 12とiOS SDK v3.27へのアップグレードが必要な場合がある。**|2021年のある時点で、Apple は IDFA の収集に許可プロンプトを要求し始める予定です。その時点で、IDFA の収集を続行するには、アプリを Xcode 12 にアップグレードし、新しい `AppTrackingTransparency` フレームワークを使用する必要があります。IDFA を Braze SDK に渡す場合は、その時点で v3.27.0 以降にアップグレードする必要もあります。<br><br>新しいiOS 14のAPIを使用していないアプリは、2021年にアップルがこの変更を実施し始めた後、IDFAを収集することができなくなり、代わりに空白のID（`00000000-0000-0000-0000-000000000000` ）を収集することになる。アプリに適用されるかどうかの詳細については、[IDFA の詳細](#idfa)を参照してください。|


## iOS 14の動作変更

### おおよその位置情報の許可

![正確な位置]({% image_buster /assets/img/ios/ios14-approximate-location.png %})({: style="float:right;max-width:45%;margin-left:15px;"})

#### 概要

位置情報の許可をリクエストする際、ユーザーは_正確な位置情報_ (以前の動作) を提供するか、新しい_おおよその位置情報_を提供するかを選択できるようになりました。おおよその位置は、正確な座標ではなく、ユーザーがいる半径を大きくして返す。

#### ジオフェンス  {#geofences}

iOS では、新しい「_おおよその位置情報」_パーミッションを選択したユーザーのジオフェンスは[サポートされなくなった](https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization)。Braze SDKの統合にアップデートは必要ないが、ジオフェンスに依存するキャンペーンについては、[ロケーションベースのマーケティング戦略を](https://www.braze.com/blog/geofencing-geo-targeting-beaconing-when-to-use/)調整する必要があるかもしれない。

#### ロケーションターゲティング {#location-tracking}

_おおよその位置情報_が付与されたときにユーザーの_最新の既知の位置情報_を引き続き収集するには、アプリを v3.26.1 以上の Braze iOS SDK にアップグレードする必要があります。ただし、位置情報は精度が低くなることに留意してください。当社のテストでは精度が最大で12,000 メートル (7 マイル以上) に達しました。Brazeダッシュボードの_最終地点_ターゲットオプションを使用する際は、新しい_おおよその位置を_考慮し、位置の半径を必ず大きくすること（少なくとも半径1マイル/1.6kmを推奨）。

Braze iOS SDK を v3.26.1 以降にアップグレードしていないアプリでは、iOS 14 デバイスで_おおよその位置情報_が付与された場合、位置情報トラッキングを使用できなくなります。

すでに位置情報アクセスを許可しているユーザーは、アップグレード後も_正確な位置情報を_提供し続ける。

Xcode 12 を使っている場合は、v3.27.0 以降にアップグレードする必要があります。

おおよその位置情報の詳細については、Appleの[What's New In Location](https://developer.apple.com/videos/play/wwdc2020/10660/)WWDC Videoを参照のこと。

### IDFAとアプリ追跡の透明性 {#idfa}

#### 概要

IDFA（Identifier for Advertisers）は、広告およびアトリビューション・パートナーとのクロスデバイス・トラッキングのためにAppleが提供する識別子であり、個人のApple IDに紐付けられている。

iOS 14.5 からは、IDFA に対する明示的なユーザーの同意を収集するために、新しい許可プロンプト (新しい`AppTrackingTransparency` フレームワークによって起動される) を表示する必要があります。「他社が所有するアプリや Web サイトでユーザーを追跡する」ためのこの許可プロンプトは、位置情報をリクエストするようにユーザーにプロンプトを出すのと同じようにリクエストされます。

ユーザーがプロンプトを受け入れない場合、またはあなたが Xcode 12 の `AppTrackingTransparency` フレームワークにアップグレードしない場合、空白の IDFA 値 (`00000000-0000-0000-0000-000000000000`) が返され、アプリは再度ユーザーにプロンプトを出すことができなくなります。

{% alert important %}
これらのIDFAアップデートは、エンドユーザーがデバイスをiOS 14.5にアップグレードした後に有効になる。IDFA の収集を計画している場合は、Xcode 12 でアプリが新しい `AppTransparencyFramework` を使用していることを確認します。
{% endalert %}

#### Braze IDFA コレクションの変更点
IDFA、

1. Braze は、アプリがユーザーの IDFA 値を Braze SDK _に_提供することを引き続き許可します。

2. オプションの自動IDFAコレクションで条件付きコンパイルを行う`ABK_ENABLE_IDFA_COLLECTION` コンパイルマクロは、iOS 14では機能しなくなり、3.27.0では削除された。 

3. キャンペーンターゲティングやアナリティクスのために "Ad Tracking Enabled "フィールドを使用する場合は、Xcode 12にアップグレードし、新しいAppTrackingTransparencyフレームワークを使用して、ユーザーのオプトインステータスを報告する必要がある。この変更の理由は、iOS 14では古い [`advertisingTrackingEnabled`](https://developer.apple.com/documentation/adsupport/asidentifiermanager/1614148-advertisingtrackingenabled)フィールドは常にNoを返すからだ。

4. あなたのアプリがBrazeの外部IDとしてIDFAまたはIDFVを使用していた場合、これらの識別子からUUIDに移行することを強く推奨する。外部 ID の移行に関する詳細については、[外部 ID 移行 API エンドポイント]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/)を参照してください。

Apple の[プライバシーに関する更新](https://developer.apple.com/app-store/user-privacy-and-data-use/)と新しい[アプリトラッキングの透明性フレームワーク](https://developer.apple.com/documentation/apptrackingtransparency)については、こちらをご覧ください。

### プッシュ認証 {#push-provisional-auth}

{% alert important %}
iOS 14 には、暫定プッシュ承認に関する変更は含まれていません。iOS 14 の以前のベータ版で、Apple は変更を導入しましたが、その後以前の動作に戻されています。
{% endalert %}

## iOS 14の新機能

### アプリのプライバシーとデータ収集の概要 {#app-privacy}

2020年12月8日以降、App Store へのすべての提出は、[Apple の新しい App Privacy 基準](https://developer.apple.com/app-store/app-privacy-details/)を遵守するための追加のステップが必要となります。

#### アップル開発者ポータル アンケート

_Apple Developer Portalで_：
* アプリまたはサードパーティパートナーがデータを収集する方法を説明するアンケートに記入するよう求められます。
  * このアンケートは、App Storeに掲載されている最新のリリースを常に反映したものであることが求められる。
  * アンケートは、新しいアプリが提出されなくても更新される可能性があります。
* あなたのアプリのプライバシーポリシーURLへのリンクを貼り付ける必要がある。

質問票に記入する際には、法務チームに相談し、以下の分野でのBrazeの使用が開示要件にどのように影響するかを検討すること。

#### Braze のデフォルトのデータ収集
**識別子** \- 匿名のデバイス識別子は、Braze SDK によって常に収集されます。これは現在、デバイスの IDFV (ベンダーの識別子) に設定されています。

**利用データ**\- Brazeのセッションデータ、および製品のインタラクションを測定するために使用するイベントまたは属性収集が含まれる。

#### オプションのデータ収集
Brazeの使用を通じて任意に収集される可能性のあるデータ：

**位置情報**\- Braze SDKは、オプションで、おおよその位置情報と正確な位置情報の両方を収集することができる。これらの機能はデフォルトでは無効になっています。

**連絡先情報**\- これには、ユーザーのIDに関連するイベントや属性を含めることができる。

**購入** \- これには、ユーザーの代わりに記録されたイベントや購入が含まれる可能性があります。

{% alert important %}
これは網羅的なリストではないことに注意してほしい。Braze で、ユーザーに関するその他の情報を手動で収集する場合に、その情報が App Privacy Questionnaire の他のカテゴリに該当する場合は、それらも開示する必要があります。
{% endalert %}

この機能の詳細については、[Apple のプライバシーとデータ利用](https://developer.apple.com/app-store/user-privacy-and-data-use/)を参照してください。

