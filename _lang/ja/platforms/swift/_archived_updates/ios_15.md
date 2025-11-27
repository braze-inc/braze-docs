---
nav_title: iOS 15 アップグレード ガイド
article_title: iOS 15 SDKアップグレードガイド
page_order: 7
platform: iOS
description: "このリファレンス記事では、新しい iOS 15 OS 更新、必要な SDK 更新、および新機能について説明します。"
hidden: true
noindex: true
---

# iOS 15 SDK アップグレードガイド

> 本書では、iOS 15 (WWDC21) で導入された変更点と、Braze iOS SDK 統合に必要なアップグレードステップについて説明します。iOS 15 の新しい更新の完全なリストについては、Apple の [iOS 15 リリースノート](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-15-release-notes)を参照してください。


## UI ナビゲーションへの透明性の変更

iOS ベータ版の年次テストの一環として、特定の UI ナビゲーションバーが非透過ではなく透明に表示される Apple によって行われた変更を確認しました。これは、コンテンツカード用のBraze のデフォルトUI を使用している場合、または別のブラウザアプリではなくアプリ内でWeb ディープリンクが開かれている場合に、iOS 15 で表示されます。

iOS 15 でのこのような視覚的な変更を回避するために、ユーザーが新しい iOS 15 オペレーティングシステムへのアップグレードを開始する前に、できるだけ早く [Braze iOS SDK v 4.3.2](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.3.2) にアップグレードすることを強くお勧めします。

## 新通知 設定s {#notification-settings}

iOS 15 では新しい通知機能が導入され、ユーザーは1日を通して集中力を保ち、頻繁な作業の中断を避けることができます。私たちは、これらの新機能のサポートを提供できることを楽しみにしています。これらの機能は、追加の SDK アップグレードを必要とせず、iOS 15 デバイスのユーザーにのみ適用されます。

### フォーカスモード {#focus-mode}

iOS 15 のユーザーは、「フォーカスモード」を作成できるようになりました。これは、フォーカスモードを中断して目立つように表示する通知を指定するためのカスタムプロファイルです。

![]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

### 割り込みレベル {#interruption-levels}

iOS 15 では、プッシュ通知は次の4つの中断レベルのいずれかで送信できます。

* **パッシブ** (新規) - サウンドなし、バイブレーションなし、画面のスリープ解除なし、フォーカス設定の突破なし。
* **アクティブ** (デフォルト) - サウンド、バイブレーション、画面のスリープ解除を許可し、フォーカス設定の突破は許可しません。
* **時間的制約** (新規) - サウンド、バイブレーション、画面のスリープ解除を許可し、許可されている場合はシステムコントロールを突破できます。
* **重大** \- サウンド、バイブレーション、画面のスリープ解除を許可し、システムコントロールを突破し、サイレントスイッチをバイパスできます。

iOS プッシュでこのオプションを設定する方法の詳細については、[iOS 通知オプション]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#interruption-level)を参照してください。

### 通知の概要 {#notification-summary}

![]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15 では、ユーザーは、(オプションで) 1日の中で特定の時間を選択して、通知の要約を受け取ることができます。即時の注意を必要としない通知 (「パッシブ」として送信されたり、ユーザーがフォーカスモードになっている間に送信されたりする) は、1日を通じて絶えず中断されないようにグループ化されます。

送信する通知ごとに、「関連性スコア」を指定して、どの通知を概要の先頭に表示するかをコントロールできるようになります。

通知の"関連性スコア"の設定方法については、[iOS 通知 Options]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#relevance-score)を参照してください。

## 位置情報ボタン {#location-buttons}

iOS 15 では、ユーザーがアプリ内で位置情報へのアクセス一時的に許可する新しい便利な方法が導入されています。 

新しい場所ボタンは、既存の「1度のみ許可」アクセス許可を基にしており、同じセッションで複数回クリックするユーザーに繰り返しプロンプトを表示することはありません。

詳細については、今年の世界開発者会議 (WWDC) での Apple の動画 [Meet the Location Button](https://developer.apple.com/videos/play/wwdc2021/10102/) をご覧ください。

{% alert tip %}
この機能により、ユーザーに権限を要求することができます。iOS 15 より前に位置情報の許可を拒否したことがあるユーザーは、位置情報ボタンをクリックすると、許可を拒否した状態から最後にリセットする機会としてプロンプトが表示されます。
{% endalert %}

### Braze で位置情報ボタンを利用する

Brazeで位置ボタンを使用する場合は、追加の統合は必要ありません。アプリは、通常どおり (権限が付与されたら)ユーザーの場所を渡し続ける必要があります。

Apple によると、すでにバックグラウンドでの位置情報へのアクセスを共有しているユーザーについては、iOS 15 にアップグレードした後も「アプリの使用中」オプションで、引き続きそのレベルの許可が与えられます。

## Apple メール {#mail}

今年、Apple はメールのトラッキングとプライバシーに関する多くの更新を発表しました。詳細については、[ブログ投稿](https://www.braze.com/resources/articles/9-ways-email-marketers-can-respond-to-apples-mail-privacy-protection-feature)をご覧ください。

## Safari IP アドレスの場所

iOS 15 では、ユーザーは IP アドレスから特定された位置情報を匿名化または一般化するように Safari を設定できます。ロケーションベースのターゲティングまたはセグメンテーションを使用する場合は、このことに留意してください。

