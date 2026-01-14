---
nav_title: Android 12 アップグレード ガイド
article_title: Android 12アップグレードガイド
page_order: 9
permalink: "/android_12/"
layout: "dev_guide"
hidden: true
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、Android 12 SDK の更新について説明し、ディープリンク、SDK 互換性などの変更点を取り上げます。"
---

# Android 12 SDK アップグレードガイド

このガイドでは、Android 12 (2021) で導入された関連のある変更と、Braze Android SDK 統合に必要なアップグレード手順について説明します。

Android 12 の完全な移行ガイドについては、[Android 開発者のドキュメント](https://developer.android.com/about/versions/12)を参照してください。

## Braze SDK適合性

Android 12 を対象とする場合は、[Braze Android SDK v 13.1.2以降](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1312)を使用する必要があります。まだ Android 12 を対象にしていない場合でも、アップグレードをお勧めします。

**Braze Android SDKをアップグレードしないとどうなるか？**

* Androidの[終了システムダイアログの](https://developer.android.com/about/versions/12/behavior-changes-all#close-system-dialogs)変更により、Braze Android SDKの古いバージョンでは、Android 12を実行しているデバイスでプッシュ通知を受信すると警告が記録される。この動作は、アプリがAndroid 12 を対象にしていない場合でも発生します。
* [コンポーネントのエクスポート](https://developer.android.com/about/versions/12/behavior-changes-12#exported)、[保留中のインテント](https://developer.android.com/about/versions/12/behavior-changes-12#pending-intent-mutability)、[通知トランポリン](https://developer.android.com/about/versions/12/behavior-changes-12#notification-trampolines)の変更は、アプリをコンパイルする機能に影響を与えたり、Braze SDK の初期化を妨げたりする可能性があります。この動作は、Android 12 を対象とするアプリケーションでのみ発生します。
* [カスタムプッシュ通知の](https://developer.android.com/about/versions/12/behavior-changes-12#custom-notifications)変更により、新しい[Androidインライン画像プッシュ]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_sending-inline-images)機能のレイアウトが変更された。この動作は、Android 12 を対象とするアプリケーションでのみ発生します。

