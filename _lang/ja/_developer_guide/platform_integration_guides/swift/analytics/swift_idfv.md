---
nav_title: IDV の収集
article_title: IDV の収集
platform: Swift
page_type: reference
description: "このリファレンス記事では、Swift SDK のオプションの IDFV フィールドを収集する方法について説明します。"
page_order: 4

---

# IDV の収集 

## バックグラウンド

Braze iOS SDK の以前のバージョンでは、IDFV (ベンダーの識別子) フィールドがユーザーのデバイス ID として自動的に収集されていました。Swift SDK v5.7.0より、IDFV フィールドがオプションで無効にされ、代わりに Braze でランダムな UUID がデバイス ID として設定されていました。Swift SDK v7.0.0以降、IDFV フィールドはデフォルトで収集されず、代わりに UUID がデバイス ID として設定されます。

`useUUIDAsDeviceId` 機能により、デバイス ID を UUID として設定するよう [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) が構成されます。従来、iOS SDK では Apple が生成した IDFV 値と同じデバイス ID が割り当てられていました。iOS アプリでこの機能がデフォルトで有効になっている場合、SDK を介して作成されたすべての新規ユーザーに、UUID と同じデバイス ID が割り当てられます。

IDFV を個別に収集する場合は、[こちら](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:))の説明に従い、Swift SDK を使用して収集できます。

## 考慮事項

### SDK バージョン

Swift SDK v7.0.0以降、`useUUIDAsDeviceId` が有効 (デフォルト) である場合、作成されたすべての新規ユーザーにランダムなデバイス ID が割り当てられます。既存のユーザーは、すべて同じデバイス ID 値を保持します。これは、IDFV である場合もあります。

この機能が有効でない場合、デバイスには引き続き作成時に IDFV が割り当てられます。

### ダウンストリーム 

**テクノロジーパートナー**: この機能を有効にすると、Braze デバイス ID から IDFV 値を取得するテクノロジーパートナーは、このデータにアクセスできなくなります。デバイスから取得された IDFV 値がパートナー連携に必要な場合は、この機能を true に設定することをお勧めします。

**Currents**: `useUUIDAsDeviceId` が true に設定されている場合、Currents で送信されたデバイス ID は IDFV 値と等しくなくなります。

## よくある質問

#### この変更は Braze の既存ユーザーに影響しますか?
いいえ。この機能を有効にしても、Braze のユーザーデータは上書きされません。デバイスが新たに作成された後 (または `wipedata()` が呼び出された後) にのみ、新しい UUID デバイス ID が生成されます。

#### この機能をオンにした後にオフにすることはできますか?
はい、この機能はオンとオフを自由に切り替えることができます。以前に保存されたデバイス ID は上書きされません。

#### Braze を介し、IDFV 値を別の場所で収集することはできますか?
はい、オプションで Swift SDK を使用して IDFV を収集することもできます (収集はデフォルトでは無効です)。 
