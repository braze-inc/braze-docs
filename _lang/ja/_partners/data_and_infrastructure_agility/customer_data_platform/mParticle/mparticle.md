---
nav_title: mParticle
article_title: mParticle
alias: /partners/mparticle/
description:「この参考記事では、BrazeとmParticleのパートナーシップについて概説しています。mParticleは、情報を収集してマーケティングスタック内のソース間でルーティングする顧客データプラットフォームです。「
page_type: partner
search_tag:Partner

---

# mParticle

{% multi_lang_include video.html id="Njhqwd36gZM" align="right" %}

> mParticleの顧客データプラットフォームにより、データをさらに活用できるようになります。洗練されたマーケターは、mParticleを使用して自社の成長スタック全体にわたってデータを調整し、カスタマージャーニー重要な瞬間を勝ち取れるようにしています。

Braze と mParticle の統合により、2 つのシステム間の情報の流れをシームレスにコントロールできます。
- mParticle オーディエンスを Braze for Braze キャンペーンとキャンバスセグメンテーションに同期します。
- 2 つのプラットフォーム間でデータを共有します。これは、mParticle キットの統合とサーバー間の統合によって実現できます。
- [Braze のユーザーインタラクションを Currents 経由で mParticle に送ることで]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/)、成長スタック全体でアクションが可能になります。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| mParticle アカウント | このパートナーシップを利用するには、[mParticleアカウントが必要です](https://app.mparticle.com/login)。 |
| Brazeインスタンス | Brazeインスタンスは [API 概要ページにあります]({{site.baseurl}}/api/basics/#endpoints)。(例:米国-01、米国-02など) |
| Braze アプリ識別子キー | アプリ識別子キー。<br><br>これは **Braze ダッシュボード > 設定の管理 > API キーにあります**。 |
| ワークスペース REST API キー | (サーバー間) Braze REST API キー<br><br>これは **Braze ダッシュボード > デベロッパーコンソール > API 設定 > API キーで作成できます**。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### オーディエンス

Braze と mParticle 's partnership to configure your integration and import mParticle audiences directly into Braze for retargeting, creating a full loop of data from one system to another. Any integration you set up will count toward your account' データポイントボリュームを使用してください。

#### オーディエンスの転送

mParticleには、「[Send Segments](#send_settings) As」構成設定によって制御されるコホートメンバーシップ属性を設定する3つの方法があります。各オプションの処理については、次のセクションを参照してください。

- [単一文字列属性](#string)
- [単一配列属性](#array)
- [Segment ごとに 1 つの属性](#per-segment)
- [単一配列属性単一文字列属性両方](#both-1)
- [1 つの配列属性 Segment ごとに 1 つの属性両方](#both-2)
- [1 つの文字列属性 Segment ごとに 1 つの属性両方](#both-3)
- [1 つの配列属性、1 つの文字列属性、およびSegment ごとに 1 つの属性](#multi)

##### 単一文字列属性 {#string}

mParticle `SegmentMembership` はというカスタム属性を 1 つ作成します。この属性値は、ユーザーと一致する mParticle オーディエンス ID をカンマで区切った文字列です。これらのオーディエンス ID は、mParticle ダッシュボードの「**オーディエンス**」にあります。

たとえば、mParticle オーディエンス「Ibiza dreamers」のオーディエンス ID が「11036」の場合、これらのユーザーをフィルター — — を使用してSegment できます。`SegmentMembership` `matches regex` `11036`

これはmParticleのデフォルトオプションですが、ほとんどのBrazeユーザーは、[Brazeでセグメントを作成するときのフィルタリングエクスペリエンスに単一配列アトリビュートを使用することを選択します](#array)。

{% alert important %}
カスタム属性の長さは最大255文字で、この方法を使用してユーザープロファイル数十または数百のオーディエンスを保存することはできないため、オーディエンスが数人以上いる場合はこの方法はお勧めしません。ユーザーあたりのコホート数が多い場合は、「Segment ごとに1つの属性」の構成を強くお勧めします。
{% endalert %}

![mParticle Segment メンバーシップ][6]

##### 単一配列属性 {#array}

mParticleは、Brazeで各ユーザー用にという名前のカスタム配列属性を1つ作成します。`SegmentMembershipArray`この属性値は、ユーザー一致する mParticle オーディエンス ID の配列です。

たとえば、あるユーザーオーディエンス ID が「13053」、「13052」、「13051」の 3 つの mParticle オーディエンスのメンバーである場合、それらのオーディエンスいずれかに一致するユーザーをフィルター — — でSegment できます。`SegmentMembershipArray` `includes value` `13051`

{% alert note %}
Braze アレイアトリビュートの最大長は 25 です。ユーザーのいずれかが25人以上のオーディエンスのメンバーである場合、メンバーシップ情報はBrazeによって切り捨てられます。この問題を回避するには、Braze の担当者に連絡して、アレイの最大長しきい値を増やしてください。
{% endalert %}

##### Segment ごとに 1 つの属性 {#per-segment}

mParticleは、ユーザー属するオーディエンスごとにブーリアンカスタム属性を作成します。たとえば、mParticle のオーディエンスが「Pussible Parisians」と呼ばれている場合、これらのユーザーをフィルター `In Possible Parisians`--でSegment できます。`equals` `true`

![mParticle カスタム属性][7]

##### 単一配列属性単一文字列属性両方 {#both-1}

mParticle は、単一配列アトリビュートと単一文字列属性ビュートの両方の記述に従って属性を送信します。

##### 1 つの配列属性 Segment ごとに 1 つの属性両方 {#both-2}

mParticle は、単一配列アトリビュートとSegment ごとに 1 つの属性ビュートの両方の記述に従って属性を送信します。

##### 1 つの文字列属性 Segment ごとに 1 つの属性両方 {#both-3}

mParticle は、1 つの文字列アトリビュートとSegment ごとに 1 つの属性ビュートの両方の記述に従って属性を送信します。

##### 1 つの配列属性、1 つの文字列属性、およびSegment ごとに 1 つの属性 {#multi}

mParticle は、1 つの配列アトリビュート、1 つの文字列属性、Segment ごとに 1 つの属性ビュートの説明に従って属性を送信します。

#### ステップ1:mParticle でオーディエンス作成する {#send_settings}

mParticle でオーディエンス作成するには:

1. \[**オーディエンス**] > \[**単一ワークスペース**] > \[**\+ 新規オーディエンス**] に移動します。
2. Braze をオーディエンスアウトプットとして接続するには、次のフィールドを指定する必要があります。

| \[フィールド名]               | 説明                                                                                                                                                                   |
| ------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API キー                  | Braze ダッシュボードの **\[設定] > \[****API キー**] にあります。<br><br>古いナビゲーションを使用している場合は、**開発者コンソール** > API **設定で API** キーを確認できます。 |
| API キーオペレーティングシステム | Braze API キーが対応するオペレーティングシステムを選択してください。この選択により、オーディエンス更新時に転送されるプッシュトークンの種類が制限されます。                          |
| セグメントを別名で送信         | オーディエンスをBrazeに送る方法。詳細については、「[オーディエンスの転送](#forwarding-audiences)」セクションを参照してください。                                                          |
| ワークスペース REST API キー   | 完全な権限を持つBraze REST APIキー。これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。                                                        |
| 外部 ID タイプ   | Braze に外部 ID として転送する mParticle ユーザー ID タイプ。これはデフォルト値のカスタマー ID のままにしておくことをお勧めします。                                          |
| 電子メール ID タイプ      | Braze にメールとして転送する mParticle ユーザー ID タイプ。                                                                                                            |
| Brazeインスタンス           | Braze データを転送するクラスターを指定します。                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2}

{:start="3"}
3\.最後に、オーディエンス**救ってください**。

数分以内にオーディエンスが Braze と同期し始めるはずです。オーディエンスメンバーシップは、を持つユーザー`external_ids`（つまり、匿名ユーザーではない）についてのみ更新。[Braze mParticle オーディエンス作成について詳しくは、mParticle ドキュメントの「環境設定」を参照してください。](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings)

#### ステップ2:Braze のセグメントユーザー

Braze でこれらのユーザーのセグメントを作成するには、「**エンゲージメント**」の下の「Segment」に移動し、**セグメントに名前を付けます**。以下に、「**セグメントを送信」で選択したオプションに応じて、セグメントの例を** 2 つ示します。各オプションの詳細については、「[オーディエンスの転送](#forwarding-audiences.)」を参照してください。

- **単一配列属性:**`SegmentMembershipArray`フィルターとして選択してください。次に、「値を含む」オプションを使用して、目的のオーディエンスIDを入力します。![mParticle セグメントフィルター「SegmentMembershipArray」が「値を含む」とオーディエンス ID に設定されました。][11]<br><br>
- **Segment ごとに 1 つの属性:**カスタム属性フィルターとして選択します。次に、「equals」オプションを使用して適切なロジックを選択します。![mParticle Segment フィルター「あり得るパリジャン」が「等しい」と「真」に設定されました。][8]

保存したら、キャンバスまたはキャンペーン作成時に「ユーザーをターゲットにする」ステップでこのSegment を参照できます。

#### 接続の無効化と削除

mParticleはBrazeでセグメントを直接管理しないため、対応するmParticleオーディエンス接続が削除または非アクティブになってもセグメントは削除されません。この場合、mParticleはBrazeのオーディエンスユーザー属性を更新して各ユーザーからオーディエンス削除しません。

削除する前に Braze ユーザーからオーディエンスを削除するには、オーディエンスを削除する前に、オーディエンスフィルターを調整してオーディエンスサイズを強制的に 0 にします。オーディエンススの計算が完了して 0 人のユーザーが返されたら、オーディエンス削除します。その後、オーディエンスメンバーシップはBrazeで単一属性オプション更新されるか、オーディエンスIDが配列形式から削除されます。`false`

## データマッピング

モバイルアプリやウェブアプリをmParticle経由でBrazeに接続したい場合は、[組み込みキット統合を使用してデータをBrazeにマッピングできます](#embedded-kit-integration)。サーバー間 [API 統合を使用して、サーバー側のデータを](#server-api-integration) Braze に転送することもできます。

どちらの方法を選択する場合でも、Braze を出力として設定する必要があります。

### Braze 出力設定を構成してください

mParticle で、\[**設定] > \[出力] > \[出力の追加**] に移動し、\[**Braze] を選択して Braze** キット設定開封。**完了したら保存します**。

| 設定名 | 説明 |
| ------------ | ----------- |
| Braze アプリ識別子キー | Braze アプリ識別子キーは、Braze ダッシュボードの **\[設定] > \[****API** キー] にあります。API キーはプラットフォーム (iOS、Android、Web) ごとに異なることに注意してください。 |
| 外部 ID タイプ | Braze に外部 ID として転送する mParticle ユーザー ID タイプ。これはデフォルト値のカスタマー ID のままにしておくことをお勧めします。 |
| 電子メール ID タイプ | Braze にメールとして転送する mParticle ユーザー ID タイプ。これはデフォルト値の \[電子メール] のままにしておくことをお勧めします。 |
| Brazeインスタンス | Braze データが転送されるクラスターは、ダッシュボードが置かれているクラスターと同じである必要があります。 |
| イベントストリーム転送を有効にする | (サーバー間) 有効にすると、すべてのイベントがリアルタイムで転送されます。そうでない場合は、すべてのイベントが一括転送されます。イベントストリーム転送を有効にする場合は、Braze [に渡すデータがレート制限に従うようにしてください]({{site.baseurl}}/api/basics/#api-limits)。 |
{: .reset-td-br-1 .reset-td-br-2}

![][10]

### 組み込みキット統合

mParticleとBraze SDKは、組み込みキットの統合を通じてアプリケーションに表示されます。ただし、Braze を直接統合する場合とは異なり、mParticle が Braze SDK メソッドの大半の呼び出しを代行してくれます。ユーザーデータ追跡に使用する mParticle メソッドは、自動的に Braze の SDK メソッドにマップされます。 

[Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy)、[iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy)、[Web](https://github.com/Appboy/integration-appboy) 用のmParticleのSDK Kのこれらのマッピングは開封であり、[mParticleのGitHubページにあります](https://github.com/mparticle-integrations)。 

組み込みキットSDKとの統合により、当社の全機能（プッシュ、アプリ内メッセージ、および関連するすべてのメッセージ分析トラッキング, 追跡）を活用できます。

{% alert note %}
コンテンツカードとカスタムのアプリ内メッセージ統合については、Braze SDK メソッドを直接呼び出します。
{% endalert %}

#### ステップ1:mParticle SDK のインテグレーション

プラットフォームニーズに応じて、適切な mParticle SDK をアプリに統合してください。

* [Android 用mParticle](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [iOS 用マパーティクル](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [Web 用 mParticle](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### ステップ2:mParticleのBraze イベントキットの完全統合

この mParticle 統合では、Braze SDK をWeb サイトやアプリに直接組み込む必要はありませんが、アプリから Braze にデータを転送するには、次の mParticle Appboy Kit をインストールする必要があります。

[mParticleのBrazeイベントキット統合ガイドでは](https://docs.mparticle.com/integrations/braze/event/#kit-integration)、メッセージングのニーズ（プッシュ、ロケーショントラッキングなど）に基づいて、mParticleとBrazeのカスタムアライメント手順を順を追って説明します。

#### ステップ3:Braze 出力の接続設定

mParticle で、\[接続] **> \[接続] > \[目的のプラットフォーム] > \[出力の接続] に移動して、Braze を出力として追加します**。**完了したら保存します**。

![][3]

すべての接続設定がすべてのプラットフォームと統合タイプに適用されるわけではありません。接続設定とそれが適用されるプラットフォームの詳細は、[mParticle のドキュメントを参照してください](https://docs.mparticle.com/integrations/braze/event/#connection-settings)。

### サーバー API 統合

これは、サーバーサイドのSDK（Ruby、Pythonなど）'re using mParticle'を使用している場合に、バックエンドデータをBrazeにルーティングするためのアドオンです。Braze とのこのサーバー間統合を設定するには、[mParticle](https://docs.mparticle.com/guides/platform-guide/connections/) のドキュメントに従ってください。

{% alert important %}
サーバー間統合では、アプリ内メッセージング、コンテンツカード、プッシュ通知などの Braze UI 機能はサポートされません。また、この方法では利用できないデバイスレベルのフィールドなど、自動的にキャプチャされたデータもあります。 

これらの機能を使用する場合は、サイドバイサイド統合を検討してください。

サーバー側のデータを Braze に転送するには、それを含める必要があります`external_id`。匿名ユーザーは転送されません。
{% endalert %}

#### Braze 出力の接続設定

mParticle で、\[接続] **> \[接続] > \[目的のプラットフォーム] > \[出力の接続] に移動して、Braze を出力として追加します**。**完了したら保存します**。 

![][4]

すべての接続設定がすべてのプラットフォームと統合タイプに適用されるわけではありません。接続設定とそれが適用されるプラットフォームの詳細は、[mParticle のドキュメントを参照してください](https://docs.mparticle.com/integrations/braze/event/#connection-settings)。

「強化されたユーザー属性」または「強化されたユーザーアイデンティティ」を有効にする前に、[データポイントの超過を確認して、これらの設定がデータポイント使用量](#potential-data-point-overages)にどのように影響するかを確認することをお勧めします。

### データマッピングの詳細

#### データタイプ
すべてのデータタイプが両方のプラットフォームでサポートされているわけではありません。
- [カスタムイベントプロパティは]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)、文字列、数値、boolean、または日付オブジェクトをサポートします。配列やネストされたオブジェクトはサポートしていません。
- [カスタム属性は]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/)、文字列、数値、ブール値、日付オブジェクト、配列をサポートしますが、オブジェクトやネストされたオブジェクトはサポートしません。 

{% alert note %}
Brazeは、`Time`タイプカスタム属性の0年前または3000年以降のタイムスタンプをサポートしていません。Braze は mParticle から送信された値を取り込みますが、値は文字列として保存されます。
{% endalert %}

#### データマッピング

| mParticle データタイプ | Braze データタイプ | 説明 |
| ------------------- | --------------- | ----------- |
| ユーザー属性 (予約済み) | 標準属性項目 | たとえば、mParticle `$FirstName` の予約済みユーザー属性キーは Braze `first_name` の標準属性項目フィールドマップされます。 |
| ユーザー属性 (その他) | カスタム属性 | mParticle に渡されたユーザー属性のうち、予約されているユーザー属性キーの範囲外のものはすべて、カスタム属性として Braze に記録されます。<br><br>ユーザー属性は、文字列、数値、ブール値、日付、配列をサポートしますが、オブジェクトやネストされたオブジェクトはサポートしません。 |
| カスタムイベント | カスタムイベント | mParticle カスタムイベントは Braze によってカスタムイベントとして認識されます。イベント属性はカスタムイベントプロパティとして転送されます。<br><br>イベントプロパティとして Braze に渡されるイベント属性は、文字列、数値、boolean、または日付オブジェクトをサポートしますが、配列やネストされたオブジェクトはサポートしません。 |
| 購入コマースイベント | 購入イベント | 購入コマースイベントは Braze 購入イベントにマッピングされます。<br><br>バンドルコマースイベントデータの設定値を、注文レベルまたは商品レベルで購入を記録するように切り替えます。たとえば、2 つのユニークな商品`false`、プロモーション、インプレッションを含む 1 つのイベントが、少なくとも 2 つの Braze イベントが発生したとします。に設定すると`true`、商品、プロモーション、インプレッションの配列がそれぞれネストされた単一の送信イベントになります。<br><br>ログに記録されるその他の商取引分野の詳細については、[mParticle のドキュメントを参照してください](https://docs.mparticle.com/integrations/braze/event/#purchase-events)。<br><br>`false`購入イベントプロパティとしてBrazeに渡される商品属性として「バンドルコマースイベントデータ」設定する場合、文字列、数値、boolean、または日付オブジェクトはサポートされますが、配列やネストされたオブジェクトはサポートされません。|
| その他すべてのコマースイベント | カスタムイベント | 他のすべてのコマースイベントはカスタムイベントにマップされます。<br><br>バンドルコマースイベントデータの設定値を、注文レベルまたは商品レベルで購入を記録するように切り替えます。たとえば、2 つのユニークな商品`false`、プロモーション、インプレッションを含む 1 つのイベントが、少なくとも 2 つの Braze イベントが発生したとします。に設定すると`true`、商品、プロモーション、インプレッションの配列がそれぞれネストされた単一の送信イベントになります。<br><br>特定のデフォルトコマース値に加えて、製品属性は Braze イベントプロパティとして記録されます。ログに記録されるその他の商取引分野の詳細については、[mParticle のドキュメントを参照してください](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events)。<br><br>イベントプロパティとして Braze `false` に渡される製品属性として「バンドルコマースイベントデータ」設定する場合、文字列、数値、boolean、または日付オブジェクトはサポートされますが、配列やネストされたオブジェクトはサポートされません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### ユーザ ID マッピング
mParticle の出力ごとに、Braze に送信する外部 ID タイプをとして選択できます。`external_id`デフォルト値は顧客 ID ですが、など`MPID`、別の ID をマッピングして Braze に送信することもできます。`external_id`顧客 ID 以外の ID を選択すると、Braze でのデータの送信方法に影響する可能性があることに注意してください。 

たとえば、`external_id` MPIDをBrazeにマッピングすると、次のような効果があります。
- MPID が割り当てられるタイミングの性質上、`external_id`すべてのユーザーにオンセッション開始が割り当てられます。
- Currents 設定では、MPIDとではデータタイプが異なるため、追加のマッピングが必要になる場合があります。`external_id`

### 消去要求 (データ主体要求) の転送

Braze へのデータ主体リクエスト出力を設定して、消去リクエストを Braze に転送します。消去リクエストを Braze に転送するには、[mParticle](https://docs.mparticle.com/integrations/braze/forwarding-dsr/) のドキュメントに従ってください。

## データポイント超過の可能性

### 強化されたユーザー属性

#### ユーザー属性/アイデンティティのエンリッチを有効にする (サーバー間のみ) {#enriched}

mParticle 接続設定で、Braze は「**強化されたユーザー属性を含める**」をオフにすることを推奨しています。有効にすると、mParticleは記録されたイベントごとに、使用可能なすべてのユーザー属性（標準属性、カスタム属性、計算属性など）を既存のプロファイルからBrazeに転送します。mParticleは呼び出しのたびに同じ属性を変更せずにBrazeに送信するため、データポイントの消費量が多くなります。

たとえば、ユーザー最初のセッションで名前、姓、電話番号を追加し、後でメールに加えて同じ情報を追加してニュースレターにサインアップすると、ニュースレターの登録イベントがトリガーされます。
- オン (デフォルト) にすると、5 つのデータポイントが生成されます。(登録イベント、メールアドレス、名、苗字、電話番号)
- オフにすると、2 つのデータポイント (登録イベントとメールアドレス) が発生します

{% alert note %}
この設定をオフにすると、元のインバウンドバッチで受信されなかったり、イベントの属性として明示的に設定されなかったりしたプロファイル優先されます。't check for changing data. It will, however, prevent the integration from sending all user attributes on the user'それでもデルタだけがBrazeに渡されることを確認することが重要です。
{% endalert %}

#### エンリッチされたユーザー属性を無効にする場合の考慮事項

「**エンリッチされたユーザー属性を含める**」をオフにする場合に注意すべき点がいくつかあります。
1. サーバー間インテグレーションでは、mParticle イベント API を使用してイベントを Braze に送信します。各リクエストはイベントによってトリガーされます。メールアドレスの更新などのユーザー属性が変更されたが、特定のイベント（プロファイル更新カスタムイベントなど）に関連付けられていない場合、新しい値は、ユーザートリガーした次のイベントのペイロードで「強化属性」としてBrazeなどの出力にのみ渡されます。「**強化されたユーザー属性を含める**」をオフにすると、特定のイベントに関連付けられていないこの新しい属性値は Braze に渡されません。
  - これを解決するには、更新された特定のユーザー属性のみを Braze に送信する「ユーザー属性更新」イベントを別途作成することをお勧めします。この方法では、「ユーザー属性更新」イベント用の追加データポイントをログに記録しますが、この機能を有効にした呼び出しごとにすべてのユーザー属性を送信するよりも、データポイント消費量がはるかに少なくなることに注意してください。
2. 計算された属性はエンリッチされたユーザー属性としてBrazeに渡されるため、「エンリッチされたユーザー属性」がオフになっていると、これらはBrazeに渡されなくなります。「強化されたユーザー属性」がオフのときに計算された属性をBrazeに転送するには、[計算された属性フィード](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed)がすべての属性をプッシュしなくても役立つ場合があります。計算された属性変更されると、フィードはBrazeのダウンストリームで更新を開始します。 

### 不要なデータや重複したデータを Braze に送信する
Braze は、値が変更されていなくても、属性が Braze に渡されるたびにデータポイントをカウントします。このため、Brazeでは、アクションに必要なデータのみをBraze内で転送し、属性のデルタのみが渡されるようにすることを推奨しています。

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
[5]: \#embedded-キットインテグレーション
