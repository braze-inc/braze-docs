## Cuestionario de privacidad de Google Play {#privacy-questionnaire}

A partir de abril de 2022, los desarrolladores de Android deberán cumplimentar el [formulario de seguridad de datos](https://support.google.com/googleplay/android-developer/answer/10787469) de Google Play para revelar las prácticas de privacidad y seguridad. Esta guía proporciona instrucciones sobre cómo rellenar este nuevo formulario con información sobre cómo gestiona Braze los datos de tu aplicación. 

Como desarrollador de la aplicación, tú controlas qué datos envías a Braze. Los datos recibidos por Braze se procesan de acuerdo con tus instrucciones. Esto es lo que Google clasifica como [proveedor de servicios](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en#zippy=%2Cwhat-kinds-of-activities-can-service-providers-perform). 

{% alert important %}
Este artículo proporciona información sobre los datos que procesa el SDK de Braze en relación con el cuestionario de la sección de seguridad de Google. Este artículo no proporciona asesoramiento jurídico, por lo que te recomendamos que consultes con tu equipo jurídico antes de enviar cualquier información a Google.
{% endalert %}

### Preguntas

|Preguntas|Respuestas para Braze SDK|
|---|---|
|¿Recoge o comparte tu aplicación alguno de los tipos de datos de usuario requeridos?|Sí, el SDK para Android de Braze recopila datos según lo configure el desarrollador de la aplicación. |
|¿Todos los datos de usuario recogidos por tu aplicación están encriptados en tránsito?|Sí.|
|¿Proporcionas alguna forma de que los usuarios puedan solicitar que se eliminen sus datos?|Sí.|

Para obtener más información sobre la gestión de las solicitudes de los usuarios sobre sus datos y su eliminación, consulta la [Información sobre la retención de datos de Braze]({{site.baseurl}}/api/data_retention/).

### Recopilación de datos

Los datos recopilados por Braze vienen determinados por tu integración específica y los datos de usuario que elijas recopilar. Para saber más sobre qué datos recopila Braze por defecto y cómo desactivar determinados atributos, consulta nuestras [opciones de recopilación de datos del SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#minimum-integration).

<table id="datatypes">
    <thead>
        <tr>
            <th width="25%">Categoría</th>
            <th width="25%">Tipo de datos</th>
            <th width="50%">Uso de Braze</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">Ubicación</td>
            <td>Ubicación aproximada</td>
            <td rowspan="15">No se recopila de manera predeterminada.</td>
        </tr>
        <tr>
            <td>Ubicación precisa</td>
        </tr>
        <tr>
            <td rowspan="9">Información personal</td>
            <td>Apellidos</td>
        </tr>
        <tr>
            <td>Dirección de correo electrónico</td>
        </tr>
        <tr>
            <td>ID de usuario</td>
        </tr>
        <tr>
            <td>Dirección</td>
        </tr>
        <tr>
            <td>Número de teléfono</td>
        </tr>
        <tr>
            <td>Raza y etnia</td>
        </tr>
        <tr>
            <td>Creencias políticas o religiosas</td>
        </tr>
        <tr>
            <td>Orientación sexual</td>
        </tr>
        <tr>
            <td>Otros datos</td>
        </tr>
        <tr>
            <td rowspan="4">Información financiera</td>
            <td>Información de pago del usuario</td>
        </tr>
        <tr>
            <td>Historial de compras</td>
        </tr>
        <tr>
            <td>Puntuación crediticia</td>
        </tr>
        <tr>
            <td>Otros datos financieros</td>      
        </tr>
        <tr>
            <td rowspan="2">Salud y forma física</td>
            <td>Información de salud</td>
            <td rowspan="2">No se recopila de manera predeterminada.</td>
        </tr>
        <tr>
            <td>Información de acondicionamiento físico</td>     
        </tr>
        <tr>
            <td rowspan="3">Mensajes</td>
            <td>Correos electrónicos</td>
            <td rowspan="2">No se recopila de manera predeterminada.</td>
        </tr>
        <tr>
            <td>SMS o MMS</td>          
        </tr>
        <tr>
            <td>Otros mensajes dentro de la aplicación</td>
            <td>Si envías mensajes dentro de la aplicación o notificaciones push a través de Braze, recopilamos información sobre cuándo los usuarios han abierto o leído estos mensajes.</td>
        </tr>
        <tr>
            <td rowspan="2">Fotos y videos</td>
            <td>Fotos</td>
            <td rowspan="8">No recopilada.</td>
        </tr>
        <tr>
            <td>Videos</td>
        </tr>
        <tr>
            <td rowspan="3">Archivos de audio</td>
            <td>Grabaciones de voz o sonido</td>
        </tr>        
        <tr>
            <td>Archivos de música</td>
        </tr>
        <tr>
            <td>Otros archivos de audio</td>
        </tr>
        <tr>
            <td>Archivos y documentos</td>
            <td>Archivos y documentos</td>
        </tr>
        <tr>
            <td>Calendario</td>
            <td>Eventos del calendario</td>
        </tr>
        <tr>
            <td>Contactos</td>
            <td>Contactos</td>
        </tr>
        <tr>
            <td rowspan="5">Actividad de la aplicación</td>
            <td>Interacciones de la aplicación</td>
            <td>Braze recopila datos de actividad de la sesión de forma predeterminada. Todas las demás interacciones y actividades están determinadas por la integración personalizada de tu aplicación.</td>
        </tr>
        <tr>
            <td>Historial de búsqueda en la aplicación</td>
            <td>No recopilada.</td>            
        </tr>
        <tr>
            <td>Aplicaciones instaladas</td>
            <td>No recopilada.</td>            
        </tr>
        <tr>
            <td>Otros contenidos generados por usuarios</td>
            <td rowspan="2">No se recopila de manera predeterminada.</td>            
        </tr>
        <tr>
            <td>Otras acciones</td>
        </tr>
        <tr>
            <td>Navegación Web</td>
            <td>Historial de navegación Web</td>
            <td>No recopilada.</td>
        </tr>
        <tr>
            <td rowspan="3">Información y rendimiento de la aplicación</td>
            <td>Registros de colisiones</td>
            <td>Braze recopila registros de errores que se producen en el SDK. Contiene el modelo de teléfono del usuario y el nivel de sistema operativo, junto con un ID de usuario específico de Braze.</td>
        </tr>
        <tr>
            <td>Diagnóstico</td>
            <td>No recopilada.</td>            
        </tr>
        <tr>
            <td>Otros datos de rendimiento de la aplicación</td>
            <td>No recopilada.</td>
        </tr>
        <tr>
            <td>ID del dispositivo u otros ID</td>
            <td>ID del dispositivo u otros ID</td>
            <td>Braze genera un ID de dispositivo para diferenciar los dispositivos de los usuarios, y comprueba si los mensajes se envían al dispositivo correcto.</td>
        </tr>
    </tbody>
</table>

Para obtener más información sobre otros datos de dispositivo que Braze recopila y que pueden quedar fuera del ámbito de las directrices de seguridad de datos de Google Play, consulta nuestro [resumen de almacenamiento de Android]({{site.baseurl}}/developer_guide/storage/?tab=android) y nuestras [opciones de recopilación de datos del SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#minimum-integration).

## Desactivar el seguimiento de datos

Para desactivar la actividad de seguimiento de datos en el SDK de Android, utiliza el método [`disableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html). Esto hará que se cancelen todas las conexiones de red, lo que significa que el SDK de Braze ya no pasará ningún dato a los servidores Braze.

## Borrar datos almacenados previamente

Puedes utilizar el método [`wipeData()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html) para borrar completamente todos los datos del lado del cliente almacenados en el dispositivo.

## Reanudar el seguimiento de los datos

Para reanudar la recopilación de datos, puedes utilizar el método [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html) método. Ten en cuenta que esto no restaurará los datos borrados previamente.
