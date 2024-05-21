---
nav_title: アンドロイド 11 アップグレードガイド
article_title: アンドロイド 11 アップグレードガイド
page_order: 9
platform: 
  - Android
  - FireOS
description: "この参考記事では Android 11 SDK のアップデートについて説明し、ディープリンクや SDK の互換性などの変更点に焦点を当てています。"
hidden: true
---

# アンドロイド 11 SDK アップグレードガイド

このガイドでは、Android 11（2020 年 9 月 8 日リリース）で導入された関連する変更点と、Braze Android SDK を統合するために必要なアップグレード手順について説明します。

Android 11 の完全な移行ガイドについては、[Android デベロッパー向けドキュメントをご覧ください](https://developer.android.com/preview/migration)。

## Braze SDK との互換性

Android 11（API 30）_をターゲットとするすべてのアプリを_ Braze メッセージング機能を引き続き使用するには、[Braze Android SDK v8.1.0+][1] にアップグレードする必要があります。

{% alert important %}
Android 11 の API の変更により、Android 11 をターゲットとするアプリで Braze Android SDK v8.1.0 以降にアップグレードしない場合、Braze UI コンポーネントからのディープリンクで問題が発生し、カスタム HTML アプリ内メッセージが正しく表示されなくなります。
{% endalert %}

### ディープリンク

Android 11 以降（API バージョン 30+）をターゲットとするアプリは、Braze メッセージ内のディープリンクを引き続き使用するには、[Braze Android SDK v8.1.0][1] にアップグレードする必要があります。Android 11 APIの変更により、少なくともAndroid SDK v8.1.0にアップグレードしないアプリでは、Brazeメッセージ（アプリ内メッセージまたはコンテンツカード）内のディープリンクに関する問題が発生します。

### HTML アプリ内メッセージ

Android 11 以降（API バージョン 30 以降）をターゲットとするアプリで、カスタム HTML アプリ内メッセージを引き続き使用するには、Braze Android SDK v8.1.0 にアップグレードする必要があります。Android 11 WebView 設定の変更により、[Braze][1] Android SDK v8.1.0 にアップグレードするまで、Android 11 の対象アプリに HTML アプリ内メッセージが正しく表示されません。 

### 位置情報権限

位置情報権限を使用するアプリは、位置情報へのアクセスをリクエストする際に Android [のベストプラクティスに従う必要があります](https://developer.android.com/preview/privacy/location#change-details)。これらの位置情報の更新では、Braze インテグレーションを変更する必要はありません。

## アンドロイド 11 の動作変更

### 1 回だけ権限を許可

ユーザーは、位置情報収集などの権限を1回だけ付与できるようになりました（詳細については、[Androidドキュメントを参照してください](https://developer.android.com/preview/privacy/location#one-time-access)）。アプリを閉じたり、バックグラウンドで長時間放置したりすると、その権限は自動的に取り消されます。アプリは、今後必要になったときにこの権限を再リクエストする必要があります。位置情報権限のリクエストの推奨フローをすでに実行しているアプリは、1 回限りの権限をサポートします。

![][3]{: height="230px" }

### バックグラウンド位置情報の許可

Android 11 では、アプリは最初にフォアグラウンド位置情報の許可をリクエストする必要があります。その後、アプリがバックグラウンドになった後、ユーザーにバックグラウンド位置情報の許可を再度求める場合があります。
Geofencesを使用しているお客様は、アプリがバックグラウンド位置情報権限の収集に関するAndroidの推奨事項に従っていることを確認する必要があります。詳細については、[Android ドキュメントを参照してください](https://developer.android.com/preview/privacy/location#background-location)。

[1]: https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#810
[3]: {% image_buster /assets/img/android/android-11-one-time-permission.svg %}
