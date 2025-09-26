---
nav_title: 편집기 블록
article_title: "인앱 메시지 편집기 블록"
description: "이 참조 문서에서는 인앱 메시지 드래그 앤 드롭 편집기에서 사용할 수 있는 편집기 블록에 대해 설명합니다."
alias: "/editor_blocks_dnd_iam/"
page_order: 5
---

# 인앱 메시지 편집기 블록

> 편집기 블록은 **빌드** 섹션의 **드래그 앤 드롭 편집기**에서 사용할 수 있는 다양한 블록입니다. 이 섹션에는 메시지에서 사용할 수 있는 다양한 종류의 콘텐츠를 나타내는 일련의 타일이 포함되어 있습니다.

## How to use editor blocks

이를 사용하려면 열 안의 편집기 블록을 드래그합니다. 열 너비에 맞게 자동으로 조정됩니다. 각 편집기 블록에는 패딩에 대한 세분화된 제어와 같은 자체 설정이 있습니다. 오른쪽 패널은 선택한 콘텐츠 요소의 속성 패널로 자동 전환됩니다.

### 유형

다음 표에서는 각 편집기 블록 유형을 사용하는 방법을 설명합니다.

| 이름 | 설명 |
| --- | --- |
| 제목 | Enters a title text into the message. |
| 단락  | Enters a paragraph text into the message. |
| 버튼 | 표준 버튼을 추가합니다. 이 블록의 속성을 사용하면 편집, 링크 설정 및 분석 로깅을 수행할 수 있습니다. |
| Radio Button | Adds a list of options from which users can select one. When submitted, the user profile logs the associated custom attribute. |
| 이미지 | Inserts an image from the media library. |
| Link | Inserts a hyperlink that users can click to navigate to a specified URL. Can be embedded within text or standalone. |
| 공백 | 다른 블록 사이에 공간이나 패딩을 추가합니다. |
| 사용자 지정 코드 | Inserts and runs custom HTML, CSS, or JavaScript for advanced customization.  |
| Phone Capture | Inserts a form field for phone numbers. When submitted, the user is subscribed to the SMS or WhatsApp subscription group. |
| Email Capture | Inserts a form field for email addresses. When submitted, the email address is added to that user's profile in Braze. |
| Dropdown      | Inserts a dropdown with a pre-defined list of items from which users can select one. You can add any custom attribute strings to the list. |
| Checkbox      | Inserts a checkbox. If the user checks the box, the block's attribute is set to `true`. If left unchecked, its attribute is set to `false`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Actions

Details for each editor block's actions are provided in the following tables.

### 버튼

| Action | 설명 |
| --- | --- |
| Submit form when button is clicked | Submits the form and performs the selected on-click behavior. Turn this off to only perform the on-click behavior. |
| Set separate behaviors for each platform | Customizes the behavior of the button for each platform separately. |
| On-click behavior | Determines the action when the user clicks the button, such as closing the message, opening the web URL, deeplinking into a specific page of the app, going to another page, or requesting push permission. |
| Log custom attributes or events | Determines if clicking the button will update the user's profile with custom data. You can also select the identifier for reporting. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 이미지

| Action | 설명 |
| --- | --- |
| Alt text | 이미지가 로드되지 않을 경우 이미지 대신 표시되는 텍스트 사본입니다. Screen readers announce alt text to explain images, so use plain language to provide key information about an image. |
| Submit form when image is clicked | Submits the form and performs the selected on-click behavior. Turn this off to only perform the on-click behavior. |
| Set separate behaviors for each platform | Customizes the behavior of the image for each platform separately. |
| On-click behavior | Determines the action when the user clicks the image, such as closing the message, opening the web URL, deeplinking into a specific page of the app, going to another page, or requesting push permission. |
| Log custom attributes or events | Determines if clicking the image will update the user's profile with custom data. You can also select the identifier for reporting. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link

| Action | 설명 |
| --- | --- |
| URL | The hyperlink to navigate to
| Identifier for Reporting | Determines what identifier is used for reporting. |
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
| Subscription group | The SMS or WhatsApp subscription group that the user will be subscribed to by collecting their phone number, with an option to collect numbers from all countries |
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
