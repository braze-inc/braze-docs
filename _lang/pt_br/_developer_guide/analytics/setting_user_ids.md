---
nav_title: Configuração de IDs de usuário
article_title: Configuração de IDs de usuário por meio do Braze SDK
page_order: 1.1
description: "Saiba como definir IDs de usuário por meio do SDK do Braze."

---

# Configuração de IDs de usuário

> Saiba como definir IDs de usuário por meio do SDK do Braze. Esses são identificadores exclusivos que permitem rastrear usuários em dispositivos e plataformas, importar seus dados por meio da [API de dados de usuários]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) e enviar mensagens direcionadas por meio da [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/). Se você não atribuir uma ID exclusiva a um usuário, o Braze atribuirá a ele uma ID anônima - no entanto, você não poderá usar esses recursos até que o faça.

{% alert note %}
Para SDKs de wrapper não listados, use o método nativo relevante do Android ou Swift.
{% endalert %}

## Sobre usuários anônimos

{% multi_lang_include anonymous_users/about_anonymous_users.md %}

## Definição de um ID de usuário

Para definir um ID de usuário, chame o método `changeUser()` depois que o usuário fizer o registro inicial. Os IDs devem ser exclusivos e seguir nossas [práticas recomendadas de nomenclatura](#naming-best-practices).

Se, em vez disso, estiver fazendo hashing de um identificador exclusivo, certifique-se de normalizar a entrada da sua função de hashing. Por exemplo, ao fazer o hash de um endereço de e-mail, remova todos os espaços à esquerda ou à direita e leve em conta a localização.

{% tabs local %}
{% tab ANDROID %}
{% subtabs %}
{% subtab JAVA %}
```java
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING);
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab SWIFT %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.changeUser(userId: "YOUR_USER_ID")
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze changeUser:@"YOUR_USER_ID_STRING"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab WEB %}
Para uma implementação padrão do Web SDK, você pode usar o seguinte método:

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

Se, em vez disso, quiser usar o Google Tag Manager, poderá usar o tipo de tag **Change User (Alterar usuário** ) para chamar o [método`changeUser` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser). Use-o sempre que um usuário registrar-se ou for identificado de outra forma com seu identificador exclusivo `external_id`.

Certifique-se de inserir o ID exclusivo do usuário atual no campo **External User ID (ID do usuário externo** ), normalmente preenchido usando uma variável de camada de dados enviada pelo seu site.

![Uma caixa de diálogo mostrando as definições de configuração da tag de ação do Braze. As configurações incluídas são "tag type" (tipo de tag) e "external user ID" (ID de usuário externo).]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})
{% endtab %}

{% tab CORDOVA %}
```javascript
BrazePlugin.changeUser("YOUR_USER_ID");
```
{% endtab %}

{% tab ROKU %}
```brightscript
m.Braze.setUserId(YOUR_USER_ID_STRING)
```
{% endtab %}

{% tab UNITY %}
```csharp
AppboyBinding.ChangeUser("YOUR_USER_ID_STRING");
```
{% endtab %}

{% tab UNREAL ENGINE %}
```cpp
UBraze->ChangeUser(TEXT("YOUR_USER_ID_STRING"));
```
{% endtab %}
{% endtabs %}

{% alert warning %}
**Não atribua uma ID padrão estática ou ligue para `changeUser()` quando um usuário se desconectar.** Isso impedirá o reengajamento de qualquer usuário registrado anteriormente em dispositivos compartilhados. Em vez disso, mantenha o controle de todos os IDs de usuário separadamente e garanta que o processo de sair do app permita o rastreamento de um usuário previamente conectado. Quando uma nova sessão for iniciada, o Braze atualizará automaticamente os dados do perfil recém-ativo.
{% endalert %}

## Alias do usuário

### Como eles funcionam

{% multi_lang_include anonymous_users/about_user_aliases.md %}

### Definição de um alias de usuário

Um alias de usuário consiste em duas partes: um nome e um rótulo. O nome se refere ao próprio identificador, enquanto o rótulo se refere ao tipo de identificador ao qual ele pertence. Por exemplo, se você tiver um usuário em uma plataforma de suporte ao cliente de terceiros com o ID externo `987654`, poderá atribuir a ele um alias no Braze com o nome `987654` e o rótulo `support_id`, para que possa fazer o rastreamento em todas as plataformas.

{% tabs local %}
{% tab Android %}
{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).getCurrentUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endsubtab %}

{% subtab kotlin %}
```kotlin
Braze.getInstance(context).currentUser?.addAlias(ALIAS_NAME, ALIAS_LABEL)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
Appboy.sharedInstance()?.user.addAlias(ALIAS_NAME, ALIAS_LABEL)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
 [[Appboy sharedInstance].user addAlias:ALIAS_NAME withLabel:ALIAS_LABEL];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab web %}
```javascript
braze.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endtab %}

{% tab API de descanso %}
```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```
{% endtab %}
{% endtabs %}

## Práticas recomendadas de nomenclatura de ID {#naming-best-practices}

Recomendamos que você crie IDs de usuário usando o padrão [UUID (Universally Unique Identifier)](https://en.wikipedia.org/wiki/Universally_unique_identifier), o que significa que são strings de 128 bits aleatórias e bem distribuídas.

Como alternativa, é possível fazer hash de um identificador exclusivo existente (como um nome ou endereço de e-mail) para gerar seus IDs de usuário. Se fizer isso, certifique-se de implementar [a autenticação do SDK]({{site.baseurl}}/developer_guide/authentication/), para evitar a simulação do usuário.

Embora seja essencial nomear corretamente seus IDs de usuário desde o início, você sempre poderá renomeá-los no futuro usando o ponto de extremidade [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/) ponto final.

| Recomendado | Não recomendado |
| ------------ | ----------- |
| 123e4567-e89b-12d3-a456-836199333115 | JonDoe829525552 |
| 8c0b3728-7fa7-4c68-a32e-12de1d3ed2d5 | Anna@email.com |
| f0a9b506-3c5b-4d86-b16a-94fc4fc3f7b0 | CompanyName-1-2-19 |
| 2d9e96a1-8f15-4eaf-bf7b-eb8c34e25962 | jon-doe-1-2-19 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert warning %}
Evite compartilhar detalhes sobre como criar IDs de usuários, pois isso pode expor sua organização a ataques maliciosos ou à remoção de dados.
{% endalert %}
