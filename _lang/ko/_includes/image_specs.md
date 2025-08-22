{% if include.variable_name == "image behavior" %}


| 레이아웃 | 동작 |
| --- | --- |
| 이미지 및 텍스트 | 키가 크거나 좁은 이미지는 축소되고 가로 중앙에 배치됩니다. 넓은 이미지는 왼쪽과 오른쪽 가장자리가 잘립니다. |
| 이미지만 | 메시지는 대부분의 가로 세로 비율에 맞게 이미지 크기를 조정합니다. |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "payload size" %}

다음 페이로드 크기를 권장합니다:

| 메시징 시스템 | 권장 페이로드 |
| --- | --- |
| iOS(iOS 8 이전 버전) | 0.256 KB |
| iOS(iOS 8 이후) | 2 KB |
| Android(FCM) | 4 KB |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "in-app messages" %}

Modal 인앱 메시지는 선택한 이미지 또는 문구의 크기와 비율을 그대로 유지하면서 기기에 가장 알맞은 최적의 비율로 채워지도록 설계되었습니다.

인앱 메시지(버튼, 헤드라인, 본문 등)에 포함할 수 있는 텍스트 글자 수에는 제한이 없지만, 사용하는 텍스트 글자 수를 조절할 수 있습니다. 텍스트가 너무 많으면 사용자가 메시지를 확장하고 스크롤해야 합니다.

모든 인앱 메시지의 권장 이미지 크기는 500KB, 최대 이미지 크기는 5MB이며 PNG, JPEG, GIF 파일 유형을 지원합니다.

{% tabs %}
{% tab 인물 사진 %}

| 유형 | 종횡비 | 이미지 품질 | 참고 |
| --- | --- | --- | --- |
| 텍스트가 포함된 세로 전체 화면 | 6:5 | 고해상도 1200 x 1000 픽셀 <br>최소 해상도 600 x 500 픽셀 | 크로핑은 모든 면에서 발생할 수 있지만, 이미지는 항상 뷰포트의 상위 50%를 채웁니다 |
| 세로 전체 화면(이미지만, 버튼 유무에 관계없이) | 3:5 | 고해상도 1200 x 2000 픽셀 <br> 최소 해상도 600 x 1000 픽셀 | 키가 큰 기기에서는 왼쪽과 오른쪽 가장자리에서 잘림 현상이 발생할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab 가로 %}

| 유형 | 종횡비 | 이미지 품질 | 참고 |
| --- | --- | --- | --- |
| 텍스트가 포함된 가로 전체 화면 | 10:3 | 고해상도 2000 x 600 픽셀 <br>최소 해상도 1000 x 300 픽셀 | 크로핑은 모든 면에서 발생할 수 있지만, 이미지는 항상 뷰포트의 상위 50%를 채웁니다. |
| 가로 전체 화면(이미지만, 버튼 유무에 관계없이) | 5:3 | 고해상도 2000 x 600 픽셀 <br> 최소 해상도 1000 x 600 픽셀 | 키가 큰 기기에서는 왼쪽과 오른쪽 가장자리에서 잘림 현상이 발생할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab 슬라이드업 %}

| 유형 | 종횡비 | 이미지 품질 | 참고 |
| --- | --- | --- | --- |
| 슬라이드업 | 1:1 | 고해상도 150 x 150 픽셀 <br> 최소 해상도 50 x 50 픽셀 | 다양한 가로 세로 비율의 이미지가 잘리지 않고 정사각형 이미지 컨테이너에 들어갑니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab 모달 %}

| 유형 | 종횡비 | 이미지 품질 | 참고 |
| --- | --- | --- | --- |
| Modal(이미지만 해당) | 1:1 | 고해상도 1200 x 2000 픽셀 <br> 최소 해상도 600 x 600 픽셀 | 메시지는 대부분의 가로 세로 비율에 맞게 이미지 크기를 조정합니다. |
| 텍스트가 있는 모달 | 29:10 | 고해상도 1450 x 500 픽셀 <br> 최소 해상도 600 x 205 픽셀 | 긴 이미지는 축소되어 가로로 가운데에 배치됩니다. 넓은 이미지는 왼쪽과 오른쪽 가장자리가 잘립니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% endtabs %}

{% endif %}

{% if include.variable_name == "push notifications" %}

| 메시지 유형 | 최대 메시지 길이 | 최대 제목 길이 |
| --- | --- | --- |
| iOS 잠금 화면 | 175자 | 43자 |
| iOS 알림 | 175자 | 43자 |
| iOS 배너 알림 | 85자 | 43자 |
| Android 잠금 화면 | 49자 | 43자 |
| Android 알림 서랍 | 597자 | 43자 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

모든 푸시 이미지의 권장 이미지 크기는 500KB입니다.

<style>
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>이미지 유형</th>
      <th>종횡비</th>
      <th>최대 픽셀</th>
      <th>최대 이미지 크기</th>
      <th>파일 유형</th>
      <th>참고</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>iOS</td>
      <td>2:1(권장)</td>
      <td>1038 x 1038</td>
      <td>5 MB</td>
      <td>PNG, JPEG, GIF</td>
      <td>2020년 1월부터 iOS 리치 푸시 알림은 1038 x 1038 픽셀의 이미지가 10MB 미만인 경우 처리할 수 있지만, 가능한 한 작은 파일 크기를 사용하는 것이 좋습니다. 실제로 대용량 파일을 전송하면 불필요한 네트워크 스트레스가 발생하고 다운로드 시간 초과가 더 자주 발생할 수 있습니다.<br><br>자세한 내용은 <a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/">iOS 리치 알림</a>을 참조하세요.</td>
    </tr>
    <tr>
      <td>Android 푸시 아이콘</td>
      <td>1:1</td>
      <td>N/A</td>
      <td>500 KB</td>
      <td>PNG, JPEG</td>
      <td></td>
    </tr>
    <tr>
      <td>Android 확장 알림 이미지</td>
      <td>2:1</td>
      <td><b>작음:</b><br>512 x 256<br><br><b>중간:</b><br>1024 x 512<br><br><b>큼:</b><br>2048 x 1024</td>
      <td>500 KB</td>
      <td>PNG, JPEG</td>
      <td><a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/">Android 리치 알림에</a> 사용됩니다.</td>
    </tr>
    <tr>
      <td>안드로이드 경사 이미지</td>
      <td>3:2</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>PNG, JPEG</td>
      <td>자세한 내용은 <a href="{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/inline_image_push/">Android 인라인 이미지 푸시</a>를 참조하세요.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4  .reset-td-br-5 .reset-td-br-6 role="presentation"}

{% endif %}

{% if include.variable_name == "email" %}

| 이메일 유형 | 권장 최대 속성 |
| --- | --- | 
| 텍스트만 | 25 KB |
| 이미지가 포함된 텍스트 | 60 KB |
| 이메일 너비 | 600 픽셀 |
{: .reset-td-br-1 .reset-td-br-2}

| 이미지 사양 | 권장 최대 속성 |
| --- | --- | 
| 크기 | 5 MB |
| 폭 | 헤더: 600 픽셀<br>본문: 480 픽셀 |
| 파일 유형 | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2}

| 텍스트 사양 | 권장 최대 속성 |
| --- | --- | 
| 제목 줄 길이 | 35자<br>6~10단어 |
| `"From: Name"` 길이 | 25자 |
| 프리헤더 길이 | 85자 |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "content cards" %}

| 카드 유형 | 종횡비     | 이미지 품질       |
| --------- | ---------------- | ------------------- |
| 클래식   | 1:1 화면비 | 60 x 60 픽셀        |
| 캡션 | 4:3 화면비 | 최소 너비 600 픽셀 |
| 배너    | 모든 종횡비 | 최소 너비 600 픽셀 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

자세한 내용은 [콘텐츠 카드 크리에이티브 세부 정보]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/)를 참조하세요.

{% endif %}