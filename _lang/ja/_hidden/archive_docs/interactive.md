---
platform: REST APIs
nav_title: 対話型エンドポイント
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

#main_content \#article-main {
  パディングトップ:0px;
}

#main_content \#article-main .ブロック ul>li::before,#main_content \#article-main .ブロック ol>li::before {
  内容:"";
}
#main_content \#article-main #swagger-ui .global-server-container, #main_content \#article-main #swagger-ui .scheme-container {
  background-color: #f4f4f7;  
}

#main_content \#article-main #swagger-ui  .opブロック-タグ {
  ボーダーボトム:1px固体rgba(59,65,81,.3);
}
#main_content \#article-main #swagger-ui .auth-container p {
  下余白:5px;
}
#main_content \#article-main #swagger-ui .auth-wrアプリer {
  -webkit-box-pack: start;
  -ms-flex-pack: start;
  justify-content: flex-start;
}

#main_content \#article-main #swagger-ui .dialog-ux .モーダル-ux-content {
  パディングトップ:0px;
}
#main_content \#article-main #swagger-ui .auth-container input[type=text]{
  境界線:1px solid #f4f4f7;
  幅:100%;

}
#main_content \#article-main #swagger-ui .opブロック-タグ-section a {
    font-family:"Sailec W00 Bold",Arial,Helvetica,sans-serif;
    display: インライン。
    色: #212123;
    ボーダーボトム幅:0px;
    境界色:透明。
    テキスト装飾: なし。
    フォントの重み:700;
    transition: all ease .2s;
    -webkit-transition: すべてease .2s;
    -moz-transition: all ease .2s
}
#main_content \#article-main  #swagger-ui .opブロック-タグ-section .tab a  {
  font-family:"Sailec W00 Regular",Arial,Helvetica,sans-serif;
  フォントの重み:500;
}
#main_content \#article-main  #swagger-ui .opブロック-タグ-section .tab .active a  {
  font-family:"Sailec W00 Bold",Arial,Helvetica,sans-serif;
  フォントの重み:700;
}
#main_content \#article-main #swagger-ui .opブロック-タグ-section a:hover {
    バックグラウンド色:透明
}


\#swagger-ui table, #swagger-ui table td, #swagger-ui table thead, #swagger-ui table tr {
  境界: なし!重要。
}
\#swagger-ui .model-box {
  幅:100%;
}
\#swagger-ui table td.col, #swagger-ui table th.col  {
  width: auto !important;
}
\#swagger-ui table thead {
  バックグラウンド：透明；

}
\#swagger-ui  table thead tr td, #swagger-ui table thead tr th {
  ボーダーボトム:1px ソリッドrgba(59,65,81,.2) !重要。
}

\#swagger-ui .btn.authorize , #swagger-ui .servers select{
  background-color: #ffffff;

}

</style>
<script src="/docs/assets/js/swagger/swagger_ui_bundle.js"> </script>
<script src="/docs/assets/js/swagger/swagger_ui_standalone_preset.js"> </script>
<script>
$(document).ready(function() {

  // システムを構築する
  const ui = SwaggerUIBundle({
    url: "/docs/assets/js/swagger/braze_swagger.json",
    dom_id: '#swagger-ui'、
    docExpansion: 'none',
    deepLinking: true,
    プリセット: [
          SwaggerUIBundle.presets.apis,
          SwaggerUIStandalonePreset
      ],
プラグイン: [
      SwaggerUIBundle.plugins.DownloadUrl
    ],
レイアウト"BaseLayout"
})

  window.ui = ui;
});
</script>
