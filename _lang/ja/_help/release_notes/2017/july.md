---
nav_title: 7月
page_order: 6
noindex: true
page_type: update
description: "この記事には2017年7月のリリースノートが含まれています。"
---

# 2017年7月

## Web プッシュにおける大きな画像

Windows および Android の Chrome 用 Web プッシュで大容量画像のサポートを追加して、豊かで魅力的なカスタマーエクスペリエンスを構築できるようにしました。[Web プッシュ][58] について詳しく学びましょう。

## メール フィールドのアップデート

間違ったアドレスを入力しないように、特定の差出人アドレスのセットにメールをロックできるようになりました。メール作成フォームには、過去6か月間に使用されたアドレスが事前に入力され、プロセスが合理化されます。[メールのベストプラクティス][57]をチェックして、詳細をご確認ください。

## キャンペーン詳細APIの更新

`/campaign/details` エンドポイントが、そのメッセージに関する情報を提供し、API を使用して件名、HTML 本文、差出人アドレス、返信先のフィールドを取得できるようになりました。[ Braze API][56] について詳しく説明します。

## リキッドテンプレーティングの更新

キャンバスとキャンペーンで、バリアント属性をテンプレート化する機能を追加しました。キャンバスではバリアントの API ID と名前を、キャンペーンではメッセージの `message_api_id` と`message_name` をテンプレート化できるようになりました。両方の更新により、メッセージングの柔軟性が向上し、パーソナライズされたキャンペーンを構築できるようになります。[パーソナライズされたメッセージング][55] について詳しく学びましょう。

## 新しいHTMLメールエディター

今では、ライブプレビュー、Liquidによるパーソナライゼーション、および行番号と構文の強調表示を備えた改良された全画面テキストエディタを可能にする全画面HTMLエディタを使用して、簡単にメールを書いてテストできます。[メールの作成][54]について詳しく学びましょう。

## プレビューの更新

キャンペーンとキャンバスでメッセージプレビューを下にスクロールすると、画面ウィンドウをたどることができ、反映された変更をいつでも確認できます。詳細については、「[プレビューとテスト][53]」を参照してください。

## 新しいセグメントメンバーシップフィルター

[セグメントメンバーシップフィルター][52]を追加しました。これにより、既存セグメントのいずれかのメンバーシップに基づいてユーザーをターゲット設定できます。さらに、「And」と「Or」ロジックの両方をセグメントフィルターで使用する機能、およびセグメントを相互にネストする機能を追加しました。これらの更新により、カスタマイズされたメッセージをより正確に顧客に送信できるようになります。 

## Androidプレビューに更新

Android N以降のAndroidの最新バージョンを反映するために、[Androidプレビュー][51]を更新しました。


[51]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#step-5-preview-message
[52]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#targeting-filters
[53]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#step-6-preview-message
[54]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template
[55]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[56]: {{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api
[57]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[58]: {{site.baseurl}}/user_guide/message_building_by_channel/push/web
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
