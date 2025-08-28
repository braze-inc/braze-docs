---
nav_title: 워크스페이스 만들기 및 관리
article_title: 워크스페이스 만들기 및 관리
page_order: 0
page_type: reference
description: "이 도움말에서는 워크스페이스를 만들고, 설정하고, 관리하는 방법에 대해 설명합니다."

---

# 작업 공간 만들기 및 관리

> 이 도움말에서는 워크스페이스를 만들고, 설정하고, 관리하는 방법에 대해 설명합니다. 

## 워크스페이스란 무엇인가요?

Braze에서 하는 모든 작업은 작업 공간 내에서 이루어집니다. 위크스페이스는 관련성 있는 모바일 앱이나 웹사이트에 대한 참여를 추적하고 관리할 수 있는 공유 작업 환경입니다. 워크스페이스는 동일하거나 매우 유사한 앱(예: 모바일 앱의 Android 및 iOS 버전)을 함께 그룹화합니다. 

## 작업 공간 만들기

### 1단계: 계획 세우기

시작하기 전에 팀 및 Braze 온보딩 매니저와 협력하여 사용 사례에 가장 적합한 워크스페이스 구성을 결정하세요. To learn more about planning your workspaces in Braze, check out our [Getting Started: Workspaces]({{site.baseurl}}/user_guide/getting_started/workspaces/) guide.

### 2단계: 워크스페이스 추가

전역 헤더의 워크스페이스 드롭다운에서 새 워크스페이스를 만들거나 기존 워크스페이스 간에 전환할 수 있습니다.

1. Select the workspace dropdown, then select <i class="fa-solid fa-square-plus" style="color: #0b8294;"></i> **Create workspace**.

![The workspace dropdown with the "Create workspace" button.]({% image_buster /assets/img/workspaces/workspace_create.png %}){: style="max-width:60%;"}

{:start="2"}
2\. 작업 공간에 이름을 지정하세요.

{% alert tip %}
회사 내 다른 사람들이 내 워크스페이스를 쉽게 찾을 수 있도록 이름 지정 규칙을 채택하는 것이 좋습니다. 예를 들어, 다음과 같습니다. "Upon Voyage US - 제작" 및 "Upon Voyage US - 스테이징".
{% endalert %}

{:start="3"}
3\. **만들기**를 선택합니다. Braze가 워크스페이스를 생성하는 데 몇 초 정도 걸릴 수 있습니다.

!["Create Workspace" modal with the name "Upon Voyage US - Staging".]({% image_buster /assets/img/workspaces/workspace_name.png %}){: style="max-width:60%" }

앱 인스턴스 추가를 시작할 수 있는 **앱 설정** 페이지로 이동합니다. 이 페이지는 **설정** > **앱 설정에서** 언제든지 액세스할 수 있습니다.

!["App Settings" page for the Upon Voyage US - Staging workspace with a button for adding an app.]({% image_buster /assets/img/workspaces/workspace_empty_state.png %})

### 3단계: 앱 인스턴스 추가

워크스페이스 내에서 수집되는 다양한 사이트와 앱을 "앱 인스턴스"라고 합니다.

1. From the **App Settings** page, select **\+ Add app**.
2. 앱 인스턴스의 이름을 지정하고 이 앱 인스턴스가 어떤 플랫폼에 있는지 선택하세요. 여러 플랫폼을 선택하면 Braze는 각 플랫폼에 대해 하나의 앱 인스턴스를 생성합니다.

!["Add New App to Upon Voyage US - Staging" modal with options to select app details.]({% image_buster /assets/img/workspaces/workspace_add_app.png %}){: style="max-width:60%" }

{:start="3"}
3\. Select **Add app** to confirm.

#### 앱 API 키

앱 인스턴스를 추가하면 해당 API 키에 액세스할 수 있습니다. API 키는 앱 인스턴스와 Braze API 간에 요청을 할 때 사용됩니다. API 키는 앱이나 웹사이트와 Braze SDK를 통합하는 데에도 중요합니다.

![Settings page for the Upon Voyage iOS app with fields for the API Key and SDK Endpoint.]({% image_buster /assets/img/workspaces/app_api_key.png %})

{% alert note %}
각 플랫폼에서 앱의 각 버전에 대해 별도의 앱 인스턴스를 생성해야 합니다. 예를 들어 iOS와 Android 모두에 무료 및 프로 버전의 앱이 있는 경우 워크스페이스 내에 4개의 앱 인스턴스(무료 iOS 앱, 무료 Android 앱, 프로 iOS 앱, 프로 Android 앱)를 생성합니다. 이렇게 하면 각 앱 인스턴스에 대해 하나씩 사용할 수 있는 4개의 API 키가 제공됩니다.
{% endalert %}

#### 라이브 SDK 버전

특정 앱의 앱 설정 페이지에 표시되는 라이브 SDK 버전은 일일 총 세션의 5% 이상이고 지난 하루 동안 500회 이상의 세션이 있는 가장 높은 앱 버전입니다.

이 필드는 앱이나 웹사이트에 Braze SDK를 통합한 후에 표시됩니다. 플랫폼에 최신 버전의 Braze SDK를 사용할 수 있는 경우 "최신 버전 사용 가능" 태그가 표시됩니다.

!["Live SDK Version" section with a field value of "5.4.0" and an icon that says a new version is available.]({% image_buster /assets/img/workspaces/app_live_sdk_version.png %})

### 4단계: 필요에 따라 반복

2단계와 3단계를 반복하여 계획에 필요한 만큼의 워크스페이스를 설정하세요. 모범 사례로, 통합 및 캠페인 테스트를 위한 테스트 워크스페이스를 만드는 것이 좋습니다.

{% alert tip %}
**테스트 작업 공간 추가**<br>프로덕션 인스턴스에서 특정 사용자를 완전히 샌드박스화하여 앱 테스트를 수행할 수 있습니다. 새 워크스페이스를 생성하고 애플리케이션을 게시할 때 Braze가 사용하는 API 키를 테스트 워크스페이스가 아닌 프로덕션 워크스페이스의 키와 일치하도록 변경해야 합니다.
{% endalert %}

## 워크스페이스 관리

### 즐겨찾기 추가

즐겨찾는 워크스페이스를 추가하여 가장 자주 사용하는 워크스페이스에 더욱 빠르게 액세스할 수 있습니다.

![Workspace dropdown with the tab for "Favorite workspaces".]({% image_buster /assets/img/workspaces/workspace_favorites.png %}){: style="max-width:50%;"}

즐겨찾는 작업 공간을 추가하려면:

1. 프로필 드롭다운을 선택한 다음 **계정 관리**를 선택합니다.
2. **계정 프로필** 섹션에서 **즐겨찾는 작업 공간** 필드를 찾습니다.
3. 목록에서 워크스페이스를 선택합니다.
4. **변경 사항 저장**을 선택합니다.

즐겨찾기에 추가할 수 있는 워크스페이스 수에는 제한이 없지만, 편의를 위해 이 목록을 짧게 작성하는 것이 좋습니다.

### 워크스페이스 이름 바꾸기

워크스페이스의 이름을 변경하려면,

1. **설정** > **앱 설정으로** 이동합니다.
2. 워크스페이스 이름 위로 마우스를 가져가 <i class="image: /assets/img/braze_icons/pencil-01.svg" style="color: #0b8294;"></i> 을 선택합니다.
3. 워크스페이스에 새 이름을 지정한 다음 <i class="fa-solid fa-square-check" style="color: #0b8294;"></i> **저장을** 선택합니다.

![The pencil icon appearing next to the workspace name.]({% image_buster /assets/img/workspaces/workspace_rename.gif %}){: style="max-width:50%;"}

### Deleting workspaces and app instances

To delete your workspace or app instance:

1. **설정** > **앱 설정으로** 이동합니다.
2. Select **Delete workspace** to delete the respective workspace, or select the trash can icon next to the respective app instance.

You cannot delete app instances or workspaces that are currently being used for targeting users or that have over 1,000 users. If you try to do so, you’ll receive an error message. To proceed and delete them, [create a Support case]({{site.baseurl}}/user_guide/administrative/access_braze/support/) that includes a dashboard link and the name of the app instance or workspace to be deleted.

{% alert warning %}
작업 공간을 삭제할 때는 주의하세요! 워크스페이스가 삭제된 후에는 복원할 수 없습니다.
{% endalert %}

![The App Settings page with a button to delete a workspace and a trash can icon to delete an app.]({% image_buster /assets/img/workspaces/workspace_delete.png %})

## 자주 묻는 질문

### 업데이트된 앱을 출시할 때 새 워크스페이스를 만들어야 하나요?

This depends on whether you're updating your app or creating an entirely new one.

#### Updating your app

If you're updating your app, you should separate the old and new versions by creating a new app instance within the same workspace. 이렇게 하면 세분화 중에 해당 앱을 선택할 때 새 버전의 사용자를 효과적으로 타겟팅할 수 있습니다. 이전 버전을 사용하는 사용자에게 메시지를 보내려면 필터를 사용하여 [이전 앱 버전을 타겟팅할]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions) 수 있습니다.

If you create a new workspace, your users will exist in two places: the old workspace and the new workspace. They could also potentially have the same push token. This can lead to users receiving a marketing message intended for only old workspace users, even if they’ve already upgraded.

#### Releasing a new app

If you're releasing an entirely new app to the app store, you should create a new workspace. 새 워크스페이스를 만들면 이전 앱 버전의 모든 기록 데이터와 고객 프로필이 이 새 워크스페이스에 존재하지 않게 됩니다. 따라서 기존 사용자가 새 앱 버전으로 업그레이드하면 이전 앱의 행동 데이터 없이 새 프로필이 생성됩니다.

### 하나의 워크스페이스에 여러 개의 앱 인스턴스가 있는데 어떻게 하면 메시지로 단일 앱만 타겟팅할 수 있나요? {#singular-app}

메시지가 특정 앱만 타겟팅하도록 하려면 선택한 앱 인스턴스의 사용자만 타겟팅하는 세그먼트를 추가하세요. 이는 사용자가 동일한 워크스페이스에서 서로 다른 앱 인스턴스에 대한 푸시 토큰을 두 개 가지고 있는 경우 특히 중요합니다. 이 시나리오에서 사용자는 현재 사용 중인 앱이 아닌 다른 앱에 대한 알림을 받을 수 있습니다. 이상적인 경험은 아닙니다!

기본적으로 세그먼트는 워크스페이스의 모든 앱과 웹사이트를 대상으로 합니다. 하나의 앱 또는 웹사이트만 타겟팅하는 세그먼트를 설정하려면 다음과 같이 하세요:

1. 의미 있는 이름으로 세그먼트를 만듭니다. Braze에서는 "모든 사용자({이름} {플랫폼})" 형식을 사용합니다. 예: "모든 사용자(Upon Voyage iOS)".
2. **타겟팅하는 앱 및 웹사이트**의 경우 **특정 앱의 사용자**를 선택합니다.
3. **특정 앱** 드롭다운에서 앱 또는 사이트를 선택합니다.

![Segment that is targeting users from specific apps.]({% image_buster /assets/img/workspaces/users_from_specific_apps_filter.png %})

그런 다음 이 세그먼트를 메시지에 추가하고 필요한 경우 추가 세그먼트 및 필터를 사용하여 오디언스를 더욱 세분화할 수 있습니다.

#### 캠페인

For campaigns, add your segment to the **Target Audiences** step of the composer.

#### Canvas

In Canvas, add your segment to your Message steps, in the **Delivery Validations** section. 전달 검증은 메시지 발송 시 오디언스가 전달 기준을 충족했음을 재확인합니다. 각 메시지 단계마다 전달 검증을 지정하여 올바른 앱으로 전달되는지 확인하세요. 엔트리 레벨에서 세분화할 필요가 없습니다.

{% details 원래 캔버스 워크플로우의 단계를 보려면 확장하세요. %}

{% alert important %}
2023년 2월 28일부터 더 이상 원본 편집기를 사용하여 캔버스를 만들거나 복제할 수 없습니다. 이 콘텐츠는 원본 편집기에서 세그먼트와 타겟팅을 이해하는 데 참조할 수 있습니다.<br><br>Braze recommends that customers who use the original Canvas experience clone their Canvases to the updated editor to better build and manage Canvases. Learn more about [cloning your Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

원래 캔버스 워크플로에서 **대상** 섹션의 캔버스 컴포넌트 레벨에 세그먼트를 추가합니다. 엔트리 레벨에서 세분화할 필요가 없습니다.
{% enddetails %}


