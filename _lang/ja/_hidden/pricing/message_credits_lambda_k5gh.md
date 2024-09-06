---
nav_title: メッセージクレジット - Lambda
permalink: "/message_credits_lambda_k5gh/"
hidden: true
noindex: true
hide_toc: true
---

# メッセージクレジット - Lambda (機密)

> メッセージクレジットは、当社の本来のSMS、MMS、およびWhatsApp製品のためのBrazeのクロスチャネルのなパッケージング構成です。Braze メッセージング チャネルsの先行タグを受講する際に、メッセージクレジットを活用し、柔軟かつ透明な体験を提供しています。このページのテーブルに表示されているチャネルのいずれかで購入されたクレジットの割り当てを使用できます。

{% alert note %}
チャネルs が異なれば、測定単位はレポート ing で異なります。<br><br>
<b>WhatsApp:</b>会話<br>
<b>SMS:</b>セグメント<br>
<b>MMS:</b>セグメント<br><br>
つまり、WhatsApp メッセージに使用されるクレジットは対話開始時に計算され、SMS とMMS メッセージの両方に使用されるクレジットは送信されるSegmentで計算されます。
<br><br>
最後に、キャリア料金は別途請求され(後払い)、このメッセージクレジットSKUの一部とはみなされません。
{% endalert %}

## 定義

列定義は次のとおりです。

|---------|-------------------------------------------------|
| **チャネル・クレジット比率** | チャネルごとの基準与信額 |
| **宛先** | Braze プラットフォームを介して送信される最終的な地域、国名、または種別 |
| **乗数** | 個別送信先のプライシングに応じて、チャンネル・クレジット・レシオにスケーラー |
| **1センドで使用したクレジット** | 1つのメッセージの送信に使用されたメッセージクレジットの正確な数<br> (伝文単位=チャネル与信比率×送信先乗数)  |
{: .reset-td-br-1 .reset-td-br-2}


## メッセージクレジットのクレジット率テーブル- Lambda

{% details クリックして展開 %}
<table>
    <colgroup>
        <col span="4" style="background-color:background-color:#FFFFFF;">
        <col style="background-color:#f0f0f5">
    </colgroup>
    <tr>
        <th><b>Channel</b></th>
        <th><b>チャネル・クレジット比率</b></th>
        <th><b>宛先</b></th>
        <th><b>乗数</b></th>
        <th class="credits-column"><b>1センドで使用したクレジット</b></th>
    </tr>
    <tr>
        <td>SMS - US/CA</td>
        <td>1</td>
        <td>米国</td>
        <td>1.00</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>SMS - US/CA</td>
        <td>1</td>
        <td>米国有料</td>
        <td>1.50</td>
        <td>1.50</td>
    </tr>
    <tr>
        <td>SMS - US/CA</td>
        <td>1</td>
        <td>カナダ</td>
        <td>1.00</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>SMS - US/CA</td>
        <td>1</td>
        <td>カナダ通行料無料</td>
        <td>1.30</td>
        <td>1.30</td>
    </tr>
    <tr>
        <td>MMS - 米国/カリフォルニア州</td>
        <td>3</td>
        <td>米国</td>
        <td>1.00</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>MMS - 米国/カリフォルニア州</td>
        <td>3</td>
        <td>米国有料</td>
        <td>2.00</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>MMS - 米国/カリフォルニア州</td>
        <td>3</td>
        <td>カナダロングコード</td>
        <td>1.50</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>MMS - 米国/カリフォルニア州</td>
        <td>3</td>
        <td>カナダ・ショートコード</td>
        <td>4.00</td>
        <td>12.00</td>
    </tr>
    <tr>
        <td>MMS - 米国/カリフォルニア州</td>
        <td>3</td>
        <td>カナダ通行料無料</td>
        <td>1.30</td>
        <td>3.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>アブハジア</td>
        <td>0.62</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>アフガニスタン</td>
        <td>2.48</td>
        <td>24.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>アルバニア</td>
        <td>1.04</td>
        <td>10.40</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>アルジェリア</td>
        <td>3.26</td>
        <td>32.60</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>アメリカ領サモア</td>
        <td>0.99</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>アンドラ</td>
        <td>1.18</td>
        <td>11.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>アンゴラ</td>
        <td>0.81</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>アングイラ</td>
        <td>0.99</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>アンティグア・バーブーダ</td>
        <td>0.98</td>
        <td>9.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>アルゼンチン</td>
        <td>1.40</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>アルメニア</td>
        <td>1.84</td>
        <td>18.40</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>アルバ</td>
        <td>0.95</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>オーストラリアのSMS</td>
        <td>0.39</td>
        <td>3.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>オーストラリアMMS</td>
        <td>該当なし</td>
        <td>該当なし</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>オーストリア</td>
        <td>0.53</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>アゼルバイジャン</td>
        <td>3.32</td>
        <td>33.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>バハマ</td>
        <td>0.93</td>
        <td>9.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>バハレーン</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>バングラデシュ</td>
        <td>2.76</td>
        <td>27.60</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>バルバドス</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ベラルーシ</td>
        <td>3.20</td>
        <td>32.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ベルギー</td>
        <td>1.48</td>
        <td>14.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ベリーズ</td>
        <td>1.66</td>
        <td>16.60</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ベナン</td>
        <td>0.92</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>バミューダ</td>
        <td>1.04</td>
        <td>10.40</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ブータン</td>
        <td>2.50</td>
        <td>25.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ボリビア</td>
        <td>1.40</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ボスニア・ヘルツェゴビナ</td>
        <td>1.01</td>
        <td>10.10</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ボツワナ</td>
        <td>1.23</td>
        <td>12.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ブラジル</td>
        <td>0.21</td>
        <td>2.10</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ブルネイ</td>
        <td>0.27</td>
        <td>2.70</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ブルガリア</td>
        <td>1.94</td>
        <td>19.40</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ブルキナファソ</td>
        <td>1.44</td>
        <td>14.40</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ブルンジ</td>
        <td>1.84</td>
        <td>18.40</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>カンボジア</td>
        <td>2.41</td>
        <td>24.10</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>カメルーン</td>
        <td>1.13</td>
        <td>11.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>カーボベルデ</td>
        <td>1.43</td>
        <td>14.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>カリブ海オランダ</td>
        <td>2.17</td>
        <td>21.70</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ケイマン諸島</td>
        <td>0.99</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>中央アフリカ共和国</td>
        <td>0.31</td>
        <td>3.10</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>チャド</td>
        <td>2.31</td>
        <td>23.10</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>チリ</td>
        <td>0.78</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>中国</td>
        <td>0.17</td>
        <td>1.70</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>コロンビア</td>
        <td>0.03</td>
        <td>0.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>コモロ</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>コンゴ</td>
        <td>0.68</td>
        <td>6.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>クック諸島</td>
        <td>0.68</td>
        <td>6.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>コスタリカ</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>クロアチア</td>
        <td>0.85</td>
        <td>8.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>キューバ</td>
        <td>1.86</td>
        <td>18.60</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>キュラカオ</td>
        <td>0.99</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>キプロス</td>
        <td>0.22</td>
        <td>2.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>チェコ共和国</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>デンマーク</td>
        <td>0.85</td>
        <td>8.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ジブチ</td>
        <td>1.09</td>
        <td>10.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ドミニカ</td>
        <td>0.96</td>
        <td>9.60</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ドミニカ共和国</td>
        <td>1.02</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>コンゴDR</td>
        <td>1.48</td>
        <td>14.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>エクアドル</td>
        <td>2.20</td>
        <td>22.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>エジプト</td>
        <td>2.10</td>
        <td>21.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>エルサルバドル</td>
        <td>0.86</td>
        <td>8.60</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>赤道ギニア</td>
        <td>0.54</td>
        <td>5.40</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>エリトリア</td>
        <td>1.47</td>
        <td>14.70</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>エストニア</td>
        <td>0.94</td>
        <td>9.40</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>エスワティーニ</td>
        <td>0.58</td>
        <td>5.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>エチオピア</td>
        <td>2.64</td>
        <td>26.40</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>フォークランド諸島</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>フェロー諸島</td>
        <td>0.23</td>
        <td>2.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>フィジー</td>
        <td>1.40</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>フィンランド</td>
        <td>1.15</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>フランス</td>
        <td>0.93</td>
        <td>9.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>フランスのギアナ</td>
        <td>2.01</td>
        <td>20.10</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>フランス領ポリネシア</td>
        <td>1.58</td>
        <td>15.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ガボン</td>
        <td>2.12</td>
        <td>21.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ガンビア</td>
        <td>1.24</td>
        <td>12.40</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>グルジア</td>
        <td>2.18</td>
        <td>21.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ドイツ</td>
        <td>1.73</td>
        <td>17.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ガーナ</td>
        <td>1.74</td>
        <td>17.40</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ジブラルタル</td>
        <td>0.16</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ギリシャ</td>
        <td>1.02</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>グリーンランド</td>
        <td>0.16</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>グレナダ</td>
        <td>1.03</td>
        <td>10.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>グアデルーペ</td>
        <td>2.00</td>
        <td>20.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>グアム</td>
        <td>0.62</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>グアテマラ</td>
        <td>1.86</td>
        <td>18.60</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ガーンジー</td>
        <td>0.87</td>
        <td>8.70</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ギニア</td>
        <td>1.83</td>
        <td>18.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ギニアビサウ</td>
        <td>1.45</td>
        <td>14.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ガイアナ</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ハイチ</td>
        <td>1.16</td>
        <td>11.60</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ホンジュラス</td>
        <td>0.72</td>
        <td>7.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>香港</td>
        <td>0.98</td>
        <td>9.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ハンガリー</td>
        <td>1.16</td>
        <td>11.60</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>アイスランド</td>
        <td>1.15</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>インド</td>
        <td>0.84</td>
        <td>8.40</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>インドネシア</td>
        <td>3.66</td>
        <td>36.60</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>イラン</td>
        <td>1.59</td>
        <td>15.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>イラク</td>
        <td>2.38</td>
        <td>23.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>アイルランド</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>マン島</td>
        <td>0.81</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>イスラエル</td>
        <td>1.50</td>
        <td>15.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>イタリア</td>
        <td>0.89</td>
        <td>8.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>コートジボワール</td>
        <td>1.55</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ジャマイカ</td>
        <td>1.10</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>日本</td>
        <td>0.92</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ジャージー</td>
        <td>0.70</td>
        <td>7.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ヨルダン</td>
        <td>2.58</td>
        <td>25.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>カザフスタン</td>
        <td>2.54</td>
        <td>25.40</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ケニア</td>
        <td>2.25</td>
        <td>22.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>キリバス</td>
        <td>0.31</td>
        <td>3.10</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>大韓民国</td>
        <td>0.30</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>コソボ</td>
        <td>0.97</td>
        <td>9.70</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>クウェート</td>
        <td>2.45</td>
        <td>24.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>キルギスタン</td>
        <td>2.64</td>
        <td>26.40</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ラオス人民民主共和国</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ラトビア</td>
        <td>0.74</td>
        <td>7.40</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>レバノン</td>
        <td>1.94</td>
        <td>19.40</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>レソト</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>リベリア</td>
        <td>0.72</td>
        <td>7.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>リビア</td>
        <td>2.68</td>
        <td>26.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>リヒテンシュタイン</td>
        <td>0.38</td>
        <td>3.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>リトアニア</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ルクセンブルグ</td>
        <td>1.03</td>
        <td>10.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>マカオ</td>
        <td>0.38</td>
        <td>3.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>マケドニア</td>
        <td>該当なし</td>
        <td>該当なし</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>マダガスカル</td>
        <td>2.22</td>
        <td>22.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>マラウイ</td>
        <td>2.24</td>
        <td>22.40</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>マレーシア</td>
        <td>0.79</td>
        <td>7.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>モルディブ</td>
        <td>0.87</td>
        <td>8.70</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>マリ</td>
        <td>2.17</td>
        <td>21.70</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>マルタ</td>
        <td>1.05</td>
        <td>10.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>マーシャル諸島</td>
        <td>該当なし</td>
        <td>該当なし</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>マルティニク</td>
        <td>1.88</td>
        <td>18.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>モーリタニア</td>
        <td>1.95</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>モーリシャス</td>
        <td>1.89</td>
        <td>18.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>マヨット</td>
        <td>2.33</td>
        <td>23.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>メキシコ</td>
        <td>0.28</td>
        <td>2.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ミクロネシア</td>
        <td>0.93</td>
        <td>9.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>モルドバ</td>
        <td>0.87</td>
        <td>8.70</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>モナコ</td>
        <td>1.62</td>
        <td>16.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>モンゴル</td>
        <td>1.93</td>
        <td>19.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>モンテネグロ</td>
        <td>0.99</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>モントセラット</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>モロッコ</td>
        <td>1.55</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>モザンビーク</td>
        <td>0.61</td>
        <td>6.10</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ミャンマー</td>
        <td>2.48</td>
        <td>24.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ナミビア</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ナウル</td>
        <td>1.12</td>
        <td>11.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ネパール</td>
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>オランダ</td>
        <td>1.82</td>
        <td>18.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ニューカレドニア</td>
        <td>1.49</td>
        <td>14.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ニュージーランド</td>
        <td>1.42</td>
        <td>14.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ニカラグア</td>
        <td>1.27</td>
        <td>12.70</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ニジェール</td>
        <td>1.60</td>
        <td>16.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ナイジェリア</td>
        <td>2.13</td>
        <td>21.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ニウエ</td>
        <td>該当なし</td>
        <td>該当なし</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ノーフォーク島</td>
        <td>該当なし</td>
        <td>該当なし</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>北マケドニア</td>
        <td>0.34</td>
        <td>3.40</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>キプロス北部</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ノルウェー</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>オマーン</td>
        <td>1.68</td>
        <td>16.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>パキスタン</td>
        <td>2.22</td>
        <td>22.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>パラオ</td>
        <td>0.37</td>
        <td>3.70</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>パレスチナ自治区</td>
        <td>該当なし</td>
        <td>該当なし</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>パナマ</td>
        <td>0.93</td>
        <td>9.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>パプアニューギニア</td>
        <td>0.99</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>パラグアイ</td>
        <td>0.28</td>
        <td>2.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ペルー</td>
        <td>1.10</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>フィリピン</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ポーランド</td>
        <td>0.39</td>
        <td>3.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ポルトガル</td>
        <td>0.37</td>
        <td>3.70</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>プエルトリコ</td>
        <td>0.13</td>
        <td>1.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>カタール</td>
        <td>0.39</td>
        <td>3.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>レユニオン/マヨット</td>
        <td>1.13</td>
        <td>11.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ルーマニア</td>
        <td>0.78</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ロシア</td>
        <td>1.89</td>
        <td>18.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ルワンダ</td>
        <td>1.21</td>
        <td>12.10</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>セントキッツとネビス</td>
        <td>0.92</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>セントルシア</td>
        <td>1.07</td>
        <td>10.70</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>セントピエールとミクロン</td>
        <td>2.31</td>
        <td>23.10</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>セントビンセントとグレナディーン諸島</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>サモア</td>
        <td>0.75</td>
        <td>7.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>サンマリノ</td>
        <td>該当なし</td>
        <td>該当なし</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>サントメ・プリンシペ</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>サウジアラビア</td>
        <td>1.07</td>
        <td>10.70</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>セネガル</td>
        <td>2.02</td>
        <td>20.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>セルビア</td>
        <td>0.89</td>
        <td>8.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>セイシェル</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>シエラレオネ</td>
        <td>1.35</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>シンガポール</td>
        <td>0.62</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>シント・マアーテン</td>
        <td>0.16</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>スロバキア</td>
        <td>0.81</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>スロベニア</td>
        <td>0.28</td>
        <td>2.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ソロモン諸島</td>
        <td>0.78</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ソマリア</td>
        <td>1.78</td>
        <td>17.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>南アフリカ</td>
        <td>0.27</td>
        <td>2.70</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>南オセチア</td>
        <td>2.05</td>
        <td>20.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>南スーダン</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>スペイン</td>
        <td>0.70</td>
        <td>7.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>スリランカ</td>
        <td>2.51</td>
        <td>25.10</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>スーダン</td>
        <td>2.24</td>
        <td>22.40</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>スリナム</td>
        <td>0.73</td>
        <td>7.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>スワジランド</td>
        <td>該当なし</td>
        <td>該当なし</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>スウェーデン</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>スイス</td>
        <td>0.61</td>
        <td>6.10</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>シリア</td>
        <td>該当なし</td>
        <td>該当なし</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>台湾</td>
        <td>1.63</td>
        <td>16.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>タジキスタン</td>
        <td>3.45</td>
        <td>34.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>タンザニア</td>
        <td>1.62</td>
        <td>16.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>タイ</td>
        <td>0.13</td>
        <td>1.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>東ティモール</td>
        <td>0.87</td>
        <td>8.70</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>トーゴ</td>
        <td>0.62</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>トンガ</td>
        <td>0.61</td>
        <td>6.10</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>トリニダード・トバゴ</td>
        <td>1.02</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>チュニジア</td>
        <td>2.20</td>
        <td>22.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>トルコ</td>
        <td>0.05</td>
        <td>0.50</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>トルクメニスタン</td>
        <td>1.97</td>
        <td>19.70</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>タークス・カイコス諸島</td>
        <td>0.99</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ツバル</td>
        <td>該当なし</td>
        <td>該当なし</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ウガンダ</td>
        <td>1.90</td>
        <td>19.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ウクライナ</td>
        <td>2.28</td>
        <td>22.80</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>アラブ首長国連邦</td>
        <td>0.42</td>
        <td>4.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>イギリス</td>
        <td>0.61</td>
        <td>6.10</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>不明</td>
        <td>該当なし</td>
        <td>該当なし</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ウルグアイ</td>
        <td>0.71</td>
        <td>7.10</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ウズベキスタン</td>
        <td>3.52</td>
        <td>35.20</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>バヌアツ</td>
        <td>1.43</td>
        <td>14.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ベネズエラ</td>
        <td>0.84</td>
        <td>8.40</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ベトナム</td>
        <td>1.49</td>
        <td>14.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>英領ヴァージン諸島</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>バージン諸島、U.S。</td>
        <td>該当なし</td>
        <td>該当なし</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ワリスとフツナ</td>
        <td>1.46</td>
        <td>14.60</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>イエメン</td>
        <td>1.63</td>
        <td>16.30</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ザンビア</td>
        <td>1.99</td>
        <td>19.90</td>
    </tr>
    <tr>
        <td>SMS/MMS - グローバル</td>
        <td>10</td>
        <td>ジンバブエ</td>
        <td>1.64</td>
        <td>16.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>アルゼンチン認証</td>
        <td>0.95</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>アルゼンチンマーケティング</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>アルゼンチンサービス</td>
        <td>0.85</td>
        <td>8.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>アルゼンチンユーティリティ</td>
        <td>1.10</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ブラジル認証</td>
        <td>0.85</td>
        <td>8.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ブラジルマーケティング</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ブラジルサービス</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ブラジルユーティリティ</td>
        <td>0.95</td>
        <td>2.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>チリ認証</td>
        <td>1.40</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>チリマーケティング</td>
        <td>2.35</td>
        <td>23.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>チリサービス</td>
        <td>1.20</td>
        <td>12.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>チリユーティリティー</td>
        <td>1.55</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>コロンビア認証</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>コロンビアマーケティング</td>
        <td>0.35</td>
        <td>3.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>コロンビア・サービス</td>
        <td>0.15</td>
        <td>1.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>コロンビア公益事業</td>
        <td>0.25</td>
        <td>0.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>エジプト認証</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>エジプト・マーケティング</td>
        <td>2.85</td>
        <td>28.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>エジプトサービス</td>
        <td>1.70</td>
        <td>17.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>エジプトユーティリティ</td>
        <td>1.80</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>フランス認証</td>
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>フランスマーケティング</td>
        <td>3.80</td>
        <td>38.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>フランスサービス</td>
        <td>2.30</td>
        <td>23.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>フランス公益事業</td>
        <td>2.05</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ドイツ認証</td>
        <td>2.05</td>
        <td>20.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ドイツマーケティング</td>
        <td>3.60</td>
        <td>36.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ドイツサービス</td>
        <td>2.15</td>
        <td>21.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ドイツ公益事業</td>
        <td>2.25</td>
        <td>14.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>インド認証</td>
        <td>0.04</td>
        <td>0.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>インド認証- 国際</td>
        <td>0.74</td>
        <td>7.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>インドマーケティング</td>
        <td>0.25</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>インドサービス</td>
        <td>0.10</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>インド公益事業</td>
        <td>0.10</td>
        <td>0.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>インドネシア認証</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>インドネシア認証- 国際</td>
        <td>3.61</td>
        <td>36.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>インドネシアマーケティング</td>
        <td>1.10</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>インドネシアサービス</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>インドネシア公益事業</td>
        <td>0.55</td>
        <td>5.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>イスラエル認証</td>
        <td>0.45</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>イスラエル・マーケティング</td>
        <td>0.95</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>イスラエルサービス</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>イスラエル公益事業</td>
        <td>0.50</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>イタリア認証</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>イタリアマーケティング</td>
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>イタリアサービス</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>イタリアユーティリティー</td>
        <td>1.10</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>マレーシア認証</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>マレーシアマーケティング</td>
        <td>2.30</td>
        <td>23.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>マレーシアサービス</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>マレーシア公益事業</td>
        <td>0.55</td>
        <td>3.70</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>メキシコ認証</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>メキシコマーケティング</td>
        <td>1.15</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>メキシコサービス</td>
        <td>0.30</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>メキシコユーティリティ</td>
        <td>0.70</td>
        <td>2.70</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>オランダ認証</td>
        <td>1.90</td>
        <td>19.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>オランダマーケティング</td>
        <td>4.25</td>
        <td>42.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>オランダサービス</td>
        <td>2.35</td>
        <td>23.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>オランダ公益事業</td>
        <td>2.10</td>
        <td>13.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ナイジェリア認証</td>
        <td>0.75</td>
        <td>7.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ナイジェリアマーケティング</td>
        <td>1.35</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ナイジェリアサービス</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ナイジェリア・ユーティリティ</td>
        <td>0.85</td>
        <td>1.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>北米認証</td>
        <td>0.35</td>
        <td>3.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>北米マーケティング</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>北米サービス</td>
        <td>0.25</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>北米ユーティリティ</td>
        <td>0.40</td>
        <td>1.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他の認証</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他マーケティング</td>
        <td>1.60</td>
        <td>16.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他のサービス</td>
        <td>0.40</td>
        <td>4.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他のユーティリティ</td>
        <td>0.90</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>パキスタン認証</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>パキスタンマーケティング</td>
        <td>1.25</td>
        <td>12.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>パキスタン・サービス</td>
        <td>0.40</td>
        <td>4.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>パキスタン・ユーティリティ</td>
        <td>0.65</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ペルー認証</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ペルーマーケティング</td>
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ペルーサービス</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ペルーユーティリティ</td>
        <td>1.10</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他のアフリカ認証</td>
        <td>0.40</td>
        <td>4.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他のアフリカマーケティング</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他のアフリカ・サービス</td>
        <td>0.95</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他のアフリカユーティリティ</td>
        <td>0.40</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他のアジアパシフィック認証</td>
        <td>1.15</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他のアジアパシフィックマーケティング</td>
        <td>1.95</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他のアジア太平洋サービス</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他のアジアパシフィックユーティリティ</td>
        <td>1.25</td>
        <td>4.20</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他の中央&amp;アンプ、東ヨーロッパ認証</td>
        <td>1.50</td>
        <td>15.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他中部&amp;アンプ、東欧マーケティング</td>
        <td>2.30</td>
        <td>23.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他中部&amp;アンプ、東欧サービス</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他中部&amp;アンプ、東欧ユーティリティー</td>
        <td>1.65</td>
        <td>9.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他のラテンアメリカ認証</td>
        <td>1.20</td>
        <td>12.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他のラテンアメリカ・マーケティング</td>
        <td>1.95</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他のラテンアメリカサービス</td>
        <td>1.10</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他のラテンアメリカ・ユーティリティ</td>
        <td>1.30</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他の中東認証</td>
        <td>0.45</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他中東マーケティング</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他の中東サービス</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他の中東電力会社</td>
        <td>0.55</td>
        <td>4.20</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他の西ヨーロッパ認証</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他の西ヨーロッパマーケティング</td>
        <td>1.55</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他の西ヨーロッパサービス</td>
        <td>1.05</td>
        <td>10.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他の西ヨーロッパユーティリティ</td>
        <td>1.10</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ロシア認証</td>
        <td>1.15</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ロシアマーケティング</td>
        <td>2.15</td>
        <td>21.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ロシアサービス</td>
        <td>1.05</td>
        <td>10.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ロシア公益事業</td>
        <td>1.25</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>サウジアラビア認証</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>サウジアラビアマーケティング</td>
        <td>1.10</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>サウジアラビアサービス</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>サウジアラビア公益事業</td>
        <td>0.65</td>
        <td>3.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>南アフリカ認証</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>南アフリカマーケティング</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>南アフリカサービス</td>
        <td>0.45</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>南アフリカユーティリティー</td>
        <td>0.55</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>スペイン認証</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>スペインマーケティング</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>スペインサービス</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>スペインユーティリティ</td>
        <td>1.00</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>トルコ認証</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>トルコマーケティング</td>
        <td>0.30</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>トルコサービス</td>
        <td>0.10</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>トルコ公益事業</td>
        <td>0.25</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>アラブ首長国連邦認証</td>
        <td>0.45</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>アラブ首長国連邦マーケティング</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>アラブ首長国連邦サービス</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>アラブ首長国連邦公益事業体</td>
        <td>0.55</td>
        <td>4.20</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>英国認証</td>
        <td>0.95</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>イギリスマーケティング</td>
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>英国サービス</td>
        <td>1.05</td>
        <td>10.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>英国公益事業</td>
        <td>1.05</td>
        <td>5.80</td>
    </tr>
</table>
{: .reset-td-br-1 .reset-td-br-2}
{% enddetails %}

------

## SMS/MMS チャネル内容

### SMSSegment

SMSメッセージSegmentは、SMS産業がメッセージを数える方法です。メッセージSegmentは、単一のSMS ディスパッチで送信される、定義された文字数(GSM-7 エンコードの場合は160、UCS-2 エンコードの場合は67)までのグループです。GSM-7 エンコードを使用して161 文字のSMS を送信すると、送信されたメッセージSegmentが2 つあることがわかります。複数のメールSegmentを送信すると、追加料金が発生します。

### MMSSegment

MMSの場合、メッセージの制限は5MBです(これにはマルチメディアアセットとメッセージ本文のサイズが含まれます)。安全のために、Braze では、マルチメディアアセットには600KB を超えず、メッセージ本文も含めることをお勧めします。

## WhatsApp チャネル内容

WhatsAppは、双方向のメッセージングに焦点を当てたチャネルであるため、(個々のメッセージの数ではなく)会話に固定されます。会話は、企業とエンドユーザーの間の24時間スレッドです。

### 会話タイプの定義

**マーケティング対話:**意識の喚起から販売・リターゲティング 顧客の促進まで、幅広い目標を達成できるビジネス主導の対話。たとえば、新商品、新サービス、機能のアナウンス、ターゲットを絞ったプロモーション/オファー、カート放棄のリマインダーなどです。

**ユーティリティの会話:**ユーザー アクション s またはリクエストのフォローアップを可能にするビジネス開始の対話。たとえば、オプトイン確認、注文/配信管理(e.g、配信更新)、取引先更新または警告(e.g、支払リマインダー)、またはフィードバック アンケートなどです。

**認証会話:**ユーザー s をワンタイムパスコードs で認証できるようにします。ログインプロセスでは、複数のステップs で認証される可能性があります(e.g、アカウント検証、アカウントリカバリ、整合性の問題)。

{% alert note %}
認証の対話はケースバイケースでのみサポートされ、Braze は特定のSLA を保証できません。また、Brazeは暗証番号の生成に対応していません。
{% endalert %}

**サービス会話:**テンプレート 以外のd メッセージで応答された、ユーザーが開始した会話。

{% alert note %}
マーケティングまたはユーティリティテンプレートで応答されるユーザ起動の対話は、そのように課金されます。
{% endalert %}

## 請求地域内訳

#### 北米

米国、カナダ

#### その他のアフリカ

アルジェリア、アンゴラ、ベニン、ボツワナ、ブルキナファソ、ブルンジ、カメルーン、チャド、コンゴ、エリトリア、エチオピア、ガボン、ガンビア、ガーナ、ギニア・ビサウ、コートジボリー、ケニア、レソト、リベリア、
マダガスカル、マラウイ、マリ、モーリタニア、モロッコ、モザンビーク、ナミビア、ニジェール、ルワンダ、セネガル、シエラレオネ、ソマリア、南スーダン、スーダン、スワジランド、タンザニア、トーゴ、チュニジア、ウガンダ、ザンビア

#### その他のアジア太平洋地域

アフガニスタン、オーストラリア、バングラデシュ、カンボジア、中国、香港、日本、ラオス、モンゴル、ネパール、ニュージーランド、パプアニューギニア、フィリピン、シンガポール、スリランカ、台湾、タジキスタン、タイ、
トルクメニスタン、ウズベキスタン、ベトナム

#### その他中部・アンプ、東欧

アルバニア、アルメニア、アゼルバイジャン、ベラルーシ、ブルガリア、クロアチア、チェコ、グルジア、ギリシャ、ハンガリー、ラトビア、リトアニア、マケドニア、モルドバ、ポーランド、ルーマニア、セルビア、スロバキア、スロベニア、ウクライナ

#### その他のラテンアメリカ

ボリビア、コスタリカ、ドミニカ共和国、エクアドル、エルサルバドル、
グアテマラ、ハイチ、ホンジュラス、ジャマイカ、ニカラグア、パナマ、パラグアイ、プエルトリコ、ウルグアイ、ベネズエラ

#### その他の中東

バハレーン、イラク、ヨルダン、クウェート、レバノン、オマーン、カタール、イエメン

#### その他の西ヨーロッパ

オーストリア、ベルギー、デンマーク、フィンランド、アイルランド、ノルウェー、ポルトガル、スウェーデン、スイス
