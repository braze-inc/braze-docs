---
nav_title: 自動ユーザープロビジョニング
article_title: 自動ユーザープロビジョニング
page_order: 10
page_type: reference
description: "このリファレンス記事では、自動ユーザープロビジョニングを行うために提供する必要がある情報と、生成されたクロスドメイン ID 管理用システム (SCIM) トークンを使用する方法と場所について説明します。"
alias: /scim/automated_user_provisioning/

---

# 自動ユーザープロビジョニング

> SCIMプロビジョニングを使用して、APIを通じてBrazeユーザーを自動的に作成・管理する。この記事では、提供すべき情報、SCIMトークンの生成方法、SCIM APIエンドポイントの場所について説明する。

{% include early_access_beta_alert.md feature='SCIM provisioning' %}

## SCIMプロビジョニング設定にアクセスする

1. Brazeのダッシュボードで、**設定**>**管理者設定**>**SCIM Provisioningに**進み、**Configure SCIM integrationを**選択する。
2. **Braze設定**ステップで、プロビジョニング方法を選択し、アクセス設定を行う。

![SCIMの統合を設定するページで、プロビジョニング方法の選択とアクセス設定のセクションがある。]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3\.**IdP設定**ステップでは、選択したプロビジョニング方法のプラットフォーム内のステップに従う。

{% tabs %}
{% tab Okta - Braze app %}

{% include early_access_beta_alert.md feature='The Okta integration' %}

OktaでSAML SSO用にBrazeアプリを設定する場合は、**Okta - Brazeアプリオプションを**使用する。SSO用にカスタムアプリを設定した場合は、[Okta - Custom app integration]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/automated_user_provisioning/?tab=okta%20-%20custom%20app%20integration#step-1-set-up-scim-provisioning)タブの指示に従う。

## ステップ 1: SCIMプロビジョニングを設定する

### ステップ1.1：SCIM を有効にする

1. Oktaで、「**アプリケーション**」>「**アプリ**」と進み、**「アプリ統合を作成**」を選択する。サインイン方法として**SAML 2.0を**選択する。
2. 以下の詳細（Braze[**IdP設定**ステップに](#accessing-scim-provisioning-settings)ある）を入力して、カスタムアプリを作成する：
- アプリのロゴ
- シングルサインオン URL
- オーディエンス URL (サービスプロバイダーエンティティ ID)
3. [**Finish**] を選択します。
4. **全般**タブを選択する。 
5. **アプリ設定**セクションで、**編集を**選択する。
6. **Provisioning**フィールドで、**SCIMを**選択する。 

### ステップ1.2：アプリケーションの可視性を無効にする

1. **アプリケーションの表示」**フィールドで、「**ユーザーにアプリケーションアイコンを表示しない」**チェックボックスを選択する。これにより、ユーザーはSCIM専用のアプリからSSOにアクセスできなくなる。 
2. [**保存**] を選択します。

### ステップ1.3：SCIMとの統合を設定する

1. **Provisioning**タブを選択する。
2. **設定**＞**統合**＞**SCIM接続で** **編集を**選択し、**SCIMプロビジョニング設定**ページのテーブル内に入力されるフィールド値を記入する。

### ステップ1.4:API 認証情報をテストする

**Test API Credentials** を選択する。統合が成功すると確認メッセージが表示され、保存できる。

### ステップ1.5:アプリへのプロビジョニングをイネーブルメントにする

1. **Provisioning**>**Settings**>**To App**>**Provisioning to Appで**、**Editを**選択する。
2. 次を有効にする: 
    - ユーザーを作成する
    - ユーザー属性を更新する
    - ユーザーを非アクティブにする
3. **セットアップ SCIM プロビジョニングページの**表に表示されるマッピングを使用して、**アトリビューションマッピングセクションを**確認し設定する。

## ステップ2: アプリにユーザーを割り当てる

1. **割り当て**タブを選択する。
2. **Assignを**選択し、オプションを選択する。
3. Brazeにアクセスすべき人にアプリを割り当てる。
4. 課題が完了したら「**完了**」を選択する。

{% endtab %}
{% tab Okta - Custom app integration %}

{% include early_access_beta_alert.md feature='The Okta integration' %}

SSO用にカスタムアプリを設定する場合は、**Okta - カスタムアプリ統合**オプションを使用する。OktaでSAML SSO用にBrazeアプリを設定した場合は、[Okta - Brazeアプリタブの]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/automated_user_provisioning/?tab=okta%20-%20braze%20app#step-1-set-up-scim-provisioning)指示に従う。

## ステップ 1: SCIMプロビジョニングを設定する

### ステップ1.1：SCIM を有効にする

1. OktaでBrazeアプリにアクセスする。
2. **全般**タブを選択する。
3. **アプリ設定**セクションで、**編集を**選択する。
4. **Provisioning**フィールドで、**SCIMを**選択する。
5. [**保存**] を選択します。

### ステップ1.2：SCIM統合の設定

1. **Provisioning**タブを選択する。
2. **設定**＞**統合**＞**SCIM接続で**、**編集を**選択し、**SCIMプロビジョニング設定**ページのテーブル内に入力されるフィールド値を記入する。
3. **Test API Credentialsを**選択してAPI認証情報をテストする。
4. [**保存**] を選択します。

### ステップ1.3：アプリへのプロビジョニングをイネーブルメントにする

1. **Provisioning**>**Settings**>**To App**>**Provisioning to Appで**、**Editを**選択する。
2. 次を有効にする: 
    - ユーザーを作成する
    - ユーザー属性を更新する
    - ユーザーを非アクティブにする
3. **セットアップ SCIM プロビジョニングページの**表に表示されるマッピングを使用して、**アトリビューションマッピングセクションを**確認し設定する。

## ステップ2: アプリにユーザーを割り当てる

1. **割り当て**タブを選択する。
2. **Assignを**選択し、オプションを選択する。
3. Brazeにアクセスすべき人にアプリを割り当てる。
4. ［**完了**] を選択します。

{% endtab %}
{% tab Entra ID %}

{% include early_access_beta_alert.md feature='The Entra ID integration' %}

## ステップ 1: SCIMプロビジョニングアプリの設定

### ステップ1.1：Microsoft Entraの管理センターにログインする

Microsoft Entraの管理センターにログインする。

### ステップ1.2：SCIMアプリの作成と設定

1. ナビゲーションメニューで、**Entra ID**>**Enterprise appsと**進む。
2. **新規アプリケーションを**選択する。
3. **独自のアプリケーションを作成する**」を選択する。
4. パネルでアプリの名前を入力する。
5. **What are you looking to do with your application? "**セクションで、"**Integrate application you don't find in gallery (Non-gallery)**" を選択する。
6. [**作成**] を選択します。

### ステップ1.3：SCIM統合の設定

1. SCIM アプリケーションの**Manage**>**Provisioning**セクションに移動する。
2. **Connect your application（アプリケーションの接続**）または**New configuration（新規構成**）を選択し、**Setup SCIM provisioning（SCIMプロビジョニングのセットアップ**）ページの表に表示されるフィールド値を入力する。

### ステップ1.4:アプリへのプロビジョニングをイネーブルメントにする

1. SCIM アプリケーションの**Manage**>**Attribute mapping (Preview)**セクションに移動する。
2. **Provision Microsoft Entra ID Users** を選択する。
3. **Attribute Mapping**セクションを確認し、**Setup SCIM provisioning**ページのテーブル内に入力される属性と一致するように設定する。
4. **アトリビュートマッピングの**ページを閉じる。

## ステップ2: アプリにユーザーを割り当てる

1. **マネージャー**＞**ユーザーとグループと**進む。
2. **Add user/groupを**選択する。
3. アプリにユーザーを割り当てるには「**None Selected**」を選択する。
4. **Select**ボタンを選択し、割り当てを確定する。

{% endtab %}
{% tab Custom %}

## ステップ 1: SCIMの設定を行う

- **デフォルトのワークスペース:**新規ユーザーをデフォルトで追加するワークスペースを選択する。[SCIM API リクエスト]({{site.baseurl}}/post_create_user_account/)でワークスペースを指定しなかった場合、Braze はこのワークスペースにユーザーを割り当てます。
- **サービス提供元:**SCIMリクエストのオリジンドメインを入力する。Braze はこれを `X-Request-Origin` ヘッダーで使用し、リクエストがどこからのものであるかを確認します。
- **IP 許可リスト (オプション):**SCIM リクエストを特定の IP アドレスに制限できます。許可する IP アドレスのコンマ区切りリストまたは範囲を入力します。各リクエストの`X-Request-Origin` ヘッダーは、リクエストIPアドレスをallowlistと照合するために使われる。

![SCIM プロビジョニング設定フォームに3つのフィールド:デフォルトのワークスペース、サービスオリジン、およびオプションのIP Allowlisting。Generate SCIM Token "ボタンは無効になっている。]({% image_buster /assets/img/scim_unfilled.png %})

## ステップ2: SCIMトークンを生成する

必須フィールドを入力してから [**SCIM トークンを生成**] を押すと、SCIM トークンが生成され、SCIM API エンドポイントが表示されます。他へ移動する前に SCIM トークンをコピーしておいてください。**このトークンは一度しか現れない。** 

![[SCIM API エンドポイント] フィールドと [SCIM トークン] フィールドに、マスクされた値とコピーボタンが表示されている。トークン・フィールドの下には「トークンをリセット」ボタンがある。]({% image_buster /assets/img/scim.png %})

Braze では、すべての SCIM リクエストに HTTP `Authorization` ヘッダー経由で添付された SCIM API ベアラートークンが含まれている必要があります。

{% endtab %}
{% endtabs %}
