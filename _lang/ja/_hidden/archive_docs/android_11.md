---
nav_title: 第11Androidアップグレードガイド
article_title: 第11Androidアップグレードガイド
page_order: 9
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、Android 11 SDK 更新について説明し、ディープリンク、互換性SDKなどの変更点を強調します。"
hidden: true
---

# Android 11 SDK アップグレードの手引き

本書では、Android 11(2020年9 月8 日リリース)で導入された関連する変更点と、Braze Android SDKインテグレーションに必要なアップグレード ステップs について説明します。

Android 11の完全なマイグレーションガイドについては、[Android 開発者 ドキュメント](https://developer.android.com/preview/migration)を参照してください。

## Braze SDK適合性

Braze メッセージング 機能を引き続き使用するには、_target_ Android 11 (API 30) が[ Braze Android SDK v8.1.0+][1] にアップグレードする必要があるすべてのアプリ。

{% alert important %}
Android 11 のAPI の変更により、Braze Android SDK v8.1.0+ にアップグレードしないAndroid 11 をターゲットとするアプリでは、Braze UI コンポーネントからのディープリンクに問題が発生し、カスタムHTML アプリ内メッセージs が正しく表示されません。
{% endalert %}

### ディープリンク

Android 11 以降(API Version 30+)をターゲットとするアプリケーションは、[ Braze Android SDK v8.1.0][1] にアップグレードして、Braze メッセージ内のディープリンクを引き続き使用する必要があります。Android 11 API の変更により、少なくともAndroid SDK v8.1.0 にアップグレードしないアプリ s では、Brazeメッセージ(アプリ内メッセージまたはコンテンツカード) 内の深いリンクに問題が発生します。

### HTML アプリ内メッセージs

Android 11 以降(API バージョン30 以降) をターゲットとするアプリは、カスタムHTML アプリ内メッセージs を引き続き使用するには、Braze Android SDK v8.1.0 にアップグレードする必要があります。Android 11 WebView 設定 s の変更により、[ Braze Android SDK v8.1.0][1] にアップグレードするまで、HTML アプリ内メッセージ s はAndroid 11 ターゲットアプリs に正しく表示されません。 

### ロケーション権限

ロケーションアクセス許可を使用するアプリケーションは、ロケーションアクセスをリクエストするときに、Androidの[ベストプラクティス](https://developer.android.com/preview/privacy/location#change-details)に従う必要があります。これらの場所更新s では、Brazeインテグレーションを変更する必要はありません。

## Android 11の挙動変化

### 許可を1 回許可

ユーザは、ロケーションコレクションなどの権限を1 回限りで付与できるようになりました(詳細については、[ Android Docs](https://developer.android.com/preview/privacy/location#one-time-access) を参照してください)。アプリがクローズされた後、またはバックグラウンドで十分な時間が経過すると、その権限は自動的に取り消されます。アプリは、今後必要に応じてこの権限を再要求する必要があります。ロケーション権限を要求するための推奨フローにすでに従うアプリケーションは、1 回限りの権限をサポートします。

![][3]{: height="230px" }

### バックグラウンドロケーション許可

Android 11 は、最初にフォアグラウンドロケーション権限をリクエストするためにアプリ s を必要とします。その後、アプリがバックグラウンドに入った後、バックグラウンドロケーション権限を再度ユーザーに要求する場合があります。
Geofencesを使用するお客様は、アプリがバックグラウンド場所の権限の収集に関するAndroidの推奨事項に従っていることを確認する必要があります。詳細については、[Android文書](https://developer.android.com/preview/privacy/location#background-location)を参照してください。

[1]: https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#810
[3]: {% image_buster /assets/img/android/android-11-one-time-permission.svg %}
