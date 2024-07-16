---
nav_title: Criteo
article_title:キャンバスオーディエンスがCriteoに同期する
description:"この参考記事では、Braze Audience SyncをCriteoに使用し、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について解説する。"
page_order:4
alias: "/audience_sync_criteo/"

Tool:
  - キャンバス
---

# オーディエンスがCriteoに同期する

Braze Audience Sync to Criteoを利用することで、ブランドは自社のBrazeインテグレーションからCriteoの顧客リストにユーザーデータを追加し、行動トリガーやセグメンテーションなどに基づいた広告配信を行うことができる。通常、ユーザーデータに基づいてBrazeキャンバスでメッセージ（プッシュ、メール、SMS、Webhookなど）をトリガーするために使用する基準はすべて、Criteoの顧客リストでそのユーザーへの広告をトリガーするために使用することができます。

**オーディエンス・シンクの一般的なユースケースには以下のようなものがある：**

- 複数のチャネルを通じて価値の高いユーザーをターゲットにし、購買やエンゲージメントを促進する。
- 他のマーケティングチャネルでレスポンシブの低いユーザーをリターゲティングする。
- サプレッション・オーディエンスを作成することで、ユーザーがすでにブランドのロイヤルティの高い消費者である場合に、広告を受け取らないようにする。
- Lookalikeオーディエンスを作成し、より効率的に新規ユーザーを獲得する

この機能により、ブランドはCriteoと共有する特定のファーストパーティデータをコントロールできる。Brazeでは、ファーストパーティデータを共有できる統合とできない統合を最大限に考慮している。詳細については、当社の[プライバシー](https://www.braze.com/privacy)ポリシーを参照のこと。

{% alert important %}
**オーディエンス・シンク・プロの免責事項**<br>
Braze Audience Sync to Criteoは、Audience Sync Proとの統合である。この統合の詳細については、Brazeアカウントマネージャーに問い合わせを。<br> 
{% endalert %}

## 前提条件 

Criteoへのオーディエンスシンクを設定する前に、以下の項目を作成または完了していることを確認する必要がある。

| 必要条件 | Origin | 説明 |
| --- | --- | --- |
| Criteo広告アカウント | [クリテオ](https://marketing.criteo.com/) | Criteoの広告アカウントは、あなたのブランドに関連付けられている。<br><br>Criteoの管理者がオーディエンスにアクセスするための適切な権限を付与していることを確認する。 |
| [Criteo広告ガイドライン](https://www.criteo.com/advertising-guidelines/)<br>そして<br>[Criteoブランド・セーフティ・ガイドライン](https://www.criteo.com/wp-content/uploads/2017/11/Criteo-Brand-Safety-Guidelines-UK-March-2016.pdf) | Criteo | Criteoのアクティブな顧客として、Criteoのキャンペーンを開始する前に、Criteoの広告およびブランドセーフティガイドラインを遵守できることを確認する必要がある。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合 

### ステップ1:Criteoに接続する

Brazeのダッシュボードで、**パートナー連携**＞**テクノロジー**パートナーと進み、**Criteoを**選択する。Criteo Audience Exportモジュールで、**Connect Criteoを**クリックする。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**統合**」の下に**テクノロジーパートナーが**ある。
{% endalert %}

![BrazeのCriteoテクノロジーページには、OverviewモジュールとCriteoモジュール（Connected Criteoボタン付き）が含まれている。][5]{: style="max-width:80%;"}

CriteoのoAuthページが表示され、オーディエンスシンク統合に関連する権限をBrazeに承認する。

確認を選択すると、Brazeに戻り、同期したいCriteo広告アカウントを選択する。 

![Criteoに接続可能な広告アカウントのリスト。][7]{: style="max-width:80%;"}

接続に成功すると、パートナーページに戻り、どのアカウントが接続されているかを確認したり、既存のアカウントを切断したりすることができる。

![Criteoテクノロジーパートナーのページが更新され、接続に成功した広告アカウントが表示されている。][4]{: style="max-width:80%;"}

Criteo接続はBrazeワークスペースレベルで適用される。Criteo管理者がCriteo広告アカウントからあなたを削除した場合、Brazeは無効なトークンを検出する。その結果、Criteoを使用しているアクティブキャンバスにエラーが表示され、Brazeはユーザーを同期できなくなる。

### ステップ2:キャンバスのエントリ基準を設定する

広告トラッキングのオーディエンスを構築する際、ユーザーの嗜好に基づき、また、[CCPAに](https://oag.ca.gov/privacy/ccpa)基づく「販売または共有しない」権利などのプライバシー法を遵守するために、特定のユーザーを含めたり除外したりしたい場合がある。マーケターは、キャンバスのエントリ基準の中で、ユーザーの適格性に関する関連フィルターを実装する必要がある。以下にいくつかの選択肢を挙げる。

[Braze SDKを通じてiOS IDFAを]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection)収集した場合、Ads Tracking Enabledフィルターを使用できるようになる。ユーザーがオプトインしたAudience Sync送信先のみにユーザーを送信するには、値をtrueに選択する。

![][11]

`opt-ins` 、`opt-outs` 、`Do Not Sell Or Share` 、またはその他の関連するカスタム属性を収集している場合は、フィルターとしてキャンバスのエントリ条件にこれらを含める必要がある：

![][12]

Brazeプラットフォーム内でこれらのデータ保護法を遵守する方法の詳細については、[データ保護テクニカルアシスタンスを]({{site.baseurl}}/dp-technical-assistance/)参照のこと。

### ステップ3:Criteoでオーディエンス同期ステップを追加する

キャンバスにコンポーネントを追加し、**オーディエンス・シンクを**選択する。

![キャンバスフローにCriteo Audienceコンポーネントを追加する前のステップのワークフロー。][9]{: style="max-width:35%;"}![キャンバスフローにCriteo Audienceコンポーネントを追加する前のステップのワークフロー。][10]{: style="max-width:28%;"}

### ステップ 4:シンクの設定

**カスタム・オーディエンス・**ボタンをクリックして、コンポーネント・エディターを開封する。

オーディエンスシンクパートナーとして**Criteoを**選択する。 

![][6]

次に、希望のCriteo広告アカウントを選択する。**Choose a New or Existing Audience（新規または既存のオーディエンスを選択**）ドロップダウンで、新規または既存のオーディエンスの名前を入力する。

{% tabs %}
{% tab Create a New Audience %}
**新しいオーディエンスを作る**<br>
新しいオーディエンスの名前を入力し、**Add Users to Audienceを**選択し、Criteoと同期したいフィールドを選択する。次に、ステップエディタの下部にある**Create Audience**ボタンをクリックして、オーディエンスを保存する。

![Expanded view of the Custom Audience Canvas step. Here, the desired Ad account is selected, and a new audience is created.]({% image_buster /assets/img/criteo/criteo3.png %})

オーディエンスの作成に成功した場合、またはこのプロセス中にエラーが発生した場合、ステップエディタの上部にユーザーに通知される。また、オーディエンスは下書きモードで作成されたため、ユーザーはキャンバスの旅の後半でユーザーを削除するためにこのオーディエンスを参照することができる。

![An alert that appears after a new audience is created in the Canvas component.]({% image_buster /assets/img/criteo/criteo1.png %})

新しいオーディエンスでキャンバスを立ち上げると、Brazeは、ユーザーがオーディエンス同期コンポーネントに入ると、ほぼリアルタイムで同期する。
{% endtab %}
{% tab Sync with an Existing Audience %}
**既存のオーディエンスに同期する**<br>
Brazeはまた、既存のCriteoオーディエンスにユーザーを追加し、これらのオーディエンスが最新であることを確認する機能も提供している。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンス名を入力し、**オーディエンスに追加**する。Brazeは、ユーザーがオーディエンス・シンク・コンポーネントに入ると、ほぼリアルタイムでユーザーを追加する。

![Expanded view of the Custom Audience Canvas step. Here, the desired Ad account and existing audience are selected.]({% image_buster /assets/img/criteo/criteo8.png %})

{% endtab %}
{% endtabs %}

### ステップ 5: キャンバスを立ち上げる

オーディエンスシンクをCriteoに設定したら、キャンバスを起動するだけ！新しいオーディエンスが作成され、オーディエンス同期ステップを通過したユーザーはCriteoのこのオーディエンスに渡される。キャンバスに後続のコンポーネントが含まれていれば、ユーザーはユーザージャーニーの次のステップに進むことができる。

Criteoでオーディエンスを表示するには、広告マネージャーのアカウントに入り、ナビゲーションの**オーディエンスライブラリーから**セグメンテーションを選択する。**セグメンテーション**ページから、各オーディエンスが～1,000に達した後のサイズを見ることができる。

![オーディエンス・ライブラリーは、セグメンテーション、ID、ソース、タイプ、サイズ、現在使用中、最終更新を表示する。][0]

## ユーザー同期とレート制限に関する考慮事項

ユーザーがオーディエンスシンクのステップに達すると、BrazeはCriteoのAPIレート制限を尊重しながら、ほぼリアルタイムでこれらのユーザーをシンクする。これが実際に意味するのは、Brazeは5秒ごとにできるだけ多くのユーザーをバッチ処理してからSnapchatに送るということだ。

CriteoのAPIレート制限では、1分間に250リクエストまでとなっている。Brazeの顧客がこのレート制限に達した場合、Braze the Canvasは最大13時間まで同期を再試行する。同期が不可能な場合、これらのユーザーはUsers Erroredメトリックの下にリストされる。 

## 分析を理解する

以下の表は、オーディエンス・シンク・コンポーネントの分析をよりよく理解するための指標と説明を含んでいる。

| メートル | 説明 |
| --- | --- |
| 入団 | Criteoに同期されるこのコンポーネントを入力したユーザーの数。 |
| 次のステップへ進む | 次のコンポーネントがある場合、何人のユーザーが次のコンポーネントに進んだか。キャンバスブランチの最後のステップであれば、すべてのユーザーが自動で進む。 |
| 同期されたユーザー | Criteoとの同期に成功したユーザー数。 |
| 同期されていないユーザー | 一致するフィールドがないために同期されなかったユーザーの数。 |
| ユーザー申請中 | 現在BrazeがCriteoに同期するために処理しているユーザー数。 |
| エラーになったユーザー | 約13時間の再試行後、APIエラーによりCriteoに同期されなかったユーザー数。エラーの原因としては、無効なCriteoトークン、またはオーディエンスがCriteo上で削除された場合などが考えられる。 |
| イグジット・キャンバス | キャンバスから退出したユーザーの数。これは、キャンバスの最後のステップがオーディエンス・シンク・コンポーネントである場合に発生する。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
バルク・フラッシュと13時間のリトライのため、同期したユーザーとエラーになったユーザーのメトリクスのレポートにはそれぞれ遅れが生じることを覚えておいてほしい。
{% endalert %}

## トラブルシューティング

{% details What should I do next if I receive an invalid token error? %}
Criteoアカウントは、Criteoパートナーページで簡単に切断・再接続できる。Criteoの管理者に、同期したい広告アカウントに適切な権限があることを確認する。
{% enddetails %}

{% details Why is my Canvas not allowed to launch? %}
Criteoパートナーページで、Criteo広告アカウントがBrazeに正常に接続されていることを確認する。

広告アカウントを選択し、新しいオーディエンスの名前を入力し、一致するフィールドを選択していることを確認する。
{% enddetails %}

{% details How do I know if users have matched after passing users to Criteo? %}
Criteoは、自社のデータ・プライバシー・ポリシーについて、この情報を提供していない。
{% enddetails %}

{% details How many audiences can Criteo support? %}
現時点では、Criteoアカウント内で1,000オーディエンスしか持つことができない。 

この制限に違反した場合、Brazeは新しいオーディエンスを作成できないことを通知する。 

Criteo広告アカウントにアクセスし、使用しなくなったオーディエンスを削除する必要がある。
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
