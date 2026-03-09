## Estados da inscrição push {#push-sub-states}

Um "estado de inscrição por push" no Braze identifica **a** preferência global **de** um **usuário** quanto ao seu desejo de receber notificações por push. Como o estado da inscrição é baseado no usuário, ele não é específico de nenhum aplicativo individual. Os estados de inscrição tornam-se sinalizadores úteis ao decidir quais usuários devem ser direcionados para notificações por push.

{% alert note %}
O estado da inscrição push de um usuário se aplica a todo o seu perfil de usuário, que inclui todos os dispositivos do usuário.
{% endalert %}

As seguintes opções de estado de inscrição existem: `Subscribed`, `Opted-In` e `Unsubscribed`.

Por padrão, para que seu usuário receba suas mensagens por push, o estado de inscrição por push deve ser `Subscribed` ou `Opted-In`, e eles devem ter o push em primeiro plano habilitado. Você pode substituir essa configuração, se necessário, ao criar uma mensagem.

|Estado de aceitação|Descrição|
|---|---|
|`Subscribed`| Estado padrão da inscrição push quando um perfil de usuário é criado no Braze. |
|`Opted-In`| Um usuário expressou explicitamente uma preferência por receber notificações por push. O Braze move automaticamente o estado de aceitação de um usuário para `Opted-In` se o usuário aceitar um prompt de push em nível de sistema operacional.<br><br>Isso não se aplica a usuários do Android 12 ou inferior.|
|`Unsubscribed`| Um usuário cancelou explicitamente a inscrição de push através do seu aplicativo ou outros métodos fornecidos pela sua marca. Por padrão, as campanhas de push do Braze visam apenas usuários que estão `Subscribed` ou `Opted-in` para push.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
O Braze não altera automaticamente o estado da inscrição push de um usuário para `Unsubscribed`. Lembre-se de que se o estado de inscrição por push de um usuário for `Unsubscribed`, então o filtro de `Foreground Push Enabled` do usuário na segmentação é `false`.
{% endalert %}

### Atualização dos estados da inscrição push {#update-push-subscription-state}

Revise as seguintes maneiras de atualizar o estado de inscrição por push de um usuário:

#### Aceitação automática (padrão)

Por padrão, o Braze define o estado da inscrição push de um usuário como `Opted-In` quando ele autoriza pela primeira vez as notificações por push para o seu app. A Braze também faz isso quando um usuário reativa as permissões push nas configurações do sistema após tê-las desativado anteriormente.

{% tabs local %}
{% tab android %}
Para desativar esse comportamento padrão, adicione a seguinte propriedade ao arquivo `braze.xml` do seu projeto do Android Studio:

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab swift %}
A partir da [versão 7.5.0 do Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0), você pode desativar ou personalizar ainda mais esse comportamento adicionando a configuração `optInWhenPushAuthorized` ao arquivo `AppDelegate.swift` do seu projeto Xcode:

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### integração de SDK

Você pode atualizar o estado da inscrição de um usuário com o Braze SDK usando o método `setPushNotificationSubscriptionType` na [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html) ou [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:)). Por exemplo, você pode usar esse método para criar uma página de configurações no seu app em que os usuários possam ativar ou desativar manualmente as notificações por push.

#### API REST

Você pode atualizar o estado de inscrição de um usuário com a API REST do Braze usando o endpoint [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para atualizar seu atributo [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object).

### Verificação do estado da inscrição push

![Perfil de usuário para John Doe com seu estado de inscrição push definido como Subscribed (Inscrito).]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Você pode verificar o estado de inscrição por push de um usuário com o Braze de qualquer uma das seguintes maneiras:

* **Perfil do usuário:** Você pode acessar perfis de usuários individuais através do dashboard do Braze na página **[Pesquisa de Usuários]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)**. Depois de encontrar o perfil de um usuário (por meio de endereço de e-mail, número de telefone ou ID de usuário externo), é possível selecionar a guia **Engajamento** para visualizar e ajustar manualmente o estado da inscrição de um usuário.
* **Exportação da API REST:** Você pode exportar perfis de usuários individuais em formato JSON usando os endpoints de exportação [Usuários por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) ou [Usuários por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). O Braze retorna um objeto de tokens de push que contém informações de habilitação de push por dispositivo.