---
nav_title: アンペア
article_title: アンペア
alias: /partners/amperity/
description: "この参考記事では、Brazeと包括的な企業顧客データプラットフォームであるAmperityのパートナーシップについて概説しており、Amperityユーザーの同期、データの統一、AWS S3バケットを使用したBrazeへのデータ送信などを可能にしている。"
page_type: partner
search_tag: Partner

---

# アンペア

> [Amperity](https://amperity.com/) は、包括的な企業向け顧客データプラットフォームであり、ブランドが顧客を理解し、戦略的な意思決定を行い、消費者により良いサービスを提供するために常に適切な措置を取れるよう支援します。Amperity は、データ管理の統合、分析、インサイト、およびアクティベーションにおけるインテリジェントな機能を提供します。

_この統合は Amperity によって管理されます。_

{% multi_lang_include video.html id="06G0lxaSjgk" align="right" %}

Braze と Amperity の統合により、2つのプラットフォームにわたる顧客の統合ビューが提供されます。この統合により、以下のことが可能になる：
- **顧客プロファイルを同期する**:ユーザーデータとカスタム属性をAmperityからBrazeにマッピングする。 
- **オーディエンスを作成、送信する**:アクティブな顧客とこれらの顧客に関連付けられているカスタム属性のリストを Braze に返すセグメントを作成して、Braze に送信します。
- **データの更新を管理する**:カスタム属性の更新をBrazeに送信する頻度を制御する。
- **データを統合する**:Amperityがサポートする様々なプラットフォームとBrazeでデータを統合する。
- **BrazeのデータをAmazon S3に同期する**：Braze Currentsを使用して、Brazeキャンペーンからのエンゲージメントデータを統合し、Apache AvroフォーマットでAmazon S3にデータを同期できる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Amperity アカウント | このパートナーシップを活用するには、[Amperity アカウント](https://amperity.com/request-a-demo)が必要です。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br> これは Braze ダッシュボードの [**開発者コンソール**] > [**REST API キー**] > [**新しい API キーを作成**] で作成できます。 |
| ブレイズインスタンス | Braze インスタンスは Braze オンボーディングマネージャーから入手できます。また、[API 概要ページ]({{site.baseurl}}/api/basics#endpoints)でも確認できます。 |
| Braze REST エンドポイント | あなたのBrazeエンドポイントURL。エンドポイントはBrazeインスタンスに依存する。 |
| Currents コネクター (オプション) | S3 Currents コネクター。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## データマッピング

標準属性とカスタム属性の両方を Amperity から Braze に送信できます。これにより、Amperity からさまざまなソースのデータを使用して、Braze の顧客プロファイルを強化できます。送信できる属性は、Amperity システムのデータと、Braze で設定した属性によって異なります。

これらの属性については、以下をお読みいただきたい。

### 標準属性 

[プロファイル属性]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)は、顧客が誰であるかを示します。これらは多くの場合、次のような顧客の身元情報に関連付けられています。
- 名前
- 生年月日
- メールアドレス
- 電話番号

### カスタム属性 

Braze の[カスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)は、ブランドが決定するフィールドです。Brazeにすでに存在するカスタム属性をAmperityで管理したい場合は、Amperityから送信される出力を、Brazeワークスペースにすでにある名前に合わせる。これには次のものが含まれます。
- 購入履歴
- ロイヤルティステータス
- 価値階層
- 最近のエンゲージメント・データ

AmperityからBrazeに送信されるカスタム属性の名前を確認する。Amperityは、一致する名前がないときはいつでもカスタム属性を追加する。

Braze 内で一致する `external_id` または`braze_id` を持つユーザーのカスタム属性のみが更新されます。

### Amperity オーディエンス

AmperityからBrazeに同期されたオーディエンスは、カスタム属性としてユーザープロファイルに記録される。これらは、Brazeでそれらのユーザーをターゲットにするために使用できる。

![カスタムデータカテゴリに表示されるカスタム属性を持つフィルタのドロップダウンリスト。]({% image_buster /assets/img/amperity/custom_attributes_filters.png %}){: style="max-width:60%;"}

![l12m_frequency" や "l12m_monetary" などのカスタム属性のドロップダウンリスト。]({% image_buster /assets/img/amperity/search_custom_attributes_filters.png %}){: style="max-width:40%;"}

### データ型

サポートされているデータタイプは以下の通りである：
- ブール値
- 日付
- 日時
- 小数
- フロート
- 整数
- String
- 可変長文字列

使用されるデータ型は属性の性質によって異なる。たとえば、メールアドレスは文字列で、顧客の年齢は整数です。

### 属性の重複

デフォルトのユーザープロファイルフィールドと重複するカスタム属性の送信は避ける。たとえば誕生日は、Braze 標準属性項目と一致させるため、「dob」という名前のユーザープロファイルフィールドとして Braze に送信する必要があります。birthday"、"Birthdate"、またはその他の文字列として送信された場合、カスタム属性が作成され、"dob "フィールドの値は更新されない。

### データポイント

Amperity は、Braze との同期間に行われた変更と、送信のステータスを追跡します。Amperityは、前回の同期以降に変更されたリストメンバーシップとその他の選択された属性のみをBrazeに送信する。  

## 統合

### ステップ1:Brazeの設定の詳細をキャプチャする

1. [**User Data**] で、`users.track` 権限を持つ Braze ワークスペースの Braze REST APIキーを作成します。`users.track` エンドポイントは、Amperity オーディエンスをカスタム属性として Braze に同期します。
2. Brazeインスタンスの[REST APIエンドポイントを]({{site.baseurl}}/api/basics#endpoints)決定する。例えば、BrazeのURLが`https://dashboard-03.braze.com` 、REST APIのエンドポイントが`https://rest.iad-03.braze.com` 、インスタンスが "US-03 "の場合。
3. Amperity から Braze に送信できる一連の[ユーザープロファイルフィールド]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)と[カスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)を決定します。

### ステップ2:Braze を宛先として設定する - DataGrid オペレーター

#### ステップ 2a: 顧客プロファイルテーブルを作成する

Amperity の Customer 360 データベース内に、「Braze Customer Attributes」という名前の新しいテーブルを作成します。このテーブルには、ブランドが Amperity で管理するすべての Braze 属性が含まれている必要があります。これには、Braze が必要とするデフォルトのユーザープロファイルフィールドとカスタム属性の両方が含まれます。[Amperity ドキュメント](https://docs.amperity.com/datagrid/destination_braze.html#customer-profiles-table)に示されているように、SQL を使用してこのテーブルの構造を定義します。

#### ステップ 2b: テーブルに名前を付け、検証し、保存する

テーブル名を "Braze Customer Attributes "とし、保存する。テーブルが**セグメントエディター**およびキャンペーン内の**属性編集**エディターにアクセス可能であることを確認する。

#### ステップ 2c: Braze を宛先として追加する

Amperity プラットフォームで [**Destinations**] タブに移動します。新しい目的地を追加するオプションを探す。利用可能なオプションから [**Braze**] を選択します。

![名前が「Braze API」、説明が「Send audience attributes to Braze」、プラグインが「Braze」である「New Destination」セクション。]({% image_buster /assets/img/amperity/destination_name.png %}){: style="max-width:60%;"}

#### ステップ 2d: 宛先の詳細を設定する

[Amperityのドキュメント](https://docs.amperity.com/datagrid/destination_braze.html#add-destination)に示されているように、[**Braze settings**] で Braze の認証情報と宛先設定を指定します。最後のステップで収集した構成の詳細を入力し、Braze識別子を定義する。マッチング可能な識別子は以下の通りである：
- `braze_id`:自動的に割り当てられるBrazeの識別子で、Brazeで作成されたときに特定のユーザーに関連付けられ、変更できない。
- `external_id`:顧客が割り当てた識別子で、通常はUUIDである。 

![インスタンスが「US-03」、ユーザー ID が「external_id」、セグメント名が空白、S3 バケットが「amperity-training-abc123」、S3 フォルダーが「braze-attributes」である「Braze Settings」セクション。]({% image_buster /assets/img/amperity/braze_settings.png %}){: style="max-width:60%;"}

#### ステップ2e:データ・テンプレートを追加する

[**Destinations**] タブで Braze 宛先のメニューを開き、[**Add data template**] を選択します。テンプレートの名前と説明（例えば、"Braze "と "Send custom attributes to Braze"）を入力し、ビジネスユーザーのアクセスを確認し、すべての構成設定をチェックする。 

必要な設定がデスティネーションの一部として構成されていない場合は、データテンプレートの一部として構成する。データ・テンプレートを保存する。

![名前が「Braze Audience Attributes」で説明が「Send audience attributes to Braze」である「Data Template Name」セクション。]({% image_buster /assets/img/amperity/data_template_name.png %}){: style="max-width:60%;"}

#### ステップ2f:設定を保存する 

必要な情報を入力したら、この設定を保存します。Braze が宛先として設定されたので、Amp360 と AmpIQ のユーザーはデータを Braze に同期できます。

### ステップ3:データをBrazeに同期させる

AmperityのテナントでBrazeが有効になっていることを確認する。有効になっていない場合は、DataGrid オペレーターまたは Amperity の担当者に支援を依頼してください。

次に、該当する Amp360 または AmpIQ の同期手順に従います。

#### 同期オプション 1：Amp360経由でBrazeにクエリー結果を送信する

Amp360のユーザーは、SQLを使って自由形式のクエリーを書き、その結果をBrazeに送信するスケジュールを設定することができる。

##### ステップ1:Amperityでクエリーを作成する

Amperityのクエリー機能に移動し、目的の顧客データセットを得るためのSQLクエリーを構築する。その結果には、Brazeに送りたい特定の属性が含まれているはずだ。購入履歴を持つユーザーのリストを返すAmperityクエリーの例を参照のこと。

##### ステップ2:Amperityに新しいオーケストレーションを追加する

1. **Orchestration**セクションに行き、新しいオーケストレーションを追加するオプションをクリックする。 
2. オーケストレーションが何をすべきかを指定する。これには通常、実行されるべきSQLクエリと、その結果の送信先を指定することが含まれる。この場合、アクティブな顧客のリストを生成するために作成したSQLクエリーを選択し、結果の送信先としてBrazeを指定する。
3. オーケストレーションをいつ、どのくらいの頻度で実行するかを定義する。たとえば、毎日特定の時間にオーケストレーションを実行できます。
4. オーケストレーションを好みに設定したら保存する。Amperityのオーケストレーションリストに追加される。
5. オーケストレーションをテストして、期待通りに動作することを確認する。手動でオーケストレーションをトリガーし、Brazeで結果をチェックすることでこれを行うことができる。

##### ステップ3:オーケストレーションを実行する 

オーケストレーションを実行してクエリを実行し、結果をBrazeに送信する。これは手動で行うことも、オーケストレーション設定で設定したスケジュールで行うこともできます。

#### 同期オプション 2：AmpIQ を介して Braze にオーディエンスを送信する

AmpIQユーザーは、SQL以外のインターフェイスを使ってAmperityでセグメントを作成し、Brazeのような下流のデスティネーションに同期させることができる。ユーザーは宛先を選択し、各宛先に送信する属性のリストを設定できます。

##### ステップ1:Amperityでセグメントを作成する 

Amperityで顧客のリストを返すセグメントを作成する。このセグメントは、Braze で更新するカスタム属性に関連付けられている必要があります。

{% alert note %}
Amperity のドキュメントで、Braze に送信できるさまざまなセグメントタイプの例を確認してください。
{% endalert %}

##### ステップ2:Amperityでキャンペーンを構築する

1. **キャンペーン・**セクションに行き、新しいキャンペーンを作成するオプションをクリックする。
2. 特に複数のキャンペーンを行っている場合は、後でキャンペーンを識別するのに役立つ、説明的でユニークな名前を付ける。
3. このキャンペーンでターゲットにする顧客のセグメントを選択します。これは先ほど作成したセグメントです。<br>![ターゲティングから除外するセグメントのドロップダウンフィールド。]({% image_buster /assets/img/amperity/select_segments.png %}){: style="max-width:50%;"}<br><br>
4. キャンペーンの一部として送信したいデータを選択する。これにはさまざまな顧客属性が含まれる可能性があります。![「Edit Campaign Attributes」モーダルでは、宛先とカスタマー属性を選択できる。]({% image_buster /assets/img/amperity/edit_campaign_attributes.png %}){: style="max-width:90%;"}<br><br>
5. キャンペーンデータの送信先として [**Braze**] を選択します。
6. いつ、どれくらいの頻度でキャンペーンを実施するかを選択する。これは1回限りのイベントでも、定期的なスケジュールでも構わない。
7. キャンペーンを保存してテストを実行し、期待通りに機能することを確認する。

##### ステップ3:キャンペーンを実施する

Brazeにセグメントを送信するためにキャンペーンを実行する。これは手動で行うことも、キャンペーン設定で設定したスケジュールに基づいて行うこともできる。


### Amperity と Braze Currents を組み合わせて使用する
Braze CurrentsのデータをAmperityに送信する：
1. Amazon S3バケットにデータを送信するために[Braze Currentをセットアップ]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents/)する。
2. [そのAmazon S3バケットからApache Avroファイルを読み込む](https://docs.amperity.com/datagrid/source_amazon_s3.html)ようにAmperityを設定する。
3. フィードを設定し、標準的なワークフローを使用してデータロードを自動化する。


