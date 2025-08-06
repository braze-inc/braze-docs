---
nav_title: Google
article_title: Sincronización del público de Canvas con Google
alias: /google_audience_sync/
description: "En este artículo de referencia se explica cómo utilizar Braze Audience Sync con Google para ofrecer anuncios basados en desencadenantes de comportamiento, segmentación, etc."
Tool:
  - Canvas
page_order: 3

---

# Sincronización de audiencias con Google

{% alert important %}
  Consulte la siguiente documentación para obtener más información.
{% endalert %}

La integración de Braze Audience Sync con Google permite a las marcas ampliar el alcance de sus recorridos del cliente multicanal a Google Search, Google Shopping, Gmail, YouTube y Google Display. Utilizando tus datos de clientes propios, puedes entregar de forma segura anuncios basados en desencadenantes dinámicos de comportamiento, segmentación y mucho más. Cualquier criterio que utilice normalmente para activar un mensaje (por ejemplo, push, correo electrónico o SMS) como parte de Braze Canvas se puede utilizar para activar un anuncio dirigido a ese usuario a través de [Customer Match](https://support.google.com/google-ads/answer/6379332?hl=en) de Google.

{% alert important %}
A partir del 1 de mayo de 2023, Google Ads dejará de generar audiencias similares, también conocidas como "lookalike audiences", para la segmentación y la generación de informes. Consulte [la documentación de Google Ads](https://support.google.com/google-ads/answer/12463119?) para obtener más información.
{% endalert %}

**Los casos de uso comunes para sincronizar Audiencias Personalizadas incluyen:**
- Dirigirse a usuarios de alto valor a través de múltiples canales para impulsar las compras o la participación.
- Reorientar a los usuarios menos receptivos a otros canales de marketing.
- Crear audiencias de supresión para evitar que los usuarios reciban anuncios cuando ya son consumidores fieles de su marca.

{% alert note %}
Esta función permite a las marcas controlar qué datos específicos de origen se comparten con Google. En Braze, las integraciones con las que puedes y no puedes compartir tus datos de origen se tienen muy en cuenta. Para obtener más información sobre nuestra política de privacidad de datos de Braze, haz [clic aquí](https://www.braze.com/privacy).
{% endalert %}

## Requisitos previos



| Requisito | Origin | Descripción |
| ----------- | ------ | ----------- |
| Cuenta de Google Ads | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | Una cuenta de anuncios de Google activa para su marca.<br><br>Si quieres compartir una audiencia en varias cuentas gestionadas, puedes cargar tus audiencias en tu [cuenta de gestor](https://support.google.com/google-ads/answer/6139186). |
| Condiciones y políticas de Google Ads | [Google](https://support.google.com/adspolicy/answer/54818?hl=en) | Debe aceptar y garantizar el cumplimiento de [las Condiciones de publicidad de Google](https://payments.google.com/u/0/paymentsinfofinder?hostOrigin=aHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tOjQ0Mw..&sri=-40) y de [las Políticas de publicidad de Google](https://support.google.com/adspolicy/answer/6008942?sjid=15557182366992806023-NC), que incluyen la [Política de consentimiento del usuario de la UE](https://www.google.com/about/company/user-consent-policy/), según le sean aplicables, en el uso que haga de Braze Audience Sync.<br><br>Consulta con tu equipo jurídico la nueva Política de consentimiento del usuario de la UE de Google para asegurarte de que obtienes el consentimiento adecuado para utilizar los servicios de Google Ads para tus usuarios finales del EEE, Reino Unido y Suiza. |
| Google Customer Match | [Google](https://support.google.com/google-ads/answer/6299717) |  Customer Match no está disponible para todos los anunciantes.<br><br>**Para utilizar Customer Match, tu cuenta debe tener:**<br>\- Un buen historial de cumplimiento de la política<br>\- Un buen historial de pagos<br>\- Al menos 90 días de historial en Google Ads<br>\- Más de 50.000 USD de gasto total durante toda la vida. Para los anunciantes cuyas cuentas se gestionen en divisas distintas del dólar estadounidense, el importe de sus gastos se convertirá a dólares estadounidenses utilizando el tipo de cambio medio mensual de esa divisa.<br><br>Si tu cuenta no cumple estos criterios, tu cuenta no es elegible actualmente para utilizar la característica Customer Match.<br><br>Ponte en contacto con tu representante de Google Ads para obtener más información sobre la disponibilidad de Customer Match para tu cuenta. |
| Señales de consentimiento de Google | [Google](https://support.google.com/google-ads/answer/14310715) |  Si desea publicar anuncios para usuarios finales del EEE mediante el servicio Customer Match de Google, deberá pasar a Braze los siguientes atributos personalizados (booleanos) como parte de la Política de consentimiento de usuarios de la UE de Google. Puedes encontrar más información en [Recopilación del consentimiento de los usuarios finales del EEE, Reino Unido y Suiza](#collecting-consent-for-eea-uk-and-switzerland-end-users): <br> - `$google_ad_user_data` <br> - `$google_ad_personalization` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Cuando utilices los SDK de Braze para recoger señales de consentimiento, asegúrate de que cumples las siguientes versiones mínimas:

{% sdk_min_versions swift:7.6.0 android:1.3.2 web:3.0.0 %}

### Recoger el consentimiento de los usuarios finales del EEE, Reino Unido y Suiza

La Política de consentimiento del usuario de la UE de Google exige a los anunciantes que revelen lo siguiente a sus usuarios finales del EEE, Reino Unido y Suiza, así como que obtengan su consentimiento para ello:

* El uso de cookies u otro tipo de almacenamiento local cuando sea legalmente necesario.
* La recopilación, el intercambio y el uso de sus datos personales para la personalización de anuncios.

Esto no afecta a los usuarios finales estadounidenses ni a ningún otro usuario final situado fuera del EEE, el Reino Unido o Suiza. Consulta con tu equipo jurídico la nueva Política de consentimiento del usuario de la UE de Google para asegurarte de que obtienes el consentimiento adecuado para utilizar los servicios de Google Ads para tus usuarios finales del EEE, Reino Unido y Suiza.

Según los requisitos de la Ley de Mercados Digitales (DMA) en vigor a partir del 6 de marzo de 2024, los anunciantes deben aprobar el consentimiento de los usuarios finales del EEE, Reino Unido y Suiza cuando compartan datos con Google. Como parte de este cambio, puede recopilar ambas señales de consentimiento en Braze como los siguientes atributos personalizados booleanos:

* `$google_ad_user_data`
* `$google_ad_personalization`

Braze sincronizará los datos de estos atributos personalizados con los [campos de consentimiento correspondientes en Google](https://support.google.com/google-ads/answer/14310715#:~:text=These%20consent%20fields%20are%3A).

#### Gestión del consentimiento revocado

Para mantener actualizadas tus listas de audiencia en caso de que un usuario final del EEE haya sido añadido a la lista de audiencia, y posteriormente se haya retractado de cualquiera de los dos consentimientos (`$google_ad_user_data` o `$google_ad_personalization`), debes configurar un Canvas para eliminar usuarios de las listas de audiencia existentes mediante un paso en Canvas de sincronización de audiencia.

{% alert note %}
Si un usuario del EEE ha dado previamente su consentimiento para ambas seÃ±ales, esos datos seguirÃ¡n utilizÃ¡ndose para Google Customer Match hasta que la lista caduque o hasta que se actualice explÃcitamente el estado del consentimiento a travÃ©s de Google Audience Sync, o ambas cosas.
{% endalert %}

#### Consejos

* Envía el valor como tipo booleano, no como tipo cadena.
* Anteponga el signo de dólar ($) al nombre del atributo. Braze utiliza un signo de dólar al principio del nombre de un atributo para indicar que se trata de una clave especial y reservada.
* 
* Aunque no se puede establecer explícitamente un usuario como no especificado, si se envía un valor `null` o `nil` o cualquier valor que no sea `true` o `false`, Braze pasará este usuario a Google como `UNSPECIFIED`.
* Los nuevos usuarios añadidos o actualizados sin especificar ninguno de los atributos de consentimiento se sincronizarán con Google con dichos atributos marcados como no especificados.

Si intentas sincronizar a un usuario del EEE sin los campos de consentimiento necesarios y el estado concedido, Google lo rechazará y no publicará anuncios a este usuario. Además, si se muestra un anuncio a un usuario del EEE sin su consentimiento explícito, usted puede ser responsable y correr riesgos financieros. Para evitarlo, sugerimos enviar campañas con filtros de segmento que sólo incluyan a los usuarios del EEE, Reino Unido y Suiza con atributos de consentimiento de Google `true`. Para obtener más información sobre la Política de consentimiento de los usuarios de la UE para los socios de carga de coincidencias de clientes, consulte [las preguntas frecuentes](https://support.google.com/google-ads/answer/14310715) de Google.

### Configuración de tu Canvas

Después de sincronizarte con Braze, los siguientes atributos de consentimiento estarán disponibles en tus perfiles de usuario y para la segmentación:

- `$google_ad_user_data`
- `$google_ad_personalization`

En cualquier Canvas en el que te dirijas a usuarios finales del EEE, Reino Unido y Suiza utilizando Google Audience Sync para añadir usuarios a una audiencia, tienes que excluir a estos usuarios siempre que ambos atributos de consentimiento tengan cualquier valor que no sea `true`. Esto se puede conseguir segmentando a estos usuarios cuando los valores de consentimiento están configurados en `true`. Esto también garantiza la sincronización de los análisis más precisos de los usuarios, ya que sabemos que Google rechazará a estos usuarios de las audiencias. Ten en cuenta que si utilizas Google Audience Sync para eliminar usuarios de una audiencia, los atributos de consentimiento no son necesarios.

## Integración

### Paso 1: Conectar la cuenta de Google

Para empezar, vaya a **Integraciones de socios** > **Socios tecnológicos** > **Anuncios de Google** y seleccione **Conectar anuncios de Google**. 

 



#### 

 En Google Audience Sync, selecciona **Añadir ID de publicidad móvil**, introduce el ID de tu aplicación para iOS y el ID de tu aplicación para Android (nombre del paquete de la aplicación), y guarda cada uno de ellos.

<br><br>
![La página actualizada de la tecnología de Google Ads muestra las cuentas de anuncios conectadas, lo que te permite volver a sincronizar cuentas y añadir ID de publicidad para móviles.]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
<br><br>

  

### Paso 2: Añadir un paso de Google Audience en Canvas Flow



 

### Paso 3: Configuración de la sincronización

1. 
2. 



{: start="3"}
3\. Seleccione la cuenta de anuncios de Google deseada.
4\.  

{% tabs %}
{% tab Crear una nueva audiencia %}

1. 
2. 
3.  Puede elegir cualquiera de los dos:

- **Información de contacto del cliente**:   
- **ID de anunciante móvil**:  

{: start="4"}
4\. 

![Vista ampliada del componente Canvas de audiencia personalizada. Aquí, se selecciona la cuenta de publicidad deseada, se crea una nueva audiencia y se selecciona la casilla "información de contacto del cliente".]({% image_buster /assets/img/audience_sync/g_sync.png %})

Los usuarios recibirán una notificación en la parte superior del editor de pasos si la audiencia se crea correctamente o si surgen errores durante este proceso. Los usuarios pueden hacer referencia a este público para la eliminación de usuarios más adelante en el recorrido Canvas, ya que el público se creó en modo borrador. 

![Una alerta que aparece después de crear un nuevo público en el componente Canvas.]({% image_buster /assets/img/audience_sync/g_sync3.png %})

 

{% alert important %}
Dados los requisitos de coincidencia de clientes de Google, no puede tener información de contacto de clientes e ID de anunciantes móviles en las mismas listas de clientes. A continuación, Google Customer Match utilizará esta información para determinar quién es segmentable en la Búsqueda de Google, Google Display, YouTube y Gmail. Para más detalles sobre los requisitos de Google Customer Match, consulta su [documentación](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507).
{% endalert %}
{% endtab %}
{% tab Sincronización con un público existente %}

Braze también ofrece la posibilidad de añadir o eliminar usuarios de las listas de clientes de Google existentes para garantizar que estas audiencias estén actualizadas. 

1. 
2. 
3.  
4.  Tu paso de Google Audience incluirá detalles sobre la nueva audiencia.

![Vista ampliada del componente Canvas de audiencia personalizada. Aquí se seleccionan la cuenta de anuncios deseada y el público existente, así como el botón de opción "Añadir usuario al público".]({% image_buster /assets/img/audience_sync/g_sync2.png %})

{% endtab %}
{% endtabs %}

### Paso 4: Lanzar Canvas

Completa el resto de tu recorrido de usuario en Canvas y ¡lánzalo! Si has optado por crear una nueva audiencia, Braze creará la audiencia dentro de Google y luego añadirá usuarios a medida que lleguen a este paso en tu Canvas. Si ha seleccionado añadir o eliminar usuarios de un público existente, Braze añadirá o eliminará usuarios cuando lleguen a este paso de su recorrido de usuario.

A continuación, los usuarios pasarán al siguiente componente del lienzo, si existe, o saldrán del lienzo si se trata del último paso del recorrido del usuario. 

## Sincronización de usuarios y consideraciones sobre el límite de velocidad

A medida que los usuarios lleguen al componente de Sincronización de Audiencia, Braze sincronizará a estos usuarios casi en tiempo real respetando los límites de tasa de Google Ads API. Lo que esto significa en la práctica es que Braze intentará procesar por lotes el mayor número de usuarios cada 5 segundos antes de enviarlos a Google. 

Cuando un cliente esté a punto de alcanzar el límite de velocidad de la API de Google Ads, Google informará a Braze sobre las recomendaciones de reintento. Si un cliente de Braze alcanza su límite de tarifa, Braze the Canvas reintentará la sincronización durante un máximo de ~13 horas. Si la sincronización no es posible, estos usuarios aparecen en la lista de la métrica Users Errored.

## Comprender los análisis 

La tabla siguiente incluye métricas y descripciones que te ayudarán a comprender mejor los análisis de tu paso de Sincronización de audiencias.

| Métrica | Descripción |
| ------ | ----------- |
| *Has entrado* | Número de usuarios que han introducido este paso para sincronizarlo con Google. |
| *Continúa con el paso siguiente* | Cuántos usuarios avanzaron al siguiente componente, si lo hay. Todos los usuarios avanzarán automáticamente. Si este es el último paso en la rama Canvas, esta métrica será 0. |
| *Usuarios sincronizados* | Número de usuarios que se han sincronizado correctamente con Google. |
| *Usuario no sincronizado* | Número de usuarios que no se han sincronizado debido a que faltan campos para coincidir o a que el atributo de consentimiento se ha establecido en `false`. |
| *Usuarios con errores* | Número de usuarios que no se sincronizaron con Google debido a un error, tras ~13 horas de reintentos. En caso de errores específicos, como interrupciones del servicio API de Google Ads, Canvas reintentará la sincronización durante un máximo de ~13 horas. Si la sincronización sigue sin ser posible en ese momento, se rellenará el campo *Usuario no sincronizado*. |
| *Usuarios pendientes* | Número de usuarios que Braze está procesando actualmente para sincronizar con Google. |
| *Has salido de Canvas* | Número de usuarios que han salido del Canvas. Esto ocurre cuando el último paso de un Canvas es un paso de Google. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Preguntas más frecuentes

### 

Google Customer Match tiene requisitos estrictos sobre cómo se formatean estas audiencias y qué información del cliente se incluye. En concreto, los ID de anunciante móvil deben cargarse por separado de la información de contacto del cliente (como el correo electrónico y el número de teléfono). Para obtener más información, consulta [la documentación de Google sobre la función Customer Match](https://support.google.com/google-ads/answer/7659867?hl=en#undefined).

### 

Una audiencia puede tardar entre 6 y 12 horas en sincronizarse con Google. 

### 

 Después, el tamaño se redondeará a los dos dígitos más significativos.

### 



### 

 


[1]: {% image_buster /assets/img/google_sync/google_sync1.png %}
[2]: {% image_buster /assets/img/google_sync/google_sync2.png %}
[3]: {% image_buster /assets/img/google_sync/google_sync3.png %}
[4]: {% image_buster /assets/img/google_sync/google_sync4.png %}
[6]: {% image_buster /assets/img/google_sync/google_sync6.png %}
[8]: {% image_buster /assets/img/google_sync/google_sync8.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/g_sync.png %}
[22]: {% image_buster /assets/img/audience_sync/g_sync2.png %}
[23]: {% image_buster /assets/img/audience_sync/g_sync3.png %}
