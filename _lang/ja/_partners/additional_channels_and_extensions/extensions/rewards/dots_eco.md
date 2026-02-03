---
nav_title: DOTS.ECO
article_title: DOTS.ECO
description: "この参考記事では、BrazeとDOTS.ECOの統合について説明している。"
alias: /partners/dots.eco/
page_type: partner
search_tag: Partner
---

# DOTS.ECO

> [DOTS.ECO](https://dots.eco) は、追跡可能なデジタル証明書を通じて、ユーザーに実際の環境影響を報酬として与えることができる。各証明書には、共有可能な証明書URLや画像写真URLなどのメタデータを含めることができるため、ユーザーは影響力の証明を閲覧（および再確認）することができる。

_この統合は DOTS.ECO によって管理されます。_

## この統合について

BrazeとDOTS.ECO は、カスタマーエンゲージメントの旅を現実世界のインパクト報酬につなげる。Braze キャンバスまたはキャンペーンステップから、コネクテッドコンテンツを使用して、DOTS.ECO 証明書作成リクエストをトリガーすることができます。DOTS.ECO は、カスタム属性として顧客プロファイルに保存し、アプリ内メッセージ、コンテンツカード、プッシュ通知などのチャネル全体で再利用できる証明書メタデータ（`certificate_url` や`certificate_image_url` など）を返します。

## ユースケース

- ユーザーがキーイベント（購入、レベル完了、サブスクリプション、紹介）を完了すると、インパクト証明書をトリガーする。
- コネクテッドコンテンツのステップ成功後、アプリ内メッセージでパーソナライズされた証明書画像を表示する。
- 証明書のURLを記載した「証明書を見る」コンテンツカードを追加し、後でアクセスできるようにする。
- 証明書メタデータ（`certificate_url` 、`certificate_image_url` 、`certificate_header` 、`greeting` など）をカスタム属性として保存し、将来のメッセージングで再利用できるようにする。
- リモート・ユーザーIDを使用して証明書を割り当てることで、ユーザーが証明書を請求し、後でその影響を確認することができる。
- 同じDOTS.ECO ユーザー更新フローを維持しながら、インパクトメッセージング（異なるコピー/画像）のABテストを実施する。


## 前提条件

始める前に、以下のものが必要だ：

| 前提条件 | 説明 |
|---|---|
| DOTS.ECO アカウント | DOTS.ECO アカウントにアクセスする。 |
| DOTS.ECO 認証情報 | この記事のリクエストには、DOTS.ECO アプトークン、APIキー、アロケーションIDが必要である。これらの情報を入手するには、DOTS.ECO のカスタマー・サクセス・マネージャーに連絡すること。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。ダッシュボードの**「設定」**>「**APIキー**」でこのキーを作成する。 |
| Braze RESTエンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合 DOTS.ECO

### ステップ 1: キャンバスを作成し、ユーザー更新ステップを追加する。

Brazeダッシュボードで、ユーザーがキーイベント（購入、サブスクリプション、マイルストーンなど）を完了したときにトリガーする新しいキャンバスを作成する。

エントリステップの直後にユーザー更新ステップを追加する。このステップは、コネクテッドコンテンツ経由でDOTS.ECO APIを呼び出し、返された証明書データをユーザープロファイルに保存するために使用される。

このステップを使用して、コネクテッドコンテンツ経由でDOTS.ECO API を呼び出し、返された証明書データをユーザープロファイルに保存する。

### ステップ 2:高度なJSONを構成する：コネクテッド・コンテンツを使ってDOTS.ECO 、POSTリクエストを行う。

**ユーザー更新**ステップで、**アドバンスドJSONエディターに**切り替え、コネクテッドコンテンツを使用して、DOTS.ECO 証明書APIにPOSTリクエストを行う。

DOTS.ECO の証明書エンドポイントを呼び出すには、`capture` タグとコネクテッドコンテンツリクエストを使用する。そして、ユーザープロファイルにカスタム属性としてレスポンスを保存する。

**コネクテッドコンテンツとユーザー更新の例**  
{% raw %}
```  
{% capture post_body %} 
{  
  "remote_user_email": "{{${email_address} | default: 'braze+nadav@dots.eco'}}",  
  "app_token": "YOUR_DOTS.ECO_APP_TOKEN",  
  "impact_qty": 1,  
  "remote_user_id": "{{${user_id} | default: ${braze_id}}}",  
  "allocation_id": "YOUR_DOTS.ECO_ALLOCATION_ID"  
}  
{% endcapture %}

{% connected_content https://impact.dots.eco/api/v1/certificate/add?format=sdk  
  :method post  
  :headers { "auth-token": "YOUR_DOTS.ECO_AUTH_TOKEN" }  
  :body {{post_body}}  
  :content_type application/json  
  :save result  
%}

{  
  "attributes": [  
    {  
      "certificate_image_url": "{{result.certificate_image_url}}",  
      "certificate_url": "{{result.certificate_url}}",  
      "certificate_id": "{{result.certificate_id}}"  
    }  
  ]  
}  
```
{% endraw %}

`https://impact.dots.eco/api/v1/certificate/add?format=sdk` にリクエストを送る。

![DOTS.ECO ユーザー更新ステップ。]({% image_buster /assets/img/dots_eco/dotseco_user_update.png %})

{% alert important %}  
この統合では、キャンバス**ユーザー更新**ステップ内部でコネクテッドコンテンツを使用し、DOTS.ECO APIを呼び出す。トークンとペイロードを検証するために、まずAPIクライアント（例えばPostman）でリクエストをテストする。  
{% endalert %}

### ステップ 3:証明書をメッセージングで表示する

証明書の属性がユーザープロファイルに保存されると、下流のキャンバスメッセージステップで参照できるようになる。

![DOTS.ECO が流れる。]({% image_buster /assets/img/dots_eco/dots.eco_flow.png %})

![DOTS.ECO メッセージングのステップだ。]({% image_buster /assets/img/dots_eco/dotseco_messages.png %})

![DOTS.ECO メッセージ作成画面セクション。]({% image_buster /assets/img/dots_eco/dotseco_messages_compose.png %})

以下に例を示します。  
- を使用してアプリ内メッセージに証明書画像を表示する。 {% raw %}`{{custom_attribute.${certificate_image_url}}}`{% endraw %}  
- を使用してホスト証明書にリンクする。 {% raw %}`{{custom_attribute.${certificate_url}}}`{% endraw %}

![DOTS.ECO メッセージをクリックしたときの動作。]({% image_buster /assets/img/dots_eco/dotseco_messages_compose_onclickbehavior.png %})


これにより、アプリ内メッセージ、コンテンツカード、プッシュ通知をインパクト確認でパーソナライズさせることができる。

## トラブルシューティング

Brazeダッシュボードの**「設定**」>「**メッセージアクティビティログ**」でコネクテッドコンテンツエラーを確認する。

- **コネクテッド・コンテンツは空を返す**：`:save result` が設定され、期待されるレスポンスフィールドを参照していることを確認する。
- **アトリビューションがメッセージステップに表示されていない**：
  - Brazeのカスタム属性名が、ユーザー更新ステップで設定した属性と完全に一致していることを確認する。
  - ユーザー更新ステップで、**プレビューとテスト**タブを使い、属性が入力されたことを確認する。その後、ユーザーにテストを送信し、ユーザープロファイルに属性が保存されていることを確認する。
- **`422` エラー（処理不能なエンティティ）**：アプリトークンとインパクト数が有効であることを確認する。
- **`401` エラー**:認証トークンが存在し、正しいことを確認する。
- **メッセージングステップに画像, 写真のプレビューがない**：ユーザー更新ステップで**Send Test to Userを**選択し、同じユーザーを使ってメッセージをプレビューする。