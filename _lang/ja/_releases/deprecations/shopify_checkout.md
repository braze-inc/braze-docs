---
nav_title: Shopify checkout.liquid
page_order: 7
description: "この記事では、Shopifyのcheckout.liquidの非推奨について、Shopifyの統合への影響と開発者向けのガイダンスを説明します。"
page_type: update

---

# Shopify checkout.liquid 廃止

Shopifyはすべてのマーチャントに`checkout.liquid`の非推奨と、カスタマイズされたチェックアウト体験を構築するための新しい基盤である[Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions)への移行について通知しました。 

Shopifyは`checkout.liquid`を2段階で廃止します:

1. **[2024年8月13日](#phase-one-august-13-2024):**情報、配送、支払いのページをアップグレードする期限。
2. **[2025年8月28日](#phase-two-august-28-2025):**スクリプトタグと追加スクリプトを使用するアプリを含む、ありがとうページと注文ステータスページをアップグレードする期限。

チェックアウト拡張機能へのアップグレードに関する一般情報については、[Shopifyのアップグレードガイド](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility)を参照してください。

## 連携への影響

BrazeとShopifyの統合は、[Shopify ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy)を使用して、ヘッドレスでないサイトにBraze Web SDKを読み込むために使用されます。`checkout.liquid` が完全に非推奨になる前に、すべてのお客様をサポートするため、2025年の期限前に新しいバージョンの連携を開始する予定です。 

2024年8月13日に予定されている変更については、以下の詳細を確認して、開発チームの影響を受けるかどうかを確認してください。

### フェーズ1:2024年8月13日

デフォルトのBrazeとShopifyの統合は、チェックアウト体験内の情報、配送、および支払いページを使用しません。そのため、デフォルトインテグレーションは影響を受けません。 

#### Shopify Plus

Shopify Plusの顧客の場合、情報、配送、または支払いページの`checkout.liquid`を変更するカスタムSDKコードスニペットは、この日以降無効になります。例えば、これらのページからイベントを記録するカスタムコードは機能しなくなります。カスタムSDKコードがある場合は、移行のための[開発者ガイダンス](#developer-guidance)をご覧ください。

#### 非Shopifyプラス

Shopify Plus以外の顧客の場合、情報、支払い、および配送ページをカスタマイズする必要がある場合は、[Shopify Plusにアップグレードする必要があります](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility#eligibility) その後、[開発者ガイダンス](#developer-guidance)に従ってください。

### フェーズ2:2025年8月28日

Shopifyは、統合で使用されている[ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy)の`checkout.liquid`ページでのサポートを廃止します。これを受けて、2025年8月の期限を大幅に前倒ししてリリースする予定の Shopify 連携の新バージョンを積極的に構築しています。Braze製品チームからの詳細情報をお待ちください。 

## 開発者ガイダンス

このガイダンスは、`checkout.liquid`の情報、配送、または支払いページにカスタムSDKコードスニペットを追加したShopify Plusの顧客に適用されます。これらのカスタマイズを行っていない場合は、このガイダンスを無視してもかまいません。

`checkout.liquid`では、情報、配送、または支払いページにカスタムSDKコードスニペットを追加できなくなります。代わりに、カスタムSDKコードスニペットをサンキューページまたは注文ステータスページに追加する必要があります。これにより、チェックアウトが完了したユーザーを調整できます。
1. ありがとうと注文ステータスページでBraze Web SDKを読み込む。
2. ユーザーからメールアドレスを取得します。
3. `setEmail` を呼び出します。

{% raw %}
```java
braze.getUser().setEmail(<email address>);
```
{% endraw %}

{: start="4"}
4\.Braze で、ユーザープロファイルをメールアドレスでマージします。

重複するユーザープロファイルが発生した場合は、データを効率化するために[一括マージツール]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging)を使用できます。 
