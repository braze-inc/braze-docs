---
nav_title: 사용자 지정 개요
article_title: 사용자 지정 개요
page_order: 10
description: "이 참조 문서에서는 SDK 메시징 채널을 사용자 지정하고 확장하는 데 필요한 필수 개념을 다룹니다."
hidden: true
layout: redirect
redirect_to: /docs/developer_guide/getting_started/
---

# 사용자 지정 개요

> Braze의 거의 모든 기능을 완벽하게 사용자 지정할 수 있습니다! 이 사용자 지정 가이드의 문서에서는 구성과 사용자 지정의 조합을 통해 Braze 환경을 개선하는 방법을 설명합니다. 이 과정에서 마케팅 팀과 엔지니어링 팀은 긴밀히 협력하여 Braze 메시징 채널을 맞춤 설정하는 방법을 정확하게 조율해야 합니다.

{% alert note %}
Braze SDK는 강력한 툴킷으로, 크게 두 가지 주요 기능을 제공합니다. 여러 플랫폼에서 통합 고객 프로필로 사용자 데이터를 수집 및 동기화하고, 인앱 메시지, 푸시 알림, 콘텐츠 카드와 같은 메시징 채널도 처리합니다. 사용자 지정 가이드의 문서에서는 이미 [SDK 구현 프로세스]({{site.baseurl}}/developer_guide/home)를 진행했다고 가정합니다.
{% endalert %}

모든 Braze 구성요소는 접근성, 적응성 및 사용자 지정이 가능하도록 제작되었습니다. 따라서 기본 `BrazeUI` 구성 요소로 시작하여 브랜드 요구 사항과 사용 사례에 맞게 사용자 지정하는 것이 좋습니다. Braze에서는 관련 노력과 제공되는 유연성 수준에 따라 사용자 지정 방식을 세 가지로 분류합니다. 이러한 접근 방식을 '기기', '걷기' 또는 '달리기'라고 합니다.

- **기기:** 기본 스타일링 옵션을 활용하여 빠르고 쉽게 구현할 수 있습니다.
- **걷기:** 기본 템플릿에 사용자 지정 스타일을 추가하여 브랜드 경험에 더 잘 어울리도록 하세요.
- **달리기:** 스타일부터 행동, 크로스채널 연결에 이르기까지 메시지의 모든 부분을 사용자 지정합니다.

<style>
table {
  width: 60%;
}
table td {
    word-break: break-word;
}
</style>

{% tabs %}
{% tab 기기 %}

![캡션 이미지 및 이미지 전용 콘텐츠 카드가 표시된 금융 앱 샘플]({% image_buster/assets/img_archive/cc_pyrite_crawl.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

기기 접근 방식에서는 마케터가 직접 사용자 지정하는 기능을 지원합니다. 앱이나 사이트와 Braze 메시징 채널을 통합하려면 사전에 약간의 개발 작업이 필요하지만, 이 접근 방식을 사용하면 더 빨리 시작하고 실행할 수 있습니다. 

마케터는 대시보드를 통해 메시지의 콘텐츠, 오디언스 및 타이밍을 결정합니다. 하지만 스타일링 옵션은 제한되어 있습니다. 이 접근 방식은 개발자 리소스가 제한적이거나 간단한 콘텐츠를 빠르게 공유하려는 팀에 가장 적합합니다. 

<table>
<thead>
  <tr>
    <th>사용자 지정</th>
    <th>설명</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>노력</b></td>
    <td>낮음</td>
  </tr>
    <tr>
    <td><b>개발자 작업</b></td>
    <td>0-1시간</td>
  </tr>
  <tr>
    <td><b>카드 스타일</b></td>
    <td>기본 Braze 템플릿을 사용합니다.</td>
  </tr>
  <tr>
    <td><b>동작</b></td>
    <td>기본 동작 옵션 중에서 선택합니다.</td>
  </tr>
  <tr>
    <td><b>애널리틱스 추적</b></td>
    <td>애널리틱스는 Braze에서 캡처됩니다.</td>
  </tr>
  <tr>
    <td><b>키-값 쌍</b></td>
    <td>선택 사항으로 추가 UI/UX 커스터마이징을 지원합니다.</td>
  </tr>
</tbody>
</table>

{% endtab %}
{% tab 걷기 %}

![콘텐츠 카드를 사용자 지정하여 보여주는 금융 앱 샘플]({% image_buster/assets/img_archive/cc_pyrite_walk.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

하이브리드 구현 방식인 걷기 구현 방식에는 마케팅 및 개발자 팀이 앱 또는 사이트의 브랜딩에 맞게 피칭을 준비하는 단계가 포함됩니다. 

구현 프로세스에서 개발자는 메시지 채널의 모양과 느낌을 브랜드에 더 부합하도록 업데이트하는 커스텀 코드를 작성합니다. 여기에는 글꼴 유형, 글꼴 크기, 둥근 모서리 및 색상 변경이 포함됩니다. 이 접근 방식은 여전히 프로그래밍에 기반한 템플릿 스타일 조정만 지원하는 기본 옵션을 사용합니다.

마케터는 계속해서 Braze 대시보드에서 직접 오디언스, 콘텐츠, 클릭 시 동작 및 만료를 관리할 수 있습니다.

<table>
<thead>
  <tr>
    <th>사용자 지정</th>
    <th>설명</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>노력</b></td>
    <td>낮음</td>
  </tr>
    <tr>
    <td><b>개발자 작업</b></td>
    <td>0-4시간</td>
  </tr>
  <tr>
    <td><b>UI</b></td>
    <td>Braze 템플릿을 사용하거나 개발자가 직접 만든 템플릿을 사용하세요.</td>
  </tr>
  <tr>
    <td><b>동작</b></td>
    <td>기본 동작 옵션 중에서 선택합니다.</td>
  </tr>
  <tr>
    <td><b>애널리틱스 추적</b></td>
    <td>기본 분석은 Braze에서 캡처됩니다.</td>
  </tr>
  <tr>
    <td><b>키-값 쌍</b></td>
    <td>선택 사항으로 추가 UI/UX 커스터마이징을 지원합니다.</td>
  </tr>
</tbody>
</table>

{% endtab %}
{% tab 실행 %}

![이메일 캡처가 포함된 사용자 지정 콘텐츠 카드를 보여주는 샘플 금융 앱]({% image_buster/assets/img_archive/cc_pyrite_run.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

달리기 접근 방식에서는 개발자가 주도적으로 사용자 경험을 완전히 제어할 수 있습니다. 커스텀 코드에서는 메시지의 모양, 작동 방식, 다른 메시징 채널과의 상호 작용 방식(예: 푸시 알림에 기반한 콘텐츠 카드 트리거)을 지정합니다.

새로운 유형의 콘텐츠 카드나 맞춤형 UI가 포함된 인앱 메시지 등 완전히 새로운 사용자 지정 콘텐츠를 생성하는 경우, Braze SDK는 자동으로 [분석을 추적하지]({{site.baseurl}}/developer_guide/analytics/) 않습니다. 마케터가 Braze 대시보드에서 노출 횟수, 클릭, 해지 등의 측정기준에 계속 액세스할 수 있도록 프로그래밍 방식으로 분석을 처리해야 합니다. SDK에서 이 데이터를 Braze에 다시 전달하도록 Braze SDK의 분석 메서드를 호출합니다. 각 메시징 채널에는 이 작업을 용이하게 수행하는 데 도움이 되는 분석 문서가 있습니다.

<table>
<thead>
  <tr>
    <th>사용자 지정</th>
    <th>설명</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>노력</b></td>
    <td>사용 사례에 따라 다릅니다.</td>
  </tr>
    <tr>
    <td><b>개발자 작업</b></td>
    <td>적은 노력: 1~4시간<br>보통 수준의 노력: 4-8시간<br>많은 노력: 8시간 이상</td>
  </tr>
  <tr>
    <td><b>UI</b></td>
    <td>커스텀</td>
  </tr>
  <tr>
    <td><b>동작</b></td>
    <td>커스텀</td>
  </tr>
  <tr>
    <td><b>애널리틱스 추적</b></td>
    <td>커스텀</td>
  </tr>
  <tr>
    <td><b>키-값 쌍</b></td>
    <td>필수</td>
  </tr>
</tbody>
</table>
{% endtab %}
{% endtabs %}

{% alert tip %}
개발자와 구현자가 Braze의 커스텀 콘텐츠를 만들 때 마케터와 협업할 수 있는 기회가 주어집니다. 예를 들어 특정 컴포넌트에 대한 새로운 UI 또는 새로운 기능을 개발하는 경우 새로운 동작과 백엔드와 통합하는 방법을 문서화하여 팀이 성공할 수 있도록 준비하세요.
{% endalert %}