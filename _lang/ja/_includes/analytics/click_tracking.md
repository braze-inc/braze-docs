{% if include.section == "UTM parameters" %}

リンクの短縮により、URL を自動的に追跡できますが、URL に UTM パラメータを追加して、Google Analytics などのサードパーティの分析ツールでキャンペーンのパフォーマンスを追跡することもできます。

URL に UTM パラメータを追加するには、次の手順を実行します。

1. ベース URL から始めます。これは、追跡するページの URL です（`https://www.example.com` など）。
2. ベース URL の後に疑問符（?）を追加します。
3. 各 UTM パラメータをアンパサンド（&）で区切って追加します。

例: `https://www.example.com?utm_source=newsletter&utm_medium=sms`

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## よくある質問

### テスト送信時に受け取るリンクは実際の URL ですか？

キャンペーンがテスト送信前に下書きとして保存されている場合は、はい。それ以外の場合は、プレースホルダーリンクです。起動されたキャンペーンで送信される正確な URL は、テスト送信で送信された URL とは異なる場合があることに注意してください。

### URL を短縮する前に UTM パラメータを追加できますか？

はい。静的パラメータとダイナミックなパラメータの両方を追加できます。 

### 短縮 URL はどのくらいの期間有効ですか？

パーソナライズ済み URL は、URL 登録時から2か月間有効です。[統合リンク短縮]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/?sdktab=unified)の場合は、静的またはパーソナライズ済みの区別がなく、すべてのリンクは9週間有効です。

### リンクを短縮するために Braze SDK をインストールする必要がありますか？

いいえ。リンクの短縮は、SDK の統合なしで機能します。

{% endif %}

{% if include.section == "Custom Domains" %}

## カスタムドメイン

リンクの短縮では、独自のドメインを使用して短縮 URL の外観をパーソナライズし、一貫したブランドイメージを表現することもできます。詳細情報については、[カスタムドメイン]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/)を参照してください。

{% endif %}