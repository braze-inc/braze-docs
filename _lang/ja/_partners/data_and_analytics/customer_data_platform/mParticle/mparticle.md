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

> mParticle の顧客データプラットフォームは、データの有効活用を支援しています。熟練したマーケターは、mParticle で成長スタック全体のデータのオーケストレーションを行い、カスタマージャーニーの重要なタイミングで適切な行動を取ることができます。

BrazeとmParticleの統合により、2つのシステム間の情報の流れをシームレスにコントロールできます。
- Braze キャンペーンとキャンバスのセグメンテーションのために、mParticle のオーディエンスを Braze に同期する。
- 2つのプラットフォーム間でデータを共有する。これは mParticl eキット統合とサーバー間統合によって可能になります。
- [Currents を介して mParticle に Braze ユーザーインタラクションを送信し]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents/)、グローススタック全体で実行可能にする。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| mParticle アカウント | このパートナーシップを利用するには、[mParticleアカウント](https://app.mparticle.com/login)が必要です。 |
| Braze インスタンス | Braze インスタンスは[API 概要ページ]({{site.baseurl}}/api/basics/#endpoints)にあります (`US-01`、`US-02` など)。 |
| Brazeアプリ識別子キー | アプリ識別子キー。<br><br>これは、**Braze ダッシュボード > 設定の管理 > API キー**内にあります。 |
| ワークスペース REST APIキー | （サーバー間）Braze REST APIキー<br><br>これは、**Braze ダッシュボード > 開発者コンソール > API 設定 > API キー**内で作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### オーディエンス

BrazeとmParticleのパートナーシップを利用して、統合を構成し、mParticleのオーディエンスを直接Brazeにインポートしてリターゲティングを行い、1つのシステムから別のシステムへのデータの完全なループを作成します。設定するすべての統合は、アカウントのデータポイントボリュームの対象となります。

#### オーディエンスの転送

mParticleは、コホートメンバーシップ属性を設定するための3つの方法を提供しており、「[Send Segments As](#send_settings)」構成設定によって制御されます。次のセクションを参照して、各オプションの処理を行ってください。

- [単一文字列属性](#string)
- [シングル配列属性](#array)
- [セグメントごとに1つの属性](#per-segment)
- [単一の配列属性と単一の文字列属性の両方](#both-1)
- [単一の配列属性とセグメントごとの1つの属性の両方](#both-2)
- [単一文字列属性とセグメントごとの1つの属性の両方](#both-3)
- [単一の配列属性、単一の文字列属性、およびセグメントごとの1つの属性](#multi)

##### 単一文字列属性 {#string}

mParticleは、`SegmentMembership`という単一のカスタム属性を作成します。この属性の値は、ユーザーに一致するカンマ区切りのmParticleオーディエンスIDの文字列です。これらのオーディエンスIDは、mParticleダッシュボードの**オーディエンス**の下にあります。

例えば、mParticleのオーディエンス「Ibiza dreamers」のオーディエンスIDが「11036」の場合、これらのユーザーをフィルター`SegmentMembership` — `matches regex` — `11036`でセグメント化できます。

これはmParticleのデフォルトオプションですが、ほとんどのBrazeユーザーはBrazeでセグメントを作成する際のフィルタリング体験のために[単一配列属性](#array)を使用することを選択します。

{% alert important %}
この方法は、オーディエンスが数人よりも多い場合にはお勧めできません。カスタム属性の最大文字数は255文字であるため、この方法では数十または数百のオーディエンスを1つのユーザープロファイルに保存することはできません。ユーザーごとに多くのコホートがある場合は、「1属性ごとに1Segment」の構成を強くお勧めします。
{% endalert %}

![mParticle セグメントのメンバーシップ]({% image_buster /assets/img_archive/mparticle1.png %})

##### 単一配列属性 {#array}

mParticleは、各ユーザーに対してBrazeに単一のカスタム配列属性を作成し、それを`SegmentMembershipArray`と呼びます。この属性の値は、ユーザーに一致するmParticleオーディエンスIDの配列です。

たとえば、ユーザーが「13053」、「13052」、および「13051」というオーディエンス ID を持つ3つのmParticleオーディエンスのメンバーである場合、それらのオーディエンスの1つに一致するユーザーを、フィルター `SegmentMembershipArray` — `includes value` — `13051`でセグメント化できます。

{% alert note %}
Braze 配列属性の最大長は 25 です。ユーザーがメンバーとなっているオーディエンスが25を超える場合には、Braze によってメンバーシップ情報が切り捨てられます。これを回避するには、Brazeの担当者に連絡して、最大配列長のしきい値を増やしてください。
{% endalert %}

##### セグメント{#per-segment}ごとに1つの属性

mParticleは、ユーザーが属する各オーディエンスに対してブール値のカスタム属性を作成します。たとえば、「Possible Parisians」という mParticle オーディエンスの場合、フィルター `In Possible Parisians` - `equals` - `true` でこれらのユーザーをセグメント化できます。

![mParticle カスタム属性]({% image_buster /assets/img_archive/mparticle2.png %})

##### 単一の配列属性と単一の文字列属性{#both-1}

mParticleは、単一の配列属性と単一の文字列属性の両方で説明されているように属性を送信します。

##### 単一の配列属性とセグメントごとの1つの属性{#both-2}

mParticle は、単一配列属性とセグメントごとに1つの属性の両方によって記述されている属性を送信します。

##### 単一の文字列属性とセグメントごとの1つの属性{#both-3}

mParticleは、単一の文字列属性とセグメントごとの1つの属性の両方で説明されているように属性を送信します。

##### 単一配列属性、単一文字列属性、およびセグメントごとの1つの属性 {#multi}

mParticleは、単一の配列属性、単一の文字列属性、およびセグメントごとの1つの属性として記述されている属性を送信します。

#### ステップ1:mParticle でオーディエンスを作成する {#send_settings}

mParticleでオーディエンスを作成するには:

1. **オーディエンス** > **シングルワークスペース** > **\+ 新しいオーディエンス**に移動します。
2. オーディエンスの出力先としてBrazeを接続するには、次のフィールドを提供する必要があります:

| フィールド名               | 説明                                                                                                                                                                   |
| ------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API キー                  | Brazeのダッシュボードの**設定** > **APIキー**にあります。<br><br>古いナビゲーションを使用している場合は、**開発者コンソール** > **API設定**でAPIキーを見つけることができます。 |
| API キー オペレーティングシステム | どのオペレーティングシステムがあなたのBraze APIキーに対応しているかを選択してください。この選択は、オーディエンス更新で転送されるプッシュトークンの種類を制限します。                          |
| セグメントとして送信         | Brazeにオーディエンスを送信する方法。詳細については、セクション[Forwarding audiences](#forwarding-audiences)を参照してください。                                                          |
| ワークスペース REST APIキー   | すべての権限を持つ Braze REST API キー。これは Braze のダッシュボードで[**設定**] > [**API キー**] から作成できます。                                                        |
| External identity type   | external ID として Braze に転送する mParticle のユーザー ID タイプ。これはデフォルト値の Customer ID のままにすることをお勧めします。                                          |
| Email identity type      | メールとして Braze に転送する mParticle のユーザー ID タイプ。                                                                                                            |
| Braze インスタンス           | どのクラスターにBrazeデータを転送するか指定します。                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="3"}
3\.最後にオーディエンスを**保存**します。

数分以内にオーディエンスが Braze に同期されることが示されます。オーディエンスのメンバーシップは、`external_ids` が設定されているユーザー （つまり匿名ユーザーではないユーザー） に対してのみ更新されます。Braze mParticle オーディエンスの作成の詳細については、mParticle の[構成設定](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings)に関するドキュメントを参照してください。

#### ステップ2:Braze でユーザーをセグメント化する

Braze でこれらのユーザーのセグメントを作成するには、**Segments** の **エンゲージメント** に移動し、セグメントに名前を付けます。次のものは、**セグメントを送信する**ために選択したオプションに応じた2つのセグメントの例です。各オプションの詳細については、[転送オーディエンス](#forwarding-audiences.)を参照してください。

- **単一配列属性:**`SegmentMembershipArray`をフィルターとして選択します。次に、[値を含む] オプションを使用して目的のオーディエンス ID を入力します。![「値を含む」およびオーディエンス ID で設定された mParticle セグメントフィルター「SegmentMembershipArray」。]({% image_buster /assets/img_archive/mparticle5.png %})<br><br>
- **セグメントごとに1つの属性:**カスタム属性をフィルターとして選択します。次に、「等しい」オプションを使用し、適切なロジックを選択します。![「equals」と「true」で設定された mParticle セグメントフィルター「パリジャンの候補者内」。]({% image_buster /assets/img_archive/mparticle3.png %})

保存すると、キャンバスやキャンペーンの作成時にターゲットユーザーのステップでこのSegmentを参照できます。

#### 接続の無効化と削除

mParticleはBraze内のセグメントを直接管理しないため、対応するmParticleオーディエンス接続が削除または無効化された場合でも、セグメントは削除されません。この場合、mParticle は各ユーザーからオーディエンスを除去するために Braze でオーディエンスユーザー属性を更新しません。

削除前に Braze ユーザーからオーディエンスを除去するには、オーディエンスフィルターを調整してオーディエンスのサイズを強制的に0にしてから、オーディエンスを削除します。オーディエンスの計算が完了して0人のユーザーが返された後に、オーディエンスを削除します。次に、単一属性オプションの場合は Braze でオーディエンスのメンバーシップが `false` に更新されるか、配列形式からオーディエンス ID が削除されます。

## データマッピング

データは、mParticleを介してモバイルおよびWebアプリをBrazeに接続したい場合、[埋め込みキット統合](#embedded-kit-integration)を使用してBrazeにマッピングできます。また、[サーバー間API統合](#server-api-integration)を使用して、サーバー側のデータをBrazeに転送することもできます。

どのアプローチを選択する場合でも、Brazeを出力として設定する必要があります。

### Brazeの出力設定を構成する

mParticleで、**セットアップ > 出力 > 出力の追加**に移動し、**Braze**を選択してBrazeキットの構成を開封します。完了したら**保存**します。

| 設定名 | 説明 |
| ------------ | ----------- |
| Brazeアプリ識別子キー | Brazeアプリ識別子キーは、**設定** > **APIキー**のBrazeダッシュボードで見つけることができます。APIキーは各プラットフォーム（iOS、Android、Web）で異なることに注意してください。 |
| External identity type | external ID として Braze に転送する mParticle のユーザー ID タイプ。これはデフォルト値の Customer ID のままにすることをお勧めします。 |
| Email identity type | メールとして Braze に転送する mParticle のユーザー ID タイプ。これはデフォルト値の Email のままにすることをお勧めします。 |
| Braze インスタンス | Brazeデータが転送されるクラスター。これは、ダッシュボードがあるクラスターと同じである必要があります。 |
| イベントストリーム転送を有効にする | （サーバー間）有効にすると、すべてのイベントがリアルタイムで転送されます。そうでない場合、すべてのイベントが一括で転送されます。イベントストリーム転送を有効にする場合、Braze に渡すデータが[レート制限]({{site.baseurl}}/api/api_limits/)を尊重することを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img_archive/configure_settings.png %})

### 組み込みキットの統合

mParticle と Braze SDK は、埋め込みキット統合によってアプリケーションに表示されます。ただし、直接の Braze 統合とは異なり、mParticle が Braze SDK のメソッドのほとんどの呼び出しを処理します。ユーザーデータの追跡に使用する mParticle メソッドは、Braze SDK メソッドに自動的に マッピングされます。 

これらのmParticleのSDKの[Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy)、[iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy)、[Web](https://github.com/Appboy/integration-appboy)のマッピングはオープンソースであり、[mParticleのGitHubページ](https://github.com/mparticle-integrations)で見つけることができます。 

埋め込みキット SDK 統合により、Braze のフルスイート機能 (プッシュ、アプリ内メッセージ、および関連するすべてのメッセージ分析トラッキング) を利用できます。

{% alert note %}
コンテンツカードとカスタムアプリ内メッセージの統合には、Braze SDKメソッドを直接呼び出します。
{% endalert %}

#### ステップ1:mParticle SDKを統合する

プラットフォームのニーズに基づいて、適切な mParticle SDK をアプリに統合します。

* [mParticle for Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle for iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle for Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### ステップ2:mParticle の Braze イベントキット統合を完了する

このmParticle統合のためにBraze SDKをWebサイトやアプリに直接含める必要はありませんが、アプリからBrazeにデータを転送するために次のmParticle Appboy Kitをインストールする必要があります。

mParticle の[Braze イベントキット統合ガイド](https://docs.mparticle.com/integrations/braze/event/#kit-integration)は、メッセージングのニーズ (プッシュ、位置情報の追跡など) に基づくカスタムの mParticle および Braze 調整手順を説明します。

#### ステップ3:Braze 出力の接続の設定

mParticle で **[Connections] > [Connect] > [[目的のプラットフォーム]] > [Connect Output]** に移動し、出力として Braze を追加します。完了したら**保存**します。

![]({% image_buster /assets/img_archive/mParticle_event_config.png %})

すべての接続設定がすべてのプラットフォームおよび統合タイプに適用されるわけではありません。接続設定とそれらが適用されるプラットフォームの内訳については、[mParticleのドキュメント](https://docs.mparticle.com/integrations/braze/event/#connection-settings)を参照してください。

### サーバーAPI統合

mParticleのサーバーサイドSDK（例えば、Ruby、Pythonなど）を使用している場合、バックエンドデータをBrazeにルーティングするためのアドオンです。Braze でこのサーバー間統合を設定するには、[mParticle のドキュメント](https://docs.mparticle.com/guides/platform-guide/connections/)の説明に従ってください。

{% alert important %}
サーバー間統合では、アプリ内メッセージング、コンテンツカード、プッシュ通知などの Braze UI 機能はサポートされていません。この方法では利用できないデバイスレベルのフィールドなど、自動的にキャプチャされたデータも存在します。 

これらの機能を使用したい場合は、並列統合を検討してください。

サーバー側のデータをBrazeに転送するには、`external_id`を含める必要があります。匿名ユーザーは転送されません。
{% endalert %}

#### Braze 出力の接続の設定

mParticle で **[Connections] > [Connect] > [[目的のプラットフォーム]] > [Connect Output]** に移動し、出力として Braze を追加します。完了したら**保存**します。 

![]({% image_buster /assets/img_archive/mParticle_connections.png %})

すべての接続設定がすべてのプラットフォームおよび統合タイプに適用されるわけではありません。接続設定とそれらが適用されるプラットフォームの内訳については、[mParticleのドキュメント](https://docs.mparticle.com/integrations/braze/event/#connection-settings)を参照してください。

「拡張ユーザー属性」または「拡張ユーザーID」を有効にする前に、これらの設定がデータポイント使用量にどのように影響するかを把握するために[データポイント超過](#potential-data-point-overages)を確認することをお勧めします。

### データマッピングの詳細

#### データ型
両方のプラットフォーム間でサポートされているデータ型はすべてではありません。
- [カスタムイベントプロパティ]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)は、文字列、数値、ブール値、または日付オブジェクトをサポートします。配列やネストされたオブジェクトはサポートされていません。
- [カスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)は文字列、数値、ブール値、日付オブジェクト、および配列をサポートしますが、オブジェクトやネストされたオブジェクトはサポートしません。 

{% alert note %}
Braze は `Time` タイプのカスタム属性で0年以前または3000年以降のタイムスタンプをサポートしていません。Braze は、これらの値が mParticle によって送信されると値を取り込みますが、値は文字列として保存されます。
{% endalert %}

#### データマッピング

| mParticle データ タイプ | Brazeデータ型 | 説明 |
| ------------------- | --------------- | ----------- |
| ユーザー属性（予約済み） | 標準属性項目 | 例えば、mParticleの`$FirstName`予約ユーザー属性キーは、Brazeの`first_name`標準属性項目フィールドにマッピングされます。 |
| ユーザー属性（その他） | カスタム属性 | mParticle に渡されたユーザー属性が、予約済みのユーザー属性キーの範囲外にある場合、そのユーザー属性はカスタム属性として Braze に記録されます。<br><br>ユーザー属性は文字列、数値、ブール値、日付、および配列をサポートしますが、オブジェクトやネストされたオブジェクトはサポートしません。 |
| カスタムイベント | カスタムイベント | mParticleカスタムイベントはBrazeによってカスタムイベントとして認識されます。イベント属性はカスタムイベントプロパティとして転送されます。<br><br>イベントプロパティとしてBrazeに渡されるイベント属性は、文字列、数値、ブール値、または日付オブジェクトをサポートしますが、配列やネストされたオブジェクトはサポートしません。 |
| 購入コマースイベント | 購入イベント | 購入コマースイベントは Braze の購入イベントにマッピングされます。<br><br>バンドルコマースイベントデータの設定値を切り替えて、注文レベルまたは製品レベルで購入を記録します。たとえば `false` の場合、2つの一意の製品、プロモーション、またはインプレッションを含む1つの受信イベントでは、少なくとも2つの送信 Braze イベントが生成されます。`true` に設定すると、ネストされた製品、プロモーション、またはインプレッションの配列を含む1つの送信イベントが生成されます。<br><br>ログに記録される追加のコマースフィールドの詳細については、[mParticle のドキュメント](https://docs.mparticle.com/integrations/braze/event/#purchase-events)を参照してください。<br><br>「バンドルコマースイベントデータ」を `false` として設定する場合、購入イベントプロパティとして Braze に渡される製品属性では、文字列、数値、ブール値、または日付オブジェクトがサポートされますが、配列やネストされたオブジェクトはサポートされません。|
| その他のすべてのコマースイベント | カスタムイベント | 他のすべての商取引イベントはカスタムイベントにマッピングされます。<br><br>バンドルコマースイベントデータの設定値を切り替えて、注文レベルまたは製品レベルで購入を記録します。たとえば `false` の場合、2つの一意の製品、プロモーション、またはインプレッションを含む1つの受信イベントでは、少なくとも2つの送信 Braze イベントが生成されます。`true` に設定すると、ネストされた製品、プロモーション、またはインプレッションの配列を含む1つの送信イベントが生成されます。<br><br>特定のデフォルトコマース値に加えて、製品属性が Braze イベントプロパティとして記録されます。ログに記録される追加のコマースフィールドの詳細については、[mParticle のドキュメント](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events)を参照してください。<br><br>「バンドルコマースイベントデータ」を `false` として設定する場合、イベントプロパティとして Braze に渡される製品属性では、文字列、数値、ブール値、または日付オブジェクトがサポートされますが、配列やネストされたオブジェクトはサポートされません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### ユーザーアイデンティティマッピング
各mParticle出力について、`external_id`としてBrazeに送信する外部IDタイプを選択できます。デフォルト値は顧客IDですが、`MPID`などの別のIDをBrazeに`external_id`として送信するようにマッピングすることもできます。顧客 ID 以外の識別子を選択すると、Braze でのデータの送信方法に影響する場合があることに注意してください。 

例えば、MPIDをBraze `external_id`にマッピングすると、次のような効果があります:
- MPIDが割り当てられるタイミングの性質上、すべてのユーザーはセッション開始時に`external_id`が割り当てられます。
- MPID と `external_id` のデータ型が異なるため、Currents の設定で追加のマッピングが必要になる場合があります。

### 消去要求 (データ主体の要求) の転送

Braze へ消去要求を転送するには、Braze へのデータ主体要求出力を設定します。消去要求を Braze に転送するには、[mParticle のドキュメント](https://docs.mparticle.com/integrations/braze/forwarding-dsr/)の説明に従います。

## 潜在的なデータポイントの超過

### 強化されたユーザー属性

#### ユーザー属性/識別子の強化を有効にする (サーバー間のみ) {#enriched}

mParticle接続設定では、Brazeは**拡張ユーザー属性を含める**をオフにすることを推奨します。有効にすると、mParticleは、既存のプロファイルから利用可能なすべてのユーザー属性（標準属性、カスタム属性、計算された属性など）を各ログイベントでBrazeに転送します。これにより、mParticleが各呼び出しで同じ変更されていない属性をBrazeに送信するため、データポイントの消費が多くなります。

たとえば、ユーザーが最初のセッションで名、姓、電話番号を追加し、その後、同じ情報とメールを追加してニュースレターに登録すると、ニュースレター登録イベントがトリガーされるとします。
- オンにすると（デフォルト）、FIVEつのデータポイントが発生します。（サインアップイベント、メールアドレス、名、姓、電話番号）
- オフにすると、2つのデータポイント（サインアップイベントとメールアドレス）が発生します

{% alert note %}
この設定をオフにすると、データの変更はチェックされません。ただし、統合が元のインバウンドバッチで受信されなかったか、イベントの属性として明示的に設定されていないユーザーのプロファイル上のすべてのユーザー属性を送信するのを防ぎます。差分のみが Braze に渡されることを確認することが重要です。
{% endalert %}

#### 強化されたユーザー属性をオフにすることの考慮事項

**リッチユーザー属性を含める**をオフにする際に注意すべき点がいくつかあります:
1. サーバー間統合はmParticleイベントAPIを使用してイベントをBrazeに送信します。各リクエストはイベントによってトリガーされます。メールアドレスの更新など、ユーザー属性が変更されても、そのユーザー属性が特定のイベント (プロファイル更新カスタムイベントなど) に関連付けられていない場合、新しい値は、ユーザーによってトリガーされる次のイベントのペイロードで「強化属性」として Braze などの出力に渡されるだけです。**Include Enriched User Attributes**がオフになっている場合、この新しい属性値は特定のイベントに関連付けられていないため、Brazeに渡されません。
  - これを解決するために、更新された特定のユーザー属性のみをBrazeに送信する「ユーザー属性更新」イベントを別途作成することをお勧めします。この方法では、「ユーザー属性更新」イベントの追加データポイントは記録されますが、データポイントの消費は、この機能が有効になっておりすべての呼び出しですべてのユーザー属性が送信される場合よりもはるかに少なくなることに注意してください。
2. 計算された属性は、強化されたユーザー属性としてBrazeに渡されるため、「強化されたユーザー属性」がオフになると、これらはもはやBrazeに渡されません。「強化されたユーザー属性」がオフになっている場合、すべての属性をプッシュすることなく、[計算された属性フィード](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed)がBrazeに計算された属性を転送するのに役立ちます。計算された属性が変更されると、フィードはBrazeに下流の更新を送信します。 

### Brazeに不要または重複するデータを送信する
Brazeは、値が変更されていない場合でも、属性がBrazeに渡されるたびにデータポイントをカウントします。このため、Braze 内でアクションを実行するために必要なデータのみを転送し、属性の差分のみが渡されるようにすることが推奨されます。

