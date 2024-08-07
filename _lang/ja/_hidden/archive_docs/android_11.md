---
nav_title: Android 11 アップグレードガイド
article_title: Android 11 アップグレードガイド
page_order: 9
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、Android 11 SDKのアップデートを取り上げ、ディープリンクやSDKの互換性などの変更点を紹介している。"
hidden: true
---

# Android 11 SDK アップグレードガイド

このガイドでは、Android 11（2020年9月8日リリース）で導入された関連する変更点と、Braze Android SDK統合に必要なアップグレード手順について説明する。

アンドロイド11の完全な移行ガイドについては、[アンドロイド開発者向けドキュメントを](https://developer.android.com/preview/migration)参照のこと。

## Braze SDKの互換性

Android 11（API 30）を_ターゲットと_するすべてのアプリは、[Brazeの][1]メッセージング機能を引き続き使用するために、[Braze Android SDK v8.1.0+に][1]アップグレードする必要がある。

{% alert important %}
Android 11のAPIの変更により、Braze Android SDK v8.1.0+にアップグレードしていないAndroid 11をターゲットとしたアプリでは、Braze UIコンポーネントからのディープリンクに問題が発生し、カスタムHTMLアプリ内メッセージが正しく表示されない。
{% endalert %}

### ディープリンク

Android 11以降（APIバージョン30以上）をターゲットとするアプリは、[Braze][1]メッセージ内でディープリンクを使用し続けるために、[Braze Android SDK v8.1.0に][1]アップグレードする必要がある。Android 11のAPIの変更により、少なくともAndroid SDK v8.1.0にアップグレードしていないアプリでは、Brazeメッセージ（アプリ内メッセージまたはコンテンツカード）内のディープリンクに問題が発生する。

### HTMLアプリ内メッセージ

Android 11以降（APIバージョン30以上）をターゲットとするアプリは、カスタムHTMLアプリ内メッセージを継続して使用するために、Braze Android SDK v8.1.0にアップグレードする必要がある。Android 11のWebView設定の変更により、[Braze Android SDK v8.1.0に][1]アップグレードするまで、Android 11をターゲットとしたアプリでHTMLアプリ内メッセージが正しく表示されない。 

### 場所の許可

位置情報パーミッションを使用するアプリは、位置情報アクセスを要求する際、Androidの[ベストプラクティスに](https://developer.android.com/preview/privacy/location#change-details)従うべきである。これらの位置情報の更新のために、Brazeとの統合を変更する必要はない。

## Android 11の動作変更

### パーミッションを一度許可する

ユーザーは、位置情報の収集などの権限を1回限り付与できるようになった（詳細は[Android Docsを](https://developer.android.com/preview/privacy/location#one-time-access)参照）。アプリが閉じられたり、バックグラウンドに長時間いたりすると、その許可は自動的に取り消される。アプリは、将来必要なときにこの許可を再要求する必要がある。位置情報の許可を要求するための推奨フローにすでに従っているアプリは、1回限りの許可をサポートする。

![][3]{: height="230px" }

### 背景位置の許可

Android 11では、アプリはまずフォアグラウンドでの位置情報の許可を要求し、アプリがバックグラウンドになった後、バックグラウンドでの位置情報の許可を再度ユーザーに要求する可能性がある。
Geofencesを使用する顧客は、アプリがバックグラウンドでの位置情報許可収集に関するAndroidの推奨に従っていることを確認する必要がある。詳細は[Android Docsを](https://developer.android.com/preview/privacy/location#background-location)参照のこと。

[1]: https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#810
[3]: {% image_buster /assets/img/android/android-11-one-time-permission.svg %}
