---
nav_title: 7月
page_order: 6
noindex: true
page_type: update
description: "この記事には、2019年7月のリリースノートが含まれています。"
---

# 2019年7月

{% alert update %}
Braze には、今月だけで**2回**の製品リリースサイクルがありました。このページでは、最新のリリースが一番上に記載され、その前のリリースは[その下に記載されています](#earlier-this-month)。
{% endalert %}

## SAML/SSO

[シングルサインオン]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/) (SSO) は、Braze ダッシュボードへのアクセスを制御する安全かつ一元化された方法を企業に提供します。つまり、1 組の認証情報を使用して、Braze を含むさまざまなアプリケーションにアクセスできます。

[OAuth 2.0 サポートを使用した Google サインイン](https://developers.google.com/identity/protocols/OAuth2)に加えて、企業は Security Assertion Markup Language (SAML) サポートを使用した SSO を希望しています。これにより、[Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/) および[Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/) を含む大規模なID プロバイダ(IdP) とシームレスに統合できます。これは、最新の業界標準(SAML 2.0) に対応しています。

Braze は以下をサポートしています。
- [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)
- [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/)
- [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)

## Adjust イベント API キーの表示

Adjust のパートナーページを更新し、お客様がこの API キーにアクセスできるようにしました。

## 新パートナーズ

いくつかの新しいパートナーが Alloys プログラムに参加し、ドキュメントに追加されました。新しいパートナーは以下のとおりです。
- [FiveTran]({{site.baseurl}}/partners/fivetran/)
- [Talon.One]({{site.baseurl}}/partners/talonone/)
- [Voucherify]({{site.baseurl}}/partners/voucherify/)

## キャンペーン内容改善

拡張キャンペーンの詳細が、**キャンペーン**ページの。..wait it...**キャンペーン詳細**セクションに表示されます!

## セグメントとキャンバスで自分のものだけを表示する

[**キャンペーン**] ページの [自分のものだけを表示] チェックフィルターは、非常に人気があることが証明されています。そのため、キャンバスおよびセグメントリストにもこのオプションを追加します。

### 昇進動作

ユーザーが1つのキャンバスステップから次のステップに[進むタイミング]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)を選択できるようになりました。これらのオプションには、[送信済みメッセージ] と [延期期間後にオーディエンス全体] が含まれます。

### キャンバスのアプリ内メッセージ

[アプリ内メッセージ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/)をキャンバスで利用できるようになりました。キャンバスステップを追加し、使用可能なチャネルを参照してアプリ内メッセージを追加します。

# 今月上旬

## ユーザープロファイルの写真の削除

Braze ユーザープロファイルおよびユーザー検索で表示されるユーザープロファイルの写真を削除します。

## コンテンツカードの Connected Content

[Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content)文字列と機能を[Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)で使用できるようになりました。

外部サーバーへの Connected Content 呼び出しは、カードがユーザーによって表示されたときではなく、カードが実際に送信されたときに実行されます。メールと同様に、ダイナミックコンテンツは、カードが実際に表示されたときではなく、送信時に計算および決定されます。

## Null 「返信先」アドレス

Braze の[**メール設定**] ページから、または [API]({{site.baseurl}}/api/endpoints/messaging/#email-object-specification) を使用して、メールメッセージの「返信先」アドレスに対して `null` 値を設定できるようになりました。 この設定を使用すると、リストの「差出人」アドレスに返信が送信されます。 "From"address フィールドを`dan@emailaddress.com`としてパーソナライズできるようになりました。そして、あなたの顧客sは直接Danに返信することができます。

Braze からメールメッセージの「返信先」アドレスに対して `null` 値を設定するには、ナビゲーションの [**設定の管理**] に移動し、[**メール設定**] タブに移動します。**Outbound Email Settings**セクションまでスクロールし、**Exclude "Reply-To"を選択し、返信を"From"**にデフォルトアドレスとして送信します。

## キャンペーン比較

[複数のキャンペーンsを一度に見て、それらの相対パフォーマンス]({{site.baseurl}}/report_builder/)をBrazeで並べて-1つのウィンドウで比較しましょう!

## Liquid でディスパッチ ID をメッセージにテンプレート化する

{% alert note %}
`dispatch_id` の動作は、キャンバスとキャンペーンで異なります。これは、Braze がキャンバスのステップ (スケジュール可能なエントリステップを除く) を、スケジュール済みの場合でもトリガーされたイベントとして扱うためです。キャンバスとキャンペーンでの [`dispatch_id` の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)の詳細を確認してください。
{% endalert %}

(URL などで) メッセージ内からのメッセージのディスパッチを追跡する場合は、`dispatch_id` でテンプレート化できます。この書式は、サポートされているパーソナライゼーション タグの一覧[Canvas Attributes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)にあります。

これは、`api_id` と同じように動作します。つまり、`api_id` はキャンペーンの作成時に使用できないため、プレースホルダとしてテンプレート化され、`dispatch_id_for_unsent_campaign` としてプレビューされます。ID はメッセージが送信される前に生成され、送信時間として含まれます。

{% alert warning %}
アプリ内メッセージには `dispatch_id_for_unsent_campaign` がないため、`dispatch_id` の Liquid テンプレート化はアプリ内メッセージでは機能しません。
{% endalert %}

## [自分のものだけを表示] 設定の保持

キャンペーングリッドの [自分のものだけを表示] フィルターは、[**キャンペーン**] ページにアクセスするたびに保持されています。

## A/B試験更新s

1回限りの [A/B テスト]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)を、最大8つのバリアント (およびオプションのコントロール) とともにユーザーが指定した割合のキャンペーンのオーディエンスに送信してから、スケジュールされた時間に残りのオーディエンスに最適なバリアントを送信できます。
