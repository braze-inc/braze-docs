---
nav_title: メッセージクレジット- ガンマ
permalink: "/message_credits_gamma_0dhr/"
hidden: true
noindex: true
hide_toc: true
---

# メッセージクレジット- ガンマ(機密)

> メッセージクレジットは、当社のネイティブなSMS、MMS、WhatsApp製品のための、Brazeのクロスチャンネル包装構造です。メッセージクレジットを使用して、Brazeメッセージングチャネルを利用する際に、柔軟で透明性のある体験を提供します。このページの表に示されているいずれかのチャネルで購入されたクレジットの割り当てを使用できます。

{% alert note %}
チャネルごとに、消費されるクレジットを定義する測定単位が異なります。<br><br>
<b>WhatsApp:</b>会話<br>
<b>SMS:</b>セグメント<br>
<b>MMS:</b>セグメント<br><br>
つまり、WhatsApp メッセージに使用されるクレジットは会話開始時に計算され、SMS メッセージとMMS メッセージの両方に使用されるクレジットは送信されるセグメントで計算されます。
<br><br>
最後に、キャリア料金は別途請求され(後払い)、このメッセージクレジットSKUの一部とはみなされません。
{% endalert %}

## 定義

列定義は次のとおりです。

|---------|-------------------------------------------------|
| **Channel Credit Ratio** | 各チャネルのベースライン与信額|
| **宛先** | Braze プラットフォーム経由で送信される特定の最終的な地域、国、またはメッセージのタイプ|
| **Multiplier** | Scaler to the Channel Credit Ratio (特定の宛先の料金に応じて)
| **1つのメッセージで消費されたクレジット**|1つのメッセージを送信するために使用されたメッセージクレジットの正確な数<br> (1 つのメッセージで消費されたクレジット= チャネルクレジットレシオx 宛先乗数) |
{: .reset-td-br-1 .reset-td-br-2}


## メッセージ・クレジット・ガンマの与信比率表

{% details Click to expand %}
<table>
    <colgroup>
        <col span="4" style="background-color:background-color:#FFFFFF;">
        <col style="background-color:#f0f0f5">
    </colgroup>
    <tr>
        <th><b>チャネル</b></th>
        <th><b>チャネル・クレジット比率</b></th>
        <th><b>宛先</b></th>
        <th><b>乗数</b></th>
        <th class="credits-column"><b>ワンメッセージで消費されるクレジット</b></th>
    </tr>
    <tbody><tr>
    <td>SMS - US/CA</td>
    <td>2.3.</td>
    <td>米国</td>
    <td>1.00</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS - US/CA</td>
    <td>2.3.</td>
    <td>米国有料</td>
    <td>2.3.</td>
    <td>0.60</td>
    </tr>
    <tr>
    <td>SMS - US/CA</td>
    <td>2.3.</td>
    <td>カナダ</td>
    <td>1.00</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS - US/CA</td>
    <td>2.3.</td>
    <td>カナダ通行料無料</td>
    <td>2.3.</td>
    <td>0.52</td>
    </tr>
    <tr>
    <td>MMS - 米国/カリフォルニア州</td>
    <td>2.3.</td>
    <td>米国</td>
    <td>1.00</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>MMS - 米国/カリフォルニア州</td>
    <td>2.3.</td>
    <td>米国有料</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>MMS - 米国/カリフォルニア州</td>
    <td>2.3.</td>
    <td>カナダロングコード</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>MMS - 米国/カリフォルニア州</td>
    <td>2.3.</td>
    <td>カナダ・ショートコード</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>MMS - 米国/カリフォルニア州</td>
    <td>2.3.</td>
    <td>カナダ通行料無料</td>
    <td>2.3.</td>
    <td>1.56</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>アブハジア</td>
    <td>0.62</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>アフガニスタン</td>
    <td>9.47</td>
    <td>94.70</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>アルバニア</td>
    <td>2.29</td>
    <td>22.90</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>アルジェリア</td>
    <td>5.23</td>
    <td>52.30</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>アメリカ領サモア</td>
    <td>4.74</td>
    <td>47.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>アンドラ</td>
    <td>3.32</td>
    <td>33.20</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>アンゴラ</td>
    <td>2.24</td>
    <td>22.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>アングイラ</td>
    <td>3.33</td>
    <td>33.30</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>アンティグア・バーブーダ</td>
    <td>2.47</td>
    <td>24.70</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>アルゼンチン</td>
    <td>1.02</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>アルメニア</td>
    <td>3.49</td>
    <td>34.90</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>アルバ</td>
    <td>2.61</td>
    <td>26.10</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>オーストラリアのSMS</td>
    <td>0.36</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>オーストラリアMMS</td>
    <td>2.3.</td>
    <td>31.00</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>オーストリア</td>
    <td>1.77</td>
    <td>17.70</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>アゼルバイジャン</td>
    <td>9.77</td>
    <td>97.70</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>バハマ</td>
    <td>1.23</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>バハレーン</td>
    <td>0.92</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>バングラデシュ</td>
    <td>5.81</td>
    <td>58.10</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>バルバドス</td>
    <td>3.09</td>
    <td>30.90</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ベラルーシ</td>
    <td>6.35</td>
    <td>63.50</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ベルギー</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ベリーズ</td>
    <td>2.3.</td>
    <td>69.00</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ベナン</td>
    <td>3.64</td>
    <td>36.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>バミューダ</td>
    <td>2.3.</td>
    <td>29.90</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ブータン</td>
    <td>10.10</td>
    <td>101.00</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ボリビア</td>
    <td>3.66</td>
    <td>36.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ボスニア・ヘルツェゴビナ</td>
    <td>2.12</td>
    <td>21.20</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ボツワナ</td>
    <td>2.52</td>
    <td>25.20</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ブラジル</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ブルネイ</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ブルガリア</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ブルキナファソ</td>
    <td>3.35</td>
    <td>33.50</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ブルンジ</td>
    <td>9.47</td>
    <td>94.70</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>カンボジア</td>
    <td>2.3.</td>
    <td>43.00</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>カメルーン</td>
    <td>3.49</td>
    <td>34.90</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>カーボベルデ</td>
    <td>3.66</td>
    <td>36.60</td>
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
    <td>3.37</td>
    <td>33.70</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>中央アフリカ共和国</td>
    <td>3.07</td>
    <td>30.70</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>チャド</td>
    <td>2.3.</td>
    <td>73.00</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>チリ</td>
    <td>1.64</td>
    <td>16.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>中国</td>
    <td>0.64</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>コロンビア</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>コモロ</td>
    <td>2.3.</td>
    <td>61.90</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>コンゴ</td>
    <td>5.04</td>
    <td>50.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>クック諸島</td>
    <td>3.52</td>
    <td>35.20</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>コスタリカ</td>
    <td>1.06</td>
    <td>10.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>クロアチア</td>
    <td>2.31</td>
    <td>23.10</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>キューバ</td>
    <td>2.12</td>
    <td>21.20</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>キュラソー島</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>キプロス</td>
    <td>2.18</td>
    <td>21.80</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>チェコ共和国</td>
    <td>1.01</td>
    <td>10.10</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>デンマーク</td>
    <td>1.01</td>
    <td>10.10</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ジブチ</td>
    <td>4.09</td>
    <td>40.90</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ドミニカ</td>
    <td>3.79</td>
    <td>37.90</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ドミニカ共和国</td>
    <td>1.29</td>
    <td>12.90</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>コンゴDR</td>
    <td>5.77</td>
    <td>57.70</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>エクアドル</td>
    <td>2.76</td>
    <td>27.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>エジプト</td>
    <td>2.43</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>エルサルバドル</td>
    <td>2.3.</td>
    <td>24.50</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>赤道ギニア</td>
    <td>4.36</td>
    <td>43.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>エリトリア</td>
    <td>2.48</td>
    <td>24.80</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>エストニア</td>
    <td>2.41</td>
    <td>24.10</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>エスワティーニ</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>エチオピア</td>
    <td>8.63</td>
    <td>86.30</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>フォークランド諸島</td>
    <td>3.43</td>
    <td>34.30</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>フェロー諸島</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>フィジー</td>
    <td>2.3.</td>
    <td>41.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>フィンランド</td>
    <td>1.46</td>
    <td>14.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>フランス</td>
    <td>0.98</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>フランス領ギアナ</td>
    <td>4.64</td>
    <td>46.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>フランス領ポリネシア</td>
    <td>4.53</td>
    <td>45.30</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ガボン</td>
    <td>2.3.</td>
    <td>66.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ガンビア</td>
    <td>2.3.</td>
    <td>41.80</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>グルジア</td>
    <td>2.63</td>
    <td>26.30</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ドイツ</td>
    <td>1.88</td>
    <td>18.80</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ガーナ</td>
    <td>2.26</td>
    <td>22.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ジブラルタル</td>
    <td>2.75</td>
    <td>27.50</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ギリシャ</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>グリーンランド</td>
    <td>1.03</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>グレナダ</td>
    <td>4.09</td>
    <td>40.90</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>グアデルーペ</td>
    <td>2.3.</td>
    <td>34.00</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>グアム</td>
    <td>1.73</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>グアテマラ</td>
    <td>2.3.</td>
    <td>32.00</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ガーンジー</td>
    <td>0.87</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ギニア</td>
    <td>3.82</td>
    <td>38.20</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ギニアビサウ</td>
    <td>3.97</td>
    <td>39.70</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ガイアナ</td>
    <td>2.3.</td>
    <td>45.00</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ハイチ</td>
    <td>5.94</td>
    <td>59.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ホンジュラス</td>
    <td>2.13</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>香港</td>
    <td>1.35</td>
    <td>13.50</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ハンガリー</td>
    <td>1.91</td>
    <td>19.10</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>アイスランド</td>
    <td>1.75</td>
    <td>17.50</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>インド</td>
    <td>1.00</td>
    <td>10.00</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>インドネシア</td>
    <td>6.63</td>
    <td>66.30</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>イラン</td>
    <td>6.25</td>
    <td>62.50</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>イラク</td>
    <td>2.3.</td>
    <td>47.90</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>アイルランド</td>
    <td>1.31</td>
    <td>13.10</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>マン島</td>
    <td>0.81</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>イスラエル</td>
    <td>3.74</td>
    <td>37.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>イタリア</td>
    <td>0.87</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>コートジボワール</td>
    <td>2.48</td>
    <td>24.80</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ジャマイカ</td>
    <td>2.3.</td>
    <td>30.50</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>日本</td>
    <td>1.02</td>
    <td>2.3.</td>
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
    <td>5.56</td>
    <td>55.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>カザフスタン</td>
    <td>5.52</td>
    <td>55.20</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ケニア</td>
    <td>2.62</td>
    <td>26.20</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>キリバス</td>
    <td>3.67</td>
    <td>36.70</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>大韓民国</td>
    <td>0.69</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>コソボ</td>
    <td>0.97</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>クウェート</td>
    <td>3.34</td>
    <td>33.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>キルギスタン</td>
    <td>2.3.</td>
    <td>61.20</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ラオス人民民主共和国</td>
    <td>2.3.</td>
    <td>15.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ラトビア</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>レバノン</td>
    <td>3.07</td>
    <td>30.70</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>レソト</td>
    <td>2.3.</td>
    <td>51.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>リベリア</td>
    <td>3.47</td>
    <td>34.70</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>リビア</td>
    <td>2.3.</td>
    <td>81.70</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>リヒテンシュタイン</td>
    <td>0.84</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>リトアニア</td>
    <td>1.37</td>
    <td>13.70</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ルクセンブルク</td>
    <td>1.86</td>
    <td>18.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>マカオ</td>
    <td>1.49</td>
    <td>14.90</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>マケドニア</td>
    <td>1.88</td>
    <td>18.80</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>マダガスカル</td>
    <td>2.3.</td>
    <td>94.00</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>マラウイ</td>
    <td>5.72</td>
    <td>57.20</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>マレーシア</td>
    <td>1.47</td>
    <td>14.70</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>モルディブ</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>マリ</td>
    <td>3.97</td>
    <td>39.70</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>マルタ</td>
    <td>1.64</td>
    <td>16.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>マーシャル諸島</td>
    <td>2.3.</td>
    <td>40.00</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>マルティニク</td>
    <td>3.33</td>
    <td>33.30</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>モーリタニア</td>
    <td>6.51</td>
    <td>65.10</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>モーリシャス</td>
    <td>4.02</td>
    <td>40.20</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>マヨット</td>
    <td>2.33</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>メキシコ</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ミクロネシア</td>
    <td>2.3.</td>
    <td>18.50</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>モルドバ</td>
    <td>1.59</td>
    <td>15.90</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>モナコ</td>
    <td>4.68</td>
    <td>46.80</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>モンゴル</td>
    <td>7.03</td>
    <td>70.30</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>モンテネグロ</td>
    <td>2.87</td>
    <td>28.70</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>モントセラト</td>
    <td>2.77</td>
    <td>27.70</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>モロッコ</td>
    <td>2.64</td>
    <td>26.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>モザンビーク</td>
    <td>2.76</td>
    <td>27.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ミャンマー</td>
    <td>5.84</td>
    <td>58.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ナミビア</td>
    <td>1.58</td>
    <td>15.80</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ナウル</td>
    <td>2.3.</td>
    <td>11.20</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ネパール</td>
    <td>3.82</td>
    <td>38.20</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>オランダ</td>
    <td>1.65</td>
    <td>16.50</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ニューカレドニア</td>
    <td>4.44</td>
    <td>44.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ニュージーランド</td>
    <td>1.92</td>
    <td>19.20</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ニカラグア</td>
    <td>2.3.</td>
    <td>19.50</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ニジェール</td>
    <td>2.3.</td>
    <td>74.90</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ナイジェリア</td>
    <td>5.01</td>
    <td>50.10</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ニウエ</td>
    <td>2.3.</td>
    <td>48.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ノーフォーク島</td>
    <td>0.71</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>北マケドニア</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>キプロス北部</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ノルウェー</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>オマーン</td>
    <td>2.3.</td>
    <td>36.00</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>パキスタン</td>
    <td>7.46</td>
    <td>74.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>パラオ</td>
    <td>2.52</td>
    <td>25.20</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>パレスチナ自治区</td>
    <td>7.68</td>
    <td>76.80</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>パナマ</td>
    <td>2.23</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>パプアニューギニア</td>
    <td>19.01</td>
    <td>190.10</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>パラグアイ</td>
    <td>1.84</td>
    <td>18.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ペルー</td>
    <td>0.81</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>フィリピン</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ポーランド</td>
    <td>0.52</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ポルトガル</td>
    <td>0.60</td>
    <td>6.00</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>プエルトリコ</td>
    <td>1.06</td>
    <td>10.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>カタール</td>
    <td>0.52</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>レユニオン/マヨット</td>
    <td>4.82</td>
    <td>48.20</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ルーマニア</td>
    <td>1.06</td>
    <td>10.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ロシア</td>
    <td>9.54</td>
    <td>95.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ルワンダ</td>
    <td>4.66</td>
    <td>46.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>セントキッツとネビス</td>
    <td>0.92</td>
    <td>2.3.</td>
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
    <td>4.68</td>
    <td>46.80</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>サンマリノ</td>
    <td>2.76</td>
    <td>27.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>サントメ・プリンシペ</td>
    <td>3.29</td>
    <td>32.90</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>サウジアラビア</td>
    <td>1.91</td>
    <td>19.10</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>セネガル</td>
    <td>2.3.</td>
    <td>51.50</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>セルビア</td>
    <td>6.09</td>
    <td>60.90</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>セイシェル</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>シエラレオネ</td>
    <td>4.73</td>
    <td>47.30</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>シンガポール</td>
    <td>0.70</td>
    <td>7.00</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>シント・マアーテン</td>
    <td>0.16</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>スロバキア</td>
    <td>2.23</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>スロベニア</td>
    <td>3.76</td>
    <td>37.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ソロモン諸島</td>
    <td>2.09</td>
    <td>20.90</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ソマリア</td>
    <td>4.74</td>
    <td>47.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>南アフリカ</td>
    <td>0.32</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>南オセチア</td>
    <td>2.3.</td>
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
    <td>0.80</td>
    <td>8.00</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>スリランカ</td>
    <td>2.3.</td>
    <td>56.00</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>セント・キッツとネビス</td>
    <td>2.3.</td>
    <td>28.00</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>セントルシア</td>
    <td>2.59</td>
    <td>25.90</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>セントピエールとミクロン</td>
    <td>2.3.</td>
    <td>38.00</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>セントビンセント・グレナディーンズ</td>
    <td>4.08</td>
    <td>40.80</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>スーダン</td>
    <td>2.3.</td>
    <td>41.50</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>スリナム</td>
    <td>3.28</td>
    <td>32.80</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>スワジランド</td>
    <td>2.32</td>
    <td>23.20</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>スウェーデン</td>
    <td>0.86</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>スイス</td>
    <td>0.60</td>
    <td>6.00</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>シリア</td>
    <td>7.86</td>
    <td>78.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>台湾</td>
    <td>0.84</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>タジキスタン</td>
    <td>11.35</td>
    <td>113.50</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>タンザニア</td>
    <td>2.3.</td>
    <td>53.80</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>タイ</td>
    <td>0.36</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>東ティモール</td>
    <td>2.86</td>
    <td>28.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>トーゴ</td>
    <td>3.84</td>
    <td>38.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>トンガ</td>
    <td>2.3.</td>
    <td>31.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>トリニダード・トバゴ</td>
    <td>3.02</td>
    <td>30.20</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>チュニジア</td>
    <td>7.06</td>
    <td>70.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>トルコ</td>
    <td>0.77</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>トルクメニスタン</td>
    <td>5.04</td>
    <td>50.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>タークス・カイコス諸島</td>
    <td>3.38</td>
    <td>33.80</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ツバル</td>
    <td>3.36</td>
    <td>33.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ウガンダ</td>
    <td>2.3.</td>
    <td>40.50</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ウクライナ</td>
    <td>2.86</td>
    <td>28.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>アラブ首長国連邦</td>
    <td>2.3.</td>
    <td>12.40</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>イギリス</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>不明</td>
    <td>3.92</td>
    <td>39.20</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ウルグアイ</td>
    <td>2.3.</td>
    <td>21.50</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ウズベキスタン</td>
    <td>6.88</td>
    <td>68.80</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>バヌアツ</td>
    <td>2.3.</td>
    <td>41.80</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ベネズエラ</td>
    <td>2.3.</td>
    <td>21.50</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ベトナム</td>
    <td>2.3.</td>
    <td>30.50</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>英領ヴァージン諸島</td>
    <td>4.73</td>
    <td>47.30</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>米国バージン諸島</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ワリスとフツナ</td>
    <td>2.77</td>
    <td>27.70</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>イエメン</td>
    <td>2.3.</td>
    <td>60.30</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ザンビア</td>
    <td>6.76</td>
    <td>67.60</td>
    </tr>
    <tr>
    <td>SMS/MMS - グローバル</td>
    <td>10</td>
    <td>ジンバブエ</td>
    <td>3.55</td>
    <td>35.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>アルゼンチン認証</td>
    <td>2.3.</td>
    <td>2.3.</td>
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
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>アルゼンチンユーティリティ</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>ブラジル認証</td>
    <td>2.3.</td>
    <td>2.3.</td>
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
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>チリ認証</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>チリマーケティング</td>
    <td>2.3.</td>
    <td>23.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>チリサービス</td>
    <td>2.3.</td>
    <td>12.00</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>チリユーティリティー</td>
    <td>2.3.</td>
    <td>15.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>コロンビア認証</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>コロンビアマーケティング</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>コロンビア・サービス</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>コロンビア公益事業</td>
    <td>2.3.</td>
    <td>2.3.</td>
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
    <td>2.3.</td>
    <td>28.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>エジプトサービス</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>エジプトユーティリティ</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>フランス認証</td>
    <td>2.3.</td>
    <td>18.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>フランスマーケティング</td>
    <td>2.3.</td>
    <td>38.00</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>フランスサービス</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>フランス公益事業</td>
    <td>2.3.</td>
    <td>20.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>ドイツ認証</td>
    <td>2.3.</td>
    <td>20.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>ドイツマーケティング</td>
    <td>2.3.</td>
    <td>36.00</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>ドイツサービス</td>
    <td>2.3.</td>
    <td>21.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>ドイツ公益事業</td>
    <td>2.3.</td>
    <td>22.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>N/A</td>
    <td>インド認証</td>
    <td>N/A</td>
    <td>N/A</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>インドマーケティング</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>インドサービス</td>
    <td>2.3.</td>
    <td>1.00</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>インド公益事業</td>
    <td>2.3.</td>
    <td>1.00</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>N/A</td>
    <td>インドネシア認証</td>
    <td>N/A</td>
    <td>N/A</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>インドネシアマーケティング</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>インドネシアサービス</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>インドネシア公益事業</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>イスラエル認証</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>イスラエル・マーケティング</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>イスラエルサービス</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>イスラエル公益事業</td>
    <td>2.3.</td>
    <td>2.3.</td>
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
    <td>2.3.</td>
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
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>マレーシア認証</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>マレーシアマーケティング</td>
    <td>2.3.</td>
    <td>2.3.</td>
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
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>メキシコ認証</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>メキシコマーケティング</td>
    <td>2.3.</td>
    <td>11.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>メキシコサービス</td>
    <td>2.3.</td>
    <td>3.00</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>メキシコユーティリティ</td>
    <td>0.70</td>
    <td>7.00</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>オランダ認証</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>オランダマーケティング</td>
    <td>2.3.</td>
    <td>42.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>オランダサービス</td>
    <td>2.3.</td>
    <td>23.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>オランダ公益事業</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>ナイジェリア認証</td>
    <td>2.3.</td>
    <td>2.3.</td>
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
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>北米認証</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>北米マーケティング</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>北米サービス</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>北米ユーティリティ</td>
    <td>2.3.</td>
    <td>2.3.</td>
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
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>その他のサービス</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>その他のユーティリティ</td>
    <td>0.90</td>
    <td>2.3.</td>
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
    <td>2.3.</td>
    <td>12.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>パキスタン・サービス</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>パキスタン・ユーティリティ</td>
    <td>2.3.</td>
    <td>2.3.</td>
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
    <td>2.3.</td>
    <td>18.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>ペルーサービス</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>ペルーユーティリティ</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>その他のアフリカ認証</td>
    <td>2.3.</td>
    <td>2.3.</td>
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
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>その他のアフリカユーティリティ</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>その他のアジアパシフィック認証</td>
    <td>2.3.</td>
    <td>11.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>その他のアジアパシフィックマーケティング</td>
    <td>2.3.</td>
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
    <td>2.3.</td>
    <td>12.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>その他の中央&アンプ、東ヨーロッパ認証</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>その他中部&アンプ、東欧マーケティング</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>その他中部&アンプ、東欧サービス</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>その他中部&アンプ、東欧ユーティリティー</td>
    <td>1.65</td>
    <td>16.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>その他のラテンアメリカ認証</td>
    <td>2.3.</td>
    <td>12.00</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>その他のラテンアメリカ・マーケティング</td>
    <td>2.3.</td>
    <td>19.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>その他のラテンアメリカサービス</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>その他のラテンアメリカ・ユーティリティ</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>その他の中東認証</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>その他中東マーケティング</td>
    <td>0.90</td>
    <td>2.3.</td>
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
    <td>2.3.</td>
    <td>2.3.</td>
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
    <td>2.3.</td>
    <td>15.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>その他の西ヨーロッパサービス</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>その他の西ヨーロッパユーティリティ</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>ロシア認証</td>
    <td>2.3.</td>
    <td>11.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>ロシアマーケティング</td>
    <td>2.3.</td>
    <td>21.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>ロシアサービス</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>ロシア公益事業</td>
    <td>2.3.</td>
    <td>12.50</td>
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
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>サウジアラビアサービス</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>サウジアラビア公益事業</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>南アフリカ認証</td>
    <td>2.3.</td>
    <td>2.3.</td>
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
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>南アフリカユーティリティー</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>スペイン認証</td>
    <td>0.90</td>
    <td>2.3.</td>
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
    <td>10.00</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>トルコ認証</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>トルコマーケティング</td>
    <td>2.3.</td>
    <td>3.00</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>トルコサービス</td>
    <td>2.3.</td>
    <td>1.00</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>トルコ公益事業</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>アラブ首長国連邦認証</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>アラブ首長国連邦マーケティング</td>
    <td>0.90</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>アラブ首長国連邦サービス</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>アラブ首長国連邦公益事業体</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>英国認証</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>イギリスマーケティング</td>
    <td>2.3.</td>
    <td>18.50</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>英国サービス</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
    <tr>
    <td>WhatsApp</td>
    <td>10</td>
    <td>英国公益事業</td>
    <td>2.3.</td>
    <td>2.3.</td>
    </tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2}
{% enddetails %}

------

## SMS/MMSチャンネルの詳細

### SMSセグメント

SMSメッセージセグメントは、SMS業界がメッセージをカウントする方法です。メッセージセグメントは、1 つのSMS ディスパッチで送信される、定義された文字数(GSM-7 エンコーディングの場合は160、UCS-2 エンコーディングの場合は67)までのグループです。GSM-7エンコーディングを使用して161文字のSMSを送信すると、送信されたメッセージセグメントが2つあることがわかります。複数のメッセージセグメントを送信すると、追加料金が発生します。

### MMSセグメント

MMSの場合、メッセージの制限は5MBです(これにはマルチメディアアセットとメッセージ本文のサイズが含まれます)。より安全な側に置くために、Braze は、メッセージ本文を含めながら、マルチメディアアセットに600KB を超えないことをお勧めします。

## WhatsAppチャネルの詳細

WhatsAppは双方向メッセージングに焦点を当てたチャネルであり、したがって(個々のメッセージの数ではなく)会話にアンカーする。会話は、ビジネスとエンドユーザーの間の24 時間スレッドです。

### 会話タイプの定義

**マーケティング対話:**意識の喚起から販売促進、顧客のターゲット変更まで、幅広い目標を達成できるビジネス主導の会話。たとえば、新製品、サービス、機能のアナウンス、ターゲットを絞ったプロモーション/オファー、カート放棄のリマインダーなどです。

**ユーティリティの会話:**ユーザーのアクションまたはリクエストのフォローアップを可能にするビジネス開始の会話。例としては、オプトイン確認、注文/配送管理(例:配送更新)、アカウント更新、警告(例:支払リマインダー)、またはフィードバック調査が挙げられる。

**認証会話:**ログインプロセスの複数のステップ(アカウントの検証、アカウントのリカバリ、整合性の問題など)で、1 回限りのパスコードでユーザーを認証できるようにします。

{% alert note %}
認証の対話はケースバイケースでのみサポートされ、Braze は特定のSLA を保証できません。また、Braze はPIN 生成をサポートしていません。
{% endalert %}

**サービス会話:**テンプレート化されていないメッセージで応答された、ユーザーが開始した会話。

{% alert note %}
マーケティングまたはユーティリティテンプレートで応答されるユーザ起動の会話は、そのように課金されます。
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
