{% if include.alert == "Shopify deprecation" %}

{% alert important %}
[新バージョンのShopifyインテグレーション]({{site.baseurl}}/partners/shopify/#new-shopify-integration)は、2025年4月から段階的にリリースされます。フェーズは、Shopify ストアのタイプと、初期統合のセットアップに使用される外部ID に基づきます。<br><br>**旧バージョンの統合は、2025年8月28日以降は利用できなくなります。この日付より前の新しいバージョンに更新すると、問題なく統合を使用し続けます。**
{% endalert %}

{% endif %}

{% if include.alert == 'Web push private browsing' %}

{% alert important %}
プライベートブラウズウィンドウはWeb プッシュに対応していません。
{% endalert %}

{% endif %}

{% if include.alert == 'BCC address billable emails' %}

{% alert important %}
キャンペーンまたはキャンバスにBCCアドレスを追加すると、キャンペーンまたはキャンバスコンポーネントの請求可能メールが倍になります。これは、Brazeがユーザーに1つのメッセージを送信し、BCCアドレスに1つのメッセージを送信するためです。
{% endalert %}

{% endif %}

{% if include.alert == 'Android notification priority' %}

{% alert important %}
通知ディスプレイの優先順位設定は、Android O 以降を実行している機器では使用されなくなりました。これらの機器では、[通知 チャネル設定](https://developer.android.com/training/notify-user/channels#importance)でプライオリティを設定します。
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
購入イベントの段階的廃止計画は、2026年に発表される予定である。最終的に、購入イベントは新しい[eCommerce推奨イベント]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/)に置き換えられます。このイベントには、セグメンテーション、レポートリング、分析などの機能が強化されています。ただし新しい e コマースイベントでは、購入イベントに関連する既存の機能 (キャンバスまたはキャンペーンでの生涯価値 (LTV) または収益の報告など) はサポートされません。購入イベントに関連する機能の完全なリストについては、[購入イベントの記録]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#logging-purchase-events)を参照してください。
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation for eCommerce filters' %}

{% alert important %}
購入イベントの段階的廃止計画は、2026年に発表される予定である。最終的に、購入イベントは新しい[eCommerce推奨イベント]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/)に置き換えられます。このイベントには、セグメンテーション、レポートリング、分析などの機能が強化されています。この置き換えが行われると、セグメントフィルターでは、購入動作でデータが入力されることがなくなります。購入イベントの完全なリストについては、[購入イベントの記録]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events)を参照してください。
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

{% if include.alert == 'time filter types' %}

{% alert important %}
**"Day of year"および"Time"フィルタータイプ**:日付を含むコンテキスト変数をフィルターする場合は、日付が毎年繰り返されるかどうかに基づいて正しい比較型を選択します。

- ** "Day of year"** 日付が毎年繰り返される場合(誕生日、記念日、クリスマスのような休日など)。この比較タイプは、年のコンポーネントを無視して、年の日付(1-365/366) に基づいて計算されます。
- **"Time"** 日付が繰り返されない絶対日付の場合(契約終了日、アプリ軟膏の日付、サブスクリプション更新日など)を使用します。この比較タイプは、年を含む完全なタイムスタンプに基づいて計算されます。

"Day of year"を使用すると、絶対日付の場合、計算では年コンポーネントが無視されるため、誤った結果または予期しない結果が生成されることがあります。例えば、4月の将来の契約終了日を比較して、63日以内かどうかを判断する場合、"Day of year&quotを使用します。4月が実際には188日離れていることを考慮せずに、日数(119対359)のみを比較するため、日付が正しく一致しない可能性があります。

**一般ガイドライン**:その日付は毎年繰り返されますか?**はい** → &quot を使用;年の日付とクォート;。**No**→"Time"を使用します。
{% endalert %}

{% endif %}
