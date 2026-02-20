---
platform: REST APIs
nav_title: Endpoints interactifs
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
  padding-top : 0px ;
}

#main_content \#article-main .block ul>li::before,#main_content \#article-main .block ol>li::before {
  contenu : "" ;
}
#main_content \#article-main #swagger-ui .global-server-container, #main_content \#article-main #swagger-ui .scheme-container {
  background-color : #f4f4f7;  
}

#main_content \#article-main #swagger-ui .opblock-tag {
  border-bottom : 1px solid rgba(59,65,81,.3) ;
}
#main_content \#article-main #swagger-ui .auth-container p {
  margin-bottom : 5px ;
}
#main_content \#article-main #swagger-ui .auth-wrapper {
  -webkit-box-pack : start ;
  -ms-flex-pack : start ;
  justify-content : flex-start ;
}

#main_content \#article-main #swagger-ui .dialog-ux .modal-ux-content {
  padding-top : 0px ;
}
#main_content \#article-main #swagger-ui .auth-container input[type=text]{
  bordure : 1px uni #f4f4f7 ;
  largeur: 100%;

}
#main_content \#article-main #swagger-ui .opblock-tag-section a {
    font-family : "Sailec W00 Bold", Arial, Helvetica, sans-serif ;
    affichage : inline ;
    couleur : #212123;
    largeur de la bordure inférieure : 0px ;
    couleur de la bordure : transparent ;
    décoration du texte : aucune ;
    poids de la police : 700 ;
    transition : all ease .2s ;
    -webkit-transition : all ease .2s ;
    -moz-transition : all ease .2s
}
#main_content \#article-main #swagger-ui .opblock-tag-section .tab a {
  font-family : "Sailec W00 Regular", Arial, Helvetica, sans-serif ;
  poids de la police : 500 ;
}
#main_content \#article-main #swagger-ui .opblock-tag-section .tab .active a {
  font-family : "Sailec W00 Bold", Arial, Helvetica, sans-serif ;
  poids de la police : 700 ;
}
#main_content \#article-main #swagger-ui .opblock-tag-section a:hover {
    couleur de fond : transparent ;
}


\#swagger-ui table, #swagger-ui table td, #swagger-ui table thead, #swagger-ui table tr {
  border : none !important ;
}
\#swagger-ui .model-box {
  largeur: 100%;
}
\#swagger-ui table td.col, #swagger-ui table th.col {
  width : auto !important ;
}
\#swagger-ui table thead {
  arrière-plan : transparent;

}
\#swagger-ui table thead tr td, #swagger-ui table thead tr th {
  border-bottom : 1px solid rgba(59,65,81,.2) !important ;
}

\#swagger-ui .btn.authorize , #swagger-ui .servers select{
  background-color : #ffffff;

}

</style>
<script src="/docs/assets/js/swagger/swagger_ui_bundle.js"> </script>
<script src="/docs/assets/js/swagger/swagger_ui_standalone_preset.js"> </script>
<script>
$(document).ready(function() {

  // Construire un système
  const ui = SwaggerUIBundle({
    url : "/docs/assets/js/swagger/braze_swagger.json",
    dom_id: '#swagger-ui',
    docExpansion: 'none',
    deepLinking: true,
    les préréglages : [
          SwaggerUIBundle.presets.apis,
          SwaggerUIStandalonePreset
      ],
plugins : [
      SwaggerUIBundle.plugins.DownloadUrl
    ],
disposition : "BaseLayout"
})

  window.ui = interface utilisateur ;
});
</script>
