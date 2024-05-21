---
nav_title: AB テスト予測
article_title: AB テスト予測
page_order: 20
hidden: true
page_type: reference
description: "この記事では、AB テスト予測の仕組み、予測の実行方法、Braze がデータをどのように使用するかについて説明します。"
---

# AB テスト予測

> A/B test projection uses neural networks to predict which subject lines perform best. Our model extracts linguistic features from winning A/B tests performed on Braze and uses those statistical language patterns to teach our AI what makes better subject lines.

{% alert note %}
この機能は現在早期アクセス段階です。早期アクセスへの参加に興味がある場合は、Braze カスタマーサクセスマネージャーまたはアカウントマネージャーにお問い合わせください。
{% endalert %}

## 予測を実行する

キャンペーンの構成で、メッセージのバリアントと件名をエディターに挿入します。準備ができたら、キャンペーン作成フローの**ターゲットオーディエンス**のステップに進みます。[**AB テスト**] パネルで、[**予測を実行**]を選択します。

<img width="518" alt="画像" src="https://github.com/braze-inc/braze-docs/assets/17167198/8e74835c-76e4-4241-9763-c4f86a622c75">

モーダルが開き、すでに作成したメッセージバリアントの件名が表示されます。オプションとして、追加の件名 (最大10件まで) をボックスに手動で入力し、予測を実行することで、追加の件名を挿入することができます。[**投影の実行**] を選択します。

<img width="722" alt="画像" src="https://github.com/braze-inc/braze-docs/assets/17167198/f9ad45a3-6565-467b-a7f6-35277bef7699">

AI が最良と予測した件名には、「**予想される勝者**」ラベルが付けられます。

### 予測の精度はどの程度でしょうか。

テストでは、実際の AB テストでメッセージのペアを選ぶ際に、予測の精度が約70% であることがわかりました。このことは、モデルが勝つと予測するメッセージを解釈するときに考慮してください。

### データはどのように利用されるのか？

この機能は、過去の A/B tests carried out on Braze. The actual copy of your or any Braze customers' messages is never provided to the model. We first extract the high-level language patterns that predict winning messages in A/B tests. Then, we provide those patterns to our AI to teach it to discern which linguistic features constitute superior subject lines. から学習します。
