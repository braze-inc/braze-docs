---
nav_title: Friendbuy
article_title: Friendbuy
description: "FriendbuyとBrazeを統合する方法を学ぶ。"
alias: /partners/friendbuy/
page_type: partner
search_tag: Partner

---

# Friendbuy

> [Friendbuyと](https://www.friendbuy.com/)Brazeを統合することで、メールやSMSの機能を拡張し、紹介やロイヤルティプログラムのコミュニケーションを簡単に自動化することができる。Braze では、Friendbuy 経由で収集されたすべてのオプトイン電話番号の顧客プロファイルが生成されます。

_この統合は Friendbuy によって管理されます。_

## 前提条件

開始する前に、次のものが必要になります。

| 前提条件          | 説明                                                                                                                              |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Friendbuyアカウント   | このパートナーシップを活用するには、[Friendbuy アカウント](https://retailer.friendbuy.io/)が必要です。                                                              |
| Braze REST API キー  | `users.track` 権限を持つ Braze REST API キー。これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。        |
| Braze RESTエンドポイント | [REST エンドポイント URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。これは Braze インスタンスの URL に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Friendbuy の統合

[Friendbuy](https://retailer.friendbuy.io/) で [**Developer Center**] > [**Integrations**] に移動し、Braze 統合カードで [**Add integration**] を選択します。

![Friendbuy の Braze 統合カード。]({% image_buster /assets/img/friendbuy/choosing_braze.png %}){: style="max-width:75%;"}

フォームに REST エンドポイントと API キーを入力し、[**Install Integration**] を選択します。

![Friendbuy 統合フォーム。]({% image_buster /assets/img/friendbuy/install_form.png %}){: style="max-width:55%;"}

[Friendbuy アカウント](https://retailer.friendbuy.io/)に戻り、ページを更新します。統合が成功すれば、以下のようなメッセージが表示される：

![統合がインストールされた]({% image_buster /assets/img/friendbuy/install_success.png %}){: style="max-width:55%;"}

### カスタム属性

| カスタム属性名            | 定義                                                                                                                                         | データ型 |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **Friendbuy Referral Status**    | 紹介者は *Advocate*、被紹介者は *Referred Friend* に分類されます。                                                          | String    |
| **Friendbuy Customer Name**      | 顧客が紹介ウィジェットから情報を送信する際に入力した名前                                                                 | String    |
| **Friendbuy Referral Link**      | Advocate に対して生成されるパーソナル紹介リンク (PURL)。例: https://fbuy.io/EzcW                                                       | String    |
| **Friendbuy Date of Last Share** | 共有チャネルを通じて最後に Advocate が Friend と共有した時点の日時。Advocate がまだ共有していない場合、このプロパティはて表示されません。 | 時刻      |
| **Friendbuy Campaign ID**        | アドボケートのために生成された個人紹介リンクに関連するキャンペーンID                                                               | String    |
| **フレンドバイキャンペーン名**      | アドボケートのために生成された個人紹介リンクに関連するキャンペーン名                                                             | String    |
| **Friendbuy クーポンコード**        | 顧客に配布された最新の紹介クーポンコード。注：表示されるコードは1つだけです。                                            | String    |
| **Friendbuy Coupon Value**       | 顧客に配布された最新のクーポンコードの通貨価値。                                                                     | 数値    |
| **Friendbuy Coupon Status**      | 顧客に配布された最新のクーポンコードのステータス。注：ステータスは「distributed」または「redeemed」です。                            | String    |
| **Friendbuy Coupon Currency**    | 顧客に配布された最新のクーポンコードに関連する通貨コード（USD、CADなど）またはパーセント（%）。                             | String    |
| **FriendbuyクーポンキャンペーンID** | 顧客のために生成されたクーポンコードに関連するキャンペーンID。                                                                          | String    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## デフォルト動作

顧客データを Braze に送信する前に、顧客は紹介ウィジェットで以下の1つ以上のボックスをオンにして、オプトインする必要があります。

![紹介ウィジェット]({% image_buster /assets/img/friendbuy/referral_widget.png %})

{% alert note %}
Friendbuyは国際標準規格(E.164)を採用し、実在する電話番号を検証している。`555-555-5555` のような無効な番号はBrazeに送られない。
{% endalert %}

### チェックボックスの動作

| チェックボックスが選択されている | 動作                                                        |
|-------------------|-----------------------------------------------------------------|
| Eメールのみ        | 顧客のメールアドレスだけが Braze に送信されます。             |
| 電話のみ        | 顧客の電話番号だけが Braze に送信されます。              |
| Neither           | 顧客データがBrazeに送信されることはない。                              |
| どちらも              | 顧客のメールアドレスと電話番号が Braze に送信されます。 |


