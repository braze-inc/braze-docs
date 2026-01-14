---
nav_title: 태그
article_title: 태그
page_order: 12
page_type: reference
description: "이 참고 문서에서는 참여를 더욱 체계적으로 정리하고 정렬하는 데 사용할 수 있는 Braze 대시보드의 태그에 대해 설명합니다."

---
# 태그

> Braze는 작성자, 편집자, 날짜 및 세그먼트, 캠페인, 캔버스에 대한 상태 정보를 추적하고 태그를 생성하여 참여를 더욱 체계적으로 정리하고 정렬할 수 있는 기능을 제공합니다.

## 캠페인, 캔버스 및 세그먼트 태그

캠페인, 캔버스 또는 세그먼트를 만들거나 편집할 때 태그를 추가할 수 있습니다. 참여 이름 아래의 <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**태그를** 클릭하고 기존 태그를 선택하거나 입력을 시작하여 새 태그를 추가합니다.

\![캠페인 생성 중 태그 추가하기.]({% image_buster /assets/img_archive/tags_add_tag.png %}){: style="max-width:60%;" }

{% alert important %}
캠페인, 캔버스 또는 세그먼트에 최대 175개의 태그를 추가할 수 있습니다.
{% endalert %}

### 대량 태그 지정

여러 참여를 선택하고 <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**다른 계정으로 태그하기를** 선택하여 여러 캠페인, 캔버스 또는 세그먼트에 태그를 추가할 수도 있습니다.

\![여러 캠페인에 동시에 태그 추가하기.]({% image_buster /assets/img_archive/tags_apply_multiple.gif %})

{% alert important %}
대량 태그 지정을 사용하여 이미 다른 태그가 있는 여러 캠페인에 새 태그를 적용하면 선택한 각 캠페인에 새 태그가 적용되며, 캠페인에 있는 모든 태그는 원래 해당 태그와 연결되어 있지 않더라도 선택한 다른 모든 캠페인에 적용됩니다.
{% endalert %}

### 태그 보기

캠페인, 캔버스 또는 세그먼트에 설정된 태그는 참여 이름 근처의 세부 정보 페이지에서 볼 수 있습니다. 캠페인 분석에도 표시됩니다.

캠페인 분석 페이지에 표시된 태그.]({% image_buster /assets/img_archive/tag_details_page.png %}){: style="max-width:60%;" }

### 태그별로 필터링하기

태그는 캠페인, 캔버스 또는 세그먼트 목록에 **보관됨** 및 **초안과** 같은 상태 레이블에 대한 추가 태그와 함께 표시됩니다. 태그를 기준으로 필터링하려면 태그 목록에서 태그 이름을 선택합니다.

캠페인 목록의 태그.]({% image_buster /assets/img_archive/tags_grid.png %})

## 커스텀 데이터 태그

[커스텀 속성]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) 및 커스텀 [이벤트를]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#managing-custom-events) 관리할 때 커스텀 데이터에 태그를 추가할 수도 있습니다. 

{% alert important %}
이 기능은 현재 얼리 액세스 중입니다. 이번 얼리 액세스에 참여하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 태그 관리하기

캠페인, 캔버스, 세그먼트에서 동일한 태그를 사용할 수 있습니다. 대시보드에서 태그의 이름을 효율적으로 변경, 제거 또는 추가하려면 **설정** > **태그 관리로** 이동하세요.

설정 관리 페이지의 태그 탭을 클릭합니다.]({% image_buster /assets/img_archive/tags_view.png %})

태그를 더욱 체계적으로 정리하려면 태그를 상위 태그 아래에 중첩하세요. 예를 들어 모든 휴일 태그를 상위 `Holidays` 태그 아래에 중첩하거나 마케팅 퍼널의 한 단계와 관련된 모든 태그를 상위 `Funnel` 태그 아래에 보관할 수 있습니다. 

이렇게 하려면 새 태그를 만들고 **아래에 태그** 중첩을 선택한 다음 새 태그를 중첩할 기존 태그를 선택합니다. **태그 관리** 페이지에서 기존 태그를 중첩할 수도 있습니다. 이 페이지에서 태그가 있는 행을 마우스로 가리키고 **<i class="fas fa-pencil-alt"></i>편집을** 클릭합니다. 그런 다음 이전과 동일한 단계를 따릅니다.

\![중첩 태그 만들기.]({% image_buster /assets/img_archive/tag_nested.png %}){: style="max-width:70%;" }

## 모범 사례 {#tags-best-practices}

태그는 참여 전술을 추적하는 데 유용한 정리 툴이 될 수 있습니다. 세그먼트와 캠페인을 비즈니스 목표, 퍼널 단계 등에 연결할 수 있습니다.

다음은 전자상거래 앱에서 유용하게 사용할 수 있는 태그의 예입니다:

<style>
table td {
    word-break: break-word;
}
</style>


<table>
<thead>
  <tr>
    <th>퍼널</th>
    <th>비즈니스 목표</th>
    <th>지역</th>
    <th>캠페인</th>
    <th>휴일</th>
    <th>트랜잭션</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>온보딩<br>재참여<br>충성도<br>PowerUser<br>고객이탈<br>분실</td>
    <td>HighSpender<br>ActiveUser<br>신규 사용자<br>페이스북 어트리뷰션<br>FirstAction</td>
    <td>미국<br>동북<br>중서부<br>South<br>West<br>LATAM<br>AP<br>서부유럽<br>중동</td>
    <td>판매<br>쿠폰<br>이벤트</td>
    <td>MLK<br>슈퍼볼<br>PiDay<br>세인트패트릭데이<br>3월의 광기<br>부활절<br>패스 오버<br>어머니의 날<br>기념일<br>아버지의 날<br>7월 넷째주<br>노동절<br>재향군인의 날<br>콜럼버스의 날<br>프레지던트데이<br>할로윈<br>로쉬하샤나<br>추수감사절<br>크리스마스<br>하누카<br>NewYears</td>
    <td>트랜잭션<br>알림<br>커넥티드 액션 취하기</td>
  </tr>
</tbody>
</table>

## 사용 사례

태그를 활용하여 메시징 라이프사이클을 관리하는 방법에 대한 영감을 찾고 계신가요? 다음은 몇 가지 일반적인 사용 사례입니다.

{% tabs %}
{% tab Throttling %}

### 스로틀링

고객이 특정 유형의 캠페인을 받는 빈도를 제한하세요. 예를 들어 다음 필터를 설정하여 프로모션 캠페인의 빈도를 제한할 수 있습니다:

`Last received campaign` 와 함께 `Promo` 태그 5 일 이상 전
<br>`OR`<br>
`Has not received campaign` 태그 포함 `Promo`

{% endtab %}
{% tab Reporting %}

### 보고

참여 보고서를 설정하여 특정 태그가 있는 모든 캠페인의 볼륨을 주시하세요. 예를 들어 모든 푸시 캠페인을 모니터링하려면 해당 캠페인에 `Push Reporting` 같은 태그를 추가한 다음 [참여 보고서를]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases) 설정하여 태그가 지정된 캠페인에 대한 보고서를 매일 전송할 수 있습니다.

{% endtab %}
{% endtabs %}