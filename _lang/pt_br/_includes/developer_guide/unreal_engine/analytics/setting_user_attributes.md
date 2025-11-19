## Atribuições padrão do usuário

### Atribuições suportadas

Os seguintes atributos devem ser definidos no objeto `UBrazeUser`:

- `SetFirstName`
- `SetLastName`
- `SetEmail`
- `SetDateOfBirth`
- `SetCountry`
- `SetLanguage`
- `SetHomeCity`
- `SetPhoneNumber`
- `SetGender`

### Definição de atribuições padrão

Para definir uma atribuição padrão para um usuário, chame o método `GetCurrentUser()` no objeto compartilhado `UBrazeUser` para obter uma referência ao usuário atual do seu app. Em seguida, é possível chamar métodos para definir uma atribuição de usuário.

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetFirstName(TEXT("Alex"));
    }
});
```

## Atributos personalizados do usuário

Além dos atributos padrão de usuários, o Braze também permite definir atributos personalizados usando vários tipos de dados diferentes. Para saber mais sobre a opção de segmentação de cada atributo, consulte [Coleta de dados de usuários]({{site.baseurl}}/developer_guide/analytics/).

{% tabs local %}
{% tab string %}
Para definir um atributo personalizado com um valor `string`:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), TEXT("your_attribute_value"));
```
{% endtab %}

{% tab inteiro %}
Para definir um atributo personalizado com um valor `integer`:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), 42);
```
{% endtab %}

{% tab pontos flutuantes %}
Braze trata os valores `float` e `double` da mesma forma em nosso banco de dados. Para definir um atributo personalizado com um valor duplo:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), 3.14);
```
{% endtab %}

{% tab booleano %}
Para definir um atributo personalizado com um valor `boolean`:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), true);
```
{% endtab %}

{% tab data %}
Para definir um atributo personalizado com um valor `date`:

```cpp
FDateTime YourDateTime = FDateTime(2023, 5, 10);
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), YourDateTime);
```
{% endtab %}

{% tab matriz %}
Para definir um atributo personalizado com um valor `array`:

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
Os valores de atributos personalizados têm um comprimento máximo de 255 caracteres; valores mais longos serão truncados.
{% endalert %}

## Configuração de inscrições de usuários

Para configurar uma inscrição por e-mail ou push para seus usuários, use os seguintes métodos.

### Configuração do envio de e-mail

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetEmailSubscriptionType(EBrazeSubscriptionType::Subscribed);
    }
});
```

### Configuração dos dados de atribuição

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetPushSubscriptionType(EBrazeSubscriptionType::OptedIn);
    }
});
```
