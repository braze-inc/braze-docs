---
nav_title: Eliminar usuarios mediante API
article_title: Eliminar usuarios mediante API
page_order: 0

page_type: reference
description: "Este artículo de ayuda describe las implicaciones de eliminar un perfil de usuario a través de la API REST de Braze."
tool: Dashboard
platform: API
---

# Eliminar usuarios mediante API

Cuando [eliminas a un usuario a través de la API REST de Braze]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/), se borran (anulan) los siguientes datos:
- Cualquier atributo que tuviera el usuario
- Dirección de correo electrónico
- Número de teléfono
- ID de usuario externo 
- Género
- País
- Idioma

Cuando [eliminas a un usuario a través de la API REST de Braze]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/), se producen los siguientes eventos:
- El perfil de usuario se ha borrado (anulado).
- El recuento de [usuarios de toda la vida]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#lifetime-users) se actualizará para tener en cuenta a los nuevos usuarios eliminados.	
- El usuario eliminado seguirá contando para el porcentaje de conversión agregado. Los recuentos de eventos personalizados y de compras no se actualizarán para los usuarios eliminados.

## Múltiples perfiles con una dirección de correo electrónico compartida

Supongamos que quieres fusionar varios perfiles de usuario que comparten la misma dirección de correo electrónico. 

Para fusionar estos perfiles de usuario:

 1. Identifica a los usuarios con direcciones de correo electrónico duplicadas. 
 2. Exporta todos los atributos de un mismo perfil. 
 3. Importa esos atributos al perfil de usuario mediante API o CSV. 
 4. Elimina los usuarios a través de la API, eliminando esencialmente estos usuarios duplicados y los datos indicados anteriormente.

_Última actualización: 13 de septiembre de 2023_

