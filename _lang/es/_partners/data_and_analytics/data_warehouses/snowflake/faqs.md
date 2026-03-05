---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre el uso compartido de datos de Snowflake
page_order: 50
page_type: FAQ
description: "Este artículo responde a las preguntas más frecuentes sobre el intercambio de datos Snowflake."

---

# Preguntas más frecuentes

### ¿Es posible ofuscar datos PII mediante el intercambio de datos Snowflake?
No, por ahora no se admite.

### ¿Necesito compartir datos de la misma región o de otras regiones?
Utiliza datos compartidos para la misma región en los siguientes escenarios:
- Tu cuenta Snowflake está en US-EAST-1 (AWS) y la región de tu panel de Braze está en EE. UU.
- Tu región Snowflake está en EU-CENTRAL-1 y la región de tu panel de Braze está en la UE.
- Tu región Snowflake está en AP-Southeast-2 (AWS) y la región de tu panel de Braze está en Australia.
- Tu región Snowflake está en AP-Southeast-3 (AWS) y la región de tu panel de Braze está en Indonesia.

Si no, utiliza el intercambio de datos entre regiones. 

### ¿Qué debo hacer con mis datos compartidos cuando cambie a una nueva cuenta Snowflake?
Puedes eliminar el antiguo recurso compartido de datos asociado a tu antigua cuenta de Snowflake y, a continuación, crear un nuevo recurso compartido para la nueva cuenta. Todos los datos históricos estarán disponibles en la nueva acción. 

### ¿Por qué no veo datos en mis datos compartidos?
Puede que hayas utilizado un ID de cuenta de Snowflake incorrecto al crear tus datos compartidos. El ID de cuenta del panel de compartición de datos debe coincidir con la salida de `CURRENT_ACCOUNT()` de tu cuenta de Snowflake.

Si tu acción es transregional, puede que los datos no estén disponibles inmediatamente. Dependiendo de tu volumen de datos, la sincronización puede tardar unas horas.

### ¿Por qué recibo un error de cumplimiento de la HIPAA al crear un intercambio de datos?

La cuenta especificada no cumple la HIPAA o está en [ediciones de Snowflake](https://docs.snowflake.com/en/user-guide/intro-editions) inferiores a Business Critical. Tu cuenta de Snowflake debe actualizarse a la edición Business Critical para cumplir con la HIPAA y poder compartir datos. Ponte en contacto con el servicio de asistencia de Snowflake si necesitas ayuda para actualizar tu cuenta.

### ¿Por qué no puedo volver a crear un recurso compartido de datos después de eliminar uno?

Es posible que el sistema aún esté procesando la eliminación de tu anterior intercambio de datos. Espera unos minutos a que finalice el proceso de desaprovisionamiento y vuelve a intentar crear el nuevo recurso compartido de datos.

### ¿Cuántas veces tengo que ejecutar `CREATE DATABASE` cuando tengo varios espacios de trabajo que comparten datos con la misma cuenta de Snowflake?

Sólo tienes que ejecutar `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` una vez. Cuando se comparten varios recursos compartidos de datos de diferentes espacios de trabajo Braze a la misma cuenta Snowflake, se combinan automáticamente en el mismo recurso compartido. Después de crear la base de datos inicial, los datos de los espacios de trabajo adicionales se añaden automáticamente a la base de datos existente sin necesidad de solicitudes de uso compartido adicionales ni pasos de creación de bases de datos.

Por ejemplo, si creas una compartición de datos a la cuenta 123 de Snowflake desde el espacio de trabajo A, acepta la solicitud de compartición y crea una base de datos. Cuando más tarde crees un recurso compartido de datos a la misma cuenta 123 de Snowflake desde el espacio de trabajo B, no se enviará ninguna nueva solicitud de recurso compartido: los datos se añadirán inmediatamente al recurso compartido existente y estarán disponibles en la base de datos creada anteriormente.

### Si tengo varios espacios de trabajo, ¿una sola base de datos contiene los datos de todos ellos?

Sí. Cuando compartes datos de varios espacios de trabajo Braze a la misma cuenta Snowflake, todos los datos se combinan en un único recurso compartido y están disponibles en la misma base de datos. Puedes filtrar los datos por `app_group_id` para distinguir entre espacios de trabajo.

Como práctica recomendada, filtra siempre por `app_group_id` en tus consultas para que estén preparadas para el futuro. Esto garantiza que tus paneles e informes sigan siendo precisos si añades espacios de trabajo adicionales en el futuro. Sin este filtro, tus métricas pueden incluir inesperadamente datos de espacios de trabajo recién añadidos.

### ¿Cuál es el enfoque recomendado para gestionar los datos de varios espacios de trabajo en Snowflake?

Envía todos los datos de Braze a la misma base de datos y filtra por `app_group_id` para distinguir entre espacios de trabajo. Este enfoque simplifica la gestión de los datos y garantiza la coherencia de los informes en toda la organización.

### ¿Cuántos conectores Snowflake Data Share necesito para varios espacios de trabajo?

El número de conectores que necesitas depende de tu configuración específica y de tus derechos. Ponte en contacto con tu equipo de cuentas Braze para obtener más información sobre qué derechos son adecuados para tu caso de uso.


