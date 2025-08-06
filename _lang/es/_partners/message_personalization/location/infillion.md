---
nav_title: Infillion
article_title: Infillion
alias: /partners/infillion/
description: ""
page_type: partner
search_tag: Partner

---

# Infillion

>  Tu SDK de localización, junto con el software de geovallado y las balizas, permite ofrecer experiencias móviles relevantes, personalizadas y cercanas.

 Esta integración de la asociación abre un abanico de casos de uso para:

- **Marketing:** Envía mensajes contextualmente relevantes y crea recorridos experienciales para los consumidores.
- **Análisis de la competencia:** Establece desencadenantes en torno a ubicaciones competitivas para comprender las tendencias y pautas de consumo.
- **Información sobre la audiencia:** Comprende los comportamientos de visita de tus usuarios y sigue segmentando en función de lo aprendido.

{% alert note %}

{% endalert %}

## Requisitos previos

| Requisito| Descripción|
| ---| ---|
|  |  |
| |  Debes tener implementado el SDK y configuradas las geovallas (o balizas). |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración de SDK

 Las siguientes integraciones para Android, FireOS e iOS crearán un evento personalizado único para cada nueva ubicación en la que entre un usuario. Estos eventos se pueden utilizar para la activación y el retargeting en tus campañas y Canvases.

Si tienes previsto crear más de 50 ubicaciones, te recomendamos crear un evento personalizado genérico `Places Entered` y añadir el nombre de la ubicación como propiedad del evento. 

1. 
2. 
3. 
4.  
5. Registra las propiedades de estos eventos (Nombre de la ubicación, Tiempo de permanencia).
6. Utiliza estas propiedades y eventos para activar campañas y Canvas en Braze. 

