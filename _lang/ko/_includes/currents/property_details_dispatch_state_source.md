<ul>
<li><code>dispatch_id</code> 특정 메시지 전송, 예를 들어 캠페인 전송을 위한 ID입니다. 같은 전송에서 발생하는 모든 푸시 이벤트는 동일한 <code>dispatch_id</code>입니다. 사용하십시오 <code>dispatch_id</code> 동일한 전송에 속하는 이벤트를 그룹화하여 해당 전송의 푸시 메시지 생애 주기를 그룹화하고 상관시킬 수 있습니다(예: 전송, 반송 및 열기).</li>
<li><code>state_change_source</code> 전체 소스 이름의 문자열을 반환합니다. 예를 들어, 소스 CSV 가져오기는 문자열을 반환합니다. <code>CSV import</code>입니다. 사용 가능한 소스는 아래에 나열되어 있습니다:</li>
</ul>
<table class="reset-td-br-1 reset-td-br-2" role="presentation">
<thead>
<tr><th>소스</th><th>설명</th></tr>
</thead>
<tbody>
<tr><td>SDK</td><td>SDK 엔드포인트</td></tr>
<tr><td>대시보드</td><td>대시보드의 사용자 프로필 페이지에서 사용자의 구독 상태가 업데이트되는 경우</td></tr>
<tr><td>구독 페이지</td><td>사용자가 환경 설정 센터가 아닌 이메일 링크를 통해 구독을 취소하는 경우</td></tr>
<tr><td>REST API</td><td>REST API 엔드포인트</td></tr>
<tr><td>CSV 가져오기</td><td>CSV 사용자 가져오기</td></tr>
<tr><td>환경설정 센터</td><td>환경설정 센터에서 사용자가 업데이트되는 경우</td></tr>
<tr><td>인바운드 메시지</td><td>SMS 등의 채널을 통해 최종 사용자의 인바운드 메시지에 의해 사용자가 업데이트되는 경우</td></tr>
<tr><td>마이그레이션</td><td>내부 마이그레이션 또는 유지 관리 스크립트에 의해 사용자가 업데이트되는 경우</td></tr>
<tr><td>사용자 병합</td><td>사용자 병합 프로세스에 의해 사용자가 업데이트되는 경우</td></tr>
<tr><td>캔버스 사용자 업데이트 단계</td><td>캔버스 사용자 업데이트 단계에서 사용자가 업데이트된 경우</td></tr>
</tbody>
</table>
