---
nav_title: グーグル
article_title:キャンバスオーディエンス同期をGoogleへ
alias: /google_audience_sync/
description:この記事では、Braze Audience SyncをGoogleに使用して、行動トリガー、セグメンテーションなどに基づいて広告を配信する方法について説明します。
Tool:
  - キャンバス
page_order:2

---

# Googleにオーディエンスを同期

{% alert important %}
Googleは、2024年3月6日から施行される[EUユーザー同意ポリシー](https://www.google.com/about/company/user-consent-policy/)の変更に対応して、[デジタル市場法（DMA）](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)を更新しています。この新しい変更により、広告主は特定の情報をEEAおよび英国のエンドユーザーに開示し、必要な同意を得る必要があります。次のドキュメントを確認して、詳細を確認してください。
{% endalert %}

Braze Audience SyncからGoogleへの統合により、ブランドはクロスチャネルの顧客ジャーニーのリーチをGoogle検索、Googleショッピング、Gmail、YouTube、およびGoogleディスプレイに拡大することができます。お客様のファーストパーティデータを使用して、動的な行動トリガー、セグメンテーションなどに基づいて安全に広告を配信できます。任意の基準'd typically use to trigger a message (for example, push, email, or SMS) as part of a Braze Canvas can be used to trigger an ad to that user via Google's [Customer Match](https://support.google.com/google-ads/answer/6379332?hl=en)。

{% alert important %}
2023年5月1日から、Google 広告はターゲティングとレポートのために「類似オーディエンス」として知られる類似オーディエンスを生成しなくなります。詳細については、[Google 広告のドキュメント](https://support.google.com/google-ads/answer/12463119?)を参照してください。
{% endalert %}

**カスタムオーディエンスの同期の一般的な使用例には次のものがあります:**
- 複数のチャネルを通じて高価値ユーザーをターゲットにし、購入やエンゲージメントを促進する。
- 他のマーケティングチャネルにあまり反応しないユーザーをリターゲティングする。
- ブランドの忠実な消費者である場合に広告を受け取らないようにするための抑制オーディエンスの作成。

{% alert note %}
この機能により、ブランドはGoogleと共有する特定のファーストパーティデータを制御できます。Brazeでは、ファーストパーティデータを共有できる統合と共有できない統合が最優先で考慮されています。Brazeのデータプライバシーポリシーについて詳しく知るには、[こちら](https://www.braze.com/privacy)をクリックしてください。
{% endalert %}

## 前提条件

Google AudienceステップをCanvasに設定する前に、次の項目が作成され、完了していることを確認する必要があります。

| 要件 | 起源 | 説明 |
| ----------- | ------ | ----------- |
| Google 広告アカウント | [グーグル](https://support.google.com/google-ads/answer/6366720?hl=en) | あなたのブランドのためのアクティブなGoogle広告アカウント。<br><br>複数の管理アカウント間でオーディエンスを共有したい場合は、オーディエンスを[マネージャーアカウント](https://support.google.com/google-ads/answer/6139186)にアップロードできます。 |
| Google 広告の利用規約と Google 広告ポリシー | [グーグル](https://support.google.com/adspolicy/answer/54818?hl=en) | Braze Audience Syncを使用するにあたり、[Googleの広告利用規約](https://payments.google.com/u/0/paymentsinfofinder?hostOrigin=aHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tOjQ0Mw..&sri=-40)および[Googleの広告ポリシー](https://support.google.com/adspolicy/answer/6008942?sjid=15557182366992806023-NC)、該当する場合は[EUユーザー同意ポリシー](https://www.google.com/about/company/user-consent-policy/)を受け入れ、遵守する必要があります。<br><br>Google の新しい EU ユーザー同意ポリシーについて法務チームに相談し、EEA/UK のエンドユーザーに対して Google 広告サービスを利用するために適切な同意を得ていることを確認してください。 |
| Google カスタマーマッチ | [グーグル](https://support.google.com/google-ads/answer/6299717) |  カスタマーマッチはすべての広告主に利用できるわけではありません。<br><br>**Customer Matchを使用するには、アカウントに以下が必要です:**<br>• ポリシー遵守の良い歴史<br>• 良好な支払い履歴<br>• Google 広告で少なくとも 90 日の履歴<br>• 生涯総支出が50,000米ドルを超える。USD以外の通貨で管理されている広告主の場合、支出額はその通貨の月平均換算レートを使用してUSDに換算されます。<br><br>お客様のアカウントがこれらの基準を満たしていない場合、お客様のアカウントは現在、Customer Matchを使用する資格がありません。<br><br>Google 広告担当者に連絡して、アカウントのカスタマーマッチの利用可能性についてさらに詳しく確認してください。 |
| Google同意シグナル | [グーグル](https://support.google.com/google-ads/answer/14310715) |  Google のカスタマーマッチサービスを使用して EEA のエンドユーザーに広告を配信したい場合は、Google の EU ユーザー同意ポリシーの一環として、次のカスタム属性 (ブール値) を Braze に渡す必要があります。詳細については、[EEAおよび英国のエンドユーザーの同意の収集](#collecting-consent-for-eea-and-uk-end-users)の下にあります。<br> `$google_ad_user_data`<br> - `$google_ad_personalization` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Braze SDKを使用して同意シグナルを収集する場合、次の最低バージョンを満たしていることを確認してください:

{% sdk_min_versions swift:7.6.0 android:1.3.2 web:3.0.0 %}

### EEAおよび英国のエンドユーザーの同意を収集する

GoogleのEUユーザー同意ポリシーは、広告主がEEAおよび英国のエンドユーザーに対して以下の事項を開示し、その同意を得ることを要求しています。

* クッキーやその他のローカルストレージの使用（法的に必要な場合）；および
* 広告のパーソナライズのための個人データの収集、共有、および使用。

これは、米国のエンドユーザーやEEAまたは英国以外に所在する他のエンドユーザーには影響しません。Google の新しい EU ユーザー同意ポリシーについて法務チームに相談し、EEA および英国のエンドユーザーに対して Google 広告のサービスを利用するために適切な同意を収集していることを確認してください。

デジタル市場法（DMA）の要件が2024年3月6日から施行されるにあたり、広告主はGoogleとデータを共有する際に、EEAのエンドユーザー（英国を除く）の同意を得る必要があります。この変更の一環として、次のブール値カスタム属性としてBrazeで両方の同意シグナルを収集できます:

* `$google_ad_user_data`
* `$google_ad_personalization`

Brazeは、これらのカスタム属性からのデータをGoogleの適切な[同意フィールドに同期します](https://support.google.com/google-ads/answer/14310715#:~:text=These%20consent%20fields%20are%3A)。

#### 同意の取り消しの管理

EEAのエンドユーザーがオーディエンスリストに追加され、その後、2つの同意のいずれか（`$google_ad_user_data` または `$google_ad_personalization`）を撤回した場合に、オーディエンスリストを最新の状態に保つためには、Audience Syncステップを使用して既存のオーディエンスリストからユーザーを削除するためのCanvasを設定する必要があります。

{% alert note %}
EEA が以前に両方のシグナルに同意した場合、そのデータはそのリストの有効期限が切れるまで、または Google Audience Sync を介してその同意ステータスが明示的に更新されるまで、またはその両方が行われるまで、Google のカスタマーマッチに使用され続けます。
{% endalert %}

#### ヒント

* 値を文字列型ではなく、ブール型として送信してください。
* 属性名の前にドル記号（$）を付けます。Brazeは、特殊で予約されたキーであることを示すために、属性名の先頭にドル記号を使用します。
* 属性名を小文字で入力してください。
* 明示的にユーザーを未指定として設定することはできませんが、`null`または`nil`の値、または`true`や`false`でない任意の値を送信すると、Brazeはこのユーザーを`UNSPECIFIED`としてGoogleに渡します。
* 新しいユーザーが追加または更新され、いずれかの同意属性を指定しない場合、それらの同意属性が未指定としてマークされてGoogleに同期されます。

必要な同意フィールドと付与されたステータスなしでEEAユーザーを同期しようとすると、Googleはこれを拒否し、このエンドユーザーに広告を配信しません。さらに、EEAユーザーに明示的な同意なしに広告が配信された場合、あなたは責任を負い、財政的リスクにさらされる可能性があります。詳細については、Googleの[FAQ](https://support.google.com/google-ads/answer/14310715)をご覧ください。 

## 統合

### ステップ1:Googleアカウントに接続

開始するには、**パートナー統合** > **テクノロジーパートナー** > **Google 広告** に移動し、**Google 広告を接続** を選択します。次に、Google 広告アカウントに関連付けられているメールを選択し、Braze に Google 広告アカウントへのアクセスを許可するためのモーダルが表示されます。

{% alert note %}
古いナビゲーションを使用している場合は、統合の下にテクノロジーパートナーを見つけることができます。
{% endalert %}

Google 広告アカウントの接続に成功すると、Google 広告パートナーページに戻ります。次に、Brazeワークスペース内でアクセスしたい広告アカウントを選択するように求められます。

![\]({% image_buster /assets/img/google_sync/googlesync.gif %}){: style="max-width:85%;"}

{% alert important %}
オーディエンス同期内でiOS IDFAまたはGoogle広告IDをエクスポートする予定がある場合、Googleはリクエスト内にiOSアプリIDとAndroidアプリIDを必要とします。Google Audience Syncモジュール内で、**モバイル広告IDを追加**を選択し、iOSアプリIDとAndroidアプリID（アプリパッケージ名）を入力して、それぞれ保存します。
<br><br>
![The updated Google Ads technology page showing the Ad accounts connected, allowing you to re-sync accounts and add mobile advertising IDs.]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
{% endalert %}

### ステップ2:キャンバスフローにGoogleオーディエンスステップを追加

キャンバスにコンポーネントを追加し、**Audience Sync**を選択します。

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### ステップ3:同期セットアップ

**カスタムオーディエンス**ボタンをクリックして、コンポーネントエディタを開きます。

**Google**を希望するオーディエンス同期パートナーとして選択します。

![][19]{: style="max-width:80%;"}

希望するGoogle広告アカウントを選択してください。「**新しいオーディエンスまたは既存のオーディエンスを選択**」ドロップダウンで、新しいオーディエンスまたは既存のオーディエンスの名前を入力します。 

{% tabs %}
{% tab Create a New Audience %}
**新しいオーディエンスを作成する**<br>
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

新しいカスタムオーディエンスの名前を入力し、**ユーザーをオーディエンスに追加**を選択し、オーディエンスに送信するファーストパーティユーザーフィールドデータを選択します。どちらかを選ぶことができます:

- **顧客連絡先情報**:Brazeに存在する場合、ユーザーのメールアドレスまたは電話番号、またはその両方が含まれます
- **モバイル広告ID**:iOS IDFAまたはAndroid GAIDのいずれかを選択してください

次に、ステップエディターの下部にある**オーディエンスを作成**ボタンをクリックして、オーディエンスを保存します。

![Expanded view of the Custom Audience Canvas component. Here, the desired Ad account is selected, a new audience is created, and the "customer contact info" checkbox is selected.]({% image_buster /assets/img/audience_sync/g_sync.png %})

ユーザーは、オーディエンスが正常に作成された場合、またはこのプロセス中にエラーが発生した場合に、ステップエディターの上部で通知されます。ユーザーは、このオーディエンスをキャンバスジャーニーで後でユーザー削除のために参照できます。なぜなら、このオーディエンスはドラフトモードで作成されたからです。 

![An alert that appears after a new audience is created in the Canvas component.]({% image_buster /assets/img/audience_sync/g_sync3.png %})

新しいオーディエンスでキャンバスを起動すると、Brazeはキャンバスの起動時に新しいカスタムオーディエンスを作成し、その後、ユーザーがGoogleオーディエンスコンポーネントに入るとほぼリアルタイムで同期します。 

{% alert important %}
Google のカスタマーマッチの要件により、顧客リストに顧客の連絡先情報とモバイル広告主 ID を同時に含めることはできません。Google カスタマーマッチは、この情報を使用して、Google 検索、Google ディスプレイ、YouTube、および Gmail 内でターゲットにできる人を特定します。詳細については、Google カスタマーマッチの要件に関する[ドキュメント](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507)を確認してください。
{% endalert %}
{% endtab %}
{% tab Sync with an Existing Audience %}
**既存のオーディエンスと同期する**<br>
Brazeは、これらのオーディエンスが最新であることを確認するために、既存のGoogle顧客リストからユーザーを追加または削除する機能も提供します。既存のオーディエンスと同期するには、同期する既存のカスタムオーディエンスを選択し、オーディエンスに**追加する**か、オーディエンスから**削除する**かを選択します。Brazeは、ユーザーがGoogle Audience Stepに入ると、ほぼリアルタイムでユーザーを追加または削除します。 

Googleオーディエンスステップを設定したら、**完了**を選択します。Google Audience ステップには、新しいオーディエンスに関する詳細が含まれます。

![Expanded view of the Custom Audience Canvas component. Here, the desired Ad account and existing audience are selected, as well as the "Add user to Audience" radio button.]({% image_buster /assets/img/audience_sync/g_sync2.png %})

{% endtab %}
{% endtabs %}

### ステップ 4:キャンバスを起動

キャンバス内でユーザージャーニーの残りを完了し、起動してください！新しいオーディエンスを作成することを選択した場合、BrazeはGoogle内にオーディエンスを作成し、Canvasのこのステップに到達したユーザーを追加します。既存のオーディエンスからユーザーを追加または削除することを選択した場合、Brazeはユーザーがこのステップに到達したときにユーザーを追加または削除します。

ユーザーは、次のコンポーネントがあればCanvasの次のコンポーネントに進み、ユーザージャーニーの最後のステップであればCanvasを終了します。 

## ユーザーの同期とレート制限の考慮事項

ユーザーがオーディエンス同期コンポーネントに到達すると、BrazeはGoogle Ads APIのレート制限を尊重しながら、ほぼリアルタイムでこれらのユーザーを同期します。これが実際に意味するところは、Brazeが5秒ごとにできるだけ多くのユーザーをバッチ処理し、これらのユーザーをGoogleに送信するということです。 

顧客がGoogle Ads APIのレート制限に近づくと、Googleは再試行の推奨事項に関するフィードバックをBrazeに提供します。Brazeの顧客がレート制限に達した場合、BrazeのCanvasは最大約13時間同期を再試行します。同期が不可能な場合、これらのユーザーは「ユーザーエラー」メトリックにリストされます。

## アナリティクスの理解 

次の表には、Audience Syncステップからの分析をよりよく理解するための指標と説明が含まれています。

| メートル法 | 説明 |
| ------ | ----------- |
| *入力済み* | Googleに同期するためにこのステップに入ったユーザーの数。 |
| *次のステップに進みました* | 次のコンポーネントがある場合、何人のユーザーが進みましたか。すべてのユーザーが自動的に進行します。これがキャンバスブランチの最後のステップである場合、このメトリックは0になります。 |
| *同期されたユーザー* | Google に正常に同期されたユーザーの数。 |
| *ユーザーが同期されていません* | フィールドが一致しないか、同意属性が`false`に設定されているために同期されていないユーザーの数。 |
| *ユーザーがエラーを起こしました* | エラーのためにGoogleと同期されなかったユーザーの数、約13時間の再試行後。特定のエラー、例えばGoogle Ads APIサービスの中断などの場合、Canvasは最大約13時間同期を再試行します。その時点で同期がまだ不可能な場合、*ユーザーが同期されていません*が表示されます。 |
| *保留中のユーザー* | 現在、Googleと同期するためにBrazeによって処理されているユーザーの数。 |
| *キャンバスを終了しました* | キャンバスを終了したユーザーの数。これは、キャンバスの最後のステップがGoogleのステップである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2}

## トラブルシューティング

{% details Why can I not select multiple fields to match in my Google Audience Step configuration? %}
Google カスタマーマッチには、これらのオーディエンスのフォーマット方法と含まれる顧客情報に関して厳しい要件があります。具体的には、モバイル広告主IDは、顧客の連絡先情報（メールや電話番号など）とは別にアップロードする必要があります。詳細については、[Google のカスタマーマッチドキュメント](https://support.google.com/google-ads/answer/7659867?hl=en#undefined)を参照してください。
{% enddetails %}

{% details How long will it take for my audiences to sync in Google? %}
Google にオーディエンスが同期されるまでに 6 ～ 12 時間かかる場合があります。
{% enddetails %}

{% details I've synced an audience, but the audience size in Google is zero. %}
プライバシーのため、ユーザーリストのサイズはリストに少なくとも**1,000人のメンバー**がいるまでゼロと表示されます。その後、サイズは最も重要な2桁に丸められます。
{% enddetails %}

{% details I've synced an audience into Google, but my ads are not serving. %}
オーディエンスに少なくとも**5,000**人のユーザーが含まれていることを確認して、広告が配信され始めるようにしてください。
{% enddetails %}

{% details How do I resolve the "Mobile App IDs Deleted" error? %}
Googleにオーディエンスを同期している場合、このエラーは、同期の一部としてモバイル識別子を同期するように選択したが、GoogleパートナーページからモバイルアプリIDを削除した場合に発生します。
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
