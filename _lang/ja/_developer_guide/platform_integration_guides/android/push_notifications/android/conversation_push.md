---
nav_title: 会話プッシュ
article_title: Android 向け会話プッシュ
platform: Android
page_order: 5.92
description: "このアプリケーションでは、Android アプリケーションに Android 会話プッシュを実装する方法を説明します。"
channel:
  - push

---

# 会話プッシュ

> このアプリケーションでは、Android アプリケーションに Android 会話プッシュを実装する方法を説明します。

![]({% image_buster /assets/img/android/push/conversations_android.png %}){: style="float:right;max-width:35%;margin-left:15px;border: 0;"}

[人と会話のイニシアチブ](https://developer.android.com/guide/topics/ui/conversations)は、スマートフォンのシステム上で人との会話を向上させることを目的とした、複数年にわたる Android の取り組みです。人との会話を優先する理由は、他のユーザーとのコミュニケーションや対話が、あらゆるユーザー層にわたる大多数のユーザーにとって、依然として最も価値のある重要な機能分野であるからです。

この機能を使用するために、追加の統合や SDK の変更は必要となりません。最小バージョン要件を満たしていないデバイスまたは SDK では、代わりに標準のプッシュ通知が表示されます。

## 使用要件

- この通知タイプには、Braze Android SDK v15.0.0 以降と Android 11 以降が搭載されたデバイスが必要です。 
- サポートされていないデバイスや SDK は、標準のプッシュ通知にフォールバックします。

この機能は、Braze REST API 経由でのみ利用できます。詳細については、[Android プッシュオブジェクト]({{site.baseurl}}/api/objects_filters/messaging/android_object#android-conversation-push-object)を参照してください。

