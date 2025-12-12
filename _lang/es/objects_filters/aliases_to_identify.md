---
nav_title: "Alias para identificar objetos"
article_title: Alias de la API para identificar objetos
page_order: 11
page_type: reference
description: "Este artículo explica los alias para identificar la especificación de objetos."

---

# Alias para identificar objetos

Una petición a la API con cualquier campo del objeto atributos creará o actualizará un atributo de ese nombre con el valor dado en el perfil de usuario especificado. 

Utiliza los nombres de campo de perfil de usuario de Braze (enumerados a continuación o cualquiera de los enumerados en la sección de [campos de perfil de usuario de Braze]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)) para actualizar esos valores especiales en el perfil de usuario en el panel o añade tus propios datos de atributos personalizados al usuario.

## Cuerpo del objeto

```json
{
  "aliases_to_identify" : (required, array of aliases to identify object)
  [
    {
      "external_id" : (required, string) see External user ID,
      // external_ids for users that do not exist will return a non-fatal error.
      // See server responses for details.
      "user_alias" : {
        "alias_name" : (required, string) see User aliases,
        "alias_label" : (required, string) see User aliases
      }
    }
  ]
}
```

- [ID usuario externo]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [Alias de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
