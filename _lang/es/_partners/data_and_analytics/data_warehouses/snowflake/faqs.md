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


