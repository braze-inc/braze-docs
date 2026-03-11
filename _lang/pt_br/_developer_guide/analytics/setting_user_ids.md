---
nav_title: Definir IDs de usuários
article_title: Definir IDs de usuários através do SDK do Braze
page_order: 1.1
description: "Aprenda como definir IDs de usuários através do SDK do Braze."

---

# Definir IDs de usuários

> Aprenda como definir IDs de usuários através do SDK do Braze. Estes são identificadores únicos que permitem rastrear usuários em dispositivos e plataformas, importar seus dados através da [API de dados de usuários]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data), e enviar mensagens direcionadas através da [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/). Se você não atribuir um ID único a um usuário, o Braze atribuirá a ele um ID anônimo em vez disso—no entanto, você não poderá usar esses recursos até que o faça.

{% alert note %}
Para SDKs wrapper não listados, use o método nativo relevante do Android ou Swift em vez disso.
{% endalert %}

## Sobre usuários anônimos

{% multi_lang_include anonymous_users/about_anonymous_users.md %}

## Definindo um ID de usuário

Para definir um ID de usuário, chame o método `changeUser()` após o usuário fazer login inicialmente. IDs devem ser únicos e seguir nossas [melhores práticas de nomenclatura](#naming-best-practices).

Se você estiver hashando um identificador único em vez disso, certifique-se de normalizar a entrada da sua função de hash. Por exemplo, ao hashar um endereço de e-mail, remova quaisquer espaços em branco no início ou no final e leve em conta a localização.

{% tabs local %}
{% tab WEB %}
Para uma implementação padrão do SDK Web, você pode usar o seguinte método:

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

Se você gostaria de usar o Google Tag Manager em vez disso, pode usar o tipo de tag **Alterar Usuário** para chamar o [`changeUser` método](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser). Use-o sempre que um usuário fizer login ou for identificado de outra forma com seu identificador único `external_id`.

Certifique-se de inserir o ID exclusivo do usuário atual no campo **External User ID (ID do usuário externo** ), normalmente preenchido usando uma variável de camada de dados enviada pelo seu site.

![Uma caixa de diálogo mostrando as definições de configuração da tag de ação do Braze. As configurações incluídas são "tipo de tag" e "ID de usuário externo".]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})
{% endtab %}

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

{% tab REACT NATIVE %}
```javascript
Braze.changeUser("YOUR_USER_ID_STRING");
```
{% endtab %}
{% endtabs %}

{% alert note %}
Chamar `changeUser()` aciona um flush de dados como parte do fechamento da sessão do usuário atual. O SDK automaticamente faz flush de quaisquer dados pendentes do usuário anterior antes de mudar para o novo usuário, então você não precisa solicitar manualmente um flush de dados antes de chamar `changeUser()`.
{% endalert %}

{% alert warning %}
**Não atribua um ID padrão estático ou chame `changeUser()` quando um usuário fizer logout.** Fazer isso impedirá que você reengaje qualquer usuário que tenha feito login anteriormente em dispositivos compartilhados. Em vez disso, mantenha o controle de todos os IDs de usuários separadamente e garanta que o processo de logout do seu app permita a troca de volta para um usuário que já estava logado. Quando uma nova sessão começa, o Braze atualizará automaticamente os dados do perfil recém-ativo.
{% endalert %}

## Alias do usuário

### Como eles funcionam

{% multi_lang_include anonymous_users/about_user_aliases.md %}

### Definindo um alias de usuário

Um alias de usuário consiste em duas partes: um nome e um rótulo. O nome refere-se ao identificador em si, enquanto o rótulo refere-se ao tipo de identificador ao qual pertence. Por exemplo, se você tiver um usuário em uma plataforma de suporte ao cliente de terceiros com o ID externo `987654`, você pode atribuir a ele um alias no Braze com o nome `987654` e o rótulo `support_id`, para que você possa rastreá-lo entre plataformas.

{% tabs local %}
{% tab web %}
```javascript
braze.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endtab %}

{% tab android %}
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

{% tab rest api %}
```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```
{% endtab %}

{% tab react native %}
```javascript
Braze.addAlias("ALIAS_NAME", "ALIAS_LABEL");
```
{% endtab %}
{% endtabs %}

## Melhores práticas para nomeação de ID {#naming-best-practices}

Recomendamos que você crie IDs de usuários usando o padrão [Identificador Único Universal (UUID)](https://en.wikipedia.org/wiki/Universally_unique_identifier), o que significa que são strings de 128 bits que são aleatórias e bem distribuídas.

Alternativamente, você pode hash um identificador único existente (como um nome ou endereço de e-mail) para gerar seus IDs de usuários. Se você fizer isso, tenha certeza de implementar [autenticação do SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication/), para que você possa evitar a simulação de usuários.

{% alert warning %}
Não use um valor previsível ou um número crescente para seu ID de usuário. Isso pode expor sua organização a ataques maliciosos ou exfiltração de dados.

Para maior segurança, use [autenticação do SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication/).
{% endalert %}

Embora seja essencial que você nomeie corretamente seus IDs de usuários desde o início, você sempre pode renomeá-los no futuro usando o endpoint [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/).

| Tipos de ID não recomendados | Exemplo não recomendado |
| ------------ | ----------- |
| ID de perfil visível do usuário ou nome de usuário | JonDoe829525552 |
| Endereço de e-mail | Anna@email.com |
| ID de usuário auto-incremental | 123 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert warning %}
Evite compartilhar detalhes sobre como você cria IDs de usuários, pois isso pode expor sua organização a ataques maliciosos ou exfiltração de dados.
{% endalert %}
