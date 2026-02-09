## Attributs par défaut de l'utilisateur

### Attributs pris en charge

Les attributs suivants doivent être définis sur l’objet `UBrazeUser` :

- `SetFirstName`
- `SetLastName`
- `SetEmail`
- `SetDateOfBirth`
- `SetCountry`
- `SetLanguage`
- `SetHomeCity`
- `SetPhoneNumber`
- `SetGender`

### Définition des attributs par défaut

Pour définir un attribut par défaut pour un utilisateur, appelez la méthode `GetCurrentUser()` sur l'objet partagé `UBrazeUser` pour obtenir une référence à l'utilisateur actuel de votre application. Vous pouvez ensuite appeler des méthodes pour définir un attribut utilisateur.

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetFirstName(TEXT("Alex"));
    }
});
```

## Attributs utilisateur personnalisés

Outre les attributs par défaut, Braze vous permet de définir des attributs personnalisés à l'aide de différents types de données. Pour plus d'informations sur l'option de segmentation de chaque attribut, voir [Collecte de données sur les utilisateurs]({{site.baseurl}}/developer_guide/analytics/).

{% tabs local %}
{% tab chaîne de caractères %}
Pour définir un attribut personnalisé avec une valeur `string`:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), TEXT("your_attribute_value"));
```
{% endtab %}

{% tab entier %}
Pour définir un attribut personnalisé avec une valeur `integer`:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), 42);
```
{% endtab %}

{% tab points flottants %}
Braze traite les valeurs `float` et `double` de la même manière dans notre base de données. Pour définir un attribut personnalisé avec une valeur double :

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), 3.14);
```
{% endtab %}

{% tab booléen %}
Pour définir un attribut personnalisé avec une valeur `boolean`:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), true);
```
{% endtab %}

{% tab date %}
Pour définir un attribut personnalisé avec une valeur `date`:

```cpp
FDateTime YourDateTime = FDateTime(2023, 5, 10);
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), YourDateTime);
```
{% endtab %}

{% tab réseau %}
Pour définir un attribut personnalisé avec une valeur `array`:

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
Les valeurs d’attribut personnalisé ont une longueur maximale de 255 caractères ; les valeurs plus longues seront tronquées.
{% endalert %}

## Configurer les abonnements des utilisateurs

Pour configurer un abonnement e-mail ou push pour vos utilisateurs, vous pouvez utiliser les méthodes suivantes.

### Configuration de l'abonnement à l'e-mail

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetEmailSubscriptionType(EBrazeSubscriptionType::Subscribed);
    }
});
```

### Définition des données d'attribution

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetPushSubscriptionType(EBrazeSubscriptionType::OptedIn);
    }
});
```
