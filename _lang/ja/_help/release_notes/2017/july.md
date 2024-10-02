---
nav_title: 7月
page_order: 6
noindex: true
page_type: update
description: "この記事には2017年7月のリリースノートが含まれています。"
---

# 2017年7月

## Web プッシュにおける大きな画像

Chrome の Windows および Android で Web プッシュの大きな画像のサポートを追加し、リッチで魅力的な顧客体験を作成できるようにしました。[Web プッシュ][58] について詳しく学びましょう。

## メールフィールドの更新

これで、特定の送信元アドレスにメールをロックすることができ、誤ったアドレスを入力することがないようにすることができます。メール作成フォームには、過去6か月間に使用されたアドレスが事前に入力され、プロセスが合理化されます。[メールのベストプラクティス][57]をチェックして、詳細をご確認ください。

## キャンペーン詳細APIの更新

`/campaign/details`エンドポイントは現在、そのメッセージに関する情報を提供しており、APIを使用して件名、HTML本文、送信元アドレス、および返信先フィールドを取得できます。Braze API について[詳しく知る][56]。

## Liquidテンプレートの更新

キャンバスとキャンペーンでテンプレートバリアント属性を追加しました。キャンバスでは、バリアントのAPI IDとバリアントの名前の両方をテンプレート化できるようになりました。また、キャンペーンではメッセージの`message_api_id`と`message_name`をテンプレート化できるようになりました。両方のアップデートにより、メッセージングの柔軟性が向上し、パーソナライズされたキャンペーンを構築できるようになります。[パーソナライズされたメッセージング][55] について詳しく学びましょう。

## 新しいHTMLメールエディター

今では、ライブプレビュー、Liquidによるパーソナライゼーション、および行番号と構文の強調表示を備えた改良された全画面テキストエディタを可能にする全画面HTMLエディタを使用して、簡単にメールを書いてテストできます。[メールの作成][54]について詳しく学びましょう。

## プレビューの更新

キャンペーンやキャンバスでメッセージプレビューをスクロールすると、画面ウィンドウに従って変更が反映されるのを常に確認できます。プレビューとテストについて[詳しく知る][53]。

## 新しいSegmentメンバーシップフィルター

[セグメントメンバーシップフィルター][52]を追加し、既存のセグメントのいずれかに基づいてユーザーをターゲットにすることができるようにしました。さらに、「And」と「Or」ロジックの両方をセグメントフィルターで使用する機能、およびセグメントを相互にネストする機能を追加しました。これらの更新により、顧客により正確にカスタマイズされたメッセージを送信できるようになります。 

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
