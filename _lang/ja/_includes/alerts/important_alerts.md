{% if include.alert == "Shopify deprecation" %}

{% alert important %}
[Shopify 連携の新バージョン]({{site.baseurl}}/partners/shopify/#new-shopify-integration)は、2025年4月から段階的にリリースされます。フェーズは、Shopify ストアのタイプと、初期連携のセットアップに使用される external ID に基づきます。<br><br>**旧バージョンの連携は、2025年8月28日以降利用できなくなります。問題なく連携を引き続き使用するには、この日付までに新バージョンに更新してください。**
{% endalert %}

{% endif %}

{% if include.alert == 'Web push private browsing' %}

{% alert important %}
プライベートブラウジングウィンドウは Web プッシュをサポートしていません。
{% endalert %}

{% endif %}

{% if include.alert == 'BCC address billable emails' %}

{% alert important %}
キャンペーンやキャンバスに BCC アドレスを追加すると、請求対象となるメール数が倍増します。これは、Braze がユーザー宛てに1通、BCC アドレス宛てに1通のメッセージを送信するためです。
{% endalert %}

{% endif %}

{% if include.alert == 'Android notification priority' %}

{% alert important %}
通知表示優先度の設定は、Android O 以降を実行するデバイスでは使用されなくなりました。これらのデバイスでは、[通知チャネルの設定](https://developer.android.com/training/notify-user/channels#importance)を通じて優先度を設定してください。
{% endalert %}

{% endif %}

{% if include.alert == "Email via SMS" %}

{% alert important %}
法的に要求されるトランザクションメールを SMS ゲートウェイに送信しないでください。これらのメールは配信されない可能性が高いためです。
<br><br>
電話番号とプロバイダーのゲートウェイドメイン（MM3 として知られている）を使用して送信したメールは、SMS（テキスト）メッセージとして受信される可能性がありますが、一部のメールプロバイダーはこの動作をサポートしていません。例えば、T-Mobile の電話番号（「9999999999@tmomail.net」など）にメールを送信した場合、SMS メッセージは T-Mobile ネットワークでその電話番号を所有している人に送信されます。
<br><br>
これらのメールが SMS ゲートウェイに配信されなくても、メール課金にはカウントされることにご注意ください。サポートされていないゲートウェイへのメール送信を避けるには、[サポートされていないゲートウェイのドメイン名のリスト](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads)を確認してください。
{% endalert %}

{% endif %}

{% if include.alert == 'SDK auth' %}

{% alert important %}
さらにセキュリティを高めるために、ユーザーのなりすましを防ぐ [SDK 認証]({{site.baseurl}}/developer_guide/authentication/)機能を追加することをお勧めします。
{% endalert %}

{% endif %}

{% if include.alert == 'Preference Center warning' %}

{% alert important %}
Naver の Android アプリや iOS アプリなど、Braze のユーザー設定センターをサポートしていないブラウザがあります。一部のユーザーがこれらのブラウザを使用することが予想される場合は、メールの環境設定を管理するための代替方法を提供することを検討してください。
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation' %}

{% alert important %}
購入イベントを段階的に廃止する計画は2026年に発表されます。購入イベントは最終的に新しい [e コマース推奨イベント]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/)に置き換えられます。これにはセグメンテーション、レポート作成、分析などの機能強化が含まれます。ただし、新しい e コマースイベントでは、購入イベントに関連する既存の機能（キャンバスやキャンペーンでの生涯価値 (LTV) や収益のレポートなど）はサポートされません。購入イベントに関連する機能の完全な一覧については、[購入イベントのログ記録]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#logging-purchase-events)を参照してください。
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation for eCommerce filters' %}

{% alert important %}
購入イベントを段階的に廃止する計画は2026年に発表されます。購入イベントは最終的に新しい [e コマース推奨イベント]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/)に置き換えられます。これにはセグメンテーション、レポート作成、分析などの機能強化が含まれます。この置き換えが行われると、Segment フィルターでは購入動作でデータが入力されなくなります。購入イベントの完全なリストについては、[購入イベントの記録]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events)を参照してください。
{% endalert %}

{% endif %}

{% if include.alert == 'S3 file bucket export' %}

{% alert important %}
S3 バケットに保存されたエクスポートファイルは、ダウンロードリンクの有効期限が切れた後（特に記載がない限り、エクスポートメール送信から4時間後）、自動的に削除されます。
{% endalert %} 

{% endif %}

{% if include.alert == 'Shopify customer create' %}

{% alert important %}
Shopify 連携は、Shopify の顧客作成と顧客更新の Webhook をサポートしています。これらはデータ設定の構成設定にあります。Shopify でユーザープロファイルが作成または更新されると、対応する Braze のユーザープロファイルも作成または更新されます。<br><br>これらのアクションは Braze でカスタムイベントをトリガーせず、[Shopify のユーザーデータを Braze と同期]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#how-the-integration-works)させるためだけに使用されます。同期されるデータには、[カスタム属性]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-custom-attributes)、[標準属性項目]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-standard-attributes)、および設定内で有効にされている場合は[サブスクリプショングループの状態]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#syncing-shopify-email-and-sms-marketing-opt-ins)が含まれます。
{% endalert %}

{% endif %}

{% if include.alert == 'context variable' %}

{% alert important %}
キャンバスのエントリプロパティは、キャンバスコンテキスト変数の一部です。つまり、`canvas_entry_properties` は `context` として参照されます。各 `context` 変数には、名前、データタイプ、および Liquid を含めることができる値が含まれます。現在、`canvas_entry_properties` は下位互換性があります。詳細については、[コンテキスト]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works)と[キャンバスコンテキストオブジェクト]({{site.baseurl}}/api/objects_filters/context_object)を参照してください。
{% endalert %}

{% endif %}

{% if include.alert == 'Braze Agents' %}

{% alert important %}
このパートナーは、[Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/) が有効になっている場合のみ、**テクノロジーパートナー**ページに表示されます。利用開始に関するサポートが必要な場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

{% endif %}

{% if include.alert == 'time filter types' %}

{% alert important %}
**「Day of year」と「Time」のフィルタータイプの選択について**：日付を含むコンテキスト変数をフィルタリングする際は、その日付が毎年繰り返されるかどうかに基づいて、適切な比較タイプを選択してください。

- **毎年繰り返される日付（誕生日、記念日、クリスマスなどの祝日など）には「Day of year」を使用してください。**この比較タイプは、年の要素を無視し、その年の日数（1〜365/366）に基づいて計算します。
- **繰り返されない絶対日付（契約終了日、予約日、サブスクリプションの更新日など）には「Time」を使用してください。**この比較タイプは、年を含む完全なタイムスタンプに基づいて計算します。

絶対日付に「Day of year」を使用すると、計算が年の要素を無視するため、誤った結果や予期しない結果が生じることがあります。例えば、4月の将来の契約終了日が63日以内かどうかを判断する場合、「Day of year」を使用すると、日付番号（119対359）のみを比較し、実際には4月まで188日あることを考慮しないため、誤った一致が生じる可能性があります。

**一般的な指針**：その日付は毎年繰り返されますか？**はい** → 「Day of year」を使用してください。**いいえ** → 「Time」を使用してください。
{% endalert %}

{% endif %}

{% if include.alert == 'granular permissions ea' %}

{% alert important %}
詳細な権限設定は早期アクセス中です。自社の移行が計画された場合、Braze の管理者はメールとダッシュボード上のバナーで[詳細な権限の移行]({{site.baseurl}}/granular_permissions_migration/)に関する通知を受け取ります。
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify cart token alias' %}

{% alert important %}
この連携では、Braze が Webhook を正しいユーザープロファイルに一致させるために、ユーザーエイリアスは以下の形式を使用する必要があります。<br><br>
- `alias_label`: `shopify_cart_${cartToken}`
- `alias_name`: `shopify_cart_token`
{% endalert %}

{% endif %}