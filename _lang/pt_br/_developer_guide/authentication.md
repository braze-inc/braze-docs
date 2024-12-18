---
nav_title: Autenticação do SDK
article_title: Autenticação do SDK
page_order: 12
description: "Este artigo de referência aborda a autenticação do SDK e como ativar esse recurso no SDK da Braze."
platform:
  - iOS
  - Android
  - Web
  
---

# Autenticação do SDK

> A autenticação do SDK permite fornecer prova criptográfica (gerada no lado do servidor) para solicitações do SDK feitas em nome de usuários registrados.

Depois de ativar esse recurso em seu app, você pode configurar o dashboard da Braze para rejeitar quaisquer solicitações com uma assinatura JSON Web Token (JWT) inválida ou ausente, o que inclui:

- Envio de eventos personalizados, atributos, compras e dados de sessão
- Criação de novos usuários em seu espaço de trabalho no Braze
- Atualização das atribuições do perfil de usuário padrão
- Receber ou disparar mensagens

Agora é possível impedir que usuários registrados não autenticados usem a chave de API SDK do seu app para executar ações mal-intencionadas, como simulação de outros usuários.

## Primeiros passos

Há quatro etapas de alto nível para começar:

1. [Integração lado a lado com o servidor](#server-side-integration) \- Gere um par de chaves públicas e privadas e use sua chave privada para criar um JWT para o usuário atualmente registrado.<br><br>
2. [Integração de SDK](#sdk-integration) \- Ative esse recurso no SDK da Braze e solicite o JWT gerado em seu servidor.<br><br>
3. [Adição de chaves públicas](#key-management) \- Adicione sua _chave pública_ ao dashboard do Braze na página **Gerenciar configurações**.<br><br>
4. [Alternar a aplicação no dashboard da Braze](#braze-dashboard) \- Alternar a aplicação desse recurso no dashboard da Braze em uma base de aplicativo por aplicativo.

## Integração lado a lado com o servidor {#server-side-integration}

### Gerar um par de chaves públicas/privadas {#generate-keys}

Gerar um par de chaves públicas/privadas RSA256. A chave pública será eventualmente adicionada ao dashboard da Braze, enquanto a chave privada deverá ser armazenada com segurança em seu servidor.

Recomendamos usar uma chave de RSA com 2048 bits para uso com o algoritmo RS256 JWT.

{% alert warning %}
Lembre-se de manter suas chaves privadas _em sigilo_. Nunca exponha ou codifique sua chave privada em seu app ou site. Qualquer pessoa que conheça sua chave privada pode fazer simulação ou criar usuários em nome do seu aplicativo.
{% endalert %}

### Crie um JSON Web Token para o usuário atual {#create-jwt}

Depois de obter a chave privada, o aplicativo no lado do servidor deve usá-la para retornar um JWT ao seu app ou site para o usuário atualmente registrado.

Normalmente, essa lógica pode ser acessada em qualquer lugar em que o aplicativo normalmente solicite o perfil do usuário atual, como um endpoint de login ou em qualquer lugar em que o aplicativo atualize o perfil do usuário atual.

Ao gerar o JWT, os seguintes campos são esperados:

**Cabeçalho JWT**

| Campo | Obrigatória | Descrição                         |
| ----- | -------- | ----------------------------------- |
| `alg` | Sim  | O algoritmo suportado é `RS256`. |
| `typ` | Sim  | O tipo deve ser igual a `JWT`.        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

**Carga útil do JWT**

| Campo | Obrigatória | Descrição                                                                            |
| ----- | -------- | -------------------------------------------------------------------------------------- |
| `sub` | Sim  | O "assunto" deve ser igual ao ID de usuário que você forneceu ao SDK da Braze ao chamar `changeUser`  |
| `exp` | Sim | A "expiração" de quando você deseja que esse token expire.                                |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Bibliotecas JWT

Para saber mais sobre os tokens da Web JSON ou para navegar pelas muitas bibliotecas de código aberto que simplificam esse processo de fazer login, consulte [https://jwt.io.](https://jwt.io)

## integração de SDK {#sdk-integration}

Esse recurso está disponível a partir das seguintes [versões do SDK]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):

{% sdk_min_versions swift:5.0.0 android:14.0.0 web:3.3.0 %}

{% alert note %}
Para integrações de iOS, esta página detalha as etapas para a Braze Swift SDK. Para obter exemplos de uso no AppboyKit iOS SDK legado, consulte [este arquivo](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/AppDelegate.m) e [este arquivo](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/Utils/SdkAuthDelegate.m).
{% endalert %}

### Ative esse recurso no SDK da Braze.

Quando essa capacitação for ativada, o SDK da Braze anexará o último JWT conhecido do usuário atual às solicitações de rede feitas aos Braze Currents.

{% alert note %}
Não se preocupe, a inicialização apenas com essa opção não afetará a coleta de dados de forma alguma, até que você comece a [aplicar a autenticação](#braze-dashboard) no dashboard do Braze.
{% endalert %}

{% tabs %}
{% tab JavaScript %}
Ao chamar `initialize`, defina a propriedade opcional `enableSdkAuthentication` como `true`.
```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
  enableSdkAuthentication: true,
});
```
{% endtab %}
{% tab Java %}
Ao configurar a instância do Appboy, ligue para `setIsSdkAuthenticationEnabled` para `true`.
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```

Como alternativa, você pode adicionar `<bool name="com_braze_sdk_authentication_enabled">true</bool>` ao seu braze.xml.
{% endtab %}
{% tab KOTLIN %}
Ao configurar a instância do Appboy, chame `setIsSdkAuthenticationEnabled` para `true`.
```kotlin
BrazeConfig.Builder brazeConfigBuilder = BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```

Como alternativa, você pode adicionar `<bool name="com_braze_sdk_authentication_enabled">true</bool>` ao seu braze.xml.
{% endtab %}
{% tab Objective C %}
Para ativar a autenticação do SDK, defina a propriedade `configuration.api.sdkAuthentication` de seu objeto `BRZConfiguration` como `YES` antes de inicializar a instância da Braze:

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                    endpoint:@"{BRAZE_ENDPOINT}"];
configuration.api.sdkAuthentication = YES;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% tab Rápido %}
Para ativar a autenticação do SDK, defina a propriedade `configuration.api.sdkAuthentication` de seu objeto `Braze.Configuration` como `true` ao inicializar o SDK:

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}",
                                        endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab Dart %}
Atualmente, a autenticação do SDK deve ser ativada como parte da inicialização do SDK no código nativo do iOS e do Android. Para ativar a autenticação do SDK no Flutter SDK, siga as integrações para iOS e Android nas outras guias. Depois que a autenticação do SDK for ativada, o restante do recurso poderá ser integrado ao Dart.
{% endtab %}
{% endtabs %}

### Definir o token JWT do usuário atual

Sempre que seu app chamar o método Braze `changeUser`, forneça também o token JWT que foi [gerado no lado do servidor](#braze-dashboard).

Também é possível configurar o token para ser atualizado no meio da sessão para o usuário atual.

{% alert note %}
Lembre-se de que o endereço `changeUser` só deve ser chamado quando a ID do usuário for _realmente alterada_. Você não deve usar esse método como forma de atualizar a assinatura se o ID do usuário não tiver sido alterado.
{% endalert %}

{% tabs %}
{% tab JavaScript %}
Forneça o token JWT ao fazer a chamada [`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser
):

```javascript
import * as braze from "@braze/web-sdk";
braze.changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER");
```

Ou quando você atualiza o token do usuário no meio da sessão:

```javascript
import * as braze from"@braze/web-sdk";
braze.setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER");
```
{% endtab %}
{% tab Java %}

Forneça o token JWT ao fazer a chamada [`appboy.changeUser`](https://braze-inc.github.io/braze-android-sdk/javadocs/com/appboy/Appboy.html#changeUser-java.lang.String-):

```java
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER");
```

Ou quando você atualiza o token do usuário no meio da sessão:

```java
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER");
```
{% endtab %}
{% tab KOTLIN %}

Forneça o token JWT ao fazer a chamada [`appboy.changeUser`](https://braze-inc.github.io/braze-android-sdk/javadocs/com/appboy/Appboy.html#changeUser-java.lang.String-):

```kotlin
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER")
```

Ou quando você atualiza o token do usuário no meio da sessão:

```kotlin
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER")
```
{% endtab %}
{% tab Objective C %}

Forneça o token JWT ao fazer a chamada [`changeUser`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8b369b40e15860b0ec18c0f4b46ac69):

```objc
[AppDelegate.braze changeUser:@"userId" sdkAuthSignature:@"signature"];
```

Ou quando você atualiza o token do usuário no meio da sessão:

```objc
[AppDelegate.braze setSDKAuthenticationSignature:@"signature"];
```
{% endtab %}
{% tab Rápido %}

Forneça o token JWT ao fazer a chamada [`changeUser`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8b369b40e15860b0ec18c0f4b46ac69):

```swift
AppDelegate.braze?.changeUser(userId: "userId", sdkAuthSignature: "signature")
```
Ou quando você atualiza o token do usuário no meio da sessão:

```swift
AppDelegate.braze?.set(sdkAuthenticationSignature: "signature")
```
{% endtab %}
{% tab Dart %}

Forneça o token JWT ao fazer a chamada [`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser):

```dart
braze.changeUser("userId", sdkAuthSignature: "signature")
```
Ou quando você atualiza o token do usuário no meio da sessão:

```dart
braze.setSdkAuthenticationSignature("signature")
```

{% endtab %}
{% endtabs %}

### Registre uma função de retorno de chamada para tokens inválidos {#sdk-callback}

Quando esse recurso for definido como [Obrigatório](#enforcement-options), os cenários a seguir farão com que as solicitações de SDK sejam rejeitadas pelo Braze:
- O JWT expirou no momento em que foi recebido pela API do Braze
- O JWT estava vazio ou ausente
- Falha na verificação do JWT para as chaves públicas que você fez upload para o dashboard da Braze

Você pode usar o site `subscribeToSdkAuthenticationFailures` para se inscrever e ser notificado quando as solicitações do SDK falharem por um desses motivos. Uma função de retorno de chamada contém um objeto com os dados relevantes [`errorCode`](#error-codes)`reason` para o erro, o `userId` da solicitação (se o usuário não for anônimo) e a autenticação `signature` que causou o erro. 

As solicitações com falha serão repetidas periodicamente até que seu app forneça um novo JWT válido. Se o usuário ainda estiver registrado, você poderá usar esse retorno de chamada como uma oportunidade para solicitar um novo JWT do seu servidor e fornecer ao SDK do Braze esse novo token válido.

{% alert tip %}
Esses métodos de retorno de chamada são um ótimo lugar para adicionar seu próprio serviço de monitoramento ou registro de erros para saber com que frequência as solicitações do Braze estão sendo rejeitadas.
{% endalert %}

{% tabs %}
{% tab JavaScript %}
```javascript
import * as braze from"@braze/web-sdk";
braze.subscribeToSdkAuthenticationFailures((error) => {
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  const updated_jwt = await getNewTokenSomehow(error);
  braze.setSdkAuthenticationSignature(updated_jwt);
});
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(this).subscribeToSdkAuthenticationFailures(error -> {
    // TODO: Optionally log to your error-reporting service
    // TODO: Check if the error user matches the currently logged-in user
    String newToken = getNewTokenSomehow(error);
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
Braze.getInstance(this).subscribeToSdkAuthenticationFailures({ error: BrazeSdkAuthenticationErrorEvent ->
    // TODO: Optionally log to your error-reporting service
    // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
    val newToken: String = getNewTokenSomehow(error)
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken)
})
```
{% endtab %}
{% tab Objective C %}

```objc
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
braze.sdkAuthDelegate = delegate;
AppDelegate.braze = braze;

// Method to implement in delegate
- (void)braze:(Braze *)braze sdkAuthenticationFailedWithError:(BRZSDKAuthenticationError *)error {
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  NSLog(@"Invalid SDK Authentication signature.");
  NSString *newSignature = getNewSignatureSomehow(error);
  [AppDelegate.braze setSDKAuthenticationSignature:newSignature];
}
```
{% endtab %}
{% tab Swift %}

```swift
let braze = Braze(configuration: configuration)
braze.sdkAuthDelegate = delegate
AppDelegate.braze = braze

// Method to implement in delegate
func braze(_ braze: Braze, sdkAuthenticationFailedWithError error: Braze.SDKAuthenticationError) {
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  print("Invalid SDK Authentication signature.")
  let newSignature = getNewSignatureSomehow(error)
  AppDelegate.braze?.set(sdkAuthenticationSignature: newSignature)
}
```
{% endtab %}
{% tab Dart %}
```dart
braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  print("Invalid SDK Authentication signature.")
  let newSignature = getNewSignatureSomehow(error)
  braze.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% endtabs %}

## Gerenciamento de chaves públicas {#key-management}

### Adição de uma chave pública

Você pode adicionar até três chaves públicas para cada app: uma primária, uma secundária e uma terciária. Você também pode adicionar a mesma chave a mais de um app, se necessário. Para adicionar uma chave pública:

1. Acesse o dashboard da Braze e selecione (**Configurações** > **Configurações do app**).
2. Escolha um aplicativo da sua lista de aplicativos disponíveis.
3. Em **Autenticação do SDK**, selecione **Adicionar chave pública**.
4. Insira uma descrição opcional, cole sua chave pública e selecione **Adicionar chave pública**.

### Atribuir uma nova chave primária

Para atribuir uma chave secundária ou terciária como sua nova chave primária:

1. Acesse o dashboard da Braze e selecione (**Configurações** > **Configurações do app**).
2. Escolha um aplicativo da sua lista de aplicativos disponíveis.
3. Em **Autenticação do SDK**, escolha uma chave e selecione **Gerenciar** > **Tornar chave primária**.

### Exclusão de uma tecla

Para excluir uma chave primária, primeiro [atribua uma nova primária](#assign-a-new-primary-key) e, em seguida, exclua sua chave. Para excluir uma chave não primária:

1. Acesse o dashboard da Braze e selecione (**Configurações** > **Configurações do app**).
2. Escolha um aplicativo da sua lista de aplicativos disponíveis.
3. Em **Autenticação do SDK**, escolha uma chave não primária e selecione **Gerenciar** > **Excluir chave pública**.

## Ativação no dashboard do Braze {#braze-dashboard}

Quando [a integração do lado a lado do servidor](#server-side-integration) e [a integração do SDK](#sdk-integration) estiverem concluídas, você poderá começar a ativar esse recurso para esses apps específicos.

Lembre-se de que as solicitações de SDK continuarão a fluir normalmente sem autenticação, a menos que a configuração de autenticação do SDK do app esteja definida como **Obrigatória** no dashboard da Braze.

Se algo der errado com sua integração (por exemplo, seu app está passando tokens incorretamente para o SDK ou seu servidor está gerando tokens inválidos), desative esse recurso no dashboard do Braze e os dados voltarão a fluir normalmente sem verificação.

### Opções de aplicação {#enforcement-options}

Na página **Manage Settings (Configurações de gerenciamento)** do dashboard, cada app tem três estados de autenticação do SDK que controlam como a Braze verifica as solicitações.

| Configuração| Descrição|
| ------ | ---------- |
| **Desativado** | O Braze não verificará o JWT fornecido para um usuário. (Configuração padrão)|
| **Opcional** | A Braze verificará as solicitações de usuários registrados, mas não rejeitará solicitações inválidas. |
| **Obrigatória** | O Braze verificará as solicitações de usuários registrados e rejeitará JWTs inválidos.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/sdk-auth-settings.png %})

A configuração **Opcional** é uma maneira útil de monitorar o impacto potencial que esse recurso terá no tráfego do SDK do seu app.

As assinaturas JWT inválidas serão relatadas nos estados **Optional (opcional** ) e **Required (obrigatório** ), mas somente o estado **Required (obrigatório** ) rejeitará as solicitações do SDK, fazendo com que os apps tentem novamente e solicitem novas assinaturas.

## Análise de dados {#analytics}

Cada app mostrará um detalhamento dos erros de autenticação do SDK coletados enquanto esse recurso estiver no estado **Opcional** e **Obrigatório**.

Os dados estão disponíveis em tempo real, e você pode passar o mouse sobre os pontos do gráfico para ver um detalhamento dos erros de uma determinada data.

![Um gráfico que mostra o número de instâncias de erros de autenticação. Também são exibidos o número total de erros, o tipo de erro e o intervalo de datas ajustável.]({% image_buster /assets/img/sdk-auth-analytics.png %}){: style="max-width:80%"}

## Códigos de erro {#error-codes}

| Código de erro| Motivo do erro | Descrição |
| --------  | ------------ | ---------  |
| 10 | `EXPIRATION_REQUIRED` | A expiração é um campo obrigatório para o uso do Braze.|
| 20 | `DECODING_ERROR` | Chave pública não correspondente ou um erro geral não detectado.|
| 21 | `SUBJECT_MISMATCH` | Os assuntos esperados e os reais não são os mesmos.|
| 22 | `EXPIRED` | O token fornecido expirou.|
| 23 | `INVALID_PAYLOAD` | A carga útil do token é inválida.|
| 24 | `INCORRECT_ALGORITHM` | O algoritmo do token não é compatível.|
| 25 | `PUBLIC_KEY_ERROR` | A chave pública não pôde ser convertida no formato adequado.|
| 26 | `MISSING_TOKEN` | Nenhum token foi fornecido na solicitação.|
| 27 | `NO_MATCHING_PUBLIC_KEYS` | Nenhuma chave pública corresponde ao token fornecido.|
| 28 | `PAYLOAD_USER_ID_MISMATCH` | Nem todos os IDs de usuário na carga útil da solicitação correspondem ao que é necessário.|
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3 role="presentation" }

## Perguntas frequentes {#faq}

#### Esse recurso precisa ser ativado em todos os meus aplicativos ao mesmo tempo? {#faq-app-by-app}

Não, esse recurso pode ser ativado para aplicativos específicos e não precisa ser usado em todos os seus aplicativos, de uma só vez.

#### O que acontece com os usuários que ainda estão em versões mais antigas do meu app? {#faq-sdk-backward-compatibility}

Quando você começar a aplicar esse recurso, as solicitações feitas por versões mais antigas do app serão rejeitadas pela Braze e tentadas novamente pelo SDK. Depois que os usuários fizerem upgrade do app para uma versão compatível, essas solicitações enfileiradas começarão a ser aceitas novamente.

Se possível, empurre os usuários para fazer o upgrade como faria para qualquer outra atualização obrigatória. Como alternativa, você pode manter o recurso [opcional](#enforcement-options) até perceber que uma porcentagem aceitável de usuários fez upgrade.

#### Que expiração devo usar ao gerar tokens JWT? {#faq-expiration}

Recomendamos usar o valor mais alto de duração média da sessão, expiração do cookie/token da sessão ou a frequência com que o aplicativo atualizaria o perfil do usuário atual.

#### O que acontece se um JWT expirar no meio da sessão de um usuário? {#faq-jwt-expiration}

Se o token de um usuário expirar no meio da sessão, o SDK tem uma [função de retorno de chamada](#sdk-callback) que será invocada para que seu app saiba que um novo token JWT é necessário para continuar enviando dados para a Braze.

#### O que acontecerá se minha integração lado a lado com o servidor falhar e eu não puder mais criar um JWT? {#faq-server-downtime}

Se o seu servidor não for capaz de fornecer tokens JWT ou se você notar algum problema de integração, sempre será possível desativar o recurso no dashboard da Braze.

Uma vez desativada, todas as solicitações pendentes do SDK que falharem serão eventualmente repetidas pelo SDK e aceitas pela Braze.

#### Por que esse recurso usa chaves públicas/privadas em vez de segredos compartilhados? {#faq-shared-secrets}

Ao usar segredos compartilhados, qualquer pessoa com acesso a esse segredo compartilhado, como a página do dashboard do Braze, poderá gerar tokens e se passar por seus usuários finais.

Em vez disso, usamos chaves públicas/privadas para que nem mesmo os Colaboradores do Braze (muito menos os usuários do seu dashboard) tenham acesso às suas chaves privadas.

#### Como as solicitações rejeitadas serão tentadas novamente? {#faq-retry-logic}

Quando uma solicitação for rejeitada devido a um erro de autenticação, o SDK invocará o retorno de chamada usado para atualizar a assinatura JWT do usuário. 

As solicitações serão repetidas periodicamente usando uma abordagem de backoff exponencial. Após 50 tentativas consecutivas sem sucesso, as novas tentativas serão pausadas até o início da próxima sessão. Cada SDK também tem um método para solicitar manualmente uma descarga de dados.

