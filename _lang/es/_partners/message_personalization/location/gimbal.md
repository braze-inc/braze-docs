---
nav_title: Gimbal
article_title: Gimbal
alias: /partners/gimbal/
description: "Este artículo de referencia describe la asociación entre Braze y Gimbal, que te permite perfeccionar la relevancia de tu marketing utilizando datos de localización."
page_type: partner
search_tag: Partner

---

# Gimbal

> [Gimbal](https://gimbal.com/) te permite perfeccionar la relevancia de tu marketing utilizando datos de localización. Tu SDK de localización, junto con el software de geovallado y las balizas, permite ofrecer experiencias móviles relevantes, personalizadas y cercanas.

Combina tu baliza o geovalla con las funciones de segmentación y mensajería de Braze para obtener más información sobre las acciones físicas de tus usuarios y enviarles mensajes en consecuencia. Esta integración de la asociación abre un abanico de casos de uso para:

- **Marketing:** Envía mensajes contextualmente relevantes y crea recorridos experienciales para los consumidores.
- **Análisis de la competencia:** Establece desencadenantes en torno a ubicaciones competitivas para comprender las tendencias y pautas de consumo.
- **Información sobre la audiencia:** Comprende los comportamientos de visita de tus usuarios y sigue segmentando en función de lo aprendido.

{% alert note %}
Esta integración funciona igual para las balizas Gimbal y las soluciones de geovalla Gimbal.
{% endalert %}

## Requisitos previos

| Requisito| Descripción|
| ---| ---|
| [Cuenta de administrador de Gimbal][1] | Para beneficiarte de esta alianza es necesario disponer de una cuenta de administrador de Gimbal. |
|[SDK de localización de Gimbal](https://docs.gimbal.com/index.html) | El SDK de localización Gimbal potencia las experiencias móviles basadas en macro y microlocalización mediante balizas de proximidad y geovallas que te permiten comunicarte más eficazmente con los usuarios de su aplicación. Debes tener implementado el SDK y configuradas las geovallas (o balizas). |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración de SDK

Para integrar Braze y Gimbal, debes implementar el SDK de localización de Gimbal y crear una cuenta de administrador de Gimbal. Las siguientes integraciones para Android, FireOS e iOS crearán un evento personalizado único para cada nueva ubicación en la que entre un usuario. Estos eventos se pueden utilizar para la activación y el retargeting en tus campañas y Canvases.

Si tienes previsto crear más de 50 ubicaciones, te recomendamos crear un evento personalizado genérico `Places Entered` y añadir el nombre de la ubicación como propiedad del evento. 

1. Integra el [SDK de Gimbal][2] para Android e iOS en tu aplicación siguiendo las instrucciones de la [documentación de Gimbal][3].
2. Utiliza [la API REST][4] de Gimbal para obtener el usuario `places`.
3. Vincula tu cuenta Gimbal a Braze introduciendo la [clave de API REST][5] de Braze.
4. Configura [eventos personalizados][6] en el SDK de Braze. Puedes integrar Gimbal con Braze para [Android y FireOS][7] y [iOS][8].
5. Registra las propiedades de estos eventos (Nombre de la ubicación, Tiempo de permanencia).
6. Utiliza estas propiedades y eventos para activar campañas y Canvas en Braze. 

[1]: https://manager.gimbal.com/login/users/sign_in
[2]: https://manager.gimbal.com/sdk_downloads
[3]: https://docs.gimbal.com/
[4]: https://docs.gimbal.com/rest.html
[5]: https://manager.gimbal.com/apps
[6]: {{site.baseurl}}/user_guide/data_and_analytics/Custom_Data/custom_events/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons