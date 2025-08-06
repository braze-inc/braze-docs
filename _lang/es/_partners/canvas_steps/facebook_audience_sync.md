---
nav_title: Facebook
article_title: Sincronización de la audiencia de Canvas con Facebook
description: "En este artículo de referencia se explica cómo utilizar Braze Audience Sync con Facebook para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más."
page_order: 2
alias: "/audience_sync_facebook/"

Tool:
  - Canvas

---

# Sincronización de audiencias con Facebook

> 

 



- 
- Reorientar a los usuarios menos receptivos a otros canales de marketing.
- Crear audiencias de supresión para evitar que los usuarios reciban anuncios cuando ya son consumidores fieles de tu marca.
- 

Esta característica permite a las marcas controlar qué datos propios específicos se comparten con Facebook. En Braze, se presta la máxima atención a las integraciones con las que puedes y no puedes compartir tus datos propios. Para más información, consulta nuestra [política de privacidad](https://www.braze.com/privacy).

## Consideraciones sobre la sincronización de usuarios y el límite de velocidad
 
 Lo que esto significa en la práctica es que Braze intentará procesar por lotes el mayor número de usuarios cada 5 segundos antes de enviarlos a Facebook. 

 Si un cliente Braze alcanza este límite de velocidad, Braze Canvas reintentará la sincronización durante un máximo de ~13 horas. Si la sincronización no es posible, estos usuarios aparecen en la métrica Usuarios erróneos.

## Requisitos previos

 

| Requisito | Origin | Descripción |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook][1] | Una herramienta centralizada para administrar los activos de Facebook de tu marca (por ejemplo, cuentas de anuncios, páginas y aplicaciones). |
| Cuenta publicitaria de Facebook | [Facebook][2] | Una cuenta de anuncios de Facebook activa vinculada al administrador de la empresa de tu marca.<br><br> Asegúrate también de que has aceptado los términos y condiciones de tu cuenta publicitaria. |
| Términos de los públicos personalizados de Facebook | [Facebook][3] | Acepta las Condiciones de públicos personalizados de Facebook para las cuentas de anuncios de Facebook que piensas utilizar con Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integración

### Paso 1: Conéctate a Facebook

En el panel de control de Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Facebook**. En Exportar audiencia de Facebook, selecciona **Conectar Facebook**.

![Página de tecnología de Facebook en Braze que incluye una sección de resumen y otra de exportación de la audiencia de Facebook con el botón de Facebook Conectado.][4]{: style="max-width:85%;"}

Aparecerá una ventana de diálogo de Facebook oAuth para autorizar a Braze a crear audiencias personalizadas en tus cuentas de anuncios de Facebook.

![El primer cuadro de diálogo de Facebook te pide "Conectarte como X", donde X es tu nombre de usuario de Facebook.][6]{: style="max-width:30%;"}  ![El segundo cuadro de diálogo de Facebook te pide permiso para administrar los anuncios de tus cuentas publicitarias.][5]{: style="max-width:40%;"}

Una vez que hayas vinculado Braze a tu cuenta de Facebook, podrás seleccionar las cuentas de anuncios que deseas sincronizar dentro de tu espacio de trabajo Braze. 

![Una lista de las cuentas de anuncios disponibles que puedes conectar a Facebook.][7]{: style="max-width:70%;"}



![Una versión actualizada de la página de socios tecnológicos de Facebook que muestra las cuentas de anuncios conectadas correctamente.][8]{: style="max-width:85%;"}

Tu conexión a Facebook se aplica a nivel del espacio de trabajo Braze. Si tu administrador de Facebook te elimina de tu administrador de empresas de Facebook o del acceso a las cuentas de Facebook conectadas, Braze detectará un token no válido. Como resultado, tus Canvas activos que utilicen componentes de Facebook Audience mostrarán errores, y Braze no podrá sincronizar usuarios. 

{% alert important %}
Para los clientes que hayan pasado previamente por el proceso de revisión de la aplicación de Facebook para la [gestión de anuncios](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) y [el acceso estándar a la gestión de anuncios](https://developers.facebook.com/docs/marketing-api/access#standard), tu token de usuario del sistema seguirá siendo válido para el componente Facebook Audience. No podrás editar ni revocar el token de usuario del sistema de Facebook a través de la página del socio de Facebook. En su lugar, puedes conectar tu cuenta de Facebook para sustituir tu token de usuario del sistema de Facebook dentro de tu espacio de trabajo Braze. 

<br><br>
{% endalert %}

### Paso 2: Aceptar las condiciones de servicio de las audiencias personalizadas



- 
- 






### Paso 3: Añadir un componente de Facebook Audience en Canvas Flow

Añade un componente en tu Canvas y selecciona **Facebook Audience**.

 

### Paso 4: Configuración de la sincronización

 



Selecciona la cuenta de anuncios de Facebook deseada. En el desplegable **Elegir una audiencia nueva o existente**, escribe el nombre de una audiencia nueva o existente. 

{% tabs %}
{% tab Crear una nueva audiencia %}

1. 
2.  
3. 



 





{% endtab %}
{% tab Sincronización con un público existente %}

 

1. 
2.  
3.  

![]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
 
{% endalert %}

{% endtab %}
{% endtabs %}

### Paso 5: Lanzar Canvas

  

La pestaña **Historial** de la audiencia personalizada en el administrador de audiencias de Facebook reflejará el número de usuarios enviados a la audiencia desde Braze. Si un usuario vuelve a entrar en el paso, se le enviará de nuevo a Facebook.

![Detalles de la audiencia y la pestaña Historial de una determinada audiencia de Facebook, que incluye una tabla Historial de la audiencia con columnas para la actividad, los detalles de la actividad, los elementos modificados y la fecha y hora.][9]{: style="max-width:80%;"}

## Comprender los análisis

La siguiente tabla incluye métricas y descripciones que le ayudarán a comprender mejor los análisis de su componente Audience Sync.

| Métrica | Descripción |
| --- | --- |
| El usuario ha entrado | Número de usuarios que entraron en este componente para ser sincronizados con Facebook. |
| Continúa con el paso siguiente | Cuántos usuarios avanzaron al siguiente componente, si lo hay. Todos los usuarios avanzarán automáticamente si este es el último paso en la rama Canvas. |
| Usuarios sincronizados | Número de usuarios que se han sincronizado correctamente con Facebook. |
| Usuarios no sincronizados | Número de usuarios que no se han sincronizado debido a que faltan campos para coincidir. |
| Usuarios pendientes | Número de usuarios que están siendo procesados por Braze para sincronizarse con Facebook. |
| Usuarios con errores | Número de usuarios que no se sincronizaron con Facebook debido a un error de la API tras unas 13 horas de reintentos. Las posibles causas de error pueden ser un token de Facebook no válido o que se haya eliminado la audiencia personalizada en Facebook. |
| Has salido de Canvas | Número de usuarios que han salido del Canvas. Esto ocurre cuando el último paso en Canvas es un paso de Facebook. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}

{% endalert %}

## Preguntas más frecuentes

### ¿Cuánto tardan mis audiencias en aparecer en mi panel de socios de Audience Sync?

El tiempo que se tarda en poblar una audiencia depende del socio concreto. Todas las redes procesarán las solicitudes de Braze e intentarán emparejar a los usuarios. 

### 

Sólo tienes que desconectar y volver a conectar tu cuenta de Facebook en la página del socio de Facebook. 

### 

- Asegúrate de que tu token de usuario del sistema está autenticado y tiene acceso a las cuentas de anuncios deseadas en Facebook Business Manager.
- Asegúrate de haber seleccionado una cuenta de publicidad, introducido un nombre para la nueva audiencia personalizada y seleccionado los campos que coincidan.
- Puede que hayas alcanzado el límite de 500 audiencias personalizadas en Facebook. 

### 

Facebook no facilita esta información por motivos de privacidad.

### 

En este momento, Braze no admite audiencias personalizadas basadas en valores. Si estás interesado en sincronizar este tipo de audiencias personalizadas, envía [tus comentarios sobre el producto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

### 



 

- 
- 
- 
- 



### 

En este momento, Braze no supone audiencias personalizadas basadas en el valor. Si intentas sincronizar con esta audiencia, pueden producirse errores en el paso Sincronizar audiencia. Para solucionarlo, sigue estos pasos:

1. Ve al panel del administrador de anuncios de Facebook y selecciona **Audiencias**.
2. Selecciona **Crear audiencia** > **Audiencia personalizada**.
3. Selecciona **Lista de clientes**.
4. Sube tu CSV o lista sin la columna **Valor**. Selecciona **No, continuar con una lista de clientes que no incluya el valor del cliente**.
5. Termina de crear tu audiencia personalizada.
6. En Braze, actualiza el paso Sincronizar audiencia de Facebook con la audiencia personalizada que has creado.

###  

Para utilizar la Sincronización de audiencias con Facebook, debes aceptar estas condiciones de servicio. 

- 
- 

Después de aceptar las condiciones de servicio de tu audiencia personalizada de Facebook, haz lo siguiente:

1. Actualiza tu token de acceso a Facebook con Braze desconectando y volviendo a conectar tu cuenta de Facebook.
2. Vuelve a habilitar el paso de sincronización con la audiencia de Facebook editando y actualizando tu Canvas.



## Solución de problemas

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 40%;
}
table th:nth-child(2) {
    width: 40%;
}
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>Error</th>
      <th>Descripción</th>
      <th>Pasos para resolver</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Token no válido</b></td>
      <td></td>
      <td> </td>
    </tr>
    <tr>
      <td><b>Tamaño de la audiencia demasiado bajo</b></td>
      <td> Si el tamaño de tu audiencia se acerca a cero, la red puede marcar que el tamaño de la audiencia es demasiado bajo para servir.</td>
      <td> </td>
    </tr>
    <tr>
      <td><b>La audiencia no existe</b></td>
      <td> </td>
      <td> <br><br>  <br><br></td>
    </tr>
    <tr>
      <td><b>Intento de acceso a la cuenta publicitaria</b></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>   </td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>
      </td>
    </tr>
    <tr>
      <td></td>
      <td>  </td>
      <td>
      </td>
    </tr>
  </tbody>
</table>

### 

 

#### 

1.  
2.  
3. 

#### 

 

1. 
- 
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`
- 
  - 
  - 





1. 
2. 
3. 



{:start="4"}

4.  



{:start="5"}
5\.   
6\. Actualiza tu token de acceso a Facebook con Braze desconectando y volviendo a conectar tu cuenta de Facebook.
7\. Vuelve a habilitar el paso de sincronización con la audiencia de Facebook editando y actualizando tu Canvas. Braze podrá sincronizar a los usuarios en cuanto lleguen al Paso de Facebook Audience.
8\. 

####  



1. 
2. 
3.  <br> 
4.  <br> 

{:start="5"}

5.  <br> 

#### 



1. 
2. 

[0]: https://www.braze.com/privacy
[1]: https://www.facebook.com/business/help/113163272211510
[2]: https://www.facebook.com/business/help/910137316041095
[3]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[4]: {% image_buster /assets/img/fb/afb_1.png %}
[5]: {% image_buster /assets/img/fb/afb_2.png %}
[6]: {% image_buster /assets/img/fb/afb_3.png %}
[7]: {% image_buster /assets/img/fb/afb_4.png %}
[8]: {% image_buster /assets/img/fb/afb_5.png %}
[9]: {% image_buster /assets/img/fb_audience_sync/audience_history.png %}
[10]: {% image_buster /assets/img/fb_audience_sync/analytics_example.jpg %}
[11]: {% image_buster /assets/img/fb_audience_sync/add_step.png %}
[12]: {% image_buster /assets/img/fb_audience_sync/add_audience.png %}
[13]: {% image_buster /assets/img/fb_audience_sync/create_audience.png %}
[14]: {% image_buster /assets/img/fb_audience_sync/new_audience.png %}
[15]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/fb_sync.png %}
[22]: {% image_buster /assets/img/audience_sync/fb_sync2.png %}
[23]: {% image_buster /assets/img/audience_sync/fb_sync3.png %}
[24]: {% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}
[25]: {% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}