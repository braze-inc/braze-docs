---
nav_title: 4月
page_order: 9
noindex: true
page_type: update
description: "この記事には2018年4月のリリースノートが含まれています。"
---
# 2018年4月

## webhook更新中

5月に、BrazeはWebhookリダイレクトのセキュリティイニシアチブを実施します。今後、Webhook送信者はこれらのリダイレクトに従うことができなくなります。代わりに、リダイレクトは無限リダイレクトループを防ぐためにエラーとして扱われます。Braze はこれが誰にも影響を与えるとは考えていませんが、リダイレクトする webhook がある場合は、そのキャンペーンを再確認して編集することをお勧めします。

## CSVストレージが増加しました

BrazeはCSV Xフィルターを更新し、以前の10件ではなく、ユーザーが更新された最新の100件のCSVを含むようにしました。

## Androidアプリのデフォルトでアンインストール追跡がオン

すべての新しいAndroidアプリの[アンインストール追跡][94]機能はデフォルトで「オン」になります。すべての既存のAndroidアプリでアンインストール追跡がオフになっているものは、今後「オン」に変更されます。Android アンインストール追跡は、もはやデバイスにプッシュを送信せず、他の更新やアクションは必要ありません。

## 更新され、改善された検索機能

Brazeは、タグ付けとより優れた検索機能をBrazeに追加し、[カスタムイベントと属性][92]、テンプレートなどを検索する際に、大規模な展開を管理する体験を向上させました。

## プッシュ通知ストーリー

[複数のページ、画像、クリック動作、およびオプションのタイトルとサブタイトルを含む通知を作成します][95]プッシュメッセージを作成し、ドロップダウンから**Push Story**を選択するだけです。

この機能を使用するには、Android（バージョン2.2.0+）およびiOS（バージョン3.2.0+）の最新バージョンに更新する必要があることに注意してください。


## 受信トレイビジョン

お客様のプラットフォームに基づいて、[メールをプレビューする][96]ことができます。サムネイルの概要ページまたは、各クライアントのHTMLレンダリングに関する問題の詳細な分析を含む大きなスクリーンショットのリストビューを通じて行うことができます。詳細については、顧客成功マネージャーまたはアカウントマネージャーにお問い合わせください。


[92]: {{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#custom-event-and-attribute-management
[94]: {{site.baseurl}}/user_guide/data_and_analytics/uninstall_tracking/#uninstall-tracking-for-campaigns
[95]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_stories/#push-stories
[96]: {{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision
