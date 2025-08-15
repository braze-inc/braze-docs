---
nav_title: OneTrust
article_title: OneTrust
description: "このリファレンス記事では、Braze と OneTrust のパートナーシップについて説明します。OneTrust は、データプライバシーおよびセキュリティソフトウェアのプロバイダーであり、お客様は OneTrust ワークフロービルダーを使用して自社製品のセキュリティワークフローを作成できます。"
alias: /partners/onetrust/
page_type: partner
search_tag: Partner

---

# OneTrust

> [OneTrust](https://www.onetrust.com/) は、プライバシーおよびセキュリティソフトウェアのプロバイダーであり、信頼の状況、強力なインサイトを活用するためのアクション、そして競争で常に優位に立つためのオートメーションをより詳しく理解するために必要な可視化機能を提供します。 

_この統合は OneTrust によって管理されます。_

## 統合について

Braze とOneTrust の統合により、OneTrust ワークフロービルダーを使用してプロダクトのセキュリティワークフローを作成できます。
## 前提条件

| 要件 | 説明 |
|---|---|
| OneTrust アカウント | このパートナーシップを活用するには、[OneTrust](https://www.onetrust.com/) アカウントが必要です。 |
| BrazeのAPIキー | OneTrust アクションが使用するエンドポイントに必要な権限を持つBraze REST API キー。<br><br>これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| Brazeインスタンス | Braze インスタンスは Braze オンボーディングマネージャーから入手できます。また、[API 概要ページ]({{site.baseurl}}/api/basics/#endpoints)でも確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

次の統合では、ユーザー同意更新ワークフローとユーザー削除ワークフローを作成するためのガイダンスを提供します。追加でサポートされるBraze エンドポイントの詳細については、[サポートされる他のアクションs](#Other-supported-actions)を参照してください。

### OneTrust に Braze 認証情報を追加する

OneTrust **Integrations** メニューで、**Credentials**> **Add New** ボタンに移動して、**Select System** 画面を表示します。ここで、**Braze**を見つけ、**Next**ボタンをクリックします。

[**Enter Credential Details**] 画面のプロンプトに従って、次の情報を入力します。完了したら、認証情報を保存します。
  - 認証情報名
  - コネクタータイプを**Webアプリ**に設定します。
  - ホスト名: `<your-braze-instance-url>`
  - **リクエストヘッダー**:
    - **Authorization**:Bearer
    - **Content-Type**: application/json
  - トークン: `<your-braze-api-key>`

### Braze をシステムとして追加する

#### ステップ1:ワークフローの作成

{% tabs %}
{% tab ユーザー同意の更新 %}
1. OneTrust 統合メニューで [**Gallery**] > [**Braze**] > [**Add**] に移動し、新しいワークフローを作成します。![]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. ワークフローモーダルに名前と通知 メールを入力します。**Create**ボタンをクリックします。作成時に Workflow Builder が表示されます。Brazeワークフローには、削除リクエストの処理に使用できるAPI コールとアクションがシードされます。<br><br>
3. Workflow Builder で、ワークフローでトリガーするアクションを選択します。<br>![]({% image_buster /assets/img/onetrust/onetrust2.png %})

{% endtab %}
{% tab ユーザー削除 %}

1. OneTrust 統合メニューで [**Gallery**] > [**Braze**] > [**Add**] に移動し、新しいワークフローを作成します。![]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. ワークフローモーダルに名前と通知 メールを入力します。**Create**ボタンをクリックします。作成時に Workflow Builder が表示されます。Brazeワークフローには、削除リクエストの処理に使用できるAPI コールとアクションがシードされます。<br><br>
3. Workflow Builder で、ワークフローでトリガーするアクションを選択します。<br>![]({% image_buster /assets/img/onetrust/onetrust8.png %})
{% endtab %}
{% endtabs %}

#### ステップ2:アクションの選択
{% tabs %}
{% tab ユーザー同意の更新 %}

1. 完了したら、**Done**をクリックし、**Add Action**を選択します。選択するアクションは、更新される設定のタイプと使用するエンドポイントによって異なることに注意してください。
- ユーザーのグローバルサブスクリプション設定を更新するには、**POST ユーザートラック-属性s**アクションを選択します。
- ユーザーのサブスクリプショングループ設定を更新するには、**POST ユーザー Track - Attributes**アクションまたは**POST Set ユーザー s サブスクリプショングループ Status**アクションを選択します。<br>![]({% image_buster /assets/img/onetrust/onetrust4.png %})<br><br>
2. 目的のアクションを選択し、以前に作成したBraze 認証情報s を選択して、**Next** をクリックします。<br>![]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% tab ユーザー削除 %}

1. 完了したら、**Done**をクリックし、**Add Action**を選択します。
- ユーザーをBrazeから削除するには、**POST ユーザー 削除アクション** アクションを選択します。
<br>![]({% image_buster /assets/img/onetrust/onetrust9.png %})<br><br>
2. 目的のアクションを選択し、以前に作成したBraze 認証情報s を選択して、**Next** をクリックします。<br>![]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% endtabs %}
#### ステップ3:更新リクエストボディ
{% tabs %}
{% tab ユーザー同意の更新 %}

1. 本文を更新して、必要なすべてのダイナミック値を含めます。アクションの本体が[`/users/track` エンドポイント](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/) と[`/subscription/status/set` エンドポイント](https://www.braze.com/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) に一致することを確認します。
2. 組織のニーズを満たすように、追加のパラメータまたは条件付きロジックを使用してワークフローをカスタマイズします。
3. 編集が終了したら、**Finish**をクリックし、次に**Activate**をクリックしてワークフローを有効にします。

{% alert note %}
OneTrust ワークフローを使用して Braze でサブスクリプショングループの設定を更新する場合、`subscription_group_id` は、サブスクリプショングループの作成時に Braze により設定された ID と一致している必要があります。サブスクリプショングループの`subscription_group_id` にアクセスするには、Braze ダッシュボードの**サブスクリプショングループ** ページに移動します。
{% endalert %}

![]({% image_buster /assets/img/onetrust/onetrust6.png %})

{% endtab %}
{% tab ユーザー削除 %}

1. 本文を更新して、必要なすべてのダイナミック値を含めます。アクションの本体が[`/users/delete`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)と一致することを確認します。
2. 編集が終了したら、**Finish**、**Activate**を選択してワークフローを有効にします。

![]({% image_buster /assets/img/onetrust/onetrust10.png %})

#### データ主体の要求ワークフローを更新する
1. [**Privacy Rights Automation**] メニューで [**Workflows**] を選択します。 
2. Brazeインテグレーションで更新するワークフローを選択します。 
3. **編集**ボタンを選択して編集を有効にします。
4. 次に、ワークフローステップを選択してBrazeインテグレーションを追加し、**接続の追加**をクリックします。
5. 以前に作成したBrazeワークフローをシステムサブタスクとして追加します。

{% endtab %}
{% endtabs %}

## サポートされるその他のアクション

**POST ユーザートラック- 属性**、**POST ユーザー設定サブスクリプショングループステータス**、および**POST ユーザー削除** アクションs に加えて、Braze は、カスタムワークフローを作成し、既存のワークフロー内でサブタスクとして使用できる他のエンドポイントをサポートします。 

サポートされているアクションの一覧を表示するには
1. OneTrust で、**Integrations** メニューから**Systems** をクリックします。 
2. **Braze** システムを選択します。
3. **Actions** タブに移動します。

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
