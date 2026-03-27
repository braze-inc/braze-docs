---
nav_title: アラート
article_title: アラートのベストプラクティス
description: "Braze ドキュメントで使用されるアラートタイプに関する情報、ガイドライン、および例です。"
page_order: 2
noindex: true
---

# アラートのベストプラクティス

> このドキュメントには、Braze ドキュメントで使用されるアラートタイプに関する情報、一般的なガイドライン、および例が含まれています。

## アラートタイプ {#alert-types}

アラートは、読者が認識すべき情報を分類します。ドキュメントで使用できるアラートタイプは4種類あります。

* 重要  
* 注記  
* ヒント  
* 警告

## アラートを使用するタイミング {#when-to-use-an-alert}

アラートは、重要な情報に読者の注意を引くために使用します。コンテンツは短く要点を押さえたものにしてください。読者の記憶に残る情報にすることが大切です。

各アラートの定義については、以下の表を参照してください。

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<colgroup><col style="width: 20%;"><col style="width: 80%;"></colgroup>
<thead>
<tr><th>アラートタイプ</th><th>定義</th></tr>
</thead>
<tbody>
<tr><td>重要</td><td>読者が対処<strong>すべき</strong>必須情報を含みます。例: <ul><li>非推奨の機能</li><li>請求への影響</li><li>関連する更新に関する情報</li><li>緊急性の高い機能の注意事項（例: ベータ機能）</li><li>その他の重要な情報</li></ul></td></tr>
<tr><td>注記</td><td>読者が知っておくべき一回限りの情報を含みます。例: <ul><li>機能の注意事項</li><li>フォーマットに関するガイダンス</li><li>役立つ補足情報</li><li>アラートの内容の重要度が下がったため、重要アラートから降格された情報（例: 長期間掲載されていた重要アラートが標準の注記に変更される場合）</li></ul></td></tr>
<tr><td>ヒント</td><td>読者が認識しておくべき補足的な知識や推奨事項を含みます。例: <ul><li>追加のトラブルシューティング記事</li><li>使いやすさを向上させるステップやショートカット（例: アプリ内メッセージの追加カスタマイズ）</li></ul></td></tr>
<tr><td>警告</td><td>読者が必ず対処すべき必須情報を含みます。以下のような内容が該当します: <ul><li>不可逆的な結果（例: キャンペーンやキャンバスの削除）</li><li>機能を破壊する動作</li><li>データの損失</li><li>その他の重大な警告</li></ul></td></tr>
</tbody>
</table>
{:/}

**アラートのベストプラクティス**  
以下は、アラートに関する一般的なガイドラインとベストプラクティスです。

一般的な原則として、記事の構造に不可欠なコンテンツ（機能の紹介、セットアップ手順、機能の使用手順など）にアラートを使用することは避けてください。判断に迷う場合は、ピアレビュー時にチームに相談してください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<colgroup><col style="width: 50%;"><col style="width: 50%;"></colgroup>
<thead>
<tr><th>ガイドライン</th><th>例</th></tr>
</thead>
<tbody>
<tr><td>アラート内の情報を明確で簡潔な文で説明します。</td><td>{% multi_lang_include alerts/note_alerts.md alert='Segment profiles first app use' %}<br><br> <a href="{{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment">ステップ4: セグメントにフィルターを追加するセクションの注記アラート</a></td></tr>
<tr><td>同じ記事の異なるセクションに適用されるアラートの場合、繰り返しのコンテンツを避けるために、これらの詳細をまとめた新しいセクションの作成を検討してください。</td><td>{% multi_lang_include currents/property_details_dispatch_state_source.md %}<br><br> <a href="{{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#subscription-group-state-change-events">メッセージエンゲージメントイベントのプロパティ詳細</a></td></tr>
<tr><td>アラート内の情報を短い段落やリストに分けます。</td><td>{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}<br><br> <a href="{{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/import_your_email_list/">メールリストのインポートの重要アラート</a></td></tr>
<tr><td>アラートの表示に影響を与える可能性のある追加のフォーマット（コードスニペット、ステップ、周囲の画像など）を考慮してください。</td><td>{% multi_lang_include alerts/tip_alerts.md alert='catalog data images' %}<br><br> <a href="{{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/#considerations">値下げ通知のコードスニペット付きヒントアラート</a></td></tr>
<tr><td>記事の冒頭にあるアラートには改行を含めます。</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_5.png %}" alt="記事の冒頭にあるアラートの例。"><br><br> <a href="{{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/implementation_guide/">コンテンツカード実装ガイド</a></td></tr>
<tr><td>ベータ機能について記述する場合、ベータステータスと関連する Braze の連絡先情報を示す重要アラートを含めます。このベータアラートは、概要テキストの後、最初のメイン見出しの前に配置してください。</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_6.png %}" alt="ベータ機能の重要アラートの例。"></td></tr>
<tr><td>可能な限り、2つ以上のアラートを連続して使用することは避けてください。代わりに、情報を再構成するか、テキストの一部として含めてください。</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_7.png %}" alt="2つのアラートが隣り合っている例。これは避けるべきです。"></td></tr>
<tr><td>アラートが長くなる場合は、情報をリストとして含む新しいセクションの作成を検討してください。例えば、トラブルシューティングの手順をアラートに含める代わりに、トラブルシューティングセクションを作成するか、関連記事へのリンクを提供することを検討してください。</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_8.png %}" alt="コンテンツの新しいセクションの例。"></td></tr>
</tbody>
</table>
{:/}

## アラートの例 {#alert-examples}

各アラートタイプがドキュメントでどのように、なぜ使用されるかについては、以下の例を参照してください。

### 重要アラート {#important-alert}

{% multi_lang_include alerts/important_alerts.md alert='Web push private browsing' %}

* **記事:** [Web プッシュ]({{site.baseurl}}/user_guide/message_building_by_channel/push/web/)
* **ユースケース:** Web プッシュのセットアップ時に読者が知っておくべき重要な機能の注意事項を含みます。
* **アラートの理由:** 注記アラートではなく重要アラートを使用します。これは、Web プッシュのセットアップ時に読者が知っておくべき内容の重要度がより高いためです。

{% multi_lang_include alerts/important_alerts.md alert='BCC address billable emails' %}

* **記事:** [メール設定]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/)
* **ユースケース:**
  - 請求対象メールが倍増する可能性に関する重要な機能の注意事項を提供します
  - 必要に応じてカスタマーサクセスマネージャーに連絡するよう読者を誘導します
* **アラートの理由:** ここでは、メール設定の BCC アドレスに関する詳細を伝えるために重要アラートを使用しています。この情報は、警告アラートではなく重要アラートとして提示するのが最適です。なぜなら、この情報を省略しても機能に不可逆的な影響（機能の破壊、永続的なデータ損失など）を与えないためです。

{% multi_lang_include alerts/important_alerts.md alert='Android notification priority' %}

* **記事:** [高度なキャンペーン設定]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#notification-display-priority)
* **ユースケース:** 通知の優先度に関する緊急性の高い機能の注意事項を含みます。読者を新しい情報にリダイレクトします。
* **アラートの理由:** ここでは、読者を最新の情報にリダイレクトし、そのセクションが特定のユーザーにのみ適用されることを強調するために、重要アラートが最適です。また、セクションヘッダーの後に配置されているため、読者はセクションの残りを読む前に重要アラートに対処する必要があります。

### 注記アラート {#note-alert}

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

* **記事:** [コンテンツカードの作成]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/)
* **ユースケース:** コンテンツカードについて詳しく学ぶ際に、読者が認識しておくべき追加情報を含みます。
* **アラートの理由:** この注記アラートは、Braze がユーザーの古いコンテンツカードをどのように循環させるかについてのバックグラウンド情報を提供します。これは読者にとって有用な補足情報であり、重要アラートやヒントアラートを使用する必要はありません。

{% multi_lang_include alerts/note_alerts.md alert='Custom Attributes time attribute' %}

* **記事:** [カスタム属性]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/)
* **ユースケース:** 読者が認識しておくべき一般的な情報を含みます。関連コンテンツ（時間属性）について詳しく学ぶための記事を提供します。
* **アラートの理由:** この情報は、重要アラートではなく注記アラートを使用して伝えるのが最適です。コンテンツの目的は一般的な情報を提供することであり、この情報を無視しても機能の使いやすさに影響しないためです。

{% multi_lang_include alerts/note_alerts.md alert='Manage custom data storage' %}

* **記事:** [カスタムデータの管理]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/#managing-properties)
* **ユースケース:** 読者が認識しておくべき一般的な情報を含みます。詳細については Braze の連絡先にリダイレクトします。
* **アラートの理由:** この注記アラートは、カスタム属性を管理する際に読者が知っておくと役立つデータストレージに関する追加情報を提供します。ただし、コンテンツは読者にとってより強い重要度の表示を必要としないため、注記アラートがここでは適切です。

### ヒントアラート {#tip-alert}

{% multi_lang_include alerts/tip_alerts.md alert='SMS segment calculator' %}

* **記事:** [SMS および RCS 請求計算ツール]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/)
* **ユースケース:** メッセージの長さと SMS セグメント数を理解するためのツールを読者に提供します。コピーの制限に関する理解に役立つ情報を提供します。
* **アラートの理由:** これは長めのヒントアラートです。コピーを入力してメッセージが何セグメントで送信されるかを確認するためのスペースを提供するためです。ヒントアラートがここでは最適な選択肢です。SMS メッセージのセットアッププロセスで読者が使用できる便利なジェネレーターだからです。

{% multi_lang_include alerts/tip_alerts.md alert='Export troubleshooting' %}

* **記事:** [日付別の日次アプリアンインストール KPI のエクスポート]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/)
* **ユースケース:** このエンドポイントを使用する際のトラブルシューティングのアドバイスを提供します。
* **アラートの理由:** ヒントアラートは読者に追加のサポートを提供します。注記アラートではなくヒントアラートを使用します。コンテンツの焦点がトラブルシューティング記事を提供して読者を支援することにあるためです。

### 警告アラート {#warning-alert}

{% multi_lang_include alerts/warning_alerts.md alert='User profile external_id' %}

* **記事:** [ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/)
* **ユースケース:** Braze でユーザープロファイルを作成する際に読者がすべきでないことを示します。
* **アラートの理由:** 警告アラートは、ユーザーを一意に識別する前に external_id を割り当てることに対して読者に注意を促すために使用されます。この情報は、重要アラートではなく警告アラートを使用して伝えるのが最適です。ユーザープロファイルに不可逆的な結果をもたらすためです。

{% multi_lang_include alerts/warning_alerts.md alert='Segment Currents multiple connectors' %}

* **記事:** [Segment for Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents/)
* **ユースケース:** Currents コネクターを作成する際に読者に注意を促します。これらのコネクターを誤って作成した場合の結果を含みます。
* **アラートの理由:** ここでは、Braze Segment Currents 統合の制限を説明するために警告アラートが最適です。重要アラートではなく警告アラートを使用します。同じ Currents コネクターを誤って複数作成すると、データが失われる可能性があるためです。

{% multi_lang_include alerts/warning_alerts.md alert='Canvas race condition audience trigger' %}

* **記事:** [キャンバスの作成]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
* **ユースケース:** 機能が正しく動作しない可能性のある情報をリストします。対象オーディエンスがキャンペーンを受信しなかったり、キャンバスに入らなかったりする可能性について詳述します。
* **アラートの理由:** ここでは、機能が正しく動作しない可能性があることを示すために警告アラートを使用しています。この情報は、重要アラートではなく警告アラートを使用して伝えるのが最適です。情報が重大であり、キャンバスの配信を破壊する可能性があるためです。