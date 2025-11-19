## Atributos predeterminados del usuario

### Atributos admitidos

Los siguientes atributos deben establecerse en el objeto `UBrazeUser`:

- `SetFirstName`
- `SetLastName`
- `SetEmail`
- `SetDateOfBirth`
- `SetCountry`
- `SetLanguage`
- `SetHomeCity`
- `SetPhoneNumber`
- `SetGender`

### Configuración de atributos predeterminados

Para establecer un atributo predeterminado para un usuario, llama al método `GetCurrentUser()` en el objeto compartido `UBrazeUser` para obtener una referencia al usuario actual de tu aplicación. A continuación, puedes llamar a los métodos para establecer un atributo de usuario.

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetFirstName(TEXT("Alex"));
    }
});
```

## Atributos personalizados del usuario

Además de los atributos predeterminados de usuario, Braze también te permite definir atributos personalizados utilizando varios tipos de datos diferentes. Para más información sobre la opción de segmentación de cada atributo, consulta [Recopilación de datos de usuario]({{site.baseurl}}/developer_guide/analytics/).

{% tabs local %}
{% tab cadena %}
Para establecer un atributo personalizado con un valor `string`:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), TEXT("your_attribute_value"));
```
{% endtab %}

{% tab entero %}
Para establecer un atributo personalizado con un valor `integer`:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), 42);
```
{% endtab %}

{% tab puntos flotantes %}
Braze trata de la misma manera los valores `float` y `double` dentro de nuestra base de datos. Para establecer un atributo personalizado con un valor doble:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), 3.14);
```
{% endtab %}

{% tab booleano %}
Para establecer un atributo personalizado con un valor `boolean`:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), true);
```
{% endtab %}

{% tab fecha %}
Para establecer un atributo personalizado con un valor `date`:

```cpp
FDateTime YourDateTime = FDateTime(2023, 5, 10);
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), YourDateTime);
```
{% endtab %}

{% tab matriz %}
Para establecer un atributo personalizado con un valor `array`:

```cpp
// Setting a custom attribute with an array value
TArray<FString> Values = {TEXT("value1"), TEXT("value2")};
UBrazeUser->SetCustomAttributeArray(TEXT("array_name"), Values);

// Adding to a custom attribute with an array value
UBrazeUser->AddToCustomAttributeArray(TEXT("array_name"), TEXT("value3"));

// Removing a value from an array type custom attribute
UBrazeUser->RemoveFromCustomAttributeArray(TEXT("array_name"), TEXT("value2"));
```
{% endtab %}
{% endtabs %}

{% alert important %}
Los valores de atributos personalizados tienen una longitud máxima de 255 caracteres; los valores más largos se truncarán.
{% endalert %}

## Configuración de las suscripciones de los usuarios

Para configurar una suscripción por correo electrónico o push para tus usuarios, puedes utilizar los siguientes métodos.

### Configuración de la suscripción por correo electrónico

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetEmailSubscriptionType(EBrazeSubscriptionType::Subscribed);
    }
});
```

### Configuración de los datos de atribución

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetPushSubscriptionType(EBrazeSubscriptionType::OptedIn);
    }
});
```
