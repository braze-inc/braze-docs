{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Registro de atributos personalizados

Braze proporciona métodos para asignar atributos a los usuarios. Podrás filtrar y segmentar a tus usuarios según estos atributos en el panel.

### Atributos predeterminados del usuario

Para configurar los atributos de usuario recogidos automáticamente por Braze, puedes utilizar los métodos de configuración que vienen con el SDK.

```javascript
Braze.setFirstName("Name");
```

Se admiten los siguientes atributos:

- Nombre
- Apellido
- Género
- Fecha de nacimiento
- Ciudad natal
- País
- Número de teléfono
- Idioma
- Correo electrónico

Todos los valores de cadena como nombre, apellidos, país y ciudad de residencia están limitados a 255 caracteres.

### Atributos personalizados del usuario

Además de nuestros métodos predefinidos de atributos de usuario, Braze también proporciona [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) para hacer un seguimiento de los datos de tus aplicaciones. 

```javascript
Braze.setCustomUserAttribute("attribute_key", "attribute_value", function(){
    // optional onResult callback
});
```

#### Desactivar atributos personalizados

```javascript
Braze.unsetCustomUserAttribute("attribute_key", function(){
    // optional onResult callback
});
```

#### Matrices de atributos personalizadas

```javascript

// Adds a string to a custom atttribute string array, or creates that array if one doesn't exist.
Braze.addToCustomUserAttributeArray("my-attribute-array", "new or existing value", optionalCallback);

// Removes a string from a custom attribute string array.


Braze.removeFromCustomUserAttributeArray("my-attribute-array", "existing value", optionalCallback);
```
