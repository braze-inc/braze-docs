---
platform: REST APIs
nav_title: Pontos de extremidade interativos
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
  preenchimento superior: 0px;
}

#main_content \#article-main .block ul>li::before,#main_content \#article-main .block ol>li::before {
  conteúdo: "";
}
#main_content \#article-main #swagger-ui .global-server-container, #main_content \#article-main #swagger-ui .scheme-container {
  background-color: #f4f4f7;  
}

#main_content \#article-main #swagger-ui  .opblock-tag {
  borda inferior: 1px sólido rgba(59,65,81,.3);
}
#main_content \#article-main #swagger-ui .auth-container p {
  margem inferior: 5px;
}
#main_content \#article-main #swagger-ui .auth-wrapper {
  -webkit-box-pack: início;
  -ms-flex-pack: início;
  justificar conteúdo: flex-start;
}

#main_content \#article-main #swagger-ui .dialog-ux .modal-ux-content {
  preenchimento superior: 0px;
}
#main_content \#article-main #swagger-ui .auth-container input[type=text]{
  border: 1px solid #f4f4f7;
  largura: 100%;

}
#main_content \#article-main #swagger-ui .opblock-tag-section a {
    família de fontes: "Sailec W00 Bold",Arial,Helvetica,sans-serif;
    exibir: inline;
    cor: #212123;
    largura da borda inferior: 0px;
    cor da borda: transparente;
    decoração do texto: nenhum;
    peso da fonte: 700;
    transição: tudo com facilidade .2s;
    -webkit-transição: tudo com facilidade .2s;
    -moz-transição: tudo com facilidade .2s
}
#main_content \#article-main  #swagger-ui .opblock-tag-section .guia a  {
  família de fontes: "Sailec W00 Regular",Arial,Helvetica,sans-serif;
  peso da fonte: 500;
}
#main_content \#article-main  #swagger-ui .opblock-tag-section .guia .ativo a  {
  família de fontes: "Sailec W00 Bold",Arial,Helvetica,sans-serif;
  peso da fonte: 700;
}
#main_content \#article-main #swagger-ui .opblock-tag-section a:hover {
    cor de fundo: transparente;
}


\#swagger-ui tabela, #swagger-ui tabela td, #swagger-ui tabela thead, #swagger-ui tabela tr {
  borda: nenhuma !importante;
}
\#swagger-ui .model-box {
  largura: 100%;
}
\#swagger-ui table td.col, #swagger-ui table th.col  {
  largura: auto !important;
}
\#swagger-ui table thead {
  Fundo: transparente;

}
\#swagger-ui  table thead tr td, #swagger-ui table thead tr th {
  borda inferior: 1px sólido rgba(59,65,81,.2) !important;
}

\#swagger-ui .btn.authorize, #swagger-ui .servers select{
  background-color: #ffffff;

}

</style>
<script src="/docs/assets/js/swagger/swagger_ui_bundle.js"> </script>
<script src="/docs/assets/js/swagger/swagger_ui_standalone_preset.js"> </script>
<script>
$(document).ready(function() {

  // Criar um sistema
  const ui = SwaggerUIBundle({
    url: "/docs/assets/js/swagger/braze_swagger.json",
    dom_id: '#swagger-ui',
    docExpansion: 'nenhum',
    deepLinking: verdadeiro,
    presets: [
          SwaggerUIBundle.presets.apis,
          SwaggerUIStandalonePreset
      ]},
plugins: [
      SwaggerUIBundle.plugins.DownloadUrl
    ]},
layout: "BaseLayout"
})

  window.ui = ui;
});
</script>
