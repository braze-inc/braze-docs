---
nav_title: iOS向けアプリ内レーティング・プロンプト
article_title: iOS向けアプリ内レーティング・プロンプト
page_order: 6
description: "この記事では、Brazeを使ってユーザーにアプリのレビューを依頼する際のアプローチとその意味について説明する。"
channel:
  - in-app messages

---

# iOS向けアプリ内評価プロンプト

> この記事では、Brazeを使ってユーザーにアプリのレビューを依頼する際のアプローチとその意味について説明する。効果的なアプリ評価キャンペーンを行うためのヒントについては、「[顧客アプリ評価の注意点](https://www.braze.com/resources/articles/the-dos-and-donts-of-customer-app-ratings)」を参照のこと。

アップルは、iOS 10.3で導入されたネイティブ・プロンプトを提供しており、ユーザーはアプリ自体からアプリを評価することができる。iOSのアプリ内メッセージを使用してユーザーにアプリの評価を要求したい場合、Appleはカスタムレビュープロンプトを許可していないため、ネイティブプロンプトを使用する必要がある（[App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/#code-of-conduct)、セクション5.6.1を参照）。

Appleのガイドラインによると、アプリのレビューのプロンプトはユーザーに対して年に最大3回表示することができるため、アプリのレビューキャンペーンは[レート制限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/)を活用する必要があります。ユーザーは、アプリの設定でアプリのレビュープロンプトを表示しないようにすることもできる。App Storeのレーティングについては、Appleの[レーティング、レビュー、レスポンスに関する](https://developer.apple.com/app-store/ratings-and-reviews/)記事を参照のこと。

## Brazeを使ってユーザーにアプリのレビューを依頼する

アップルはネイティブのプロンプトを使用することを義務付けているが、Brazeのキャンペーンを活用すれば、適切なタイミングでユーザーにアプリの評価やレビューを求めることができる。主に2つのアプローチがある。

### アプローチ1：App Storeへのディープリンク

このアプローチでは、ユーザーがApp Storeを訪れてレビューを追加するよう促したい。そのためには、App Storeに[ディープリンク]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/)するアプリ内メッセージキャンペーンを作成する。

![2つのモバイル画面が並んでいる。1つ目は、App Storeでアプリを評価するようユーザーに求めるアプリ内メッセージだ。もうひとつは、そのアプリのiOS App Storeページだ。][1]

### アプローチ2：ソフト・プライミング

ユーザーをアプリから離脱させたくない場合は、まずアプリ内の別メッセージでユーザーに呼びかけることができる。プライミングとは、ネイティブのApp Storeレビュープロンプトを送信する前に、ユーザーに許可を求める方法である。そのためには、アプリ内メッセージキャンペーンを作成し、クリックされると`requestReview` メソッドを呼び出すカスタムディープリンクを追加する。 

詳しい手順については、[Custom App Store review promptを]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/custom_app_store_review_prompt/)参照のこと。

![2つのアプリ内メッセージを並べる。1つ目は、アプリを評価する時間があるかどうかを尋ねることで、ユーザーにアプリを評価するよう促すものだ。2つ目は、iOS App Storeのネイティブ・レビュー・メッセージで、ユーザーがアプリを評価するために選択できる5つ星のスケールが表示される。][2]

ユーザーはネイティブのApp Storeレビュープロンプトを通じて評価を提出し、アプリを離れることなくレビューを書いて提出することができる。

### 考慮事項

ソフトプライミングの代わりに、Brazeのソフトプライマーメッセージを表示せずに、iOSアプリのレーティングプロンプトを直接表示することもできる。この利点は、ユーザーがアプリのレビュープロンプトをオプトアウトしている場合、アプリを評価しようとしても、そのためのプロンプトが表示されないという、最適とは言えないユーザー体験が発生しないことだ。

{% alert important %}
iOSネイティブアプリのレーティングプロンプトを模倣したカスタムHTMLアプリ内メッセージを作成しないこと。
{% endalert %}

[1]: {% image_buster /assets/img_archive/app_store_app_review.png %}
[2]: {% image_buster /assets/img_archive/prime_app_review.png %}