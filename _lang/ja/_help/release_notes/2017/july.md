---
nav_title: 7月
page_order: 6
noindex: true
page_type: update
description: "この記事には、2017 年 7 月のリリースノートが含まれています。"
---

# 2017 年 7 月

## Web プッシュの大きな画像

Windows 版と Android 版 Chrome のウェブプッシュで大きな画像のサポートが追加され、魅力的で魅力的なカスタマーエクスペリエンスを実現できるようになりました。[Web プッシュの詳細をご覧ください][58]。

## メールフィールドの更新

メールを特定の差出人アドレスにロックして、誤って間違ったアドレスを入力しないようにすることができます。メール作成フォームには、プロセスを効率化するために、過去 6 か月間に使用されたアドレスがあらかじめ入力されます。詳細については、「[Eメールのベストプラクティス][57]」を参照してください。

## キャンペーン詳細 API の更新

`/campaign/details`エンドポイントがメッセージに関する情報を提供するようになり、API を使用して件名、HTML 本文、送信者アドレス、返信先のフィールドを取得できるようになりました。[Braze API][56] の詳細については、こちらをご覧ください。

## Liquid テンプレートのアップデート

キャンバスとキャンペーンのバリアント属性をテンプレート化する機能が追加されました。Canvasでは、バリアントのAPI IDとバリアントの名前の両方をテンプレート化できるようになりました。キャンペーンでは、メッセージの `message_api_id`「and」をテンプレート化できるようになりました`message_name`。どちらのアップデートでも、メッセージの柔軟性が高まり、パーソナライズされたキャンペーンを構築できます。[パーソナライズドメッセージングの詳細をご覧ください][55]。

## 新しい HTML メールエディター

ライブプレビュー、Liquidによるパーソナライゼーションを可能にするフルスクリーンHTMLエディター、および行番号と構文強調機能を備えた改良されたフルスクリーンテキストエディターを使用して、電子メールを簡単に作成およびテストできるようになりました。[メール作成の詳細をご覧ください][54]。

## プレビューの更新

キャンペーンやキャンバスのメッセージプレビューを下にスクロールしながら画面ウィンドウをたどることができるようになり、変更が反映されたことをいつでも確認できるようになりました。[プレビューとテストの詳細をご覧ください][53]。

## 新しいセグメントメンバーシップフィルター

[セグメントメンバーシップフィルターが追加され][52]、既存のセグメントのいずれかのメンバーシップに基づいてユーザーをターゲットにできるようになりました。さらに、セグメントフィルターで「AND」と「OR」の両方のロジックを使用できる機能と、セグメントを相互にネストする機能を追加しました。これらの更新により、カスタマイズされたメッセージをより正確にお客様に送信できるようになります。 

## Android プレビューへのアップデート

Android N 以降の [Android の最新バージョンを反映するように Android プレビューを更新しました][51]。


[51]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#step-5-preview-message
[52]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#targeting-filters
[53]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#step-6-preview-message
[54]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template
[55]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[56]: {{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api
[57]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[58]: {{site.baseurl}}/user_guide/message_building_by_channel/push/web
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
