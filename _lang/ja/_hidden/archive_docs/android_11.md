---
nav_title: Android 11アップグレードガイド
article_title: 第11Androidアップグレードガイド
page_order: 9
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、Android 11 SDK の更新について説明し、ディープリンク、SDK 互換性などの変更点を取り上げます。"
hidden: true
---

# Android 11 SDK アップグレードの手引き

このガイドでは、Android 11 (2020年9月8日リリース) で導入された関連のある変更と、Braze Android SDK 統合に必要なアップグレード手順について説明します。

Android 11の完全なマイグレーションガイドについては、[Android 開発者 ドキュメント](https://developer.android.com/preview/migration)を参照してください。

## Braze SDK適合性

Android 11 (API 30) を_対象とする_すべてのアプリで Brazeメッセージング機能を引き続き使用するには、[Braze Android SDK v8.1.0以降](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#810)にアップグレードする必要があります。

{% alert important %}
Android 11 の API の変更により、Braze Android SDK v8.1.0以降にアップグレードしていない Android 11向けのアプリでは、Braze UI コンポーネントからのディープリンクで問題が発生し、カスタム HTML アプリ内メッセージが正常に表示されません。
{% endalert %}

### ディープリンク

Android 11 以降(API Version 30+)をターゲットとするアプリケーションは、[ Braze Android SDK v8.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#810) にアップグレードして、Braze メッセージ内のディープリンクを引き続き使用する必要があります。Android 11の API の変更により、Android SDK v8.1.0以降にアップグレードしないアプリでは、Braze メッセージ (アプリ内メッセージまたはコンテンツカード) 内のディープリンクで問題が発生します。

### HTML アプリ内メッセージs

Android 11以降 (APIバージョン30以上) を対象にしたアプリは、カスタム HTML のアプリ内メッセージを引き続き使用するには、Braze Android SDK v8.1.0にアップグレードする必要があります。Android 11 WebView の設定が変更されたため、Android 11 対象アプリでは[Braze Android SDK v8.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#810) にアップグレードするまで、HTML アプリ内メッセージが適切に表示されません。 

### 位置情報の許可

ロケーションアクセス許可を使用するアプリケーションは、ロケーションアクセスをリクエストするときに、Androidの[ベストプラクティス](https://developer.android.com/preview/privacy/location#change-details)に従う必要があります。これらの位置情報の更新には、Braze 統合への変更は必要ありません。

## Android 11の挙動変化

### 1回限りのアクセスを許可する

ユーザは、ロケーションコレクションなどの権限を1 回限りで付与できるようになりました(詳細については、[ Android Docs](https://developer.android.com/preview/privacy/location#one-time-access) を参照してください)。アプリが閉じられた後、またはバックグラウンドで十分な時間が経過すると、その権限は自動的に取り消されます。アプリは、今後必要に応じてこの権限を再要求する必要があります。位置情報の許可を要求するための推奨フローにすでに従っているアプリでは、1回限りのアクセス許可がサポートされます。

![]({% image_buster /assets/img/android/android-11-one-time-permission.svg %}){: height="230px" }

### バックグラウンドでの位置情報許可

Android 11 では、アプリは最初にフォアグラウンドでの位置情報の許可を要求する必要があり、アプリがバックグラウンドになったら、バックグラウンドでの位置情報の許可をユーザーに再度求めることができます。
ジオフェンスを使用する顧客は、バックグラウンドでの位置情報の許可の収集に関する Android の推奨事項にアプリが従っていることを確認する必要があります。詳細については、[Android文書](https://developer.android.com/preview/privacy/location#background-location)を参照してください。

