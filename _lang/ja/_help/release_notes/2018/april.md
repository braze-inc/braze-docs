---
nav_title: 4月
page_order: 9
noindex: true
page_type: update
description: "この記事には2018年4月のリリースノートが含まれている。"
---
# 2018年4月

## Webhooksの更新が始まる

5月、BrazeはWebhookリダイレクトのセキュリティ対策を実施する。今後、Webhook送信者はこれらのリダイレクトに従うことができなくなる。その代わり、リダイレクトはエラーとして扱われ、リダイレクトの無限ループを防ぐ。Brazeでは、このことが誰かに影響を与えるとは考えていないが、リダイレクトするWebhookをお持ちの場合は、そのキャンペーンを再検討し、編集することをお勧めする。

## CSVストレージが増加

Brazeは、CSV Xフィルターを更新し、ユーザーが更新したCSVの最新100件を含めるようにした。

## Androidアプリのトラッキング追跡をデフォルトでアンインストールする。

すべての新しいAndroidアプリの[アンインストール追跡][94]機能は、デフォルトで "オン "になる。アンインストール追跡が "オフ "になっている既存のAndroidアプリはすべて "オン "に変更される。Androidのアンインストール追跡はデバイスにプッシュを送信しなくなり、他の更新やアクションは必要ない。

## 検索機能の更新と改善

Brazeは、[カスタムイベントやアトリビューション][92]、テンプレートなどを検索しながら、Brazeの大規模なデプロイメントを管理する経験を向上させるために、Brazeにタグ付けとより優れた検索機能を追加した。

## プッシュ通知ストーリー

複数のページ、画像、写真、クリック動作、オプションのタイトルとサブタイトルで[通知を作成][95]する。プッシュ・メッセージを作成し、ドロップダウンから**「プッシュ・ストーリー**」を選択するだけだ。

なお、この機能を使うには、Android（バージョン2.2.0+）とiOS（バージョン3.2.0+）を最新版に更新する必要がある。


## 受信トレイのビジョン

顧客のプラットフォーム別に[メールをプレビュー][96]できるようになり、サムネイルの概要ページや、大きなスクリーンショットを含むリストビューで、各クライアントのHTMLレンダリングに存在する可能性のある問題をより具体的に分析できるようになった。詳細については、カスタマー・サクセス・マネージャーまたはアカウントマネージャーに問い合わせを。


[92]: {{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#custom-event-and-attribute-management
[94]: {{site.baseurl}}/user_guide/data_and_analytics/uninstall_tracking/#uninstall-tracking-for-campaigns
[95]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_stories/#push-stories
[96]: {{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision
