{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Atributos predeterminados del usuario

### Atributos admitidos

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

{% alert important %}
Todos los valores de cadena como nombre, apellidos, país y ciudad de residencia están limitados a 255 caracteres.
{% endalert %}

### Configuración de atributos predeterminados 

Para configurar los atributos de usuario recogidos automáticamente por Braze, puedes utilizar los métodos de configuración incluidos en el SDK.

```dart
braze.setFirstName('Name');
```

## Atributos personalizados del usuario

### Establecer atributos personalizados

Además de los atributos de usuario predeterminados, Braze también te permite definir atributos personalizados utilizando distintos tipos de datos:

{% tabs %}
{% tab Cadena %}
Para establecer un atributo personalizado con un valor `string`:

```dart
braze.setStringCustomUserAttribute("custom string attribute", "string custom attribute");
```

{% endtab %}
{% tab Entero %}
Para establecer un atributo personalizado con un valor `integer`:

```dart
// Set Integer Attribute
braze.setIntCustomUserAttribute("custom int attribute key", integer);
// Increment Integer Attribute
braze.incrementCustomUserAttribute("key", integer);
```

{% endtab %}
{% tab Doble %}
Para establecer un atributo personalizado con un valor `double`:

```dart
braze.setDoubleCustomUserAttribute("custom double attribute key", double);
```

{% endtab %}
{% tab Booleano %}
Para establecer un atributo personalizado con un valor `boolean`:

```dart
braze.setBoolCustomUserAttribute("custom boolean attribute key", boolean);
```
{% endtab %}

{% tab Fecha %}
Para establecer un atributo personalizado con un valor `date`:

```dart
braze.setDateCustomUserAttribute("custom date attribute key", date);
```
{% endtab %}
{% tab Matriz %}
Para establecer un atributo personalizado con un valor `array`:

```dart
// Adding to an Array
braze.addToCustomAttributeArray("key", "attribute");
// Removing an item from an Array
braze.removeFromCustomAttributeArray("key", "attribute");
```
{% endtab %}
{% endtabs %}

{% alert important %}
Los valores de atributos personalizados tienen una longitud máxima de 255 caracteres; los valores más largos se truncarán.
{% endalert %}

### Desactivar atributos personalizados

Para desactivar un atributo personalizado, pasa la clave del atributo correspondiente al método `unsetCustomUserAttribute`.

```dart
braze.unsetCustomUserAttribute('attribute_key');
```
