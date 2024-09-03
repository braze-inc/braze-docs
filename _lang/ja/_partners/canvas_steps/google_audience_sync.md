---
nav_title: グーグル
article_title: キャンバス オーディエンス Googleに同期
alias: /google_audience_sync/
description: "このリファレンス記事では、Brazeオーディエンス同期をGoogleに使用して、行動トリガー、セグメンテーションなどに基づいて広告を配信する方法について説明します。"
Tool:
  - Canvas
page_order: 2

---

# オーディエンスをGoogleに同期する

{% alert important %}
Googleは、2024年3月6日から施行される[デジタル市場法（DMA）](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)の変更に対応して、[EUユーザー同意ポリシー](https://www.google.com/about/company/user-consent-policy/)を更新しています。この新しい変更により、広告主はEEAおよび英国のエンドユーザーに特定の情報を開示し、必要な同意を得る必要があります。次のドキュメントを確認して、詳細を学んでください。
{% endalert %}

Brazeオーディエンス同期をGoogle統合により、ブランドはクロスチャネルの顧客ジャーニーのリーチをGoogle検索、Googleショッピング、Gmail、YouTube、およびGoogleディスプレイに拡張できます。最初のパーティーの顧客データを使用して、ダイナミックな行動トリガー、セグメンテーションなどに基づいて安全に広告を配信できます。Braze キャンバスの一部としてメッセージ（例えば、プッシュ、メール、またはSMS）をトリガーするために通常使用する任意の基準を使用して、Googleの[顧客マッチ](https://support.google.com/google-ads/answer/6379332?hl=en)を介してそのユーザーに広告をトリガーすることができます。

{% alert important %}
2023年5月1日より、Google 広告はターゲティングおよびレポートのために「類似オーディエンス」（「類似オーディエンス」とも呼ばれる）を生成しなくなります。[Google 広告ドキュメント](https://support.google.com/google-ads/answer/12463119?)を参照して詳細を確認してください。
{% endalert %}

カスタムオーディエンスの同期の一般的な使用例には以下が含まれます：
- 複数のチャネルを介して高価値ユーザーをターゲットにして、購入またはエンゲージメントを促進します。
- 他のマーケティングチャネルに対してレスポンシブでないユーザーをリターゲティングする。
- ブランドの忠実な消費者である場合に、ユーザーが広告を受け取らないようにするための抑制オーディエンスの作成。

{% alert note %}
この機能により、ブランドはどの特定のファーストパーティデータをGoogleと共有するかをコントロールできます。Brazeでは、ファーストパーティデータを共有できる統合と共有できない統合が最優先で考慮されます。Brazeのデータプライバシーポリシーの詳細については、[こちら](https://www.braze.com/privacy)をクリックしてください。
{% endalert %}

## 前提条件

キャンバスでGoogle オーディエンスのステップを設定する前に、次の項目が作成され、完了していることを確認する必要があります。

| 要件 | Origin | 説明 |
| ----------- | ------ | ----------- |
| Google 広告アカウント | [グーグル](https://support.google.com/google-ads/answer/6366720?hl=en) | あなたのブランドのためのアクティブなGoogle 広告アカウント。<br><br>複数の管理アカウントにオーディエンスを共有したい場合は、オーディエンスを[マネージャーアカウント](https://support.google.com/google-ads/answer/6139186)にアップロードできます。 |
| Google 広告規約とGoogle 広告ポリシー | [グーグル](https://support.google.com/adspolicy/answer/54818?hl=en) | Braze Audience Syncを使用するにあたり、[Googleの広告利用規約](https://payments.google.com/u/0/paymentsinfofinder?hostOrigin=aHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tOjQ0Mw..&sri=-40)および[Googleの広告ポリシー](https://support.google.com/adspolicy/answer/6008942?sjid=15557182366992806023-NC)、該当する場合には[EUユーザー同意ポリシー](https://www.google.com/about/company/user-consent-policy/)を受け入れ、遵守する必要があります。<br><br>Google の新しい EU ユーザー同意ポリシーについて法務チームに相談し、EEA/英国のエンドユーザーに Google 広告のサービスを利用するために適切な同意を得ていることを確認してください。 |
| Google 顧客 Match | [グーグル](https://support.google.com/google-ads/answer/6299717) |  顧客マッチはすべての広告主に利用できるわけではありません。<br><br>**顧客マッチを使用するには、アカウントに以下が必要です:**<br>• ポリシー遵守の良い歴史<br>• 良好な支払い履歴<br>• Google 広告での少なくとも90日の履歴<br>• 生涯総支出が50,000米ドルを超える。USD以外の通貨で管理されている広告主の場合、支出額はその通貨の月平均コンバージョンレートを使用してUSDに変換されます。<br><br>お客様のアカウントがこれらの基準を満たしていない場合、お客様のアカウントは現在、顧客マッチを使用する資格がありません。<br><br>Google 広告担当者に連絡して、アカウントの顧客マッチの利用可能性について詳しく確認してください。 |
| Googleの同意シグナル | [グーグル](https://support.google.com/google-ads/answer/14310715) |  EEAのエンドユーザーにGoogleの顧客マッチサービスを使用して広告を配信したい場合、GoogleのEUユーザー同意ポリシーの一環として、次のカスタム属性（ブール値）をBrazeに渡す必要があります。詳細については、[EEAおよび英国のエンドユーザーの同意を収集する](#collecting-consent-for-eea-and-uk-end-users)の下にあります。<br> `$google_ad_user_data`<br> - `$google_ad_personalization` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Braze SDKを使用して同意シグナルを収集する場合、次の最低バージョンを満たしていることを確認してください:

{% sdk_min_versions swift:7.6.0 android:1.3.2 web:3.0.0 %}

### EEAおよび英国のエンドユーザーの同意を収集する

Google の EU ユーザー同意ポリシーは、広告主が EEA および 英国 のエンドユーザーに対して以下を開示し、同意を得ることを要求しています。

* クッキーやその他のローカルストレージの使用（法的に必要な場合）; そして
* 広告のパーソナライゼーションのための個人データの収集、共有、および使用。

これは、米国のエンドユーザーやEEAまたは英国以外に所在する他のエンドユーザーには影響しません。Google の新しい EU ユーザー同意ポリシーについて法務チームに相談し、EEA および英国のエンドユーザーに Google 広告のサービスを利用するために適切な同意を収集していることを確認してください。

2024年3月6日から施行されるデジタル市場法（DMA）の要件に基づき、広告主はGoogleとデータを共有する際に、EEAのエンドユーザー（英国を除く）の同意を得る必要があります。この変更の一環として、次のブール値カスタム属性としてBrazeで両方の同意シグナルを収集できます:

* `$google_ad_user_data`
* `$google_ad_personalization`

Braze は、これらのカスタム属性からのデータを適切な [Google の同意フィールド](https://support.google.com/google-ads/answer/14310715#:~:text=These%20consent%20fields%20are%3A) に同期します。

#### 同意の取り消しの管理

EEAのエンドユーザーがオーディエンスリストに追加され、その後2つの同意のいずれか（`$google_ad_user_data` または `$google_ad_personalization`）を撤回した場合に、オーディエンスリストを最新の状態に保つために、キャンバスを設定して、オーディエンス同期ステップを使用して既存のオーディエンスリストからユーザーを削除する必要があります。

{% alert note %}
EEA が以前に両方のシグナルに対して同意を提供していた場合、そのデータはそのリストの有効期限が切れるまで、またはその同意ステータスが Google Audience Sync を介して明示的に更新されるまで、またはその両方が行われるまで、Google の顧客マッチに使用され続けます。
{% endalert %}

#### ヒント

* 値をブール型として送信し、文字列型として送信しないでください。
* 属性名の前にドル記号（$）を付けます。Brazeは、属性名の先頭にドル記号を使用して、これが特別で予約されたキーであることを示します。
* 属性名を小文字で入力してください。
* 明示的にユーザーを未指定として設定することはできませんが、`null`または`nil`の値、または`true`または`false`でない任意の値を送信すると、Brazeはこのユーザーを`UNSPECIFIED`としてGoogleに渡します。
* 新しいユーザーが追加または更新され、いずれかの同意属性が指定されていない場合、それらの同意属性が未指定としてマークされてGoogleと同期されます。

必要な同意フィールドと付与されたステータスなしでEEAユーザーを同期しようとすると、Googleはこれを拒否し、このエンドユーザーに広告を配信しません。さらに、EEAユーザーに明示的な同意なしに広告が配信された場合、あなたは責任を負う可能性があり、財政的なリスクにさらされる可能性があります。顧客マッチアップロードパートナー向けのEUユーザー同意ポリシーの詳細については、Googleの[FAQ](https://support.google.com/google-ads/answer/14310715)をご覧ください。 

## 統合

### ステップ1:Googleアカウントを接続する

開始するには、**パートナー統合** > **テクノロジーパートナー** > **Google 広告** に移動し、**Google 広告を接続** を選択します。次に、Google 広告アカウントに関連付けられたメールを選択し、Braze に Google 広告アカウントへのアクセスを許可するためのモーダルが表示されます。

{% alert note %}
古いナビゲーションを使用している場合は、統合の下にテクノロジーパートナーを見つけることができます。
{% endalert %}

Google 広告アカウントの接続に成功すると、Google 広告パートナーページに戻ります。次に、Brazeワークスペース内でアクセスしたい広告アカウントを選択するように求められます。

![]({% image_buster /assets/img/google_sync/googlesync.gif %}){: style="max-width:85%;"}

{% alert important %}
オーディエンス同期内でiOS IDFAまたはGoogle広告IDをエクスポートする予定がある場合、Googleはリクエスト内にiOSアプリIDおよびAndroidアプリIDを要求します。Google オーディエンス同期モジュール内で、**モバイル広告IDを追加**を選択し、iOSアプリIDとAndroidアプリID（アプリパッケージ名）を入力して、それぞれ保存します。
<br><br>
![更新されたGoogle 広告技術ページには、接続された広告アカウントが表示され、アカウントの再同期やモバイル広告IDの追加が可能です。]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
{% endalert %}

### ステップ2:キャンバスフローにGoogle オーディエンスステップを追加

キャンバスにコンポーネントを追加し、**オーディエンス同期**を選択します。

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### ステップ3:同期設定

**カスタムオーディエンス** ボタンをクリックして、コンポーネントエディタを開封します。

希望するオーディエンス同期パートナーとして**Google**を選択します。

![][19]{: style="max-width:80%;"}

希望するGoogle広告アカウントを選択してください。**新しいまたは既存のオーディエンスを選択**ドロップダウンで、新しいまたは既存のオーディエンスの名前を入力します。 

{% tabs %}
{% tab 新しいオーディエンスを作成する %}
**新しいオーディエンスを作成**<br>
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

新しいカスタムオーディエンスの名前を入力し、**ユーザーをオーディエンスに追加**を選択し、オーディエンスに送信するファーストパーティのユーザーフィールドデータを選択します。どちらかを選ぶことができます:

- **顧客 Contact Info**:Brazeに存在する場合、ユーザーのメールまたは電話番号、またはその両方が含まれます
- **モバイル広告ID**:iOS IDFA または Android GAID のいずれかを選択してください

次に、ステップエディタの下部にある**オーディエンスを作成**ボタンをクリックしてオーディエンスを保存します。

![カスタムオーディエンスキャンバスコンポーネントの拡大ビュー。ここで、希望する広告アカウントが選択され、新しいオーディエンスが作成され、「顧客連絡先情報」チェックボックスが選択されます。]({% image_buster /assets/img/audience_sync/g_sync.png %})

ユーザーは、オーディエンスが正常に作成された場合、またはこのプロセス中にエラーが発生した場合に、ステップエディターの上部で通知されます。ユーザーは、オーディエンスが下書きモードで作成されたため、キャンバスの旅の後でユーザーの削除のためにこのオーディエンスを参照できます。 

![キャンバスコンポーネントで新しいオーディエンスが作成された後に表示されるアラートです。]({% image_buster /assets/img/audience_sync/g_sync3.png %})

新しいオーディエンスでキャンバスを起動すると、Brazeはキャンバスの起動時に新しいカスタムオーディエンスを作成し、その後、ユーザーがGoogle オーディエンスコンポーネントに入るとほぼリアルタイムで同期します。 

{% alert important %}
Google の顧客マッチ要件によると、顧客リストに顧客の連絡先情報とモバイル広告主 ID を同時に含めることはできません。Google 顧客 Match は次にこの情報を使用して、Google 検索、Google ディスプレイ、YouTube、および Gmail 内でターゲットにできる人を判断します。Google顧客マッチの要件の詳細については、彼らの[ドキュメント](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507)を確認してください。
{% endalert %}
{% endtab %}
{% tab 既存のオーディエンスと同期する %}
**既存のオーディエンスと同期する**<br>
Brazeは、これらのオーディエンスが最新であることを確認するために、既存のGoogle顧客リストからユーザーを追加または削除する機能も提供します。既存のオーディエンスと同期するには、既存のカスタムオーディエンスを選択して同期し、**オーディエンスに追加する**か**オーディエンスから削除する**かを選択します。Brazeは、ユーザーがGoogle オーディエンス ステップに入ると、ほぼリアルタイムでユーザーを追加または削除します。 

Google オーディエンス ステップを構成したら、**完了**を選択します。あなたのGoogleオーディエンスステップには、新しいオーディエンスに関する詳細が含まれます。

![カスタムオーディエンスキャンバスコンポーネントの拡大ビュー。ここで、希望する広告アカウントと既存のオーディエンスが選択され、「オーディエンスにユーザーを追加」ラジオボタンが選択されます。]({% image_buster /assets/img/audience_sync/g_sync2.png %})

{% endtab %}
{% endtabs %}

### ステップ4:キャンバスを起動

キャンバス内でユーザーの旅の残りを完了し、次に進みましょう！新しいオーディエンスを作成することを選択した場合、BrazeはGoogle内にオーディエンスを作成し、ユーザーがキャンバスのこのステップに到達すると追加します。既存のオーディエンスにユーザーを追加または削除することを選択した場合、Brazeはユーザーがユーザージャーニーのこのステップに到達したときにユーザーを追加または削除します。

ユーザーは次のコンポーネントに進みます。キャンバスがあれば、キャンバスの最後のステップでユーザーの旅が終了します。 

## ユーザーの同期とレート制限の考慮事項

ユーザーがオーディエンス同期コンポーネントに到達すると、BrazeはGoogle 広告APIのレート制限を遵守しながら、これらのユーザーをほぼリアルタイムで同期します。これが実際に意味するところは、Brazeが5秒ごとにできるだけ多くのユーザーをバッチ処理し、これらのユーザーをGoogleに送信しようとするということです。 

顧客がGoogle 広告APIのレート制限に近づくと、Googleは再試行の推奨事項に関するフィードバックをBrazeに提供します。Brazeの顧客がレート制限に達した場合、Brazeのキャンバスは同期を最大約13時間再試行します。同期が不可能な場合、これらのユーザーは「ユーザーエラー」メトリックにリストされます。

## 分析を理解する 

次の表には、オーディエンス同期ステップからの分析をよりよく理解するための指標と説明が含まれています。

| メートル法 | 説明 |
| ------ | ----------- |
| *入力済み* | このステップに入ったユーザー数をGoogleに同期します。 |
| *次のステップに進みました* | 次のコンポーネントがある場合、何人のユーザーが次のコンポーネントに進みましたか。すべてのユーザーが自動的に進行します。これがキャンバスBranchの最後のステップである場合、このメトリックは0になります。 |
| *ユーザーが同期されました* | Google に正常に同期されたユーザーの数。 |
| *ユーザー Not Synced* | 欠落しているフィールドが一致しないか、同意属性が`false`に設定されているために同期されていないユーザーの数。 |
| *ユーザーがエラーを起こしました* | エラーのためにGoogleと同期されなかったユーザーの数、約13時間の再試行後。特定のエラー、例えばGoogle 広告APIサービスの中断の場合、キャンバスは同期を最大約13時間再試行します。その時点で同期がまだ不可能な場合、*ユーザー未同期*が入力されます。 |
| *保留中のユーザー* | 現在、BrazeによってGoogleに同期されているユーザーの数。 |
| *キャンバスを終了しました* | キャンバスを終了したユーザーの数。これは、キャンバスの最後のステップがGoogleステップである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2}

## トラブルシューティング

{% details Google オーディエンス ステップ設定で複数のフィールドを選択して一致させることができないのはなぜですか？ %}
Google 顧客マッチには、これらのオーディエンスの形式や含まれる顧客情報に関して厳格な要件があります。具体的には、モバイル広告主IDは顧客の連絡先情報（メールや電話番号など）とは別にアップロードする必要があります。詳細については、[Googleの顧客マッチドキュメント](https://support.google.com/google-ads/answer/7659867?hl=en#undefined)を参照してください。
{% enddetails %}

{% details Googleでオーディエンスが同期するのにどれくらい時間がかかりますか？ %}
Googleにオーディエンスが同期されるまでに6〜12時間かかることがあります。
{% enddetails %}

{% details オーディエンスを同期しましたが、Googleのオーディエンスサイズがゼロです。 %}
プライバシーの目的で、ユーザーリストのサイズはリストに少なくとも**1,000人のメンバー**がいるまでゼロと表示されます。その後、サイズは最も重要な2桁に丸められます。
{% enddetails %}

{% details オーディエンスをGoogleに同期しましたが、広告が配信されていません。 %}
オーディエンスに少なくとも**5,000**人のユーザーが含まれていることを確認して、広告が配信され始めるようにしてください。
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
