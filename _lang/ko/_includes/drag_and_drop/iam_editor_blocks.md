## 인앱 메시지 편집기 블록 사용하기

편집기 블록은 인앱 메시지 **구축** 섹션 아래에 있습니다. 이를 사용하려면 열 안의 편집기 블록을 드래그합니다. 열 너비에 맞게 자동으로 조정됩니다. 각 편집기 블록에는 패딩에 대한 세분화된 제어와 같은 자체 설정이 있습니다. 오른쪽 패널은 선택한 콘텐츠 요소의 속성 패널로 자동 전환됩니다.

## 유형

다음 표에서는 각 편집기 블록 유형을 사용하는 방법을 설명합니다.

| 이름 | 설명 |
| --- | --- |
| 제목 | Enters a title text into the message. |
| 단락  | Enters a paragraph text into the message. |
| 버튼 | 표준 버튼을 추가합니다. 이 블록의 속성을 사용하면 편집, 링크 설정 및 분석 로깅을 수행할 수 있습니다. |
| Radio Button | 사용자가 선택할 수 있는 옵션 목록을 추가합니다. 제출되면 사용자 프로필은 관련 사용자 지정 속성을 기록합니다. |
| 이미지 | [미디어 라이브러리에서]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) 이미지를 삽입합니다. |
| 링크 | Inserts a hyperlink that users can click to navigate to a specified URL. Can be embedded within text or standalone. |
| 공백 | 다른 블록 사이에 공간이나 패딩을 추가합니다. |
| 사용자 지정 코드 | Inserts and runs custom HTML, CSS, or JavaScript for advanced customization.  |
| Phone Capture | Inserts a form field for phone numbers. 제출하면 사용자는 [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) 또는 [WhatsApp 구독 그룹에]({{site.baseurl}}/whatsapp_subscription_groups/) 가입하게 됩니다. |
| 이메일 캡처 | Inserts a form field for email addresses. When submitted, the email address is added to that user's profile in Braze. |
| Dropdown      | Inserts a dropdown with a pre-defined list of items from which users can select one. You can add any custom attribute strings to the list. |
| Checkbox      | Inserts a checkbox. If the user checks the box, the block's attribute is set to `true`. If left unchecked, its attribute is set to `false`. |
| 체크박스 그룹| 사용자는 제시된 여러 선택지 중에서 선택할 수 있습니다. 값은 정의된 배열 커스텀 속성에 설정되거나 추가됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 등록정보

각 편집기 블록의 속성에 대한 자세한 내용은 다음 표에 나와 있습니다.

### 제목 및 단락

| Property | 설명 |
| --- | --- |
| Font family | The font style for the text |
| Font weight | Determines the thickness of the text |
| Font size | Determines the size of the text |
| Line height | 텍스트 줄 사이의 거리를 수정합니다. |
| 문자 간격 | 각 문자 사이의 거리를 수정합니다. |
| Text alignment | 텍스트를 왼쪽, 가운데, 오른쪽 또는 맞춤으로 정렬하도록 이동합니다. |
| Text color | 텍스트의 색상을 수정합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 버튼

| Property | 설명 |
| --- | --- |
| Button width | Modifies the width of the button to be automatic or manual |
| Font family | This is the font style for the text |
| Font weight | Determines the thickness of the text |
| Font size | Determines the size of the text |
| 문자 간격 | 각 문자 사이의 거리를 수정합니다. |
| Button alignment | Moves the button to be left, center, or right-oriented |
| Button text color | Modifies the color of the text on the button |
| 배경색 | Modifies the color of the button's background |
| Border style | Determines the style of the button's border of the button | 
| Border radius | 모서리를 얼마나 둥글게 만들지 결정합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 이미지

| Property | 설명 |
| --- | --- |
| URL | The hosted address for the image |
| Alignment | Moves the image to be left, center, or right-oriented |
| 배경색 | Modifies the color of the image's background |
| Border style | Determines the style of the image's border | 
| Border radius | Determines how round you would like the corners of the image |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link

| Property | 설명 |
| --- | --- |
| Font family | This is the font style for the text |
| Font weight | Determines the thickness of the text |
| 문자 간격 | 각 문자 사이의 거리를 수정합니다. |
| Text color | 텍스트의 색상을 수정합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 공백

| Property | 설명 |
| --- | --- |
| 배경색 | 스페이서의 배경색을 수정합니다. |
| 높이 | 스페이서의 높이를 수정합니다. 스페이서의 크기 조정 핸들을 사용하여 수정할 수도 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Custom code

| Property | 설명 |
| --- | --- |
| 사용자 지정 코드 | 인앱 메시지의 HTML, CSS 및 JavaScript를 추가, 편집 또는 삭제할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Phone capture

| Property | 설명 |
| --- | --- |
| 구독 그룹 | 사용자가 전화번호를 수집하여 가입할 [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) 또는 [WhatsApp 구독 그룹]({{site.baseurl}}/whatsapp_subscription_groups/) (모든 국가의 번호를 수집할 수 있는 옵션 포함) |
| Text alignment | 텍스트를 왼쪽, 가운데, 오른쪽 또는 맞춤으로 정렬하도록 이동합니다. |
| Placeholder text | A placeholder phone number to display |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Email capture

| Property | 설명 |
| --- | --- |
| Font family | The font style for the text |
| Font weight | Determines the thickness of the text |
| Font size | Determines the size of the text |
| Line height | 텍스트 줄 사이의 거리를 수정합니다. |
| Text color | 텍스트의 색상을 수정합니다. |
| 문자 간격 | 각 문자 사이의 거리를 수정합니다. |
| Text alignment | 텍스트를 왼쪽, 가운데, 오른쪽 또는 맞춤으로 정렬하도록 이동합니다. |
| Placeholder text | A placeholder email address to display |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 행동

사용자가 메시징의 버튼, 링크 또는 이미지를 탭할 때 발생하는 동작을 지정할 수 있습니다. [Liquid를]({{site.baseurl}}/liquid/) 사용하여 작업을 개인화할 수도 있습니다. Details for each editor block's actions are provided in the following tables.

### 버튼

| Action | 설명 |
| --- | --- |
| Submit form when button is clicked | Submits the form and performs the selected on-click behavior. Turn this off to only perform the on-click behavior. |
| Set separate behaviors for each platform | Customizes the behavior of the button for each platform separately. |
| On-click behavior | 사용자가 메시지 닫기, 웹 URL 열기, 앱의 특정 페이지로 디링크, 다른 페이지로 이동, [푸시 권한 요청]({{site.baseurl}}/push_primer/) 등 버튼을 클릭할 때 수행할 작업을 결정합니다. |
| Log custom attributes or events | Determines if clicking the button will update the user's profile with custom data. You can also select the identifier for reporting. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 이미지

이미지 사양은 [인앱 메시지 이미지 사양을]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/image_specs/#in-app-messages) 참조하세요.

| Action | 설명 |
| --- | --- |
| Alt text | 이미지가 로드되지 않을 경우 이미지 대신 표시되는 텍스트 사본입니다. Screen readers announce alt text to explain images, so use plain language to provide key information about an image. |
| Submit form when image is clicked | Submits the form and performs the selected on-click behavior. Turn this off to only perform the on-click behavior. |
| Set separate behaviors for each platform | Customizes the behavior of the image for each platform separately. |
| On-click behavior | 사용자가 이미지를 클릭할 때 수행할 작업(예: 메시지 닫기, 웹 URL 열기, 앱의 특정 페이지로 디링크, 다른 페이지로 이동, [푸시 권한 요청]({{site.baseurl}}/push_primer/) 등)을 결정합니다. |
| Log custom attributes or events | Determines if clicking the image will update the user's profile with custom data. You can also select the identifier for reporting. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link

| Action | 설명 |
| --- | --- |
| URL | The hyperlink to navigate to |
| Identifier for Reporting | 보고에 사용할 식별자를 결정합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

