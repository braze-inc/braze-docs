---
nav_title: その他の SDK のカスタマイズ
article_title: iOS 向けのその他の SDK カスタマイズ
platform: iOS
description: "この参照記事では、ログレベル、IDFA 収集、その他のカスタマイズなどの SDK のカスタマイズについて説明します。"
page_order: 3

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# その他の SDK のカスタマイズ

## Braze ログレベル

Braze iOS SDK のデフォルトのログレベルは最小 (次の表では `8`) です。このレベルでは、ほとんどのロギングが抑制されるため、本番リリースのアプリケーションで機密情報がログに記録されることはありません。

次の使用可能なログレベルのリストを参照してください。

### ログレベル

| レベル    | 説明 |
|----------|-------------|
| 0        | 詳細。すべてのログ情報はiOSコンソールに記録される。  |
| 1        | デバッグ。デバッグとそれ以上のログ情報はiOSコンソールに記録される。  |
| 2        | 警告。警告以上のログ情報はiOSコンソールに記録される。  |
| 4        | エラー。エラーとそれ以上のログ情報はiOSコンソールに記録される。  |
| 8        | 最小限。最小限の情報が iOS コンソールに記録されます。SDKのデフォルト設定。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 詳細なログ記録

ログレベルは、使用可能な任意の値に構成できます。ただし、ログレベルを verbose または `0` に設定すると、統合に関する問題のデバッグに非常に役立ちます。このレベルは開発環境のみを対象としており、リリースされたアプリケーションでは設定しないでください。詳細なログ記録では、追加のユーザー情報や新しいユーザー情報が Braze に送信されることはありません。

### ログレベルの設定

ログレベルはコンパイル時または実行時に割り当てることができます。

{% tabs local %}
{% tab Compile Time %}

`Braze` という名前の辞書を `Info.plist` ファイルへ追加します。`Braze` 辞書内で、`LogLevel` 文字列サブエントリを追加し、値を `0` に設定します。 

{% alert note %}
Braze iOS SDK v4.0.2 より前では、辞書キー `Appboy` を `Braze` の代わりに使用する必要があります。
{% endalert %} 

例 `Info.plist` コンテンツ:

```
<key>Braze</key>
<dict>
  <key>LogLevel</key>
  <string>0</string>
</dict>
```

{% endtab %}
{% tab Runtime %}

`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` に渡された `appboyOptions` パラメーター内に `ABKLogLevelKey` を追加します。その値を整数 `0` に設定します。

{% subtabs %}
{% subtab OBJECTIVE-C %}

```objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKLogLevelKey] = @(0);
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endsubtab %}
{% subtab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  ABKLogLevelKey : 0
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
ログレベルは、Braze iOS SDK v4.4.0 以降で実行時にのみ設定できます。それ以前のバージョンの SDK を使用している場合は、代わりにコンパイル時にログレベルを設定します。
{% endalert %} 

{% endtab %}
{% endtabs %}

## オプションの IDFV 収集 - Swift

Braze iOS Swift SDK の以前のバージョンでは、IDFV （ベンダーの識別子) フィールドがユーザーのデバイス ID として自動的に収集されました。 

Swift SDK v5.7.0 以降では、IDFV フィールドをオプションで無効にすることができ、代わりに Braze はランダムな UUID をデバイス ID として設定します。詳細については、「[IDFV の収集]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift)」を参照してください。

## オプションの IDFA 収集

IDFA 収集は Braze SDK 内ではオプションであり、デフォルトでは無効になっています。IDFA 収集は、[インストールアトリビューション統合]({{site.baseurl}}/partners/message_orchestration/attribution/adjust/)を利用する場合にのみ Braze 内で必要になります。IDFA を保存することを選択した場合は、無料で保存されるため、追加の開発作業を行わずに、リリース後すぐにこれらのオプションを利用できます。

そのため、次の基準のいずれかを満たしている場合は、引き続き IDFA を収集することをお勧めします。

- アプリのインストールが以前に配信された広告に起因している
- アプリケーション内のアクションが以前に配信された広告に起因している

### iOS 14.5 アプリトラッキングの透明性

Apple は、IDFA を収集するためにユーザーに許可プロンプトを通じてオプトインすることを要求しています。

IDFA を収集するには、`ABKIDFADelegate` プロトコルを実装するだけでなく、アプリケーションでは、アプリトラッキングの透過性フレームワークで Apple の `ATTrackingManager` を使用してユーザーから承認を要求する必要があります。詳細については、Apple の[ユーザー プライバシーに関する記事](https://developer.apple.com/app-store/user-privacy-and-data-use/)を参照してください。

アプリトラッキングの透明性承認のプロンプトには、識別子の使用法を説明する `Info.plist` エントリが必要です。

```
<key>NSUserTrackingUsageDescription</key>
<string>To retarget ads and build a global profile to better serve you things you would like.</string>
```

### IDFA 収集の実装

IDFA 収集を実装するには、次の手順に従います。

##### ステップ1:ABKIDFADelegate を実装する

[`ABKIDFADelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKIDFADelegate.h) プロトコルに準拠したクラスを作成します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
#import "IDFADelegate.h"
#import <AdSupport/ASIdentifierManager.h>
#import <AppTrackingTransparency/AppTrackingTransparency.h>

@implementation IDFADelegate

- (NSString *)advertisingIdentifierString {
  return [[[ASIdentifierManager sharedManager] advertisingIdentifier] UUIDString];
}

- (BOOL)isAdvertisingTrackingEnabledOrATTAuthorized {
  if (@available(iOS 14, *)) {
    return [ATTrackingManager trackingAuthorizationStatus] == ATTrackingManagerAuthorizationStatusAuthorized;
  }
  return [[ASIdentifierManager sharedManager] isAdvertisingTrackingEnabled];
}

@end
```

{% endtab %}
{% tab swift %}

```swift
import Appboy_iOS_SDK
import AdSupport
import AppTrackingTransparency

class IDFADelegate: NSObject, ABKIDFADelegate {
   func advertisingIdentifierString() -> String {
    return ASIdentifierManager.shared().advertisingIdentifier.uuidString
  }

  func isAdvertisingTrackingEnabledOrATTAuthorized() -> Bool {
    if #available(iOS 14, *) {
      return ATTrackingManager.trackingAuthorizationStatus ==  ATTrackingManager.AuthorizationStatus.authorized
    }
    return ASIdentifierManager.shared().isAdvertisingTrackingEnabled
  }
}
```
{% endtab %}
{% endtabs %}

##### ステップ2:Braze の初期化中にデリゲートを設定する

`startWithApiKey:inApplication:withAppboyOptions:` に渡された `appboyOptions` 辞書で、`ABKIDFADelegateKey` キーを `ABKIDFADelegate` 準拠クラスのインスタンスに設定します。

## iOS SDKのおおよそのサイズ {#ios-sdk-size}

iOS SDK フレームワークファイルのおおよそのサイズは 30 MB、.ipa (アプリ ファイルへの追加) のおおよそのサイズは 1 MB ～ 2 MB です。

Brazeは、[アプリのサイズ設定に関する Apple の推奨事項](https://developer.apple.com/library/content/qa/qa1795/_index.html)に従って、SDK が `.ipa` のサイズに与える影響を観察することで、iOS SDK のサイズを測定します。アプリケーションに追加される iOS SDK のサイズを計算する場合は、[「アプリサイズレポートの取得」](https://developer.apple.com/library/content/qa/qa1795/_index.html)に従って、Braze iOS SDK を統合する前と後の `.ipa` のサイズの違いを比較することをお勧めします。アプリの縮小サイズレポートからサイズを比較する場合は、縮小された `.ipa` ファイルのアプリサイズを確認することもお勧めします。ユニバーサル `.ipa` ファイルは、App Store からダウンロードしてユーザーのデバイスにインストールしたバイナリーよりも大きくなるためです。

{% alert note %}
CocoaPods 経由で `use_frameworks!` と統合する場合は、正確なサイズ設定のためにターゲットのビルド設定で `Enable Bitcode = NO` を設定します。
{% endalert %}

