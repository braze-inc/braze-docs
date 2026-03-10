{% if include.alert == "Shopify deprecation" %}

{% alert important %}
Shopify連携の新バージョンは、2025年4月から段階的にリリースされる。フェーズは、Shopify ストアのタイプと、初期統合のセットアップに使用される外部ID に基づきます。<br><br>**旧バージョンの統合機能は、2025年8月28日以降利用できなくなる。この日付までに新バージョンに更新しないと、統合機能に問題が生じる。**
{% endalert %}

{% endif %}

{% if include.alert == 'Web push private browsing' %}

{% alert important %}
プライベートブラウジングウィンドウはWeb プッシュをサポートしない。
{% endalert %}

{% endif %}

{% if include.alert == 'BCC address billable emails' %}

{% alert important %}
キャンペーンやCanvasにBCCアドレスを追加すると、請求対象となるメール数が倍増する。Brazeはユーザー宛てに1通、BCCアドレス宛てに1通のメッセージを送信するためだ。
{% endalert %}

{% endif %}

{% if include.alert == 'Android notification priority' %}

{% alert important %}
通知表示優先度の設定は、Android O以降を実行する端末では使用されなくなった。これらのデバイスでは、[通知チャネルの設定](https://developer.android.com/training/notify-user/channels#importance)を通じて優先度を設定する。
{% endalert %}

{% endif %}

{% if include.alert == "Email via SMS" %}

{% alert important %}
法的に要求されているトランザクションメールを SMS ゲートウェイに送信しないでください。これらのメールは配信されない可能性が高いためです。
<br><br>
電話番号とプロバイダーのゲートウェイドメイン（MM3として知られている）を使用して送信したメールは、SMS（テキスト）メッセージとして受信される可能性があるが、一部のメールプロバイダーはこの動作をサポートしていない。例えば、T-モバイルの電話番号（"9999999999@tmomail.net"など）にメールを送った場合、SMSメッセージはT-モバイル・ネットワークでその電話番号を所有している人に送信される。
<br><br>
これらのメールがSMSゲートウェイに配信されなくても、メール課金にはカウントされることを覚えておいてほしい。サポートされていないゲートウェイへのメール送信を避けるには、[サポートされていないゲートウェイのドメイン名のリスト](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads)を確認します。
{% endalert %}

{% endif %}

{% if include.alert == 'SDK auth' %}

{% alert important %}
さらにセキュリティを高めるために、ユーザーの偽装やなりすましを防ぐ[SDK認証]({{site.baseurl}}/developer_guide/authentication/)機能を追加することをお勧めする。
{% endalert %}

{% endif %}

{% if include.alert == 'Preference Center warning' %}

{% alert important %}
Naver Android や iOS アプリなど、Braze のユーザー設定センターをサポートしていないブラウザもあります。一部のユーザーがこれらのブラウザを使用することが予想される場合は、ユーザーがメールの環境設定を管理するための代替方法を提供することを検討してください。
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation' %}

{% alert important %}
購入イベントを段階的に廃止する計画は2026年に発表される。購入イベントは最終的に新しい[e コマース推奨イベント]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/)に置き換えられる。これにはセグメンテーション、レポート作成、分析などの機能が強化される。ただし新しい e コマースイベントでは、購入イベントに関連する既存の機能 (キャンバスまたはキャンペーンでの生涯価値 (LTV) または収益の報告など) はサポートされません。購入イベントに関連する機能の完全な一覧については、[「購入イベントのログ記録」]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#logging-purchase-events)を参照のこと。
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation for eCommerce filters' %}

{% alert important %}
購入イベントを段階的に廃止する計画は2026年に発表される。購入イベントは最終的に新しい[e コマース推奨イベント]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/)に置き換えられる。これにはセグメンテーション、レポート作成、分析などの機能が強化される。この置き換えが行われると、セグメントフィルターでは、購入動作でデータが入力されることがなくなります。購入イベントの完全なリストについては、[購入イベントの記録]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events)を参照してください。
{% endalert %}

{% endif %}

{% if include.alert == 'S3 file bucket export' %}

{% alert important %}
S3バケットに保存されたエクスポートファイルは、ダウンロードリンクの有効期限が切れた後（特に記載がない限り、エクスポートメール送信から4時間後）、自動的に削除される。
{% endalert %} 

{% endif %}

{% if include.alert == 'Shopify customer create' %}

{% alert important %}
Shopify連携は、Shopifyの顧客作成と顧客更新のWebhookをサポートしている。これらはデータ設定の構成設定にある。Shopifyでユーザープロファイルが作成または更新されると、対応するBrazeのユーザープロファイルも作成または更新される。<br><br>これらのアクションはBrazeでカスタムイベントをトリガーせず、[ShopifyのユーザーデータをBrazeと同期]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#how-the-integration-works)させるためだけに使用される。同期されるデータには、[カスタム属性]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-custom-attributes)、[標準属性項目]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-standard-attributes)、および設定内でイネーブルメントされている場合、[サブスクリプショングループの状態]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#syncing-shopify-email-and-sms-marketing-opt-ins)が含まれる。
{% endalert %}

{% endif %}

{% if include.alert == 'context variable' %}

{% alert important %}
キャンバスのエントリプロパティは、キャンバスコンテキスト変数の一部である。これは、がとして参照されることを`canvas_entry_properties``context`意味する。各`context` 変数には、名前、データ型、およびLiquid を含めることができる値が含まれます。現在、`canvas_entry_properties`それらは下位互換性がある。詳細については、[コンテキスト]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works)と[キャンバスコンテキストオブジェクトを]({{site.baseurl}}/api/objects_filters/context_object)参照せよ。
{% endalert %}

{% endif %}

{% if include.alert == 'Braze Agents' %}

{% alert important %}
このパートナーは[、Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/)のイネーブルメントが有効になっている場合のみ、あなたの**テクノロジーパートナー**ページに表示される。利用開始に関するサポートが必要な場合は、顧客サクセスマネージャーに連絡する。
{% endalert %}

{% endif %}

{% if include.alert == 'time filter types' %}

{% alert important %}
**「年の日数」と「時刻」のフィルタータイプを選ぶ場合**：日付を含むコンテキスト変数をフィルターでフィルタリングする際は、その日付が毎年繰り返されるかどうかによって、適切な比較タイプを選択せよ。

- 毎年繰り返される日付（誕生日、記念日、クリスマスなどの祝日など）には**「年の日数」を使用する**。この比較タイプは、年の要素を無視し、その年の日数（1～365/366）に基づいて計算する。
- 日付が絶対日付で繰り返さない場合（契約終了日、予約日、サブスクリプションの更新日など）は**「時間」を使用する**。この比較タイプは、年を含む完全なタイムスタンプに基づいて計算する。

絶対日付に「年の日数」を使用すると、計算が年成分を無視するため、誤った結果や予期しない結果が生じることがある。例えば、4月の先物契約終了日を63日以内かどうか判断する場合、「年の日数」を使用すると誤った一致が生じる可能性がある。これは単に日付番号（119対359）を比較するだけで、実際には4月まで188日あることを考慮しないためだ。

**一般的な指針**：その日付は毎年繰り返されるのか？**はい** → 「年の日数」を使う。**いいえ** → 「時間」を使う。
{% endalert %}

{% endif %}

{% if include.alert == 'granular permissions ea' %}

{% alert important %}
詳細な権限設定は早期アクセス中だ。自社の移行が計画された場合、Brazeの管理者はメールとダッシュボード上のバナーで通知を受け取る。これらは[詳細な権限の移行]({{site.baseurl}}/granular_permissions_migration/)について知らせるものだ。
{% endalert %}

{% endif %}