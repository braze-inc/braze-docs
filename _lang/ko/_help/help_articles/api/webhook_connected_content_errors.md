---
nav_title: 웹훅 및 연결된 콘텐츠 요청 문제 해결
article_title: 웹훅 및 연결된 콘텐츠 요청 문제 해결
page_order: 3
channel:
  - webhooks
description: "이 문서에서는 웹훅 및 커넥티드 콘텐츠 오류 코드를 해결하는 방법과 오류의 유형 및 해결 단계를 설명합니다."
---

# 웹훅 및 커넥티드 콘텐츠 요청 문제 해결하기

> 이 문서에서는 웹훅 및 연결된 콘텐츠의 일반적인 오류 코드를 해결하는 방법을 다루고 요청에서 이러한 오류가 어떻게 발생할 수 있는지에 대한 자세한 설명을 제공합니다.

## 4XX 오류

`4XX` 오류는 엔드포인트로 전송된 요청에 문제가 있음을 나타냅니다. 이러한 오류는 일반적으로 잘못된 매개변수, 인증 헤더 누락, 잘못된 URL 등 잘못된 요청으로 인해 발생합니다.

오류 코드 세부 정보 및 해결 단계는 다음 표를 참조하세요:

<style>
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>오류 코드</th>
      <th>의미</th>
      <th>해결 단계</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>400 잘못된 요청</b></td>
      <td>요청에 잘못된 구문이 있습니다.</td>
      <td>
        <ul>
          <li>요청 페이로드에 구문 오류가 있는지 확인합니다.</li>
          <li>모든 필수 필드가 포함되어 있고 형식이 올바른지 확인합니다.</li>
          <li>JSON 페이로드를 전송하는 경우 JSON 구조의 유효성을 검사합니다.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>401 승인되지 않음</b></td>
      <td>요청에는 사용자 인증이 필요합니다.</td>
      <td>
        <ul>
          <li>요청 헤더에 올바른 인증 자격 증명(예: API 키 또는 토큰)이 포함되어 있는지 확인합니다.</li>
          <li>엔드포인트에 액세스할 수 있는 사용자 권한이 있는지 확인합니다.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>403 금지됨</b></td>
      <td>엔드포인트가 요청을 이해하지만 권한 부여를 거부합니다.</td>
      <td>
        <ul>
          <li>API 키 또는 토큰에 필요한 권한이 있는지 확인합니다.</li>
          <li>엔드포인트에 액세스할 수 있는 사용자 권한이 있는지 확인합니다.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>404 찾을 수 없음</b></td>
      <td>엔드포인트에서 요청된 리소스를 찾을 수 없습니다.</td>
      <td>
        <ul>
          <li>엔드포인트 URL에 오타나 잘못된 경로가 있는지 확인하세요.</li>
          <li>액세스하려는 리소스가 존재하는지 확인합니다.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>405 메서드 허용되지 않음</b></td>
      <td>요청 방법은 엔드포인트에서 알고 있지만 대상 리소스에서 지원되지 않습니다.</td>
      <td>
        <ul>
          <li>요청에 사용된 HTTP 메서드(DELETE, GET, POST, PUT)를 확인합니다.</li>
          <li>엔드포인트가 사용 중인 방법을 지원하는지 확인합니다.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>408 요청 시간 초과</b></td>
      <td>엔드포인트에서 요청을 처리하는 동안 시간이 초과되었습니다.</td>
      <td>
        <ul>
          <li>요청에 사용된 HTTP 메서드(DELETE, GET, POST, PUT)를 확인합니다.</li>
          <li>엔드포인트가 사용 중인 방법을 지원하는지 확인합니다.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>409 충돌</b></td>
      <td>리소스의 현재 상태와 충돌하여 요청이 불완전합니다.</td>
      <td>
        <ul>
          <li>요청에 사용된 HTTP 메서드(DELETE, GET, POST, PUT)를 확인합니다.</li>
          <li>엔드포인트가 사용 중인 방법을 지원하는지 확인합니다.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>429 너무 많은 요청</b></td>
      <td>주어진 시간 내에 너무 많은 요청이 전송되었습니다.</td>
      <td>
        <ul>
          <li>캠페인 또는 캔버스 단계의 요금 한도를 낮추세요.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## 5XX 오류

`5XX` 오류는 엔드포인트에 문제가 있음을 나타냅니다. 이러한 오류는 일반적으로 서버 측 문제로 인해 발생합니다.

| 오류 코드                    | 의미                                                                                                                                         |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **500 내부 서버 오류** | 엔드포인트에서 예기치 않은 조건이 발생하여 요청을 완료하지 못했습니다.                                                       |
| **502 불량 게이트웨이**           | 엔드포인트가 업스트림 서버로부터 잘못된 응답을 받았습니다.                                                                                   |
| **503 서비스를 사용할 수 없음**   | 일시적인 과부하 또는 유지 관리로 인해 엔드포인트가 현재 요청을 처리할 수 없습니다.                                                    |
| **504 게이트웨이 시간 초과**       | 엔드포인트가 업스트림 서버로부터 적시에 응답을 받지 못했습니다.                                                                               |
| **599 연결 오류**      | Braze가 엔드포인트에 연결을 시도하는 동안 네트워크 연결 시간 초과 오류가 발생했습니다. 이는 엔드포인트가 불안정하거나 다운되었을 수 있음을 의미합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 5XX 오류 해결

다음은 일반적인 `5XX` 오류를 해결하는 팁입니다:

- **메시지 활동 로그에서** 오류 메시지를 검토하여 구체적인 세부 정보를 확인할 수 있습니다. 웹훅의 경우, Braze 홈페이지의 **시간 경과에 따른 성과** 섹션으로 이동하여 웹훅 통계를 선택합니다. 여기에서 오류가 발생한 시점을 나타내는 타임스탬프를 찾을 수 있습니다.
- 엔드포인트에 과부하가 걸리는 요청을 너무 많이 보내지 않도록 하세요. 일괄 전송하거나 속도 제한을 조정하여 오류가 줄어드는지 확인할 수 있습니다.
