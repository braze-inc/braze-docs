 
# Définir des ID utilisateur
 
> Cet article de référence montre comment définir des ID utilisateur dans votre application Android ou FireOS, des conventions de dénominations d’ID utilisateur suggérées, ainsi que certaines bonnes pratiques.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## Convention de dénomination des ID utilisateurs suggérée

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

### Attribuer un ID utilisateur

Vous devez effectuer l’appel suivant dès que l’utilisateur est identifié (généralement après s’être connecté) afin de définir l’ID utilisateur :

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING)
```

{% endtab %}
{% endtabs %}

{% alert warning %}
**N’appelez pas `changeUser()` lorsqu’un utilisateur se déconnecte. `changeUser()` ne doit être appelé que lorsque l’utilisateur se connecte à l’application.** Définir `changeUser()` sur une valeur par défaut statique associera TOUTES les activités de l’utilisateur avec cet « utilisateur » par défaut jusqu’à ce qu’il se connecte à nouveau.
{% endalert %}

De plus, nous vous recommandons de ne **pas** changer l'ID utilisateur lorsqu'un utilisateur se déconnecte, car cela vous empêche de cibler l'utilisateur précédemment connecté avec des campagnes de réengagement. Si vous anticipez plusieurs utilisateurs sur le même appareil, mais que vous souhaitez uniquement cibler l’un d’eux lorsque votre application est à l’état déconnecté, nous vous recommandons de suivre séparément l’ID utilisateur que vous souhaitez cibler durant la déconnexion et de basculer vers cet ID utilisateur dans le cadre du processus de déconnexion de votre application.

Pour plus d’informations, reportez-vous à la documentation [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html).

## Meilleures pratiques et remarques sur l’intégration de l’ID utilisateur

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## Alias d’utilisateurs

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Android" %}

