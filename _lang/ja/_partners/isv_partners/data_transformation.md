---
nav_title: データ変換
hidden: true
---

# Braze Data Transformation

> Braze [データ変換]({{site.baseurl}}/data_transformation/)は、パートナープラットフォームからのWebhookを取り込み、顧客がそのWebhookのペイロードをBrazeユーザープロファイル上の属性、イベント、購入などの目的のユーザーデータに変換するためのマッピングを定義できるようにします。

## Data Transformation に基づく統合の仕組み

Data Transformation 機能に基づくパートナー連携は、公開ドキュメントを通じて顧客と共有される変換コードテンプレートである可能性があります。

共通のお客様にとっては、次のようになります。

1. 彼らはあなたのプラットフォームにログインし、webhookを設定します。
2. Braze チームと連携して Braze Data Transformation にアクセスし、Braze ダッシュボード内に新しい変換を作成します。
3. 変換によって生成されたURLがコピーされます。
4. Brazeに戻って、コピーした変換URLにテストWebhookを送信します。
5. Brazeでは、変換コードテンプレートをコピーして貼り付けます。
6. 変換を有効にします。
7. 有効にすると、Brazeユーザー検索ツールを使用して、Webhookに基づいてユーザープロファイルが更新されていることを確認し、必要に応じて変換コードを編集できます。

{% alert tip %}
Braze に送信される Webhook タイプごとに変換を作成することをお勧めします。変換コードの例を作成する際に役立ちます。
{% endalert %}
