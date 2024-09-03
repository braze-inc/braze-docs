---
nav_title: Friendbuy
article_title: Friendbuy
description: "FriendbuyとBrazeを統合する方法を学ぶ。"
alias: /partners/friendbuy/
page_type: partner
search_tag: Partner

---

# Friendbuy

> FriendbuyとBrazeの統合により、EメールやSMSの機能を拡張し、紹介やロイヤルティプログラムのコミュニケーションを簡単に自動化することができる。Brazeは、Friendbuyを通じて収集したオプトイン済みの電話番号の顧客プロファイルを作成する。

## 前提条件

始める前に、以下のものが必要だ：

| 前提条件          | 説明                                                                                                                              |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Friendbuyアカウント   | このパートナーシップを利用するには、[Friendbuyアカウントが][1]必要だ。                                                              |
| Braze REST API キー  | `users.track` 権限を持つ Braze REST API キー。これは、Brazeダッシュボードの**「設定**」>「**APIキー**」から作成できる。        |
| Braze RESTエンドポイント | [RESTエンドポイントURLは]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)、BrazeインスタンスのURLに依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**Developer Console**>**API Settingsで**APIキーを作成できる。
{% endalert %}

## フレンドバイの統合

[Friendbuyで][1] **Developer Center**>**Integrationsを**選択し、Brazeインテグレーションカードで**Add integrationを**選択する。

![フレンドバイのブレイズ統合カード。][100]{: style="max-width:75%;"}

フォームにRESTエンドポイントとAPIキーを入力し、**Install Integrationを**選択する。

![Friendbuyの統合フォーム。][101]{: style="max-width:55%;"}

[Friendbuyアカウントに][1]戻り、ページを更新する。統合が成功すれば、以下のようなメッセージが表示される：

![統合をインストールした][102]{: style="max-width:55%;"}

### カスタム属性

| カスタム属性名            | 定義                                                                                                                                         | データ型 |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **フレンドバイ紹介状況**    | 紹介者は「*Advocate」*、被紹介者は「*Referred Friend*」に分類される。                                                          | String    |
| **フレンドバイカスタマー名**      | 顧客が紹介ウィジェットから情報を送信する際に入力した名前                                                                 | String    |
| **フレンドバイ紹介リンク**      | アドボケイトのために生成された個人紹介リンク（PURL）。例えば、こうだ、 https://fbuy.io/EzcW                                                       | String    |
| **フレンドシップ最終購入日** | アドボケイトが最後に共有チャネルを通じてフレンドと共有した日時。アドボケイトがまだシェアしていない場合、プロパティは表示されない。 | 時刻      |
| **フレンド購入キャンペーンID**        | アドボケートのために生成された個人紹介リンクに関連するキャンペーンID                                                               | String    |
| **フレンドバイキャンペーン名**      | アドボケートのために生成された個人紹介リンクに関連するキャンペーン名                                                             | String    |
| **Friendbuy クーポンコード**        | 顧客に配布された最新の紹介クーポンコード。注：表示されるコードは1つだけである。                                            | string    |
| **フレンドバイクーポン**       | 顧客に配布された最新のクーポンコードの通貨価値。                                                                     | 数値    |
| **Friendbuyクーポンステータス**      | 顧客に配布された最新のクーポンコードのステータス。注：ステータスは「分配」または「償還」となる。                            | string    |
| **Friendbuyクーポン**    | 顧客に配布された最新のクーポンコードに関連する通貨コード（USD、CADなど）またはパーセント（%）。                             | String    |
| **FriendbuyクーポンキャンペーンID** | 顧客のために生成されたクーポンコードに関連するキャンペーンID。                                                                          | String    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## デフォルトの動作

顧客データがBrazeに送信される前に、顧客は紹介ウィジェットを通じて以下のボックスの1つ以上にチェックを入れてオプトインする必要がある：

![紹介ウィジェット][103]

{% alert note %}
Friendbuyは国際標準規格(E.164)を採用し、実在する電話番号を検証している。`555-555-5555` のような無効な番号はBrazeに送られない。
{% endalert %}

### チェックボックスの動作

| チェックボックスが選択されている | 動作                                                        |
|-------------------|-----------------------------------------------------------------|
| Eメールのみ        | Brazeに送信されるのは顧客のEメールアドレスのみである。             |
| 電話のみ        | 顧客の電話番号だけがブレイズに送られる。              |
| どちらでもない           | 顧客データがBrazeに送信されることはない。                              |
| どちらも              | 顧客の電子メールアドレスと電話番号がブレイズに送信される。 |

[1]: https://retailer.friendbuy.io/
[100]: {% image_buster /assets/img/friendbuy/choosing_braze.png %}
[101]: {% image_buster /assets/img/friendbuy/install_form.png %}
[102]: {% image_buster /assets/img/friendbuy/install_success.png %}
[103]: {% image_buster /assets/img/friendbuy/referral_widget.png %}
