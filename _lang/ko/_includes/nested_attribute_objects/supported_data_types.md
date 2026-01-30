## Supported data types

다음 데이터 유형이 지원됩니다:

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
      <td>숫자 값, 예를 들어 <code>1</code> 또는 <code>5.5</code>이.</td>
    </tr>
    <tr>
      <td>문자열</td>
      <td>텍스트 값, 예를 들어 <code>"Hello"</code> 또는 <code>"The Hobbit"</code>이.</td>
    </tr>
    <tr>
      <td>부울</td>
      <td>참 또는 거짓으로 평가되는 값 <code>true</code> 또는 <code>false</code>이.</td>
    </tr>
    <tr>
      <td>배열</td>
      <td>값의 목록, 예를 들어 <code>["red", "blue", "green"]</code>이.</td>
    </tr>
    <tr>
      <td>Time</td>
      <td>
        날짜 및 시간 비교에 사용되는 타임스탬프 값입니다. 중첩된 시간 커스텀 속성을 필터링할 때 선택할 수 있습니다:<br><br>
        <ul>
          <li><strong>연중일</strong>: 비교를 위해 월과 일만 확인합니다, 예를 들어 <code>03-15</code>이.</li>
          <li><strong>Time</strong>: 연도를 포함한 전체 타임스탬프를 비교합니다, 예를 들어 <code>2023-03-15T12:00:00Z</code>이.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>객체</td>
      <td>키-값 쌍이 있는 구조화된 값, 예를 들어 <code>{"author": "Tolkien"}</code>이.</td>
    </tr>
    <tr>
      <td>객체 배열</td>
      <td>
        객체의 목록, 예를 들어 <code>[{"title": "The Hobbit"}, {"title": "Dune"}]</code>이. 
        자세한 내용은 참조하십시오 
        <a href="{{site.baseurl}}/array_of_objects/">객체의 배열</a>.
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
