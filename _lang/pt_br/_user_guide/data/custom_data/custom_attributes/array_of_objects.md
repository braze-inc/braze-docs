---
nav_title: Vetor de objetos
article_title: Vetor de objetos
alias: "/array_of_objects/"
page_order: 0
page_type: reference
description: "Este artigo de referência aborda o uso de um vetor de objetos como um tipo de dados para atributos personalizados, incluindo limitações e exemplos de uso." 
---

# Vetor de objetos

> Esta página aborda como usar um vetor de objetos para agrupar atribuições relacionadas. Por exemplo, você pode ter um grupo de objetos de estimação, objetos de música e objetos de conta que pertencem a um usuário. Esses vetores de objetos podem ser usados para personalizar o envio de mensagens com o Liquid ou criar segmentos de público se algum elemento de um objeto corresponder aos critérios.

## Limitações

- Os vetores de objetos destinam-se a atributos personalizados enviados por meio da API. Não há suporte para fazer upload de CSV. Isso ocorre porque as vírgulas no arquivo CSV serão interpretadas como um separador de coluna, e as vírgulas nos valores causarão erros de análise. 
- Os vetores de objetos não têm limite para o número de itens, mas têm um tamanho máximo de 100 KB.
- Nem todos os Braze Partners suportam vetores de objetos. Consulte a [documentação do parceiro]({{site.baseurl}}/partners/home) para confirmar se a integração suporta esse recurso.

A atualização ou remoção de itens em uma matriz exige a identificação do item por chave e valor, portanto, considere a inclusão de um identificador exclusivo para cada item da matriz. A exclusividade tem escopo apenas para o vetor e é útil se você quiser atualizar e remover objetos específicos do vetor. Isso não é aplicado pela Braze.

{% alert tip %}
Para saber mais sobre o uso de vetores de objetos para objetos de atributos do usuário, consulte [Objeto de atributos do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object).
{% endalert %}

## Exemplo de API

{% tabs local %}
{% tab Criar %}

A seguir, um exemplo de `/users/track` com uma matriz `pets`. Para capturar as propriedades dos animais de estimação, envie uma solicitação de API que liste `pets` como um vetor de objetos. Note que foi atribuído a cada objeto um endereço `id` exclusivo que pode ser consultado posteriormente ao fazer atualizações.

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
{% tab Adicionar %}

Adicione outro item à matriz usando o operador `$add`. O exemplo a seguir mostra a adição de mais três objetos pet ao vetor `pets` do usuário.

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
{% tab Atualização %}

Atualize os valores de objetos específicos em um vetor de objetos usando o parâmetro `_merge_objects` e o operador `$update`. Semelhante às atualizações de objetos simples [de atributos personalizados aninhados]({{site.baseurl}}/nested_custom_attribute_support/#api-request-body), essa ação realiza uma mesclagem profunda.

Observe que o site `$update` não pode ser usado para remover uma propriedade aninhada de um objeto dentro de um vetor de objeto. Para fazer isso, você precisará remover todo o item do vetor e, em seguida, adicionar o objeto sem essa chave específica (usando uma combinação de `$remove` e `$add`).

O exemplo a seguir mostra a atualização da propriedade `breed` para `goldfish` para o objeto com um `id` de `4`. Esse exemplo de solicitação também atualiza o objeto com `id` igual a `5` com um novo `name` de `Annette`. Como o parâmetro `_merge_objects` está definido como `true`, todos os outros campos desses dois objetos permanecem iguais.

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
Você deve definir `_merge_objects` como verdadeiro, ou seus objetos serão substituídos. `_merge_objects` é falso por padrão.
{% endalert %}

{% endtab %}
{% tab Remover %}

Remova objetos de um vetor usando o operador `$remove` em combinação com uma chave correspondente (`$identifier_key`) e um valor (`$identifier_value`).

O exemplo a seguir mostra a remoção de qualquer objeto do vetor `pets` que tenha um `id` com o valor `1`, um `id` com o valor `2` e um `type` com o valor `dog`. Se houver vários objetos com o valor `type` de `dog`, todos os objetos correspondentes serão removidos.

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

## Exemplo de SDK

{% tabs local %}
{% tab SDK para Android %}

**Criar**
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

**Adicionar**
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

**Atualizar**
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

**Excluir**
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
{% tab Swift SDK %}

**Criar**
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

**Adicionar**
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

**Atualizar**
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

**Excluir**
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
Atributos personalizados aninhados não são compatíveis com o AppboyKit.
{% endalert %}

{% endtab %}
{% tab SDK da Web %}

**Criar**
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

**Adicionar**
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

**Atualizar**
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

**Excluir**
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

## Modelos Liquid

Você pode usar essa matriz `pets` para personalizar uma mensagem. O exemplo de modelo do Liquid a seguir mostra como fazer referência às propriedades do objeto de atributo personalizado salvas na solicitação anterior da API e usá-las no envio de mensagens.

{% raw %}
```liquid
{% assign pets = {{custom_attribute.${pets}}} %} 
 
{% for pet in pets %}
I have a {{pet.type}} named {{pet.name}}! They are a {{pet.breed}}.
{% endfor %} 
```
{% endraw %}

Nesse cenário, você pode usar o Liquid para percorrer a matriz `pets` e imprimir uma declaração para cada animal de estimação. [Atribua uma variável]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) ao atributo personalizado `pets` e use a notação de ponto para acessar as propriedades de um objeto. Especifique o nome do objeto, seguido por um ponto `.`, seguido pelo nome da propriedade.

## Segmentação

Ao segmentar usuários com base em vetores de objetos, um usuário se qualificará para o segmento se qualquer objeto do vetor corresponder aos critérios. 

Crie um novo segmento e selecione **Atributo personalizado aninhado** como seu filtro. Em seguida, procure e selecione o nome de seu vetor de objetos.

![Filtrar por vetor de objetos.]({% image_buster /assets/img_archive/array_of_objects_segmenting_1.gif %})

Use a notação de ponto para especificar qual campo do vetor de objetos você deseja usar. Inicie o campo de texto com um conjunto vazio de colchetes `[]` para informar ao Braze que você está procurando dentro de um vetor de objetos. Depois disso, adicione um ponto `.`, seguido do nome do campo que você deseja usar.

Por exemplo, se você quiser filtrar o vetor de objetos `pets` com base no campo `type`, digite `[].type` e escolha o tipo de animal de estimação a ser filtrado, como `snake`.

![Filtrar por tipo de animal de estimação igual a cobra.]({% image_buster /assets/img_archive/array_of_objects_segmenting_3.png %})

Ou você pode filtrar por animais de estimação que tenham um `type` de `dog`. Aqui, um usuário tem pelo menos um cachorro, portanto, ele se qualifica para o segmento de "qualquer usuário que tenha pelo menos um animal de estimação do tipo cachorro".

![Filtrar por tipo de animal de estimação igual a cachorro.]({% image_buster /assets/img_archive/array_of_objects_segmenting_2.png %})

### Níveis de aninhamento

Você pode criar um segmento com até um nível de aninhamento de matriz (matriz dentro de outra matriz). Por exemplo, dadas as seguintes atribuições, você pode criar um segmento para `pets[].name` contém `Gus`, mas não pode criar um segmento para `pets[].nicknames[]` contém `Gugu`.

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

## Pontos de dados

Os pontos de dados são consumidos de forma diferente, dependendo do fato de você criar, atualizar ou remover uma propriedade.

{% tabs local %}
{% tab Criar %}

A criação de um novo vetor consome um ponto de dados para cada atribuição em um objeto. Este exemplo custa oito pontos de dados – cada objeto pet tem quatro atribuições e há dois objetos.

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
{% tab Atualização %}

A atualização de uma matriz existente consome um ponto de dados para cada propriedade adicionada. Esse exemplo custa dois pontos de dados, pois atualiza apenas uma propriedade em cada um dos dois objetos.

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
{% tab Remover %}

A remoção de um objeto de um vetor consome um ponto de dados para cada critério de remoção enviado. Esse exemplo custa três pontos de dados, embora você possa estar removendo vários cães com essa declaração.

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

