{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Registro de atributos personalizados

O Braze fornece métodos para atribuir atribuições aos usuários. Você poderá filtrar e segmentar seus usuários de acordo com essas atribuições no dashboard.

### Atribuições padrão do usuário

Para definir as atribuições do usuário coletadas automaticamente pelo Braze, você pode usar os métodos setter fornecidos com o SDK.

```javascript
Braze.setFirstName("Name");
```

Há suporte para as seguintes atribuições:

- Nome
- Sobrenome
- Gênero
- Data de nascimento
- Cidade
- País
- Número de telefone
- Idioma
- E-mail

Todos os valores de string, como nome, sobrenome, país e cidade natal, estão limitados a 255 caracteres.

### Atributos personalizados do usuário

Além de nossos métodos predefinidos de atributos de usuários, o Braze também fornece [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) para rastrear dados de seus aplicativos. 

```javascript
Braze.setCustomUserAttribute("attribute_key", "attribute_value", function(){
    // optional onResult callback
});
```

#### Desativação de atributos personalizados

```javascript
Braze.unsetCustomUserAttribute("attribute_key", function(){
    // optional onResult callback
});
```

#### Matrizes de atributos personalizados

```javascript

// Adds a string to a custom atttribute string array, or creates that array if one doesn't exist.
Braze.addToCustomUserAttributeArray("my-attribute-array", "new or existing value", optionalCallback);

// Removes a string from a custom attribute string array.


Braze.removeFromCustomUserAttributeArray("my-attribute-array", "existing value", optionalCallback);
```
