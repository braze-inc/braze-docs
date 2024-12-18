---
nav_title: Google
article_title: キャンバス オーディエンス Googleに同期
alias: /google_audience_sync/
description: "このリファレンス記事では、Brazeオーディエンス同期をGoogleに使用して、行動トリガー、セグメンテーションなどに基づいて広告を配信する方法について説明します。"
Tool:
  - Canvas
page_order: 3

---

# オーディエンスをGoogleに同期する

{% alert important %}
Googleは、2024年3月6日から施行される[デジタル市場法（DMA）](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)の変更に対応して、[EUユーザー同意ポリシー](https://www.google.com/about/company/user-consent-policy/)を更新しています。この新しい変更により、広告主はEEA、英国、スイスのエンドユーザーに特定の情報を開示し、必要な同意を得ることが求められる。次のドキュメントを確認して、詳細を学んでください。
{% endalert %}

Braze Audience Sync to Google 統合により、ブランドは、クロスチャネルのカスタマージャーニーの範囲を Google 検索、Google ショッピング、Gmail、YouTube、および Google ディスプレイに拡大できます。ファーストパーティの顧客データを使用して、ダイナミックな行動トリガー、セグメンテーションなどに基づいて安全に広告を配信できます。Braze キャンバスの一部としてメッセージ（例えば、プッシュ、メール、またはSMS）をトリガーするために通常使用する任意の基準を使用して、Googleの[顧客マッチ](https://support.google.com/google-ads/answer/6379332?hl=en)を介してそのユーザーに広告をトリガーすることができます。

{% alert important %}
2023年5月1日以降、Google 広告は、ターゲティングおよびレポート用に「類似オーディエンス」とも呼ばれる類似性の高いオーディエンスを生成しません。[Google 広告ドキュメント](https://support.google.com/google-ads/answer/12463119?)を参照して詳細を確認してください。
{% endalert %}

**カスタムオーディエンス同期の一般的なユースケースには次のものがあります。**
- 複数のチャネルを通じて価値の高いユーザーをターゲットにして、購入やエンゲージメントを促進する。
- 他のマーケティングチャネルに対してレスポンシブでないユーザーをリターゲティングする。
- すでに自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑制オーディエンスを作成する。

{% alert note %}
この機能により、ブランドはどの特定のファーストパーティデータをGoogleと共有するかをコントロールできます。Braze では、ファーストパーティデータを共有できる統合と共有できない統合を最大限に考慮しています。Brazeのデータプライバシーポリシーの詳細については、[こちら](https://www.braze.com/privacy)をクリックしてください。
{% endalert %}

## 前提条件

キャンバスで Google オーディエンスステップを設定する前に、以下の項目が作成、完了していることを確認する必要があります。

| 要件 | 提供元 | 説明 |
| ----------- | ------ | ----------- |
| Google 広告アカウント | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | あなたのブランドのためのアクティブなGoogle 広告アカウント。<br><br>複数の管理対象アカウントでオーディエンスを共有する場合は、[マネージャーアカウント](https://support.google.com/google-ads/answer/6139186)にオーディエンスをアップロードできます。 |
| Google 広告規約とGoogle 広告ポリシー | [Google](https://support.google.com/adspolicy/answer/54818?hl=en) | Braze Audience Syncを使用するにあたり、[Googleの広告利用規約](https://payments.google.com/u/0/paymentsinfofinder?hostOrigin=aHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tOjQ0Mw..&sri=-40)および[Googleの広告ポリシー](https://support.google.com/adspolicy/answer/6008942?sjid=15557182366992806023-NC)、該当する場合には[EUユーザー同意ポリシー](https://www.google.com/about/company/user-consent-policy/)を受け入れ、遵守する必要があります。<br><br>Googleの新しいEUユーザー同意ポリシーについて法務チームと相談し、EEA、英国、スイスのエンドユーザーに対してGoogle広告のサービスを利用するために適切な同意を収集していることを確認する。 |
| Google カスタマーマッチ | [Google](https://support.google.com/google-ads/answer/6299717) |  すべての広告主がカスタマーマッチを利用できるわけではありません。<br><br>**カスタマーマッチを使用するには、アカウントが以下の条件を満たしている必要があります。**<br>• これまでポリシーを遵守してきた実績があること<br>• これまで支払いに関して問題が発生していないこと<br>• Google 広告で 90 日以上の利用実績があること<br>• 利用金額が通算5万米ドルを超えていること米ドル以外の通貨でアカウントを管理している広告主の利用金額は、その通貨の月別平均為替レートで米ドルに換算されます。<br><br>アカウントが上記の要件を満たしていない場合、現時点ではそのアカウントではカスタマーマッチを利用できません。<br><br>Google 広告の担当者に連絡して、アカウントでのカスタマーマッチの利用可能性について詳しいガイダンスを受けてください。 |
| Google の同意シグナル | [Google](https://support.google.com/google-ads/answer/14310715) |  EEAのエンドユーザーにGoogleの顧客マッチサービスを使用して広告を配信したい場合、GoogleのEUユーザー同意ポリシーの一環として、次のカスタム属性（ブール値）をBrazeに渡す必要があります。詳細は、「[EEA、英国、スイスのエンドユーザーに対する同意の収集](#collecting-consent-for-eea-uk-and-switzerland-end-users)」に記載されている：<br> - `$google_ad_user_data`<br> - `$google_ad_personalization` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Braze SDK を使用して同意シグナルを収集する場合は、以下の最小バージョン要件を満たしていることを確認します。

{% sdk_min_versions swift:7.6.0 android:1.3.2 web:3.0.0 %}

### EEA、英国、スイスのエンドユーザーに対する同意の収集

グーグルのEUユーザー同意ポリシーは、広告主に対して、EEA、英国、スイスのエンドユーザーに以下を開示し、その同意を得ることを求めている：

* 法的に義務付けられている場合の Cookie やその他のローカルストレージの使用
* 広告のパーソナライゼーションのための個人データの収集、共有、および使用。

これは米国のエンドユーザーや、EEA、英国、スイス以外の国のエンドユーザーには影響しない。Googleの新しいEUユーザー同意ポリシーについて法務チームと相談し、EEA、英国、スイスのエンドユーザーに対してGoogle広告のサービスを利用するために適切な同意を収集していることを確認する。

2024年3月6日から施行されるデジタル市場法（DMA）の要件により、広告主はグーグルとデータを共有する際、EEA、英国、スイスのエンドユーザーの同意を得なければならない。この変更の一環として、次のブール値カスタム属性としてBrazeで両方の同意シグナルを収集できます:

* `$google_ad_user_data`
* `$google_ad_personalization`

Braze は、これらのカスタム属性からのデータを適切な [Google の同意フィールド](https://support.google.com/google-ads/answer/14310715#:~:text=These%20consent%20fields%20are%3A) に同期します。

#### 同意の取り消しの管理

EEA のエンドユーザーがオーディエンスリストに追加され、その後2つの同意 (`$google_ad_user_data` または`$google_ad_personalization`) のいずれかを取り消した場合にオーディエンスリストを最新の状態に保つには、オーディエンスの同期ステップを使用して既存のオーディエンスリストからユーザーを削除するようにキャンバスを設定する必要があります。

{% alert note %}
以前に EEA のエンドユーザーから両方のシグナルへの同意が提出された場合、そのリストの有効期限を経過するか、その同意ステータスが Google オーディエンスの同期により明示的に更新されるか、あるいはこの両方に該当するまで、そのデータが Google のカスタマーマッチに引き続き利用されます。
{% endalert %}

#### ヒント

* 値をブール型として送信し、文字列型として送信しないでください。
* 属性名の前にドル記号（$）を付けます。Braze は属性名の先頭のドル記号を使用して、これが特殊な予約済みのキーであることを示します。
* 属性名を小文字で入力してください。
* ユーザーを指定なしとして明示的に設定することはできませんが、`null` 値または`nil` 値、あるいは `true` と`false` 以外の値を送信すると、Braze はこのユーザーを `UNSPECIFIED` として Google に渡します。
* 新しいユーザーが追加または更新され、いずれかの同意属性が指定されていない場合、それらの同意属性が未指定としてマークされてGoogleと同期されます。

必要な同意フィールドとステータスが付与されていないEEAユーザーを同期しようとすると、Googleはこれを拒否し、このユーザーには広告を配信しない。さらに、EEAユーザーに明示的な同意なしに広告が配信された場合、あなたは責任を負う可能性があり、財政的なリスクにさらされる可能性があります。これを避けるには、`true` Googleの同意属性を持つEEA、英国、スイスのユーザーのみを含むセグメンテーションフィルターを使ってキャンペーンを送信することをお勧めする。顧客マッチアップロードパートナー向けのEUユーザー同意ポリシーの詳細については、Googleの[FAQ](https://support.google.com/google-ads/answer/14310715)をご覧ください。

### キャンバスの設定

Brazeに同期後、以下の同意属性がユーザープロファイルおよびセグメンテーションで利用可能になる：

- `$google_ad_user_data`
- `$google_ad_personalization`

Google Audience Syncを使用してユーザーをオーディエンスに追加し、EEA、英国、およびスイスのエンドユーザーをターゲットにしているキャンバスでは、両方の同意属性が`true` 以外の値である場合は、これらのユーザーを除外する必要がある。これは、同意値が`true` に設定されているときに、これらのユーザーをセグメンテーションすることで達成できる。また、Googleがこれらのユーザーをオーディエンスから拒否することがわかっているため、より正確なユーザー分析が同期される。オーディエンスからユーザーを削除するためにGoogle Audience Syncを使用している場合、同意属性は必要ないことに注意すること。

## 統合

### ステップ1:Googleアカウントを接続する

開始するには、**パートナー統合** > **テクノロジーパートナー** > **Google 広告** に移動し、**Google 広告を接続** を選択します。その後モーダルが表示され、Google 広告アカウントに関連付けられているメールを選択し、Google 広告アカウントに Braze アクセスを付与することが促されます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、[**テクノロジーパートナー**] は [**統合**] にあります。
{% endalert %}

Google 広告アカウントに接続したら、Google 広告パートナーページが再び表示されます。次に、Brazeワークスペース内でアクセスしたい広告アカウントを選択するように求められます。

![]({% image_buster /assets/img/google_sync/googlesync.gif %}){: style="max-width:85%;"}

{% alert important %}
オーディエンス同期内でiOS IDFAまたはGoogle広告IDをエクスポートする予定がある場合、Googleはリクエスト内にiOSアプリIDおよびAndroidアプリIDを要求します。Google Audience Syncで、**Add Mobile Advertising IDsを**選択し、iOSアプリIDとAndroidアプリID（アプリパッケージ名）を入力し、それぞれ保存する。
<br><br>
![更新されたGoogle 広告技術ページには、接続された広告アカウントが表示され、アカウントの再同期やモバイル広告IDの追加が可能です。]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
{% endalert %}

### ステップ2:キャンバスフローに Google オーディエンスステップを追加する

キャンバスにコンポーネントを追加し、[**オーディエンスの同期**] を選択します。

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### ステップ3:同期セットアップ

[**カスタムオーディエンス**] ボタンをクリックしてコンポーネントエディターを開きます。

希望するオーディエンス同期パートナーとして**Google**を選択します。

![][19]{: style="max-width:80%;"}

希望するGoogle広告アカウントを選択してください。[**新規または既存のオーディエンスを選択**] ドロップダウンで、新しいオーディエンスまたは既存のオーディエンスの名前を入力します。 

{% tabs %}
{% tab 新規オーディエンスの作成 %}
**新規オーディエンスの作成**<br>
新しいカスタムオーディエンスの名前を入力し、**ユーザーをオーディエンスに追加**を選択し、Googleと同期したいフィールドを選択します。Googleと同期するために一致させるフィールドを選択できます:

- メール 
- 電話
- 名/姓
- 市区町村
- 国
- 生年月日
- 性別
- モバイル広告ID
  - Braze SDKを通じて[IDFA]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection)または[GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection#google-advertising-id-android-only)の収集にオプトインする必要があります。

新しいカスタムオーディエンスの名前を入力し、[**ユーザーをオーディエンスに追加**] を選択し、オーディエンスに送信するファーストパーティユーザーフィールドデータを選択します。次のいずれかを選択できます。

- **お客様の連絡先情報**:Brazeに存在する場合、ユーザーのメールまたは電話番号、またはその両方が含まれます
- **モバイル広告主 ID**:iOS IDFA または Android GAID のいずれかを選択してください

次に、ステップエディタの下部にある**オーディエンスを作成**ボタンをクリックしてオーディエンスを保存します。

![カスタムオーディエンスキャンバスコンポーネントの展開ビュー。目的の広告アカウントが選択され、新しいオーディエンスが作成され、「お客様の連絡先情報」チェックボックスが選択されている。]({% image_buster /assets/img/audience_sync/g_sync.png %})

ユーザーは、オーディエンスが正常に作成された場合、またはこのプロセス中にエラーが発生した場合に、ステップエディターの上部で通知されます。ユーザーは、後でキャンバスジャーニーでユーザーを削除するためにこのオーディエンスを参照することができます。これは、オーディエンスが下書きで作成されたためです。 

![キャンバスコンポーネントで新しいオーディエンスが作成された後に表示されるアラート。]({% image_buster /assets/img/audience_sync/g_sync3.png %})

新しいオーディエンスを使用してキャンバスを起動すると、Braze はキャンバスの起動時にカスタムオーディエンスを作成し、その後、オーディエンスが Google オーディエンスの同期ステップに入るたびに、ほぼリアルタイムでユーザーが同期されます。 

{% alert important %}
Google のカスタマーマッチの要件のため、顧客の連絡先情報とモバイル広告主 ID を同じ顧客リストに含めることはできません。Google カスタマーマッチはその後この情報を使用して、Google 検索、Google ディスプレイ、YouTube、Gmail でターゲットにできる人物を決定します。Google顧客マッチの要件の詳細については、彼らの[ドキュメント](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507)を確認してください。
{% endalert %}
{% endtab %}
{% tab 既存のオーディエンスと同期する %}
**既存のオーディエンスとの同期**<br>
Braze では、これらのオーディエンスが最新の状態であるようにするために、既存の Google 顧客リストからユーザーを追加または削除することもできます。既存のオーディエンスと同期するには、同期する既存のカスタムオーディエンスを選択し、[**ユーザーをオーディエンスに追加**] または [**オーディエンスからユーザーを削除**] のいずれかを選択します。Brazeは、ユーザーがGoogle オーディエンス ステップに入ると、ほぼリアルタイムでユーザーを追加または削除します。 

Google オーディエンス ステップを構成したら、**完了**を選択します。Google オーディエンスステップには、新しいオーディエンスに関する詳細情報が含まれます。

![カスタムオーディエンスキャンバスコンポーネントの展開ビュー。目的の広告アカウントと既存のオーディエンス、および「ユーザーをオーディエンスに追加」ラジオボタンが選択されている。]({% image_buster /assets/img/audience_sync/g_sync2.png %})

{% endtab %}
{% endtabs %}

### ステップ4:キャンバスを起動

キャンバス内でユーザージャーニーの残りの部分を完了し、キャンバスを起動します。新しいオーディエンスを作成することを選択した場合、Braze により Google 内にオーディエンスが作成され、キャンバスのこのステップに到達したユーザーが追加されます。既存のオーディエンスにユーザーを追加または削除することを選択した場合、Brazeはユーザーがユーザージャーニーのこのステップに到達したときにユーザーを追加または削除します。

その後、キャンバスに次のコンポーネントがある場合は、ユーザーはそのコンポーネントに進みます。ユーザージャーニーの最後のステップである場合は、キャンバスを終了します。 

## ユーザーの同期とレート制限の考慮事項

ユーザーがオーディエンス同期コンポーネントに到達すると、Braze は Google 広告 API のレート制限を尊重しながら、これらのユーザーをほぼリアルタイムで同期します。これが実際に意味するところは、Brazeが5秒ごとにできるだけ多くのユーザーをバッチ処理し、これらのユーザーをGoogleに送信しようとするということです。 

顧客が Google 広告 API のレート制限に近づいたら、Google は再試行の推奨事項に関して Braze にフィードバックを提供します。Brazeの顧客がレート制限に達した場合、Brazeのキャンバスは同期を最大約13時間再試行します。同期が不可能な場合、これらのユーザーは「ユーザーエラー」メトリックにリストされます。

## 分析を理解する 

次の表には、オーディエンス同期ステップからの分析をよりよく理解するための指標と説明が含まれています。

| 指標 | 説明 |
| ------ | ----------- |
| *入力* | Google と同期するためにこのステップに入ったユーザーの数。 |
| *次のステップに進む* | 次のコンポーネントがある場合、次のコンポーネントに進んだユーザーの数。すべてのユーザーが自動的に進みます。これがキャンバスブランチの最後のステップである場合、この指標は0になります。 |
| *ユーザーの同期* | Google に正常に同期されたユーザーの数。 |
| *同期されていないユーザー* | 欠落しているフィールドが一致しないか、同意属性が`false`に設定されているために同期されていないユーザーの数。 |
| *エラーが発生したユーザー数* | エラーのためにGoogleと同期されなかったユーザーの数、約13時間の再試行後。特定のエラー (Google 広告 API サービスの中断など) が発生すると、キャンバスは最大13時間にわたって同期を再試行します。その時点で同期がまだ不可能な場合、*ユーザー未同期*が入力されます。 |
| *保留中のユーザー* | Braze が Google と同期するために現在処理されているユーザーの数。 |
| *終了済みのキャンバス* | キャンバスを終了したユーザーの人数。これは、キャンバスの最後のステップがGoogleステップである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## トラブルシューティング

{% details Google オーディエンス ステップ設定で複数のフィールドを選択して一致させることができないのはなぜですか？ %}
Google カスタマーマッチには、このようなオーディエンスの形式と含める顧客情報に関して厳しい要件があります。具体的には、モバイル広告主 ID は、顧客の連絡先情報 (メールや電話番号など) とは別にアップロードする必要があります。詳細については、[Googleの顧客マッチドキュメント](https://support.google.com/google-ads/answer/7659867?hl=en#undefined)を参照してください。
{% enddetails %}

{% details オーディエンスが Google に同期されるまでにどのくらいの時間がかかりますか？ %}
オーディエンスが Googleに同期されるまでには6～12時間かかることがあります。
{% enddetails %}

{% details オーディエンスを同期しましたが、Google のオーディエンスサイズがゼロです。 %}
プライバシーの目的で、ユーザーリストのサイズはリストに少なくとも**1,000人のメンバー**がいるまでゼロと表示されます。その後、サイズは最も重要な2桁に丸められます。
{% enddetails %}

{% details オーディエンスをGoogleに同期しましたが、広告が配信されていません。 %}
広告が確実に配信開始されるようにするため、オーディエンスに少なくとも**5,000**人のユーザーが含まれていることを確認してください。
{% enddetails %}

{% details 「モバイルアプリIDが削除されました」エラーを解決するにはどうすればよいですか？ %}
Googleにオーディエンスを同期している場合、このエラーは、同期の一環としてモバイル識別子を同期するように選択したが、GoogleパートナーページからモバイルアプリIDを削除した場合にトリガーされます。
この問題を解決するには、iOSおよびAndroidの適切なモバイルアプリIDをGoogleパートナーページに追加したことを確認してください。
{% enddetails %}

[1]: {% image_buster /assets/img/google_sync/google_sync1.png %}
[2]: {% image_buster /assets/img/google_sync/google_sync2.png %}
[3]: {% image_buster /assets/img/google_sync/google_sync3.png %}
[4]: {% image_buster /assets/img/google_sync/google_sync4.png %}
[6]: {% image_buster /assets/img/google_sync/google_sync6.png %}
[8]: {% image_buster /assets/img/google_sync/google_sync8.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/g_sync.png %}
[22]: {% image_buster /assets/img/audience_sync/g_sync2.png %}
[23]: {% image_buster /assets/img/audience_sync/g_sync3.png %}
