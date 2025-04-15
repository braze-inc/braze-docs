---
nav_title: 데이터 센터
article_title: 데이터 센터
page_order: 0.1
page_type: reference
description: "이 참조 문서에서는 데이터 센터의 위치, 지역별 데이터 센터에 가입하는 방법 등 데이터 센터에 대한 정보를 다룹니다."
---

# 데이터 센터

> Braze 데이터 센터는 사용자의 데이터가 처리되고 저장되는 위치에 대한 옵션을 제공하기 위해 구축되었습니다. 이를 통해 데이터 주권, 유연성 및 관리와 관련된 위험을 효과적으로 관리할 수 있습니다. Braze 데이터 센터를 선택하면 당사의 플랫폼이 데이터 관리의 모든 현지 요구 사항을 충족하거나 능가한다는 것을 확신할 수 있습니다.

## 작동 방식

Braze는 전 세계 여러 지역에 위치한 여러 데이터 센터를 운영하고 있습니다. 이러한 데이터 센터를 통해 안정적이고 확장 가능한 서비스를 제공할 수 있습니다. 이러한 지리적 분포는 데이터가 서버와 사용자 간에 이동하는 데 걸리는 시간인 지연 시간을 최소화하는 데 도움이 됩니다. 

즉, 사용자가 앱이나 웹사이트와 상호 작용할 때 요청이 가장 가까운 데이터 센터로 전달되어 성능을 최적화하고 로드 시간을 단축할 수 있습니다. 가장 가까운 데이터 센터에 연결하면 실시간 메시징과 사용자 참여에 특히 중요한 빠른 로딩 시간을 경험할 수 있습니다.

사용자에게 푸시 알림을 보내는 모바일 앱이 있다고 가정해 보겠습니다. 멜버른에 있는 사용자가 알림을 받으면 해당 알림 전송 요청이 호주에서 가장 가까운 데이터 센터로 라우팅됩니다. 프로모션 이벤트 기간 동안 모바일 앱 사용자가 급증하는 경우, Braze는 여러 데이터 센터를 통해 수요 증가를 처리할 수 있는 확장 가능한 인프라를 갖추고 있습니다.

## 데이터 센터 목록

사용 가능한 데이터 센터 목록은 다음 표를 참조하세요.

<style>
table th:nth-child(1) {
    width: 10%;
}
table th:nth-child(2) {
    width: 33%;
}
table th:nth-child(3) {
    width: 33%;
}
table th:nth-child(4) {
    width: 24%;
}
table td {
    word-break: break-word;
}
</style>
<table>
  <thead>
    <tr>
      <th>데이터 센터 지역</th>
      <th>대시보드 URL</th>
      <th>REST 엔드포인트</th>
      <th>SDK 엔드포인트</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>호주</b></td>
      <td><code>https://dashboard.au-01.braze.com</code></td>
      <td><code>https://rest.au-01.braze.com</code></td>
      <td><code>sdk.au-01.braze.com</code></td>
    </tr>
    <tr>
      <td><b>유럽</b></td>
      <td>
        <ul>
          <li><code>https://dashboard-01.braze.eu</code></li>
          <li><code>https://dashboard-02.braze.eu</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>https://rest.fra-01.braze.eu</code></li>
          <li><code>https://rest.fra-02.braze.eu</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>sdk.fra-01.braze.eu</code></li>
          <li><code>sdk.fra-02.braze.eu</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>미국</b></td>
      <td>
        <ul>
          <li><code>https://dashboard-01.braze.com</code></li>
          <li><code>https://dashboard-02.braze.com</code></li>
          <li><code>https://dashboard-03.braze.com</code></li>
          <li><code>https://dashboard-04.braze.com</code></li>
          <li><code>https://dashboard-05.braze.com</code></li>
          <li><code>https://dashboard-06.braze.com</code></li>
          <li><code>https://dashboard-07.braze.com</code></li>
          <li><code>https://dashboard-08.braze.com</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>https://rest.iad-01.braze.com</code></li>
          <li><code>https://rest.iad-02.braze.com</code></li>
          <li><code>https://rest.iad-03.braze.com</code></li>
          <li><code>https://rest.iad-04.braze.com</code></li>
          <li><code>https://rest.iad-05.braze.com</code></li>
          <li><code>https://rest.iad-06.braze.com</code></li>
          <li><code>https://rest.iad-07.braze.com</code></li>
          <li><code>https://rest.iad-08.braze.com</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>sdk.iad-01.braze.com</code></li>
          <li><code>sdk.iad-02.braze.com</code></li>
          <li><code>sdk.iad-03.braze.com</code></li>
          <li><code>sdk.iad-04.braze.com</code></li>
          <li><code>sdk.iad-05.braze.com</code></li>
          <li><code>sdk.iad-06.braze.com</code></li>
          <li><code>sdk.iad-07.braze.com</code></li>
          <li><code>sdk.iad-08.braze.com</code></li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## 지역별 데이터 센터에 가입하기

Braze 계정을 설정할 때 지역별 데이터 센터에 가입할 수 있습니다. 사용자의 지역에 따라 가장 적합한 데이터 센터에 대한 정보 및 권장 사항은 계정 관리자에게 문의하세요.
