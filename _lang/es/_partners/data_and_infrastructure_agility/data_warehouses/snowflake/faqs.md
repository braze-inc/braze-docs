---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre el uso compartido de datos de Snowflake
page_order: 4
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


