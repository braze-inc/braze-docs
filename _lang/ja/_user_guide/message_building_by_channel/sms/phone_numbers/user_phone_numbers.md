---
nav_title: "ユーザーの電話番号"
article_title: SMSユーザーの電話番号
page_order: 1
description: "このリファレンス記事では、SMS 電話番号の書式設定、電話番号のインポート方法、および SMS 購読グループにユーザーを追加する方法について説明します。"
page_type: reference
channel: 
  - SMS
  
---

# ユーザーの電話番号

> この記事では、ユーザーや顧客の電話番号にまつわるさまざまなトピックについて説明する。自分の番号に関する情報を探している場合は、当社の[「送信電話番号」]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/short_and_long_codes/)の記事を参照してください。

電話番号は、ユーザープロファイルに数字の文字列として表示されます。数字以外 (`,`、`-`、`(`など) を含む数字をインポートすると、数字以外が削除されます。たとえば、`+1 (724) 123-4567` をインポートすると、`17241234567` と表示されます。

## 電話番号のインポート

電話番号をインポートするには、[CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) をアップロードするか、[API]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) 経由でユーザーを作成します。

### フォーマット

ベストプラクティスとして、電話番号をインポートする最良の方法は [`E.164`](https://en.wikipedia.org/wiki/e.164)形式である。ただし、Brazeは、U.S.番号を可能な限り解釈または変換するよう努める。

U.S. のすべての番号は、有効な市外局番を持つ 10 桁の有効な電話番号でなければなりません。`+` とカントリーコードを指定せずに入力できます。Braze はすべての有効な10 桁の電話番号をU.S. 番号としてマッピングします。

すべての国際番号は、`+` で始まり、その後に国別コードと電話番号が続きます(e.g `+442071838750`)。

![][picture]{: style="max-width:50%;border: 0;"}

ただし、国コードや市外局番が異なる複数の地域に送信する場合は、`E.164` 形式を使用することをお勧めします。これは米国ベースの電話番号でも同様です。

次の表では、ローカル数値フォーマットとユニバーサル、`E.164` フォーマットの違いを確認できます。

| 国 | ローカル | 国コード | `E.164` |
|---|---|---|---|
| アメリカ合衆国 | `4155552671` | 1 | `+14155552671` |
| 英国 | `2071838750` | 44 | `+442071838750` |
| ブラジル | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

### SMS受信グループにユーザーを追加する

顧客が SMS メッセージを受信するには、有効な電話番号を持っていて、購読グループにオプトインしている必要があります。サブスクリプション・グループは、あなたが実行しているSMSプログラムと連動している（[SMSの法的要件に従い]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/)、各顧客の同意が記録されていることを確認する）。詳細については、[SMS サブスクリプショングループ][1]を参照してください。 

### 無効な電話番号を処理する

電話番号が無効であると判断された場合、Brazeはユーザーの電話番号を無効としてマークし、その電話番号に以降の通信を送信しようとしない。無効な電話番号には、ユーザープロファイルの [**エンゲージメント**] タブでマークが付けられます。

![][picture2]{: style="max-width:50%;border: 0;"}

電話番号は以下の理由で無効とみなされる：
- **プロバイダーエラー**: SMS プロバイダーから永続的なエラーを受信した。これは、提供された電話番号が正しくフォーマットされていないか、永久にSMSメッセージを受信できないことを示している。
- **非アクティブ化**: 携帯電話加入者がサービスを終了し、通信手段から番号を解放したため、電話番号が非アクティブになった (最終的にはその番号がリサイクルされ、新規ユーザーに割り当てられる可能性がある)。

これらの無効な電話番号は、[SMS エンドポイントを]({{site.baseurl}}/api/endpoints/sms/)使用して管理できます。 

{% alert note %}
複数のユーザープロファイルに同じ電話番号があり、その電話番号が無効とマークされている場合、その電話番号を持つ既存のユーザープロファイルはすべて無効と表示される。新規に作成されたユーザープロファイルに、最初から無効のマークが付けられることはありません。
{% endalert %}

また、[セグメントを作成する][2]ときに、無効な電話番号を持つユーザーを含めることも除外することもできます。 

### サードパーティの調達と検証

Brazeは、無効数字のソースとしてサードパーティのツールに依存している。Brazeは、これらのサービスの停止や誤報について責任を負わない。したがって、このツールは、無効な番号を確認するための唯一の遵守方法として信頼すべきではない。

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/
[2]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment
[picture] ： {% image_buster /assets/img/sms/e164.png %}
[picture2] ： {% image_buster /assets/img/sms/invalid_banner.png %}
