---
nav_title: 7月
page_order: 6
noindex: true
page_type: update
description: "この記事には2017年7月のリリースノートが含まれている。"
---

# 2017年7月

## Webプッシュに大きな画像, 写真

Windows版ChromeとAndroid版ChromeのWebプッシュで、リッチでエンゲージメントの高いカスタマーエクスペリエンスを実現できるよう、大きな画像のサポートを追加した。[Webプッシュについて][58]もっと学習しよう。

## メールフィールドの更新

特定の差出人アドレスにメールをロックできるようになったので、誤ってアドレスを入力することがなくなった。メール作成フォームには、プロセスを合理化するため、過去6ヶ月間に使用されたアドレスがあらかじめ入力される。詳しくは[Eメールのベストプラクティスを][57]チェックしよう。

## キャンペーン詳細APIの更新

`/campaign/details` エンドポイントがメッセージに関する情報を提供するようになり、APIを使って件名、HTML本文、差出人アドレス、返信先フィールドを引き出せるようになった。[Braze APIについて][56]もっと学習する。

## Liquidテンプレートの更新

キャンバスとキャンペーンにバリアント属性のテンプレート機能を追加した。キャンバスでは、バリアントの API ID とバリアント名の両方をテンプレートできるようになった。キャンペーンでは、メッセージの`message_api_id` と`message_name` をテンプレートできるようになった。どちらの更新も、メッセージングの柔軟性を高め、パーソナライズされたキャンペーンを構築できるようにした。[パーソナライズされたメッセージングについて][55]学習する。

## 新しいHTMLメールエディター

ライブプレビューが可能なフルスクリーンHTMLエディター、パーソナライゼーションされたLiquid、行番号とシンタックスハイライトを備えた改良されたフルスクリーンテキストエディターで、簡単にメールを書いたりテストしたりできるようになった。[メール作成について][54]詳しく学習する。

## プレビューの更新

キャンペーンやキャンバスのメッセージプレビューをスクロールしながら、スクリーンウィンドウを追うことができるようになり、常に反映された変更を確認できるようになった。[プレビューとテストについて][53]詳しく学習する。

## 新しいセグメンテーションフィルター

[セグメントメンバーシップフィルターを][52]追加し、既存のセグメントのメンバーシップに基づいてユーザーをターゲティングできるようになった。さらに、セグメンテーション・フィルターで「And」と「Or」の両方のロジックが使えるようになり、セグメント同士を入れ子にする機能も追加された。これらの更新により、顧客にカスタマイズされたメッセージをより正確に送ることができる。 

## Androidプレビューへの更新

我々は、[Android][51]N以降のより新しいバージョンの[Androidを][51]反映させるため、[Androidプレビューを][51]更新した。


[51]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#step-5-preview-message
[52]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#targeting-filters
[53]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#step-6-preview-message
[54]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template
[55]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[56]: {{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api
[57]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[58]: {{site.baseurl}}/user_guide/message_building_by_channel/push/web
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
