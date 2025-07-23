## Google Play 개인정보 질문서 {#privacy-questionnaire}

2022년 4월부터 Android 개발자는 Google Play의 [데이터 안전 양식](https://support.google.com/googleplay/android-developer/answer/10787469)을 작성하여 개인정보 및 보안 관행을 공개해야 합니다. 이 가이드는 Braze가 앱 데이터를 처리하는 방법에 대한 정보와 함께 이 새 양식을 작성하는 방법에 대한 지침을 제공합니다. 

앱 개발자는 Braze에 전송하는 데이터를 직접 관리할 수 있습니다. Braze가 수신한 데이터는 사용자의 지침에 따라 처리됩니다. Google은 이를 [서비스 제공업체로](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en#zippy=%2Cwhat-kinds-of-activities-can-service-providers-perform) 분류합니다. 

{% alert important %}
이 문서에서는 Google 안전 섹션 설문조사와 관련하여 Braze SDK가 처리하는 데이터와 관련된 정보를 제공합니다. 이 문서는 법률 자문을 제공하지 않으므로 Google에 정보를 제출하기 전에 법무팀과 상담하는 것이 좋습니다.
{% endalert %}

### 질문

|질문|Braze SDK에 대한 답변|
|---|---|
|앱에서 필수 사용자 데이터 유형을 수집하거나 공유하나요?|예. Braze Android SDK는 앱 개발자가 구성한 대로 데이터를 수집합니다. |
|앱에서 수집한 모든 사용자 데이터는 전송 중에 암호화되나요?|예.|
|사용자가 자신의 데이터 삭제를 요청할 수 있는 방법을 제공하나요?|예.|

사용자의 데이터 및 삭제 요청 처리에 대한 자세한 내용은 [Braze 데이터 유지 정보]({{site.baseurl}}/api/data_retention/)를 참조하세요.

### 데이터 수집

Braze에서 수집하는 데이터는 특정 통합 및 수집하기로 선택한 사용자 데이터에 따라 결정됩니다. Braze가 기본적으로 수집하는 데이터와 특정 속성을 비활성화하는 방법에 대해 자세히 알아보려면 [SDK 데이터 수집 옵션]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#minimum-integration)을 참조하세요.

<table id="datatypes">
    <thead>
        <tr>
            <th width="25%">카테고리</th>
            <th width="25%">데이터 유형</th>
            <th width="50%">Braze 사용</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">위치</td>
            <td>대략적인 위치</td>
            <td rowspan="15">기본적으로 수집되지 않습니다.</td>
        </tr>
        <tr>
            <td>정확한 위치</td>
        </tr>
        <tr>
            <td rowspan="9">개인 정보</td>
            <td>이름</td>
        </tr>
        <tr>
            <td>이메일 주소</td>
        </tr>
        <tr>
            <td>사용자 ID</td>
        </tr>
        <tr>
            <td>주소</td>
        </tr>
        <tr>
            <td>전화번호</td>
        </tr>
        <tr>
            <td>인종 및 민족</td>
        </tr>
        <tr>
            <td>정치적 또는 종교적 신념</td>
        </tr>
        <tr>
            <td>성적 취향</td>
        </tr>
        <tr>
            <td>기타 정보</td>
        </tr>
        <tr>
            <td rowspan="4">재무 정보</td>
            <td>사용자 결제 정보</td>
        </tr>
        <tr>
            <td>구매 내역</td>
        </tr>
        <tr>
            <td>신용 점수</td>
        </tr>
        <tr>
            <td>기타 재무 정보</td>      
        </tr>
        <tr>
            <td rowspan="2">건강 및 피트니스</td>
            <td>건강 정보</td>
            <td rowspan="2">기본적으로 수집되지 않습니다.</td>
        </tr>
        <tr>
            <td>피트니스 정보</td>     
        </tr>
        <tr>
            <td rowspan="3">메시지</td>
            <td>이메일</td>
            <td rowspan="2">기본적으로 수집되지 않습니다.</td>
        </tr>
        <tr>
            <td>SMS 또는 MMS</td>          
        </tr>
        <tr>
            <td>기타 인앱 메시지</td>
            <td>Braze를 통해 인앱 메시지 또는 푸시 알림을 보내는 경우, 당사는 사용자가 이러한 메시지를 열거나 읽은 시점에 대한 정보를 수집합니다.</td>
        </tr>
        <tr>
            <td rowspan="2">사진 및 동영상</td>
            <td>사진</td>
            <td rowspan="8">수집되지 않습니다.</td>
        </tr>
        <tr>
            <td>동영상</td>
        </tr>
        <tr>
            <td rowspan="3">오디오 파일</td>
            <td>음성 또는 사운드 녹음</td>
        </tr>        
        <tr>
            <td>음악 파일</td>
        </tr>
        <tr>
            <td>기타 오디오 파일</td>
        </tr>
        <tr>
            <td>파일 및 문서</td>
            <td>파일 및 문서</td>
        </tr>
        <tr>
            <td>캘린더</td>
            <td>캘린더 이벤트</td>
        </tr>
        <tr>
            <td>연락처</td>
            <td>연락처</td>
        </tr>
        <tr>
            <td rowspan="5">앱 활동</td>
            <td>앱 상호 작용</td>
            <td>Braze는 기본적으로 세션 활동 데이터를 수집합니다. 다른 모든 상호 작용과 활동은 앱의 커스텀 통합에 의해 결정됩니다.</td>
        </tr>
        <tr>
            <td>앱 내 검색 기록</td>
            <td>수집되지 않습니다.</td>            
        </tr>
        <tr>
            <td>설치된 앱</td>
            <td>수집되지 않습니다.</td>            
        </tr>
        <tr>
            <td>기타 사용자 제작 콘텐츠</td>
            <td rowspan="2">기본적으로 수집되지 않습니다.</td>            
        </tr>
        <tr>
            <td>기타 작업</td>
        </tr>
        <tr>
            <td>웹 브라우징</td>
            <td>웹 검색 기록</td>
            <td>수집되지 않습니다.</td>
        </tr>
        <tr>
            <td rowspan="3">앱 정보 및 성능</td>
            <td>충돌 로그</td>
            <td>Braze는 SDK 내에서 발생하는 오류에 대한 크래시 로그를 수집합니다. 여기에는 사용자의 휴대폰 모델 및 OS 수준과 Braze 특정 사용자 ID가 포함됩니다.</td>
        </tr>
        <tr>
            <td>진단</td>
            <td>수집되지 않습니다.</td>            
        </tr>
        <tr>
            <td>기타 앱 성능 데이터</td>
            <td>수집되지 않습니다.</td>
        </tr>
        <tr>
            <td>장치 또는 기타 ID</td>
            <td>장치 또는 기타 ID</td>
            <td>Braze는 사용자의 기기를 구분하기 위해 기기 ID를 생성하고, 메시지가 의도한 기기로 제대로 전송되었는지 확인합니다.</td>
        </tr>
    </tbody>
</table>

Braze가 수집하는 기타 디바이스 데이터 중 Google Play 데이터 안전 가이드라인의 범위를 벗어날 수 있는 데이터에 대해 자세히 알아보려면 [Android 스토리지 개요]({{site.baseurl}}/developer_guide/storage/?tab=android) 및 [SDK 데이터 수집 옵션]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#minimum-integration)을 참조하세요.

## 데이터 추적 비활성화

Android SDK에서 데이터 추적 활동을 비활성화하려면 [`disableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html) 메서드를 사용하세요. 이로 인해 모든 네트워크 연결이 취소되며, Braze SDK는 더 이상 Braze 서버에 데이터를 전송하지 않습니다.

## 이전에 저장된 데이터 삭제

장치에 저장된 모든 클라이언트 측 데이터를 완전히 지우려면 [`wipeData()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html) 메서드를 사용할 수 있습니다.

## 데이터 추적 재개

데이터 수집을 재개하려면 [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html) 메서드를 사용할 수 있습니다. 이 점을 염두에 두세요. 이는 이전에 삭제된 데이터를 복원하지 않습니다.
