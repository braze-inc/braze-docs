---
nav_title: 내 엽서
article_title: 내 엽서
page_order: 1
description: "이 참고 문서에서는 다이렉트 메일을 CRM 워크플로우의 추가 채널로 사용할 수 있는 Braze와 MyPostcard의 파트너십에 대해 간략하게 설명합니다."
alias: /partners/mypostcard/
page_type: partner
search_tag: Partner

---

# 내 엽서

> 선도적인 글로벌 엽서 앱인 [MyPostcard를][1] 사용하면 다이렉트 메일 캠페인을 쉽게 실행하여 고객과 원활하고 수익성 있는 방식으로 소통할 수 있습니다. 

내 엽서와 Braze 통합 기능을 사용하여 고객에게 손쉽게 인쇄 메일을 보낼 수 있습니다.

## 필수 조건

| 요구 사항                      | 설명                                                                                                             |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| 내 엽서 B2B 계정           | 이 통합 기능을 이용하려면 MyPostcard에 등록해야 합니다.                                          |
| B2B API 키 및 자격 증명        | API 키와 자격 증명은 MyPostcard B2B 관리자 도구에서 찾을 수 있습니다.                                         |
| 승인된 마이엽서 B2B 캠페인 | 이 통합 기능을 활용하려면 MyPostcard B2B 도구에서 인쇄 메일링 캠페인을 설정해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 사용 사례

다이렉트 메일 캠페인의 수준을 높이려면 기존의 대량 메일을 넘어 인쇄 메일을 워크플로우에 원활하게 통합하는 것이 중요합니다. 이 접근 방식을 사용하면 이메일 뉴스레터 수신을 거부했거나 이메일이 스팸으로 표시된 특정 고객에게 도달할 수 있습니다. My엽서를 사용하면 Braze를 통해 직접 인쇄 메일 캠페인을 손쉽게 보낼 수 있습니다.

- 기술 전문 지식 없이도 인쇄 메일을 강력한 새 채널로 통합하여 Braze에서 직관적인 워크플로를 구축할 수 있습니다.
- 몇 가지 간단한 단계를 통해 개인화된 인쇄 메일링의 잠재력을 활용하세요.
- 전담 팀의 맞춤형 지원이 뒷받침되는 간편한 구현의 이점을 누려보세요.

## 통합

내 엽서와 통합하려면 [로그인하거나 가입][2] 한 후 [Braze 웹훅을][3] 통해 첫 번째 캠페인을 생성하여 사용하세요.

### 1단계: Braze 웹훅 템플릿 만들기

Braze 플랫폼에서 **템플릿** > **웹훅 템플릿으로** 이동하여 향후 캠페인이나 캔버스에서 사용할 MyPostcard 웹훅 템플릿을 만드세요.

{% alert note %}
[이전 탐색을]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/) 사용하는 경우 **참여** > **템플릿 및 미디어** > **웹훅 템플릿으로** 이동합니다.
{% endalert %}

일회성 내 엽서 웹훅 캠페인을 만들거나 기존 템플릿을 사용하려면 새 캠페인을 만들 때 Braze에서 **웹훅을** 선택합니다. 다음 입력란을 작성합니다:

| 필드         | 설명                                               |
|---------------|-----------------------------------------------------------|
| **웹훅 URL** | B2B 관리자 도구에 표시된 웹훅 URL입니다.             |
| **요청 본문** | 원시 텍스트(B2B 관리자 도구에 있는 JSON 형식).        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 요청 방법 및 헤더

내 엽서에는 템플릿에 다음 HTTP 헤더와 함께 HTTP 메서드가 포함되어야 합니다.

{% raw %}
<table>
  <thead>
    <tr>
      <th><strong>필드</strong></th>
      <th><strong>세부 정보</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>HTTP 메서드</strong></td>
      <td><code>POST</code></td>
    </tr>
    <tr>
      <td><strong>사용자 이름</strong></td>
      <td><code>{{ '&lt;username&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>비밀번호</strong></td>
      <td><code>{{ '&lt;password&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>콘텐츠-유형</strong></td>
      <td><code>application/json</code></td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 요청 본문

B2B 관리 도구에 표시되는 요청 본문을 복사한 다음 Liquid 개인화 태그를 사용하여 플레이스홀더를 콘텐츠로 채웁니다.

![작성 탭에는 JSON 본문과 웹훅 정보가 표시됩니다.][4]

### 2단계: 요청 미리보기

그런 다음 **미리보기** 패널에서 요청을 미리 보거나 **테스트** 탭으로 이동하여 무작위 사용자, 기존 사용자를 선택하거나 사용자 지정 사용자를 만들어 웹훅을 테스트할 수 있습니다. 페이지에서 나가기 전에 템플릿을 저장하는 것을 잊지 마세요!

![다양한 필드를 사용하여 웹훅 탭을 테스트하여 구현을 검증합니다.][5]

{% alert important %}
페이지에서 나가기 전에 템플릿을 저장하는 것을 잊지 마세요! <br>업데이트된 웹훅 템플릿은 새 [웹훅 캠페인을]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) 만들 때 **저장된 웹훅 템플릿** 목록에서 찾을 수 있습니다.
{% endalert %}

[1]: https://www.mypostcard.com
[2]: https://www.mypostcard.com/b2b/admin/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks
[4]: {% image_buster /assets/img/mypostcard/mypostcard_compose.jpg %}
[5]: {% image_buster /assets/img/mypostcard/mypostcard_test.jpg %}
