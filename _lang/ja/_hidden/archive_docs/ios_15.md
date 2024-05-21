---
nav_title: iOS 15 アップグレードガイド
article_title: iOS 15 SDK アップグレードガイド
page_order: 7
hidden: true
platform: iOS
description: "このリファレンス記事では、新しいiOS 15 OS のアップデート、必要なSDK のアップデート、および新機能について説明します。"

---

# iOS 15 SDK アップグレードガイド

このガイドでは、iOS 15 (WWDC21) で導入された変更点と、Braze iOS SDK 統合に必要なアップグレード手順について説明します。

> 新しいiOS 15 アップデートの完全なリストについては、Apple の[iOS 15 リリースノート](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-15-release-notes) を参照してください。


## UI ナビゲーションへの透明性の変更

iOSベータの年次テストの一環として、特定のUIナビゲーションバーが不透明ではなく透明に見えるようにするAppleによる変更を特定しました。これは、Braze のデフォルトUI for Content Card を使用している場合、または別のブラウザアプリではなくアプリ内でWeb ディープリンクが開かれている場合に、iOS 15 で表示されます。

iOS 15 でこのような視覚的な変更を避けるには、ユーザーが新しいiOS 15 オペレーティングシステムへの電話機のアップグレードを開始する前に、できるだけ早く[Braze iOS SDK v4.3.2][1] にアップグレードすることを強くお勧めします。

## 新しい通知設定 {#notification-settings}

iOS 15では、ユーザーが集中力を保ち、1日中の頻繁な中断を避けるための新しい通知機能が導入されました。私たちは、これらの新機能のサポートを提供できることを楽しみにしています。これらの機能は、追加のSDK アップグレードを必要とせず、iOS 15 デバイス上のユーザーにのみ適用されます。

### フォーカスモード {#focus-mode}

iOS 15 ユーザーは"Focus Modes"-フォーカスを突き破って目立つように表示したい通知を決定するために使用されるカスタムプロファイルを作成できるようになりました。

{% image_buster /assets/img/ios/ios15-notification-settings.png %}

### 割り込みレベル {#interruption-levels}

iOS 15 では、以下の4 つの中断レベルのいずれかでプッシュ通知を送信できます。

* **パッシブ** (新規) - 音なし、振動なし、スクリーンウェイク、フォーカス設定のブレークスルーなし。
* **アクティブ** (既定値) - サウンド、バイブレーション、画面のウェイクアップ、フォーカス設定のブレークスルーを禁止します。
* **Time-Sensitive** (新規) - サウンド、振動、スクリーンウェイキングが可能な場合、システムコントロールを突破できます。
* **Critical** \- サウンド、振動、スクリーンウェイク、システムコントロールのブレイクスルー、およびリンガースイッチのバイパスが可能です。

iOS プッシュでこのオプションを設定する方法の詳細については、[iOS 通知オプション]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#interruption-level)を参照してください。

### 通知サマリー {#notification-summary}

![\]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15 では、ユーザーは1 日を通して特定の時間を選択して、通知の要約を受信できます(オプション)。即時の注意を必要としない通知("Passive&quot、またはユーザーがフォーカスモードの間に送信されるなど)は、1日中の継続的な中断を防ぐためにグループ化されます。

送信する通知ごとに、すぐに"relevance score&quotを指定できるようになります。これにより、サマリーの上部に表示される通知を制御できます。

通知の"relevance score"を設定する方法の詳細については、[iOS通知オプション]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#relevance-score)を参照してください。

## 位置ボタン {#location-buttons}

iOS 15は、ユーザーがアプリ内で一時的に位置アクセスを許可するための新しい便利な方法を紹介しています。 

新しいロケーションボタンは、既存の"Allow Once"許可を、同じセッションで複数回クリックするユーザーに繰り返しプロンプトを表示することなく作成します。

詳しくは、Appleの[今年のWWDC(Worldwide Developer Conference)のロケーションボタン](https://developer.apple.com/videos/play/wwdc2021/10102/)ビデオをご覧ください。

{% alert tip %}
この機能により、ユーザーに許可を求めることができます。iOS 15 より前にロケーション権限を拒否したことがあるユーザーは、ロケーションボタンをクリックすると、前回拒否した状態から権限をリセットする機会としてプロンプトが表示されます。
{% endalert %}

### ロケーションボタンをろう付けで使用する

ロケーションボタンをろう付けで使用する場合は、追加の統合は必要ありません。アプリは、通常どおり(権限が付与されたら)ユーザーの場所を渡し続ける必要があります。

Appleによると、既にバックグラウンドロケーションアクセスを共有しているユーザーの場合、"App"オプションを使用している間は、iOS 15にアップグレードした後も、そのレベルの権限が引き続き付与されます。

## アップルメール {#mail}

今年、アップルは電子メールの追跡とプライバシーに関する多くの更新を発表した。詳細については、[ブログ投稿](https://www.braze.com/resources/articles/9-ways-email-marketers-can-respond-to-apples-mail-privacy-protection-feature)をご覧ください。

## Safari IP アドレスの場所

iOS 15 では、IP アドレスから決定された場所を匿名化または一般化するようにSafari を設定できます。ロケーションベースのターゲティングまたはセグメンテーションを使用する場合は、この点に注意してください。

[1]: https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.3.2
[2]: https://github.com/Appboy/appboy-ios-sdk/issues
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#interruption-level
