---
nav_title: Infillion
article_title: Infillion
alias: /partners/infillion/
description: "Este artículo de referencia describe la asociación entre Braze e Infillion, que te habilita para perfeccionar la relevancia de tu marketing utilizando datos de ubicación."
page_type: partner
search_tag: Partner

---

# Infillion

> [Infillion](https://infillion.com/) te habilita para perfeccionar la relevancia de tu marketing utilizando datos de ubicación. Tu SDK de localización, junto con el software de geovallado y las balizas, permite ofrecer experiencias móviles relevantes, personalizadas y cercanas.

Combina tu baliza o soporte de geovalla con las características de segmentación y mensajería de Braze para conocer mejor las acciones físicas de tu usuario y enviarle mensajes en consecuencia. Esta integración de la asociación abre un abanico de casos de uso para:

- **Marketing:** Envía mensajes contextualmente relevantes y crea recorridos experienciales para los consumidores.
- **Análisis de la competencia:** Establece desencadenantes en torno a ubicaciones competitivas para comprender las tendencias y pautas de consumo.
- **Información sobre la audiencia:** Comprende los comportamientos de visita de tus usuarios y sigue segmentando en función de lo aprendido.

{% alert note %}
Esta integración funciona igual para las balizas Infillion y las soluciones de geovalla Infillion.
{% endalert %}

## Requisitos previos

| Requisito| Descripción|
| ---| ---|
| [Administrador de cuentas Infillion](https://manager.gimbal.com/login/users/sign_in) | Se necesita una cuenta de administrador de Infillion para beneficiarse de esta asociación. |
|[SDK de ubicación Infillion](https://docs.gimbal.com/index.html) | El SDK de ubicación de Infillion impulsa experiencias móviles basadas en macro y micro ubicaciones utilizando balizas de proximidad y geovallas que te permiten comunicarte más eficazmente con los usuarios de tu aplicación. Debes tener implementado el SDK y configuradas las geovallas (o balizas). |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración de SDK

Para integrar Braze e Infillion, debes implementar el SDK de ubicación de Infillion y crear una cuenta de administrador de Infillion. Las siguientes integraciones para Android, FireOS e iOS crearán un evento personalizado único para cada nueva ubicación en la que entre un usuario. Estos eventos se pueden utilizar para la activación y el retargeting en tus campañas y Canvases.

Si tienes previsto crear más de 50 ubicaciones, te recomendamos crear un evento personalizado genérico `Places Entered` y añadir el nombre de la ubicación como propiedad del evento. 

1. Integra el [SDK de Infillion](https://manager.gimbal.com/sdk_downloads) para Android e iOS en tu aplicación siguiendo las instrucciones de la [documentación de Infillion](https://docs.gimbal.com/).
2. Utiliza [la API REST del sitio](https://docs.gimbal.com/rest.html) de Infillion para obtener el usuario `places`.
3. Vincula tu cuenta de Infillion a Braze introduciendo la [clave de API REST](https://manager.gimbal.com/apps) de Braze.
4. Configura [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) en el SDK de Braze. Puedes integrar Infillion con Braze para [Android y FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons) e [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons).
5. Registra las propiedades de estos eventos (Nombre de la ubicación, Tiempo de permanencia).
6. Utiliza estas propiedades y eventos para activar campañas y Canvas en Braze. 

