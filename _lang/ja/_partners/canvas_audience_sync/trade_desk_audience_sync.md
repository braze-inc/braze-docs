---
nav_title: The Trade Desk
article_title: キャンバスオーディエンス同期 - The Trade Desk
description: "このリファレンス記事では、Braze Audience Sync を The Trade Desk と連携して、行動トリガー、セグメンテーションなどに基づいた広告配信を行う方法について説明します。"
alias: /trade_desk_audience_sync/
Tool:
  - Canvas
page_order: 7
---

# The Trade Desk への Audience Sync

> Braze Audience Sync to The Trade Desk を使用すると、Braze のファーストパーティユーザーデータを The Trade Desk に直接ダイナミックに同期し、広告リターゲティング、類似モデリング、抑制に活用できます。

**オーディエンス同期の一般的なユースケース:**

- The Trade Desk で既存ユーザーにパーソナライズ済みキャンペーンをリターゲティングする。
- 除外ターゲティングのためにファーストパーティデータを The Trade Desk に送信する。
- ユーザーを新規または既存のオーディエンスや CRM データセグメントに同期する。

## 前提条件

キャンバスで The Trade Desk との Audience Sync ステップを設定する前に、以下の項目が作成、完了、または承認されていることを確認してください。

| 要件 | Origin | 説明 |
| --- | --- | --- |
| API トークン | [The Trade Desk](https://partner.thetradedesk.com/v3/portal/api/doc/Authentication#ui-method-create) | The Trade Desk プラットフォームで作成された標準 API トークンです。The Trade Desk Audience Sync を使用するキャンバスへの影響を最小限に抑えるため、API トークンの有効期間を最大1年に設定することをお勧めします。 |
| The Trade Desk の利用規約とポリシー | The Trade Desk | The Trade Desk へのデータ送信を有効にするには、UID2/CRM 参加ポリシーに同意する必要があります。The Trade Desk の担当者に連絡して、The Trade Desk へのデータ配信を有効にするための適切な署名があることを確認してください。<br><br> {::nomarkdown}<ul><li>アカウントで CRM データ管理アクセスが有効になっていることを確認してください。The Trade Desk の担当者がサポートします。広告主 ID が必要です。</li><li>標準 API トークンを準備してください。このページの手順に従って生成できます。</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 統合

### ステップ 1: The Trade Desk アカウントを接続する

開始するには、**パートナー連携** > **テクノロジーパートナー** > **The Trade Desk** に移動します。Trade Desk アカウントから以下の詳細を入力してください:

- **API トークン**
- **広告主 ID 名**（このオプション名は、Audience Sync キャンバスステップで参照する広告主アカウントを識別します）
- **広告主 ID**

次に、**接続** を選択します。

![The Trade Desk の未接続の Audience Sync の例。]({% image_buster /assets/img/audience_sync/trade_desk/connect_sync.png %}){: style="max-width:90%;"}

### ステップ 2: The Trade Desk との Audience Sync ステップを追加する

キャンバスにコンポーネントを追加し、**Audience Sync** を選択します。次に、Audience Sync パートナーとして **The Trade Desk** を選択します。

![Audience Sync ステップで同期するパートナーを選択するオプション。]({% image_buster /assets/img/audience_sync/trade_desk/audience_sync_step.png %}){: style="max-width:90%;"}

### ステップ 3: 同期を設定する

次に、同期の詳細を設定します:

1. 広告アカウントを選択します。
2. 既存のオーディエンスを選択するか、新しいオーディエンスを作成します。

![オーディエンスフィールドに「valentines2025」という名前が含まれる Audience Sync の設定。]({% image_buster /assets/img/audience_sync/trade_desk/choose_audience.png %}){: style="max-width:90%;"}

{: start="3"}
3. **オーディエンスにユーザーを追加** または **オーディエンスからユーザーを削除** のいずれかのアクションを選択します。

![オーディエンスにユーザーを追加する Audience Sync の設定。]({% image_buster /assets/img/audience_sync/trade_desk/audience_sync_step2.png %}){: style="max-width:90%;"}

{: start="4"}
4. マッチングに使用するフィールドを選択します: **メール**、**電話番号**、または **モバイル広告主 ID**。

{% alert note %}
EU リージョンが設定された The Trade Desk のオーディエンスに同期する場合、電話番号は The Trade Desk でサポートされていません。EU リージョンでの電話番号サポートについては、The Trade Desk にお問い合わせください。
{% endalert %}

### ステップ 4: キャンバスを起動する

The Trade Desk への Audience Sync を設定したら、キャンバスを起動する準備が整いました。新しいオーディエンスが作成され、Audience Sync ステップを通過するユーザーは The Trade Desk のこのオーディエンスに渡されます。キャンバスに後続のコンポーネントが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

## よくある質問

### The Trade Desk でオーディエンスサイズが反映されるまでどのくらいかかりますか？

最大24時間かかる場合があります。

### 広告アカウント内で The Trade Desk が反映するための最小オーディエンスサイズはありますか？

The Trade Desk の CRM オーディエンスには最小オーディエンスサイズはありません。

### The Trade Desk にユーザーを渡した後、ユーザーがマッチしたかどうかはどのように確認できますか？

The Trade Desk では、受信した ID がセグメントの横に表示されます。

- 受信済み ID は、過去30日間に受信した ID の数です。
- アクティブ ID は、過去7日間に入札で確認された ID の数です。

### The Trade Desk はいくつのオーディエンスをサポートできますか？

The Trade Desk でサポートできるオーディエンス数に制限はありません。