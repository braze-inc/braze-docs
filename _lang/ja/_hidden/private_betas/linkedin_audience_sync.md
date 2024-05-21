---
nav_title: LinkedInへのオーディエンス同期
article_title: キャンバスのオーディエンスをLinkedInに同期
permalink: /linkedin_audience_sync/
description: "この参考記事では、Braze Audience SyncをLinkedInに利用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
Tool:
  - Canvas
hidden: true
---

# LinkedInへのオーディエンス同期

Braze Audience Sync to LinkedInを使用することで、ブランドはBrazeの統合からLinkedInの顧客リストにユーザーデータを追加し、行動トリガーやセグメンテーションなどに基づいて広告を配信することができます。ユーザーデータに基づいてBraze Canvasでメッセージ（プッシュ、Eメール、SMS、ウェブフックなど）をトリガーするために通常使用する基準はすべて、LinkedInの顧客リスト内のそのユーザーに広告をトリガーすることができます。

**オーディエンス・シンクの一般的な使用例には、**以下のようなものがある：

- 購買やエンゲージメントを促進するために、複数のチャネルを通じて価値の高いユーザーをターゲットにする。
- 他のマーケティング・チャネルで反応が低いユーザーをリターゲティングする。
- サプレッション（抑制）オーディエンスを作成することで、ユーザーがすでにブランドの忠実な消費者である場合に広告を受け取らないようにする。

この機能により、ブランドはLinkedInと共有される特定のファーストパーティデータをコントロールすることができる。Brazeでは、ファーストパーティデータを共有できる統合と共有できない統合を最大限に考慮しています。詳しくは[プライバシー](https://www.braze.com/privacy)ポリシーをご覧ください。

{% alert important %}
Audience Sync to LinkedInは現在ベータ版です。ベータ版への参加をご希望の方は、Brazeのアカウントマネージャーにご連絡ください。
{% endalert %}

## 前提条件

CanvasでLinkedIn Audience Syncステップを設定する前に、以下の項目が作成、完了、または承認されていることを確認する必要があります。

| 要件｜原産地｜説明
| --- | --- | --- |
| LinkedIn広告アカウント｜[LinkedIn](https://www.linkedin.com/campaignmanager)｜あなたのブランドに結びついたアクティブなLinkedIn広告アカウント。<br><br>そのアカウントにアクセスし使用するための関連するLinkedInの利用規約に同意し、LinkedInの管理者からオーディエンスを管理するための適切な権限が付与されていることを確認してください。|
| LinkedInの利用規約とポリシー｜LinkedIn｜LinkedIn Audience Syncの使用に関連するLinkedInの必要な規約、ポリシー、ガイドライン、文書（参照することでそこに組み込まれるLinkedInの規約、ポリシー、ガイドライン、文書を含む）を遵守することに同意します：サービス規約、広告規約、データ処理規約、およびプロフェッショナル・コミュニティ・ガイドライン。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合

### ステップ 3:LinkedInに接続する

Brazeのダッシュボードで**Technology Partnersに**進み、**LinkedInを**選択します。LinkedIn Audience Exportモジュールで、**Connect LinkedInを**クリックします。

BrazeのLinkedInテクノロジーページには、OverviewモジュールとLinkedIn Audience Exportモジュールがあり、Connected LinkedInボタンがあります][3]。{: style="max-width:75%;"}

その後、LinkedIn OAuthページにリダイレクトされ、BrazeのAudience Sync統合に関連する権限を承認します。**Confirm（確認**）を選択すると、Brazeに戻り、同期するLinkedIn広告アカウントを選択します。 

![][7]{: style="max-width:75%;"}

接続に成功すると、パートナーページに戻り、どのアカウントが接続されているかを確認したり、既存のアカウントを切断したりすることができます。

![][6]{: style="max-width:75%;"}

LinkedInのコネクションは、Brazeワークスペースレベルで適用されます。LinkedInの管理者がLinkedIn広告アカウントからあなたを削除した場合、Brazeは無効なトークンを検出します。その結果、LinkedInを使用してアクティブなCanvasesにエラーが表示され、Brazeはユーザーを同期できなくなります。

### ステップ 3:キャンバスのエントリー基準を設定する

広告トラッキングのオーディエンスを構築する際、ユーザーの嗜好に基づいて特定のユーザーを含めたり除外したり、[CCPAに](https://oag.ca.gov/privacy/ccpa)基づく「販売または共有しない」権利などのプライバシー法を遵守したい場合があります。マーケティング担当者は、キャンバスのエントリー基準の中で、ユーザーの適格性に関する関連フィルターを実装する必要があります。以下に、いくつかのオプションを挙げる。 

[Braze SDKを通じてiOS IDFAを]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overviewother_sdk_customizations/#optional-idfa-collection)収集した場合、**Ads Tracking Enabled**フィルターを使用することができます。`true` を選択すると、ユーザーがオプトインしたAudience Sync送信先にのみユーザーを送信します。 

![][5]{: style="max-width:75%;"}

`opt-ins` 、`opt-outs` 、`Do Not Sell Or Share` 、またはその他の関連するカスタム属性を収集する場合は、フィルタとしてキャンバスの入力条件にこれらを含める必要があります：

opted\_in\_marketing "が "true "に等しいキャンバス][4]。{: style="max-width:75%;"}

Brazeプラットフォーム内でこれらのデータ保護法を遵守する方法の詳細については、[データ保護テクニカルアシスタンスを]({{site.baseurl}}/dp-technical-assistance/)ご覧ください。

### ステップ 3:LinkedInとのオーディエンス同期ステップを追加する

キャンバスにコンポーネントを追加し、Audience Syncを選択します。**Custom Audience**ボタンをクリックして、コンポーネントエディタを開く。

![][2]

### ステップ 4: シンクの設定

**LinkedInを**Audience Syncのパートナーとして選択します。

![][9]{: style="max-width:70%;"}

次に、目的のLinkedIn広告アカウントを選択します。**Choose a New or Existing Audience（新規または既存のオーディエンスを選択**）］ドロップダウンで、新規または既存のオーディエンスの名前を入力します。

![][11]

{% tabs %}
{% tab Create a New Audience %}

**新しいオーディエンスを作る**<br>
新しいオーディエンスの名前を入力し、**オーディエンスにユーザーを追加**を選択し、LinkedInと同期するフィールドを選択します。この統合については、現在以下のものをサポートしている：
メール
\- 姓と名
Android GAID

次に、ステップエディタの下部にある**Create Audience**ボタンをクリックして、オーディエンスを保存します。

{% image_buster /assets/img/linkedin/linkedin10.png %}

オーディエンスが正常に作成された場合、またはこのプロセス中にエラーが発生した場合、ステップエディタの上部にユーザーに通知されます。また、オーディエンスはドラフトモードで作成されたため、Canvasジャーニーの後半でユーザがこのオーディエンスを参照し、ユーザを削除することもできます。

{% image_buster /assets/img/linkedin/linkedin9.png %}

新しいオーディエンスでキャンバスを立ち上げると、Brazeは、オーディエンス同期コンポーネントに入力されたユーザーをほぼリアルタイムで同期します。

{% endtab %}
{% tab Sync with an Existing Audience %}

**既存のオーディエンスとの同期**<br>
Brazeはまた、既存のLinkedInオーディエンスにユーザーを追加し、これらのオーディエンスが最新であることを確認する機能も提供しています。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンス名を入力し、**オーディエンスに追加**します。Brazeは、ユーザーがAudience Syncコンポーネントに入ると、ほぼリアルタイムでユーザーを追加します。

![Expanded view of the Custom Audience Canvas step. Here, the desired ad account and existing audience are selected.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### ステップ 5: キャンバスを開始

LinkedInへのオーディエンスシンクを設定したら、キャンバスを起動するだけです！新しいオーディエンスが作成され、オーディエンス同期ステップを通過したユーザーはLinkedInのこのオーディエンスに渡されます。キャンバスに後続のコンポーネントが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

LinkedInのオーディエンスを見るには、広告アカウントに入り、ナビゲーションの**資産**セクションで**オーディエンスを**選択します。**Audiences（オーディエンス**）ページでは、300人以上に達した後の各オーディエンスのサイズを確認することができます。

LinkedInのページには、指定されたオーディエンスに対して以下のメトリクスがリストアップされている][8]。

## ユーザー同期とレート制限の考慮

ユーザーがオーディエンス同期ステップに達すると、BrazeはLinkedInのAPIレート制限を尊重しながら、ほぼリアルタイムでこれらのユーザーを同期します。実際には、Brazeは5秒ごとにできるだけ多くのユーザーをバッチ処理してからLinkedInに送信しようとします。

LinkedInのAPIレート制限では、1秒あたり10クエリ以内、1リクエストあたり100kユーザー以内となっている。Brazeのお客様がこのレート制限に達した場合、Braze the Canvasは最大13時間まで同期を再試行します。同期が不可能な場合、これらのユーザーはUsers Erroredメトリックの下にリストされます。

## アナリティクスを理解する

以下の表には、Audience Syncコンポーネントのアナリティクスをより理解するための指標と説明が記載されています。

| メトリック
| ------ | ----------- |
| LinkedInに同期されるこのコンポーネントを入力したユーザーの数。|
| 次のステップに進みましたか？これがキャンバスブランチの最後のステップであれば、すべてのユーザーが自動で進みます。|
| 同期されたユーザー｜LinkedInに正常に同期されたユーザーの数。|
| 同期されていないユーザー数｜一致するフィールドが見つからないために同期されていないユーザーの数。|
| 保留中のユーザー数｜BrazeがLinkedInに同期するために処理中のユーザー数。|
| ユーザーエラー｜約13時間のリトライの後、APIエラーのためにLinkedInに同期されなかったユーザーの数。エラーの原因としては、LinkedInトークンが無効な場合や、LinkedInでオーディエンスが削除された場合などが考えられます。|
| キャンバスを終了したユーザーの数。これは、キャンバスの最後のステップがオーディエンス同期コンポーネントである場合に発生します。|
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
一括フラッシュと13時間の再試行により、同期されたユーザーとエラーになったユーザーのメトリクスのレポートにはそれぞれ遅れが生じることを忘れないでください。
{% endalert %}

{% alert important %}
LinkedInは、プラットフォーム内でマッチ率に関する追加指標を提供している。特定のAudience Syncの一致を確認するには、Audience Syncステップのメトリクスをクリックして、**キャンバスのステップ詳細**ページに移動します。
<br><br>
パートナーを**LinkedIn**、広告アカウント、オーディエンスを選択すると、LinkedInからのオーディエンスサイズとマッチ率が表示されます。

{% image_buster /assets/img/linkedin/linkedin11.png %}
{% endalert %}

## トラブルシューティング

{% details How long will it take for the audience sizes to populate in LinkedIn? %}
LinkedInアカウント内でオーディエンスを表示するには、最大48時間の遅れがあります。
{% enddetails %}

{% details What is the minimum audience size for LinkedIn to populate within your ad account?  %}
LinkedInアカウント内のオーディエンスのサイズを入力するには、オーディエンスに少なくとも300人のメンバーが含まれている必要があります。
{% enddetails %}

{% details What should I do next if I receive an invalid token error? %}
LinkedInパートナーページでは、LinkedInアカウントの切断と再接続ができます。LinkedInの管理者に、同期したい広告アカウントに適切な権限があることを確認します。
{% enddetails %}

{% details Why is my Canvas not allowed to launch? %}
LinkedInのパートナーページで、お客様のLinkedIn広告アカウントがBrazeに正常に接続されていることをご確認ください。
広告アカウントを選択し、新しいオーディエンスの名前を入力し、一致するフィールドを選択していることを確認してください。
{% enddetails %}

{% details How do I know if users have matched after passing users to LinkedIn? %}
\- LinkedInにユーザーを渡した後、ユーザーがマッチしたかどうかを知るにはどうすればよいですか？
LinkedInは、ダッシュボード内でマッチ率に関する情報を提供している。LinkedInの「**オーディエンス**」セクションで確認できる。
\- さらに、オーディエンス同期ステップのキャンバスステップ詳細ページで、LinkedInオーディエンスのマッチ率を確認することができます。
{% enddetails %} 

{% details How many audiences can LinkedIn support? %}
現在、LinkedIn広告アカウントのオーディエンスの数に制限はありません。
{% enddetails %}

{% details Why is a segment stuck in BUILDING status and not updated? %}
ドラフトまたはアクティブなキャンペーンで30日間継続的に使用されないと、セグメントは未使用とみなされ、アーカイブに設定されます。このため、アーカイブされたセグメントにアップデートがストリーミングされ、そのセグメントがBUILDINGの状態になり、再びアーカイブされる直前に、新しいアップデートが未使用のセグメントにストリーミングされると、セグメントはBUILDINGの状態で「立ち往生」しているように見えることがある。
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