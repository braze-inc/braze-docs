---
nav_title: Conjunto de objetos
article_title: Conjunto de objetos
alias: "/array_of_objects/"
page_order: 0
page_type: reference
description: "Este artículo de referencia cubre el uso de un array de objetos como tipo de datos para atributos personalizados, incluyendo limitaciones y ejemplos de uso." 
---

# Conjunto de objetos

> Esta página explica cómo utilizar una matriz de objetos para agrupar atributos relacionados. Por ejemplo, puede tener un grupo de objetos mascota, objetos canción y objetos cuenta que pertenezcan todos a un usuario. Estas matrices de objetos pueden utilizarse para personalizar sus mensajes con Liquid, o crear segmentos de audiencia si algún elemento de un objeto coincide con los criterios.

## Limitaciones

- Las matrices de objetos están pensadas para atributos personalizados enviados a través de la API. No es posible cargar archivos CSV. Esto se debe a que las comas en el archivo CSV se interpretarán como un separador de columnas, y las comas en los valores causarán errores de análisis. 
- Las matrices de objetos no tienen límite en el número de elementos, pero sí un tamaño máximo de 100 KB.
- No todos los socios Braze admiten matrices de objetos. Consulta la [documentación del socio]({{site.baseurl}}/partners/home) para confirmar si la integración admite esta característica.

Actualizar o eliminar elementos de una matriz requiere identificar el elemento por clave y valor, así que considera la posibilidad de incluir un identificador único para cada elemento de la matriz. La unicidad se aplica sólo a la matriz y es útil si desea actualizar y eliminar objetos específicos de su matriz. Braze no lo aplica.

{% alert tip %}
Para más información sobre el uso de matrices de objetos para objetos de atributos de usuario, consulta [Objeto de atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object).
{% endalert %}

## Ejemplo de API

{% tabs local %}
{% tab Crear %}

A continuación se muestra un ejemplo de `/users/track` con una matriz `pets`. Para capturar las propiedades de las mascotas, envíe una solicitud de API que enumere `pets` como una matriz de objetos. Tenga en cuenta que a cada objeto se le ha asignado un único `id` al que se puede hacer referencia posteriormente al realizar actualizaciones.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Añadir %}

Añade otro elemento a la matriz utilizando el operador `$add`. El siguiente ejemplo muestra la adición de tres objetos mascota más a la matriz `pets` del usuario.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$add": [
          {
            "id": 3,
            "type": "dog",
            "breed": "corgi",
            "name": "Doug"
          },
          {
            "id": 4,
            "type": "fish",
            "breed": "salmon",
            "name": "Larry"
          },
           {
            "id": 5,
            "type": "bird",
            "breed": "parakeet",
            "name": "Mary"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Actualización %}

Actualice los valores de objetos específicos dentro de una matriz utilizando el parámetro `_merge_objects` y el operador `$update`. De forma similar a las actualizaciones de objetos de [atributos personalizados anidados]({{site.baseurl}}/nested_custom_attribute_support/#api-request-body) simples, esto realiza una fusión profunda.

Ten en cuenta que `$update` no puede utilizarse para eliminar una propiedad anidada de un objeto dentro de una matriz. Para ello, tendrás que eliminar todo el elemento de la matriz y luego añadir el objeto sin esa clave específica (utilizando una combinación de `$remove` y `$add`).

El siguiente ejemplo muestra la actualización de la propiedad `breed` a `goldfish` para el objeto con un `id` de `4`. Este ejemplo de solicitud también actualiza el objeto con `id` igual a `5` con un nuevo `name` de `Annette`. Dado que el parámetro `_merge_objects` se establece en `true`, todos los demás campos de estos dos objetos siguen siendo los mismos.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```

{% alert warning %}
Debe establecer `_merge_objects` como verdadero, o sus objetos se sobrescribirán. `_merge_objects` es falso por defecto.
{% endalert %}

{% endtab %}
{% tab Eliminar %}

Elimina objetos de una matriz utilizando el operador `$remove` en combinación con una clave (`$identifier_key`) y un valor (`$identifier_value`) coincidentes.

El siguiente ejemplo muestra la eliminación de cualquier objeto de la matriz `pets` que tenga un `id` con un valor de `1`, un `id` con un valor de `2`, y un `type` con un valor de `dog`. Si hay varios objetos con el valor `type` de `dog`, se eliminarán todos los objetos coincidentes.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

## Ejemplo de SDK

{% tabs local %}
{% tab SDK para Android %}

**Crear**
```kotlin
val json = JSONArray()
    .put(JSONObject()
        .put("id", 1)
        .put("type", "dog")
        .put("breed", "beagle")
        .put("name", "Gus"))
    .put(JSONObject()
        .put("id", 2)
        .put("type", "cat")
        .put("breed", "calico")
        .put("name", "Gerald")
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json)
}
```

**Añadir**
```kotlin
val json = JSONObject()
    .put("\$add", JSONArray()
        .put(JSONObject()
            .put("id", 3)
            .put("type", "dog")
            .put("breed", "corgi")
            .put("name", "Doug"))
        .put(JSONObject()
            .put("id", 4)
            .put("type", "fish")
            .put("breed", "salmon")
            .put("name", "Larry"))
        .put(JSONObject()
            .put("id", 5)
            .put("type", "bird")
            .put("breed", "parakeet")
            .put("name", "Mary")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```

**Actualizar**
```kotlin
val json = JSONObject()
    .put("\$update", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 4)
            .put("\$new_object", JSONObject()
                .put("breed", "goldfish")
            )
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 5)
            .put("\$new_object", JSONObject()
                .put("name", "Annette")
            )
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```

**Eliminar**
```kotlin
val json = JSONObject()
    .put("\$remove", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 1)
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 2)
        )
        .put(JSONObject()
            .put("\$identifier_key", "type")
            .put("\$identifier_value", "dog")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```

{% endtab %}
{% tab SDK de Swift %}

**Crear**
```swift
let json: [[String: Any?]] = [
  [
    "id": 1,
    "type": "dog",
    "breed": "beagle",
    "name": "Gus"
  ],
  [
    "id": 2,
    "type": "cat",
    "breed": "calico",
    "name": "Gerald"
  ]
]

braze.user.setCustomAttribute(key: "pets", array: json)
```

**Añadir**
```swift
let json: [String: Any?] = [
  "$add": [
    [
      "id": 3,
      "type": "dog",
      "breed": "corgi",
      "name": "Doug"
    ],
    [
      "id": 4,
      "type": "fish",
      "breed": "salmon",
      "name": "Larry"
    ],
    [
      "id": 5,
      "type": "bird",
      "breed": "parakeet",
      "name": "Mary"
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```

**Actualizar**
```swift
let json: [String: Any?] = [
  "$update": [
    [
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": [
        "breed": "goldfish"
      ]
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": [
        "name": "Annette"
      ]
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```

**Eliminar**
```swift
let json: [String: Any?] = [
  "$remove": [
    [
      "$identifier_key": "id",
      "$identifier_value": 1,
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 2,
    ],
    [
      "$identifier_key": "type",
      "$identifier_value": "dog",
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```

{% alert important %}
Los atributos personalizados anidados no son compatibles con AppboyKit.
{% endalert %}

{% endtab %}
{% tab SDK Web %}

**Crear**
```javascript
import * as braze from "@braze/web-sdk";
const json = [{
  "id": 1,
  "type": "dog",
  "breed": "beagle",
  "name": "Gus"
}, {
  "id": 2,
  "type": "cat",
  "breed": "calico",
  "name": "Gerald"
}];
braze.getUser().setCustomUserAttribute("pets", json);
```

**Añadir**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$add": [{
    "id":  3,
    "type":  "dog",
    "breed":  "corgi",
    "name":  "Doug",
  }, {
    "id":  4,
    "type":  "fish",
    "breed":  "salmon",
    "name":  "Larry",
  }, {
    "id":  5,
    "type":  "bird",
    "breed":  "parakeet",
    "name":  "Mary",
  }]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```

**Actualizar**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$update": [
    {
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": {
        "breed": "goldfish"
      }
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": {
        "name": "Annette"
      }
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```

**Eliminar**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$remove": [
    {
      "$identifier_key": "id",
      "$identifier_value": 1,
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 2,
    },
    {
      "$identifier_key": "type",
      "$identifier_value": "dog",
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```

{% endtab %}
{% endtabs %}

## Plantillas de Liquid

Puede utilizar esta matriz `pets` para personalizar un mensaje. El siguiente ejemplo de plantilla de Liquid muestra cómo hacer referencia a las propiedades del objeto de atributo personalizado guardadas de la solicitud de API anterior y utilizarlas en su mensajería.

{% raw %}
```liquid
{% assign pets = {{custom_attribute.${pets}}} %} 
 
{% for pet in pets %}
I have a {{pet.type}} named {{pet.name}}! They are a {{pet.breed}}.
{% endfor %} 
```
{% endraw %}

En este caso, puede utilizar Liquid para recorrer la matriz `pets` e imprimir una declaración para cada mascota. [Asigne una variable]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) al atributo personalizado `pets` y utilice la notación de puntos para acceder a las propiedades de un objeto. Especifica el nombre del objeto, seguido de un punto `.`, seguido del nombre de la propiedad.

## Segmentación

Cuando se segmentan usuarios basándose en matrices de objetos, un usuario cumplirá los requisitos para el segmento si cualquier objeto de la matriz coincide con los criterios. 

Cree un nuevo segmento y seleccione **Atributo personalizado anidado** como filtro. A continuación, busque y seleccione el nombre de su matriz de objetos.

![Filtrar por matriz de objetos.]({% image_buster /assets/img_archive/array_of_objects_segmenting_1.gif %})

Utilice la notación por puntos para especificar qué campo de la matriz de objetos desea utilizar. Inicie el campo de texto con un conjunto vacío de corchetes `[]` para indicar a Braze que está buscando dentro de una matriz de objetos. Después, añade un punto `.`, seguido del nombre del campo que quieras utilizar.

Por ejemplo, si desea filtrar la matriz de objetos `pets` basándose en el campo `type`, introduzca `[].type` y elija el tipo de mascota por el que desea filtrar, como `snake`.

![Filtrar por tipo de mascota igual a serpiente.]({% image_buster /assets/img_archive/array_of_objects_segmenting_3.png %})

O puedes filtrar por mascotas que tengan un `type` de `dog`. En este caso, un usuario tiene al menos un perro, por lo que entra en el segmento de "cualquier usuario que tenga al menos una mascota de tipo perro".

![Filtrar por tipo de mascota igual a perro.]({% image_buster /assets/img_archive/array_of_objects_segmenting_2.png %})

### Niveles de anidamiento

Puede crear un segmento con un máximo de un nivel de anidamiento de matrices (matriz dentro de otra matriz). Por ejemplo, dados los siguientes atributos, puede hacer que un segmento para `pets[].name` contenga `Gus`, pero no puede hacer que un segmento para `pets[].nicknames[]` contenga `Gugu`.

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus",
          "nicknames": [
            "Gugu",
            "Gusto"
          ]
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald",
          "nicknames": [
            "GeGe",
            "Gerry"
          ]
        }
      ]
    }
  ]
}
```
{% endraw %}

## Puntos de datos

Los puntos de datos se consumen de forma diferente dependiendo de si se crea, actualiza o elimina una propiedad.

{% tabs local %}
{% tab Crear %}

La creación de una nueva matriz consume un punto de datos por cada atributo de un objeto. Este ejemplo cuesta ocho puntos de datos: cada objeto mascota tiene cuatro atributos y hay dos objetos.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Actualización %}

La actualización de una matriz existente consume un punto de datos por cada propiedad añadida. Este ejemplo cuesta dos puntos de datos, ya que sólo actualiza una propiedad en cada uno de los dos objetos.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Eliminar %}

Eliminar un objeto de un array consume un punto de datos por cada criterio de eliminación que envíes. Este ejemplo cuesta tres puntos de datos, a pesar de que puede estar eliminando varios perros con esta declaración.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```

{% endtab %}
{% endtabs %}

