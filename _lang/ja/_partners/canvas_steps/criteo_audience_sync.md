---
nav_title: Criteo
article_title: キャンバスのオーディエンスがCriteoに同期する
description: "このリファレンス記事では、Braze Audience Sync to Criteo を使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
page_order: 1
alias: "/audience_sync_criteo/"

Tool:
  - Canvas
---

# Audience Sync to Criteo

Braze Audience Sync to Criteo を使用すると、ブランドは独自の Braze 統合からのユーザーデータを Criteo の顧客リストに追加して、行動トリガーやセグメンテーションなどに基づいて広告を配信できます。ユーザーデータに基づいて Braze キャンバスでメッセージをトリガーするために通常使用する基準 (プッシュ、メール、SMS、Webhook など) を、Criteo 顧客リスト内の該当ユーザーに対して広告をトリガーするために使用できるようになりました。

**オーディエンス同期の一般的なユースケースには次のものがあります。**

- 購買やエンゲージメントを促進するために、複数のチャネルを通じて価値の高いユーザーをターゲット。
- 他のマーケティング チャネルにあまりレスポンシブでないユーザーのリターゲッティング
- すでに自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑制オーディエンスの作成
- Lookalikeオーディエンスを作成し、新規ユーザーをより効率的に獲得する

この機能により、ブランドは Criteo と共有される特定のファーストパーティデータを制御できるようになります。Braze では、ファーストパーティデータを共有できる統合と共有できない統合を最大限に考慮しています。詳細については、私たちの[プライバシーポリシー](https://www.braze.com/privacy)を参照してください。

{% alert important %}
**Audience Sync Pro 免責条項**<br>
Braze Audience Sync to Criteo は Audience Sync Pro 統合です。この統合の詳細については、Brazeのアカウント・マネージャーに問い合わせを。<br> 
{% endalert %}

## 前提条件 

キャンバスで Criteo へのオーディエンス同期のステップを設定するには、以下の項目が作成され完了していることを確認する必要があります。

| 要件 | 提供元 | 説明 |
| --- | --- | --- |
| Criteo広告アカウント | [Criteo](https://marketing.criteo.com/) | ブランドに関連付けられたアクティブな Criteo 広告アカウント。<br><br>Criteo 管理者から、オーディエンスにアクセスするための適切な権限が付与されていることを確認します。 |
| [Criteo 広告ガイドライン](https://www.criteo.com/advertising-guidelines/)<br>そして<br>[Criteo ブランドセーフティガイドライン](https://www.criteo.com/wp-content/uploads/2017/11/Criteo-Brand-Safety-Guidelines-UK-March-2016.pdf) | Criteo | Criteo のアクティブな顧客として、Criteo キャンペーンを開始する前に、Criteo の広告ガイドラインを遵守できることを確認します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 統合 

### ステップ1:Criteo に接続する

Braze ダッシュボードで [**パートナー連携**] > [**テクノロジーパートナー**] に移動し、[**Criteo**] を選択します。[Criteo Audience Export] で、[**Criteo を接続**] を選択します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、[**テクノロジーパートナー**] は [**統合**] にあります。
{% endalert %}

![Braze の Criteo テクノロジーページ。[概要] セクション、[Criteo] セクション、[接続済みの Criteo] ボタンが表示されています。][5]{: style="max-width:80%;"}

次に、Criteo oAuth ページにリダイレクトされ、Braze に Audience Sync 統合に関連するアクセス許可を承認します。

[confirm] を選択すると、Braze にリダイレクトされます。同期する Criteo 広告アカウントを選択します。 

![Criteo に接続できる広告アカウントのリスト。][7]{: style="max-width:80%;"}

接続に成功すると、パートナーページが再び表示され、どのアカウントが接続されているかを表示したり、既存のアカウントを切断したりできます。

![広告アカウントが接続されたことを示す更新後の Criteo テクノロジーパートナーページ。][4]{: style="max-width:80%;"}

Criteoとの接続は、Brazeワークスペースレベルで適用されます。Criteo 管理者が Criteo 広告アカウントからユーザーを削除した場合、Braze は無効なトークンを検出します。その結果、Criteoを使用しているアクティブなCanvasesにはエラーが表示され、Brazeはユーザーを同期できなくなります。

### ステップ2:キャンバスのエントリ基準を設定する

広告追跡のためにオーディエンスを作成する場合、その好みに基づいて特定のユーザーを含めるか除外し、[CCPA](https://oag.ca.gov/privacy/ccpa)の「販売または共有を禁止する」権利などのプライバシー法に従うことを希望する場合があります。マーケターは、キャンバスのエントリ基準の範囲内で、ユーザーの適格性に関する適切なフィルターを実装する必要があります。以下にいくつかの選択肢を挙げます。

[Braze SDK で iOS IDFA]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection) を収集した場合、[広告の追跡が有効] フィルターを使用できます。ユーザーがオプトインしたオーディエンス同期の宛先にのみユーザーを送信するには、値を true に選択します。

![][11]

`opt-ins`、`opt-outs`、`Do Not Sell Or Share`、または他の関連するカスタム属性を収集する場合は、キャンバスのエントリ基準にこれらをフィルターとして含める必要があります。

![][12]

Braze プラットフォーム内でこれらのデータ保護法を遵守する方法の詳細については、[データ保護テクニカルアシスタンス]({{site.baseurl}}/dp-technical-assistance/)を参照してください。

### ステップ3:Criteoでオーディエンス同期ステップを追加する

キャンバスにコンポーネントを追加し、[**オーディエンスの同期**] を選択します。

![キャンバスフローに Criteo オーディエンスコンポーネントを追加するための前のステップのワークフロー。][9]{: style="max-width:35%;"}![キャンバスフローに Criteo オーディエンスコンポーネントを追加するための前のステップのワークフロー。][10]{: style="max-width:28%;"}

### ステップ4:同期設定

[**カスタムオーディエンス**] ボタンをクリックしてコンポーネントエディターを開きます。

**Criteo** を目的のオーディエンス同期パートナーとして選択します。 

![][6]

次に、目的の Criteo 広告アカウントを選択します。[**新規または既存のオーディエンスを選択**] ドロップダウンで、新しいオーディエンスまたは既存のオーディエンスの名前を入力します。

{% tabs %}
{% tab 新規オーディエンスの作成 %}
**新規オーディエンスの作成**<br>
新しいオーディエンスの名前を入力し、[**ユーザーをオーディエンスに追加**] を選択し、Criteo と同期するフィールドを選択します。次に、ステップエディタの下部にある**オーディエンスを作成**ボタンをクリックしてオーディエンスを保存します。

![カスタムオーディエンスキャンバスステップの展開ビュー。ここでは目的の広告アカウントが選択され、新しいオーディエンスが作成されます。]({% image_buster /assets/img/criteo/criteo3.png %})

ユーザーは、オーディエンスが正常に作成された場合、またはこのプロセス中にエラーが発生した場合に、ステップエディターの上部で通知されます。ユーザーは、後でキャンバスジャーニーでユーザーを削除するためにこのオーディエンスを参照することもできます。これは、オーディエンスが下書きで作成されたためです。

![キャンバスコンポーネントで新しいオーディエンスが作成された後に表示されるアラート。]({% image_buster /assets/img/criteo/criteo1.png %})

新しいオーディエンスを使用してキャンバスを起動すると、オーディエンス同期コンポーネントに入る時点で、Braze はユーザーをほぼリアルタイムで同期します。
{% endtab %}
{% tab 既存のオーディエンスと同期する %}
**既存のオーディエンスとの同期**<br>
また、Braze は、これらのオーディエンスが最新であることを確認するために、既存の Criteo オーディエンスにユーザーを追加する機能も提供します。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンスの名前を入力し、**オーディエンスに追加します。**Braze は、オーディエンス同期コンポーネントに入ると、ほぼリアルタイムでユーザーを追加します。

![カスタムオーディエンスキャンバスステップの展開ビュー。ここでは、目的の広告アカウントと既存のオーディエンスが選択されています。]({% image_buster /assets/img/criteo/criteo8.png %})

{% endtab %}
{% endtabs %}

### ステップ 5: キャンバスを起動

Audience Sync to Criteo を設定したら、キャンバスを起動します。新しいオーディエンスが作成され、オーディエンス同期ステップを通過するユーザーは Criteo のこのオーディエンスに送られます。キャンバスに後続のコンポーネントが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

Criteo でオーディエンスを表示するには、広告マネージャーアカウントにログインし、ナビゲーションの**オーディエンス** からセグメントを選択します。**セグメント**ページから、各オーディエンスが～1,000に達した後のサイズを見ることができます。

![セグメント、ID、ソース、タイプ、サイズ、現在使用中であるかどうか、および最終更新日時を示すオーディエンスライブラリ。][0]

## ユーザーの同期とレート制限の考慮事項

ユーザーがオーディエンス同期ステップに到達すると、Braze は Criteo の API レート制限を尊重しながら、これらのユーザーをほぼリアルタイムで同期します。これが実際に意味するのは、Brazeは5秒ごとにできるだけ多くのユーザーをバッチ処理してからSnapchatに送るということを示します。

Criteo の API レート制限では、1分あたりに250のリクエストを超えないように設定されています。Brazeの顧客がこのレート制限に達した場合、Braze the Canvasは最大13時間まで同期を再試行します。同期が不可能な場合、これらのユーザーは「ユーザーエラー」メトリックにリストされます。 

## 分析の理解

次の表に、オーディエンス同期コンポーネントからの分析をよりよく理解するのに役立つ指標と説明を示します。

| 指標 | 説明 |
| --- | --- |
| 入力 | Criteo と同期するためにこのコンポーネントに入ったユーザーの数。 |
| 次のステップに進む | 次のコンポーネントがある場合、次のコンポーネントに進んだユーザーの数。これがキャンバスブランチの最後のステップである場合、すべてのユーザーは自動的に進みます。 |
| ユーザーの同期 | Criteo に正常に同期されたユーザー数。 |
| 同期されていないユーザー | 一致するフィールドが不足しているため、同期されていないユーザーの数。 |
| 保留中のユーザー | BrazeがCriteoに同期するために現在処理しているユーザー数。 |
| エラーが発生したユーザー数 | 約13時間の再試行後、APIエラーによりCriteoに同期されなかったユーザー数。エラーの原因としては、Criteo トークンが無効である場合や、Criteo でオーディエンスが削除された場合などが考えられます。 |
| 終了済みのキャンバス | キャンバスを終了したユーザーの人数。これは、キャンバスの最後のステップがオーディエンス同期コンポーネントである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
一括フラッシャーと13時間の再試行のために、同期されたユーザーとエラーが発生したユーザーの指標のレポートに遅延が発生することに注意してください。
{% endalert %}

## トラブルシューティング

{% details 無効なトークンエラーが表示された場合、次に何をすればよいですか？ %}
Criteo パートナーページで Criteo アカウントの接続を解除してから再接続できます。同期する広告アカウントに対する適切なアクセス許可があることを Criteo 管理者に確認します。
{% enddetails %}

{% details なぜキャンバスは起動できないのでしょうか？ %}
Criteo パートナーページで、Criteo 広告アカウントが Braze に正常に接続されていることを確認してください。

広告アカウントを選択し、新しいオーディエンスの名前を入力し、一致するフィールドを選択していることを確認してください。
{% enddetails %}

{% details ユーザーを Criteo に渡した後、ユーザーが一致したかどうかを知るにはどうすればよいですか? %}
Criteoは、自社のデータ・プライバシー・ポリシーについて、この情報を提供していません。
{% enddetails %}

{% details Criteo がサポート可能なオーディエンス数は? %}
現時点では、Criteo アカウントに含めることができるオーディエンスの数は1,000です。 

この制限を超えると、Braze は新しいオーディエンスを作成できないことを通知します。 

Criteo の広告アカウントにログインして、使用していないオーディエンスを削除する必要があります。
{% enddetails %} 

[0]: {% image_buster /assets/img/criteo/criteo.png %}
[1]: {% image_buster /assets/img/criteo/criteo1.png %}
[2]: {% image_buster /assets/img/criteo/criteo2.png %}
[3]: {% image_buster /assets/img/criteo/criteo3.png %}
[4]: {% image_buster /assets/img/criteo/criteo4.png %}
[5]: {% image_buster /assets/img/criteo/criteo5.png %}
[6]: {% image_buster /assets/img/criteo/criteo6.png %}
[7]: {% image_buster /assets/img/criteo/criteo7.png %}
[8]: {% image_buster /assets/img/criteo/criteo8.png %}
[9]: {% image_buster /assets/img/criteo/criteo9.png %}
[10]: {% image_buster /assets/img/criteo/criteo10.png %}
[11]: {% image_buster /assets/img/criteo/criteo11.png %}
[12]: {% image_buster /assets/img/criteo/criteo12.png %}
