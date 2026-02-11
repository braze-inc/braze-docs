---
platform: REST APIs
nav_title: Interaktive Endpunkte
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
  padding-top: 0px;
}

#main_content \#article-main .block ul>li::before,#main_content \#article-main .block ol>li::before {
  Inhalt: "";
}
#main_content \#article-main #swagger-ui .global-server-container, #main_content \#article-main #swagger-ui .scheme-container {
  background-color: #f4f4f7;  
}

#main_content \#article-main #swagger-ui .opblock-tag {
  Rand-unten: 1px solid rgba(59,65,81,.3);
}
#main_content \#article-main #swagger-ui .auth-container p {
  Rand-unten: 5px;
}
#main_content \#article-main #swagger-ui .auth-wrapper {
  -webkit-box-pack: start;
  -ms-flex-pack: Start;
  justify-content: flex-start;
}

#main_content \#article-main #swagger-ui .dialog-ux .modal-ux-content {
  padding-top: 0px;
}
#main_content \#article-main #swagger-ui .auth-container input[type=text]{
  Grenze: 1px solid #f4f4f7;
  Breite: 100%;

}
#main_content \#article-main #swagger-ui .opblock-tag-section a {
    font-family: "Sailec W00 Bold", Arial, Helvetica, sans-serif;
    Anzeige: inline;
    Farbe: #212123;
    border-bottom-width: 0px;
    Rahmen-Farbe: Transparent;
    text-decoration: keine;
    font-weight: 700;
    Übergang: alle Leichtigkeit .2s;
    -webkit-transition: all ease .2s;
    -moz-transition: all ease .2s
}
#main_content \#article-main #swagger-ui .opblock-tag-section .tab a {
  font-family: "Sailec W00 Regular", Arial, Helvetica, sans-serif;
  font-weight: 500;
}
#main_content \#article-main #swagger-ui .opblock-tag-section .tab .active a {
  font-family: "Sailec W00 Bold", Arial, Helvetica, sans-serif;
  font-weight: 700;
}
#main_content \#article-main #swagger-ui .opblock-tag-section a:hover {
    Hintergrundfarbe: transparent;
}


\#swagger-ui table, #swagger-ui table td, #swagger-ui table thead, #swagger-ui table tr {
  border: none !important;
}
\#swagger-ui .model-box {
  Breite: 100%;
}
\#swagger-ui table td.col, #swagger-ui table th.col {
  Breite: auto !important;
}
\#swagger-ui Tabelle thead {
  Hintergrund: transparent;

}
\#swagger-ui table thead tr td, #swagger-ui table thead tr th {
  Rand-unten: 1px solid rgba(59,65,81,.2) !important;
}

\#swagger-ui .btn.authorize, #swagger-ui .server select{
  background-color: #ffffff;

}

</style>
<script src="/docs/assets/js/swagger/swagger_ui_bundle.js"> </script>
<script src="/docs/assets/js/swagger/swagger_ui_standalone_preset.js"> </script>
<script>
$(document).ready(function() {

  // Bauen Sie ein System
  const ui = SwaggerUIBundle({
    url: "/docs/assets/js/swagger/braze_swagger.json",
    dom_id: '#swagger-ui',
    docExpansion: 'keine',
    deepLinking: true,
    Voreinstellungen: [
          SwaggerUIBundle.presets.apis,
          SwaggerUIStandalonePreset
      ],
Plugins: [
      SwaggerUIBundle.plugins.DownloadUrl
    ],
Layout: "BaseLayout"
})

  window.ui = UI;
});
</script>
