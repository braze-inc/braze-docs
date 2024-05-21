---
nav_title: Android 12 アップグレード ガイド
article_title: Android 12 アップグレード ガイド
page_order: 9
permalink: "/android_12/"
layout: "dev_guide"
hidden: true
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、Android 12 SDK アップデートについて説明し、ディープリンク、SDK の互換性などの変更点に焦点を当てています。"
---

# Android 12 SDK アップグレード ガイド

このガイドでは、Android 12 (2021) で導入された関連する変更と、Braze Android SDK 統合に必要なアップグレード手順について説明します。

Android 12 の完全な移行ガイドについては、[Android 開発者向けドキュメント](https://developer.android.com/about/versions/12)をご覧ください。

## Braze SDK の互換性

Android 12 をターゲットとする場合は、[Braze Android SDK v13.1.2+][1]を使用する必要があります。まだ Android 12 をターゲットにしていない場合でも、アップグレードすることをお勧めします。

**Braze Android SDK をアップグレードしないとどうなりますか?**

* Android の [終了システム ダイアログ](https://developer.android.com/about/versions/12/behavior-changes-all#close-system-dialogs)の変更により、Android 12 を実行しているデバイスでプッシュ通知を受信すると、古いバージョンの Braze Android SDK で警告がログに記録されます。この動作は、アプリが Android 12 をターゲットにしていない場合でも発生します。
* [コンポーネントのエクスポート](https://developer.android.com/about/versions/12/behavior-changes-12#exported)、 [保留中のインテント](https://developer.android.com/about/versions/12/behavior-changes-12#pending-intent-mutability)、 [通知トランポリン](https://developer.android.com/about/versions/12/behavior-changes-12#notification-trampolines) の変更により、アプリのコンパイル機能に影響が出たり、Braze SDK の初期化が妨げられたりする可能性があります。この動作は、Android 12 をターゲットとするアプリでのみ発生します。
* [カスタム プッシュ通知](https://developer.android.com/about/versions/12/behavior-changes-12#custom-notifications) の変更により、新しい [Android インライン画像プッシュ]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/inline_image_push/) 機能のレイアウトが変更されました。この動作は、Android 12 をターゲットとするアプリでのみ発生します。

[1]: https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1312
