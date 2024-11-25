---
nav_title: メッセージクレジット - デルタ
permalink: "/message_credits_delta_a3sy/"
hidden: true
noindex: true
hide_toc: true
---

# メッセージクレジット - デルタ (社外秘)

> メッセージクレジットは、Brazeのクロスチャネルのパッケージ構造で、ネイティブSMS、MMS、およびWhatsAppの提供に対応しています。メッセージ・クレジットは、Brazeメッセージング・チャンネルを利用する際に、柔軟で透明性のある体験を提供します。クレジットは、このページの表に示されているチャネルにアクセスできます。

{% alert note %}
異なるチャネルは、報告において異なる測定単位を持つでしょう。<br><br>
<b>WhatsApp:</b>会話<br>
<b>SMS:</b>セグメント<br>
<b>MMS:</b>セグメント<br><br>
つまり、WhatsApp メッセージごとのクレジットは会話開始時に計算され、SMS メッセージとMMS メッセージの両方のクレジットは送信されたセグメントごとに計算されます。
<br><br>
最後に、通信事業者料金は別途請求され (後払い)、このメッセージクレジット SKU の一部とは見なされません。
{% endalert %}

## 定義

列の定義は次のとおりです:

|---------|-------------------------------------------------|
| **チャネルのクレジット比率** | 各チャネルのベースラインクレジット額 |
| **送信先** | Braze プラットフォームから送信されるメッセージの最終送信先の特定の地域、国、またはメッセージの種類 |
| **乗数** | 特定の送信先の価格設定に応じたチャネルのクレジット比率の係数 |
| **1センドあたりのクレジット** | 1通のメッセージを送信するメッセージクレジットの正確な番号<br> (メッセージあたりのクレジット = チャネルのクレジット比率 x 宛先係数） |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


## メッセージクレジットのクレジット比率の表 - デルタ

{% details クリックして展開 %}
<table>
    <colgroup>
        <col span="4" style="background-color:background-color:#FFFFFF;">
        <col style="background-color:#f0f0f5">
    </colgroup>
    <tr>
        <th><b>Channel</b></th>
        <th><b>チャネルのクレジット比率</b></th>
        <th><b>送信先</b></th>
        <th><b>乗数</b></th>
        <th class="credits-column"><b>1センドあたりのクレジット</b></th>
    </tr>
    <tr>
        <td>SMS - 米国 / カナダ</td>
        <td>1</td>
        <td>アメリカ合衆国</td>
        <td>1.00</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>SMS - 米国 / カナダ</td>
        <td>1</td>
        <td>アメリカ合衆国フリーダイヤル</td>
        <td>1.50</td>
        <td>1.50</td>
    </tr>
    <tr>
        <td>SMS - 米国 / カナダ</td>
        <td>1</td>
        <td>カナダ</td>
        <td>1.00</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>SMS - 米国 / カナダ</td>
        <td>1</td>
        <td>カナダのフリーダイヤル</td>
        <td>1.30</td>
        <td>1.30</td>
    </tr>
    <tr>
        <td>MMS - 米国 / カナダ</td>
        <td>3</td>
        <td>アメリカ合衆国</td>
        <td>1.00</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>MMS - 米国 / カナダ</td>
        <td>3</td>
        <td>アメリカ合衆国フリーダイヤル</td>
        <td>2.00</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>MMS - 米国 / カナダ</td>
        <td>3</td>
        <td>カナダロングコード</td>
        <td>1.50</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>MMS - 米国 / カナダ</td>
        <td>3</td>
        <td>カナダショートコード</td>
        <td>4.00</td>
        <td>12.00</td>
    </tr>
    <tr>
        <td>MMS - 米国 / カナダ</td>
        <td>3</td>
        <td>カナダのフリーダイヤル</td>
        <td>1.30</td>
        <td>3.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>アブハジア</td>
        <td>0.62</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>アフガニスタン</td>
        <td>9.47</td>
        <td>94.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>アルバニア</td>
        <td>2.29</td>
        <td>22.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>アルジェリア</td>
        <td>5.23</td>
        <td>52.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>アメリカ領サモア</td>
        <td>4.74</td>
        <td>47.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>アンドラ</td>
        <td>3.32</td>
        <td>33.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>アンゴラ</td>
        <td>2.24</td>
        <td>22.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>アンギラ</td>
        <td>3.33</td>
        <td>33.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>アンティグア・バーブーダ</td>
        <td>2.47</td>
        <td>24.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>アルゼンチン</td>
        <td>1.02</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>アルメニア</td>
        <td>3.49</td>
        <td>34.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>アルバ</td>
        <td>2.61</td>
        <td>26.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>オーストラリア SMS</td>
        <td>0.36</td>
        <td>3.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>オーストラリア MMS</td>
        <td>3.10</td>
        <td>31.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>オーストリア</td>
        <td>1.77</td>
        <td>17.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>アゼルバイジャン</td>
        <td>9.77</td>
        <td>97.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>バハマ</td>
        <td>1.23</td>
        <td>12.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>バーレーン</td>
        <td>0.92</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>バングラデシュ</td>
        <td>5.81</td>
        <td>58.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>バルバドス</td>
        <td>3.09</td>
        <td>30.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ベラルーシ</td>
        <td>6.35</td>
        <td>63.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ベルギー</td>
        <td>2.40</td>
        <td>24.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ベリーズ</td>
        <td>6.90</td>
        <td>69.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ベナン</td>
        <td>3.64</td>
        <td>36.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>バミューダ</td>
        <td>2.99</td>
        <td>29.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ブータン</td>
        <td>10.10</td>
        <td>101.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ボリビア</td>
        <td>3.66</td>
        <td>36.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ボスニア・ヘルツェゴビナ</td>
        <td>2.12</td>
        <td>21.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ボツワナ</td>
        <td>2.52</td>
        <td>25.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ブラジル</td>
        <td>0.25</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ブルネイ</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ブルガリア</td>
        <td>2.70</td>
        <td>27.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ブルキナファソ</td>
        <td>3.35</td>
        <td>33.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ブルンジ</td>
        <td>9.47</td>
        <td>94.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>カンボジア</td>
        <td>4.30</td>
        <td>43.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>カメルーン</td>
        <td>3.49</td>
        <td>34.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>カーボベルデ</td>
        <td>3.66</td>
        <td>36.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>カリブ海オランダ</td>
        <td>2.17</td>
        <td>21.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ケイマン諸島</td>
        <td>3.37</td>
        <td>33.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>中央アフリカ共和国</td>
        <td>3.07</td>
        <td>30.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>チャド</td>
        <td>7.30</td>
        <td>73.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>チリ</td>
        <td>1.64</td>
        <td>16.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>中国</td>
        <td>0.64</td>
        <td>6.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>コロンビア</td>
        <td>0.02</td>
        <td>0.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>コモロ</td>
        <td>6.19</td>
        <td>61.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>コンゴ</td>
        <td>5.04</td>
        <td>50.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>クック諸島</td>
        <td>3.52</td>
        <td>35.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>コスタリカ</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>クロアチア</td>
        <td>2.31</td>
        <td>23.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>キューバ</td>
        <td>2.12</td>
        <td>21.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>キュラソー</td>
        <td>0.99</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>キプロス</td>
        <td>2.18</td>
        <td>21.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>チェコ共和国</td>
        <td>1.01</td>
        <td>10.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>デンマーク</td>
        <td>1.01</td>
        <td>10.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ジブチ</td>
        <td>4.09</td>
        <td>40.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ドミニカ</td>
        <td>3.79</td>
        <td>37.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ドミニカ共和国</td>
        <td>1.29</td>
        <td>12.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>コンゴ民主共和国</td>
        <td>5.77</td>
        <td>57.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>エクアドル</td>
        <td>2.76</td>
        <td>27.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>エジプト</td>
        <td>2.43</td>
        <td>24.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>エルサルバドル</td>
        <td>2.45</td>
        <td>24.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>赤道ギニア</td>
        <td>4.36</td>
        <td>43.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>エリトリア</td>
        <td>2.48</td>
        <td>24.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>エストニア</td>
        <td>2.41</td>
        <td>24.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>エスワティニ</td>
        <td>0.58</td>
        <td>5.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>エチオピア</td>
        <td>8.63</td>
        <td>86.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>フォークランド諸島</td>
        <td>3.43</td>
        <td>34.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>フェロー諸島</td>
        <td>1.70</td>
        <td>17.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>フィジー</td>
        <td>4.16</td>
        <td>41.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>フィンランド</td>
        <td>1.46</td>
        <td>14.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>フランス</td>
        <td>0.98</td>
        <td>9.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>フランス領ギアナ</td>
        <td>4.64</td>
        <td>46.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>フランス領ポリネシア</td>
        <td>4.53</td>
        <td>45.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ガボン</td>
        <td>6.64</td>
        <td>66.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ガンビア</td>
        <td>4.18</td>
        <td>41.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ジョージア</td>
        <td>2.63</td>
        <td>26.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ドイツ</td>
        <td>1.88</td>
        <td>18.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ガーナ</td>
        <td>2.26</td>
        <td>22.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ジブラルタル</td>
        <td>2.75</td>
        <td>27.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ギリシャ</td>
        <td>0.99</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>グリーンランド</td>
        <td>1.03</td>
        <td>10.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>グレナダ</td>
        <td>4.09</td>
        <td>40.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>グアドループ</td>
        <td>3.40</td>
        <td>34.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>グアム</td>
        <td>1.73</td>
        <td>17.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>グアテマラ</td>
        <td>3.20</td>
        <td>32.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ガーンジー</td>
        <td>0.87</td>
        <td>8.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ギニア</td>
        <td>3.82</td>
        <td>38.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ギニアビサウ</td>
        <td>3.97</td>
        <td>39.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ガイアナ</td>
        <td>4.50</td>
        <td>45.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ハイチ</td>
        <td>5.94</td>
        <td>59.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ホンジュラス</td>
        <td>2.13</td>
        <td>21.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>香港</td>
        <td>1.35</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ハンガリー</td>
        <td>1.91</td>
        <td>19.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>アイスランド</td>
        <td>1.75</td>
        <td>17.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>インド</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>インドネシア</td>
        <td>6.63</td>
        <td>66.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>イラン</td>
        <td>6.25</td>
        <td>62.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>イラク</td>
        <td>4.79</td>
        <td>47.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>アイルランド</td>
        <td>1.31</td>
        <td>13.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>マン島</td>
        <td>0.81</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>イスラエル</td>
        <td>3.74</td>
        <td>37.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>イタリア</td>
        <td>0.78</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>コートジボワール</td>
        <td>2.48</td>
        <td>24.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ジャマイカ</td>
        <td>3.05</td>
        <td>30.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>日本</td>
        <td>1.02</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ジャージー</td>
        <td>0.70</td>
        <td>7.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ジョーダン</td>
        <td>5.56</td>
        <td>55.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>カザフスタン</td>
        <td>5.52</td>
        <td>55.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ケニア</td>
        <td>2.62</td>
        <td>26.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>キリバス</td>
        <td>3.67</td>
        <td>36.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>大韓民国</td>
        <td>0.69</td>
        <td>6.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>コソボ</td>
        <td>0.97</td>
        <td>9.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>クウェート</td>
        <td>3.34</td>
        <td>33.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>キルギス</td>
        <td>6.12</td>
        <td>61.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ラオス人民民主共和国</td>
        <td>1.54</td>
        <td>15.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ラトビア</td>
        <td>1.80</td>
        <td>18.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>レバノン</td>
        <td>3.07</td>
        <td>30.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>レソト</td>
        <td>5.14</td>
        <td>51.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>リベリア</td>
        <td>3.47</td>
        <td>34.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>リビア</td>
        <td>8.17</td>
        <td>81.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>リヒテンシュタイン</td>
        <td>0.84</td>
        <td>8.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>リトアニア</td>
        <td>1.37</td>
        <td>13.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ルクセンブルク</td>
        <td>1.86</td>
        <td>18.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>マカオ</td>
        <td>1.49</td>
        <td>14.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>マケドニア</td>
        <td>1.88</td>
        <td>18.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>マダガスカル</td>
        <td>9.40</td>
        <td>94.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>マラウイ</td>
        <td>5.72</td>
        <td>57.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>マレーシア</td>
        <td>1.47</td>
        <td>14.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>モルディブ</td>
        <td>1.80</td>
        <td>18.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>マリ</td>
        <td>3.97</td>
        <td>39.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>マルタ</td>
        <td>1.64</td>
        <td>16.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>マーシャル諸島</td>
        <td>4.00</td>
        <td>40.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>マルティニーク</td>
        <td>3.33</td>
        <td>33.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>モーリタニア</td>
        <td>6.51</td>
        <td>65.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>モーリシャス</td>
        <td>4.02</td>
        <td>40.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>マヨット</td>
        <td>2.33</td>
        <td>23.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>メキシコ</td>
        <td>0.27</td>
        <td>2.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ミクロネシア</td>
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>モルドバ</td>
        <td>1.59</td>
        <td>15.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>モナコ</td>
        <td>4.68</td>
        <td>46.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>モンゴル</td>
        <td>7.03</td>
        <td>70.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>モンテネグロ</td>
        <td>2.87</td>
        <td>28.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>モンセラット</td>
        <td>2.77</td>
        <td>27.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>モロッコ</td>
        <td>2.64</td>
        <td>26.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>モザンビーク</td>
        <td>2.76</td>
        <td>27.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ミャンマー</td>
        <td>5.84</td>
        <td>58.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ナミビア</td>
        <td>1.58</td>
        <td>15.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ナウル</td>
        <td>1.12</td>
        <td>11.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ネパール</td>
        <td>3.82</td>
        <td>38.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>オランダ</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ニューカレドニア</td>
        <td>4.44</td>
        <td>44.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ニュージーランド</td>
        <td>1.92</td>
        <td>19.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ニカラグア</td>
        <td>1.95</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ニジェール</td>
        <td>7.49</td>
        <td>74.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ナイジェリア</td>
        <td>5.01</td>
        <td>50.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ニウエ</td>
        <td>4.86</td>
        <td>48.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ノーフォーク島</td>
        <td>0.71</td>
        <td>7.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>北マケドニア</td>
        <td>0.34</td>
        <td>3.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>北キプロス</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ノルウェー</td>
        <td>1.05</td>
        <td>10.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>オマーン</td>
        <td>3.60</td>
        <td>36.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>パキスタン</td>
        <td>7.46</td>
        <td>74.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>パラオ</td>
        <td>2.52</td>
        <td>25.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>パレスチナ領土</td>
        <td>7.68</td>
        <td>76.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>パナマ</td>
        <td>2.23</td>
        <td>22.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>パプアニューギニア</td>
        <td>19.01</td>
        <td>190.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>パラグアイ</td>
        <td>1.84</td>
        <td>18.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ペルー</td>
        <td>0.81</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>フィリピン</td>
        <td>0.28</td>
        <td>2.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ポーランド</td>
        <td>0.52</td>
        <td>5.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ポルトガル</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>プエルトリコ</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>カタール</td>
        <td>0.52</td>
        <td>5.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>レユニオン/マヨット</td>
        <td>4.82</td>
        <td>48.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ルーマニア</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ロシア</td>
        <td>9.54</td>
        <td>95.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ルワンダ</td>
        <td>4.66</td>
        <td>46.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>セントクリストファー・ネイビス</td>
        <td>0.92</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>セントルシア</td>
        <td>1.07</td>
        <td>10.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>サンピエール島・ミクロン島</td>
        <td>2.31</td>
        <td>23.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>セントビンセントおよびグレナディーン諸島</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>サモア</td>
        <td>4.68</td>
        <td>46.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>サンマリノ</td>
        <td>2.76</td>
        <td>27.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>サントメ・プリンシペ</td>
        <td>3.29</td>
        <td>32.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>サウジアラビア</td>
        <td>1.91</td>
        <td>19.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>セネガル</td>
        <td>5.15</td>
        <td>51.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>セルビア</td>
        <td>6.09</td>
        <td>60.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>セーシェル</td>
        <td>0.94</td>
        <td>9.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>シエラレオネ</td>
        <td>4.73</td>
        <td>47.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>シンガポール</td>
        <td>0.70</td>
        <td>7.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>シント・マールテン</td>
        <td>0.16</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>スロバキア</td>
        <td>2.23</td>
        <td>22.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>スロベニア</td>
        <td>3.76</td>
        <td>37.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ソロモン諸島</td>
        <td>2.09</td>
        <td>20.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ソマリア</td>
        <td>4.74</td>
        <td>47.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>南アフリカ</td>
        <td>0.32</td>
        <td>3.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>南オセチア</td>
        <td>2.05</td>
        <td>20.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>南スーダン</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>スペイン</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>スリランカ</td>
        <td>5.60</td>
        <td>56.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>スーダン</td>
        <td>4.15</td>
        <td>41.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>スリナム</td>
        <td>3.28</td>
        <td>32.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>スワジランド</td>
        <td>2.32</td>
        <td>23.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>スウェーデン</td>
        <td>0.86</td>
        <td>8.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>スイス</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>シリア</td>
        <td>7.86</td>
        <td>78.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>台湾</td>
        <td>0.84</td>
        <td>8.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>タジキスタン</td>
        <td>11.35</td>
        <td>113.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>タンザニア</td>
        <td>5.38</td>
        <td>53.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>タイ</td>
        <td>0.36</td>
        <td>3.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>東ティモール</td>
        <td>2.86</td>
        <td>28.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>トーゴ</td>
        <td>3.84</td>
        <td>38.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>トンガ</td>
        <td>3.14</td>
        <td>31.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>トリニダード・トバゴ</td>
        <td>3.02</td>
        <td>30.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>チュニジア</td>
        <td>7.06</td>
        <td>70.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>トルコ</td>
        <td>0.77</td>
        <td>7.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>トルクメニスタン</td>
        <td>5.04</td>
        <td>50.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>タークス・カイコス諸島</td>
        <td>3.38</td>
        <td>33.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ツバル</td>
        <td>3.36</td>
        <td>33.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ウガンダ</td>
        <td>4.05</td>
        <td>40.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ウクライナ</td>
        <td>2.86</td>
        <td>28.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>アラブ首長国連邦</td>
        <td>1.24</td>
        <td>12.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>イギリス</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>不明</td>
        <td>3.92</td>
        <td>39.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ウルグアイ</td>
        <td>2.15</td>
        <td>21.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ウズベキスタン</td>
        <td>6.88</td>
        <td>68.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>バヌアツ</td>
        <td>4.18</td>
        <td>41.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ベネズエラ</td>
        <td>2.15</td>
        <td>21.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ベトナム</td>
        <td>3.05</td>
        <td>30.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>イギリス領バージン諸島</td>
        <td>4.73</td>
        <td>47.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>バージン諸島、U.S。</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ウォリス・フツナ</td>
        <td>2.77</td>
        <td>27.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>イエメン</td>
        <td>6.03</td>
        <td>60.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ザンビア</td>
        <td>6.76</td>
        <td>67.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - グローバル</td>
        <td>10</td>
        <td>ジンバブエ</td>
        <td>3.55</td>
        <td>35.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>アルゼンチン 認証</td>
        <td>0.95</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>アルゼンチン マーケティング</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>アルゼンチン: ユーティリティ</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ブラジル: 認証</td>
        <td>0.85</td>
        <td>8.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ブラジル マーケティング</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ブラジル: ユーティリティ</td>
        <td>0.21</td>
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
        <td>チリ マーケティング</td>
        <td>2.35</td>
        <td>23.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>チリ: ユーティリティ</td>
        <td>0.53</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>コロンビア 認証</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>コロンビア マーケティング</td>
        <td>0.35</td>
        <td>3.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>コロンビア: ユーティリティ</td>
        <td>0.01</td>
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
        <td>エジプト マーケティング</td>
        <td>2.85</td>
        <td>28.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>エジプト: ユーティリティ</td>
        <td>0.14</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>フランス: 認証</td>
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>フランス マーケティング</td>
        <td>3.80</td>
        <td>38.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>フランス: ユーティリティ</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ドイツ: 認証</td>
        <td>2.05</td>
        <td>20.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ドイツ マーケティング</td>
        <td>3.60</td>
        <td>36.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ドイツ: ユーティリティ</td>
        <td>1.46</td>
        <td>14.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>インド: 認証</td>
        <td>0.04</td>
        <td>0.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>インド認証 - 国際</td>
        <td>0.74</td>
        <td>7.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>インド マーケティング</td>
        <td>0.25</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>インド: ユーティリティ</td>
        <td>0.04</td>
        <td>0.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>インドネシア 認証</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>インドネシア 認証 - 国際</td>
        <td>3.61</td>
        <td>36.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>インドネシア マーケティング</td>
        <td>1.10</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>インドネシア: ユーティリティ</td>
        <td>0.55</td>
        <td>5.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>イスラエル 認証</td>
        <td>0.45</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>イスラエル マーケティング</td>
        <td>0.95</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>イスラエル: ユーティリティ</td>
        <td>0.14</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>イタリア 認証</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>イタリア マーケティング</td>
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>イタリア: ユーティリティ</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>マレーシア: 認証</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>マレーシア マーケティング</td>
        <td>2.30</td>
        <td>23.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>マレーシア: ユーティリティ</td>
        <td>0.37</td>
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
        <td>メキシコ マーケティング</td>
        <td>1.15</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>メキシコ: ユーティリティ</td>
        <td>0.27</td>
        <td>2.70</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>オランダ: 認証</td>
        <td>1.90</td>
        <td>19.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>オランダ: マーケティング</td>
        <td>4.25</td>
        <td>42.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>オランダ: ユーティリティ</td>
        <td>1.33</td>
        <td>13.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ナイジェリア 認証</td>
        <td>0.75</td>
        <td>7.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ナイジェリア マーケティング</td>
        <td>1.35</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ナイジェリア: ユーティリティ</td>
        <td>0.18</td>
        <td>1.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>北アメリカ 認証</td>
        <td>0.35</td>
        <td>3.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>北アメリカマーケティング</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>北米: ユーティリティ</td>
        <td>0.11</td>
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
        <td>その他のマーケティング</td>
        <td>1.60</td>
        <td>16.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>その他: ユーティリティ</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>パキスタン 認証</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>パキスタン マーケティング</td>
        <td>1.25</td>
        <td>12.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>パキスタン: ユーティリティ</td>
        <td>0.14</td>
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
        <td>ペルー マーケティング</td>
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ペルー: ユーティリティ</td>
        <td>0.53</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>アフリカのその他諸国: 認証</td>
        <td>0.40</td>
        <td>4.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>アフリカのその他諸国: マーケティング</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>アフリカのその他諸国: ユーティリティ</td>
        <td>0.16</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>REST of Asia Pacific 認証</td>
        <td>1.15</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>アジア太平洋地域のその他諸国: マーケティング</td>
        <td>1.95</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>アジア太平洋地域のその他諸国: ユーティリティ</td>
        <td>0.42</td>
        <td>4.20</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>中東欧地域のその他諸国: 認証</td>
        <td>1.50</td>
        <td>15.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>中東欧地域ののその他諸国: マーケティング</td>
        <td>2.30</td>
        <td>23.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>中東欧地域のその他諸国: ユーティリティ</td>
        <td>0.94</td>
        <td>9.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ラテンアメリカ地域のその他諸国: 認証</td>
        <td>1.20</td>
        <td>12.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ラテンアメリカの残りのマーケティング</td>
        <td>1.95</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ラテンアメリカ地域のその他諸国: ユーティリティ</td>
        <td>0.30</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>REST of Middle East 認証</td>
        <td>0.45</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>中東地域のその他の諸国: マーケティング</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>中東地域のその他諸国: ユーティリティ</td>
        <td>0.42</td>
        <td>4.20</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>REST of Western Europe 認証</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>西欧地域のその他諸国: マーケティング</td>
        <td>1.55</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>西欧地域のその他諸国: ユーティリティ</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ロシア 認証</td>
        <td>1.15</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ロシア マーケティング</td>
        <td>2.15</td>
        <td>21.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>ロシア: ユーティリティ</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>サウジアラビア 認証</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>サウジアラビア マーケティング</td>
        <td>1.10</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>サウジアラビア: ユーティリティ</td>
        <td>0.31</td>
        <td>3.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>南アフリカ 認証</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>南アフリカ マーケティング</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>南アフリカ: ユーティリティ</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>スペイン 認証</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>スペイン マーケティング</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>スペイン: ユーティリティ</td>
        <td>0.53</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>トルコ 認証</td>
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
        <td>トルコ: ユーティリティ</td>
        <td>0.14</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>アラブ首長国連邦 認証</td>
        <td>0.45</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>アラブ首長国連邦 マーケティング</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>アラブ首長国連邦: ユーティリティ</td>
        <td>0.42</td>
        <td>4.20</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>イギリス 認証</td>
        <td>0.95</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>イギリス マーケティング</td>
        <td>1.40</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>イギリスUtility</td>
        <td>0.58</td>
        <td>5.80</td>
    </tr>
    <tr>
        <td>LINE</td>
        <td>1</td>
        <td>全地域</td>
        <td>0.15</td>
        <td>0.15</td>
    </tr>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% enddetails %}

------

## SMS/MMSチャネルの詳細

### SMSセグメント

SMSメッセージセグメントは、SMS業界がメッセージをカウントする方法です。メッセージセグメントとは、定義された文字数（GSM-7エンコーディングでは160文字、UCS-2エンコーディングでは67文字）までのグループであり、1回のSMSディスパッチで送信される。GSM-7エンコーディングを使用して161文字のSMSを送信すると、送信されたメッセージセグメントが2つあることがわかります。複数のメッセージセグメントを送信すると追加料金が発生します。

### MMSセグメント

MMSの場合、メッセージの制限は5 MBです（これにはマルチメディアアセットとメッセージ本文のサイズが含まれます）。安全のために、Brazeはメッセージ本文を含めたマルチメディアアセットのサイズを600KBを超えないようにすることを推奨しています。

## WhatsAppチャネルの詳細

WhatsAppは双方向メッセージングに焦点を当てたチャネルであり、したがって会話（個々のメッセージの数ではなく）に基づいています。会話は、ビジネスとエンドユーザーの間の24時間のスレッドです。

### 会話タイプの定義

**マーケティングの会話:**ビジネスが開始した会話は、認知度の向上から販売促進、リターゲティングによる顧客の再ターゲットまで、幅広い目標を達成することができます。例としては、新製品、サービス、または機能の発表、ターゲットを絞ったプロモーション/オファー、そしてカート放棄のリマインダーが含まれます。

**ユーティリティの会話:**ビジネスが開始した会話により、ユーザーのアクションやリクエストをフォローアップすることができます。例としては、オプトインの確認、注文/配送管理 (e.g、配送の最新情報)、アカウントのアップデートやアラート (e.g、支払いリマインダーなど)、フィードバックアンケートなどがあります。

**認証の会話:**ワンタイムパスコードでユーザーを認証できます。ログインプロセスの複数ステップ (e.g、アカウント認証、アカウントリカバリー、整合性チェックなど) で使用されます。

{% alert note %}
認証の会話はケースバイケースでのみサポートされ、Braze は特定の SLA を保証できません。さらに、BrazeはPIN生成をサポートしていません。
{% endalert %}

**サービスの会話:**ユーザーが開始した会話に対して、テンプレート化されていないメッセージで応答する。

{% alert note %}
2024年11月1日現在、サービスタイプの会話は無料であり、購入したクレジット割当からは控除されません。
{% endalert %}

## 請求地域の分類

#### 北アメリカ

アメリカ合衆国、カナダ

#### 残りのアフリカ

アルジェリア、アンゴラ、ベナン、ボツワナ、ブルキナファソ、ブルンジ、カメルーン、チャド、コンゴ、エリトリア、エチオピア、ガボン、ガンビア、ガーナ、ギニアビサウ、コートジボワール、ケニア、レソト、リベリア、リビア、
マダガスカル、マラウイ、マリ、モーリタニア、モロッコ、モザンビーク、ナミビア、ニジェール、ルワンダ、セネガル、シエラレオネ、ソマリア、南スーダン、スーダン、スワジランド、タンザニア、トーゴ、チュニジア、ウガンダ、ザンビア

#### アジア太平洋地域の残りの部分

アフガニスタン、オーストラリア、バングラデシュ、カンボジア、中国、香港、日本、ラオス、モンゴル、ネパール、ニュージーランド、パプアニューギニア、フィリピン、シンガポール、スリランカ、台湾、タジキスタン、タイ、
トルクメニスタン、ウズベキスタン、ベトナム

#### 中東欧地域のその他諸国

アルバニア、アルメニア、アゼルバイジャン、ベラルーシ、ブルガリア、クロアチア、チェコ共和国、ジョージア、ギリシャ、ハンガリー、ラトビア、リトアニア、マケドニア、モルドバ、ポーランド、ルーマニア、セルビア、スロバキア、スロベニア、ウクライナ

#### ラテンアメリカの残りの部分

ボリビア、コスタリカ、ドミニカ共和国、エクアドル、エルサルバドル、
グアテマラ、ハイチ、ホンジュラス、ジャマイカ、ニカラグア、パナマ、パラグアイ、プエルトリコ、ウルグアイ、ベネズエラ

#### 中東の残りの部分

バーレーン、イラク、ヨルダン、クウェート、レバノン、オマーン、カタール、イエメン

#### 西欧地域のその他諸国

オーストリア、ベルギー、デンマーク、フィンランド、アイルランド、ノルウェー、ポルトガル、スウェーデン、スイス
