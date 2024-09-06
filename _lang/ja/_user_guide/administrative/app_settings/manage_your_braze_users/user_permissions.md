---
nav_title: 権限
article_title: Braze許可
page_order: 2
page_type: reference
description: "このリファレンス記事では、Braze でのユーザー権限の動作について説明します。ここでは、ユーザー権限の編集および設定を行って、アプリにアクセスできるユーザーをダッシュボードで選択する方法を学習できます。"
tool: Dashboard

---

# Braze許可

> 権限セットの作成、ロールの作成、ユーザー権限の編集、およびユーザー権限のエクスポートの方法について説明します。これにより、ユーザーが必要なワークスペースと機能にのみアクセスできるようになります。

## 権限セットの作成

権限セットを使用して、特定のサブジェクト領域またはアクションに関連する権限をバンドルします。ワークスペースが異なれば、同じアクセス権を必要とするダッシュボード ユーザーにアプリ嘘をついてしまうことがあります。権限セットを作成するには、**Settings** > **Permission Settings** に移動し、**Create permission set** を選択します。各権限については、[権限一覧](#list-of-permissions)を参照してください。

{% tabs ローカル %}
{% tab 許可セットの例 %}
|名前|権限|
\|-----------|----------------|
|開発者|"Dev Console へのアクセス"|
|マーカー|"キャンペーン、キャンバス、カード、機能フラグ、セグメント、メディアライブラリ、および環境設定センターへのアクセス" <br> 「メディアライブラリアセットの管理」|
|ユーザ管理|"ダッシュボードユーザの管理" <br> 「チームの管理」|
{: .reset-td-br-1 .reset-td-br-2}
{% endtab %}
{% endtabs %}

## ロールの作成

{% alert note %}
ロールは現在初期アクセス中です。初期のアクセスに参加したい場合は、Braze 顧客のサクセスマネージャーにお問い合わせください。
{% endalert %}

ロールを使用すると、ワークスペースのアクセスコントロールと個別のカスタムアクセス許可をバンドルすることで、より多くの構成が可能になります。これは、1 つのダッシュボードに多数のブランドまたは地域ワークスペースs がある場合に便利です。ロールを使用して、適切なワークスペースs にダッシュボード ユーザーs を追加し、関連付けられた権限をそれらに直接付与することができます。各権限については、[権限一覧](#list-of-permissions)を参照してください。

{% tabs ローカル %}
{% tab 役割例 %}
| ロール名| ワークスペース| 権限  
----------- | ----------- | ---------
| Marketer - Fashion Brands | {::nomarkdown}\[DEV] Fashion Brand, \[QA] Fashion Brand, \[PROD] Fashion Brand {:/} | “Access Campaigns, Canvases, Cards, Feature Flags, Segments, Media Library, and Preference Center"<br>「メディアライブラリアセットの管理」|
| マーケター- スキンケア・ブランド|{::nomarkdown}\[DEV meta id="2"/> スキンケア・ブランド、\[QA] スキンケア・ブランド、\[PROD] スキンケア・ブランド{:/}|"アクセス・キャンペーン、キャンバス、カード、機能フラグ、セグメント、メディア・ライブラリ、およびプリファレンス・センター" <br>「メディアライブラリアセットの管理」|
| ユーザー管理- すべてのブランド|{::nomarkdown}\[DEV meta id="2" /> ファッションブランド、\[QA meta id="3" /> ファッションブランド、\[PROD] ファッションブランド、\[DEV] スキンケアブランド、\[QA] スキンケアブランド、\[PROD] スキンケアブランド{:/} | "ダッシュボードユーザーの管理"<br>「チームの管理」|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% endtab %}
{% endtabs %}

## ユーザーの権限の編集

ユーザーの現在の [admin](#admin)、[company](#company)、または [ワークスペース](#workspace) 権限を変更するには、**設定**> **Company ユーザー s** に移動して名前を選択します。

!["Company ユーザー s"ページはBrazeで、結果に1つのユーザーがリストされています。]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %}){: style="max-width:80%;"}

### 管理者

管理者は、すべての機能および企業設定を変更する機能を使用できます。また、Brazeでは管理者しかできないこともいくつかあります。 

管理者のみが以下を実行できます。

- 変更 [ アプリ roval 設定 s]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)
- 他の[Braze ユーザーs]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users)を追加、編集、削除、一時停止、または一時停止解除する
- Braze ユーザーs をCSV としてエクスポート

管理者権限を付与または削除するには、**このユーザーは管理者**を選択し、**アップデートユーザー**を選択します。

![focus.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %})のadminチェックボックスで選択したユーザーの内容{: style="max-width:40%;"}

{% alert warning %}
ユーザーから管理者権限を削除すると、少なくとも1 つの[company-level](#company) または[ワークスペース-level](#workspace) 権限を割り当てるまで、Brazeにアクセスできなくなります。
{% endalert %}

### 会社

ユーザーの次の会社レベルの権限を管理するには、その権限の横にあるチェックボックスをオンまたはオフにします。終了したら、**ユーザーをアップデート**を選択します。

|許可名|説明|
|----------|-----------|
|企業設定の管理|ユーザー s が企業設定を変更できるようにします。|
|ワークスペースの作成と削除s|ユーザー s がワークスペースs を作成および削除できるようにします。|
{: .reset-td-br-1 .reset-td-br-2}

### workspace

Braze に属するワークスペースごとに、ユーザーにさまざまな権限を与えることができます。ワークスペースレベルの権限を管理するには、**ワークスペースと権限**を選択し、権限を手動で選択するか、以前に作成した権限セット[を割り当てます。

さまざまなワークスペースにユーザーのさまざまな権限を付与する必要がある場合は、必要に応じてこの処理を何度も繰り返します。各権限については、[権限一覧](#list-of-permissions)を参照してください。

{% tabs ローカル %}
{% tab 手動で選択する %}
**ワークスペース s** で、ドロップダウンから1 つ以上のワークスペースを選択します。次に、**Permissions** の下で、ドロップダウンから1 つ以上の権限を選択します。これらの権限は、選択したワークスペースにのみ割り当てられます。必要に応じて、このワークスペースの完全な権限を付与する場合は、**Enable Admin Access** を選択できます。

終了したら、**ユーザーをアップデート**を選択します。

![Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})で手動で選択されているワークスペースレベルの権限
{% endtab %}

{% tab 許可セットを割り当てる %}
**ワークスペース s** で、ドロップダウンから1 つ以上のワークスペースを選択します。次に、**Permission Sets**の下で、1つの権限セットを選択します。これらの権限は、選択したワークスペースにのみ割り当てられます。

終了したら、**ユーザーをアップデート**を選択します。

![Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})の権限セットを使用して割り当てられるワークスペースレベルの権限
{% endtab %}
{% endtabs %}

## ユーザー権限のエクスポート

ユーザーとその権限の読み込む一覧を表示するには、**Settings**> **Company ユーザー s**に移動し、**エクスポートユーザーs**を選択します。すぐにCSVファイルがあなたのメールの住所に送られます。

![The "Company Users" page in Braze with the "Export Users" option in focus.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## 権限のリスト

{% alert important %}
2024年4月現在、プロモーションコード一覧を作成または更新するには、Braze ユーザーに「アクセスキャンペーン、キャンバス、カード、セグメント、メディアライブラリ」権限が必要です。
{% endalert %}

|レベル|名前|定義|
|---|---|---|
|管理者|管理者|ユーザーが利用可能なすべての機能を利用できるようにします。これはすべての新規ユーザーのデフォルト設定です。企業設定s(企業名とタイムゾーン)を更新できます。これは、制限されたユーザーsではできません。|
|会社|ワークスペースの作成と削除s|ユーザー s がワークスペースs を作成および削除できるようにします。|
|会社|企業設定の管理|ユーザー s が企業設定を変更できるようにします。|
|workspace|キャンペーン、キャンバス、カード、コンテンツブロック、機能フラグ、セグメント、メディアライブラリ、ロケーション、プロモーションコード、および環境設定センターへのアクセス|キャンペーンとキャンバスのパフォーマンスメトリクスの表示、キャンペーンとキャンバスのドラフトの作成と複製、キャンペーンとキャンバスドラフトとテンプレートの編集、ニュースフィードのドラフトの表示、Segments、テンプレートs、メディアの作成、テンプレートs、アップロードメディアの作成、プロモーションコードリストの作成または更新、エンゲージメント レポートs の表示、ダッシュボードでのグローバルメッセージ設定s の付与ができます。ただし、この権限を持つユーザー s では、既存のライブコンテンツを一時停止または変更することはできません。|
|workspace|Dev Console へのアクセス|次の設定s およびログへのフルアクセスを許可します。{::nomarkdown}<ul><li><a href='/docs/user_guide/administrative/app_settings/api_settings_tab/'>API キー</a></li><li><a href='/docs/user_guide/administrative/app_settings/internal_groups_tab/'>内部グループ</a></li><li><a href='/docs/user_guide/administrative/app_settings/message_activity_log_tab/'>メッセージアクティビティログ</a></li><li><a href='/docs/user_guide/administrative/app_settings/event_user_log_tab/'>イベントユーザーログ</a></li><li><a href='/docs/user_guide/data_and_analytics/cloud_ingestion/'>クラウドデータ取り込みの管理</a></li></ul>{:/}|
|workspace|キャンペーンの承認と拒否|ユーザーsがキャンペーンsをアプリローブまたは拒否できるようにします。この権限を適用するには、[キャンペーンの承認ワークフロー]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval)を有効にする必要があります。この設定は現在早期アクセス段階です。早いアクセスに参加したい場合は、アカウントマネージャーに連絡してください。|
|workspace|キャンバスの承認と拒否|ユーザー s がキャンバスをアプリまたは拒否できるようにします。この権限 アプリでは、[ Canvases]({{site.baseurl}}/canvas_approval) のアプリ 認証ワークフローを有効にする必要があります。|
|workspace|エディットCurrents統合|ユーザー s が認証情報 s を含むCurrentsコネクションを変更できるようにします。デフォルトでは、ユーザーは"External Integrations"権限もこの権限を割り当てられます。|
|workspace|セグメントの編集|ユーザーs がSegments を作成および変更できるようにします。この権限がなくても、既存のセグメントとフィルターを使用してキャンペーンを作成できます。この権限は、CSV 内のユーザーs からSegmentを生成するか、CSV 内のユーザーs のグループをリターゲティングするする必要があります。|
|workspace|ユーザーデータのエクスポート|ユーザーs がSegments、キャンペーンs、およびキャンバスからユーザーデータをエクスポートできるようにします。|
|workspace|ユーザーデータのインポートと更新|ユーザー s は、ユーザーインポートページを表示するだけでなく、CSV および更新のアプリ ユーザー s を読み込むことができます。これにより、ユーザーのサブスクリプション ステータスとサブスクリプショングループのオプトイン/オプトアウト規則を変更することもできます。|
|workspace|コンテンツブロックの起動|ユーザーs が[Content Blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/) を起動できるようにします。|
|workspace|環境設定センターの起動|ユーザー s が[ユーザー設定センター s]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/) を起動できるようにします。|
|workspace|アプリの管理|ユーザーsが**アプリ設定**を変更できるようにします。|
|workspace|カタログの管理ダッシュボード権限|ユーザーs がカタログs を作成および管理できるようにします。|
|workspace|ダッシュボードユーザーの管理|ユーザー s が**Company ユーザー s** ページを表示、編集、管理できるようにします。この権限を持つユーザーは、自分を含むすべてのユーザーの権限を変更できます。そのため、この権限は管理者アクセスレベルと見なす必要があります。ユーザーを削除できるのは管理者だけなので、この権限ではユーザーを削除できません。|
|workspace|メール設定の管理|ユーザー s がメール設定変更を保存できるようにします(**設定** > **メール設定**)。|
|workspace|イベント、属性、購入の管理|ユーザーsがカスタム属性sを編集できるようにします(この機能を持たないユーザーsは、カスタム属性sを引き続き表示できます)。また、カスタムイベントsのプロパティーを編集および表示したり、**データ設定**でプロダクトのプロパティーを編集および表示したりできます。|
|workspace|外部統合の管理|**Technology Partners**のすべてのタブにアクセスし、Brazeを他のプラットフォームと同期する機能を許可します。|
|workspace|機能フラグの管理|ユーザーsが[フィーチャーフラグs]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/about/)を作成または変更できるようにします。|
|workspace|メディアライブラリアセットの管理|ユーザー s で、用紙ライブラリーアセットを追加、編集、および削除できます。|
|workspace|サブスクリプショングループの管理|ユーザーs がサブスクリプショングループs を作成および管理できるようにします。|
|workspace|タグの管理|ユーザーsがタグs(**タグマネジメント**)を変更または削除できるようにします。この権限では、キャンペーンsまたはSegmentsにタグsを追加する必要はありません。|
|workspace|チームの管理|ユーザー s が**内部チーム** を管理できるようにします。この権限を選択できるかどうかは、Braze との契約によって異なります。|
|workspace|変換の管理|ユーザーがデータトランスフォーメーションを作成および管理できるようにします。|
|workspace|カードの発行|この権限は、非推奨になっているニュースフィードでアカウントが有効になっている場合にのみ表示されます。これはコンテンツカードに影響しません。ニュースフィードカードの作成と編集をユーザーに許可します。この権限がなくても、ニュースフィードカードを閲覧できます。アカウントでニュースフィードが有効になっており、ユーザーが既存のコンテンツブロックを起動できる必要がある場合は、"Publish Cards"および"Launch Content Blocks"権限の両方が必要です。|
|workspace|キャンペーン、キャンバスの送信|ユーザーs で、キャンペーンとキャンバスの編集、アーカイブ、および停止、キャンペーンの作成、キャンバスの起動ができます。|
|workspace|請求詳細の表示|ユーザー s がサブスクリプションと請求を表示できるようにします。|
|workspace|Currentsインテグレーションの表示|ユーザー s は、認証情報 s を除く、Currentsコネクションに関するすべての情報を表示できます。デフォルトでは、ユーザーは"Access Campaigns、Canvases、Cards、Content Blocks、Feature Flags、Segments、Media Library、Locations、Promotion Codes、Preference Centers"権限も割り当てられます。|
|workspace|PII としてマークされたカスタム属性の表示|このユーザーは、管理者ではなくPIIとしてマークされたカスタム属性を表示できます。|
|workspace|PIIの表示|ユーザー s は、ダッシュボード内の企業によって定義された個人識別可能な情報フィールドs を表示できます。|
|workspace|PII 準拠のユーザープロファイル表示|ユーザーs はユーザープロファイルs を表示できますが、会社が個人識別情報(PII)として定義したフィールドを赤く処理します。|
|workspace|変形の表示|ユーザー s が[Brazeデータトランスフォーメーションを表示できるようにします]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/overview/)。|
|workspace|使用状況データの表示|ユーザー s がチャネル パフォーマンス ダッシュボードs を含むアプリの使用状況を表示できるようにします。|
|workspace|重複するユーザーのマージ|ユーザーs が重複するユーザープロファイルs をマージできるようにします。|
|workspace|重複ユーザーのプレビュー|ユーザーs が重複するユーザープロファイルをプレビューできるようにします。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
