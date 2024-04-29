---
nav_title: フレンドバイ
article_title: フレンドバイ
description: "FriendbuyとBrazeを統合する方法を学ぶ。"
alias: /partners/friendbuy/
page_type: partner
search_tag: Partner

---

# フレンドバイ

> FriendbuyとBrazeの統合により、EメールやSMSの機能を拡張し、紹介やロイヤルティプログラムのコミュニケーションを簡単に自動化することができる。Brazeは、Friendbuyを通じて収集したオプトイン済みの電話番号の顧客プロファイルを作成する。

## 前提条件

始める前に、以下のものが必要だ：

| 前提条件         | 説明                                                                                                                    |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Friendbuy アカウント｜このパートナーシップを利用するには[Friendbuyアカウントが][1]必要だ。                                                              |
| Braze REST APIキー｜`users.track` 権限を持つBraze REST APIキー。これはBrazeダッシュボードの**Settings**>**API Keys**から作成できる。        |
| BrazeインスタンスのURLに依存する[。]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)|
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**Developer Console**>**API Settingsで**APIキーを作成できる。
{% endalert %}

## フレンドバイの統合

[Friendbuyで][1] **Developer Center**>**Integrationsを**選択し、Brazeインテグレーションカードで**Add integrationを**選択する。

フレンドバイのブレイズ統合カードだ。{: style="max-width:75%;"}

フォームにRESTエンドポイントとAPIキーを入力し、**Install Integrationを**選択する。

フレンドバイの統合フォーム][101]。{: style="max-width:55%;"}

[Friendbuyアカウントに][1]戻り、ページを更新する。統合が成功すれば、以下のようなメッセージが表示される：

![統合がインストールされた][102]。{: style="max-width:55%;"}

### カスタム属性

| カスタム属性名｜定義｜データタイプ
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
**| フレンドバイの紹介状況**｜紹介者は「*Advocate」*、紹介者は「*Referred Friend*」に分類される｜String｜文字列
|**Friendbuy Customer Name**｜紹介ウィジェットから情報を送信する際に顧客が入力した名前｜String｜文字列
**| Friendbuy紹介リンク**｜アドボケイトのために作成された個人紹介リンク（PURL）。例えば、httpsである：//fbuy.io/EzcW                                                       | String    |
|**Friendbuy Date of Last Share**｜最後に友達と共有した日時。アドボケイトがまだシェアしていない場合、プロパティは表示されない。| 時間
|**Friendbuy キャンペーンID**｜アドボケートのために生成された個人紹介リンクに関連するキャンペーンID｜String｜文字列
|**Friendbuy キャンペーン名**｜アドボケイトのために生成された個人紹介リンクに関連するキャンペーン名｜文字列｜**FriendbuyCampaign**Name
|**Friendbuy クーポンコード**｜お客様に配布された最新の紹介クーポンコード。注：表示されるコードは1つだけである。
|**Friendbuy Coupon Value**｜顧客に配布された最新のクーポンコードの通貨価値。                                                                     | 番号
|**Friendbuy クーポンステータス**｜直近に配信されたクーポンコードのステータス。注：ステータスは「分配」または「償還」となる。
|**Friendbuy Coupon Currency**｜顧客に配布された最新のクーポンコードに関連する通貨コード（USD、CADなど）またはパーセント（%）。                             | 文字列
|**Friendbuy クーポンキャンペーンID**｜クーポンコードに関連するキャンペーンID。                                                                          | 文字列
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## デフォルトの動作

顧客データがBrazeに送信される前に、顧客は紹介ウィジェットを通じて以下のボックスの1つ以上にチェックを入れてオプトインする必要がある：

紹介ウィジェット][103]だ。

{% alert note %}
Friendbuyは国際標準規格（E.164）を使用して電話番号を検証している。`555-555-5555` のような無効な番号はBrazeに送られない。
{% endalert %}

### 例

| チェックボックスが選択されている
|-------------------|-----------------------------------------------------------------|
| Eメールのみ｜お客様のEメールアドレスのみをBrazeに送信する。             |
| 電話のみ｜お客様の電話番号のみをBrazeに送信する。              |
| 顧客データがBrazeに送信されない。                              |
| 両方｜お客様のメールアドレスと電話番号がBrazeに送信される。|

[1]: https://retailer.friendbuy.io/
[100]: {% image_buster /assets/img/friendbuy/choosing_braze.png %}
[101]: {% image_buster /assets/img/friendbuy/install_form.png %}
[102]: {% image_buster /assets/img/friendbuy/install_success.png %}
[103]: {% image_buster /assets/img/friendbuy/referral_widget.png %}
