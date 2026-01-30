---
platform: REST APIs
nav_title: Puntos finales interactivos
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

#main_content \#artículo-principal {
  acolchado-top: 0px;
}

#main_content \#article-main .block ul>li::before,#main_content \#article-main .block ol>li::before {
  contenido: "";
}
#main_content \#article-main #swagger-ui .global-server-container, #main_content \#article-main #swagger-ui .scheme-container {
  background-color: #f4f4f7;  
}

#main_content \#article-main #swagger-ui .opblock-tag {
  borde inferior: 1px solid rgba(59,65,81,.3);
}
#main_content \#article-main #swagger-ui .auth-container p {
  margen inferior: 5px;
}
#main_content \#article-main #swagger-ui .auth-wrapper {
  -webkit-box-pack: inicio;
  -ms-flex-pack: inicio;
  justify-content: flex-start;
}

#main_content \#article-main #swagger-ui .dialog-ux .modal-ux-content {
  acolchado-top: 0px;
}
#main_content \#article-main #swagger-ui .auth-container input[type=text]{
  border: 1px solid #f4f4f7;
  anchura: 100%;

}
#main_content \#article-main #swagger-ui .opblock-tag-section a {
    font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;
    visualización: en línea;
    color: #212123;
    ancho del borde inferior: 0px;
    color del borde: transparente;
    decoración del texto: ninguna;
    font-weight: 700;
    transición: todo facilidad .2s;
    -webkit-transición: todo facilidad .2s;
    -moz-transición: todo facilidad .2s
}
#main_content \#article-main #swagger-ui .opblock-tag-section .pestaña a {
  font-family: "Sailec W00 Regular",Arial,Helvetica,sans-serif;
  font-weight: 500;
}
#main_content \#article-main #swagger-ui .opblock-tag-section .pestaña .active a {
  font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;
  font-weight: 700;
}
#main_content \#article-main #swagger-ui .opblock-tag-section a:hover {
    color de fondo: transparente;
}


\#swagger-ui table, #swagger-ui table td, #swagger-ui table thead, #swagger-ui table tr {
  borde: ninguno !importante;
}
\#swagger-ui .model-box {
  anchura: 100%;
}
\#swagger-ui tabla td.col, #swagger-ui tabla th.col {
  width: auto !important;
}
\#swagger-ui table thead {
  fondo: transparente;

}
\#swagger-ui table thead tr td, #swagger-ui table thead tr th {
  borde inferior: 1px solid rgba(59,65,81,.2) !important;
}

\#swagger-ui .btn.authorize , #swagger-ui .servers select{
  background-color: #ffffff;

}

</style>
<script src="/docs/assets/js/swagger/swagger_ui_bundle.js"> </script>
<script src="/docs/assets/js/swagger/swagger_ui_standalone_preset.js"> </script>
<script>
$(document).ready(function() {

  // Construye un sistema
  const ui = SwaggerUIBundle({
    url: "/docs/assets/js/swagger/braze_swagger.json",
    dom_id: \#swagger-ui
    docExpansion: 'ninguna',
    deepLinking: true,
    preajustes: [
          SwaggerUIBundle.presets.apis,
          SwaggerUIStandalonePreset
      ],
plugins: [
      SwaggerUIBundle.plugins.DownloadUrl
    ],
diseño: "BaseLayout"
})

  window.ui = ui;
});
</script>
