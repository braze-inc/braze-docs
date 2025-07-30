---
nav_title: 태그
article_title: 태그
page_order: 12
page_type: reference
description: "이 참조 문서에서는 Braze 대시보드의 태그에 대해 설명하며, 이를 사용하여 인게이지먼트를 더욱 체계적으로 정리하고 분류할 수 있습니다."

---
# 태그

> Braze는 세그먼트, 캠페인 및 캔버스에 대한 작성자, 편집자, 날짜 및 상태 정보를 추적하고 인게이지먼트를 더욱 체계적으로 정리하고 정렬할 수 있도록 태그를 생성할 수 있는 기능을 제공합니다.

## 캠페인, 캔버스, 그리고 세그먼트 태그

캠페인, 캔버스 또는 세그먼트를 만들거나 편집할 때 태그를 추가할 수 있습니다. 클릭 <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**태그** 참여 이름 아래에서 기존 태그를 선택하거나 새 태그를 추가하려면 입력을 시작하세요.

![캠페인 생성 중 태그 추가][2]

여러 참여를 선택하고 <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**태그로 지정**을 클릭하여 여러 캠페인, 캔버스 또는 세그먼트에 태그를 추가할 수도 있습니다.

![여러 캠페인에 태그 추가하기][5]

캠페인, 캔버스 또는 세그먼트에 설정된 태그는 참여 이름 근처의 세부 페이지에서 볼 수 있습니다.

![캠페인 세부 정보 페이지에 표시된 태그][3]

그들은 또한 캠페인, 캔버스 또는 세그먼트 목록에서 **보관됨** 및 **초안**과 같은 상태 레이블에 대한 추가 태그와 함께 볼 수 있습니다.

![캠페인 목록의 태그][4]{: style ="max-width:70%;" }

태그로 필터링하려면 태그 목록에서 태그 이름을 선택하거나 `tag:` 선택기를 사용하여 검색 창에서 태그를 검색하십시오. 예를 들어 `Onboarding` 태그를 검색하려면 "태그:온보딩"을 입력하세요.

![Welcome 이메일로 태그된 모든 캠페인 검색][6]

{% alert important %}
캠페인, 캔버스 또는 세그먼트에 최대 175개의 태그를 추가할 수 있습니다.
{% endalert %}

## 커스텀 데이터 tags

태그는 [커스텀 속성]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) 및 [커스텀 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#managing-custom-events)을(를) 관리할 때 커스텀 데이터에 추가될 수도 있습니다. 

{% alert important %}
이 기능은 현재 초기 액세스 중입니다. 이 얼리 액세스에 참여하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 모범 사례 {#tags-best-practices}

태그는 인게이지먼트 전술을 추적하는 데 유용한 조직 도구가 될 수 있습니다. 세그먼트와 캠페인을 비즈니스 목표, 퍼널 단계 등과 연결할 수 있습니다.

The following is an example of tags an eCommerce app might find useful:

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
    <th>거래</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>온보딩<br>재참여<br>충실한<br>파워유저<br>고객이탈<br>유실</td>
    <td>고지출자<br>액티브유저<br>신규 사용자<br>페이스북어트리뷰션<br>첫번째행동</td>
    <td>미국<br>북동<br>중서부<br>남쪽<br>서쪽<br>남미<br>AP<br>서유럽<br>중동</td>
    <td>매출<br>쿠폰<br>이벤트</td>
    <td>MLK<br>슈퍼볼<br>파이데이<br>성패트릭의날<br>3월의광란<br>부활절<br>유월절<br>어머니의 날<br>현충일<br>아버지의 날<br>독립기념일<br>노동절<br>재향 군인의 날<br>콜럼버스데이<br>대통령의 날<br>할로윈<br>로쉬하샤나<br>추수 감사절<br>크리스마스<br>하누카<br>새해</td>
    <td>트랜잭션<br>알림<br>연결된조치취함</td>
  </tr>
</tbody>
</table>

캠페인, 캔버스 및 세그먼트 전반에 걸쳐 동일한 태그를 사용할 수 있습니다. 대시보드에서 태그를 효율적으로 이름 바꾸기, 제거 또는 추가하려면 **설정** > **태그 관리**로 이동하십시오.

![설정 관리 페이지의 탭 태그][8]

태그를 더 잘 정리하려면 태그를 상위 태그 아래에 중첩하세요. 예를 들어, 모든 휴일 태그를 상위 `Holidays` 태그 아래에 중첩시키거나, 마케팅 퍼널의 단계와 관련된 모든 태그를 상위 `Funnel` 태그 아래에 중첩시킬 수 있습니다. 

그렇게 하려면 새 태그를 만들고 **태그 아래에 중첩**을 선택한 다음 새 태그를 중첩할 기존 태그를 선택합니다. 기존 태그를 **태그 관리** 페이지에서 중첩할 수도 있습니다. 이 페이지에서 태그가 있는 행 위로 마우스를 가져가서 **<i class="fas fa-pencil-alt"></i>편집**을 클릭하세요. 그런 다음 이전과 동일한 단계를 따르십시오.

![태그를 중첩하여 만들기][1]{: style ="max-width:70%;" }

## 사용 사례

태그를 활용하여 메시징 생애주기를 관리하는 방법에 대한 영감을 찾고 계신가요? 다음은 몇 가지 일반적인 사용 사례입니다:

### 제한

고객이 특정 유형의 캠페인을 받는 빈도를 제한하십시오. 예를 들어, 다음 필터를 설정하여 프로모션 캠페인의 빈도를 제한할 수 있습니다:

5일 이전 `Promo` 태그가 있는 `Last received campaign`
<br>`OR`<br>
`Promo` 태그가 있는 `Has not received campaign`

### 보고

특정 태그가 있는 모든 캠페인의 볼륨을 주시하기 위해 참여 보고서를 설정하십시오. 예를 들어, 모든 푸시 캠페인을 모니터링하려면 해당 캠페인에 `Push Reporting`와 같은 태그를 추가한 다음, 태그된 캠페인의 보고서를 매일 보내는 [참여 보고서]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases)를 설정할 수 있습니다.



[1]: {% image_buster /assets/img_archive/tag_nested.png %}
[2]: {% image_buster /assets/img_archive/tags_add_tag.png %}
[3]: {% image_buster /assets/img_archive/tag_details_page.png %}
[4]: {% image_buster /assets/img_archive/tags_grid.png %}
[5]: {% image_buster /assets/img_archive/tags_apply_multiple.png %}
[6]: {% image_buster /assets/img_archive/tags_filtering.png %}
[7]: {% image_buster /assets/img_archive/Tags-Potential_Tags.png %}
[8]: {% image_buster /assets/img_archive/tags_view.png %}
