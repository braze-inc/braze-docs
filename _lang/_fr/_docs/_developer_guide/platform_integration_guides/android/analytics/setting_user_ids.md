---
nav_title: Paramétrage des identifiants d'utilisateur
article_title: Paramétrage des identifiants utilisateur pour Android/FireOS
platform:
  - Android
  - Pare-feu
page_order: 1
description: "Cet article montre comment définir les identifiants d'utilisateur dans votre application Android, suggérer des conventions de nommage des identifiants d'utilisateur et quelques bonnes pratiques."
---
 
# Paramétrage des identifiants d'utilisateur pour Android/FireOS

{% include archive/setting_user_ids/setting_user_ids.md %}

## Convention de nommage des identifiants d'utilisateur suggérée

{% include archive/setting_user_ids/naming_convention.md %}

### Assigner un ID utilisateur

Vous devriez faire l'appel suivant dès que l'utilisateur est identifié (généralement après la connexion) afin de définir l'identifiant de l'utilisateur :

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(contexte).changeUser(VOTRE_USER_ID_STRING);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(contexte).changeUser(VOTRE_USER_ID_STRING)
```

{% endtab %}
{% endtabs %}

{% alert warning %}
__N'appelez pas `changeUser()` lorsqu'un utilisateur se déconnecte. `changeUser()` ne doit être appelé que lorsque l'utilisateur se connecte dans l'application.__ Le paramétrage de `changeUser()` à une valeur par défaut statique associera TOUTES les activités de l'utilisateur à cet utilisateur par défaut "utilisateur" jusqu'à ce que l'utilisateur se reconnecte.
{% endalert %}

En outre, nous recommandons __contre__ de changer l'ID de l'utilisateur quand un utilisateur se déconnecte, car cela vous rend incapable de cibler l'utilisateur précédemment connecté avec des campagnes de réengagement. Si vous prévoyez plusieurs utilisateurs sur le même appareil, mais que vous voulez seulement cibler l'un d'eux lorsque votre application est dans un état déconnecté, Nous vous recommandons de garder séparément la trace de l'identifiant de l'utilisateur que vous voulez cibler pendant la déconnexion et de revenir à cet identifiant utilisateur dans le cadre du processus de déconnexion de votre application.

Reportez-vous à la documentation [changeUser][4] pour plus d'informations.

**Exemple d'implémentation**

Des informations complètes sur la classe peuvent être trouvées dans le [javadocs][4].

## Meilleures pratiques et notes d'intégration des identifiants utilisateur

{% include archive/setting_user_ids/best_practices.md %}

## Aliasing des utilisateurs

{% include archive/setting_user_ids/aliasing.md platform="Android" %}

[4]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#changeUser-java.lang.String-
[4]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#changeUser-java.lang.String-
