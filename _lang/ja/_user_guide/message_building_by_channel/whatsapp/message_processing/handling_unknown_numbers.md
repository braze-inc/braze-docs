---
nav_title: 知らない電話番号への対応
article_title: 不明な電話番号への対応
description: "この参考記事では、BrazeがWhatsAppユーザーの不明な電話番号をどのように処理するかについて説明する。"
page_type: reference
channel:
  - WhatsApp
page_order: 50
---

# 知らない電話番号への対応

> BrazeでWhatsAppを立ち上げると、見知らぬユーザーからメッセージが届くことがある。以下のステップでは、未確認のユーザーと番号がどのように処理されるかを説明する。

## 不明な番号に対するオプトイン/アウトおよびカスタム・キーワード・ワークフロー

Brazeはまず、番号の一致するユーザーを探そうとする。何も見つからない場合、Braze は 2 つの方法のいずれかで不明な番号を自動的に処理します。

1. **[[オプトインキャンバス]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/)] のトリガーワードが設定されている場合**
- Braze によって匿名プロファイルが作成される
- プロファイルに以下の詳細を持つユーザーエイリアスを割り当てる
  - `alias_name` - 値はユーザーが提供した電話番号
  - `alias_label` - 値は `phone`
- システムによって phone 属性が設定される
- ユーザーは、キャンバス内で設定されたロジックに基づいて、対応するサブスクリプショングループにサブスクライブされる。<br><br>
2. **オプトインキャンバスが設定されていない場合**
- Braze によって匿名プロファイルが作成される
- プロファイルに以下の詳細を持つユーザーエイリアスを割り当てる
  - `alias_name` - 値はユーザーが提供した電話番号
  - `alias_label` - 値は `phone`
- システムによって phone 属性が設定される
- ユーザーの購読ステータスは、すべての WhatsApp 購読グループでデフォルトの `unsubscribed` になる<br><br>

