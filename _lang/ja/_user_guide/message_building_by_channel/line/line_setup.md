---
nav_title: LINE の設定
article_title: LINE の設定
description: "この記事では、Braze の LINE チャネルを設定する方法について、前提条件や推奨される次のステップを含めて説明します。"
page_type: partner
search_tag: パートナー
page_order: 0
channel:
 - LINE
alias: /line/line_setup/
---


# LINE の設定

> この記事では、Braze で LINE チャネルを設定する方法について、ユーザーの設定方法、ユーザー ID の照合方法、Braze での LINE テストユーザーの作成方法などを説明します。

## 前提条件

LINE と Braze を統合するには、以下が必要です。

- [LINE ビジネスアカウント](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- プレミアムまたは認証済みアカウントのステータス（既存のフォロワーを同期するために必要です）
   - [LINE のアカウントガイドライン](https://terms2.line.me/official_account_guideline_oth)を参照してください
- [LINE 開発者アカウント](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [LINE メッセージング API チャネル](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

Braze から LINE メッセージを送信すると、アカウントのメッセージクレジットが消費されます。

{% alert note %}
**`native_line_id` の設定**：ユーザー更新を Braze に送信することで `native_line_id` を設定できます（例：[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) エンドポイント、[CSV インポート]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import)、または[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/cloud_ingestion/)を使用）。クライアントサイドの SDK に `native_line_id` 専用のフィールドがない場合は、サーバーサイドのユーザー更新時にこれらの方法のいずれかで送信してください。
{% endalert %}

## LINE アカウントのタイプ

| アカウントタイプ | 説明 |
| --- | --- |
| 未認証アカウント | 未審査のアカウントで、誰でも（個人でも法人でも）取得できます。このアカウントはグレーのバッジで表示され、LINE アプリ内の検索結果には表示されません。 |
| 認証済みアカウント | LINE Yahoo の審査に合格したアカウントです。このアカウントは青いバッジで表示され、LINE アプリ内の検索結果に表示されます。<br><br>このアカウントは、日本、台湾、タイ、インドネシアに拠点を置くアカウントでのみ利用できます。  |
| プレミアムアカウント | LINE Yahoo の審査に合格したアカウントです。このアカウントは緑色のバッジで表示され、LINE アプリ内の検索結果に表示されます。このアカウントタイプは、LINE の判断で審査時に自動的に付与されます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 必要なアカウントタイプ

フォロワーを Braze に同期するには、LINE アカウントが認証済みかプレミアムである必要があります。アカウントを作成すると、デフォルトのステータスは「未認証」になります。アカウント認証を申請する必要があります。

### 認証済み LINE アカウントを申請する

{% alert important %}
認証済みアカウントは、日本、台湾、タイ、インドネシアを拠点とするアカウントでのみ利用できます。
{% endalert %}

1. LINE の [**公式アカウント**] ページで [**設定**] を選択します。
2. [**情報の公開**] の [認証ステータス] で、[**アカウント認証をリクエスト**] を選択します。
3. 必要な情報を入力します。
4. 審査結果の通知を待ちます。

## LINE を統合する

一貫したユーザー更新を設定するには、既存ユーザーの LINE ID を引き継ぎ、LINE のサブスクリプション状態にすべて同期させます。

1. [既存の既知ユーザーをインポートまたは更新する](#step-1-import-or-update-existing-line-users)
2. [LINE チャネルを統合する](#step-2-integrate-line-channel)
3. [ユーザー ID を照合する](#step-3-reconcile-user-ids)
4. [ユーザー更新方法を変更する](#step-4-change-your-user-update-methods)
5. [(オプション) ユーザープロファイルをマージする](#step-5-merge-profiles-optional)

{% alert note %}
1 つのワークスペースには、LINE アカウントを 1 つしか持つことができません。複数の LINE アカウントを持っている場合は、それぞれを別のワークスペースで使用することを推奨します。
{% endalert %}

## ステップ 1: 既存の LINE ユーザーをインポートまたは更新する

このステップは、すでに存在している識別済みの LINE ユーザーがいる場合に必要です。Braze が後から自動的にサブスクリプションステータスを取得して正しいユーザープロファイルを更新するためです。過去にユーザーと LINE ID を照合していない場合は、このステップをスキップしてください。 

[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) エンドポイント、[CSV インポート]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import)、または[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/cloud_ingestion/)など、Braze がサポートするどの方法でもユーザーをインポートまたは更新できます。 

どの方法を使用する場合でも、ユーザーの LINE ID を提供するために `native_line_id` を更新します。`native_line_id` の詳細については、[ユーザー設定](#user-setup)を参照してください。

{% alert note %}
サブスクリプショングループの状態は指定すべきではなく、指定しても無視されます。LINE はユーザーのサブスクリプションステータスの信頼できる情報源であり、サブスクリプション同期ツールまたはイベント更新によって Braze に同期されます。
{% endalert %}

## ステップ 2: LINE チャネルを統合する

統合プロセスが完了すると、Braze は自動的にそのチャネルの LINE フォロワーを Braze に取り込みます。すでに Braze ユーザープロファイルに紐付いている LINE ID については、各プロファイルのステータスが「subscribed」に更新され、残りの LINE ID は匿名ユーザーとして生成されます。さらに、LINE チャネルの新しいフォロワーがチャネルをフォローすると、未識別のユーザープロファイルが作成されます。

### ステップ 2.1: Webhook 設定を編集する

1. LINE の [**メッセージング API**] タブで、[**Webhook の設定**] を編集します。
   - [**Webhook URL**] を `https://anna.braze.com/line/events` に設定します。
      - これは、Braze により、ダッシュボードのクラスターに基づいて、統合時に別の URL に自動的に変更されます。
   - [**Webhook を使用**] と [**Webhook の再配信**] をオンにします。<br><br> ![Webhook 設定ページでは、Webhook URL の確認や編集、「Webhook を使用」、「Webhook の再配信」、「エラー統計の集約」のオンとオフを切り替えることができます。]({% image_buster /assets/img/line/webhook_settings.png %}){: style="max-width:70%;"}
2. [**プロバイダー**] タブに表示される以下の情報をメモしておきます。

| 情報タイプ | ロケーション |
| --- | --- |
| プロバイダー ID | プロバイダーを選択し、[**設定**] > [**基本情報**] の順に進みます。 |
| チャネル ID | プロバイダーを選択し、[**チャネル**] > 対象のチャネル > [**基本設定**] の順に進みます。 |
| チャネルシークレット | プロバイダーを選択し、[**チャネル**] > 対象のチャネル > [**基本設定**] の順に進みます。 |
| チャネルアクセストークン | プロバイダーを選択し、[**チャネル**] > 対象のチャネル > [**メッセージング API**] の順に進みます。チャネルアクセストークンがない場合は、[**発行**] を選択してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="3"}
3. [**設定**] ページ > [**応答設定**] の順に進み、以下を実行します。
   - [**グリーティングメッセージ**] をオフにします。これは、Braze ではフォロー時のトリガーで処理できます。
   - [**自動応答メッセージ**] をオフにします。トリガーメッセージはすべて Braze 経由で送信されます。これにより、LINE コンソールから直接送信できなくなることはありません。
   - [**Webhook**] をオンにします。

![アカウントがチャットを処理する方法を切り替えられる、応答設定ページ。]({% image_buster /assets/img/line/response_settings.png %}){: style="max-width:80%;"}

### ステップ 2.2: Braze で LINE サブスクリプショングループを作成する

1. LINE の Braze テクノロジーパートナーページにアクセスし、LINE の [**プロバイダー**] タブからメモした情報を入力します。
   - プロバイダー ID
   - チャネル ID
   - チャネルシークレット
   - チャネルアクセストークン

LINE アカウントに IP ホワイトリストを追加する場合は、[IP 許可リスト]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-allowlisting)にあるクラスターにリストされているすべての IP アドレスを許可リストに追加してください。

{% alert important %}
統合中は、チャネルシークレットが正しいことを確認してください。間違っている場合は、サブスクリプションステータスに不整合が生じる可能性があります。
{% endalert %}

![LINE 統合セクションが掲載された、LINE メッセージング統合ページ。]({% image_buster /assets/img/line/integration.png %}){: style="max-width:80%;"}

{: start="2"}
2. 接続後、Braze によって、ワークスペースに正常に追加された LINE 統合ごとに Braze サブスクリプショングループが自動的に生成されます。<br><br> フォロワーリストの変更（新しいフォロワーやフォロー解除など）は、自動的に Braze にプッシュされます。

![「LINE」チャネルに 1 つのサブスクリプショングループを表示する LINE サブスクリプショングループセクション。]({% image_buster /assets/img/line/line_subscription_groups.png %}){: style="max-width:80%;"}

## ステップ 3: ユーザー ID を照合する

[ユーザー ID の照合](#user-id-reconciliation)の手順に従って、ユーザーの LINE ID と既存の Braze ユーザープロファイルを組み合わせます。

## ステップ 4: ユーザーの更新方法を変更する 

Braze にユーザー更新を提供する方法がすでに確立されている場合、その方法を更新して新しいフィールド `native_line_id` を含める必要があります。これにより、Braze にその後送信されるユーザー更新にはそのフィールドが含まれるようになります。

サブスクリプションステータスの同期プロセスの一環として、または新しいフォロワーがチャネルをフォローしたときに作成された、`native_line_id` を持つ未識別のユーザープロファイルが Braze に存在する可能性があります。 

アプリケーションで、[ユーザー照合](#user-id-reconciliation)などの方法で LINE ユーザーが識別される場合は、[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) エンドポイントを使用して、Braze で未識別ユーザープロファイルをターゲットに設定できます。`native_line_id` が含まれるすべての未識別ユーザープロファイルには、ユーザーエイリアス `line_id` も含まれています。このユーザーエイリアスを使用して、ユーザープロファイルを識別対象として設定できます。

以下に、ユーザーエイリアス `line_id` を使用して未識別ユーザープロファイルをターゲットに設定する `/users/identify` のペイロードの例を示します。 

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

指定された `external_id` に対応する既存のユーザープロファイルが存在しない場合、これは未識別ユーザープロファイルに追加され、識別済みになります。`external_id` に対応するユーザープロファイルが存在する場合、未識別ユーザープロファイルにのみ存在するすべての属性は、既知のユーザープロファイルにコピーされます（`native_line_id` およびユーザーのサブスクリプションステータスを含む）。

アプリケーションで既知の LINE ユーザーを [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) エンドポイントから更新するには、それらのユーザーの外部識別子と `native_line_id` を渡します。あるユーザーに対して未識別ユーザープロファイルがすでに存在し、同じ `native_line_id` が `/users/track` を通じて別のユーザープロファイルに追加された場合、そのユーザーは未識別ユーザープロファイルのすべてのサブスクリプション状態を継承します。ただし、同じ `native_line_id` に対してユーザープロファイルが重複して存在することになります。イベント更新からの後続のサブスクリプション更新によって、すべてのプロファイルが適切に更新されます。 

{% alert note %}
LINE のサブスクリプション状態は `external_id` ではなく `native_line_id` によって追跡されます。例えば、ユーザー B のユーザープロファイルがユーザー A と同じ `native_line_id` で作成されたが、同じ `external_id` ではない場合、ユーザー B はユーザー A の LINE サブスクリプションステータスを継承します。
{% endalert %}

以下に、`native_line_id` を追加するために外部ユーザー ID でユーザープロファイルを更新する `/users/track` のペイロードの例を示します。 

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

## ステップ 5: プロファイルをマージする（省略可）

前述したように、同じ `native_line_id` を持つユーザープロファイルが複数存在する可能性があります。更新方法によって重複するユーザープロファイルが作成される場合は、`/user/merge` エンドポイントを使用して、未識別ユーザープロファイルを識別済みユーザープロファイルにマージできます。 

以下に、ユーザーエイリアス `line_id` により未識別ユーザープロファイルをターゲットに設定する `/users/merge` のペイロードの例を示します。

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
Braze での重複するユーザーの管理については、「[重複ユーザー]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users)」を参照してください。
{% endalert %}

## ユーザー設定

LINE は、ユーザーのサブスクリプション状態の信頼できる情報源です。ユーザーの LINE ID（`native_line_id`）を持っていても、そのユーザーが送信元の LINE チャネルをフォローしていなければ、LINE はそのユーザーにメッセージを配信しません。

これを管理するために、Braze は、サブスクリプションの同期や LINE のフォロー・フォロー解除のイベント更新など、適切に統合されたユーザー群をサポートするツールとロジックを提供しています。

### サブスクリプションの同期とイベントロジック

1. **サブスクリプション同期ツール：**このツールは、LINE チャネル統合が成功すると自動的にデプロイされます。既存のプロファイルの更新や新規プロファイルの作成に使用します。<br><br>LINE チャネルをフォローしている `native_line_id` を持つすべての Braze ユーザープロファイルは、サブスクリプショングループのステータスが `subscribed` に更新されます。LINE チャネルのフォロワーのうち、`native_line_id` を持つ Braze ユーザープロファイルがないフォロワーには、次のものが作成されます。<br><br>- `native_line_id` を、チャネルをフォローしているユーザーの LINE ID に設定した匿名ユーザープロファイル <br>- ユーザーエイリアス `line_id` がチャネルをフォローしているユーザーの LINE ID に設定される <br>- サブスクリプショングループステータス `subscribed`

{: start="2"}
2. **イベント更新：**これらはユーザーのサブスクリプションステータスを更新するために使用されます。Braze が統合 LINE チャネルのユーザーイベント更新を受信し、そのイベントがフォローである場合、ユーザープロファイルのサブスクリプショングループステータスは `subscribed` になります。イベントがフォロー解除の場合、ユーザープロファイルのサブスクリプショングループのステータスは `unsubscribed` になります。<br><br>- `native_line_id` が一致するすべての Braze ユーザープロファイルが自動的に更新されます。 <br>- イベントに一致するユーザープロファイルが存在しない場合、Braze は[匿名ユーザーを作成します]({{site.baseurl}}/line/user_management/)。

## ユースケース

これらは、上記のセットアップステップに従った後、ユーザーがどのように更新されるかのユースケースです。

##### 既存の Braze ユーザープロファイルがすでに LINE チャネルをフォローしている

1. Braze ユーザープロファイルが `native_line_id` 属性で更新されます。デフォルトのサブスクリプションステータスは `unsubscribed` です。
2. サブスクリプション同期ツールが実行され、ユーザーが LINE チャネルをフォローしていることが確認され、ユーザープロファイルがサブスクリプションステータス `subscribed` で更新されます。
3. サブスクリプションのステータスが変更された場合（ユーザーがチャネルをブロック、友だち解除、リフォローなど）、Braze は LINE から更新情報を受信し、それに応じて `native_line_id` を持つユーザープロファイルを更新します。

##### 既存のユーザープロファイルが LINE チャネルをブロック、友だち解除、フォロー解除している 

1. Braze ユーザープロファイルが `native_line_id` 属性で更新されます。デフォルトのサブスクリプションステータスは `unsubscribed` です。
2. サブスクリプション同期ツールは、ユーザーが LINE チャネルをフォローしていることを検出せず、ユーザーのサブスクリプションステータスは `unsubscribed` のままです。
3. その後、ユーザーがチャネルをフォローすると、Braze は LINE からの更新を受信し、ユーザープロファイルのサブスクリプションステータスを `subscribed` に更新します。

##### ユーザープロファイルの作成が LINE フォロー後に行われる

1. チャネルに新しい LINE フォロワーが増えます。
2. Braze は、`native_line_id` 属性をフォロワーの LINE ID に設定し、`line_id` のユーザーエイリアスをフォロワーの LINE ID に設定した匿名ユーザープロファイルを作成します。プロファイルのサブスクリプションステータスは `subscribed` です。
3. [ユーザーの照合](#user-id-reconciliation)により、ユーザーに LINE ID があることが確認されます。
  - 匿名ユーザープロファイルは、[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) エンドポイントを使用して識別できます。このユーザープロファイルに対する（[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) エンドポイント、[CSV インポート]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import)、または[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/cloud_ingestion/)による）その後の更新では、この既知の `external_id` でユーザーをターゲットに設定できます。

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

  - `native_line_id` を設定して、新しいユーザープロファイルを（[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) エンドポイント、[CSV インポート]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import)、または[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/cloud_ingestion/)により）作成できます。この新しいプロファイルは、既存の匿名ユーザープロファイルのサブスクリプションステータスの状態を継承します。この場合、複数のプロファイルが同じ `native_line_id` を共有することになります。これらはいつでも `/users/merge` エンドポイントを使用してマージできます。手順は[ステップ 5](#step-5-merge-profiles-optional) を参照してください。

##### ユーザープロファイルの作成が LINE のフォローより先に行われる

1. 新しいユーザーを獲得し、その情報を Braze に送信します。新しいユーザープロファイルが作成されます（プロファイル 1）。
2. ユーザーが LINE アカウントをフォローします。
3. Braze はフォローイベントを受信し、匿名ユーザープロファイル（プロファイル 2）を作成します。
4. [ユーザーの照合](#user-id-reconciliation)により、ユーザーに LINE ID があることが確認されます。
5. プロファイル 1 を更新し、`native_line_id` 属性を設定します。このプロファイルは、プロファイル 2 のサブスクリプションステータスを継承します。
  - これで、同じ `native_line_id` を持つ 2 つのユーザープロファイルが存在することになります。これらはいつでも `/users/merge` エンドポイントを使用してマージできます。手順は[ステップ 5](#step-5-merge-profiles-optional) を参照してください。

## ユーザー ID の照合 

LINE ID は、ユーザーがチャネルをフォローしたとき、または 1 回限りの「フォロワー同期」ワークフローを使用したときに、Braze が自動的に受信します。また、LINE ID はユーザーがフォローしているチャネルに固有のものであるため、ユーザーが自分の LINE ID を提供できる可能性は低いです。

LINE ID と既存の Braze ユーザープロファイルを組み合わせるには、2 つの方法があります。

- [LINE ログイン](#line-login)
- [ユーザーアカウントのリンク](#user-account-linking)

### LINE ログイン

この方法では、ソーシャルメディアのログインを利用して照合を行います。ユーザーがアプリにログインする際、[LINE ログイン](https://developers.line.biz/en/docs/line-login/overview/)を使ってユーザーアカウントを作成するか、ログインするかの選択肢が与えられます。

{% alert note %}
ユーザーごとに正しい LINE ID を取得するため、Braze と連携している LINE 公式アカウントやチャネルと同じプロバイダーで LINE ログインを設定してください。 
{% endalert %}

1. LINE Developer Console にアクセスし、LINE ログインでアプリにログインしたユーザーの[メールアドレスを取得する権限を申請します](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission)。

2. LINE が提供する適切なステップに従って、LINE ログインを実装します。<br><br>
  - [Web アプリの手順](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [ネイティブアプリの手順](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>検証リクエストの[スコープ設定](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes)には、必ず `email` を含めてください。 

{: start="3"}
3. [ID トークン検証呼び出し](https://developers.line.biz/en/reference/line-login/#verify-id-token)を使用して、ユーザーのメールアドレスを取得します。 

4. ユーザーの LINE ID（`native_line_id`）を、データベースにあるメールアドレスと一致するユーザープロファイルに保存するか、ユーザーのメールアドレスと LINE ID で新しいユーザープロファイルを作成します。

5. [`/user/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users/)、[CSV インポート]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import)、または[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/cloud_ingestion/)を使用して、新しいユーザー情報または更新されたユーザー情報を Braze に送信します。

#### ワークフロー

##### 既存フォロワーが LINE ログインを利用する

**シナリオ：**最初のサブスクライバー同期または「follow」イベントによる統合の後に、匿名ユーザーが作成されました。

1. ユーザーは LINE ログインを使ってアプリにログインします。
2. LINE はユーザーのメールアドレスを提供します。
3. Braze に更新されたユーザー情報を送信します（そのメールアドレスの既存ユーザープロファイルに LINE ID を追加するか、匿名ユーザーにメールアドレスを追加して更新します）。

##### 新規フォロワーが LINE ログインを使用する

**シナリオ：**ユーザーの LINE ID を持つユーザープロファイルが Braze に存在していません。

1. ユーザーは LINE ログインを使ってアプリにログインします。
2. LINE はユーザーのメールアドレスを提供します。
3. 次のいずれかを行います。
  - そのメールアドレスの既存ユーザープロファイルを更新し、ユーザーの LINE ID も含めます。
  - メールアドレスと LINE ID で新しいユーザープロファイルを作成します。
4. ユーザーが LINE 公式アカウントをフォローすると、Braze はフォローイベントを受信し、ユーザーのサブスクリプションステータスを `subscribed` に更新します。

### ユーザーアカウントのリンク 

この方法によって、ユーザーは LINE アカウントとアプリのユーザーアカウントをリンクさせることができます。その後、Braze で {% raw %}`{{line_id}}`{% endraw %} などの Liquid を使用して、ユーザーの LINE ID を Web サイトまたはアプリに渡すパーソナライズされた URL を作成します。渡された LINE ID は、既知のユーザーに関連付けることができます。

1. サブスクリプションの状態変化に基づき、ユーザーが LINE チャネルをサブスクライブしたときにトリガーされるアクションベースのキャンバスを作成します。<br>![ユーザーが LINE チャネルをサブスクライブした時にトリガーされるキャンバス。]({% image_buster /assets/img/line/account_link_1.png %})
2. （Liquid を使用して）ユーザーの LINE ID をクエリパラメーターとして渡し、Web サイトやアプリへのログインを促す次のようなメッセージを作成します。

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3. クーポンコードを配信するフォローアップメッセージを作成します。
4. （オプション）LINE ユーザーが識別されたときにトリガーして、ユーザーにクーポンコードを送信するアクションベースのキャンペーンまたはキャンバスを作成します。<br>![LINE ユーザーが識別された際にトリガーされるアクションベースのキャンペーン。]({% image_buster /assets/img/line/account_link_2.png %})

#### 仕組み

ユーザーのログイン後に、Web サイトまたはアプリに対して変更が行われます。この変更により、ユーザー ID が Braze に送信され、URL の一部として渡された LINE ID に関連付けられます。次にコードの例を示します。

```javascript
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

##### 既存ユーザーが LINE チャネルをフォローする

**シナリオ：**Braze の既存ユーザーが LINE でチャネルをフォローします。

1. LINE は Braze にフォローイベントを送ります。
2. Braze により、LINE ID、`line_id` ユーザーエイリアス、および LINE サブスクリプショングループステータス `subscribed` を持つ匿名ユーザープロファイルが作成されます。
3. ユーザーは、Web サイトやアプリへのリンクが記載された LINE メッセージを受け取り、ログインします。これでユーザープロファイルが既知になります。
4. 作成された匿名ユーザープロファイルが識別され、[/users/identify エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)によってユーザーの既知のユーザープロファイルにマージされます。既知のユーザープロファイルには LINE ID が含まれ、サブスクリプションのステータスは `subscribed` となります。
5. （省略可）クーポンコードが含まれている LINE メッセージをユーザーが受信し、Braze がその送信を Braze ユーザープロファイルに記録します。

## Braze で LINE テストユーザーを作成する

[ユーザー照合](#user-id-reconciliation)を設定する前に、「私は誰」キャンバスやキャンペーンを作成することで、LINE チャネルをテストすることができます。

1. 特定のトリガーワードでユーザーの Braze ユーザー ID を返すキャンバスを設定します。<br><br>トリガーの例 <br><br>![特定のサブスクリプショングループにインバウンド LINE を送信したユーザーにキャンペーンを送信するトリガー。]({% image_buster /assets/img/line/trigger.png %}){: style="max-width:80%;"}<br><br>メッセージの例<br><br>![Braze ユーザー ID を記載した LINE メッセージ。]({% image_buster /assets/img/line/message.png %}){: style="max-width:40%;"}<br><br>

2. Braze で、Braze ID を使用して特定のユーザーを検索し、必要に応じて変更します。

{% alert important %}
キャンバスに、送信を妨げるグローバルコントロールやコントロールグループがないことを確認してください。
{% endalert %}