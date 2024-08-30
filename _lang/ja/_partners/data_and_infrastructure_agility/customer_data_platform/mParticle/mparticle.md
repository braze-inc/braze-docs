---
nav_title: mParticle
article_title: mParticle
alias: /partners/mparticle/
description: "この記事は、BrazeとmParticleのパートナーシップについて説明しています。mParticleは、マーケティングスタック内のソース間で情報を収集およびルーティングする顧客データプラットフォームです。"
page_type: partner
search_tag: Partner

---

# mParticle

{% multi_lang_include video.html id="Njhqwd36gZM" align="right" %}

> mParticleの顧客データプラットフォームは、データを活用する力を高めます。洗練されたマーケターは、mParticleを使用して成長スタック全体にわたるデータを調整し、重要なカスタマージャーニーの瞬間に勝利することを可能にします。

BrazeとmParticleの統合により、2つのシステム間の情報の流れをシームレスにコントロールできます。
- mParticleのオーディエンスをBrazeに同期して、Brazeのキャンペーンとキャンバスのセグメンテーションを行います。
- 2つのプラットフォーム間でデータを共有する。これはmParticleキット統合とサーバー間統合を通じて行うことができます。
- [mParticleを通じてBrazeユーザーのインタラクションをCurrentsに送信]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/)し、成長スタック全体でアクション可能にします。 

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| mParticle アカウント | このパートナーシップを利用するには、[mParticleアカウント](https://app.mparticle.com/login)が必要です。 |
| Brazeインスタンス | Brazeインスタンスは[API概要ページ]({{site.baseurl}}/api/basics/#endpoints)にあります。例えば：米国-01、米国-02、など。 |
| Brazeアプリ識別子キー | あなたのアプリ識別子キー。<br><br>これは、**Braze ダッシュボード > 設定の管理 > API キー**内にあります。 |
| ワークスペース REST APIキー | （サーバー間）Braze REST APIキー<br><br>これは、**Braze ダッシュボード > 開発者コンソール > API 設定 > API キー**内で作成できます。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### 観客

BrazeとmParticleのパートナーシップを利用して、統合を構成し、mParticleのオーディエンスを直接Brazeにインポートしてリターゲティングを行い、1つのシステムから別のシステムへのデータの完全なループを作成します。設定した任意の統合は、アカウントのデータポイント量にカウントされます。

#### 転送オーディエンス

mParticleは、コホートメンバーシップ属性を設定するための3つの方法を提供しており、「[Send Segments As](#send_settings)」構成設定によって制御されます。次のセクションを参照して、各オプションの処理を行ってください。

- [シングルストリング属性](#string)
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
このソリューションは、オーディエンスが数人以上いる場合にはお勧めできません。カスタム属性は最大255文字まで可能なので、この方法では数十または数百のオーディエンスをユーザープロファイルに保存することはできません。ユーザーごとに多くのコホートがある場合は、「1属性ごとに1Segment」の構成を強くお勧めします。
{% endalert %}

![mParticle Segment メンバーシップ][6]

##### 単一配列属性 {#array}

mParticleは、各ユーザーに対してBrazeに単一のカスタム配列属性を作成し、それを`SegmentMembershipArray`と呼びます。この属性の値は、ユーザーに一致するmParticleオーディエンスIDの配列です。

例えば、ユーザーが3つのmParticleオーディエンス（オーディエンスIDが「13053」、「13052」、「13051」）のメンバーである場合、`SegmentMembershipArray` — `includes value` — `13051`のフィルターを使用して、それらのオーディエンスのいずれかに一致するユーザーをセグメント化できます。

{% alert note %}
Braze 配列属性の最大長は 25 です。ユーザーが25以上のオーディエンスのメンバーである場合、Brazeによってメンバーシップ情報が切り捨てられます。これを回避するには、Brazeの担当者に連絡して、最大配列長のしきい値を増やしてください。
{% endalert %}

##### セグメント{#per-segment}ごとに1つの属性

mParticleは、ユーザーが属する各オーディエンスに対してブール値のカスタム属性を作成します。例えば、mParticleのオーディエンスが「Possible Parisians」と呼ばれる場合、これらのユーザーを`In Possible Parisians` - `equals` - `true`のフィルターでSegmentできます。

![mParticleカスタム属性][7]

##### 単一の配列属性と単一の文字列属性{#both-1}

mParticleは、単一の配列属性と単一の文字列属性の両方で説明されているように属性を送信します。

##### 単一の配列属性とセグメントごとの1つの属性{#both-2}

mParticleは、単一の配列属性とセグメントごとの1つの属性の両方で説明されているように属性を送信します。

##### 単一の文字列属性とセグメントごとの1つの属性{#both-3}

mParticleは、単一の文字列属性とセグメントごとの1つの属性の両方で説明されているように属性を送信します。

##### 単一の配列属性、単一の文字列属性、およびセグメント{#multi}ごとの1つの属性

mParticleは、単一の配列属性、単一の文字列属性、およびセグメントごとの1つの属性として記述されている属性を送信します。

#### ステップ1:mParticleでオーディエンスを作成する {#send_settings}

mParticleでオーディエンスを作成するには:

1. **オーディエンス** > **シングルワークスペース** > **\+ 新しいオーディエンス**に移動します。
2. オーディエンスの出力先としてBrazeを接続するには、次のフィールドを提供する必要があります:

| フィールド名               | 説明                                                                                                                                                                   |
| ------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API キー                  | Brazeのダッシュボードの**設定** > **APIキー**にあります。<br><br>古いナビゲーションを使用している場合は、**開発者コンソール** > **API設定**でAPIキーを見つけることができます。 |
| API キー オペレーティングシステム | どのオペレーティングシステムがあなたのBraze APIキーに対応しているかを選択してください。この選択は、オーディエンス更新で転送されるプッシュトークンの種類を制限します。                          |
| セグメントとして送信         | Brazeにオーディエンスを送信する方法。詳細については、セクション[Forwarding audiences](#forwarding-audiences)を参照してください。                                                          |
| ワークスペース REST APIキー   | Braze REST APIキー with full permissions.これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。                                                        |
| 外部アイデンティティタイプ   | mParticleのユーザーIDタイプを外部IDとしてBrazeに転送します。これをデフォルト値のままにしておくことをお勧めします、顧客ID。                                          |
| メールアイデンティティタイプ      | mParticleのユーザーIDタイプをメールとしてBrazeに転送します。                                                                                                            |
| Brazeインスタンス           | どのクラスターにBrazeデータを転送するか指定します。                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2}

{:start="3"}
3\.最後に**オーディエンス**を保存します。

数分以内にBrazeにオーディエンスの同期が開始されるはずです。オーディエンスメンバーシップは、`external_ids`（つまり、匿名ユーザーではない）を持つユーザーに対してのみ更新されます。Braze mParticleオーディエンスの作成に関する詳細は、mParticleの[設定](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings)に関するドキュメントを参照してください。

#### ステップ2:Brazeでセグメントユーザー

Braze でこれらのユーザーのセグメントを作成するには、**Segments** の **エンゲージメント** に移動し、セグメントに名前を付けます。次のものは、**セグメントを送信する**ために選択したオプションに応じた2つのセグメントの例です。各オプションの詳細については、[転送オーディエンス](#forwarding-audiences.)を参照してください。

- **単一の配列属性:**`SegmentMembershipArray`をフィルターとして選択します。次に、「値を含む」オプションを使用して、希望するオーディエンスIDを入力します。 ![mParticle Segment フィルター「SegmentMembershipArray」を「値を含む」として設定し、オーディエンスIDを入力します。][11]<br><br>
- **セグメントごとに1つの属性:**カスタム属性をフィルターとして選択します。次に、「等しい」オプションを使用し、適切なロジックを選択します。![mParticle Segment フィルター「in possible parisians」を「等しい」と「true」に設定します。][8]

保存すると、キャンバスやキャンペーンの作成時にターゲットユーザーのステップでこのSegmentを参照できます。

#### 接続の無効化と削除

mParticleはBraze内のセグメントを直接管理しないため、対応するmParticleオーディエンス接続が削除または無効化された場合でも、セグメントは削除されません。このような場合、mParticleはBrazeのオーディエンスユーザー属性を更新せず、各ユーザーからオーディエンスを削除しません。

Brazeユーザーからオーディエンスを削除するには、オーディエンスを削除する前にオーディエンスフィルターを調整してオーディエンスサイズを0にします。オーディエンスの計算が完了して0人のユーザーが返された後、オーディエンスを削除します。次に、オーディエンスメンバーシップは、単一の属性オプションの場合は`false`に更新され、または配列形式からオーディエンスIDが削除されます。

## データマッピング

データは、mParticleを介してモバイルおよびWebアプリをBrazeに接続したい場合、[埋め込みキット統合](#embedded-kit-integration)を使用してBrazeにマッピングできます。また、[サーバー間API統合](#server-api-integration)を使用して、サーバー側のデータをBrazeに転送することもできます。

どのアプローチを選択する場合でも、Brazeを出力として設定する必要があります。

### Brazeの出力設定を構成する

mParticleで、**セットアップ > 出力 > 出力の追加**に移動し、**Braze**を選択してBrazeキットの構成を開封します。**保存** 完了したら。

| 設定名 | 説明 |
| ------------ | ----------- |
| Brazeアプリ識別子キー | Brazeアプリ識別子キーは、**設定** > **APIキー**のBrazeダッシュボードで見つけることができます。APIキーは各プラットフォーム（iOS、Android、Web）で異なることに注意してください。 |
| 外部アイデンティティタイプ | mParticleのユーザーIDタイプを外部IDとしてBrazeに転送します。これをデフォルト値のままにしておくことをお勧めします、顧客ID |
| メールアイデンティティタイプ | mParticleのユーザーIDタイプをメールとしてBrazeに転送します。これをデフォルト値のままにしておくことをお勧めします、メール、 |
| Brazeインスタンス | Brazeデータが転送されるクラスター。これは、ダッシュボードがあるクラスターと同じである必要があります。 |
| イベントストリーム転送を有効にする | （サーバー間）有効にすると、すべてのイベントがリアルタイムで転送されます。そうでない場合、すべてのイベントが一括で転送されます。イベントストリーム転送を有効にする場合、Braze に渡すデータが[レート制限]({{site.baseurl}}/api/basics/#api-limits)を尊重することを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2}

![][10]

### 組み込みキットの統合

mParticleとBraze SDKは、埋め込みキット統合を通じてアプリケーションに存在します。ただし、直接のBraze統合とは異なり、mParticleはBraze SDKメソッドの大部分を呼び出すことを担当します。mParticleのメソッドを使用してユーザーデータを追跡すると、自動的にBrazeのSDKメソッドにマッピングされます。 

これらのmParticleのSDKの[Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy)、[iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy)、[Web](https://github.com/Appboy/integration-appboy)のマッピングはオープンソースであり、[mParticleのGitHubページ](https://github.com/mparticle-integrations)で見つけることができます。 

埋め込みキットSDKの統合により、フル機能スイート（プッシュ、アプリ内メッセージ、およびすべての関連するメッセージ分析トラッキング）を活用できます。

{% alert note %}
コンテンツカードとカスタムアプリ内メッセージの統合には、Braze SDKメソッドを直接呼び出します。
{% endalert %}

#### ステップ1:mParticle SDKを統合する

プラットフォームのニーズに基づいて、適切なmParticle SDKをアプリに統合します。

* [Android 用 mParticle](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [iOS用mParticle](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [Web用mParticle](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### ステップ2:mParticleのBrazeイベントキット統合を完了する

このmParticle統合のためにBraze SDKをWebサイトやアプリに直接含める必要はありませんが、アプリからBrazeにデータを転送するために次のmParticle Appboy Kitをインストールする必要があります。

mParticleの[Brazeイベントキット統合ガイド](https://docs.mparticle.com/integrations/braze/event/#kit-integration)は、メッセージングのニーズ（プッシュ、位置情報の追跡など）に基づいて、カスタムmParticleとBrazeの調整手順を案内します。

#### ステップ3:Braze出力の接続設定

mParticleで、**接続 > 接続 > \[希望するプラットフォーム] > 出力を接続**して、Brazeを出力として追加します。**保存** 完了したら。

![][3]

すべての接続設定がすべてのプラットフォームおよび統合タイプに適用されるわけではありません。接続設定とそれらが適用されるプラットフォームの内訳については、[mParticleのドキュメント](https://docs.mparticle.com/integrations/braze/event/#connection-settings)を参照してください。

### サーバーAPI統合

mParticleのサーバーサイドSDK（例えば、Ruby、Pythonなど）を使用している場合、バックエンドデータをBrazeにルーティングするためのアドオンです。このサーバー間統合をBrazeで設定するには、[mParticleのドキュメント](https://docs.mparticle.com/guides/platform-guide/connections/)に従ってください。

{% alert important %}
サーバー間統合は、アプリ内メッセージング、コンテンツカード、プッシュ通知などのBraze UI機能をサポートしていません。この方法では利用できないデバイスレベルのフィールドなど、自動的にキャプチャされたデータも存在します。 

これらの機能を使用したい場合は、並列統合を検討してください。

サーバー側のデータをBrazeに転送するには、`external_id`を含める必要があります。匿名ユーザーは転送されません。
{% endalert %}

#### Braze出力の接続設定

mParticleで、**接続 > 接続 > \[希望するプラットフォーム] > 出力を接続**して、Brazeを出力として追加します。**保存** 完了したら。 

![][4]

すべての接続設定がすべてのプラットフォームおよび統合タイプに適用されるわけではありません。接続設定とそれらが適用されるプラットフォームの内訳については、[mParticleのドキュメント](https://docs.mparticle.com/integrations/braze/event/#connection-settings)を参照してください。

「拡張ユーザー属性」または「拡張ユーザーID」を有効にする前に、これらの設定がデータポイント使用量にどのように影響するかを把握するために[データポイント超過](#potential-data-point-overages)を確認することをお勧めします。

### データマッピングの詳細

#### データ型
両方のプラットフォーム間でサポートされているデータ型はすべてではありません。
- [カスタムイベントプロパティ]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)は、文字列、数値、ブール値、または日付オブジェクトをサポートします。配列やネストされたオブジェクトはサポートされていません。
- [カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/)は文字列、数値、ブール値、日付オブジェクト、および配列をサポートしますが、オブジェクトやネストされたオブジェクトはサポートしません。 

{% alert note %}
Brazeは`Time`タイプのカスタム属性で0年以前または3000年以降のタイムスタンプをサポートしていません。BrazeはmParticleによって送信されたこれらの値を取り込みますが、その値は文字列として保存されます。
{% endalert %}

#### データマッピング

| mParticle データ タイプ | Brazeデータ型 | 説明 |
| ------------------- | --------------- | ----------- |
| ユーザー属性（予約済み） | 標準属性項目 | 例えば、mParticleの`$FirstName`予約ユーザー属性キーは、Brazeの`first_name`標準属性項目フィールドにマッピングされます。 |
| ユーザー属性（その他） | カスタム属性 | mParticle に渡される予約済みユーザー属性キーの範囲外のユーザー属性は、Braze にカスタム属性として記録されます。<br><br>ユーザー属性は文字列、数値、ブール値、日付、および配列をサポートしますが、オブジェクトやネストされたオブジェクトはサポートしません。 |
| カスタムイベント | カスタムイベント | mParticleカスタムイベントはBrazeによってカスタムイベントとして認識されます。イベント属性はカスタムイベントプロパティとして転送されます。<br><br>イベントプロパティとしてBrazeに渡されるイベント属性は、文字列、数値、ブール値、または日付オブジェクトをサポートしますが、配列やネストされたオブジェクトはサポートしません。 |
| 購入コマースイベント | 購入イベント | 購入コマースイベントはBraze購入イベントにマッピングされます。<br><br>バンドルコマースイベントデータの設定値を切り替えて、注文レベルまたは製品レベルで購入を記録します。例えば、`false`、2つのユニークな製品、プロモーション、またはインプレッションを含む単一の受信イベントは、少なくとも2つの送信Brazeイベントをもたらします。設定を`true`にすると、ネストされた製品、プロモーション、またはインプレッションの配列を持つ単一の送信イベントが生成されます。<br><br>追加のコマースフィールドのログに関する詳細については、[mParticleのドキュメント](https://docs.mparticle.com/integrations/braze/event/#purchase-events)を参照してください。<br><br>「バンドルコマースイベントデータ」を`false`として設定する場合、製品属性は購入イベントプロパティとしてBrazeに渡され、文字列、数値、ブール値、または日付オブジェクトがサポートされますが、配列やネストされたオブジェクトはサポートされません。|
| 他のすべての商取引イベント | カスタムイベント | 他のすべての商取引イベントはカスタムイベントにマッピングされます。<br><br>バンドルコマースイベントデータの設定値を切り替えて、注文レベルまたは製品レベルで購入を記録します。例えば、`false`、2つのユニークな製品、プロモーション、またはインプレッションを含む単一の受信イベントは、少なくとも2つの送信Brazeイベントをもたらします。設定を`true`にすると、ネストされた製品、プロモーション、またはインプレッションの配列を持つ単一の送信イベントが生成されます。<br><br>特定のデフォルトコマース値に加えて、製品属性はBrazeイベントプロパティとして記録されます。追加のコマースフィールドのログ記録に関する詳細については、[mParticleのドキュメント](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events)を参照してください。<br><br>「バンドルコマースイベントデータ」を`false`製品属性としてBrazeにイベントプロパティとして渡す場合、文字列、数値、ブール値、または日付オブジェクトをサポートしますが、配列やネストされたオブジェクトはサポートしません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### ユーザーアイデンティティマッピング
各mParticle出力について、`external_id`としてBrazeに送信する外部IDタイプを選択できます。デフォルト値は顧客IDですが、`MPID`などの別のIDをBrazeに`external_id`として送信するようにマッピングすることもできます。識別子以外の顧客IDを選択すると、Brazeに送信されるデータに影響を与える可能性があることに注意してください。 

例えば、MPIDをBraze `external_id`にマッピングすると、次のような効果があります:
- MPIDが割り当てられるタイミングの性質上、すべてのユーザーはセッション開始時に`external_id`が割り当てられます。
- Currentsのセットアップには、MPIDと`external_id`の間でデータ型が異なるため、追加のマッピングが必要な場合があります。

### 消去要求の転送（データ主体の要求）

Brazeにデータ主体リクエスト出力を設定して、消去リクエストをBrazeに転送します。消去リクエストをBrazeに転送するには、[mParticleのドキュメント](https://docs.mparticle.com/integrations/braze/forwarding-dsr/)に従ってください。

## 潜在的なデータポイントの超過

### 強化されたユーザー属性

#### ユーザー属性/アイデンティティの有効化（サーバー間のみ）{#enriched}

mParticle接続設定では、Brazeは**拡張ユーザー属性を含める**をオフにすることを推奨します。有効にすると、mParticleは、既存のプロファイルから利用可能なすべてのユーザー属性（標準属性、カスタム属性、計算された属性など）を各ログイベントでBrazeに転送します。これにより、mParticleが各呼び出しで同じ変更されていない属性をBrazeに送信するため、データポイントの消費が多くなります。

例えば、ユーザーが最初のセッション中に名、姓、電話番号を追加し、後で同じ情報に加えてメールを追加してニュースレターにサインアップする場合、ニュースレターのサインアップイベントがトリガーされます。
- オンにすると（デフォルト）、FIVEつのデータポイントが発生します。（サインアップイベント、メールアドレス、名、姓、電話番号）
- オフにすると、2つのデータポイント（サインアップイベントとメールアドレス）が発生します

{% alert note %}
この設定をオフにすると、データの変更をチェックしません。ただし、統合が元のインバウンドバッチで受信されなかったか、イベントの属性として明示的に設定されていないユーザーのプロファイル上のすべてのユーザー属性を送信するのを防ぎます。依然としてデルタのみがBrazeに渡されることを確認することが重要です。
{% endalert %}

#### 強化されたユーザー属性をオフにすることの考慮事項

**リッチユーザー属性を含める**をオフにする際に注意すべき点がいくつかあります:
1. サーバー間統合はmParticleイベントAPIを使用してイベントをBrazeに送信します。各リクエストはイベントによってトリガーされます。ユーザー属性が変更されたとき、例えばメールアドレスの更新など、特定のイベントに関連付けられていない場合（例えば、プロファイル更新カスタムイベント）、新しい値はユーザーによってトリガーされた次のイベントのペイロード内の「強化された属性」としてBrazeのような出力にのみ渡されます。**Include Enriched User Attributes**がオフになっている場合、この新しい属性値は特定のイベントに関連付けられていないため、Brazeに渡されません。
  - これを解決するために、更新された特定のユーザー属性のみをBrazeに送信する「ユーザー属性更新」イベントを別途作成することをお勧めします。このアプローチでは、「ユーザー属性更新」イベントの追加のデータポイントを記録していますが、機能が有効になっているすべての呼び出しでユーザー属性をすべて送信するよりも、データポイントの消費は大幅に少なくなります。
2. 計算された属性は、強化されたユーザー属性としてBrazeに渡されるため、「強化されたユーザー属性」がオフになると、これらはもはやBrazeに渡されません。「強化されたユーザー属性」がオフになっている場合、すべての属性をプッシュすることなく、[計算された属性フィード](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed)がBrazeに計算された属性を転送するのに役立ちます。計算された属性が変更されると、フィードはBrazeに下流の更新を送信します。 

### Brazeに不要または重複するデータを送信する
Brazeは、値が変更されていない場合でも、属性がBrazeに渡されるたびにデータポイントをカウントします。このため、BrazeはBraze内でアクションを実行するために必要なデータのみを転送し、属性のデルタのみが渡されることを確認することを推奨します。

[1]: https://dashboard.braze.com/app_settings/developer_console
[2]: {% image_buster /assets/img_archive/dashboard_keys_locations.png %}
[3]: {% image_buster /assets/img_archive/mParticle_event_config.png %}
[4]: {% image_buster /assets/img_archive/mParticle_connections.png %}
[6]: {% image_buster /assets/img_archive/mparticle1.png %}
[7]: {% image_buster /assets/img_archive/mparticle2.png %}
[8]: {% image_buster /assets/img_archive/mparticle3.png %}
[9]: {% image_buster /assets/img_archive/mparticle4.png %}
[10]: {% image_buster /assets/img_archive/configure_settings.png %}
[11]: {% image_buster /assets/img_archive/mparticle5.png %}
[5]: \#組み込みキット統合
