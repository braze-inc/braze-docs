 
# Nutzer:innen IDs festlegen
 
> Dieser referenzierte Artikel zeigt Ihnen, wie Sie Nutzer:innen IDs in Ihrer Android oder FireOS App einrichten, welche Namenskonventionen für Nutzer:innen vorgeschlagen werden und wie Sie am besten vorgehen.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## Vorgeschlagene Namenskonvention für Nutzer:in

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

### Zuweisung einer Nutzer:in ID

Sobald der Nutzer identifiziert ist (in der Regel nach der Anmeldung), sollten Sie den folgenden Aufruf tätigen, um die Nutzer-ID festzulegen:

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
**Rufen Sie `changeUser()` nicht auf, wenn sich ein:e Nutzer abmeldet. `changeUser()` sollte nur aufgerufen werden, wenn sich der oder die Nutzer:in in die Anwendung einloggt.** Wenn Sie `changeUser()` auf einen statischen Standardwert setzen, werden ALLE Nutzeraktivitäten mit diesem Standardnutzer verknüpft, bis sich der oder die Nutzer:in sich erneut anmeldet.
{% endalert %}

Außerdem empfehlen wir, die ID bei der Abmeldung **nicht** zu ändern, da Sie dann den zuvor angemeldeten Nutzer nicht mit erneuten Interaktionskampagnen ansprechen können. Wenn Sie mit mehreren Benutzern auf demselben Gerät rechnen, aber nur einen von ihnen ansprechen möchten, wenn sich Ihre App im abgemeldeten Zustand befindet, empfehlen wir Ihnen, die Benutzer-ID, die Sie ansprechen möchten, während Sie abgemeldet sind, separat zu verfolgen und im Rahmen des Abmeldevorgangs Ihrer App wieder zu dieser Benutzer-ID zu wechseln.

Weitere Informationen finden Sie in der Dokumentation zu [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html).

## Best Practices und Hinweise zur Integration von Nutzer:in

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## User:innen Aliasing

{% multi_lang_include archive/setting_user_ids/aliasing.md plattform="Android" %}

