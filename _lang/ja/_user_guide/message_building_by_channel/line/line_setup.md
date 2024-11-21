---
nav_title: LINE の設定
article_title: LINE の設定
description: "この記事では、Braze の LINE チャネルを設定する方法について、前提条件や推奨される次のステップを含めて説明します。"
page_type: partner
search_tag: Partner
page_order: 0
channel:
 - LINE
alias: /line/line_setup/
---


# LINE の設定

> この記事では、BrazeでLINEチャネルを設定する方法について、ユーザーの設定方法、ユーザーIDの照合方法、BrazeでのLINEテストユーザーの作成方法などを紹介する。

## 前提条件

LINE と Braze を統合するには、以下が必要です。

- [LINE ビジネスアカウント](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- プレミアムまたは認証済みアカウントのステータス（既存のフォロワーを同期するために必要である）
   - [LINE のアカウントガイドライン](https://terms2.line.me/official_account_guideline_oth)を見る
- [LINE 開発者アカウント](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [LINE メッセージング API チャネル](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

BrazeからLINEメッセージを送信すると、アカウントのメッセージクレジットが消費される。

## LINE アカウントのタイプ

| アカウントタイプ | 説明 |
| --- | --- |
| 未認証アカウント | 未審査のアカウントで、誰でも (個人でも法人でも) 取得できます。このアカウントはグレーのバッジで表示され、LINE アプリ内の検索結果には表示されません。 |
| 認証済みアカウント | LINE Yahoo の審査に合格したアカウント。このアカウントは青いバッジで表示され、LINE アプリ内の検索結果に表示されます。<br><br>このアカウントは、日本、台湾、タイ、インドネシアに拠点を置くアカウントでのみ利用できます。  |
| プレミアムアカウント | LINE Yahoo の審査に合格したアカウント。このアカウントは緑色のバッジで表示され、LINE アプリ内の検索結果に表示されます。このアカウントタイプは、LINE の判断で審査時に自動的に付与されます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 必要な口座タイプ

フォロワーを Braze に同期するには、LINE アカウントが認証済みかプレミアムである必要があります。アカウントを作成すると、デフォルトのステータスは「未認証」になります。アカウント認証を申請する必要があります。

### 認証済みLINEアカウントを申請する

{% alert important %}
認証済みアカウントは、日本、台湾、タイ、インドネシアを拠点とするアカウントでのみ利用できます。
{% endalert %}

1. LINE の [**公式アカウント**] ページで [**設定**] を選択します。
2. [**情報の公開**] の [認証ステータス]で、[**アカウント認証をリクエスト**] を選択します。
3. 必要な情報を入力します。
4. 審査結果の通知を待ちます。

## LINEを統合する

一貫したユーザー更新を設定するには、既存ユーザーのLINE IDを引き継ぎ、LINEのサブスクリプション状態に同期させる：

1. [既存の既知ユーザーをインポートまたは更新する](#step-1-import-or-update-existing-line-users)
2. [LINEチャンネルを統合する](#step-2-integrate-line-channel)
3. [サブスクリプション・ステータスの同期をリクエストする](#step-3-request-a-subscription-status-sync)
4. [ユーザーの更新方法](#step-4-change-your-user-update-methods)
5. [(オプション）ユーザーをマージする](#step-5-merge-profiles-optional)

## ステップ 1: 既存のLINEユーザーをインポートまたは更新する

Brazeが自動的にサブスクリプションの状態を取得し、正しいユーザープロファイルを更新するからだ。過去にユーザーとLINE IDを照合していない場合は、このステップをスキップする。 

エンドポイント、CSVインポート、Cloud Data Ingestionなど、Brazeがサポートするどの方法でもユーザーをインポートまたは更新できる。 [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)エンドポイント、[CSVインポート]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import)、または[Cloud Data Ingestionを]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/)含む。 

どの方法を使うにせよ、`native_line_id` 、ユーザーのLINE IDを提供するように更新する。`native_line_id` の詳細については、[ユーザー設定を](#user-setup)参照のこと。

{% alert note %}
サブスクリプショングループの状態は指定すべきではなく、無視される。LINEはユーザーのサブスクリプションステータスの真実の情報源であり、サブスクリプション同期ツールまたはイベント更新によってBrazeに同期される。
{% endalert %}

## ステップ2:LINEチャネルを統合する

統合プロセスが完了すると、Brazeは自動的にそのチャネルのLINEフォロワーをBrazeに取り込む。すでにユーザープロファイルに紐付いているLINE IDについては、各プロファイルのステータスが「サブスクライバー」に更新され、残っているLINE IDは匿名ユーザーとなる。さらに、あなたのLINEチャンネルの新しいフォロワーがチャンネルをフォローすると、未確認のユーザープロファイルが作成される。

### ステップ 2.1:Webhook設定を編集する

1. LINE の [**メッセージング API**] タブで、[**Webhook の設定**] を編集します。
   - [**Webhook URL**] を [`https://anna.braze.com/line/events`] に設定します。
      - これは、Braze により、ダッシュボードのクラスターに基づいて、統合時に別の URL に自動的に変更されます。
   - [**Webhook を使用**] と [**Webhook の再配信**] をオンにします。<br><br> ![Webhook 設定ページでは、Webhook URL の確認や編集、[webhook を使用]、[Webhook の再配信]、[エラー統計の集約]のオンとオフを切り替えることができます。][1]{: style="max-width:70%;"}
2. [**プロバイダー**] タブに表示される以下の情報をメモしておきます。

| 情報タイプ | ロケーション |
| --- | --- |
| プロバイダー ID | プロバイダーを選択し、[**設定**] > [**基本情報**] の順に進みます。 |
| チャネル ID | プロバイダーを選択し、[**チャネル**] > [チャネル] > [**基本設定**] の順に進みます。 |
| チャネルシークレット | プロバイダーを選択し、[**チャネル**] > [チャネル] > [**基本設定**] の順に進みます。 |
| チャネルアクセストークン | プロバイダーを選択し、[**チャネル**] > [チャネル] > [**メッセージング API**] の順に進みます。チャネルアクセストークンがない場合は、[**発行**] を選択してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="3"}
3\.[**設定**] ページ > [**応答設定**]の順に進み、以下を実行します。
   - [**グリーティングメッセージ**]をオフにする。これは、Braze では、トリガーオンフォロー (trigger on follow) で処理できます。
   - [**自動応答メッセージ**] をオフにする。トリガーメッセージはすべて Braze 経由で送信されます。これにより、LINE コンソールから直接送信できなくなることはありません。
   - [**Webhook**] をオンにする。

![アカウントがチャットを処理する方法を切り替えられる、応答設定ページ。][2]{: style="max-width:80%;"}

### ステップ 2.2:BrazeでLINEサブスクリプショングループを作成する

1. LINE の Braze テクノロジーパートナーページにアクセスし、LINE の [**プロバイダー**] タブからメモした情報を入力します。
   - プロバイダー ID
   - チャネル ID
   - チャネルシークレット
   - チャネルアクセストークン

![LINE 統合セクションが掲載された、LINE メッセージング統合ページ。][3]{: style="max-width:80%;"}

{: start="2"}
2\.接続後、Brazeによって、ワークスペースに正常に追加された LINE 統合ごとに Braze サブスクリプショングループが自動的に生成されます。<br><br> フォロワーリストの変更 (新しいフォロワーやフォロー解除など) は、自動的に Braze にプッシュされます。

![「LINE」チャネルに 1 つのサブスクリプショングループを表示する LINE サブスクリプショングループセクション。][4]{: style="max-width:80%;"}

## ステップ 3:ユーザーIDを照合する

ユーザー[ID照合の](#user-id-reconciliation)ステップに従い、ユーザーのLINE IDと既存のBrazeユーザープロファイルを統合する。

## ステップ4:ユーザーの更新方法を変更する 

Brazeにユーザーアップデートを提供するメソッドがすでにあると仮定すると、それを更新して新しいフィールド`native_line_id` 、Brazeに送信される後続のユーザーアップデートにそのフィールドが含まれるようにする必要がある。

サブスクリプションステータスの同期プロセスの一環として、または新しいフォロワーがあなたのチャネルをフォローしたときに作成された、`native_line_id` を持つ未確認のユーザープロファイルがBrazeに存在する可能性がある。 

[ユーザー照合などで](#user-id-reconciliation)アプリケーションにLINEユーザーが識別子として登録された場合、Brazeで未登録の可能性があるユーザープロファイルをターゲットにすることができる。 [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)エンドポイントを使用する。`native_line_id` を持つすべての未確認ユーザープロファイルは、ユーザーエイリアス`line_id` も持っており、これを使用してユーザープロファイルを特定することができる。

以下は、`/users/identify` に対するペイロードの例である。このペイロードは、ユーザーエイリアス`line_id` 、未確認のユーザープロファイルをターゲットとしている： 

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

提供された`external_id` に対して既存のユーザープロファイルが存在しない場合、そのユーザープロファイルは未確認のユーザープロファイルに追加され、識別される。`external_id` に対してユーザープロファイルが存在する場合、未確認のユーザープロファイルにのみ存在するすべての属性は、`native_line_id` およびユーザーのサブスクリプションステータスを含め、既知のユーザープロファイルにコピーされる。

アプリケーションで既知のLINEユーザーを更新するには、そのユーザーの外部識別子をエンドポイントに渡す。 [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)`native_line_id`エンドポイントから更新することができる。あるユーザーに対して未確認ユーザープロファイルがすでに存在し、同じ`native_line_id` が`/users/track` を通じて別のユーザープロファイルに追加された場合、そのユーザーは未確認ユーザープロファイルのすべてのサブスクリプション状態を継承する。ただし、ユーザープロファイルは、同じ`native_line_id` で重複して存在する。イベント更新によるその後のサブスクリプション更新は、それに応じてすべてのプロファイルを更新する。 

`native_line_id` を追加するために、外部ユーザーIDによってユーザープロファイルを更新する、`/users/track` へのペイロードの例を以下に示す： 

{% raw %}
```json
{
   "attributes": [
       {
           "external_id": "known_external_id_from_your_application",
           "native_line_id": "U89f4a626548ccd48482f529a482f138b",
           "other": "attribute"
       }
   ]
}
```
{% endraw %}

## ステップ 5: プロファイルのマージ（オプション）

上記のように、同じ`native_line_id` で複数のユーザープロファイルが存在する可能性がある。更新方法によって重複したユーザープロファイルが作成される場合、`/user/merge` エンドポイントを使用して、識別子未設定のユーザープロファイルを識別済みのユーザープロファイルにマージすることができる。 

以下は、ユーザーエイリアス`line_id` による未確認のユーザープロファイルをターゲットとする、`/users/merge` へのペイロードの例である：

{% raw %}
```json
{
 "merge_updates": [
   {
     "identifier_to_merge": {
       "user_alias": {
         "alias_name": "U89f4a626548ccd48482f529a482f138b",
         "alias_label": "line_id"
       }
     },
     "identifier_to_keep": {
       "external_id": "known_external_id_from_your_application"
     }
   }
 ]
}
```
{% endraw %}

{% alert tip %}
Brazeでの重複ユーザーの管理については、[重複ユーザーを]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users)参照。
{% endalert %}

## ユーザー設定

LINEは、ユーザーのサブスクリプション状態の真実の情報源である。ユーザーのLINE ID (`native_line_id`) を持っていても、そのユーザーが送信元のLINEチャネルをフォローしていなければ、LINEはそのユーザーにメッセージを配信しない。

これを管理するために、Brazeは、サブスクリプションの同期やLINEのフォロー・アンフォローのイベント更新など、うまく統合されたユーザー群をサポートするツールとロジックを提供している。

### サブスクリプションの同期とイベントロジック

1. **サブスクリプション同期ツール：**このツールは、LINEチャネル統合が成功すると自動的に導入される。既存のプロファイルの更新や新規プロファイルの作成に使用する。<br><br>LINEチャネルをフォローする`native_line_id` を持つすべてのBrazeユーザープロファイルは、サブスクリプショングループのステータスが`subscribed` に更新される。LINEチャンネルのフォロワーで、Brazeのユーザープロファイルを持っていない人は、`native_line_id` ：<br><br>-`native_line_id` 、チャンネルに続くユーザーLINE IDに設定された匿名ユーザープロファイルが作成される。 <br>\- ユーザーエイリアス`line_id` チャンネルに続くユーザーLINE IDに設定される。 <br>\- サブスクリプショングループのステータスは以下のとおりである。 `subscribed`

{: start="2"}
2\.**イベントの更新**これらはユーザーのサブスクリプションステータスを更新するために使用される。Brazeが統合LINEチャネルのユーザーイベント更新を受信し、そのイベントがフォローである場合、ユーザープロファイルのサブスクリプショングループステータスは`subscribed` 。イベントがフォロー解除の場合、ユーザープロファイルのサブスクリプショングループのステータスは`unsubscribed` となる。<br><br>-`native_line_id` が一致するすべてのBrazeユーザープロファイルが自動的に更新される。<br>\- イベントに一致するユーザープロファイルが存在しない場合、Brazeは[匿名ユーザーを作成する](https://www.braze.com/docs/line/user_management/)。

## ユースケース

これらは、上記のセットアップステップに従った後、ユーザーがどのように更新されるかのユースケースである。

##### 既存のBrazeユーザープロファイルがすでにLINEチャネルをフォローしている

1. Brazeユーザープロファイルが`native_line_id` 属性で更新される。デフォルトのサブスクリプション・ステータスは`unsubscribed` である。
2. サブスクリプション同期ツールを実行し、ユーザーがLINEチャネルをフォローしていることを確認し、ユーザープロファイルのサブスクリプションステータス`subscribed` を更新する。
3. サブスクリプションのステータスが変更された場合（ユーザーがチャンネルをブロック、友だち解除、リフォローなど）、BrazeはLINEから更新情報を受信し、それに応じてユーザープロファイルを更新する（`native_line_id` ）。

##### 既存のユーザープロファイルがLINEチャネルをブロック、友だち解除、フォロー解除している 

1. Brazeユーザープロファイルが`native_line_id` 属性で更新される。デフォルトのサブスクリプション・ステータスは`unsubscribed` である。
2. サブスクリプション同期ツールは、ユーザーがLINEチャネルをフォローしていることを検出せず、ユーザーのサブスクリプションステータスは`unsubscribed` のままである。
3. その後、ユーザーがチャンネルをフォローすると、BrazeはLINEからの更新を受信し、ユーザープロファイルにサブスクリプションステータス`subscribed` を更新する。

##### ユーザープロファイル作成はLINEフォロー後に行われる

1. チャネルに新しいLINEフォロワーが増える。
2. Brazeは、`native_line_id` 属性をフォロワーのLINE ID に設定し、`line_id` のユーザーエイリアスをフォロワーのLINE ID に設定した匿名ユーザープロファイルを作成する。プロファイルのサブスクリプション・ステータスは`subscribed` である。
3. ユーザーは、[ユーザー照合によって](#user-id-reconciliation)LINE IDを持つことが識別される。
  - 匿名ユーザープロファイルは、エンドポイント [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)エンドポイントを使う。その後の更新（エンドポイント、CSVインポート、またはクラウド・データ・インジェストを通じて）は、この既知の。 [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)エンドポイント、[CSV ユーザーインポート]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import)、または[クラウドデータインジェスチョンを通じて]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/)）、このユーザープロファイルは、この既知の`external_id` によってユーザーをターゲットにすることができる。

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

  - 新しいユーザープロファイルは、 を設定することで（エンドポイント、CSVインポート、またはクラウドデータ・インジェストを通じて）作成できる。 [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)エンドポイント、[CSV インポート]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import)、または[クラウド・データ・インジェストによって]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/))、新しいユーザー・プロファイルを作成するには、`native_line_id` を設定する。この新しいプロファイルは、既存の匿名ユーザープロファイルのサブスクリプションステータスの状態を継承する。この場合、複数のプロファイルが同じ`native_line_id` を共有することになる。これらは、[ステップ5で](#step-5-merge-profiles-optional)説明したプロセスで、`/users/merge` エンドポイントを使用して、いつでも統合することができる。

##### ユーザープロファイルの作成はLINEのフォローより先に行われる

1. 新しいユーザーを獲得し、その情報をBrazeに送信する。新しいユーザープロファイルが作成される（プロファイル1）。
2. ユーザーはあなたのLINEアカウントをフォローしている。
3. Brazeはフォローイベントを受信し、匿名ユーザープロファイル（プロファイル2）を作成する。
4. ユーザーは、[ユーザー照合によって](#user-id-reconciliation)LINE IDを持つことが識別される。
5. プロファイル1を更新し、`native_line_id` 属性を設定する。このプロファイルは、プロファイル2のサブスクリプション・ステータス状態を継承する。
  - これで、同じ`native_line_id` を持つ2つのユーザープロファイルが存在することになる。これらは、[ステップ5で](#step-5-merge-profiles-optional)説明したプロセスで、`/users/merge` エンドポイントを使用して、いつでも統合することができる。

## ユーザーIDの照合 

LINE IDは、ユーザーがあなたのチャネルをフォローしたとき、または1回限りの「フォロワー同期」ワークフローを使用したときに、Brazeが自動的に受信する。また、LINE IDはユーザーがフォローしているチャネルに固有のものであるため、ユーザーがLINE IDを提供できる可能性は低い。

LINE IDと既存のBrazeユーザープロファイルを組み合わせるには、2つの方法がある：

- [LINEログイン](#line-login)
- [ユーザーアカウントのリンク](#user-account-linking)

### LINEログイン

この方法では、ソーシャルメディアのログインを利用して照合を行う。ユーザーがアプリにログインする際、[LINEログインを使って](https://developers.line.biz/en/docs/line-login/overview/)ユーザーアカウントを作成するか、ログインするかの選択肢が与えられる。

{% alert note %}
ユーザーごとに正しいLINE IDを取得するため、Brazeと連携しているLINE公式アカウントやチャネルと同じプロバイダでLINEログインを設定する。
{% endalert %}

1. LINE Developer Consoleにアクセスし、LINEログインでアプリにログインしたユーザーの[メールアドレスを取得する権限を申請する](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission)。

2. LINEが提供する適切なステップに従って、LINEログインを実施する：<br><br>
  - [ウェブアプリの方向性](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [ネイティブアプリの案内](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>検証依頼のために[設定したスコープには](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes)、必ず`email` 。 

{: start="3"}
3\.[Verify IDトークン・コールを](https://developers.line.biz/en/reference/line-login/#verify-id-token)使用して、ユーザーのメールを取得する。 

4. ユーザーのLINE ID (`native_line_id`)を、データベースにあるメールと一致するユーザープロファイルに保存するか、ユーザーのメールとLINE IDで新しいユーザープロファイルを作成する。

5. [`/user/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users/)、[CSVインポート]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import)、または[クラウドデータインジェストを]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/)使用して、新規または更新ユーザー情報をBrazeに送信する。

#### ワークフロー

##### 既存フォロワーがLINEログインを利用する

**シナリオはこうだ：**匿名ユーザーは、最初のサブスクライバー同期中、または統合後に "フォロー "イベントを通じて作成された。

1. ユーザーはLINEログインを使ってアプリにログインする。
2. LINEはユーザーのメールを提供する。
3. Brazeに更新ユーザー（LINE IDを追加するためにそのメールを既存のユーザープロファイルに送る）、または匿名ユーザーにそのメールを更新する。

##### 新規フォロワーはLINEログインを使用する

**シナリオはこうだ：**ユーザーIDのユーザープロファイルがBrazeに存在しない。

1. ユーザーはLINEログインを使ってアプリにログインする。
2. LINEはユーザーのメールを提供する。
3. どちらかだ：
  - 既存のユーザープロファイルを更新し、そのメールのユーザーIDをLINE IDとして登録する。
  - メールとLINE IDで新しいユーザープロファイルを作成する。
4. ユーザーがLINE公式アカウントをフォローすると、Brazeはフォローイベントを受信し、ユーザーのサブスクリプションステータスを`subscribed` に更新する。

### ユーザーアカウントのリンク 

この方法によって、ユーザーはLINEアカウントとアプリのユーザーアカウントをリンクさせることができる。その後、BrazeのパーソナライズされたURL（{% raw %}`{{line_id}}`{% endraw %} など）を作成し、ユーザーのLINE IDをWebサイトやアプリに渡すことで、既知のユーザーと関連付けることができる。

1. サブスクリプションの状態変化に基づき、ユーザーがLINEチャネルにサブスクライブしたときにトリガーされるアクションベースのキャンバスを作成する。<br>![][9]
2. ユーザーのLINE IDをクエリーパラメーターとして（Liquidを通して）渡し、Webサイトやアプリへのログインを促すメッセージを作成する：

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3\.クーポンコードを配信するフォローアップメッセージを作成する。
4. (オプション) LINEユーザーが識別子されたときにトリガーして、ユーザーにクーポンコードを送信するアクションベースのキャンペーンまたはキャンバスを作成する。<br>![][10]

#### 仕組み

ユーザーがログインした後、Webサイトやアプリを変更し、ユーザーIDをBrazeに送り返し、URLの一部として渡されたLINE IDと関連付ける：

```json
const currentUrl = new URL(window.location.href)
const queryParams = new URLSearchParams(currentUrl.search);
const lineUserId = queryParams.get("line_user_id")

if (user && isLoggedIn && lineUserId) {
  post(
   "https://rest.iad-03.braze.com	/users/identify",
   {
     "aliases_to_identify": [
       {
   "external_id": user.getUserId(),
   "user_alias": {
     "alias_name": lineUserId,
     "alias_label": "line_id"
   }
 }
      ]
    }
  )
  braze.logCustomEvent("identified_line_user_for_promotion");
}
```

#### ワークフロー

##### 既存ユーザーがあなたのLINEチャネルをフォローしている

**シナリオはこうだ：**Brazeの既存ユーザーがLINEであなたのチャネルをフォローしている。

1. LINEはBrazeにフォローイベントを送る。
2. Brazeは、LINE ID、`line_id` ユーザーエイリアス、`subscribed` のLINEサブスクリプショングループステータスを持つ匿名ユーザープロファイルを作成する。
3. ユーザーは、あなたのWebサイトやアプリへのリンクが記載されたLINEメッセージを受け取り、ログインする。ユーザープロファイルが判明した。
4. 作成された匿名ユーザープロファイルは識別され、[/users/identifyエンドポイントを通じて]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)ユーザーの既知のユーザープロファイルにマージされる。既知のユーザープロファイルにはLINE IDが含まれ、サブスクリプションのステータスは`subscribed` となっている。
5. (オプション) ユーザーはクーポンコードのLINEメッセージを受信し、Brazeはユーザープロファイルに送信をメッセージングする。

## BrazeでLINEテストユーザーを作成する

[ユーザー照合を](#user-id-reconciliation)設定する前に、「私は誰」キャンバスやキャンペーンを作成することで、LINEチャネルをテストすることができる。

1. 特定のトリガーワードでユーザーの Braze ユーザー ID を返すキャンバスを設定します。<br><br>トリガーの例 <br><br>![特定のサブスクリプショングループにインバウンド LINE を送信したユーザーにキャンペーンを送信するトリガー。][7]{: style="max-width:80%;"}<br><br>メッセージの例<br><br>![Braze ユーザー ID を記載した LINE メッセージ。][8]{: style="max-width:40%;"}<br><br>

2. Braze で、Braze ID を使用して特定のユーザーを検索し、必要に応じて変更します。

{% alert important %}
キャンバスに、送信を妨げるグローバルコントロールやコントロールグループがないことを確認します。
{% endalert %}


[1]: {% image_buster /assets/img/line/webhook_settings.png %}
[2]: {% image_buster /assets/img/line/response_settings.png %}
[3]: {% image_buster /assets/img/line/integration.png %}
[4]: {% image_buster /assets/img/line/line_subscription_groups.png %}
[5]: {% image_buster /assets/img/line/filter_group.png %}
[6]: {% image_buster /assets/img/line/csv_export_user_data.png %}
[7]: {% image_buster /assets/img/line/trigger.png %}
[8]: {% image_buster /assets/img/line/message.png %}
[9]: {% image_buster /assets/img/line/account_link_1.png %}
[10]: {% image_buster /assets/img/line/account_link_2.png %}