---
nav_title: 푸시 권한 재설정
article_title: 푸시 권한 재설정
page_type: solution
description: "이 도움말 문서에서는 브라우저 푸시 권한 및 데이터를 재설정하는 방법을 다룹니다."
channel: push
---

# 푸시 권한 재설정

브라우저에서 푸시 알림에 문제가 있는 경우 사이트의 알림 권한을 재설정하고 사이트의 저장소를 지워야 할 수 있습니다. 이 단계들을 참조하여 도움을 받으세요.

## 데스크탑에서 Chrome 재설정

1. Chrome 브라우저에서 URL 옆에 있는 **사이트 정보 보기** 슬라이더 아이콘을 클릭하세요.
2. 알림에서, **권한 재설정**을 클릭하십시오.
3. Chrome 개발자 도구를 엽니다. 다음은 운영 체제별 관련 단축키입니다.

<style> 
table {
    max-width: 50%;
}
</style>

| OS      | 키보드 단축키                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="4"}
4\. DevTools에서 **Application** 탭으로 이동합니다.
5\. 사이드바에서 **스토리지**를 선택합니다.
6\. **사이트 데이터 지우기**를 클릭합니다.
7\. Chrome은 업데이트된 설정을 적용하기 위해 페이지를 새로 고치도록 요청할 것입니다. **새로고침**을 클릭합니다.

귀하의 푸시 권한이 이제 재설정되었습니다. 새 탭을 열어 사이트에 접속하여 시도해 보세요.

## Android에서 Chrome 재설정

사이트에서 Android 알림 드로어에 알림이 표시되는 경우:

1. 푸시 알림에서 <i class="fas fa-cog" title="설정"></i>을(를) 탭하고 **사이트 설정**을(를) 선택합니다.
2. **사이트 설정**에서 **지우기 및 재설정**을 탭하세요.

사이트에서 알림을 열지 않은 경우:

1. Android에서 Chrome을 여세요.
2. <i class="fas fa-ellipsis-vertical"></i> 메뉴를 누르세요.
3. **설정** > **사이트 설정** > **알림**로 이동하십시오.
4. 알림이 "보내기 전에 묻기(권장)"로 설정되어 있는지 확인하십시오.
5. 목록에서 귀하의 사이트를 찾으세요.
6. 항목을 선택하고 **지우기 및 재설정**을 탭하세요.

귀하의 푸시 권한이 이제 재설정되었습니다. 새 탭을 열어 사이트에 접속하여 시도해 보세요.

## 데스크톱에서 Firefox 재설정

1. 사이트 URL 옆에 <i class="fa-solid fa-circle-info" alt="info icon"></i> 또는 <i class="fas fa-lock" alt="lock icon"></i>을 클릭하세요.
2. **권한**에서 **알림 받기** 옆에 있는 <i class="fa-solid fa-circle-xmark" title="이 권한을 지우고 다시 요청"></i>을 선택하여 알림 권한을 지웁니다.
3. 같은 메뉴에서 **쿠키 및 사이트 데이터 지우기**를 선택합니다.
4. 대화 상자가 나타나 선택을 확인합니다. **확인**을 클릭합니다.

귀하의 푸시 권한이 이제 재설정되었습니다. 새 탭을 열어 사이트에 접속하여 시도해 보세요.

## Android에서 Firefox 재설정

Android에서 푸시 권한을 재설정하려면 이 [Mozilla 지원 문서](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser)를 참조하세요.

## MacOS에서 Safari 재설정

{% alert note %}
이 단계는 MacOS 전용입니다. Apple은 Windows의 Safari에 대해 웹 푸시를 지원하지 않기 때문입니다.
{% endalert %}

1. Safari를 여세요.
2. Mac의 [메뉴 막대](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac)에서 **Safari** > **설정** > **웹사이트** > **알림**으로 이동합니다.
3. 목록에서 사이트를 선택하세요.
4. **제거**를 클릭하여 사이트의 알림 권한을 삭제합니다.
5. 그런 다음, **개인정보 보호** > **웹사이트 데이터 관리**로 이동합니다.
6. 목록에서 사이트를 선택하세요.
7. **제거**를 클릭하거나 모든 사이트 데이터를 제거하려면 **모두 제거**를 클릭합니다.
8. **완료**를 클릭합니다.

귀하의 푸시 권한이 이제 재설정되었습니다. 새 탭을 열어 사이트에 접속하여 시도해 보세요.


*마지막 업데이트 날짜: 2024년 2월 12일*