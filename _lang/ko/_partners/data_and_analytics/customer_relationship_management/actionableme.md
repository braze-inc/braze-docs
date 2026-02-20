---
nav_title: actionable.me
article_title: actionable.me
description: "This reference article outlines the partnership between Braze and actionable.me, a proprietary software and processes, that allow you to get the most out of your Braze investment right away."
alias: /partners/actionableme/
page_type: partner
search_tag: Partner

---

# actionable.me

> [actionable.me](https://actionable.me), built by the team at Massive Rocket, a data and CRM agency, is a standardized and automated approach to running CRM programs, providing tools and processes designed to get Braze customers to value quickly, consistently, and predictably. 

_This integration is maintained by actionable.me._

## 통합 정보

The Braze and actionable.me integration allows you to deploy a service to monitor your progress in the utilization of Braze. Through a combination of tools and processes, they will rapidly benchmark your CRM performance, identify new opportunities and provide recommendations on how to perform better.

## Prerequisites

| Requirement | Description |
| --- | --- |
| actionable.me account | An actionable.me account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with the permissions listed in the next section.<br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

To integrate Braze and actionable.me, the actionable.me platform must be configured, and a Braze API key needs to be created in Braze and configured in the actionable.me dashboard.

### Step 1: Create your Braze API Key

In Braze, navigate to **Settings** > **API Keys**. Select **Create New API Key** and ensure following permissions are added:

- `campaigns.list`
- `campaigns.data_series`
- `campaigns.details`
- `sends.data_series`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `events.list`
- `canvas.list`
- `canvas.data_series`
- `canvas.details`
- `canvas.data_summary`
- `kpi.mau.data_series`
- `kpi.dau.data_series`
- `kpi.new_users.data_series`
- `kpi.uninstalls.data_series`

### Step 2: Provide information to the actionable.me team

통합을 완료하려면 REST API 키와 [REST 엔드포인트 URL을]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) actionable.me 운영팀에 제공해야 합니다. 그러면 actionable.me 에서 연결을 설정하고 설정이 완료된 후 연락하여 인사이트 공유를 시작할 수 있도록 안내합니다.

![actionable.me 운영팀에서 구성할 actionable.me "플랫폼 추가" 페이지입니다.]({% image_buster /assets/img/actionableme/image2.png %})

## 문제 해결

Contact the actionable.me or Massive Rocket team for additional support: [info@massiverocket.com](mailto:info@massiverocket.com)


