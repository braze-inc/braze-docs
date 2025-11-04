---
nav_title: Mozart Data
article_title: Mozart Data
description: "Este artículo de referencia describe la asociación entre Braze y Mozart Data, una plataforma de datos moderna todo en uno, que te permite utilizar Fivetran para importar datos a Snowflake, crear transformaciones, combinar datos y mucho más."
alias: /partners/mozart_data/
page_type: partner
search_tag: Partner

---

# Mozart Data

{% multi_lang_include video.html id="HU6dSOClcQ0" align="right" %}

> [Mozart Data](https://mozartdata.com/) es una moderna plataforma de datos todo en uno impulsada por Fivetran, Portable y Snowflake.

La integración de datos de Braze y Mozart te permite:
- Utilizar Fivetran para importar datos de Braze a Snowflake
- Crear transformaciones combinando datos de Braze con datos de otras aplicaciones y analizar eficazmente los comportamientos de los usuarios.
- Importar datos de Snowflake a Braze para crear nuevas oportunidades de interacción con los clientes.
- Combinar los datos de Braze con los de otras aplicaciones para obtener una comprensión más holística de los comportamientos de los usuarios.
- Integralo con una herramienta de inteligencia empresarial para explorar más a fondo los datos almacenados en Snowflake.

## Requisitos previos

<style>
table th:nth-child(1) {
    width: 25%;
}
table th:nth-child(2) {
    width: 75%;
}
table td {
    word-break: break-word;
}
</style>

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Mozart Data | Se necesita una cuenta de Mozart Data para beneficiarse de esta asociación. [Regístrate aquí.](https://app.mozartdata.com/signup)|
| Cuenta Snowflake<br>Opción 1: Cuenta nueva | Selecciona **Crear una nueva cuenta de Snowflake** durante el proceso de creación de la cuenta de Mozart Data para que Mozart Data te facilite una nueva cuenta de Snowflake. |
| Cuenta Snowflake<br>Opción 2: Cuenta existente | Si tu organización ya tiene una cuenta Snowflake, puedes utilizar la opción Mozart Data Connected.<br><br>Selecciona la opción **Ya tengo una cuenta Snowflake** para conectar una cuenta Snowflake existente. Para seguir esta opción, un usuario con permisos a nivel de cuenta debe [seguir estos pasos](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

La integración es compatible tanto para sincronizar datos de [Braze con Mozart Data](#syncing-data-from-braze-to-mozart-data) como [de Mozart Data con Braze](#syncing-data-from-mozart-data-to-braze).

### Sincronizar datos de Braze con Mozart Data

#### Paso 1: Configurar el conector Braze

1. En Mozart Data, ve a **Conectores** y haz clic en **Añadir conector**.
2. Busca "Braze" y selecciona la tarjeta de conector.
3. Introduce un nombre de esquema de destino donde se almacenarán todos los datos sincronizados de Braze. Recomendamos utilizar el nombre predeterminado del esquema `braze`.
4. Haz clic en **Añadir conector**.

#### Paso 2: Rellena el formulario del conector Fivetran

Se te redirigirá a la página del conector Fivetran. En esta página, rellena los campos indicados. A continuación, haz clic en **Continuar** > **Guardar y probar** para completar el conector Fivetran.

Fivetran comenzará a sincronizar los datos de su cuenta Braze con tu almacén de datos Snowflake. Puede acceder a los datos de la consulta desde Mozart Data una vez que el conector haya finalizado la sincronización. 

### Sincronización de datos de Mozart Data con Braze

#### Paso 1: Configurar un almacén de datos Snowflake

Siga las instrucciones de [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake) para configurar una tabla, un usuario y un permiso desde la interfaz de Snowflake. Nota que este paso requiere acceso Snowflake a nivel de administrador.

#### Paso 2: Configurar tu integración Snowflake en Braze

Después de configurar tu almacén Snowflake, en Mozart Data, ve a la página **Integración** y selecciona **Braze**. Aquí encontrarás las credenciales que deberá proporcionar a Braze.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

A continuación, mientras estás conectado a Braze, ve a **Integraciones > Socios tecnológicos > Snowflake** para iniciar el proceso de integración. Copia las credenciales de Mozart Data y añádelas a la página de importación de Snowflake Data. Haz clic en **Configurar detalles de sincronización** e introduce tu cuenta Snowflake y la información de la tabla de origen. 

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

A continuación, elige un nombre para la sincronización, proporciona las direcciones de correo electrónico de los contactos y selecciona un tipo de datos y una frecuencia de sincronización. 

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-importsync.png %}){: style="max-width:80%;"}

#### Paso 3: Añadir una clave pública al usuario Braze
En este punto, tendrás que volver a Snowflake para completar la configuración. Añade la clave pública que aparece en el tablero Braze al usuario que creaste para que Braze se conecte a Snowflake.

Para más información sobre cómo hacerlo, consulta la [documentación de Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Si quieres rotar las claves en cualquier momento, Mozart Data puede generar un nuevo par de claves y proporcionarte la nueva clave pública.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### Paso 4: Probar conexión

Una vez que el usuario esté actualizado con la clave pública, vuelve al panel de Braze y haz clic en **Probar conexión**. Si tienes éxito, verás una vista previa de los datos. Si, por alguna razón, la conexión no tiene éxito, se mostrará un mensaje de error para ayudar a solucionar el problema.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
Debe probar con éxito una integración antes de que pueda pasar del estado Borrador al Activo. Si necesita salir de la página de creación, su integración se guardará y podrá volver a visitar la página de detalles para realizar cambios y pruebas.  
{% endalert %}

## Uso de esta integración

### Cómo acceder a los datos de Braze como usuario de Mozart Data
Tras crear correctamente una cuenta de Mozart Data, podrás acceder desde Mozart Data a tus datos de Braze sincronizados con tu almacén de datos de Snowflake.

#### Transformaciones
Mozart Data ofrece una capa de transformación SQL que permite a los usuarios crear una vista o una tabla. Puedes crear una tabla de dimensiones a nivel de usuario (por ejemplo, `dim_users`) para resumir los datos de uso del producto, el historial de transacciones y las actividades de interacción con mensajes Braze de cada usuario. 

#### Análisis
Utilizando los modelos de transformación o los datos brutos sincronizados desde Braze, puedes analizar la interacción de los usuarios con los mensajes Braze. Además, puedes combinar los datos de Braze con otros datos de la aplicación y analizar cómo la información obtenida de la interacción de los usuarios con los mensajes de Braze se relaciona con otros datos que puedas tener sobre los usuarios. Por ejemplo, su información demográfica, historial de compras, uso de productos y participación en el servicio de atención al cliente. 

Esto puede ayudarte a tomar decisiones más informadas sobre las estrategias de interacción para mejorar la retención de usuarios. Todo esto puede hacerse dentro de la interfaz de Mozart Data utilizando la herramienta Consulta, donde puedes exportar los resultados a una hoja de Google o a un CSV para prepararlos para una presentación.

#### Inteligencia empresarial (BI)
¿Listo para visualizar y compartir tus ideas con otros miembros del equipo? Mozart Data se integra con casi todas las herramientas de BI. Si aún no tienes una herramienta de BI, ponte en contacto con Mozart Data para crear una cuenta gratuita de Metabase. 