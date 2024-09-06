---
nav_title: アンドロイド12アップグレードガイド
article_title: アンドロイド12アップグレードガイド
page_order: 9
permalink: "/android_12/"
layout: "dev_guide"
hidden: true
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、Android 12 SDKのアップデートを取り上げ、ディープリンクやSDKの互換性などの変更点を紹介している。"
---

# Android 12 SDK アップグレードガイド

このガイドでは、Android 12 (2021)で導入された関連する変更と、Braze Android SDK統合に必要なアップグレード手順について説明する。

Android 12への完全な移行ガイドについては、[Android開発者向けドキュメントを](https://developer.android.com/about/versions/12)参照のこと。

## Braze SDKの互換性

Android 12をターゲットとする場合は、[Braze Android SDK v13.1.2+を][1]使用する必要がある。まだアンドロイド12をターゲットにしていない場合は、アップグレードすることをお勧めする。

**Braze Android SDKをアップグレードしないとどうなるか？**

* Androidの[終了システムダイアログの](https://developer.android.com/about/versions/12/behavior-changes-all#close-system-dialogs)変更により、Braze Android SDKの古いバージョンでは、Android 12を実行しているデバイスでプッシュ通知を受信すると警告が記録される。この動作は、アプリがアンドロイド12をターゲットにしていなくても発生する。
* [コンポーネントのエクスポート](https://developer.android.com/about/versions/12/behavior-changes-12#exported)、[保留中のインテント](https://developer.android.com/about/versions/12/behavior-changes-12#pending-intent-mutability)、および[通知トランポリンの](https://developer.android.com/about/versions/12/behavior-changes-12#notification-trampolines)変更は、アプリをコンパイルする能力に影響を与えたり、Braze SDKの初期化を妨げる可能性がある。この動作は、アンドロイド12をターゲットにしたアプリでのみ発生する。
* [カスタムプッシュ通知の](https://developer.android.com/about/versions/12/behavior-changes-12#custom-notifications)変更により、新しい[Androidインライン画像プッシュ]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/inline_image_push/)機能のレイアウトが変更された。この動作は、アンドロイド12をターゲットにしたアプリでのみ発生する。

[1]: https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1312
