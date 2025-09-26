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

Apple のガイドラインによると、アプリのレビュープロンプトはユーザーに対して年に最大 3 回表示できるため、アプリのレビューキャンペーンでは[レート制限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/)を活用する必要があります。ユーザーは、アプリの設定でアプリのレビュープロンプトを全く表示しないようにすることもできます。App Store のレーティングについては、Apple の[レーティング、レビュー、レスポンス](https://developer.apple.com/app-store/ratings-and-reviews/)に関する記事を参照してください。

## Brazeを使ってユーザーにアプリのレビューを依頼する

アップルはネイティブのプロンプトを使用することを義務付けているが、Brazeのキャンペーンを活用すれば、適切なタイミングでユーザーにアプリの評価やレビューを求めることができる。主に2つのアプローチがある。

### アプローチ1：App Storeへのディープリンク

このアプローチでは、ユーザーがApp Storeを訪れてレビューを追加するよう促したい。そのためには、App Storeに[ディープリンク]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/)するアプリ内メッセージキャンペーンを作成する。

![2 つのモバイル画面を並べて表示。1つ目は、App Storeでアプリを評価するようユーザーに求めるアプリ内メッセージだ。2つ目は、そのアプリの iOS App Store ページである。]({% image_buster /assets/img_archive/app_store_app_review.png %})

### アプローチ2：ソフトプライミング

ユーザーをアプリから離脱させたくない場合は、まずアプリ内の個別メッセージでユーザーに呼びかけることができます。プライミングとは、ネイティブのApp Storeレビュープロンプトを送信する前に、ユーザーに許可を求める方法である。そのためには、アプリ内メッセージキャンペーンを作成し、クリックされると`requestReview` メソッドを呼び出すカスタムディープリンクを追加する。 

詳しい手順については、[カスタム App Store レビュープロンプト]({{site.baseurl}}/developer_guide/in_app_messages/customization/#swift_customizing-the-app-store-review-prompt)を参照してください。

![2 つのアプリ内メッセージを並べて表示。1 つ目は、アプリを評価する時間があるかどうかを尋ね、ユーザーにアプリを評価してもらうよう促します。2つ目はiOSのApp Storeのネイティブレビューメッセージで、ユーザーがアプリを評価するために選択できる5つ星のスケールが表示される。]({% image_buster /assets/img_archive/prime_app_review.png %})

ユーザーはネイティブの App Store レビュープロンプトを介して評価を提出し、アプリを離れることなく、レビューを書き込んで提出することができます。

### 考慮事項

ソフトプライミングの代わりに、事前に Braze のソフトプライマーメッセージを表示せずに、iOS アプリのレーティングプロンプトを直接表示することもできます。この利点は、ユーザーがアプリのレビュープロンプトをオプトアウトしている場合、アプリを評価しようとしても、そのためのプロンプトが表示されないという、最適とは言えないユーザー体験が発生しないことだ。

{% alert important %}
iOS ネイティブのアプリレーティングプロンプトを模倣したカスタムの HTML アプリ内メッセージは作成しないでください。これは Apple のガイドラインに違反する行為です。
{% endalert %}

