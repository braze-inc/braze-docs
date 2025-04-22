---
nav_title: ActionIQ
article_title: ActionIQ
description: "この参考記事では、BrazeとActionIQの統合について取り上げている。この統合により、ブランドはActionIQのデータをBrazeに直接同期し、マッピングすることができる。"
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ
---

# ActionIQ

> 



## 統合について



- 
- ActionIQ で追跡されたイベントをリアルタイムで Braze に転送し、パーソナライズされ、ターゲットを絞ったキャンペーンをトリガーする
- 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| ActionIQアカウント | この統合を利用するには、ActionIQアカウントが必要である。 |
| Braze REST API キー | <br><br> |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL][1]。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### オーディエンスのメンバーシップ

この統合は、Brazeのプロファイルがセグメントに属しているかどうかを示すカスタム属性を作成することによって、ActionIQのオーディエンスメンバーシップをBrazeと同期させるために使用される。各ActionIQオーディエンスは、固有のブーリアン・カスタム属性に対応している。

作成されたカスタム属性の標準的な命名規則は次のとおりである：`AIQ_<Audience ID>_<Split ID>` 。


1. 
2. 
3. 
4.  
5. セグメントを作成した後、キャンペーンまたはキャンバスを作成する際に、オーディエンスフィルターとして選択することができる。



#### 要件

これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 

ActionIQ で、REST API キーと Braze REST エンドポイントを指定して、Braze 接続を設定します。 

Braze プラットフォームで消費者と一致するためには、アクティベーション設定に次の識別子が含まれている必要があります。
- `braze_id`
- `external_id`

### イベント



#### 要件

これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 

イベント統合は以下の情報をBrazeに送信する：
- イベント名
- 消費者識別子（`braze_id` または`external_id` ）。
- タイムスタンプ
- イベントプロパティ (エクスポート設定で追加の属性により取り込まれる)

### トリガーキャンペーン





#### 要件

これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。


- 消費者識別子（`braze_id` または`external_id` ）。
- キャンペーン ID


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.actioniq.com/