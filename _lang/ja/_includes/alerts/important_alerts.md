{% if include.alert == "Shopify deprecation" %}

{% alert important %}
[新バージョンのShopifyインテグレーション]({{site.baseurl}}/partners/shopify/#new-shopify-integration)は、2025年4月から段階的にリリースされます。フェーズは、Shopify ストアのタイプと、初期統合のセットアップに使用される外部ID に基づきます。<br><br>**旧バージョンの統合は、2025年8月28日以降は利用できなくなります。この日付より前の新しいバージョンに更新すると、問題なく統合を使用し続けます。**
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
購入イベントの段階的廃止計画が2025年後半に発表される予定です。将来的には、購入イベントは新しい[e コマースの推奨イベント]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/)に置き換わる予定です。新しい e コマースの推奨イベントには、セグメンテーション、レポート、分析などの強化された機能が組み込まれる予定です。ただし新しい e コマースイベントでは、購入イベントに関連する既存の機能 (キャンバスまたはキャンペーンでの生涯価値 (LTV) または収益の報告など) はサポートされません。購入イベントに関連する機能の完全なリストについては、[購入イベントの記録]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#logging-purchase-events)を参照してください。
{% endalert %}

{% endif %}

{% if include.alert == 'S3 file bucket export' %}

{% alert important %}
S3 バケットに保存されているエクスポートファイルは、ダウン読み込むの有効期限が切れた後(特に指定がない限り、エクスポートメールが送信されてから 4 時間後)に自動的に削除されます。
{% endalert %} 

{% endif %}

{% if include.alert == 'Shopify customer create' %}

{% alert important %}
Shopifyインテグレーションでは、データコンフィギュレーション設定にあるShopify 顧客の作成と顧客 更新 webhookがサポートされます。ユーザープロファイルが作成されるか、更新dがShopifyで作成されると、対応するBrazeのユーザープロファイルが作成されるか、更新dが作成されます。<br><br>これらのアクションはBrazeではs をトリガー カスタムイベントせず、[Braze]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#how-the-integration-works) との同期Shopify ユーザーデータにのみ使用されます。同期されるデータには、[カスタム属性s]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-custom-attributes)、[標準属性項目s]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-standard-attributes)が含まれ、設定内で有効になっている場合は、[サブスクリプショングループステート]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#syncing-shopify-email-and-sms-marketing-opt-ins)が含まれます。
{% endalert %}

{% endif %}

{% if include.alert == 'context variable' %}

{% alert important %}
キャンバスコンテキストの初期アクセスに参加している場合、キャンバスエントリのプロパティはキャンバスコンテキスト変数の一部です。これは、`canvas_entry_properties` が`context` として参照されることを意味します。各コンテキスト変数には、名前、データ型、およびLiquid を含めることができる値が含まれます。現在、`canvas_entry_properties` は下位互換性があります。詳しくは、[コンテキスト]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works)および[キャンバスエントリプロパティオブジェクト]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)を参照してください。
{% endalert %}

{% endif %}