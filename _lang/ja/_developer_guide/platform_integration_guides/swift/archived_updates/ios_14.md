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

> このガイドでは、iOS 14で導入されたBraze関連の変更と、Braze iOS SDK統合に必要なアップグレード手順について説明する。iOS 14の新しいアップデートの完全なリストについては、アップルの[iOS 14ページを](https://www.apple.com/ios/ios-14/)参照のこと。

{% alert tip %}
iOS 14.5以降、**IDFAの**収集と[特定のデータ共有には](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track)、新しい[AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency)フレームワークの許可プロンプトが必要になる[（詳細はこちら）](#idfa)。
{% endalert %}

#### iOS 14の変更点のまとめ

- iOS 14 / Xcode 12をターゲットとするアプリは、我々の[公式iOS 14リリースを][1]使用しなければならない。
- [iOSでは][4]、新しい「_おおよその位置情報」_パーミッションを選択したユーザーのジオフェンスは[サポートされなくなった][4]。
- Last Known Location」ターゲティング機能の使用には、_おおよその位置情報_許可との互換性のため、Braze iOS SDK v3.26.1+へのアップグレードが必要。Xcode 12を使っている場合は、少なくともv3.27.0にアップグレードする必要がある。
- iOS 14.5以降、IDFAの収集と[特定のデータ共有には][5]、新しい[AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency)フレームワークの許可プロンプトが必要となる。
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
|Xcode 12|**iOS SDK v3.27以降にアップグレードする。**|Xcode 12を使用している顧客は、互換性のためにv3.27.0+を使用しなければならない。もしiOS 14との互換性に関する問題や質問があれば、[GitHubの][2]新しい[課題を開いて][2]ほしい。|
|直近の所在地| **iOS SDK v3.26.1以降にアップグレードする。**|直近の場所ターゲティング機能を使用し、まだXcode 11を使用している場合は、新しい_近似位置_機能をサポートする少なくともiOS SDK v3.26.1にアップグレードする必要がある。古いSDKは、ユーザーがiOS 14にアップグレード_し、_"おおよその位置 "を選択した場合、確実に位置情報を収集することができない。<br><br>あなたのアプリがiOS 14をターゲットにしていなくても、ユーザーがiOS 14にアップグレードし、新しい位置情報精度オプションを使い始めるかもしれない。iOS SDK v3.26.1+にアップグレードしていないアプリは、iOS 14デバイスでユーザーが_おおよその位置情報を_提供した場合、位置情報を確実に収集することができない。|
|IDFA広告トラッキングID| **Xcode 12とiOS SDK v3.27へのアップグレードが必要な場合がある。**|2021年のある時点で、アップルはIDFAの収集に許可プロンプトを要求し始めるだろう。その時点で、アプリはXcode 12にアップグレードし、IDFAの収集を継続するために新しい`AppTrackingTransparency` フレームワークを使用しなければならない。IDFAをBraze SDKに渡す場合は、その時点でv3.27.0+にアップグレードする必要がある。<br><br>新しいiOS 14のAPIを使用していないアプリは、2021年にアップルがこの変更を実施し始めた後、IDFAを収集することができなくなり、代わりに空白のID（`00000000-0000-0000-0000-000000000000` ）を収集することになる。あなたのアプリに適用されるかどうかの詳細については、[IDFAの詳細を](#idfa)参照のこと。|


## iOS 14の動作変更

### おおよその場所の許可

![正確な位置]({% image_buster /assets/img/ios/ios14-approximate-location.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

#### 概要

位置情報の許可をリクエストする際、ユーザーは_正確な位置情報_（以前の動作_）を_提供するか、新しい_おおよその位置情報を_提供するかを選択できるようになった。おおよその位置は、正確な座標ではなく、ユーザーがいる半径を大きくして返す。

#### ジオフェンス  {#geofences}

[iOSでは][4]、新しい「_おおよその位置情報」_パーミッションを選択したユーザーのジオフェンスは[サポートされなくなった][4]。Braze SDKの統合にアップデートは必要ないが、ジオフェンスに依存するキャンペーンについては、[ロケーションベースのマーケティング戦略を](https://www.braze.com/blog/geofencing-geo-targeting-beaconing-when-to-use/)調整する必要があるかもしれない。

#### ロケーション・ターゲティング {#location-tracking}

_おおよその位置情報が_付与された場合に、ユーザーの_最終既知位置情報の_収集を継続するには、アプリをBraze iOS SDKの少なくともv3.26.1にアップグレードする必要がある。私たちのテストでは、12,000メートル（7マイル以上）以上であった。Brazeダッシュボードの_最終地点_ターゲットオプションを使用する際は、新しい_おおよその位置を_考慮し、位置の半径を必ず大きくすること（少なくとも半径1マイル/1.6kmを推奨）。

Braze iOS SDKを少なくともv3.26.1にアップグレードしていないアプリは、iOS 14デバイスで_おおよその位置情報が_付与された場合、位置情報トラッキングを使用できなくなる。

すでに位置情報アクセスを許可しているユーザーは、アップグレード後も_正確な位置情報を_提供し続ける。

Xcode 12を使っている場合は、少なくともv3.27.0にアップグレードする必要がある。

おおよその位置情報の詳細については、Appleの[What's New In Location](https://developer.apple.com/videos/play/wwdc2020/10660/)WWDC Videoを参照のこと。

### IDFAとアプリ追跡の透明性 {#idfa}

#### 概要

IDFA（Identifier for Advertisers）は、広告およびアトリビューション・パートナーとのクロスデバイス・トラッキングのためにAppleが提供する識別子であり、個人のApple IDに紐付けられている。

iOS 14.5からは、IDFAに対する明示的なユーザーの同意を収集するために、新しい許可プロンプト（新しい`AppTrackingTransparency` フレームワークによって起動される）を表示する必要がある。他社が所有するアプリやウェブサイトを横断してあなたを追跡する」ためのこの許可プロンプトは、ユーザーに位置情報を要求するプロンプトと同様に要求される。

ユーザーがプロンプトを受け入れない場合、または Xcode 12 の`AppTrackingTransparency` フレームワークにアップグレードしない場合、空白の IDFA 値 (`00000000-0000-0000-0000-000000000000`) が返され、アプリは再度ユーザーにプロンプトを出すことができない。

{% alert important %}
これらのIDFAアップデートは、エンドユーザーがデバイスをiOS 14.5にアップグレードした後に有効になる。IDFAの収集を計画している場合は、アプリがXcode 12で新しい`AppTransparencyFramework` 。
{% endalert %}

#### ブレイズIDFAコレクションの変更点
![IDFA]({% image_buster /assets/img/ios/ios14-idfa.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

1. Brazeは今後も、アプリがユーザーのIDFA値をBraze_SDKに_提供できるようにする。

2. オプションの自動IDFAコレクションで条件付きコンパイルを行う`ABK_ENABLE_IDFA_COLLECTION` コンパイルマクロは、iOS 14では機能しなくなり、3.27.0では削除された。 

3. キャンペーンターゲティングやアナリティクスのために "Ad Tracking Enabled "フィールドを使用する場合は、Xcode 12にアップグレードし、新しいAppTrackingTransparencyフレームワークを使用して、ユーザーのオプトインステータスを報告する必要がある。この変更の理由は、iOS 14では古い [`advertisingTrackingEnabled`](https://developer.apple.com/documentation/adsupport/asidentifiermanager/1614148-advertisingtrackingenabled)フィールドは常にNoを返すからだ。

4. あなたのアプリがBrazeの外部IDとしてIDFAまたはIDFVを使用していた場合、これらの識別子からUUIDに移行することを強く推奨する。外部IDの移行に関する詳細は、[外部ID移行APIエンドポイントを]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/)参照のこと。

アップルによる[プライバシーに関するアップデートと](https://developer.apple.com/app-store/user-privacy-and-data-use/)、新しい[App Tracking Transparencyフレームワークについての](https://developer.apple.com/documentation/apptrackingtransparency)詳細を読む。

### プッシュ認証 {#push-provisional-auth}

{% alert important %}
iOS 14では、暫定プッシュ認証に変更はない。iOS14の以前のベータ版で、アップルは変更を導入したが、その後、以前の動作に戻されている。
{% endalert %}

## iOS 14の新機能

### アプリのプライバシーとデータ収集の概要 {#app-privacy}

2020年12月8日以降、App Storeへのすべての投稿は、[アップルの新しいAppプライバシー基準を](https://developer.apple.com/app-store/app-privacy-details/)遵守するための追加ステップが必要となる。

#### アップル開発者ポータル アンケート

_Apple Developer Portalで_：
* あなたのアプリやサードパーティパートナーがどのようにデータを収集しているか、アンケートに記入してもらう。
  * このアンケートは、App Storeに掲載されている最新のリリースを常に反映したものであることが求められる。
  * アンケートは、新しいアプリが提出されなくても更新される可能性がある。
* あなたのアプリのプライバシーポリシーURLへのリンクを貼り付ける必要がある。

質問票に記入する際には、法務チームに相談し、以下の分野でのBrazeの使用が開示要件にどのように影響するかを検討すること。

#### ブレイズのデフォルトデータ収集
**識別子**\- 匿名のデバイス識別子は、Braze SDKによって常に収集される。これは現在、デバイスのIDFV（ベンダーの識別子）に設定されている。

**使用データ**\- これには、Brazeのセッションデータ、および製品のインタラクションを測定するために使用するイベントまたは属性の収集が含まれる。

#### オプションのデータ収集
Brazeの使用を通じて任意に収集される可能性のあるデータ：

**位置情報**\- Braze SDKは、オプションで、おおよその位置情報と正確な位置情報の両方を収集することができる。これらの機能はデフォルトでは無効になっている。

**連絡先情報**\- これには、ユーザーのIDに関連するイベントや属性を含めることができる。

**購入**\- これは、ユーザーに代わって記録されたイベントや購入を含むことができる。

{% alert important %}
これは網羅的なリストではないことに注意してほしい。Brazeでユーザーに関するその他の情報を手動で収集し、アプリプライバシー調査票の他のカテゴリーに該当する場合は、それらも開示する必要がある。
{% endalert %}

この機能の詳細については、[Appleのプライバシーとデータ利用を](https://developer.apple.com/app-store/user-privacy-and-data-use/)参照のこと。

[1]: https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.27.0
[2]: https://github.com/Appboy/appboy-ios-sdk/issues
[4]: https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization
[5]: https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track
