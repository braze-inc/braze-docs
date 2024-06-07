---
nav_title: "ポスト:ユーザー設定センターを作成"
article_title: "ポスト:ユーザー設定センターを作成"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、プリファレンスセンターの Braze エンドポイントの作成について詳しく説明します。"

---
{% api %}
# ユーザー設定センターを作成
{% apimethod post %}
/preference_center/v1
{% endapimethod %}

> このエンドポイントを使用してプリファレンスセンターを作成し、ユーザーがメールキャンペーンの通知設定を管理できるようにします。API [で生成されたプリファレンスセンターを構築する手順については、「API によるプリファレンスセンターの作成]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/#create-a-preference-center-via-api)」を参照してください。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e15d7065-2cbc-4eb3-ae16-32efe43357a6 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`preference_center.update`権限のある [API キーが必要です]({{site.baseurl}}/api/basics#rest-api-key/)。

## レート制限

このエンドポイントのレート制限は、ワークスペースごとに 1 分あたり 10 リクエストです。

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "name": "string",
  "preference_center_title": "string",
  "preference_center_page_html": "string",
  "confirmation_page_html": "string",
  "state": (optional) Choose `active` or `draft`. Defaults to `active` if not specified,
  "options": {
    "meta-viewport-content": "string", (optional) Only the `content` value of the meta tag
  }
}
```

## リクエストパラメーター

| パラメーター | 必須 | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `name` | 必須 | 文字列 | 以下の要件を満たすプリファレンスセンターの名前:<br>-文字、数字、ハイフン、アンダースコアのみを含む <br>-スペースなし |
| `preference_center_title` | オプション | 文字列 | プリファレンスセンターと確認ページのタイトル。タイトルが指定されていない場合、ページのタイトルはデフォルトで「プリファレンスセンター」になります。|
| `preference_center_page_html` | 必須 | 文字列 | プリファレンスセンターページのHTML。|
| `confirmation_page_html` | 必須 | 文字列 | 確認ページのHTML。|
| `state` | オプション | 文字列 | `active` またはを選択してください`draft`。`active`指定しない場合はデフォルトです。|
| `options` | オプション | オブジェクト | 属性:`meta-viewport-content`.存在する場合、`viewport``content= <value of attribute>`メタタグがでページに追加されます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
プリファレンスセンター名は、作成後は編集できません。
{% endalert %}

### 液体タグ

プリファレンスセンターページでユーザーのサブスクリプション状態を生成するには、HTMLに含めることができる以下のLiquidタグを参照してください。

{% raw %}

#### ユーザーサブスクリプションの状態

| リキッド | 説明 |
| --------- | ---------|
| `{{subscribed_state.${email_global}}}` | ユーザーのグローバルな電子メール購読状態（「opted_in」、「購読済み」、「購読解除」など）を取得する。|
| `{{subscribed_state.${<subscription_group_id>}}}` | ユーザーの指定されたサブスクリプショングループのサブスクライブ状態（「サブスクライブ済み」や「サブスクライブ解除」など）を取得する。|
{: .reset-td-br-1 .reset-td-br-2}

#### フォーム入力とアクション

| リキッド | 説明 |
| --------- | ---------|
| `{% form_field_name :email_global_state %}` | 特定のフォーム入力要素がユーザーのグローバル電子メール購読状態に対応することを示します。グローバル電子メール購読状態の選択データとともにフォームが送信される場合、ユーザーの選択状態は「opted\_in」、「subscribed」、または「unsubscribed」である必要があります。チェックボックスの場合、ユーザーは「opted\_in」または「unsubscribe」になります。非表示の入力の場合、「サブスクライブ済み」状態も有効です。|
| `{% form_field_name :subscription_group <subscription_group_id> %}` | 特定のフォーム入力要素が特定のサブスクリプショングループに対応することを示します。特定の購読グループの選択データを含むフォームを送信する場合、ユーザーの選択状態は「購読済み」または「購読解除」のいずれかでなければなりません。|
| `{{preference_center_submit_url}}` | フォーム送信用のURLを生成します。|
{: .reset-td-br-1 .reset-td-br-2}

{% endraw %}

## レスポンス例
{% raw %}
```
{
  "preference_center_api_id": "preference_center_api_id_example",
  "liquid_tag": "{{preference_center.${MyPreferenceCenter2022-09-22}}}",
  "created_at": "2022-09-22T18:28:07+00:00",
  "message": "success"
}
```
{% endraw %}

{% endapi %}
