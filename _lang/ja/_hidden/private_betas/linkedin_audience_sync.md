---
nav_title: オーディエンスがLinkedInに同期する
article_title: キャンバスのオーディエンスをLinkedInに同期する
permalink: /linkedin_audience_sync/
description: "この参考記事では、Braze Audience SyncをLinkedInに使って、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法を紹介する。"
Tool:
  - Canvas
hidden: true
---

# オーディエンスがLinkedInに同期する

Braze Audience Sync to LinkedInを使用することで、ブランドはBrazeとの統合によるユーザーデータをLinkedInの顧客リストに追加し、行動トリガーやセグメンテーションなどに基づいた広告を配信することができる。ユーザーデータに基づいてBraze Canvasでメッセージ（プッシュ、Eメール、SMS、ウェブフックなど）をトリガーするために通常使用するあらゆる基準が、LinkedInの顧客リストでそのユーザーへの広告をトリガーできるようになった。

**オーディエンス・シンクの一般的な使用例には、以下のようなものがある**：

- 購買やエンゲージメントを促進するために、複数のチャネルを通じて価値の高いユーザーをターゲットにする。
- 他のマーケティング・チャネルで反応が低いユーザーをリターゲティングする
- 抑制オーディエンスを作成することで、ユーザーがすでにブランドの忠実な消費者である場合に広告を受け取らないようにする。

この機能により、ブランドはリンクトインと共有される特定のファーストパーティデータをコントロールすることができる。Brazeでは、ファーストパーティデータを共有できる統合とできない統合を最大限に考慮している。詳細については、当社の[プライバシーポリシーを](https://www.braze.com/privacy)参照のこと。

{% alert important %}
Audience Sync to LinkedInは現在ベータ版である。ベータ版への参加を希望する場合は、Brazeのアカウントマネージャーに連絡すること。
{% endalert %}

## 前提条件

CanvasでLinkedIn Audience Syncステップを設定する前に、以下の項目が作成、完了、または承認されていることを確認する必要がある。

| 必要条件 | 起源 | 説明 |
| --- | --- | --- |
| リンクトイン広告アカウント | [LinkedIn](https://www.linkedin.com/campaignmanager) | LinkedInの広告アカウントは、あなたのブランドと結びついている。<br><br>そのアカウントにアクセスし使用するための関連するLinkedInの利用規約に同意し、LinkedInの管理者からオーディエンスを管理するための適切な権限が付与されていることを確認する。 |
| LinkedInの規約とポリシー | LinkedIn | LinkedIn Audience Syncの使用に関連するLinkedInの要求条項、ポリシー、ガイドライン、および文書（参照することによりそこに組み込まれる条項、ポリシー、ガイドライン、および文書（LinkedInのものを含む場合がある）を含む）を遵守することに同意すること：サービス規約、広告規約、データ処理規約、プロフェッショナル・コミュニティ・ガイドライン。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合

### ステップ1:LinkedInに接続する

Brazeのダッシュボードで、**Technology Partnersに**行き、**LinkedInを**選択する。LinkedIn Audience Exportモジュールで、**Connect LinkedInを**クリックする。

![BrazeのLinkedInテクノロジーページには、OverviewモジュールとLinkedIn Audience Exportモジュールがあり、Connected LinkedInボタンがある。][3]{: style="max-width:75%;"}

その後、LinkedIn OAuthページにリダイレクトされ、BrazeにAudience Sync統合に関連する権限を承認する。**Confirm（確認）**」を選択すると、Brazeに戻り、同期するLinkedIn広告アカウントを選択する。 

![][7]{: style="max-width:75%;"}

接続に成功すると、パートナーページに戻り、どのアカウントが接続されているかを確認したり、既存のアカウントを切断したりできる。

![][6]{: style="max-width:75%;"}

LinkedInのコネクションは、Brazeのワークスペース・レベルで適用される。LinkedInの管理者がLinkedIn広告アカウントからあなたを削除した場合、Brazeは無効なトークンを検出する。その結果、LinkedInを使用してアクティブなCanvasesにはエラーが表示され、Brazeはユーザーを同期できなくなる。

### ステップ2:キャンバスのエントリー基準を設定する

広告トラッキングのオーディエンスを構築する際、ユーザーの嗜好に基づき、また[CCPAに](https://oag.ca.gov/privacy/ccpa)基づく「販売または共有しない」権利などのプライバシー法を遵守するために、特定のユーザーを含めたり除外したりしたい場合がある。マーケティング担当者は、キャンバスのエントリー基準の中で、ユーザーの適格性に関する関連フィルタを実装する必要がある。以下にいくつかの選択肢を挙げる。 

[Braze SDKを通じてiOS IDFAを]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overviewother_sdk_customizations/#optional-idfa-collection)収集した場合、**Ads Tracking Enabled**フィルターを使用できるようになる。ユーザーがオプトインしたAudience Sync送信先にのみユーザーを送信する場合は、`true` 。 

![][5]{: style="max-width:75%;"}

`opt-ins` 、`opt-outs` 、`Do Not Sell Or Share` 、またはその他の関連するカスタム属性を収集する場合は、フィルタとしてキャンバスの入力条件にこれらを含める必要がある：

![エントリーのオーディエンスが "opted_in_marketing "のキャンバスは、"true "に等しい。][4]{: style="max-width:75%;"}

Brazeプラットフォーム内でこれらのデータ保護法を遵守する方法の詳細については、[データ保護テクニカルアシスタンスを]({{site.baseurl}}/dp-technical-assistance/)参照のこと。

### ステップ3:LinkedInとのオーディエンス同期ステップを追加する

キャンバスにコンポーネントを追加し、Audience Syncを選択する。**Custom Audience**ボタンをクリックして、コンポーネント・エディターを開く。

![][2]{: style="max-width:35%;"} ![][1]{: style="max-width:29%;"}

### ステップ4:シンクの設定

希望するAudience Syncパートナーとして**LinkedInを**選択する。

![][9]{: style="max-width:70%;"}

次に目的のLinkedIn広告アカウントを選択する。**Choose a New or Existing Audience（新規または既存のオーディエンスを選択**）ドロップダウンで、新規または既存のオーディエンスの名前を入力する。

![][11]

{% tabs %}
{% tab 新しいオーディエンスを作る %}

**新しいオーディエンスを作る**<br>
新しいオーディエンスの名前を入力し、**Add Users to Audienceを**選択し、LinkedInと同期したいフィールドを選択する。この統合については、現在以下のものをサポートしている： 
- メール
- 姓と名
- アンドロイドGAID

次に、ステップエディタの下部にある**Create Audience**ボタンをクリックしてオーディエンスを保存する。

![]({% image_buster /assets/img/linkedin/linkedin10.png %})

オーディエンスが正常に作成された場合、またはこのプロセス中にエラーが発生した場合、ステップエディタの上部にユーザーに通知される。また、オーディエンスはドラフトモードで作成されたため、ユーザーはキャンバスの旅の後半でユーザーを削除するためにこのオーディエンスを参照することができる。

![]({% image_buster /assets/img/linkedin/linkedin9.png %})

新しいオーディエンスでキャンバスを立ち上げると、Brazeは、オーディエンス同期コンポーネントに入力されたユーザーをほぼリアルタイムで同期する。

{% endtab %}
{% tab 既存のオーディエンスと同期する %}

**既存のオーディエンスと同期する**<br>
Brazeはまた、既存のLinkedInオーディエンスにユーザーを追加し、これらのオーディエンスが最新であることを確認する機能も提供している。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンス名を入力し、**オーディエンスに追加する**。Brazeは、ユーザーがAudience Syncコンポーネントに入ると、ほぼリアルタイムでユーザーを追加する。

![カスタムオーディエンスキャンバスステップの拡大図。] （{% image_buster /assets/img/linkedin/linkedin17.png %} ）。

{% endtab %}
{% endtabs %}

### ステップ 5: キャンバスを立ち上げる

LinkedInにオーディエンス・シンクを設定したら、キャンバスを起動するだけだ！新しいオーディエンスが作成され、オーディエンス同期ステップを通過したユーザーは、LinkedInのこのオーディエンスに渡される。キャンバスに後続のコンポーネントが含まれていれば、ユーザーはユーザー・ジャーニーの次のステップに進むことができる。

LinkedInのオーディエンスを見るには、広告アカウントに入り、ナビゲーションの**資産**セクションで**オーディエンスを**選択する。**Audiences（オーディエンス）**ページでは、300人以上に達した後の各オーディエンスのサイズを見ることができる。

![LinkedInのページには、指定されたオーディエンスに対して以下の指標が掲載されている。][8]

## ユーザー同期とレート制限の考慮

ユーザーがオーディエンス同期ステップに達すると、BrazeはLinkedInのAPIレート制限を尊重しながら、ほぼリアルタイムでこれらのユーザーを同期する。実際には、Brazeは5秒ごとにできるだけ多くのユーザーをバッチ処理してからLinkedInに送信しようとする。

LinkedInのAPIレート制限では、1秒あたり10クエリ以下、1リクエストあたり100kユーザー以下となっている。Brazeの顧客がこのレート制限に達した場合、Braze the Canvasは最大13時間まで同期を再試行する。同期が不可能な場合、これらのユーザーはUsers Erroredメトリックの下にリストされる。

## アナリティクスを理解する

以下の表は、Audience Syncコンポーネントのアナリティクスをより理解するのに役立つメトリクスとその説明である。

| METRIC | 説明 |
| ------ | ----------- | 
| 入団 | LinkedInに同期されるこのコンポーネントを入力したユーザーの数。 |
| 次のステップへ進む | 次のコンポネントがある場合、何人のユーザーが次のコンポネントに進んだのか？これがキャンバスブランチの最後のステップであれば、すべてのユーザーが自動で進む。 |
| 同期されたユーザー | LinkedInへの同期に成功したユーザー数。 |
| 同期されていないユーザー | 一致するフィールドがないために同期されていないユーザーの数。 |
| 保留中のユーザー | 現在BrazeがLinkedInに同期するために処理しているユーザー数。 |
| ユーザーエラー | 約13時間の再試行後、APIエラーのためにLinkedInに同期されなかったユーザーの数。エラーの原因として考えられるのは、LinkedInトークンが無効であるか、LinkedInでオーディエンスが削除されている場合である。 |
| イグジット・キャンバス | キャンバスを退出したユーザーの数。これは、キャンバスの最後のステップがオーディエンス同期コンポーネントである場合に発生する。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
バルク・フラッシュと13時間のリトライのため、同期したユーザーとエラーになったユーザーのメトリクスのレポートにはそれぞれ遅れが生じることを忘れないでほしい。
{% endalert %}

{% alert important %}
LinkedInは、そのプラットフォーム内で、マッチ率に関する追加指標を提供している。特定のAudience Syncのマッチを確認するには、Audience Syncステップのメトリクスをクリックして、**キャンバスのステップ詳細**ページに入る。
<br><br>
パートナーを**LinkedIn**、広告アカウント、オーディエンスを選択し、LinkedInからのオーディエンスサイズとマッチ率を確認する。

![]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## トラブルシューティング

{% details LinkedInにオーディエンスのサイズが反映されるまで、どれくらいの時間がかかるのか？ %}
LinkedInアカウント内でオーディエンスを表示するには、最大48時間の遅れがある。
{% enddetails %}

{% details LinkedInが広告アカウントに入力するオーディエンスの最小サイズは？ %}
LinkedInアカウント内のオーディエンスのサイズを入力するには、オーディエンスに少なくとも300人のメンバーが含まれていなければならない。
{% enddetails %}

{% details 無効なトークンエラーが表示された場合、次に何をすればよいか？ %}
LinkedInのパートナーページで、LinkedInアカウントの切断と再接続ができる。LinkedInの管理者に、同期したい広告アカウントに適切な権限があることを確認する。
{% enddetails %}

{% details なぜキャンバスは起動できないのか？ %}
LinkedInパートナーページで、LinkedIn広告アカウントがBrazeに正常に接続されていることを確認する。
広告アカウントを選択し、新しいオーディエンスの名前を入力し、一致するフィールドを選択していることを確認する。
{% enddetails %}

{% details LinkedInにユーザーを渡した後、ユーザーがマッチングしたかどうかを知るには？ %}
- LinkedInにユーザーを渡した後、ユーザーがマッチングしたかどうかを知るには？
LinkedInは、ダッシュボード内でマッチ率に関する情報を提供している。LinkedInの**「オーディエンス」**セクションで確認できる。 
- さらに、オーディエンス同期ステップのキャンバスステップ詳細ページで、LinkedInオーディエンスのマッチ率を確認することができる。
{% enddetails %} 

{% details LinkedInは何人のオーディエンスをサポートできるのか？ %}
現在、LinkedIn広告アカウントのオーディエンスの数に制限はない。
{% enddetails %}

{% details なぜセグメントはBUILDINGステータスに留まり、更新されないのか？ %}
セグメントは、ドラフトまたはアクティブなキャンペーンで30日間継続的に使用されないと、未使用とみなされ、ARCHIVEDに設定される。このため、アーカイブされたセグメントにアップデートがストリーミングされ、そのセグメントがBUILDINGの状態になり、再びアーカイブされる直前に、新しいアップデートが未使用のセグメントにストリーミングされると、セグメントはBUILDINGの状態で「立ち往生」しているように見えることがある。
{% enddetails %}

[1]: {% image_buster /assets/img/linkedin/linkedin1.png %}
[2]: {% image_buster /assets/img/linkedin/linkedin2.png %}
[3]: {% image_buster /assets/img/linkedin/linkedin3.png %}
[4]: {% image_buster /assets/img/linkedin/linkedin4.png %}
[5]: {% image_buster /assets/img/linkedin/linkedin5.png %}
[6]: {% image_buster /assets/img/linkedin/linkedin6.png %}
[7]: {% image_buster /assets/img/linkedin/linkedin7.png %}
[8]: {% image_buster /assets/img/linkedin/linkedin8.png %}
[9]: {% image_buster /assets/img/linkedin/linkedin.png %}
[11]: {% image_buster /assets/img/linkedin/linkedin20.png %}