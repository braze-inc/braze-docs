{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Atribuições padrão do usuário

### Atribuições suportadas

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

### Definindo atributos padrão 

Para definir atributos de usuário coletados automaticamente pelo Braze, você pode usar os métodos de configuração incluídos no SDK.

```dart
braze.setFirstName('Name');
```

## Atributos personalizados do usuário

### Definindo atributos personalizados

Além dos atributos de usuário padrão, o Braze também permite que você defina atributos personalizados usando uma série de diferentes tipos de dados:

{% tabs %}
{% tab String %}
Para definir um atributo personalizado com um valor de `string`:

```dart
braze.setStringCustomUserAttribute("custom string attribute", "string custom attribute");
```

{% endtab %}
{% tab Inteiro %}
Para definir um atributo personalizado com um valor de `integer`:

```dart
// Set Integer Attribute
braze.setIntCustomUserAttribute("custom int attribute key", integer);
// Increment Integer Attribute
braze.incrementCustomUserAttribute("key", integer);
```

{% endtab %}
{% tab Double %}
Para definir um atributo personalizado com um valor de `double`:

```dart
braze.setDoubleCustomUserAttribute("custom double attribute key", double);
```

{% endtab %}
{% tab Booleano %}
Para definir um atributo personalizado com um valor de `boolean`:

```dart
braze.setBoolCustomUserAttribute("custom boolean attribute key", boolean);
```
{% endtab %}

{% tab Data %}
Para definir um atributo personalizado com um valor de `date`:

```dart
braze.setDateCustomUserAttribute("custom date attribute key", date);
```
{% endtab %}
{% tab Vetor %}
Para definir um atributo personalizado com um valor de `array`:

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

### Removendo atributos personalizados

Para remover um atributo personalizado, passe a chave do atributo relevante para o método `unsetCustomUserAttribute`.

```dart
braze.unsetCustomUserAttribute('attribute_key');
```
