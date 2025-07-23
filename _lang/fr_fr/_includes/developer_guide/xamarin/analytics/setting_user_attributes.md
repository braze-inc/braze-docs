{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Définition des attributs de l'utilisateur

Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez filtrer et segmenter vos utilisateurs en fonction de ces attributs sur le tableau de bord.

### Attributs par défaut de l’utilisateur

Pour définir les attributs utilisateur collectés automatiquement par Braze, vous pouvez utiliser les méthodes setter fournies avec le SDK. Par exemple, vous pouvez définir le prénom de l'utilisateur :

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).CurrentUser.SetFirstName("first_name");
```

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetFirstName("first_name");
```

{% endtab %}
{% endtabs %}

Les attributs suivants sont pris en charge :

- Prénom
- Nom
- Genre
- Date de naissance
- Ville d’origine
- Pays
- Numéro de téléphone
- E-mail

### Attributs utilisateur personnalisés

Outre nos méthodes prédéfinies d'attribut utilisateur, Braze propose également des attributs personnalisés utilisant `SetCustomUserAttribute` pour suivre les données de vos applications.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).CurrentUser.SetCustomUserAttribute("custom_attribute_key", true);
```

Consultez les [instructions d'intégration Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android) pour une discussion approfondie sur les meilleures pratiques et les interfaces de suivi des attributs.

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetCustomAttributeWithKey("custom_attribute_key", true);
```

Consultez les [instructions d'intégration iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift) pour une discussion approfondie sur les meilleures pratiques et interfaces de suivi des attributs.

{% endtab %}
{% endtabs %}
