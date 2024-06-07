---
nav_title: 7月
page_order: 6
noindex: true
page_type: update
description: "この記事には、2019 年 7 月のリリース ノートが含まれています。"
---

# 2019年7月

{% alert update %}
Braze では今月、2 回 (その通り、**2 回**です) の製品リリース サイクルがありました。最新リリースは上部に記載されており、以前のリリースは [このページの下から始まります](#earlier-this-month)。
{% endalert %}

## SSO の有効化

[シングル サインオン]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/) (SSO) により、企業は Braze ダッシュボードへのアクセスを安全かつ集中的に制御できるようになります。つまり、単一の資格情報セットを使用して、Braze を含むさまざまなアプリケーションにアクセスできます。

企業は、[OAuth 2.0 サポートを使用した Google ログイン](https://developers.google.com/identity/protocols/OAuth2)に加えて、セキュリティ アサーション マークアップ言語 (SAML) サポートを使用した SSO を希望しています。これにより、最新の業界標準 (SAML 2.0) をサポートする [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/azure_ad/) や [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)などの大規模な ID プロバイダー (IdP) とシームレスに統合できるようになります。

Braze は以下をサポートします:
- [ワンログイン]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)
-[Azure アクティブ ディレクトリ]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/azure_ad/)
- [オクタ]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)

## イベントAPIキーの表示を調整する

この API キーをお客様が利用できるように、Adjust のパートナー ページを更新しました。

## 新しいパートナー

いくつかの新しいパートナーが Alloys プログラムに参加し、ドキュメントに追加されました。挨拶しましょう:
- [ファイブトラン]({{site.baseurl}}/partners/fivetran/)
- [タロンワン]({{site.baseurl}}/partners/talonone/)
- [バウチャー]({{site.baseurl}}/partners/voucherify/)

## キャンペーン詳細の改善

**キャンペーン** ページの**[キャンペーンの詳細]** セクションに、拡張されたキャンペーンの詳細が表示されるようになりました。

## セグメントとキャンバスに自分のものだけを表示

**キャンペーン** ページの「自分のものだけを表示」チェック フィルターは、非常に人気があることが証明されています。その結果、このオプションはキャンバス リストとセグメント リストにも追加されます。

### 進歩行動

[ユーザーが Canvas の 1 つのステップから次のステップに進むタイミングを]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) 選択できるようになりました。これらのオプションには、「メッセージを送信」と「遅延後に全視聴者に通知」が含まれます。

### Canvasのアプリ内メッセージ

Canvas で[アプリ内メッセージ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/) が利用できるようになりました。キャンバス ステップを追加し、利用可能なチャネルを参照してアプリ内メッセージを追加します。

# 今月上旬

## ユーザープロフィール画像の削除

Braze ユーザー プロファイルとユーザー検索に表示されるユーザー プロファイル写真を削除します。

## コンテンツ カード内の接続されたコンテンツ

[コンテンツ カード]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/overview/)で [接続されたコンテンツの]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) 文字列と機能を使用できるようになりました。

外部サーバーへの接続されたコンテンツの呼び出しは、カードがユーザーによって表示されたときではなく、カードが実際に送信されたときに行われます。電子メールと同様に、動的コンテンツはカードが実際に表示されたときではなく、送信時に計算され、決定されます。

## 返信先アドレスが空です

お客様は、 `null`Braze の **メール設定** ページまたは [API]({{site.baseurl}}/api/endpoints/messaging/#email-object-specification)を使用して、メール メッセージの「返信先」アドレスの値を取得します。 使用すると、返信はリストされた「送信元」アドレスに送信されます。 「差出人」アドレス欄を以下のようにカスタマイズできるようになりました。 `dan@emailaddress.com`すると、顧客は Dan に直接返信できるようになります。

設定するには `null` Braze からの電子メール メッセージの「返信先」アドレスの値を変更するには、ナビゲーションの **[設定の管理]** に移動し、**[電子メール設定]** タブに移動します。**[送信メール設定]** セクションまでスクロールし、**[「返信先」を除外し、返信をデフォルトのアドレスとして「送信元」に送信する]** を選択します。

## キャンペーンの比較

Braze では、1 つのウィンドウで [複数のキャンペーンを一度に確認して、それらの相対的なパフォーマンスを並べて比較できます]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/comparing_campaigns/)。

## Liquid でメッセージにディスパッチ ID をテンプレート化する

{% alert note %}
行動 `dispatch_id` Braze は、Canvas ステップ (スケジュール可能なエントリ ステップを除く) を、たとえ「スケジュール」されている場合でもトリガーされたイベントとして扱うため、Canvas とキャンペーンでは異なります。詳細はこちら [`dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/) キャンバスとキャンペーンでの動作。
{% endalert %}

メッセージ内（例えばURL内）からメッセージの送信を追跡したい場合は、 `dispatch_id`。この書式設定については、[Canvas 属性]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)の下にある、サポートされているパーソナライズ タグのリストを参照してください。

これは、 `api_id`、その点で `api_id` キャンペーン作成時には利用できませんが、プレースホルダーとしてテンプレート化されており、次のようにプレビューされます。 `dispatch_id_for_unsent_campaign`。ID はメッセージが送信される前に生成され、送信時間として含められます。

{% alert warning %}
液体テンプレートの `dispatch_id_for_unsent_campaign` アプリ内メッセージでは機能しません。アプリ内メッセージには `dispatch_id`。
{% endalert %}

## 「自分のものだけを表示」設定が維持される

キャンペーン グリッドの「自分のものだけを表示」フィルターは、 **キャンペーン** ページにアクセスするたびにオンのままになります。

## A/B テストのアップデート

最大 8 つのバリエーション (およびオプションのコントロール) を含む 1 回限りの [A/B テストを、]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/) キャンペーンのオーディエンスのユーザー指定の割合に送信し、その後、事前にスケジュールされた時間に残りのオーディエンスに最適なバリエーションを送信できます。
