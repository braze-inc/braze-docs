---
nav_title: 7月
page_order: 6
noindex: true
page_type: update
description: "この記事には2019年7月のリリースノートが含まれています。"
---

# 2019年7月

{% alert update %}
Brazeは今月、**2**回の製品リリースサイクルを持っていました！最新リリースは上部に記載されており、以前のリリースはこのページのさらに下に[開始します](#earlier-this-month)！
{% endalert %}

## SAML/SSO

[シングルサインオン]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/)（SSO）は、企業にBrazeダッシュボードへのアクセスを制御するための安全で集中化された方法を提供します。要するに、1つの資格情報セットを使用して、Brazeを含むさまざまなアプリケーションにアクセスできます。

さらに、[OAuth 2.0 を使用した Google サインインのサポート<1>に加えて、企業は Security Assertion Markup Language (SAML) サポートを備えた SSO を希望しています。これにより、[Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/azure_ad/)や[Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)などの大手アイデンティティプロバイダー（IdP）とシームレスに統合でき、最新の業界標準（SAML 2.0）をサポートします。

Brazeはサポートしています:
- [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)
- [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/azure_ad/)
- [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)

## Adjust イベント API キーを表示

Adjust のパートナーページを更新して、この API キーを顧客が利用できるようにしました。

## 新しいパートナー

新しいパートナーが私たちのAlloysプログラムに参加し、Docsに追加されました！こんにちはと言ってください：
- [Fivetran]({{site.baseurl}}/partners/fivetran/)
- [Talon.One]({{site.baseurl}}/partners/talonone/)
- [Voucherify]({{site.baseurl}}/partners/voucherify/)

## キャンペーン詳細の改善

拡張されたキャンペーンの詳細は、...待ってください...**キャンペーンの詳細**セクションに表示されます**キャンペーン**ページ！

## セグメントで自分のものだけを表示 & キャンバス

「自分のものだけ表示」チェックフィルターは**キャンペーン**ページで非常に人気があります。その結果、このオプションをキャンバスおよびSegmentリストにも追加します！

### 昇進動作

ユーザーが1つのキャンバスステップから次のステップに進むタイミングを選択できるようになりました。これらのオプションには「メッセージ送信済み」と「遅延後の全オーディエンス」が含まれます。

### キャンバスのアプリ内メッセージ

[アプリ内メッセージ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/)は現在キャンバスで利用可能です！キャンバスステップを追加し、利用可能なチャネルを参照してアプリ内メッセージを追加します。

# 今月初め

## ユーザープロファイル画像削除

Brazeユーザープロファイルおよびユーザー検索に表示されるユーザープロファイル画像を削除しています。

## コンテンツカードのコネクテッドコンテンツ

[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content)の文字列と機能を[コンテンツカード]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/overview/)で使用できるようになりました。

コネクテッドコンテンツ calls to external servers will happen when a カード is actually sent, not when the カード is viewed by the ユーザー.メールと同様に、ダイナミックなコンテンツは実際にカードが表示されるときではなく、送信時に計算および決定されます。

## Null "返信先" address

顧客は現在、Brazeの**メール設定**ページまたは[API]({{site.baseurl}}/api/endpoints/messaging/#email-object-specification)を使用して、メールメッセージの「返信先」アドレスに`null`値を設定できます。 使用すると、返信は記載された「差出人」アドレスに送信されます。 「From」アドレスフィールドを`dan@emailaddress.com`としてパーソナライズできるようになり、顧客はDanに直接返信することができます。

メールメッセージの「返信先」アドレスに`null`値を設定するには、ナビゲーションの**設定の管理**に移動し、**メール設定**タブに移動します。**送信メール設定**セクションまでスクロールし、デフォルトのアドレスとして**「返信先」を除外し、「From」に返信を送信**を選択します。

## キャンペーンの比較

Braze で複数のキャンペーンを一度に見て、それらの相対的なパフォーマンスを比較し、一つのウィンドウで並べて表示します！

## テンプレート dispatch ID into messages with Liquid

{% alert note %}
Canvasとキャンペーンの間での`dispatch_id`の動作は異なります。なぜなら、BrazeはCanvasのステップ（エントリステップはスケジュール可能ですが）を「スケジュールされた」場合でもトリガーイベントとして扱うためです。キャンバスとキャンペーンでの[`dispatch_id`行動]({{site.baseurl}}/help/help_articles/data/dispatch_id/)について詳しく学びましょう。
{% endalert %}

メッセージ内からメッセージの送信を追跡したい場合（たとえば、URL内など）、`dispatch_id`にテンプレートを使用できます。このフォーマットは、サポートされているパーソナライゼーションタグのリストの[キャンバス属性]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)の下にあります。

これはちょうど`api_id`のように動作します。キャンペーン作成時に`api_id`が利用できないため、プレースホルダーとしてテンプレート化され、`dispatch_id_for_unsent_campaign`としてプレビューされます。IDはメッセージが送信される前に生成され、送信時に含まれます。

{% alert warning %}
Liquidテンプレートの`dispatch_id_for_unsent_campaign`はアプリ内メッセージでは機能しません。なぜなら、アプリ内メッセージには`dispatch_id`がないからです。
{% endalert %}

## 「自分のもののみを表示」設定が持続する

「自分のもののみ表示」フィルターは、キャンペーングリッド上で**キャンペーン**ページにアクセスするたびにオンのままになります。

## AB テスト更新

ユーザー指定の割合のキャンペーンのオーディエンスに、最大8つのバリアント（およびオプションのコントロール）を含む一度限りの[A/Bテスト]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/)を送信し、事前にスケジュールされた時間に残りのオーディエンスに最適なバリアントを送信できます。
