{% if include.section == "UTM parameters" %}

リンクの短縮により、URL を自動的に追跡できますが、URL にUTM パラメータを追加して、Google Analytics などのサードパーティの分析ツールでキャンペーンのパフォーマンスを追跡することもできます。

URL にUTM パラメータを追加するには、次の手順を実行します。

1. ベースURL から始めます。これは、追跡するページのURL です(`https://www.example.com` など)。
2. ベースURL の後に疑問符(?) を追加します。
3. アンパサンド(&) で区切られた各UTM パラメータを追加します。

例は`https://www.example.com?utm_source=newsletter&utm_medium=sms`です。

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## よくある質問

### テスト送信時に受け取るリンクは実際のURLですか？

キャンペーンがテスト送信前に下書きとして保存されている場合は、はい。それ以外の場合は、プレースホルダーリンクです。送信されたキャンペーンで送信された正確な URL は、テスト送信で送信された URL とは異なる場合があることに注意してください。

### URLを短縮する前にUTMパラメータを追加できますか？

はい。静的パラメータとダイナミックなパラメータの両方を追加できます。 

### 短縮URLはどのくらいの期間有効ですか？

パーソナライズされた URL は、URL 登録時から2か月間有効です。

### リンクを短縮するためにBraze SDKをインストールする必要がありますか？

いいえ。リンクの短縮は、SDKの統合なしで機能します。

{% endif %}

{% if include.section == "Custom Domains" %}

## カスタムドメイン

リンクの短縮は、独自のドメインを使用して短縮URLの外観をパーソナライズし、一貫したブランド画像を表現するのに役立ちます。詳細については、[カスタムドメイン]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/)を参照してください。

{% endif %}