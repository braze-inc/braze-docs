---
nav_title: 4月
page_order: 9
noindex: true
page_type: update
description: "この記事には、2018 年 4 月のリリース ノートが含まれています。"
---
# 2018年4月

## Webhook のアップデートが進行中

5 月に、Braze は Webhook リダイレクトのセキュリティ イニシアチブを実装する予定です。今後、Webhook 送信者はこれらのリダイレクトに従うことができなくなります。代わりに、無限リダイレクト ループを防ぐために、リダイレクトはエラーとして扱われます。Braze はこれが誰かに影響を与えるとは考えていませんが、リダイレクトする Webhook がある場合は、そのキャンペーンを再確認して編集することをお勧めします。

## CSVストレージの増加

Braze は CSV X フィルターを更新し、以前の 10 件ではなく、ユーザーが更新された最新の 100 件の CSV を含めるようになりました。

## Android アプリのアンインストール追跡をデフォルトでオンにする

すべての新しい Android アプリの [アンインストール追跡][94] 機能は、デフォルトで「オン」になります。 アンインストール追跡がオフになっている既存の Android アプリはすべて「オン」に変更されます。 Android のアンインストール追跡ではデバイスにプッシュが送信されなくなり、ユーザー側で他の更新やアクションを実行する必要もありません。

## 検索機能の更新と改善

Braze では [、カスタム イベントや属性][92]、テンプレートなどを検索しながら、Braze の大規模な展開を管理するエクスペリエンスを向上させるために、タグ付けと検索機能が向上しました。

## プッシュストーリー

複数のページ、画像、クリック動作、オプションのタイトルとサブタイトルを含む[通知を作成します][95] 。プッシュ メッセージを作成し、ドロップダウンから **[プッシュ ストーリー]** を選択するだけです。

この機能を使用するには、Android (バージョン 2.2.0 以上) および iOS (バージョン 3.2.0 以上) を最新バージョンにアップデートする必要があることに注意してください。


## 受信トレイのビジョン

サムネイルの概要ページ、または大きなスクリーンショットと各クライアントの HTML レンダリングに存在する可能性のある問題のより具体的な分析を含むリスト ビューのいずれかを使用して、顧客のプラットフォームに基づいて [メールをプレビュー][96] できるようになりました。詳細については、カスタマー サクセス マネージャーまたはアカウント マネージャーにお問い合わせください。


[92]: {{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#custom-event-and-attribute-management
[94]: {{site.baseurl}}/user_guide/data_and_analytics/uninstall_tracking/#uninstall-tracking-for-campaigns
[95]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_stories/#push-stories
[96]: {{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision
