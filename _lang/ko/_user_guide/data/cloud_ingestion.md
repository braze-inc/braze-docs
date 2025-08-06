---
nav_title: 클라우드 데이터 수집
article_title: Braze 클라우드 데이터 수집
alias: /cloud_ingestion/
description: "이 참조 문서에서는 Braze 클라우드 데이터 수집 소스 및 데이터 설정 권장 사항을 다룹니다."
layout: dev_guide
page_order: 0.1
page_type: landing

guide_top_header: "Braze 클라우드 데이터 수집"
guide_top_text: "<h2>이것은 무엇인가요?</h2>Braze 클라우드 데이터 수집(CDI)을 사용하면 데이터 스토리지 솔루션에서 Braze로 직접 연결하여 관련 사용자 또는 카탈로그 데이터를 동기화하고 사용자를 삭제하도록 설정할 수 있습니다. Braze에 동기화되면 이 데이터를 개인화 또는 세분화와 같은 사용 사례에 활용할 수 있습니다. 클라우드 데이터 수집의 유연한 통합은 중첩된 JSON 및 개체 배열을 포함한 복잡한 데이터 구조를 지원합니다. <br><br>**Braze 클라우드 데이터 수집 기능:**<br> 몇 분안에 데이터 웨어하우스 또는 파일 스토리지 솔루션에서 Braze로 직접 단순 통합을 생성합니다.<br>- 데이터 웨어하우스에서 Braze로 속성, 이벤트 및 구매를 포함한 사용자 데이터를 안전하게 동기화합니다.<br>- 클라우드 데이터 수집을 커런츠 또는 Snowflake 데이터 공유와 결합하여 Braze로 데이터 루프를 닫으세요.<br><br>**클라우드 데이터 수집은 데이터를 동기화할 수 있습니다**:<br> - Amazon Redshift<br> - Databricks<br> - Google BigQuery<br> - Microsoft Fabric<br> - S3<br> Snowflake"

guide_featured_title: "섹션 기사"
guide_featured_list:
  - name: 개요 및 모범 사례
    link: /docs/user_guide/data/cloud_ingestion/overview/
    image: /assets/img/braze_icons/users-01.svg
  - name: 연결된 소스
    link: /docs/user_guide/data/cloud_ingestion/connected_sources/
    image: /assets/img/braze_icons/server-01.svg
  - name: 데이터 웨어하우스 통합
    link: /docs/user_guide/data/cloud_ingestion/integrations/
    image: /assets/img/braze_icons/cloud-blank-01.svg
  - name: 파일 저장 통합
    link: /docs/user_guide/data/cloud_ingestion/file_storage_integrations/
    image: /assets/img/braze_icons/folder.svg 
  - name: 카탈로그 데이터 동기화
    link: /docs/user_guide/data/cloud_ingestion/sync_catalogs_data/
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: CDI로 사용자 삭제
    link: /docs/user_guide/data/cloud_ingestion/delete_users/
    image: /assets/img/braze_icons/trash-01.svg
  - name: 자주 묻는 질문
    link: /docs/user_guide/data/cloud_ingestion/faqs/
    image: /assets/img/braze_icons/annotation-question.svg
---

[1]: {% image_buster /assets/img/cloud_ingestion/ingestion_1.png %}
[2]: {% image_buster /assets/img/cloud_ingestion/ingestion_2.png %}
[3]: {% image_buster /assets/img/cloud_ingestion/ingestion_3.png %}
[4]: {% image_buster /assets/img/cloud_ingestion/ingestion_4.png %}
[5]: {% image_buster /assets/img/cloud_ingestion/ingestion_5.png %}
