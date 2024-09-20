---
nav_title: iOS 15 アップグレードガイド
article_title: iOS 15 SDKアップグレードガイド
page_order: 7
platform: iOS
description: "このリファレンス記事では、新しいiOS 15 OS 更新、必要なSDK 更新、および新機能について説明します。"
hidden: true
noindex: true
---

# iOS 15 SDK アップグレード

> 本書では、iOS 15 (WWDC21) で導入された変更点と、Braze iOS SDKインテグレーションに必要なアップグレード ステップについて説明します。新しいiOS 15 更新の一覧については、Apple の[iOS 15 リリースノート](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-15-release-notes) を参照してください。


## UI ナビゲーションへの透明性の変更

iOSベータの年次テストの一環として、不透明ではなく、特定のUIナビゲーションバーが耳の透明をアプリするアプリ leによる変更を特定しました。これは、Braze のデフォルト UI for Content Card を使用する場合、またはWeb ディープリンクが別のブラウザーアプリではなくアプリ内で開封される場合に、iOS 15 で表示されます。

iOS 15 でこのような視覚的な変化を避けるために、できるだけ早く[ Braze iOS SDK v4.3.2][1] にアップグレードすることを強くお勧めします。そうしないと、ユーザー は電話機を新しいiOS 15 オペレーティングシステムにアップグレードし始めます。

## 新通知 設定s {#notification-settings}

iOS 15は新しい通知機能を導入し、ユーザーの集中を維持し、昼間の頻繁な中断を避けました。私たちは、これらの新機能のサポートを提供できることを楽しみにしています。これらの機能は、追加のSDK アップグレードを必要とせず、iOS 15 機器のユーザーにのみアプリな役割を果たします。

### フォーカスモード {#focus-mode}

iOS 15 ユーザー s は"Focus Modes"-カスタムプロファイル s を使用して、どの通知に焦点を当てて目立つように表示したいかを判断できるようになりました。

![]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

### 割り込みレベル {#interruption-levels}

iOS 15 では、プッシュ通知 s は4 つの中断レベルのいずれかで送信できます。

* **パッシブ** (新規) - 音なし、振動なし、スクリーンウェイク、フォーカス設定のブレークスルーなしs。
* **アクティブ** (デフォルト) - サウンド、バイブレーション、スクリーンウェイク、フォーカス設定s のブレークスルーを禁止します。
* **Time-Sensitive** (新規) - サウンド、バイブレーション、スクリーンウェイキングが許可されている場合、システムコントロールを突破できます。
* **Critical** \- サウンド、バイブレーション、スクリーンウェイク、システムコントロールのブレークスルー、およびリンガー切り替えるのバイパスを可能にします。

iOS プッシュでこのオプションを設定する方法の詳細については、[iOS 通知オプション]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#interruption-level)を参照してください。

### 通知サマリー {#notification-summary}

![]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15 では、ユーザー s は通知s のサマリーを受信するために、1 日を通して特定の時間を選択できます(オプション)。即時の注意を必要としない通知("Passive&quot、またはユーザーがフォーカスモードの間に送信されるような)は、1日中の継続的な中断を防ぐためにグループ化されます。

送信する通知ごとに、"relevance score"を、サマリーの上部にあるどの通知をアプリするかをコントロールするために、すぐに指定できるようになります。

通知の"関連性スコア"の設定方法については、[iOS 通知 Options]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#relevance-score)を参照してください。

## 位置ボタン {#location-buttons}

iOS 15では、ユーザー sがアプリ内の位置情報を一時的に許可する新しい便利な方法が導入されています。 

新しいロケーションボタンは、既存の"Allow Once"権限を、同じセッションで何度もクリックしたユーザーに繰り返しプロンプトすることなく構築します。

詳しくは、今年の世界開発者会議(WWDC)でアップルの[ロケーションボタン](https://developer.apple.com/videos/play/wwdc2021/10102/)動画をご覧ください。

{% alert tip %}
この機能により、ユーザーに権限を要求することができます。iOS 15 より前にロケーション権限を拒否したことがあるユーザーは、ロケーションボタンをクリックすると、前回拒否した状態から権限をリセットする機会としてプロンプトが表示されます。
{% endalert %}

### Brazeで位置情報を利用する

Brazeで位置ボタンを使用する場合は、追加の統合は必要ありません。アプリは、通常どおり(権限が付与されたら)ユーザーの場所を渡し続ける必要があります。

Appleによると、すでにバックグラウンドの場所へのアクセス権を共有しているユーザーの場合、"App"オプションを使用すると、iOS 15にアップグレードした後も、引き続きその権限が付与されます。

## アップルメール {#mail}

今年、アップルは多くの更新をメール "トラッキングとプライバシーに向けて発表した。詳細については、[ブログ投稿](https://www.braze.com/resources/articles/9-ways-email-marketers-can-respond-to-apples-mail-privacy-protection-feature)をご覧ください。

## Safari IP アドレスの場所

iOS 15 では、ユーザー s はIP アドレスから決定された場所を匿名化または一般化するようにSafari を設定できます。ロケーションベースのターゲティングまたはセグメンテーションを使用する場合は、このことに留意してください。

[1]: https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.3.2
[2]: https://github.com/Appboy/appboy-ios-sdk/issues
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#interruption-level
