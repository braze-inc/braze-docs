{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Atribuições padrão do usuário

Para definir as atribuições do usuário coletadas automaticamente pelo Braze, você pode usar os métodos setter fornecidos com o SDK.

```dart
braze.setFirstName('Name');
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

{% alert important %}
Todos os valores de string, como nome, sobrenome, país e cidade natal, estão limitados a 255 caracteres.
{% endalert %}

## Atributos personalizados do usuário

### Definindo atributos personalizados

Além dos atributos padrão de usuários, o Braze também permite definir atributos personalizados usando vários tipos de dados diferentes:

{% tabs %}
{% tab String %}
Para definir um atributo personalizado com um valor `string`:

```dart
braze.setStringCustomUserAttribute("custom string attribute", "string custom attribute");
```

{% endtab %}
{% tab Inteiro %}
Para definir um atributo personalizado com um valor `integer`:

```dart
// Set Integer Attribute
braze.setIntCustomUserAttribute("custom int attribute key", integer);
// Increment Integer Attribute
braze.incrementCustomUserAttribute("key", integer);
```

{% endtab %}
{% tab Double %}
Para definir um atributo personalizado com um valor `double`:

```dart
braze.setDoubleCustomUserAttribute("custom double attribute key", double);
```

{% endtab %}
{% tab Booleano %}
Para definir um atributo personalizado com um valor `boolean`:

```dart
braze.setBoolCustomUserAttribute("custom boolean attribute key", boolean);
```
{% endtab %}

{% tab Data %}
Para definir um atributo personalizado com um valor `date`:

```dart
braze.setDateCustomUserAttribute("custom date attribute key", date);
```
{% endtab %}
{% tab Vetor %}
Para definir um atributo personalizado com um valor `array`:

```dart
// Adding to an Array
braze.addToCustomAttributeArray("key", "attribute");
// Removing an item from an Array
braze.removeFromCustomAttributeArray("key", "attribute");
```
{% endtab %}
{% endtabs %}

{% alert important %}
Os valores de atributos personalizados têm um comprimento máximo de 255 caracteres; valores mais longos serão truncados.
{% endalert %}

### Desconfigurando um atributo personalizado

```dart
braze.unsetCustomUserAttribute('attribute_key');
```
