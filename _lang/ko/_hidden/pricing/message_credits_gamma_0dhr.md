---
nav_title: 메시지 크레딧 - 감마
permalink: "/message_credits_gamma_0dhr/"
hidden: true
noindex: true
hide_toc: true
---

# 메시지 크레딧 - 감마(기밀)

> 메시지 크레딧은 Braze의 크로스채널 패키징 구조로, 자사 네이티브 SMS, MMS, 및 WhatsApp 제공을 위한 것입니다. 메시지 크레딧은 Braze 메시징 채널을 활용할 때 유연하고 투명한 경험을 제공합니다. 크레딧을 사용하면 이 페이지의 표에 나와 있는 모든 채널에 액세스할 수 있습니다.

{% alert note %}
채널마다 보고에서 다른 측정 단위를 가질 것입니다.<br><br>
<b>WhatsApp:</b> 대화<br>
<b>SMS:</b> 세그먼트<br>
<b>MMS:</b> 세그먼트<br><br>
즉, WhatsApp 메시지당 크레딧은 대화 시작 시 계산되며, SMS 및 MMS 메시지 모두에 대한 크레딧은 전송된 세그먼트에 대해 계산됩니다.
<br><br>
마지막으로, 통신사 수수료는 별도로 청구되며(연체 시) 이 메시지 크레딧 SKU의 일부로 간주되지 않습니다.
{% endalert %}

## 정의

열 정의는 다음과 같습니다:

|---------|-------------------------------------------------|
| **채널 크레딧 비율** | 각 채널에 대한 기준 신용 금액 |
| **대상** | 특정 최종 지역, 국가 또는 Braze 플랫폼을 통해 전송되는 메시지 유형 |
| **승수** | 특정 대상의 가격에 따라 채널 크레딧 비율 대비 계수기 |
| **1회 전송당 크레딧** | 하나의 메시지를 전송할 수 있는 정확한 메시지 크레딧 수<br> (메시지당 크레딧 = 채널 크레딧 비율 x 대상 승수) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


## 메시지 크레딧에 대한 크레딧 비율 테이블 - 감마

{% details 펼치려면 클릭 %}
<table>
    <colgroup>
        <col span="4" style="background-color:background-color:#FFFFFF;">
        <col style="background-color:#f0f0f5">
    </colgroup>
    <tr>
        <th><b>채널</b></th>
        <th><b>채널 크레딧 비율</b></th>
        <th><b>대상</b></th>
        <th><b>승수</b></th>
        <th class="credits-column"><b>1회 전송당 크레딧</b></th>
    </tr>
    <tbody><tr>
        <td>SMS - 미국 / 캐나다</td>
        <td>0.4</td>
        <td>미국</td>
        <td>1.00</td>
        <td>0.40</td>
    </tr>
    <tr>
        <td>SMS - 미국 / 캐나다</td>
        <td>0.4</td>
        <td>미국 무료 전화</td>
        <td>1.50</td>
        <td>0.60</td>
    </tr>
    <tr>
        <td>SMS - 미국 / 캐나다</td>
        <td>0.4</td>
        <td>캐나다</td>
        <td>1.00</td>
        <td>0.40</td>
    </tr>
    <tr>
        <td>SMS - 미국 / 캐나다</td>
        <td>0.4</td>
        <td>캐나다 무료 전화</td>
        <td>1.30</td>
        <td>0.52</td>
    </tr>
    <tr>
        <td>MMS - 미국 / 캐나다</td>
        <td>1.2</td>
        <td>미국</td>
        <td>1.00</td>
        <td>1.20</td>
    </tr>
    <tr>
        <td>MMS - 미국 / 캐나다</td>
        <td>1.2</td>
        <td>미국 무료 전화</td>
        <td>2.00</td>
        <td>2.40</td>
    </tr>
    <tr>
        <td>MMS - 미국 / 캐나다</td>
        <td>1.2</td>
        <td>캐나다 긴 코드</td>
        <td>1.50</td>
        <td>1.80</td>
    </tr>
    <tr>
        <td>MMS - 미국 / 캐나다</td>
        <td>1.2</td>
        <td>캐나다 짧은 코드</td>
        <td>4.00</td>
        <td>4.80</td>
    </tr>
    <tr>
        <td>MMS - 미국 / 캐나다</td>
        <td>1.2</td>
        <td>캐나다 무료 전화</td>
        <td>1.30</td>
        <td>1.56</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>압하지야</td>
        <td>0.62</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>아프가니스탄</td>
        <td>9.47</td>
        <td>94.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>알바니아</td>
        <td>2.29</td>
        <td>22.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>알제리</td>
        <td>5.23</td>
        <td>52.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>미국령 사모아</td>
        <td>4.74</td>
        <td>47.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>안도라</td>
        <td>3.32</td>
        <td>33.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>앙골라</td>
        <td>2.24</td>
        <td>22.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>앵귈라</td>
        <td>3.33</td>
        <td>33.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>앤티가 바부다</td>
        <td>2.47</td>
        <td>24.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>아르헨티나</td>
        <td>1.02</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>아르메니아</td>
        <td>3.49</td>
        <td>34.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>아루바</td>
        <td>2.61</td>
        <td>26.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>호주 SMS</td>
        <td>0.36</td>
        <td>3.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>호주 MMS</td>
        <td>3.10</td>
        <td>31.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>오스트리아</td>
        <td>1.77</td>
        <td>17.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>아제르바이잔</td>
        <td>9.77</td>
        <td>97.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>바하마</td>
        <td>1.23</td>
        <td>12.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>바레인</td>
        <td>0.92</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>방글라데시</td>
        <td>5.81</td>
        <td>58.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>바베이도스</td>
        <td>3.09</td>
        <td>30.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>벨라루스</td>
        <td>6.35</td>
        <td>63.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>벨기에</td>
        <td>2.40</td>
        <td>24.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>벨리즈</td>
        <td>6.90</td>
        <td>69.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>베냉</td>
        <td>3.64</td>
        <td>36.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>버뮤다</td>
        <td>2.99</td>
        <td>29.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>부탄</td>
        <td>10.10</td>
        <td>101.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>볼리비아</td>
        <td>3.66</td>
        <td>36.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>보스니아 헤르체고비나</td>
        <td>2.12</td>
        <td>21.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>보츠와나</td>
        <td>2.52</td>
        <td>25.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>브라질</td>
        <td>0.25</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>브루나이</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>불가리아</td>
        <td>2.70</td>
        <td>27.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>부키나 파소</td>
        <td>3.35</td>
        <td>33.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>부룬디</td>
        <td>9.47</td>
        <td>94.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>캄보디아</td>
        <td>4.30</td>
        <td>43.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>카메룬</td>
        <td>3.49</td>
        <td>34.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>카보베르데</td>
        <td>3.66</td>
        <td>36.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>카리브 네덜란드</td>
        <td>2.17</td>
        <td>21.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>케이맨 제도</td>
        <td>3.37</td>
        <td>33.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>중앙아프리카공화국</td>
        <td>3.07</td>
        <td>30.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>차드</td>
        <td>7.30</td>
        <td>73.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>칠레</td>
        <td>1.64</td>
        <td>16.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>중국</td>
        <td>0.64</td>
        <td>6.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>콜롬비아</td>
        <td>0.02</td>
        <td>0.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>코모로</td>
        <td>6.19</td>
        <td>61.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>콩고</td>
        <td>5.04</td>
        <td>50.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>쿡 제도</td>
        <td>3.52</td>
        <td>35.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>코스타리카</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>크로아티아</td>
        <td>2.31</td>
        <td>23.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>쿠바</td>
        <td>2.12</td>
        <td>21.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>퀴라소</td>
        <td>0.99</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>키프로스</td>
        <td>2.18</td>
        <td>21.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>체코공화국</td>
        <td>1.01</td>
        <td>10.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>덴마크</td>
        <td>1.01</td>
        <td>10.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>지부티</td>
        <td>4.09</td>
        <td>40.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>도미니카</td>
        <td>3.79</td>
        <td>37.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>도미니카공화국</td>
        <td>1.29</td>
        <td>12.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>콩고 민주 공화국</td>
        <td>5.77</td>
        <td>57.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>에콰도르</td>
        <td>2.76</td>
        <td>27.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>이집트</td>
        <td>2.43</td>
        <td>24.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>엘살바도르</td>
        <td>2.45</td>
        <td>24.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>적도 기니</td>
        <td>4.36</td>
        <td>43.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>에리트레아</td>
        <td>2.48</td>
        <td>24.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>에스토니아</td>
        <td>2.41</td>
        <td>24.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>에스와티니</td>
        <td>0.58</td>
        <td>5.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>에티오피아</td>
        <td>8.63</td>
        <td>86.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>포클랜드 제도</td>
        <td>3.43</td>
        <td>34.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>페로 제도</td>
        <td>1.70</td>
        <td>17.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>피지</td>
        <td>4.16</td>
        <td>41.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>핀란드</td>
        <td>1.46</td>
        <td>14.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>프랑스</td>
        <td>0.98</td>
        <td>9.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>프랑스령 기아나</td>
        <td>4.64</td>
        <td>46.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>프랑스령 폴리네시아</td>
        <td>4.53</td>
        <td>45.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>가봉</td>
        <td>6.64</td>
        <td>66.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>감비아</td>
        <td>4.18</td>
        <td>41.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>조지아</td>
        <td>2.63</td>
        <td>26.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>독일</td>
        <td>1.88</td>
        <td>18.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>가나</td>
        <td>2.26</td>
        <td>22.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>지브롤터</td>
        <td>2.75</td>
        <td>27.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>그리스</td>
        <td>0.99</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>그린란드</td>
        <td>1.03</td>
        <td>10.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>그레나다</td>
        <td>4.09</td>
        <td>40.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>과들루프</td>
        <td>3.40</td>
        <td>34.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>괌</td>
        <td>1.73</td>
        <td>17.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>과테말라</td>
        <td>3.20</td>
        <td>32.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>건지</td>
        <td>0.87</td>
        <td>8.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>기니</td>
        <td>3.82</td>
        <td>38.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>기니비사우</td>
        <td>3.97</td>
        <td>39.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>가이아나</td>
        <td>4.50</td>
        <td>45.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>아이티</td>
        <td>5.94</td>
        <td>59.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>온두라스</td>
        <td>2.13</td>
        <td>21.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>홍콩</td>
        <td>1.35</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>헝가리</td>
        <td>1.91</td>
        <td>19.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>아이슬란드</td>
        <td>1.75</td>
        <td>17.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>인도</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>인도네시아</td>
        <td>6.63</td>
        <td>66.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>이란</td>
        <td>6.25</td>
        <td>62.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>이라크</td>
        <td>4.79</td>
        <td>47.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>아일랜드</td>
        <td>1.31</td>
        <td>13.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>맨 섬</td>
        <td>0.81</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>이스라엘</td>
        <td>3.74</td>
        <td>37.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>이탈리아</td>
        <td>0.78</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>코트디부아르</td>
        <td>2.48</td>
        <td>24.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>자메이카</td>
        <td>3.05</td>
        <td>30.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>일본</td>
        <td>1.02</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>저지</td>
        <td>0.70</td>
        <td>7.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>요르단</td>
        <td>5.56</td>
        <td>55.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>카자흐스탄</td>
        <td>5.52</td>
        <td>55.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>케냐</td>
        <td>2.62</td>
        <td>26.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>키리바시</td>
        <td>3.67</td>
        <td>36.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>대한민국</td>
        <td>0.69</td>
        <td>6.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>코소보</td>
        <td>0.97</td>
        <td>9.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>쿠웨이트</td>
        <td>3.34</td>
        <td>33.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>키르기스스탄</td>
        <td>6.12</td>
        <td>61.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>라오스 인민 민주 공화국</td>
        <td>1.54</td>
        <td>15.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>라트비아</td>
        <td>1.80</td>
        <td>18.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>레바논</td>
        <td>3.07</td>
        <td>30.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>레소토</td>
        <td>5.14</td>
        <td>51.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>라이베리아</td>
        <td>3.47</td>
        <td>34.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>리비아</td>
        <td>8.17</td>
        <td>81.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>리히텐슈타인</td>
        <td>0.84</td>
        <td>8.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>리투아니아</td>
        <td>1.37</td>
        <td>13.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>룩셈부르크</td>
        <td>1.86</td>
        <td>18.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>마카오</td>
        <td>1.49</td>
        <td>14.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>마케도니아</td>
        <td>1.88</td>
        <td>18.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>마다가스카르</td>
        <td>9.40</td>
        <td>94.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>말라위</td>
        <td>5.72</td>
        <td>57.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>말레이시아</td>
        <td>1.47</td>
        <td>14.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>몰디브</td>
        <td>1.80</td>
        <td>18.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>말리</td>
        <td>3.97</td>
        <td>39.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>몰타</td>
        <td>1.64</td>
        <td>16.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>마셜 제도</td>
        <td>4.00</td>
        <td>40.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>마르티니크</td>
        <td>3.33</td>
        <td>33.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>모리타니</td>
        <td>6.51</td>
        <td>65.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>모리셔스</td>
        <td>4.02</td>
        <td>40.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>마요트</td>
        <td>2.33</td>
        <td>23.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>멕시코</td>
        <td>0.27</td>
        <td>2.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>미크로네시아</td>
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>몰도바</td>
        <td>1.59</td>
        <td>15.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>모나코</td>
        <td>4.68</td>
        <td>46.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>몽골</td>
        <td>7.03</td>
        <td>70.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>몬테네그로</td>
        <td>2.87</td>
        <td>28.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>몬세라트</td>
        <td>2.77</td>
        <td>27.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>모로코</td>
        <td>2.64</td>
        <td>26.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>모잠비크</td>
        <td>2.76</td>
        <td>27.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>미얀마</td>
        <td>5.84</td>
        <td>58.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>나미비아</td>
        <td>1.58</td>
        <td>15.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>나우루</td>
        <td>1.12</td>
        <td>11.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>네팔</td>
        <td>3.82</td>
        <td>38.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>네덜란드</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>뉴 칼레도니아</td>
        <td>4.44</td>
        <td>44.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>뉴질랜드</td>
        <td>1.92</td>
        <td>19.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>니카라과</td>
        <td>1.95</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>니제르</td>
        <td>7.49</td>
        <td>74.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>나이지리아</td>
        <td>5.01</td>
        <td>50.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>니우에</td>
        <td>4.86</td>
        <td>48.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>노퍽 섬</td>
        <td>0.71</td>
        <td>7.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>북마케도니아</td>
        <td>0.34</td>
        <td>3.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>북키프로스</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>노르웨이</td>
        <td>1.05</td>
        <td>10.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>오만</td>
        <td>3.60</td>
        <td>36.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>파키스탄</td>
        <td>7.46</td>
        <td>74.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>팔라우</td>
        <td>2.52</td>
        <td>25.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>팔레스타인 영토</td>
        <td>7.68</td>
        <td>76.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>파나마</td>
        <td>2.23</td>
        <td>22.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>파푸아뉴기니</td>
        <td>19.01</td>
        <td>190.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>파라과이</td>
        <td>1.84</td>
        <td>18.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>페루</td>
        <td>0.81</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>필리핀</td>
        <td>0.28</td>
        <td>2.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>폴란드</td>
        <td>0.52</td>
        <td>5.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>포르투갈</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>푸에르토리코</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>카타르</td>
        <td>0.52</td>
        <td>5.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>레위니옹/마요트</td>
        <td>4.82</td>
        <td>48.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>루마니아</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>러시아</td>
        <td>9.54</td>
        <td>95.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>르완다</td>
        <td>4.66</td>
        <td>46.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>세인트키츠 네비스</td>
        <td>0.92</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>세인트루시아</td>
        <td>1.07</td>
        <td>10.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>생 피에르 미클롱</td>
        <td>2.31</td>
        <td>23.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>세인트빈센트 그레나딘</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>사모아</td>
        <td>4.68</td>
        <td>46.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>산 마리노</td>
        <td>2.76</td>
        <td>27.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>상투메 프린시페</td>
        <td>3.29</td>
        <td>32.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>사우디아라비아</td>
        <td>1.91</td>
        <td>19.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>세네갈</td>
        <td>5.15</td>
        <td>51.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>세르비아</td>
        <td>6.09</td>
        <td>60.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>세이셸</td>
        <td>0.94</td>
        <td>9.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>시에라리온</td>
        <td>4.73</td>
        <td>47.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>싱가포르</td>
        <td>0.70</td>
        <td>7.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>신트마르턴</td>
        <td>0.16</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>슬로바키아</td>
        <td>2.23</td>
        <td>22.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>슬로베니아</td>
        <td>3.76</td>
        <td>37.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>솔로몬 제도</td>
        <td>2.09</td>
        <td>20.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>소말리아</td>
        <td>4.74</td>
        <td>47.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>남아프리카</td>
        <td>0.32</td>
        <td>3.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>남오세티야</td>
        <td>2.05</td>
        <td>20.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>남수단</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>스페인</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>스리랑카</td>
        <td>5.60</td>
        <td>56.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>수단</td>
        <td>4.15</td>
        <td>41.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>수리남</td>
        <td>3.28</td>
        <td>32.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>스와질란드</td>
        <td>2.32</td>
        <td>23.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>스웨덴</td>
        <td>0.86</td>
        <td>8.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>스위스</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>시리아</td>
        <td>7.86</td>
        <td>78.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>대만</td>
        <td>0.84</td>
        <td>8.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>타지키스탄</td>
        <td>11.35</td>
        <td>113.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>탄자니아</td>
        <td>5.38</td>
        <td>53.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>태국</td>
        <td>0.36</td>
        <td>3.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>동티모르</td>
        <td>2.86</td>
        <td>28.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>토고</td>
        <td>3.84</td>
        <td>38.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>통가</td>
        <td>3.14</td>
        <td>31.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>트리니다드 토바고</td>
        <td>3.02</td>
        <td>30.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>튀니지</td>
        <td>7.06</td>
        <td>70.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>튀르키예</td>
        <td>0.77</td>
        <td>7.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>투르크메니스탄</td>
        <td>5.04</td>
        <td>50.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>터크스 케이커스 제도</td>
        <td>3.38</td>
        <td>33.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>투발루</td>
        <td>3.36</td>
        <td>33.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>우간다</td>
        <td>4.05</td>
        <td>40.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>우크라이나</td>
        <td>2.86</td>
        <td>28.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>아랍에미리트</td>
        <td>1.24</td>
        <td>12.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>영국</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>알 수 없음</td>
        <td>3.92</td>
        <td>39.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>우루과이</td>
        <td>2.15</td>
        <td>21.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>우즈베키스탄</td>
        <td>6.88</td>
        <td>68.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>바누아투</td>
        <td>4.18</td>
        <td>41.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>베네수엘라</td>
        <td>2.15</td>
        <td>21.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>베트남</td>
        <td>3.05</td>
        <td>30.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>버진 아일랜드, 영국령</td>
        <td>4.73</td>
        <td>47.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>버진 아일랜드, U.S.</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>월리스 푸투나</td>
        <td>2.77</td>
        <td>27.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>예멘</td>
        <td>6.03</td>
        <td>60.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>잠비아</td>
        <td>6.76</td>
        <td>67.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - 글로벌</td>
        <td>10</td>
        <td>짐바브웨</td>
        <td>3.55</td>
        <td>35.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>아르헨티나 인증</td>
        <td>0.95</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>아르헨티나 마케팅</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>아르헨티나 유틸리티</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>브라질 인증</td>
        <td>0.85</td>
        <td>8.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>브라질 마케팅</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>브라질 유틸리티</td>
        <td>0.21</td>
        <td>2.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>칠레 인증</td>
        <td>1.40</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>칠레 마케팅</td>
        <td>2.35</td>
        <td>23.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>칠레 유틸리티</td>
        <td>0.53</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>콜롬비아 인증</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>콜롬비아 마케팅</td>
        <td>0.35</td>
        <td>3.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>콜롬비아 유틸리티</td>
        <td>0.01</td>
        <td>0.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>이집트 인증</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>이집트 마케팅</td>
        <td>2.85</td>
        <td>28.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>이집트 유틸리티</td>
        <td>0.14</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>프랑스 인증</td>
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>프랑스 마케팅</td>
        <td>3.80</td>
        <td>38.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>프랑스 유틸리티</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>독일 인증</td>
        <td>2.05</td>
        <td>20.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>독일 마케팅</td>
        <td>3.60</td>
        <td>36.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>독일 유틸리티</td>
        <td>1.46</td>
        <td>14.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>인도 인증</td>
        <td>0.04</td>
        <td>0.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>인도 인증 - 국제</td>
        <td>0.74</td>
        <td>7.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>인도 마케팅</td>
        <td>0.25</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>인도 유틸리티</td>
        <td>0.04</td>
        <td>0.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>인도네시아 인증</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>인도네시아 인증 - 국제</td>
        <td>3.61</td>
        <td>36.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>인도네시아 마케팅</td>
        <td>1.10</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>인도네시아 유틸리티</td>
        <td>0.55</td>
        <td>5.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>이스라엘 인증</td>
        <td>0.45</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>이스라엘 마케팅</td>
        <td>0.95</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>이스라엘 유틸리티</td>
        <td>0.14</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>이탈리아 인증</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>이탈리아 마케팅</td>
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>이탈리아 유틸리티</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>말레이시아 인증</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>말레이시아 마케팅</td>
        <td>2.30</td>
        <td>23.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>말레이시아 유틸리티</td>
        <td>0.37</td>
        <td>3.70</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>멕시코 인증</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>멕시코 마케팅</td>
        <td>1.15</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>멕시코 유틸리티</td>
        <td>0.27</td>
        <td>2.70</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>네덜란드 인증</td>
        <td>1.90</td>
        <td>19.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>네덜란드 마케팅</td>
        <td>4.25</td>
        <td>42.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>네덜란드 유틸리티</td>
        <td>1.33</td>
        <td>13.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>나이지리아 인증</td>
        <td>0.75</td>
        <td>7.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>나이지리아 마케팅</td>
        <td>1.35</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>나이지리아 유틸리티</td>
        <td>0.18</td>
        <td>1.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>북미 인증</td>
        <td>0.35</td>
        <td>3.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>북미 마케팅</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>북아메리카 유틸리티</td>
        <td>0.11</td>
        <td>1.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>기타 인증</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>기타 마케팅</td>
        <td>1.60</td>
        <td>16.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>기타 유틸리티</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>파키스탄 인증</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>파키스탄 마케팅</td>
        <td>1.25</td>
        <td>12.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>파키스탄 유틸리티</td>
        <td>0.14</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>페루 인증</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>페루 마케팅</td>
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>페루 유틸리티</td>
        <td>0.53</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>아프리카 나머지 인증</td>
        <td>0.40</td>
        <td>4.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>REST of Africa 마케팅</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>아프리카 나머지 유틸리티</td>
        <td>0.16</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>기타 아시아 태평양 인증</td>
        <td>1.15</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>기타 아시아 태평양 지역 마케팅</td>
        <td>1.95</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>기타 아시아 태평양 지역 유틸리티</td>
        <td>0.42</td>
        <td>4.20</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>기타 중앙 및 동유럽 인증</td>
        <td>1.50</td>
        <td>15.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>REST of Central &amp; Eastern Europe 마케팅</td>
        <td>2.30</td>
        <td>23.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>기타 중앙 및 동유럽 유틸리티</td>
        <td>0.94</td>
        <td>9.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>라틴 아메리카 나머지 인증</td>
        <td>1.20</td>
        <td>12.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>REST of Latin America 마케팅</td>
        <td>1.95</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>기타 라틴 아메리카 유틸리티</td>
        <td>0.30</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>REST 중동 인증</td>
        <td>0.45</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>기타 중동 마케팅</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>기타 중동 유틸리티</td>
        <td>0.42</td>
        <td>4.20</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>기타 서유럽 인증</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>기타 서유럽 마케팅</td>
        <td>1.55</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>기타 서유럽 유틸리티</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>러시아 인증</td>
        <td>1.15</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>러시아 마케팅</td>
        <td>2.15</td>
        <td>21.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>러시아 유틸리티</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>사우디아라비아 인증</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>사우디아라비아 마케팅</td>
        <td>1.10</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>사우디아라비아 유틸리티</td>
        <td>0.31</td>
        <td>3.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>남아프리카 공화국 인증</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>남아프리카공화국 마케팅</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>남아프리카 유틸리티</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>스페인 인증</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>스페인 마케팅</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>스페인 유틸리티</td>
        <td>0.53</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>터키 인증</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>터키 마케팅</td>
        <td>0.30</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>터키 유틸리티</td>
        <td>0.14</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>아랍에미리트 인증</td>
        <td>0.45</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>아랍에미리트 마케팅</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>아랍에미리트 유틸리티</td>
        <td>0.42</td>
        <td>4.20</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>영국 인증</td>
        <td>0.95</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>영국 마케팅</td>
        <td>1.40</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>영국 유틸리티</td>
        <td>0.58</td>
        <td>5.80</td>
    </tr>
    <tr>
        <td>LINE</td>
        <td>1</td>
        <td>모든 지역</td>
        <td>0.15</td>
        <td>0.15</td>
    </tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% enddetails %}

------

## SMS/MMS 채널 details

### SMS 세그먼트

SMS 메시지 세그먼트는 SMS 업계가 메시지를 세는 방법입니다. 메시지 세그먼트는 단일 SMS 발송으로 전송되는 최대 정의된 문자 수(GSM-7 인코딩의 경우 160자, UCS-2 인코딩의 경우 67자)로 구성된 그룹입니다. GSM-7 인코딩을 사용하여 161자의 SMS를 전송하면 두 (2)개의 메시지 세그먼트가 전송된 것을 볼 수 있습니다. 여러 메시지 세그먼트를 보내면 추가 요금이 부과됩니다.

### MMS 세그먼트

MMS의 경우 메시지 제한은 5MB입니다(멀티미디어 자산 및 메시지 본문 크기 포함). 안전을 위해 Braze는 메시지 본문을 포함하면서 멀티미디어 자산의 용량을 600KB를 넘지 않는 것을 권장합니다.

## WhatsApp 채널 details

WhatsApp은 양방향 메시징에 중점을 둔 채널이며 개별 메시지 수 대신 대화에 중점을 둡니다. 대화는 비즈니스와 최종 사용자 간의 24시간 스레드입니다.

### 대화 유형 정의

**마케팅 Conversations:** 비즈니스 주도 대화는 인지도를 높이는 것부터 판매 촉진 및 리타겟팅 고객에 이르기까지 다양한 목표를 달성할 수 있게 해줍니다. 예를 들어, 신제품, 서비스 또는 기능 발표, 타겟 프로모션/제안 및 장바구니 유기 알림이 포함됩니다.

**유틸리티 대화:** 사용자 행동 또는 요청을 후속 조치할 수 있도록 하는 비즈니스 주도 대화. 예에는 옵트인 확인, 주문/전달 관리(e.g., 전달 업데이트), 계정 업데이트 또는 알림(e.g., 결제 알림) 또는 피드백 설문조사가 포함됩니다.

**인증 대화:** 사용자가 로그인 프로세스(e.g., 계정 인증, 계정 복구, 무결성 도전)에서 여러 단계에 걸쳐 일회용 비밀번호로 인증할 수 있도록 합니다.

{% alert note %}
인증 대화는 사례별로만 지원되며 Braze는 특정 SLA를 보장할 수 없습니다. 또한, Braze는 PIN 생성을 지원하지 않습니다.
{% endalert %}

**서비스 Conversations:** 사용자가 시작한 대화에 템플릿이 아닌 메시지로 응답하는 경우.

{% alert note %}
2024년 11월 1일부터 서비스형 대화는 무료로 제공되며 구매한 크레딧 할당량에서 차감되지 않습니다.
{% endalert %}

## 청구 지역 분석

#### 북아메리카

미국, 캐나다

#### 나머지 아프리카

알제리, 앙골라, 베냉, 보츠와나, 부르키나파소, 부룬디, 카메룬, 차드, 콩고, 에리트레아, 에티오피아, 가봉, 감비아, 가나, 기니비사우, 코트디부아르, 케냐, 레소토, 라이베리아, 리비아,
마다가스카르, 말라위, 말리, 모리타니아, 모로코, 모잠비크, 나미비아, 니제르, 르완다, 세네갈, 시에라리온, 소말리아, 남수단, 수단, 스와질란드, 탄자니아, 토고, 튀니지, 우간다, 잠비아

#### 아시아 태평양의 나머지 지역

아프가니스탄, 호주, 방글라데시, 캄보디아, 중국, 홍콩, 일본, 라오스, 몽골, 네팔, 뉴질랜드, 파푸아뉴기니, 필리핀, 싱가포르, 스리랑카, 대만, 타지키스탄, 태국,
투르크메니스탄, 우즈베키스탄, 베트남

#### 그 외 중앙 및 동유럽

알바니아, 아르메니아, 아제르바이잔, 벨라루스, 불가리아, 크로아티아, 체코 공화국, 조지아, 그리스, 헝가리, 라트비아, 리투아니아, 마케도니아, 몰도바, 폴란드, 루마니아, 세르비아, 슬로바키아, 슬로베니아, 우크라이나

#### 라틴 아메리카의 나머지 지역

볼리비아, 코스타리카, 도미니카 공화국, 에콰도르, 엘살바도르,
과테말라, 아이티, 온두라스, 자메이카, 니카라과, 파나마, 파라과이, 푸에르토리코, 우루과이, 베네수엘라

#### 기타 중동

바레인, 이라크, 요르단, 쿠웨이트, 레바논, 오만, 카타르, 예멘

#### 기타 서유럽

오스트리아, 벨기에, 덴마크, 핀란드, 아일랜드, 노르웨이, 포르투갈, 스웨덴, 스위스
