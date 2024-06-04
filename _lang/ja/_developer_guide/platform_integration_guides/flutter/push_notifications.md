---
nav_title: プッシュ通知
article_title: Flutter のプッシュ通知
platform: Flutter
page_order: 2
description: "この記事では、Flutter でのプッシュ通知の実装とテストについて説明します。"
channel: push

---

# プッシュ通知の統合

> プッシュ通知は、重要なアップデートが発生したときにユーザーの画面に表示されるアプリ外のアラートです。プッシュ通知は、時間的制約があって関連性の高いコンテンツをユーザーに提供したり、ユーザーをアプリに再エンゲージしたりするための効果的な方法です。この記事では、Flutter でのプッシュ通知の実装とテストについて説明します。

{% alert important %}
Braze は、プッシュ通知またはディープリンクを送信するための Flutter ラッパーレイヤーの使用をサポートしていません。Flutter アプリでこの機能を使用するには、ネイティブプラットフォームごとに個別にプッシュ通知を構成する必要があります。
- **Android:**[Android の統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/)に従ってください。
- **iOS:**[iOS の統合手順](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b1-standard-push-notifications)に従ってください。
{% endalert %}


## プッシュ通知をテストする

ネイティブレイヤーでプッシュ通知を構成したら、次の手順に従ってプッシュ統合をテストします。

{% alert note %}
Xcode 14 では、iOS シミュレーター上でリモートプッシュ通知をテストできます。
{% endalert %}

1. Flutter アプリケーションでアクティブユーザーを設定します。これを行うには、`braze.changeUser('your-user-id')` を呼び出してプラグインを初期化します。
2. [**キャンペーン**] に移動し、新しいプッシュ通知キャンペーンを作成します。テストしたいプラットフォームを選択します。
3. テスト通知を作成し、[**テスト**] タブに移動します。テストユーザーと同じ `user-id` を追加し、[**テストを送信**] をクリックします。
4. まもなくデバイスに通知が届くはずです。通知が表示されない場合は、通知センターで確認するか、設定を更新する必要が生じる場合があります。
