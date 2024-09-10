---
nav_title: 視聴者がLinkedIn に同期する
article_title: Canvas Audience とLinkedIn の同期
permalink: /linkedin_audience_sync/
description: "このレファレンス記事では、Braze Audience Sync をLinkedIn に使用して、ビヘイビアートリガーs、セグメンテーションなどに基づいてアドバタイズメントを配信する方法について説明します。"
Tool:
  - Canvas
hidden: true
---

# 視聴者がLinkedIn に同期する

Brazeオーディエンス同期を使用して、ブランドはBrazeインテグレーションのユーザーデータをLinkedIn 顧客一覧に追加して、動作トリガーs、セグメンテーションなどに基づいてアドバタイズメントを配信できます。通常、メッセージのトリガーに使用する基準(プッシュ、メール、SMS、Webhookなど)が、ユーザーデータに基づいてBrazeキャンバスに設定され、LinkedIn 顧客一覧のそのユーザーに広告をトリガーできるようになりました。

**オーディエンス同期の一般的なユースケースには**が含まれます。

- 多重チャネルによる高価値ユーザーをターゲットに、仕入・エンゲージメントを牽引
- 他のマーケティング チャネルにあまりレスポンシブでないユーザーのリターゲット
- 自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑圧オーディエンスsの作成

この機能により、ブランドはLinkedInと共有されている特定のファーストパーティデータをコントロールできます。Brazeでは、ファーストパーティデータを共有できる統合と共有できない統合を最大限に検討します。詳細については、[プライバシーポリシー](https://www.braze.com/privacy)を参照してください。

{% alert important %}
Audience Sync to LinkedInは現在ベータ版にある。ベータ版に参加したい場合は、Braze アカウントマネージャーにお問い合わせください。
{% endalert %}

## 前提条件

キャンバスでLinkedIn Audience Sync ステップを設定するには、以下のアイテムが作成、完了、または受け入れられていることを確認する必要があります。

| 要件 | Origin | 説明 |
| --- | --- | --- |
| LinkedInの広告アカウント | [LinkedIn](https://www.linkedin.com/campaignmanager) | ブランドに関連付けられたアクティブなLinkedIn アドアカウント。<br><br>関連するLinkedIn 利用規約を受け入れ、そのアカウントを使用していること、およびLinkedIn 管理者がオーディエンスを管理するための適切な権限をアプリに付与していることを確認してください。 |
| LinkedIn用語&ポリシー | LinkedIn | LinkedIn Audience Sync の使用に関連するLinkedIn の必要な用語、ポリシー、ガイドライン、およびドキュメントのいずれかに準拠することに同意します。これには、LinkedIn の以下の用語、ポリシー、ガイドライン、およびドキュメントが含まれます。サービス条件、広告契約、データ処理契約、および専門家コミュニティガイドライン。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合

### ステップ1:LinkedIn への接続

Braze ダッシュボードで、**Technology Partners**に移動し、**LinkedIn**を選択します。LinkedIn Audience Export モジュールで、**Connect LinkedIn** をクリックします。

![Braze のLinkedIn テクノロジページには、Overview モジュールとLinkedIn Audience Export モジュールとConnected LinkedIn ボタンがあります。][3]{: style="max-width:75%;"}

次に、LinkedIn OAuth ページにリダイレクトされ、オーディエンスシンクインテグレーションに関連する権限のBrazeを許可します。**Confirm** を選択すると、Braze にリダイレクトされ、同期するLinkedIn アドアカウントを選択します。 

![][7]{: style="max-width:75%;"}

接続に成功すると、パートナーページに戻り、どのアカウントが接続されているかを表示したり、既存のアカウントを切断したりできます。

![][6]{: style="max-width:75%;"}

あなたのLinkedInコネクションは、アプリはBraze ワークスペースの段階にあります。LinkedIn 管理者がLinkedIn アドアカウントからユーザを削除すると、Braze は不正なトークンを検出します。そのため、LinkedIn を使用しているアクティブなキャンバスにはエラーs が表示され、Braze はユーザーs を同期できません。

### ステップ2:キャンバスのエントリ条件を設定する

広告追跡のためにオーディエンスsを構築する場合、その好みに基づいて特定のユーザーsを含めるか除外し、[CCPA](https://oag.ca.gov/privacy/ccpa)の下で「売らない、共有しない」権利などのプライバシー法に従うことを希望する場合があります。マーケターは、キャンバスのエントリ基準の範囲内で、ユーザーの適格性に関連するフィルターを実施すべきである。以下に、いくつかのオプションを示します。 

[iOS IDFAをBraze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overviewother_sdk_customizations/#optional-idfa-collection)を通して収集した場合、**Ads Tracking Enabled**フィルターを使用することができます。`true` として値を選択すると、ユーザーs が選択されているオーディエンス同期送信先s にのみ送信されます。 

![][5]{: style="max-width:75%;"}

`opt-ins`、`opt-outs`、`Do Not Sell Or Share`、または他の関連するカスタム属性s を収集する場合は、キャンバスのエントリ基準にこれらをフィルターとして含める必要があります。

![エントリ オーディエンスが"opted_in_マーケティング" equals "true" のキャンバス。][4]{: style="max-width:75%;"}

Braze プラットフォーム内でこれらのデータプロテクション法を遵守する方法の詳細については、[データプロテクションテクニカルサポート]({{site.baseurl}}/dp-technical-assistance/)を参照してください。

### ステップ3:LinkedIn を使用したオーディエンス同期ステップの追加

キャンバスにコンポーネントを追加し、「オーディエンス同期」を選択します。コンポーネントエディターを開封するには、**Custom Audience**ボタンを押します。

![][2]{: style="max-width:35%;"} ![][1]{: style="max-width:29%;"}

### ステップ4:同期設定

必要なAudience Sync パートナーとして**LinkedIn** を選択します。

![][9]{: style="max-width:70%;"}

次に、目的のLinkedIn ad アカウントを選択します。**新規または既存のオーディエンス**ドロップダウンから、新規または既存のオーディエンスの名前を入力します。

![][11]

{% tabs %}
{% tab 新規オーディエンスの作成 %}

**新規オーディエンスの作成**<br>
新しいオーディエンスの名前を入力し、**オーディエンス** にユーザを追加を選択し、LinkedIn と同期するフィールドを選択します。この統合では、現在以下をサポートしています。 
- メール
- 姓と名
- Androidガイド

次に、ステップエディタの下部にある**オーディエンス**を作成ボタンをクリックして、オーディエンスを保存します。

![]({% image_buster /assets/img/linkedin/linkedin10.png %})

オーディエンスが正常に作成された場合、またはこの処理中にエラーが発生した場合は、ステップエディタの上部にユーザが通知されます。ユーザー s は、このオーディエンスを参照して、後でキャンバスジャーニーでユーザーを削除することもできます。これは、オーディエンスが下書きで作成されたためです。

![]({% image_buster /assets/img/linkedin/linkedin9.png %})

新しいオーディエンスを使用してキャンバスを起動すると、オーディエンスシンクコンポーネントに入ったときに、Braze はユーザーをほぼリアルタイムで同期します。

{% endtab %}
{% tab 既存のオーディエンスとの同期 %}

**既存のオーディエンスとの同期**<br>
また、Brazeは、これらのオーディエンスが最新であることを確認するために、既存のLinkedIn オーディエンス sにユーザーを追加する機能も提供します。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンスの名前を入力し、**オーディエンスに追加します。**Braze は、オーディエンスシンクコンポーネントに入ると、ほぼリアルタイムでユーザーs を追加します。

![カスタムオーディエンスキャンバスステップの展開表示。ここでは、目的の広告アカウントと既存のオーディエンスが選択されます。]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### ステップ 5: キャンバスの起動

Audience Sync to LinkedIn を設定したら、キャンバスを起動します。新しいオーディエンスが作成され、LinkedIn でこのオーディエンスにオーディエンス同期 を流れるユーザーs ステップが渡されます。キャンバスに後続のコンポーネントが含まれている場合、ユーザーs はユーザーの移動の次回のステップに進みます。

LinkedIn のオーディエンスを表示するには、広告アカウントに移動し、ナビゲーションの**Assets** セクションで**オーディエンスs** を選択します。**オーディエンス s**ページから、300人以上の会員に達した後、それぞれのオーディエンスの大きさを見ることができます。

![Linked 指定されたオーディエンスの次のメトリクスを一覧表示します。][8]

## ユーザの同期とレート制限に関する考慮事項

ユーザーがオーディエンス同期ステップに到達すると、BrazeはLinkedInのAPIレート制限を尊重しながら、これらのユーザーをほぼリアルタイムで同期します。実際には、Braze は、これらのユーザーをLinkedIn に送信する前に、5 秒ごとに最大数のユーザーをバッチ処理して処理しようとします。

LinkedIn のAPI レート制限では、1 秒あたり10 件のクエリーと1 リクエストあたり100k のユーザーを超えないように設定されています。Braze 顧客がこのレート制限に達した場合、キャンバスをBrazeすると最大13 時間までシンクが再試行されます。同期できない場合、これらのユーザーは「エラーメトリクス」のユーザーに表示されます。

## 分析について

次のテーブルには、オーディエンスシンクコンポーネントからの分析をよりよく理解するためのメトリクスと説明が含まれています。

| メトリック | 説明 |
| ------ | ----------- | 
| 入力 | このコンポーネントをLinkedIn に同期するために入力したユーザーの人数。 |
| 次のステップに進む | 次のコンポーネントがある場合、次のコンポーネントに進んだユーザーの数は?すべてのユーザーs は、これがキャンバスブランチの最後のステップである場合、自動的に進みます。 |
| ユーザーの同期 | LinkedIn に正常に同期されたユーザーの件数。 |
| 同期されていないユーザー | 照合するフィールドs がないために同期されていないユーザーの個数。 |
| 保留中のユーザー | Braze がLinkedIn に同期するために現在処理されているユーザーの数。 |
| ユーザーのエラー | 約13 時間の再試行後にAPI エラーのためにLinkedIn に同期されなかったユーザーの数。エラーs の潜在的な原因に、不正なLinkedIn トークンが含まれているか、またはオーディエンスがLinkedIn で削除されている可能性があります。 |
| 廃止されたキャンバス | キャンバスを終了したユーザーの人数。これは、キャンバスの最後のステップがオーディエンス同期コンポーネントである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
バルクフラッシュおよび13 時間の再試行のために、それぞれユーザー s 同期およびユーザー s エラーのメトリクスのレポートが遅延することを覚えておいてください。
{% endalert %}

{% alert important %}
LinkedIn は、プラットフォーム内のマッチングレートに関する追加のメトリクスを提供します。特定のオーディエンス同期の一致を確認するには、オーディエンス同期ステップメトリクスを選択して、**キャンバスステップ詳細**ページに移動します。
<br><br>
パートナーを**LinkedIn**、広告アカウント、およびオーディエンスとして選択し、LinkedInからオーディエンスのサイズとマッチングレートを確認します。

![]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## トラブルシューティング

{% details オーディエンスの大きさがLinkedInに入るのにどれくらいかかりますか？ %}
LinkedIn アカウント内のオーディエンスを表示するのに最大48 時間の遅延があります。
{% enddetails %}

{% details LinkedInが広告アカウント内に入力するための最低オーディエンス容量はいくらですか? %}
オーディエンスには、LinkedIn アカウント内のオーディエンス容量を入力するために、少なくとも300 のメンバが含まれている必要があります。
{% enddetails %}

{% details 不正なトークン エラーを受信した場合、次にどうすればよいですか? %}
LinkedIn パートナーページで、LinkedIn アカウントを切断して再接続できます。LinkedIn 管理者に、同期する広告アカウントに対するアプリの適切な権限があることを確認します。
{% enddetails %}

{% details キャンバスを起動できないのはなぜですか? %}
LinkedIn アドアカウントが、LinkedIn パートナーページでBraze に正常に接続されたことを確認してください。
広告アカウントを選択し、新しいオーディエンスの名前を入力し、照合するフィールドs を選択していることを確認します。
{% enddetails %}

{% details ユーザーs をLinkedIn に渡した後、ユーザーs が一致したかどうかを知るにはどうすればよいですか? %}
- ユーザーs をLinkedIn に渡した後、ユーザーs が一致したかどうかを知るにはどうすればよいですか?
LinkedIn は、ダッシュボード内のマッチレートに関する情報を提供します。LinkedIn の**Audiences** セクションで確認できます。 
- さらに、オーディエンス同期ステップのキャンバスステップ詳細ページで、LinkedIn オーディエンスのマッチングレートを確認できます。
{% enddetails %} 

{% details LinkedInが支援できるオーディエンス数は? %}
現在、LinkedIn アドアカウントのオーディエンスの件数に制限はありません。
{% enddetails %}

{% details ビルディングステータスでSegmentが詰まっていて、更新 dではないのはなぜですか? %}
Segmentは、下書きまたは有効なキャンペーンで30日間継続的に使用されない場合、未使用と見なされ、ARCHIVEDに設定されます。このため、Segmentはear & quot;stuck&quot をアプリすることがあります。ARCHIVED Segmentに更新がストリーミングされ、それがビルド状態にプッシュされ、再アーカイブされる直前に、新しい更新が未使用のSegmentにストリーミングされます。
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