---
platform: REST APIs
nav_title: 대화형 엔드포인트
page_order: 2.5
noindex: true
hidden: true
---

<link rel="stylesheet" type="text/css" href="/docs/assets/css/swagger/swagger_ui.css" >

<div id="swagger-ui"></div>
<style type="text/css">
#swagger-ui .information-container .main a {
  display: none !important;
}

#main_content \#기사 메인 {
  패딩 탑: 0px;
}

#main_content \#기사 메인 .블록 ul>li::before,#main_content \#기사 메인 .블록 ol>li::before {
  콘텐츠: "";
}
#main_content \#기사-메인 #swagger-ui .global-server-container, #main_content \#기사-메인 #swagger-ui .scheme-container { {
  background-color: #f4f4f7;  
}

#main_content \#기사-메인 #스웨거-ui .opblock-tag {
  테두리-하단: 1px 솔리드 RGBA(59,65,81,.3);
}
#main_content \#기사-메인 #스웨거-ui .auth-container p { {
  여백-하단: 5px;
}
#main_content \#기사-메인 #스웨거-ui .auth-wrapper {
  -웹킷-박스-팩: 시작;
  -ms-flex-pack: 시작;
  정정-콘텐츠: 플렉스 시작;
}

#main_content \#기사-메인 #스웨거-ui .dialog-ux .모달-ux-content {
  패딩 탑: 0px;
}
#main_content \#기사 메인 #스웨거-ui .auth-container 입력[유형=텍스트]{
  border: 1px solid #f4f4f7;
  너비: 100%;

}
#main_content \#기사-메인 #스웨거-ui .opblock-tag-section a { {
    글꼴 가족: "Sailec W00 굵게",아랄,헬베티카,산세리프;
    표시: 인라인;
    색상: #212123;
    테두리-하단-폭: 0px;
    테두리 색상: 투명;
    텍스트 장식: 없음;
    글꼴 무게: 700;
    전환: 모두 쉽게 0.2초;
    -웹킷-전환: 모두 0.2초;
    -moz-transition: 모두 쉽게 .2초
}
#main_content \#기사-메인 #스웨거-ui .op블록-태그-섹션 .탭 a { {
  글꼴 가족: "Sailec W00 Regular",아랄,헬베티카,산세리프;
  글꼴 무게: 500;
}
#main_content \#기사-메인 #스웨거-ui .op블록-태그-섹션 .탭 .활성 a {
  글꼴 가족: "Sailec W00 굵게",아랄,헬베티카,산세리프;
  글꼴 무게: 700;
}
#main_content \#기사-메인 #스웨거-ui .opblock-tag-section a:hover { {
    배경색: 투명;
}


\#swagger-ui table, #swagger-ui table td, #swagger-ui table thead, #swagger-ui table tr { {
  테두리: 없음 !중요;
}
\#스웨거-ui .model-box {
  너비: 100%;
}
\#스웨거-ui 테이블 td.col, #swagger-ui 테이블 th.col {
  너비: 자동 !중요;
}
\#swagger-ui 테이블 thead {
  배경: 투명;

}
\#swagger-ui 테이블 thead tr td, #swagger-ui 테이블 thead tr th {
  테두리-하단: 1px solid rgba(59,65,81,.2) !중요;
}

\#swagger-ui .btn.authorize , #swagger-ui .servers select{
  background-color: #ffffff;

}

</style>
<script src="/docs/assets/js/swagger/swagger_ui_bundle.js"> </script>
<script src="/docs/assets/js/swagger/swagger_ui_standalone_preset.js"> </script>
<script>
$(document).ready(function() {

  // 시스템 구축
  const ui = SwaggerUIBundle({
    URL: "/docs/assets/js/swagger/braze_swagger.json",
    dom_id: '#swagger-ui',
    문서 확장: '없음',
    딥링킹: true,
    사전 설정: [
          SwaggerUIBundle.presets.apis,
          스웨거UIS독립형 프리셋
      ],
플러그인: [
      SwaggerUIBundle.plugins.DownloadUrl
    ],
레이아웃: "BaseLayout"
})

  window.ui = ui;
});
</script>
