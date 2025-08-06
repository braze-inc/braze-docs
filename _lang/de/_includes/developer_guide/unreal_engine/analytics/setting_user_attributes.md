## Standard Attribute für Nutzer:innen

Um ein Standardattribut für einen Nutzer festzulegen, rufen Sie die Methode `GetCurrentUser()` für das gemeinsame Objekt `UBrazeUser` auf, um einen Verweis auf den aktuellen Nutzer:in Ihrer App zu erhalten. Dann können Sie Methoden aufrufen, um ein Nutzer:in-Attribut zu setzen.

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetFirstName(TEXT("Alex"));
    }
});
```

Die folgenden Attribute sollten für das Objekt `UBrazeUser` festgelegt werden:

- `SetFirstName`
- `SetLastName`
- `SetEmail`
- `SetDateOfBirth`
- `SetCountry`
- `SetLanguage`
- `SetHomeCity`
- `SetPhoneNumber`
- `SetGender`

## Angepasste Attribute für Nutzer:innen

Zusätzlich zu den standardmäßigen Nutzer:innen-Attributen können Sie in Braze auch angepasste Attribute unter Verwendung verschiedener Datentypen definieren. Weitere Informationen zu den Segmentierungsoptionen der einzelnen Attribute finden Sie unter [Nutzer:innen-Datenerfassung]({{site.baseurl}}/developer_guide/analytics/).

{% tabs local %}
{% tab String %}
So legen Sie ein angepasstes Attribut mit einem `string` Wert fest:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), TEXT("your_attribute_value"));
```
{% endtab %}

{% tab Ganzzahl %}
So passen Sie ein angepasstes Attribut mit einem `integer` Wert an:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), 42);
```
{% endtab %}

{% tab Gleitkommazahlen %}
Braze behandelt die Werte von `float` und `double` in unserer Datenbank gleich. So legen Sie ein angepasstes Attribut mit einem doppelten Wert fest:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), 3.14);
```
{% endtab %}

{% tab boolean %}
So legen Sie ein angepasstes Attribut mit einem `boolean` Wert fest:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), true);
```
{% endtab %}

{% tab Datum %}
So legen Sie ein angepasstes Attribut mit einem `date` Wert fest:

```cpp
FDateTime YourDateTime = FDateTime(2023, 5, 10);
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), YourDateTime);
```
{% endtab %}

{% tab Array %}
So passen Sie ein angepasstes Attribut mit einem `array` Wert an:

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
Angepasste Attributwerte haben eine maximale Länge von 255 Zeichen; längere Werte werden abgeschnitten.
{% endalert %}

## Einstellen von Nutzer:in-Abonnements

Um ein E-Mail- oder Push-Abonnement für Ihre Nutzer:innen einzurichten, können Sie die folgenden Methoden verwenden.

### E-Mail Abo einstellen

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetEmailSubscriptionType(EBrazeSubscriptionType::Subscribed);
    }
});
```

### Einstellung der Attribution Daten

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetPushSubscriptionType(EBrazeSubscriptionType::OptedIn);
    }
});
```
