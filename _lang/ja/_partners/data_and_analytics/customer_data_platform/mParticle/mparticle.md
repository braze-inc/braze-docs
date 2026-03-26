---
nav_title: mParticle by Rokt
article_title: mParticle by Rokt
alias: /partners/mparticle/
description: "このリファレンス記事では、Braze と mParticle のパートナーシップについて説明します。mParticle は、マーケティングスタックのソース間で情報を収集してルーティングする顧客データプラットフォームです。"
page_type: partner
search_tag: Partner

---

# mParticle by Rokt

{% multi_lang_include video.html id="Njhqwd36gZM" align="right" %}

> mParticle の顧客データプラットフォームは、データの有効活用を支援します。熟練したマーケターは、mParticle でグローススタック全体のデータのオーケストレーションを行い、カスタマージャーニーの重要なタイミングで適切なアクションを取ることができます。

Braze と mParticle の統合により、2つのシステム間の情報の流れをシームレスにコントロールできます。
- Braze キャンペーンとキャンバスのセグメンテーションのために、mParticle のオーディエンスを Braze に同期する。
- 2つのプラットフォーム間でデータを共有する。これは mParticle キット統合とサーバー間統合によって実現できます。
- [Currents を介して Braze ユーザーインタラクションを mParticle に送信し]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents/)、グローススタック全体でアクションに活用する。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| mParticle アカウント | このパートナーシップを利用するには、[mParticle アカウント](https://app.mparticle.com/login)が必要です。 |
| Brazeインスタンス | Brazeインスタンスは [API 概要ページ]({{site.baseurl}}/api/basics/#endpoints)で確認できます（`US-01`、`US-02` など）。 |
| Braze アプリ識別子キー | アプリ識別子キー。<br><br>これは、Braze ダッシュボードの**Manage Settings** > **API Key** で確認できます。 |
| ワークスペース REST API キー | （サーバー間）Braze REST API キー<br><br>これは、Braze ダッシュボードの **Developer Console** > **API Settings** > **API Key** で作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### オーディエンス

Braze と mParticle のパートナーシップを利用して統合を構成し、mParticle のオーディエンスを直接 Braze にインポートしてリターゲティングを行い、1つのシステムから別のシステムへのデータの完全なループを作成します。 

設定した統合はすべてデータポイントを記録します。Braze データポイントの詳細についてご質問があれば、Braze アカウントマネージャーがお答えします。

#### オーディエンスの転送

mParticle は、コホートメンバーシップ属性を設定するための3つの方法を提供しており、「[Send Segments As](#send_settings)」構成設定によって制御されます。各オプションの処理については、次のセクションを参照してください。

- [単一文字列属性](#string)
- [単一配列属性](#array)
- [セグメントごとに1つの属性](#per-segment)
- [単一配列属性と単一文字列属性の両方](#both-1)
- [単一配列属性とセグメントごとに1つの属性の両方](#both-2)
- [単一文字列属性とセグメントごとに1つの属性の両方](#both-3)
- [単一配列属性、単一文字列属性、およびセグメントごとに1つの属性](#multi)

##### 単一文字列属性 {#string}

mParticle は、`SegmentMembership` という単一のカスタム属性を作成します。この属性の値は、ユーザーに一致するカンマ区切りの mParticle オーディエンス ID の文字列です。これらのオーディエンス ID は、mParticle ダッシュボードの **Audiences** で確認できます。

例えば、mParticle のオーディエンス「Ibiza dreamers」のオーディエンス ID が「11036」の場合、フィルター `SegmentMembership` — `matches regex` — `11036` でこれらのユーザーをセグメント化できます。

これは mParticle のデフォルトオプションですが、ほとんどのユーザーは Braze でセグメントを作成する際のフィルタリング体験のために[単一配列属性](#array)を使用することを選択します。

{% alert important %}
この方法は、オーディエンスが数個よりも多い場合にはお勧めできません。カスタム属性の最大文字数は255文字であるため、この方法では数十または数百のオーディエンスを1つのユーザープロファイルに保存することはできません。ユーザーごとに多くのコホートがある場合は、「セグメントごとに1つの属性」の構成を強くお勧めします。
{% endalert %}

![mParticle セグメントのメンバーシップ]({% image_buster /assets/img_archive/mparticle1.png %})

##### 単一配列属性 {#array}

mParticle は、各ユーザーに対して Braze に `SegmentMembershipArray` という単一のカスタム配列属性を作成します。この属性の値は、ユーザーに一致する mParticle オーディエンス ID の配列です。

たとえば、ユーザーが「13053」、「13052」、および「13051」というオーディエンス ID を持つ3つの mParticle オーディエンスのメンバーである場合、フィルター `SegmentMembershipArray` — `includes value` — `13051` でそれらのオーディエンスの1つに一致するユーザーをセグメント化できます。

{% alert note %}
Braze 配列属性の最大長は25です。ユーザーがメンバーとなっているオーディエンスが25を超える場合、Braze によってメンバーシップ情報が切り捨てられます。これを回避するには、Braze の担当者に連絡して、最大配列長のしきい値を増やしてください。
{% endalert %}

##### セグメントごとに1つの属性 {#per-segment}

mParticle は、ユーザーが属する各オーディエンスに対してブール値のカスタム属性を作成します。たとえば、「Possible Parisians」という mParticle オーディエンスの場合、フィルター `In Possible Parisians` - `equals` - `true` でこれらのユーザーをセグメント化できます。

![mParticle カスタム属性]({% image_buster /assets/img_archive/mparticle2.png %})

##### 単一配列属性と単一文字列属性の両方 {#both-1}

mParticle は、単一配列属性と単一文字列属性の両方で説明されているとおりに属性を送信します。

##### 単一配列属性とセグメントごとに1つの属性の両方 {#both-2}

mParticle は、単一配列属性とセグメントごとに1つの属性の両方で説明されているとおりに属性を送信します。

##### 単一文字列属性とセグメントごとに1つの属性の両方 {#both-3}

mParticle は、単一文字列属性とセグメントごとに1つの属性の両方で説明されているとおりに属性を送信します。

##### 単一配列属性、単一文字列属性、およびセグメントごとに1つの属性 {#multi}

mParticle は、単一配列属性、単一文字列属性、およびセグメントごとに1つの属性で説明されているとおりに属性を送信します。

#### ステップ 1:mParticle でオーディエンスを作成する {#send_settings}

mParticle でオーディエンスを作成するには:

1. **Audiences** > **Single Workspace** > **+ New Audience** に移動します。
2. オーディエンスの出力先として Braze を接続するには、次のフィールドを指定する必要があります:

| フィールド名               | 説明                                                                                                                                                                   |
| ------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API キー                  | Braze ダッシュボードの **Settings** > **API Keys** にあります。<br><br>古いナビゲーションを使用している場合は、**Developer Console** > **API Settings** で API キーを確認できます。 |
| API キー オペレーティングシステム | Braze API キーに対応するオペレーティングシステムを選択します。この選択により、オーディエンス更新時に転送されるプッシュトークンの種類が制限されます。                          |
| セグメントとして送信         | Braze にオーディエンスを送信する方法です。詳細については、[オーディエンスの転送](#forwarding-audiences)セクションを参照してください。                                                          |
| ワークスペース REST API キー   | すべての権限を持つ Braze REST API キーです。これは Braze ダッシュボードの **Settings** > **API Keys** から作成できます。                                                        |
| External identity type   | external ID として Braze に転送する mParticle のユーザー ID タイプです。デフォルト値の Customer ID のままにすることをお勧めします。                                          |
| Email identity type      | メールとして Braze に転送する mParticle のユーザー ID タイプです。                                                                                                            |
| Brazeインスタンス           | Braze データを転送するクラスターを指定します。                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="3"}
3. 最後にオーディエンスを **Save** します。

数分以内にオーディエンスが Braze に同期され始めます。オーディエンスのメンバーシップは、`external_ids` が設定されているユーザー（つまり匿名ユーザーではないユーザー）に対してのみ更新されます。Braze mParticle オーディエンスの作成の詳細については、mParticle の[構成設定](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings)に関するドキュメントを参照してください。

#### ステップ 2:Braze でユーザーをセグメント化する

Braze でこれらのユーザーのセグメントを作成するには、**Engagement** の下の **Segments** に移動し、セグメントに名前を付けます。以下は、**Send segments as** で選択したオプションに応じた2つのセグメントの例です。各オプションの詳細については、[オーディエンスの転送](#forwarding-audiences)を参照してください。

- **単一配列属性:** `SegmentMembershipArray` をフィルターとして選択します。次に、「includes value」オプションを使用して目的のオーディエンス ID を入力します。![「includes value」とオーディエンス ID が設定されている mParticle セグメントフィルター「SegmentMembershipArray」。]({% image_buster /assets/img_archive/mparticle5.png %})<br><br>
- **セグメントごとに1つの属性:** カスタム属性をフィルターとして選択します。次に、「equals」オプションを使用し、適切なロジックを選択します。![mParticle セグメントフィルター「in possible parisians」を「equals」と「true」に設定。]({% image_buster /assets/img_archive/mparticle3.png %})

保存すると、キャンバスやキャンペーンの作成時にターゲットユーザーのステップでこのセグメントを参照できます。

#### 接続の無効化と削除

mParticle は Braze で直接セグメントを管理しないため、対応する mParticle オーディエンス接続が削除または無効化されても、セグメントは削除されません。この場合、mParticle は各ユーザーからオーディエンスを除去するために Braze のオーディエンスユーザー属性を更新しません。

削除前に Braze ユーザーからオーディエンスを除去するには、オーディエンスフィルターを調整してオーディエンスのサイズを強制的に0にしてから、オーディエンスを削除します。オーディエンスの計算が完了して0人のユーザーが返された後に、オーディエンスを削除します。その後、オーディエンスメンバーシップが Braze で更新され、単一属性オプションの場合は `false` に、配列形式の場合はオーディエンス ID が削除されます。

## データマッピング

データは、mParticle を介してモバイルおよび Web アプリを Braze に接続したい場合、[埋め込みキット統合](#embedded-kit-integration)を使用して Braze にマッピングできます。また、[サーバー間 API 統合](#server-api-integration)を使用して、サーバー側のデータを Braze に転送することもできます。

どのアプローチを選択する場合でも、Braze を出力として設定する必要があります。

### Braze の出力設定を構成する

mParticle で、**Setup > Outputs > Add Outputs** と進み、**Braze** を選択して Braze キット設定を開きます。完了したら **Save** します。

| 設定名 | 説明 |
| ------------ | ----------- |
| Braze アプリ識別子キー | Braze アプリ識別子キーは、Braze ダッシュボードの **Settings** > **API Keys** で確認できます。API キーは各プラットフォーム（iOS、Android、Web）で異なることに注意してください。 |
| External identity type | external ID として Braze に転送する mParticle のユーザー ID タイプです。デフォルト値の Customer ID のままにすることをお勧めします。 |
| Email identity type | メールとして Braze に転送する mParticle のユーザー ID タイプです。デフォルト値の Email のままにすることをお勧めします。 |
| Brazeインスタンス | Braze データが転送されるクラスターです。ダッシュボードがあるクラスターと同じである必要があります。 |
| イベントストリーム転送を有効にする | （サーバー間）有効にすると、すべてのイベントがリアルタイムで転送されます。無効の場合、すべてのイベントが一括で転送されます。イベントストリーム転送を有効にする場合、Braze に渡すデータが[レート制限]({{site.baseurl}}/api/api_limits/)を遵守することを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img_archive/configure_settings.png %})

### 埋め込みキット統合

mParticle と Braze の SDK は、埋め込みキット統合を通じてアプリケーション上に存在します。ただし、直接の Braze 統合とは異なり、mParticle が Braze SDK のメソッドのほとんどの呼び出しを処理します。ユーザーデータのトラッキングに使用する mParticle メソッドは、Braze SDK メソッドに自動的にマッピングされます。 

mParticle の [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy)、[iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy)、[Web](https://github.com/mparticle-integrations/mparticle-javascript-integration-braze) 用 SDK のこれらのマッピングはオープンソースであり、[mParticle の GitHub ページ](https://github.com/mparticle-integrations)で確認できます。 

埋め込みキット SDK 統合により、Braze のフルスイート機能（プッシュ、アプリ内メッセージ、および関連するすべてのメッセージ分析トラッキング）を利用できます。

{% alert note %}
コンテンツカードとカスタムアプリ内メッセージの統合には、Braze SDK メソッドを直接呼び出してください。
{% endalert %}

#### ステップ 1:mParticle SDK を統合する

プラットフォームのニーズに基づいて、適切な mParticle SDK をアプリに統合します。

* [mParticle for Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle for iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle for Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### ステップ 2:mParticle の Braze イベントキット統合を完了する

この mParticle 統合のために Braze SDK を Web サイトやアプリに直接含める必要はありませんが、アプリから Braze にデータを転送するために次の mParticle Appboy Kit をインストールする必要があります。

mParticle の [Braze イベントキット統合ガイド](https://docs.mparticle.com/integrations/braze/event/#kit-integration)では、メッセージングのニーズ（プッシュ、位置情報の追跡など）に基づくカスタムの mParticle および Braze 調整手順を説明しています。

#### ステップ 3:Braze 出力の接続設定

mParticle で、**Connections** > **Connect** > **[希望のプラットフォーム]** > **Connect Output** に移動し、出力として Braze を追加します。次に、**Save** を選択します。

![]({% image_buster /assets/img_archive/mParticle_event_config.png %})

すべての接続設定がすべてのプラットフォームおよび統合タイプに適用されるわけではありません。接続設定とそれらが適用されるプラットフォームの内訳については、[mParticle のドキュメント](https://docs.mparticle.com/integrations/braze/event/#connection-settings)を参照してください。

### サーバー API 統合

mParticle のサーバーサイド SDK（例: Ruby、Python など）を使用している場合に、バックエンドデータを Braze にルーティングするためのアドオンです。Braze でこのサーバー間統合を設定するには、[mParticle のドキュメント](https://docs.mparticle.com/guides/platform-guide/connections/)の説明に従ってください。

{% alert important %}
サーバー間統合では、アプリ内メッセージ、コンテンツカード、プッシュ通知などの Braze UI 機能はサポートされません。また、デバイスレベルのフィールドなど、自動的にキャプチャされるデータもこの方法では利用できません。 

これらの機能を使用したい場合は、並列統合を検討してください。

サーバー側のデータを Braze に転送するには、`external_id` を含める必要があります。匿名ユーザーは転送されません。
{% endalert %}

#### Braze 出力の接続設定

mParticle で、**Connections > Connect > [希望のプラットフォーム] > Connect Output** に移動し、出力として Braze を追加します。完了したら **Save** します。 

![]({% image_buster /assets/img_archive/mParticle_connections.png %})

すべての接続設定がすべてのプラットフォームおよび統合タイプに適用されるわけではありません。接続設定とそれらが適用されるプラットフォームの内訳については、[mParticle のドキュメント](https://docs.mparticle.com/integrations/braze/event/#connection-settings)を参照してください。

「Enriched User Attributes」または「Enriched User Identities」を有効にする前に、これらの設定がデータポイント使用量にどのように影響するかを把握するために[データポイント超過](#potential-data-point-overages)を確認することをお勧めします。

### データマッピングの詳細

#### データタイプ
両方のプラットフォーム間ですべてのデータタイプがサポートされているわけではありません。
- [カスタムイベントプロパティ]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)は、文字列、数値、ブール値、または日付オブジェクトをサポートします。配列やネストされたオブジェクトはサポートされていません。
- [カスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)は、文字列、数値、ブール値、日付オブジェクト、配列をサポートしますが、オブジェクトやネストされたオブジェクトはサポートしません。 

{% alert note %}
Braze は `Time` タイプのカスタム属性で0年以前または3000年以降のタイムスタンプをサポートしていません。Braze は、これらの値が mParticle から送信されたときに取り込みますが、値は文字列として保存されます。
{% endalert %}

#### データマッピング

| mParticle データタイプ | Braze データタイプ | 説明 |
| ------------------- | --------------- | ----------- |
| ユーザー属性（予約済み） | 標準属性項目 | 例えば、mParticle の `$FirstName` 予約ユーザー属性キーは、Braze の `first_name` 標準属性項目フィールドにマッピングされます。 |
| ユーザー属性（その他） | カスタム属性 | mParticle に渡されたユーザー属性が、予約済みのユーザー属性キーの範囲外にある場合、そのユーザー属性はカスタム属性として Braze に記録されます。<br><br>ユーザー属性は文字列、数値、ブール値、日付、および配列をサポートしますが、オブジェクトやネストされたオブジェクトはサポートしません。 |
| カスタムイベント | カスタムイベント | mParticle カスタムイベントは Braze によってカスタムイベントとして認識されます。イベント属性はカスタムイベントプロパティとして転送されます。<br><br>イベントプロパティとして Braze に渡されるイベント属性は、文字列、数値、ブール値、または日付オブジェクトをサポートしますが、配列やネストされたオブジェクトはサポートしません。 |
| 購入コマースイベント | 購入イベント | 購入コマースイベントは Braze の購入イベントにマッピングされます。<br><br>バンドルコマースイベントデータの設定値を切り替えて、注文レベルまたは製品レベルで購入を記録します。たとえば `false` の場合、2つのユニークな製品、プロモーション、またはインプレッションを含む1つの受信イベントでは、少なくとも2つの送信 Braze イベントが生成されます。`true` に設定すると、ネストされた製品、プロモーション、またはインプレッションの配列を含む1つの送信イベントが生成されます。<br><br>ログに記録される追加のコマースフィールドの詳細については、[mParticle のドキュメント](https://docs.mparticle.com/integrations/braze/event/#purchase-events)を参照してください。<br><br>「バンドルコマースイベントデータ」を `false` に設定する場合、購入イベントプロパティとして Braze に渡される製品属性では、文字列、数値、ブール値、または日付オブジェクトがサポートされますが、配列やネストされたオブジェクトはサポートされません。|
| その他のすべてのコマースイベント | カスタムイベント | その他のすべてのコマースイベントはカスタムイベントにマッピングされます。<br><br>バンドルコマースイベントデータの設定値を切り替えて、注文レベルまたは製品レベルで購入を記録します。たとえば `false` の場合、2つのユニークな製品、プロモーション、またはインプレッションを含む1つの受信イベントでは、少なくとも2つの送信 Braze イベントが生成されます。`true` に設定すると、ネストされた製品、プロモーション、またはインプレッションの配列を含む1つの送信イベントが生成されます。<br><br>特定のデフォルトコマース値に加えて、製品属性が Braze イベントプロパティとして記録されます。ログに記録される追加のコマースフィールドの詳細については、[mParticle のドキュメント](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events)を参照してください。<br><br>「バンドルコマースイベントデータ」を `false` に設定する場合、イベントプロパティとして Braze に渡される製品属性では、文字列、数値、ブール値、または日付オブジェクトがサポートされますが、配列やネストされたオブジェクトはサポートされません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br_3 role="presentation" }

#### ユーザー ID マッピング
各 mParticle 出力について、`external_id` として Braze に送信する外部 ID タイプを選択できます。デフォルト値は顧客 ID ですが、`MPID` などの別の ID を Braze に `external_id` として送信するようにマッピングすることもできます。顧客 ID 以外の識別子を選択すると、Braze でのデータ送信方法に影響を与える可能性があることに注意してください。 

例えば、MPID を Braze の `external_id` にマッピングすると、次のような影響があります:
- MPID が割り当てられるタイミングの性質上、すべてのユーザーはセッション開始時に `external_id` が割り当てられます。
- MPID と `external_id` のデータタイプが異なるため、Currents の設定で追加のマッピングが必要になる場合があります。

### 消去リクエスト（データ主体リクエスト）の転送

Braze へ消去リクエストを転送するには、Braze へのデータ主体リクエスト出力を設定します。消去リクエストを Braze に転送するには、[mParticle のドキュメント](https://docs.mparticle.com/integrations/braze/forwarding-dsr/)の説明に従ってください。

## 潜在的なデータポイントの超過

### Enriched User Attributes

#### ユーザー属性/ID の Enrich を有効にする（サーバー間のみ） {#enriched}

mParticle 接続設定では、Braze は **Include Enriched User Attributes** をオフにすることを推奨します。有効にすると、mParticle は、既存のプロファイルから利用可能なすべてのユーザー属性（標準属性、カスタム属性、計算された属性など）を各ログイベントで Braze に転送します。これは、mParticle が毎回同じ変更されていない属性を Braze に送信するため、データポイントを大量に消費する結果となります。

例えば、ユーザーが最初のセッションで名、姓、電話番号を追加し、その後ニュースレターに登録して同じ情報とメールを追加した場合、ニュースレター登録イベントがトリガーされます:
- オンの場合（デフォルト）、5つのデータポイントが発生します（サインアップイベント、メールアドレス、名、姓、電話番号）。
- オフの場合、2つのデータポイントが発生します（サインアップイベントとメールアドレス）。

{% alert note %}
この設定をオフにしても、データの変更はチェックされません。ただし、元のインバウンドバッチで受信されなかったか、イベントの属性として明示的に設定されていないユーザープロファイル上のすべてのユーザー属性を統合が送信するのを防ぎます。差分のみが Braze に渡されることを確認することが重要です。
{% endalert %}

#### Enriched User Attributes をオフにする際の考慮事項

**Include Enriched User Attributes** をオフにする際に注意すべき点がいくつかあります:
1. サーバー間統合は mParticle イベント API を使用してイベントを Braze に送信します。各リクエストはイベントによってトリガーされます。メールアドレスの更新など、ユーザー属性が変更されても、特定のイベント（プロファイル更新カスタムイベントなど）に関連付けられていない場合、新しい値は、ユーザーによってトリガーされる次のイベントのペイロードで「enriched attribute」として Braze などの出力に渡されるだけです。**Include Enriched User Attributes** がオフになっている場合、特定のイベントに関連付けられていないこの新しい属性値は Braze に渡されません。
  - これを解決するために、更新された特定のユーザー属性のみを Braze に送信する別の「ユーザー属性更新」イベントを作成することをお勧めします。このアプローチでは、「ユーザー属性更新」イベントに対して追加のデータポイントを記録することになりますが、この機能を有効にしてすべての呼び出しですべてのユーザー属性を送信するよりもデータポイント使用量ははるかに少なくなります。
2. 計算された属性は enriched user attribute として Braze に渡されるため、「Enriched User Attributes」がオフになると、これらは Braze に渡されなくなります。「Enriched User Attributes」がオフの場合に計算された属性を Braze に転送するには、すべての属性をプッシュすることなく[計算された属性フィード](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed)を利用できます。計算された属性が変更されると、フィードが Braze にダウンストリームの更新を送信します。 

## トラブルシューティング

### Braze イベントキットを使用した iOS プッシュ通知のトラブルシューティング

iOS で Braze イベントキット（埋め込みキット統合）を使用しているときにプッシュ通知が機能しない場合は、以下を確認してください:
1. **プッシュトークンの転送:** mParticle がプッシュトークンを Braze に転送していることを確認します。mParticle ダッシュボードで、Braze キット接続でプッシュが有効になっていること、および Braze ダッシュボードで正しい Apple プッシュ認証情報が設定されていることを確認してください。
2. **キットの初期化順序:** Braze キットは、アプリがプッシュ権限を要求する前に初期化される必要があります。キットがアクティブになる前にプッシュ権限が要求された場合、プッシュトークンが Braze に転送されない可能性があります。mParticle SDK がアプリのライフサイクルの早い段階で開始されていることを確認してください。
3. **メソッドスウィズリング:** mParticle Apple キットは、メソッドスウィズリングを使用してプッシュトークンを自動的に転送し、プッシュ通知イベントを処理します。スウィズリングを無効にしている場合や、別の SDK が干渉している場合、プッシュトークンが Braze に届かない可能性があります。mParticle 設定でスウィズリングが有効になっていることを確認してください。
4. **手動トークン処理:** プッシュトークンを手動で管理している場合（例: `application:didRegisterForRemoteNotificationsWithDeviceToken:` を実装している場合）、プッシュ通知トークンプロパティに割り当てることでトークンを mParticle に渡していることを確認してください。例: `MParticle.sharedInstance().pushNotificationToken = deviceToken`。キットがそれを Braze に転送します。
5. **環境の不一致:** APN 認証情報の環境（開発 vs. 本番）がアプリのビルドと一致していることを確認してください。詳細については、[iOS プッシュのトラブルシューティング]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/ios/)を参照してください。

### Braze に不要または重複するデータを送信する
Braze は、値が変更されていない場合でも、属性が Braze に渡されるたびにデータポイントをカウントします。このため、Braze 内でアクションを実行するために必要なデータのみを転送し、属性の差分のみが渡されるようにすることをお勧めします。