---
nav_title: Shopify チェックアウト.liquid
page_order: 7
description: "この記事では、Shopifyのcheckout.liquidの非推奨について、Shopifyの統合への影響と開発者向けのガイダンスを説明します。"
page_type: update

---

# Shopify checkout.liquid 廃止

Shopifyはすべてのマーチャントに`checkout.liquid`の非推奨と、カスタマイズされたチェックアウト体験を構築するための新しい基盤である[Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions)への移行について通知しました。 

Shopifyは`checkout.liquid`を2段階で廃止します:

1. **[2024年8月13日](#phase-one-august-13-2024):**情報、配送、および支払いページをアップグレードする締め切り。
2. **[2025年8月28日](#phase-two-august-28-2025):**感謝ページと注文ステータスページをアップグレードする締め切り、スクリプトタグや追加スクリプトを使用するアプリを含みます。

チェックアウト拡張機能へのアップグレードに関する一般情報については、[Shopifyのアップグレードガイド](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility)を参照してください。

## 統合への影響

BrazeとShopifyの統合は、[Shopify ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy)を使用して、ヘッドレスでないサイトにBraze Web SDKを読み込むために使用されます。2025年の期限前に新しいバージョンの統合を開始し、`checkout.liquid`が完全に廃止される前にすべての顧客をサポートする予定です。 

2024年8月13日に予定されている変更について、開発チームによって影響を受けるかどうかを確認するには、以下の詳細を確認してください。

### フェーズ1:2024年8月13日

デフォルトのBrazeとShopifyの統合は、チェックアウト体験内の情報、配送、および支払いページを使用しません。その結果、デフォルトの統合には影響しません。 

#### Shopify Plus

Shopify Plusの顧客の場合、情報、配送、または支払いページの`checkout.liquid`を変更するカスタムSDKコードスニペットは、この日以降無効になります。例えば、これらのページからイベントを記録するカスタムコードは機能しなくなります。カスタムSDKコードがある場合は、移行のための[開発者ガイダンス](#developer-guidance)をご覧ください。

#### Non-Shopify Plus の日本語訳

Shopify Plus以外の顧客の場合、情報、支払い、および配送ページをカスタマイズする必要がある場合は、[Shopify Plusにアップグレードする必要があります](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility#eligibility) その後、[開発者ガイダンス](#developer-guidance)に従ってください。

### フェーズ2:2025年8月28日

Shopifyは、統合で使用されている[ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy)の`checkout.liquid`ページでのサポートを廃止します。それに応じて、私たちは2025年8月の期限に十分先立ってリリースする予定の新しいバージョンのShopify統合を積極的に構築しています。Braze製品チームからの詳細情報をお待ちください。 

## 開発者 guidance

このガイダンスは、`checkout.liquid`の情報、配送、または支払いページにカスタムSDKコードスニペットを追加したShopify Plusの顧客に適用されます。これらのカスタマイズを行っていない場合は、このガイダンスを無視してもかまいません。

`checkout.liquid`では、情報、配送、または支払いページにカスタムSDKコードスニペットを追加できなくなります。代わりに、カスタムSDKコードスニペットをサンキューページまたは注文ステータスページに追加する必要があります。これにより、チェックアウトを完了したユーザーを照合できます。
1. ありがとうと注文ステータスページでBraze Web SDKを読み込む。
2. ユーザーからメールを取得します。
3. `setEmail` を呼び出します。

{% raw %}
```java
braze.getUser().setEmail(<email address>);
```
{% endraw %}

{: start="4"}
4\.Brazeで、メールのユーザープロファイルをマージします。

重複するユーザープロファイルが発生した場合は、データを効率化するために[一括マージツール]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging)を使用できます。 
