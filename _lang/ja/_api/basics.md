---
nav_title: "API の概要"
article_title: API の概要
page_order: 2.1
description: "このリファレンス記事では、REST API とは何か、用語、API キーの概要など、API の基本について説明します。"
page_type: reference
alias: /api/api_key/
---

# API の概要

> このリファレンス記事では、一般的な用語や、REST API キーの概要、アクセス許可、およびそれらをセキュリティで保護する方法など、API の基本について説明します。 

## API 定義

以下は、Braze REST APIドキュメントに記載されている用語の概要です。

### エンドポイント

Brazeは、ダッシュボードとRESTエンドポイントのさまざまなインスタンスを管理しています。アカウントがプロビジョニングされたら、次のいずれかの URL にログインします。プロビジョニング先のインスタンスに基づいて、正しい REST エンドポイントを使用します。不明な場合は、[サポート チケット][サポート] を開くか、次の表を使用して、使用するダッシュボードの URL を正しい REST エンドポイントと照合します。

{% alert important %}
API呼び出しにエンドポイントを使用する場合は、RESTエンドポイントを使用します。

SDK統合には、REST [エンドポイントではなくSDKエンドポイント]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)を使用します。
{% endalert %}

|インスタンス|URL|REST エンドポイント|SDK エンドポイント|
|---|---|---|
|US-01| `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` | `sdk.iad-01.braze.com` |
|US-02| `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` | `sdk.iad-02.braze.com` |
|US-03| `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` | `sdk.iad-03.braze.com` |
|US-04| `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` | `sdk.iad-04.braze.com` |
|US-05| `https://dashboard-05.braze.com` | `https://rest.iad-05.braze.com` | `sdk.iad-05.braze.com` |
|US-06| `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` | `sdk.iad-06.braze.com` |
|US-07| `https://dashboard-07.braze.com` | `https://rest.iad-07.braze.com` | `sdk.iad-07.braze.com` |
|US-08| `https://dashboard-08.braze.com` | `https://rest.iad-08.braze.com` | `sdk.iad-08.braze.com` |
|EU-01| `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu` | `sdk.fra-01.braze.eu` |
|EU-02| `https://dashboard-02.braze.eu` | `https://rest.fra-02.braze.eu` | `sdk.fra-02.braze.eu` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### API の制限

ほとんどのAPIでは、Brazeのデフォルトのレート制限は1時間あたり250,000リクエストです。ただし、特定のリクエストタイプには、顧客ベース全体で大量のデータをより適切に処理するために、独自のレート制限が適用されます。詳細については、[API レート制限]({{site.baseurl}}/api/api_limits/)を参照してください

### ユーザー ID 

- 外部ユーザー IDは `external_id` 、データを送信する一意のユーザー識別子として機能します。この識別子は、同じユーザーに対して複数のプロファイルが作成されないように、Braze SDKで設定したものと同じにする必要があります。
- **BrazeユーザーID**: `braze_id` Brazeが設定する一意のユーザー識別子として機能します。この識別子は、external\_idsに加えて REST API を使用してユーザーを削除するために使用できます。

詳細については、お使いのプラットフォームに応じて、 [iOS][9]、 [Android][10]、 [Web][13] の記事を参照してください。

## REST API キー

RESTアプリケーション・プログラミング・インターフェース・キー(REST APIキー)は、APIコールを認証し、呼出し側アプリケーションまたはユーザーを識別するためにAPIに渡される一意のコードです。API アクセスは、会社の REST API エンドポイントへの HTTPS Web 要求を使用して行われます。Brazeでは、REST APIキーとアプリ識別子キーを併用して、データの追跡、アクセス、送信、エクスポート、分析を行い、お客様と当社の両方ですべてがスムーズに実行されていることを確認しています。

ワークスペースとAPIキーはBrazeで密接に関連しています。ワークスペースは、複数のプラットフォーム間で同じアプリケーションのバージョンを格納するように設計されています。また、多くのお客様は、ワークスペースを使用して、同じプラットフォーム上にアプリケーションの無料バージョンとプレミアム バージョンを含めています。お気づきかもしれませんが、これらのワークスペースも REST API を利用しており、独自の REST API キーを持っています。これらのキーに個別のスコープを設定すれば、API 上の特定のエンドポイントにアクセスできるようになります。API の呼び出しには必ず、エンドポイントへのアクセス権を持つキーを含める必要があります。

REST API キーとワークスペース API キー `api_key`の両方を .は `api_key` 、各リクエストにリクエストヘッダーとして含まれており、REST APIを使用できるようにする認証キーとして機能します。これらのREST APIは、ユーザーの追跡、メッセージの送信、ユーザーデータのエクスポートなどに使用されます。新しい REST API キーを作成するときは、特定のエンドポイントへのアクセス権を付与する必要があります。APIキーに特定の権限を割り当てることで、APIキーが認証できる呼び出しを正確に制限できます。

![[API キー] ページの [REST API キー] パネル。[27]

{% alert tip %}
REST API キーに加えて、アプリ、テンプレート、キャンバス、キャンペーン、コンテンツカード、セグメントなど、特定のものを API から参照するために使用できる識別子キーと呼ばれるタイプのキーも存在します。詳細については、「API 識別子のタイプ」を参照してください。
{% endalert %}

### REST API キーのアクセス許可

APIキーの権限は、特定のAPIコールへのアクセスを制限するためにユーザーまたはグループに割り当てることができる権限です。APIキーの権限のリストを表示するには、[ **設定** ]> **[APIキー**]に移動し、APIキーを選択します。

{% tabs %}
{% tab User Data %}

|権限 |エンドポイント |説明 |
|---|---|---|
ユーザー属性、カスタムイベント、および購入を記録します。
ユーザーを削除します。
既存のユーザーの新しいエイリアスを作成します。
外部 ID を持つエイリアス専用ユーザーを識別します。
ユーザー ID を使用してユーザープロファイル情報を照会します。
セグメントを使用してユーザープロファイル情報を照会します。
既存ユーザー 2 人を双方向マージ
既存のユーザーの外部 ID を変更します。
既存のユーザーの external ID を削除します。
既存ユーザーのエイリアスを更新します。
グローバルコントロールグループ内のユーザープロファイル情報を照会します。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

 {% endtab %}
 {% tab Email %}

|権限 |エンドポイント |説明 |
|---|---|---|
配信停止されたメールアドレスを照会します。
メールアドレスのステータスを変更します。
ハードバウンスされたメールアドレスを照会します。
ハードバウンスリストからメールアドレスを削除します。
迷惑メールリストからメールアドレスを削除します。
| `email.blacklist` | [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist/) |メールアドレスをブロックリストに登録します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Messages %}

|権限 |エンドポイント |説明 |
|---|---|---|
| `messages.send` | [`/messages/send `]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) |特定のユーザーに即時メッセージを送信します。|
メッセージを特定の時刻に送信するようにスケジュールします。
スケジュールされたメッセージを更新します。
スケジュールされたメッセージを削除します。
スケジュールされたブロードキャストメッセージをすべて照会します。
iOS ライブアクティビティを更新
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Campaigns %}

|権限 |エンドポイント |説明 |
|---|---|---|
既存のキャンペーンの送信をトリガーします。
API トリガー配信を使用してキャンペーンの今後の送信をスケジュールします。
API トリガー配信を使用してスケジュールされたキャンペーンを更新します。
API トリガー配信を使用してスケジュールされたキャンペーンを削除します。
キャンペーンのリストを照会します。
特定の期間のキャンペーン分析を照会します。
特定のキャンペーンの詳細を照会します。
特定の期間のメッセージ送信分析を照会します。
メッセージブラスト追跡の送信 ID を作成します。
キャンペーン内の特定のメッセージバリエーションの URL 詳細を照会します。
トランザクションメッセージングエンドポイントを使用してトランザクションメッセージングを送信できるようにします。
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Canvas %}

|権限 |エンドポイント |説明 |
|---|---|---|
既存のキャンバスの送信をトリガーします。
API トリガー配信を使用してキャンバスの今後の送信をスケジュールします。
API トリガー配信を使用してスケジュールされたキャンバスを更新します。
API トリガー配信を使用してスケジュールされたキャンバスを削除します。
キャンバスのリストを照会します。
特定の期間のキャンバス分析を照会します。
特定のキャンバスの詳細を照会します。
特定の期間のキャンバス分析のロールアップを照会します。
キャンバスステップ内の特定のメッセージバリエーションの URL 詳細を照会します。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Segments %}

|権限 |エンドポイント |説明 |
|---|---|---|
セグメントのリストを照会します。
特定の期間のセグメント分析を照会します。
特定のセグメントの詳細を照会します。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Purchases %}

|権限 |エンドポイント |説明 |
|---|---|---|
アプリで購入した製品のリストを照会します。
特定の期間内の、1 日あたりのアプリ内支出額の合計を照会します。
| `purchases.quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) |ある期間におけるアプリ内の 1 日あたりの合計購入数を照会します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Events %}

|権限 |エンドポイント |説明 |
|---|---|---|
カスタムイベントのリストを照会します。
特定の期間内に発生したカスタムイベントを照会します。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab News Feed %}

{% alert note %}
ニュースフィードは非推奨になります。Braze では、ニュースフィードツールをご利用のお客様に、コンテンツカードのメッセージングチャネルへの移行を推奨しています。柔軟性、カスタマイズ性、信頼性が向上します。詳細については、[移行ガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

|権限 |エンドポイント |説明 |
|---|---|---|
ニュースフィードカードのリストを照会します。
特定の期間のニュースフィード分析を照会します。
特定のニュースフィードの詳細を照会します。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Sessions %}

|権限 |エンドポイント |説明 |
|---|---|---|
特定の時間範囲内の、1 日あたりのセッション数を照会します。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab KPIs %}

|権限 |エンドポイント |説明 |
|---|---|---|
特定の期間内の、1 日あたりの固有のアクティブユーザー数を照会します。
特定の期間内の、30 日間ごとの固有のアクティブユーザー数の合計を照会します。
特定の期間内の、1 日あたりの新規ユーザー数を照会します。
特定の時間範囲内の、1 日あたりのアプリアンインストール数を照会します。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Templates %}

|権限 |エンドポイント |説明 |
|---|---|---|
ダッシュボードに新しいメールテンプレートを作成します。
特定のテンプレートの情報を照会します。
メールテンプレートのリストを照会します。
ダッシュボードに保存されているメールテンプレートを更新します。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab SSO %}

|権限 |説明 |
|---|---|---|
| `sso.saml.login` |ID プロバイダーが開始するログインを設定します。詳細については、「 [サービス プロバイダー (SP) が開始するログイン]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)」を参照してください。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Content Blocks %}

|権限 |エンドポイント |説明 |
|---|---|---|
特定のテンプレートの情報を照会します。
コンテンツブロックのリストを照会します。
ダッシュボードに新しいコンテンツブロックを作成します。
ダッシュボードの既存のコンテンツブロックを更新します。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Preference Center %}

|権限 |エンドポイント |説明 |
|---|---|---|
ユーザー設定センターを取得します。
ユーザー設定センターをリストします。
| `preference_center.update` | [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br><br>[`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/) |プリファレンスセンターを作成または更新します。|
ユーザー用のユーザー設定センターのリンクを取得します。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Subscription %}

|権限 |エンドポイント |説明 |
|---|---|---|
サブスクリプショングループのステータスを設定します
サブスクリプショングループのステータスを取得します。
| `subscription.groups.get` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) |特定のユーザーが明示的にサブスクライブおよびサブスクライブ解除されているサブスクリプション グループの状態を取得します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab SMS %}

|権限 |エンドポイント |説明 |
|---|---|---|
無効な電話番号を照会します。
ユーザーから無効な電話番号フラグを削除します。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Catalogs %}

|権限 |エンドポイント |説明 |
|---|---|---|
既存のカタログに複数の項目を追加します。
既存のカタログ内の複数の項目を更新します。
既存のカタログから複数の項目を削除します。
既存のカタログから単一の項目を取得します。
既存のカタログの単一の項目を更新します。
既存のカタログに単一の項目を作成します。
既存のカタログから単一の項目を削除します。
既存のカタログから単一の項目を置換します。
カタログを作成します。
カタログリストを取得
カタログを削除します。
既存のカタログから項目プレビューを取得します。
既存カタログの項目を置換
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% endtabs %}

## REST API キーの作成

新しい REST API キーを作成するには、次のようにします。

1. [ **設定** ] > **[API キー**] に移動します。このページには、既存の API キーが表示されます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、**開発者コンソール**の **[API 設定**] > API キーを作成できます。
{% endalert %}

{:start="2"}
2. [ **\+ Create New API Key]** をクリックします。
3. 新しいキーに名前を付けて、一目で識別できるようにします。
4. 新しいキーに関連付ける [アクセス許可](#rest-api-key-permissions) を選択します。
5. 新しいキーの [許可リストに登録された IP アドレス](#api-ip-allowlisting) とサブネットを指定します。

{% alert important %}
新しい API キーを作成した後は、権限の範囲や許可リストに登録された IP を編集できないことに注意してください。この制限は、セキュリティ上の理由から適用されています。キーのスコープを変更する必要がある場合は、更新されたアクセス許可で新しいキーを作成し、古いキーの代わりにそのキーを実装します。実装が完了したら、古いキーを削除してください。
{% endalert %}

## REST API キーの管理

REST APIキーは作成後に編集できませんが、「 **APIキー** 」ページからREST APIキーの詳細を表示したり、既存のREST APIキーを削除したりできます。**[Rest API Keys**] リストには、各キーについて次の情報が一目でわかります。

|分野 |説明 |
| ------------ | :------------------------------------------------------------------------------------------------------------------ |
|API キー名 |作成時にキーに付けられた名前。                                                                           |
|識別子 |API キー。                                                                                                       |
|作成者 |キーを作成したユーザーのメールアドレス。このフィールドは「N」と表示されます/A" for keys created before June 2023. |
| Date Created | The date this key was created.                                                                                      |
| Last Seen    | The date this key was last used. This field will show as "N/A" for keys that have never been used.                  |
{: .reset-td-br-1 .reset-td-br-2}

特定のキーの詳細を表示するには、リストからキーを選択します。その後、このキーが持つすべての権限、ホワイトリストに登録されたIP(存在する場合)、およびこのキーがBraze IPホワイトリストにオプトインされているかどうかを確認できます。

![][30]

キーを削除するには、 をクリックし <i class="fas fa-gear" alt="Settings"></i> 、対応するオプションを選択します。

![][29]

## REST API キーのセキュリティ

API キーは、API 呼び出しを認証するために使用されます。新しい REST API キーを作成するときには、特定のエンドポイントへのアクセス権をキーに付与する必要があります。APIキーに特定の権限を割り当てることで、APIキーが認証できる呼び出しを正確に制限できます。

REST API キーを使用すると、機密性の高い REST API エンドポイントにアクセスできるため、これらのキーをセキュリティで保護し、信頼できるパートナーとのみ共有します。ただしこれらのキーは一般公開しないでください。たとえば、このキーを使用して、Web サイトから AJAX 呼び出しを行ったり、その他のパブリックな方法で公開したりしないでください。

セキュリティのベストプラクティスは、ジョブを完了するために必要なアクセス権のみをユーザーに割り当てることです:この原則は、各キーに権限を割り当てることでAPIキーにも適用できます。これらの権限により、アカウントのさまざまな領域に対するセキュリティと制御が向上します。 

![APIキー作成時に利用可能なAPIキー権限][25]

{% alert warning %}
REST API キーを使用すると、機密性の高い可能性のある REST API エンドポイントにアクセスできるため、それらが安全に保存および使用されていることを確認してください。たとえば、このキーを使用して、Web サイトから AJAX 呼び出しを行ったり、その他のパブリックな方法で公開したりしないでください。
{% endalert %}

キーが誤って公開されてしまった場合は、開発者コンソールから削除できます。このプロセスに関するヘルプについては、[サポートチケット][サポート]を開いてください。

### API IP の許可リスト

さらなるセキュリティ強化のため、特定の REST API キーに対して REST API 要求が許可されている IP アドレスやサブネットのリストを指定できます。これは、許可リストまたはホワイトリストと呼ばれます。特定の IP アドレスやサブネットを許可するには、新規の REST API キーの作成時に [**IP をホワイトリストに追加**] セクションにそれらを追加します。 

![APIキー作成時にIPをホワイトリストに登録するオプション][26]

何も指定しない場合、すべての IP アドレスからリクエストを送信できます。

{% alert tip %}
Braze to Braze webhook を作成し、許可リストを使用する場合は、[ホワイトリストに追加する IP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting) のリストを確認してください。
{% endalert %}

## その他のリソース

### Ruby クライアントライブラリ

Rubyを使用してBrazeを実装している場合は、 [Rubyクライアントライブラリ](https://github.com/braze-inc/braze-api-client-ruby) を使用してデータのインポート時間を短縮できます。クライアントライブラリは、1 つのプログラミング言語 (この場合は Ruby) に固有のコードのコレクションであり、API の使用を容易にします。

Rubyクライアントライブラリは、 [ユーザーエンドポイント]({{site.baseurl}}/api/endpoints/user_data)をサポートしています。

{% alert note %}
このクライアントライブラリは現在ベータ版です。このライブラリをより良くするのを手伝ってみませんか?[smb-product@braze.com](mailto:smb-product@braze.com) でフィードバックをお送りください。
{% endalert %}

[1]: https://en.wikipedia.org/wiki/UTF-8
[7]: {{site.baseurl}}/api/objects_filters/connected_audience/
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/
[2]: {{site.baseurl}}/api/identifier_types/
[5]: {{site.baseurl}}/api/basics/
[6]: https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro
[25]: {% image_buster /assets/img_archive/api-key-permissions.png %}
[26]: {% image_buster /assets/img_archive/api-key-ip-whitelisting.png %}
[サポート]: {{site.baseurl}}/braze_support/
[28]: {% image_buster /assets/img_archive/create-new-key.png %}
[29]: {% image_buster /assets/img_archive/api-key-options.png %}
[27]: {% image_buster /assets/img_archive/rest-api-key.png %}
[30]: {% image_buster /assets/img_archive/view-api-key.png %}
