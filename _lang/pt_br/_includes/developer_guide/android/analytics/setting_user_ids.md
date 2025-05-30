 
# Configuração de IDs de usuário
 
> Este artigo de referência mostra como definir IDs de usuário em seu app para Android ou FireOS, sugere convenções de nomenclatura de IDs de usuário e algumas práticas recomendadas.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## Convenção de nomenclatura de ID de usuário sugerida

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

### Atribuindo uma ID de usuário

Você deve fazer a seguinte chamada assim que o usuário for identificado (geralmente após o login) para definir o ID do usuário:

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
**Não chame `changeUser()` quando um usuário fizer logout. `changeUser()` só deve ser usado quando o usuário fizer o registro no aplicativo.** A configuração de `changeUser()` como um valor padrão estático associará TODAS as atividades do usuário a esse "usuário" padrão até que o usuário acesse novamente.
{% endalert %}

Além disso, recomendamos **não** alterar o ID do usuário quando um usuário se desconecta, pois isso impede o direcionamento de campanhas de reengajamento para o usuário conectado anteriormente. Se você antecipar vários usuários no mesmo dispositivo, mas quiser direcionar apenas um deles quando o aplicativo estiver em um estado de logout, recomendamos acompanhar separadamente o ID de usuário que deseja direcionar enquanto estiver desconectado e voltar para esse ID de usuário como parte do processo de logout do app.

Consulte a documentação de [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html) para saber mais.

## Notas e práticas recomendadas de integração de ID de usuário

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## Alias de usuários

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Android" %}

