---
nav_title: 7月
page_order: 6
noindex: true
page_type: update
description: "この記事には、2019年7月のリリースノートが含まれています。"
---

# 2019年7月

{% alert update %}
Braze には今月、**2回**の製品リリースサイクルがありました。このページでは、最新のリリースが一番上に記載され、それより前のリリースは[その下に記載されています](#earlier-this-month)。
{% endalert %}

## SAML/SSO

[シングルサインオン]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/) (SSO) は、Braze ダッシュボードへのアクセスを制御する安全かつ一元化された方法を企業に提供します。つまり、1 組の認証情報を使用して、Braze を含むさまざまなアプリケーションにアクセスできます。

[OAuth 2.0 サポートを使用した Google サインイン](https://developers.google.com/identity/protocols/OAuth2)に加えて、企業は Security Assertion Markup Language (SAML) サポートを使用した SSO を希望しています。これにより、[Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/azure_ad/) および[Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/) を含む大規模なID プロバイダ(IdP) とシームレスに統合できます。これは、最新の業界標準(SAML 2.0) に対応しています。

Braze は以下をサポートしています。
- [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)
- [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/azure_ad/)
- [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)

## イベント API キー表示を調整する

Adjust のパートナーページを更新し、お客様がこの API キーにアクセスできるようにしました。

## 新パートナーズ

いくつかの新しいパートナーが Alloys プログラムに参加し、ドキュメントに追加されました。新しいパートナーは以下のとおりです。
- [FiveTran]({{site.baseurl}}/partners/fivetran/)
- [Talon.One]({{site.baseurl}}/partners/talonone/)
- [Voucherify]({{site.baseurl}}/partners/voucherify/)

## キャンペーン内容改善

拡張キャンペーンの詳細が、**キャンペーン**ページの。..wait it...**キャンペーン詳細**セクションに表示されます!

## セグメントとキャンバスで自分のもののみを表示する

"Show Only Mine" **Campaigns**ページのチェックフィルターは、非常に人気があることが証明されています。その結果、キャンバスとセグメントリストにもこのオプションを追加しています!

### 昇進動作

ユーザーがあるキャンバスステップから次のキャンバスに進むと、[を選択できるようになりました。これらのオプションには、"Message Sent"および"Entire Audience After Delay"が含まれます。

### キャンバスのアプリ内メッセージ

[In-アプリ messages]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/)がキャンバスで利用可能になりました!キャンバスステップを追加し、使用可能なチャネルs を参照してアプリ内メッセージを追加します。

# 今月上旬

## ユーザプロファイル "画像の削除

Braze ユーザープロファイル s とユーザー 検索で表示されているユーザープロファイル画像を削除しています。

## コンテンツカードの接続コンテンツ

[Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content)文字列と機能を[Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/overview/)で使用できるようになりました。

外部サーバへの接続されたコンテンツコールは、カードが実際に送信されたときにアプリします。カードがユーザによって表示されたときではありません。メールと同様に、ダイナミックなの内容は、実際に表示されるときではなく、送信時に計算され決定されます。

## Null "; 返信先" 住所

顧客は、メールメッセージの" 返信先" address に`null` 値を設定できるようになりました。Braze の** メール Settings** ページから、または[API]({{site.baseurl}}/api/endpoints/messaging/#email-object-specification) を使用して設定します。 使用すると、リストされた"From"アドレスに返信が送信されます。 "From"address フィールドを`dan@emailaddress.com`としてパーソナライズできるようになりました。そして、あなたの顧客sは直接Danに返信することができます。

メール メッセージの"返信先-" address に`null` 値を設定するには、ナビゲーションで**Manage Settings** に移動し、** メール Settings** タブを選択します。**Outbound Email Settings**セクションまでスクロールし、**Exclude "Reply-To"を選択し、返信を"From"**にデフォルトアドレスとして送信します。

## キャンペーン比較

[複数のキャンペーンsを一度に見て、それらの相対パフォーマンス]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/comparing_campaigns/)をBrazeで並べて-1つのウィンドウで比較しましょう!

## Template dispatch ID をLiquid でメッセージに送信する

{% alert note %}
`dispatch_id` の動作は、キャンバスとキャンペーン s 間で異なります。これは、Braze では、キャンバスステップs (エントリ ステップ s (スケジュールされた可能) を除く) が、"スケジュールされた" であっても、トリガーのed イベントとして扱われるためです。[`dispatch_id` ビヘイビア]({{site.baseurl}}/help/help_articles/data/dispatch_id/) の詳細については、キャンバスとキャンペーン s を参照してください。
{% endalert %}

(URL などで) メッセージ内からのメッセージの配信を追跡する場合は、`dispatch_id` をテンプレートできます。この書式は、サポートされているパーソナライゼーション タグの一覧[Canvas Attributes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)にあります。

これは`api_id` と同じように動作します。この場合、`api_id` はキャンペーン作成時には使用できないため、プレースホルダとしてd がテンプレートされ、`dispatch_id_for_unsent_campaign` としてプレビューされます。ID はメッセージが送信される前に生成され、送信時間として含まれます。

{% alert warning %}
アプリ内メッセージ には`dispatch_id` がないため、`dispatch_id_for_unsent_campaign` のリキッドテンプレートはアプリ内メッセージs では機能しません。
{% endalert %}

## "Show Only Mine" 設定は持続します

"Show Only Mine"キャンペーン表枠のフィルターは、**キャンペーン s**ページにアクセスするたびに表示されます。

## A/B試験更新s

1 回限りの[A/B テスト]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/) に最大8 つのバリアント(およびオプションのコントロール)を付けて、ユーザーが指定したキャンペーンのタグe のオーディエンスに送信し、最適なオーディエンスをプレスケジュールされた時に残りのオーディエンスに送信できます。
