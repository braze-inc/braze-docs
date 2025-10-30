## Supported data types

지원되는 데이터 유형은 다음과 같습니다:

<table>
  <thead>
    <tr>
      <th>Data Type</th>
      <th>설명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>숫자</td>
      <td>다음과 같은 숫자 값입니다. <code>1</code> 또는 <code>5.5</code>.</td>
    </tr>
    <tr>
      <td>문자열</td>
      <td>다음과 같은 텍스트 값입니다. <code>"Hello"</code> 또는 <code>"The Hobbit"</code>.</td>
    </tr>
    <tr>
      <td>부울</td>
      <td>다음 중 하나로 평가되는 값입니다. <code>true</code> 또는 <code>false</code>.</td>
    </tr>
    <tr>
      <td>배열</td>
      <td>다음과 같은 값 목록 <code>["red", "blue", "green"]</code>.</td>
    </tr>
    <tr>
      <td>Time</td>
      <td>
        날짜 및 시간 비교에 사용되는 타임스탬프 값입니다. 중첩된 시간 커스텀 속성을 필터링할 때 선택할 수 있습니다:<br><br>
        <ul>
          <li><strong>연도</strong>: 다음과 같이 비교를 위해 월과 일만 확인합니다. <code>03-15</code>.</li>
          <li><strong>Time</strong>: 다음과 같이 연도를 포함한 전체 타임스탬프를 비교합니다. <code>2023-03-15T12:00:00Z</code>.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>객체</td>
      <td>다음과 같이 키-값 페어가 있는 구조화된 값입니다. <code>{"author": "Tolkien"}</code>.</td>
    </tr>
    <tr>
      <td>객체 배열</td>
      <td>
        다음과 같은 개체 목록 <code>[{"title": "The Hobbit"}, {"title": "Dune"}]</code>. 
        자세한 내용은 다음을 참조하세요. 
        <a href="{{site.baseurl}}/array_of_objects/">오브젝트 배열</a>.
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
