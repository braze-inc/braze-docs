---
nav_title: OneTrust
article_title:ワントラスト
description:"この参考記事では、BrazeとデータプライバシーとセキュリティソフトウェアのプロバイダーであるOneTrust社との提携について概説している。"OneTrust社のワークフロービルダーを使用して、自社製品のセキュリティワークフローを作成することができる。
alias: /partners/onetrust/
page_type: partner
search_tag:Partner

---

# ワントラスト

> [OneTrustは](https://www.onetrust.com/)、プライバシーとセキュリティのソフトウェアプロバイダであり、信頼の状況をよりよく理解するために必要な可視性、強力なインサイトを活用するためのアクション、競合他社から優位に立つためのオートメーションを提供する。 

BrazeとOneTrustの統合により、OneTrustワークフロービルダーを使用して、製品のセキュリティワークフローを作成することができる。
## 前提条件

| 要件 | 説明 |
|---|---|
| ワントラストアカウント | このパートナーシップを利用するための[OneTrust](https://www.onetrust.com/)口座。 |
| APIキー | OneTrustアクションが使用するエンドポイントに必要な権限を持つBraze REST APIキー。<br><br>これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Brazeインスタンス | Brazeインスタンスは、Brazeオンボーディングマネージャーから取得するか、[API概要ページで]({{site.baseurl}}/api/basics/#endpoints)確認できる。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

以下の統合は、ユーザー同意更新ワークフローおよびユーザー削除ワークフローを作成するためのガイダンスを提供する。追加でサポートされるBrazeエンドポイントの詳細については、「[その他サポートされるアクション](#Other-supported-actions)」を参照のこと。

### Braze認証情報をOneTrustに追加する

OneTrust**Integrations**]メニューで、\[**Credentials**] > \[**Add New**]ボタンに移動して、\[**Select System**]画面を表示する。ここで**Brazeを**見つけ、「**Next」**ボタンをクリックする。

**Enter Credential Details**画面の指示に従って、以下の情報を入力する。完了したら認証情報を保存する。
  - 認証情報名
  - コネクタータイプを**Webアプリ**に設定する
  - Hostname: `<your-braze-instance-url>`
  - **リクエストヘッダー**：
    - **認可する**：ベアラー
    - **Content-Type**: application/json
  - Token: `<your-braze-api-key>`

### システムとしてBrazeを追加する

#### ステップ1:ワークフローを作成する

{% tabs %}
{% tab User Consent Update %}
1. OneTrustの統合メニューで、**Gallery**>**Braze**>**Addに**移動し、新しいワークフローを作成する。![\]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. ワークフローモーダルに名前と通知メールを入力する。**作成**ボタンをクリックする。作成すると、ワークフ ロー・ビルダーが表示される。Brazeワークフローには、削除リクエストの処理に使用できるAPIコールとアクションがシードされる。<br><br>
3. ワークフロービルダーで、ワークフローでトリガーしたいアクションを選択する。<br>![\]({% image_buster /assets/img/onetrust/onetrust2.png %})

{% endtab %}
{% tab User Deletion %}

1. OneTrustの統合メニューで、**Gallery**>**Braze**>**Addに**移動し、新しいワークフローを作成する。![\]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. ワークフローモーダルに名前と通知メールを入力する。**作成**ボタンをクリックする。作成すると、ワークフ ロー・ビルダーが表示される。Brazeワークフローには、削除リクエストの処理に使用できるAPIコールとアクションがシードされる。<br><br>
3. ワークフロービルダーで、ワークフローでトリガーしたいアクションを選択する。<br>![\]({% image_buster /assets/img/onetrust/onetrust8.png %})
{% endtab %}
{% endtabs %}

#### ステップ2:アクションを選択する
{% tabs %}
{% tab User Consent Update %}

1. 完了したら、**Doneを**クリックし、**Add Actionを**選択する。選択するアクションは、更新されるプリファレンスの種類と、希望するエンドポイントによって異なることに注意。
- ユーザーのグローバルサブスクリプションプリファレンスを更新するには、**POST User track - attributes**アクションを選択する。
- ユーザーのサブスクリプショングループプリファレンスを更新するには、**POST User Track - Attributes**アクションまたは**POST Set Users Subscription Group Status**アクションを選択する。<br>![\]({% image_buster /assets/img/onetrust/onetrust4.png %})<br><br>
2. 希望するアクションを選択し、以前に作成したBraze認証情報を選択し、**Nextを**クリックする。<br>![\]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% tab User Deletion %}

1. 完了したら、**Doneを**クリックし、**Add Actionを**選択する。
- Brazeからユーザーを削除するには、**POST User Delete Action**アクションを選択する。
<br>![\]({% image_buster /assets/img/onetrust/onetrust9.png %})<br><br>
2. 希望するアクションを選択し、以前に作成したBraze認証情報を選択し、**Nextを**クリックする。<br>![\]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% endtabs %}
#### ステップ3:更新リクエスト本文
{% tabs %}
{% tab User Consent Update %}

1. 本文を更新し、必要なダイナミックな値を含める。アクションのボディが[`/users/track` エンド](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/)ポイントと[`/subscription/status/set` エンド](https://www.braze.com/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)ポイントと一致していることを確認する。
2. 組織のニーズに合わせて、追加パラメータや条件ロジックでワークフローをカスタマイズする。
3. 編集が終了したら、**Finishを**クリックし、**Activateを**クリックしてワークフローをイネーブルメントにする。

{% alert note %}
OneTrustワークフローを使用してサブスクリプショングループの環境設定を更新する場合、`subscription_group_id` 、サブスクリプショングループの作成時にBrazeが設定したIDと一致する必要がある。ダッシュボードの**サブスクリプショングループページに**移動すると、サブスクリプショングループの`subscription_group_id` 。
{% endalert %}

![\]({% image_buster /assets/img/onetrust/onetrust6.png %})

{% endtab %}
{% tab User Deletion %}

1. 本文を更新し、必要なダイナミックな値を含める。アクションのボディが[`/users/delete` のエンド]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)ポイントと一致していることを確認する。
2. 編集が終了したら、**Finishを**選択し、**Activateを**選択してワークフローをイネーブルメントにする。

![\]({% image_buster /assets/img/onetrust/onetrust10.png %})

#### データ対象者の要求ワークフローを更新する
1. **プライバシー権のオートメーション」**メニューで、「**ワークフロー**」を選択する。 
2. Braze統合で更新したいワークフローを選択する。 
3. **編集**ボタンを選択し、イネーブルメントを有効にする。
4. 次に、Braze統合を追加するワークフローのステップを選択し、**Add Connectionを**クリックする。
5. 先に作成したBrazeワークフローをシステムのサブタスクとして追加する。

{% endtab %}
{% endtabs %}

## その他のアクション

**POST User track - Attributes**、**POST Set Users Subscription Group Status**、**POST User Delete**アクションに加え、Brazeは、カスタムワークフローを作成したり、既存のワークフロー内のサブタスクとして使用できる他のエンドポイントもサポートしている。 

対応アクションの全リストを見る：
1. OneTrust で、**\[Integrations]**メニューから\[**Systems**]をクリックする。 
2. **Braze**システムを選択する。
3. **アクション**タブに移動する。

![][7]

[1]: {% image_buster /assets/img/onetrust/onetrust.png %}
[2]: {% image_buster /assets/img/onetrust/onetrust2.png %}
[3]: {% image_buster /assets/img/onetrust/onetrust3.png %}
[4]: {% image_buster /assets/img/onetrust/onetrust4.png %}
[5]: {% image_buster /assets/img/onetrust/onetrust5.png %}
[6]: {% image_buster /assets/img/onetrust/onetrust6.png %}
[7]: {% image_buster /assets/img/onetrust/onetrust7.png %}
[8]: {% image_buster /assets/img/onetrust/onetrust8.png %}
[9]: {% image_buster /assets/img/onetrust/onetrust9.png %}
[10]: {% image_buster /assets/img/onetrust/onetrust10.png %}
