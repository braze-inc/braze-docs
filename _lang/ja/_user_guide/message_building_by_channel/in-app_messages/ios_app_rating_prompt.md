---
nav_title: iOSのアプリ内評価プロンプト
article_title: iOSのアプリ内評価プロンプト
page_order: 6
description: "この記事では、Braze を使用してユーザーにアプリのレビューを依頼するためのアプローチとインプリケーションについて説明します。"
channel:
  - in-app messages

---

# iOSのアプリ内レーティングプロンプト

> この記事では、Braze を使用してユーザーにアプリのレビューを依頼するためのアプローチとインプリケーションについて説明します。効果的なアプリ評価キャンペーンの作り方についてのヒントは、[The Do's and Don'ts of Customer App Ratings](https://www.braze.com/resources/articles/the-dos-and-donts-of-customer-app-ratings)をご覧ください。

Apple は、iOS 10.3 で導入されたネイティブプロンプトを提供しており、アプリ自体からアプリを評価できます。iOS でアプリ内メッセージを使用してユーザーからアプリ評価をリクエストする場合は、Apple がカスタムレビュープロンプトを許可しないため、ネイティブプロンプトを使用する必要があります([App Store レビューガイドライン](https://developer.apple.com/app-store/review/guidelines/#code-of-conduct)、セクション5.6.1 を参照)。

Appleのガイドラインに従って、アプリレビュープロンプトを年に3回までユーザーに表示できるため、アプリレビューキャンペーンでは[レート制限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/)を利用する必要があります。ユーザーは、アプリ設定でアプリレビュープロンプトを完全に表示しないこともできます。App Store の定格の詳細については、Apple の記事[定格、レビュー、およびレスポンス](https://developer.apple.com/app-store/ratings-and-reviews/) を参照してください。

## Braze を使用してユーザーにアプリのレビューを依頼する

Apple ではネイティブプロンプトを使用する必要がありますが、Braze キャンペーンを利用して、ユーザーにアプリの評価とレビューを適時に依頼することができます。2つの主なアプローチがあります。

### アプローチ1:App Storeへのディープリンク

このアプローチでは、ユーザがApp Store にアクセスしてレビューを追加することを奨励します。そのためには、[Deep links]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/)をApp Storeにリンクするアプリ内メッセージキャンペーンを作成します。

![2つのモバイルスクリーンを並べて。1つ目はアプリ内メッセージで、App Storeでアプリを評価するようユーザーに求めます。2つ目は、そのアプリのiOS App Storeページです。][1]

### アプローチ2:ソフトプライム

ユーザーがアプリを離れたくない場合は、まず別のアプリ内メッセージでユーザーをプライムできます。プライミングは、ネイティブのApp Store レビュープロンプトを送信する前に、ユーザーに許可を求める方法です。そのためには、アプリ内メッセージキャンペーンを登録し、クリック時に`requestReview` メソッドを呼び出すカスタムディープリンクを追加します。 

詳細な手順については、[カスタムApp Store レビュープロンプト]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/custom_app_store_review_prompt/)を参照してください。

![アプリ内メッセージを並べて2つ。最初に、アプリを評価する瞬間があるかどうかを尋ねることで、アプリの評価をユーザーにプライムします。2つ目は、iOS App Storeのネイティブレビューメッセージで、ユーザーがアプリを評価するために選択できる5つ星のスケールが表示されます。[2]

ユーザーはネイティブのApp Storeレビュープロンプトを介して評価を送信し、アプリを離れることなくレビューを書き込み、送信することができます。

### 考慮事項

ソフトプライミングの代わりに、前に表示されたブレーズソフトプライマーメッセージなしで、iOSアプリの評価プロンプトを直接表示することもできます。この利点は、ユーザーがアプリレビュープロンプトからオプトアウトされた場合、アプリケーションを評価しようとしても、プロンプトが表示されないという最適なユーザーエクスペリエンスが得られないことです。

{% alert important %}
Apple のガイドラインに違反するため、ネイティブiOS アプリ評価プロンプトを模倣したカスタムHTML インアプリメッセージを作成しないでください。
{% endalert %}

[1]: {% image_buster /assets/img_archive/app_store_app_review.png %}
[2]: {% image_buster /assets/img_archive/prime_app_review.png %}