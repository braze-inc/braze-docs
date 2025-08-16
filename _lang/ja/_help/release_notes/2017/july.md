---
nav_title: 7月
page_order: 6
noindex: true
page_type: update
description: "この記事には2017年7月のリリースノートが含まれています。"
---

# 2017年7月

## Web プッシュにおける大きな画像

Windows および Android の Chrome 用 Web プッシュで大容量画像のサポートを追加して、豊かで魅力的なカスタマーエクスペリエンスを構築できるようにしました。[Web プッシュ]({{site.baseurl}}/user_guide/message_building_by_channel/push/web) について詳しく学びましょう。

## メール フィールドのアップデート

間違ったアドレスを入力しないように、特定の差出人アドレスのセットにメールをロックできるようになりました。メール作成フォームには、過去6か月間に使用されたアドレスが事前に入力され、プロセスが合理化されます。[メールのベストプラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices)をチェックして、詳細をご確認ください。

## キャンペーン詳細APIの更新

`/campaign/details` エンドポイントが、そのメッセージに関する情報を提供し、API を使用して件名、HTML 本文、差出人アドレス、返信先のフィールドを取得できるようになりました。[ Braze API]({{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api) について詳しく説明します。

## リキッドテンプレーティングの更新

キャンバスとキャンペーンで、バリアント属性をテンプレート化する機能を追加しました。キャンバスではバリアントの API ID と名前を、キャンペーンではメッセージの `message_api_id` と`message_name` をテンプレート化できるようになりました。両方の更新により、メッセージングの柔軟性が向上し、パーソナライズされたキャンペーンを構築できるようになります。[パーソナライズされたメッセージング]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) について詳しく学びましょう。

## 新しいHTMLメールエディター

今では、ライブプレビュー、Liquidによるパーソナライゼーション、および行番号と構文の強調表示を備えた改良された全画面テキストエディタを可能にする全画面HTMLエディタを使用して、簡単にメールを書いてテストできます。[メールの作成]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template)について詳しく学びましょう。

## プレビューの更新

キャンペーンとキャンバスでメッセージプレビューを下にスクロールすると、画面ウィンドウをたどることができ、反映された変更をいつでも確認できます。詳細については、「[プレビューとテスト]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#step-6-preview-message)」を参照してください。

## 新しいセグメントメンバーシップフィルター

[セグメントメンバーシップフィルター]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#targeting-filters)を追加しました。これにより、既存セグメントのいずれかのメンバーシップに基づいてユーザーをターゲット設定できます。さらに、「And」と「Or」ロジックの両方をセグメントフィルターで使用する機能、およびセグメントを相互にネストする機能を追加しました。これらの更新により、カスタマイズされたメッセージをより正確に顧客に送信できるようになります。 

## Androidプレビューに更新

Android N以降のAndroidの最新バージョンを反映するために、[Androidプレビュー]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#step-5-preview-message)を更新しました。


