---
nav_title: "Shopifyチェックアウト&#46;リキッド"
page_order: 7
description: "この記事では、Shopifyチェックアウト&#46;liquidの非推奨について、Shopifyとの統合への影響や開発者のためのガイダンスを含めて説明する。"
page_type: update

---

# Shopifycheckout.liquid 非推奨

Shopifyは全ての顧客に対し、`checkout.liquid` の廃止と、カスタマイズされたチェックアウト体験を構築するための新しい基盤である[Checkout Extensibilityへの](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions)移行について通知した。 

Shopifyは`checkout.liquid` 、2段階に分けて非推奨とする：

1. **[2024年8月13日](#phase-one-august-13-2024)だ：**情報、配送、支払いページのアップグレード期限。
2. **[2025年8月28](#phase-two-august-28-2025)日だ：**スクリプトタグや追加スクリプトを使用したアプリを含む、サンキューページやオーダーステータスページのアップグレード期限。

Checkout Extensibiltyへのアップグレードに関する一般的な情報は、[Shopifyのアップグレードガイドを](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility)参照のこと。

## 統合への影響

BrazeとShopifyの統合は、[Shopify ScriptTagsを](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy)使用して、非ヘッドレスサイト用のBraze Web SDKを読み込む。我々は、`checkout.liquid` が完全に非推奨となる前にすべての顧客をサポートするため、2025年の期限までに統合の新バージョンを発表する予定だ。 

2024年8月13日に予定されている変更については、以下の詳細をチェックして、開発者に影響があるかどうかを確認しよう。

### 第1段階だ：2024年8月13日

デフォルトのBrazeとShopifyの統合は、チェックアウト体験の中で情報、配送、支払いのページを使用しない。その結果、デフォルトの統合に影響はない。 

#### Shopifyプラス

Shopify Plus顧客の場合、情報ページ、配送ページ、支払いページの`checkout.liquid` を変更するカスタムSDKコードスニペットは、この日以降無効となる。例えば、これらのページからのイベントを記録するカスタムコードは動作しなくなる。カスタムSDKコードをお持ちの場合は、[開発者向け](#developer-guidance)移行[ガイダンスを](#developer-guidance)参照のこと。

#### Shopifyプラス以外

Shopify Plus以外の顧客の場合、情報、支払い、配送ページをカスタマイズする必要がある場合は、[Shopify Plusにアップグレード](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility#eligibility)し、[開発者のガイダンスに](#developer-guidance)従う[必要が](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility#eligibility)ある。

### 第2段階だ：2025年8月28日

Shopifyは、統合で使用されている`checkout.liquid` ページの[ScriptTagsの](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy)サポートを廃止する。これを受けて、我々はShopifyとの統合の新バージョンを積極的に構築しており、2025年8月の期限よりもかなり前にリリースする予定だ。Braze製品チームからのさらなる情報にご期待いただきたい。 

## 開発者ガイダンス

このガイダンスは、カスタム SDK コードスニペットを`checkout.liquid` の情報ページ、配送ページ、支払いページに追加した Shopify Plus 顧客に適用される。これらのカスタマイズを行っていない場合は、このガイダンスを無視して構わない。

`checkout.liquid` のインフォメーション、シッピング、ペイメントページにカスタムSDKコードスニペットを追加することができなくなる。その代わりに、サンキューページや注文ステータスページにカスタムSDKコードスニペットを追加する必要がある。これにより、チェックアウトを完了したユーザーを照合することができる。
1. サンキューページと注文ステータスページでBraze Web SDKを読み込む。
2. ユーザーからメールを取得する。
3. `setEmail` を呼び出します。

{% raw %}
```java
braze.getUser().setEmail(<email address>);
```
{% endraw %}

{: start="4"}
4\.Brazeで、メールのユーザープロファイルをマージする。

ユーザープロファイルの重複が発生した場合は、[一括マージツールを](https://www.braze.com/docs/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging)使用してユーザーデータを効率化することができる。 
