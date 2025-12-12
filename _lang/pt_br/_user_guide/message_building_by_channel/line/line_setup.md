---
nav_title: Configuração de LINE
article_title: Configuração de linha
description: "Este artigo aborda como configurar o canal Braze LINE, incluindo os pré-requisitos e as próximas etapas sugeridas."
page_type: partner
search_tag: Partner
page_order: 0
channel:
 - LINE
alias: /line/line_setup/
---


# Configuração de LINE

> Este artigo aborda como configurar o canal LINE no Braze, incluindo como configurar usuários, reconciliar IDs de usuário e criar usuários de teste LINE no Braze.

## Pré-requisitos

Você precisará dos seguintes itens para integrar o LINE ao Braze:

- [Conta comercial LINE](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- Status de conta premium ou verificada (necessário para sincronizar seguidores existentes)
   - Veja [as diretrizes de conta do LINE](https://terms2.line.me/official_account_guideline_oth)
- [Conta de desenvolvedores do LINE](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [Canal da API de mensagens do LINE](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

O envio de mensagens LINE a partir do Braze será feito com os créditos de mensagens de sua conta.

## Tipos de contas LINE

| Tipo de conta | Descrição |
| --- | --- |
| Conta não verificada | Uma conta não revisada que pode ser obtida por qualquer pessoa (física ou jurídica). Essa conta é representada por um emblema cinza e não aparecerá nos resultados de pesquisa no aplicativo LINE. |
| Conta verificada | Uma conta que passou na triagem do LINE Yahoo. Essa conta é representada por um emblema azul e aparecerá nos resultados de pesquisa no aplicativo LINE.<br><br>Essa conta está disponível apenas para contas sediadas no Japão, Taiwan, Tailândia e Indonésia.  |
| Conta Premium | Uma conta que passou na triagem do LINE Yahoo. Essa conta é representada por um emblema verde e aparecerá nos resultados de pesquisa no aplicativo LINE. Esse tipo de conta é concedido automaticamente durante a triagem, a critério da LINE. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Tipo de conta necessário

Para sincronizar seguidores no Braze, sua conta LINE precisa ser verificada ou premium. Quando você cria uma conta, seu status padrão é não verificado. Você precisará solicitar a verificação da conta.

### Solicitação de uma conta LINE verificada

{% alert important %}
As contas verificadas estão disponíveis apenas para contas sediadas no Japão, Taiwan, Tailândia e Indonésia.
{% endalert %}

1. Na página da **conta oficial** do LINE, selecione **Configurações**.
2. Em **Status de verificação de divulgação de informações**, selecione **Solicitar verificação de conta**.
3. Insira as informações necessárias.
4. Aguarde uma notificação com os resultados da revisão.

## Integração do LINE

Para configurar atualizações consistentes de usuários, traga os IDs LINE dos usuários existentes e sincronize todos eles com os estados de assinatura do LINE:

1. [Importar ou atualizar usuários conhecidos existentes](#step-1-import-or-update-existing-line-users)
2. [Integrar o canal LINE](#step-2-integrate-line-channel)
3. [Reconciliar IDs de usuários](#step-3-reconcile-user-ids)
4. [Alterar os métodos de atualização do usuário](#step-4-change-your-user-update-methods)
5. [(Opcional) Mesclar perfis de usuário](#step-5-merge-profiles-optional)

## Etapa 1: Importar ou atualizar usuários existentes do LINE

Essa etapa é necessária se você tiver um usuário LINE existente e identificado, pois o Braze extrairá automaticamente o estado da assinatura e atualizará o perfil de usuário correto. Se você não tiver reconciliado anteriormente os usuários com o respectivo LINE ID, ignore esta etapa. 

Você pode importar ou atualizar usuários usando qualquer um dos métodos suportados pelo Braze, incluindo o [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)[importação de CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) ou [ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/cloud_ingestion/). 

Independentemente do método utilizado, atualize o site `native_line_id` para fornecer a ID da LINHA do usuário. Para saber mais sobre o `native_line_id`, consulte [Configuração do usuário](#user-setup).

{% alert note %}
O estado do grupo de assinatura não deve ser especificado e será ignorado. O LINE é a fonte da verdade para o status da assinatura do usuário, que será sincronizado com o Braze por meio da ferramenta de sincronização de assinaturas ou por atualizações de eventos.
{% endalert %}

## Etapa 2: Integrar o canal LINE

Após a conclusão do processo de integração, o Braze puxará automaticamente os seguidores do LINE desse canal para o Braze. Para quaisquer IDs LINE que já estejam associados a um perfil de usuário Braze, cada perfil será atualizado com o status "inscrito", e quaisquer IDs LINE restantes gerarão usuários anônimos. Além disso, os novos seguidores do seu canal LINE terão perfis de usuário não identificados criados quando seguirem o canal.

### Etapa 2.1: Editar configurações de webhook

1. No LINE, acesse a guia **Messaging API** e edite suas **configurações de Webhook**:
   - Defina o **URL do webhook** como `https://anna.braze.com/line/events`.
      - O Braze mudará automaticamente para um URL diferente durante a integração, com base no cluster de seu painel.
   - Ative **Usar webhook** e **Reentrega de webhook**. <br><br> Página de configurações do webhook para verificar ou editar o URL do webhook, ativando ou desativando "Use webhook", "Webhook redelivery" e "Error statistics aggregation".]({% image_buster /assets/img/line/webhook_settings.png %}){: style="max-width:70%;"}
2. Observe as seguintes informações na guia **Providers (Provedores** ):

| Tipo de informação | Localização |
| --- | --- |
| ID do provedor | Selecione seu provedor e, em seguida, vá para **\*Configurações** > **Informações básicas** |
| ID do canal | Selecione seu provedor e vá para **Channels** > seu canal > **Configurações básicas** |
| Canal secreto | Selecione seu provedor e, em seguida, vá para **Channels** > seu canal > **Configurações básicas**. |
| Token de acesso ao canal | Selecione seu provedor e, em seguida, vá para **Channels** > seu canal > **Messaging API**. Se não houver um token de acesso ao canal, selecione **Issue**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="3"}
3\. Vá para a página **Configurações** > **Configurações de resposta** e faça o seguinte:
   - Desativar **a mensagem de saudação**. Isso pode ser tratado no Braze por meio do acionamento no follow.
   - Desative **as mensagens de resposta automática**. Todas as mensagens acionadas devem ser enviadas pelo Braze. Isso não o impedirá de enviar diretamente do console LINE.
   - Ativar **Webhooks**.

Página de configurações de resposta com opções de como sua conta tratará os bate-papos.]({% image_buster /assets/img/line/response_settings.png %}){: style="max-width:80%;"}

### Etapa 2.2: Gerar grupos de assinatura LINE no Braze

1. Vá para a página Braze Technology Partners do LINE e insira as informações que você anotou na guia LINE **Providers (Provedores** do LINE):
   - ID do provedor
   - ID do canal
   - Canal secreto
   - Token de acesso ao canal

Se quiser adicionar a lista de permissões de IP em sua conta LINE, adicione todos os endereços IP listados para seu cluster na [lista de permissões de IP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-allowlisting) à sua lista de permissões.

{% alert important %}
Durante a integração, certifique-se de verificar se o segredo do canal está correto. Se estiver incorreto, pode haver inconsistências no status da assinatura.
{% endalert %}

Página de integração de mensagens do LINE com a seção de integração do LINE.]({% image_buster /assets/img/line/integration.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Após a conexão, o Braze gerará automaticamente um grupo de assinatura do Braze para cada integração LINE adicionada com êxito ao seu espaço de trabalho. <br><br> Todas as alterações em sua lista de seguidores (como novos seguidores ou pessoas que deixaram de segui-lo) serão automaticamente enviadas para o Braze.

\![Seção de grupos de assinatura LINE exibindo um grupo de assinatura para o canal "LINE".]({% image_buster /assets/img/line/line_subscription_groups.png %}){: style="max-width:80%;"}

## Etapa 3: Reconciliar IDs de usuários

Combine os IDs LINE de seus usuários com seus perfis de usuário Braze existentes seguindo as etapas em [Reconciliação de ID de usuário](#user-id-reconciliation).

## Etapa 4: Altere seus métodos de atualização de usuário 

Supondo que você já tenha um método para fornecer atualizações de usuários ao Braze, será necessário atualizá-lo para incluir o novo campo `native_line_id` para que as atualizações de usuários subsequentes enviadas ao Braze incluam esse campo.

Podem existir perfis de usuário não identificados com `native_line_id` no Braze que foram criados como parte do processo de sincronização do status da assinatura ou quando um novo seguidor seguiu seu canal. 

Quando um usuário LINE é identificado em seu aplicativo por meio da [reconciliação de usuários](#user-id-reconciliation) ou por outros meios, você pode direcionar um possível perfil de usuário não identificado no Braze usando o [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) endpoint. Todo perfil de usuário não identificado com um `native_line_id` também tem um alias de usuário `line_id` que pode ser usado para direcionar o perfil de usuário a ser identificado.

Aqui está um exemplo de payload para `/users/identify` que tem como alvo um perfil de usuário não identificado pelo alias de usuário `line_id`: 

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

Se não houver nenhum perfil de usuário existente para o seu `external_id` fornecido, ele será adicionado ao perfil de usuário não identificado, tornando-o identificado. Se houver um perfil de usuário para o `external_id`, todos os atributos que estiverem exclusivamente no perfil de usuário não identificado serão copiados para o perfil de usuário conhecido, incluindo o `native_line_id` e o status de assinatura do usuário.

Você pode atualizar os usuários do LINE que são conhecidos em seu aplicativo por meio do endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) passando seus identificadores externos e `native_line_id`. Se já existir um perfil de usuário não identificado para um usuário e o mesmo `native_line_id` for adicionado a um perfil de usuário diferente por meio de `/users/track`, ele herdará todos os estados de assinatura do perfil de usuário não identificado. No entanto, existirão perfis de usuário duplicados com o mesmo `native_line_id`. Todas as atualizações de assinatura subsequentes de atualizações de eventos atualizarão todos os perfis de acordo. 

Aqui está um exemplo de payload para `/users/track` que atualiza um perfil de usuário pelo ID de usuário externo para adicionar um `native_line_id`: 

{% raw %}
```json
{
   "attributes": [
       {
           "external_id": "known_external_id_from_your_application",
           "native_line_id": "U89f4a626548ccd48482f529a482f138b",
           "other": "attribute"
       }
   ]
}
```
{% endraw %}

## Etapa 5: Mesclar perfis (opcional)

Conforme descrito acima, existe a possibilidade de existirem vários perfis de usuário com o mesmo `native_line_id`. Se os seus métodos de atualização criarem perfis de usuário duplicados, você poderá mesclar perfis de usuário não identificados a perfis de usuário identificados com o ponto de extremidade `/user/merge`. 

Aqui está um exemplo de payload para `/users/merge` que tem como alvo um perfil de usuário não identificado pelo alias de usuário `line_id`:

{% raw %}
```json
{
 "merge_updates": [
   {
     "identifier_to_merge": {
       "user_alias": {
         "alias_name": "U89f4a626548ccd48482f529a482f138b",
         "alias_label": "line_id"
       }
     },
     "identifier_to_keep": {
       "external_id": "known_external_id_from_your_application"
     }
   }
 ]
}
```
{% endraw %}

{% alert tip %}
Para saber mais sobre como gerenciar usuários duplicados no Braze, consulte [Usuários duplicados]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users).
{% endalert %}

## Configuração do usuário

O LINE é a fonte da verdade para os estados de assinatura do usuário. Mesmo que você tenha o ID do LINE para um usuário (`native_line_id`), se esse usuário não tiver seguido o canal do LINE do qual você está enviando, o LINE não entregará mensagens ao usuário.

Para ajudar a gerenciar isso, a Braze oferece ferramentas e lógica que suportam uma base de usuários bem integrada, incluindo sincronização de assinaturas e atualizações de eventos para quem segue e deixa de seguir o LINE.

### Sincronização de assinaturas e lógica de eventos

1. **Ferramenta de sincronização de assinaturas:** Essa ferramenta é implantada automaticamente após uma integração bem-sucedida do canal LINE. Use-o para atualizar perfis existentes e criar novos perfis.<br><br>Todos os perfis de usuário do Braze que têm um `native_line_id` que segue o canal LINE serão atualizados para ter um status de grupo de assinatura de `subscribed`. Qualquer seguidor do canal LINE que não tenha um perfil de usuário Braze com o `native_line_id` terá:<br><br>\- Um perfil de usuário anônimo criado com `native_line_id` definido como o ID da linha do usuário que segue o canal <br>\- Um alias de usuário `line_id` definido para o ID da linha do usuário após o canal <br>\- Um status de grupo de assinatura de `subscribed`

{: start="2"}
2\. **Atualizações do evento:** São usados para atualizar o status da assinatura de um usuário. Quando o Braze receber atualizações de eventos do usuário para o canal LINE integrado e o evento for um follow, o perfil do usuário terá um status de grupo de assinatura de `subscribed`. Se o evento for um unfollow, o perfil do usuário terá um status de grupo de assinatura de `unsubscribed`.<br><br>\- Todos os perfis de usuário Braze com um `native_line_id` correspondente serão atualizados automaticamente. <br>\- Se não houver um perfil de usuário correspondente para um evento, o Braze criará [um usuário anônimo]({{site.baseurl}}/line/user_management/).

## Casos de uso

Esses são casos de uso de como os usuários podem ser atualizados depois que você seguir as etapas de configuração acima.

##### O perfil de usuário existente do Braze já segue o canal LINE

1. O perfil de usuário do Braze é atualizado com um atributo `native_line_id`. Seu status de assinatura padrão é `unsubscribed`.
2. A ferramenta de sincronização de assinatura é executada, descobre que o usuário está seguindo o canal LINE e atualiza o perfil do usuário com o status da assinatura `subscribed`.
3. Se ocorrer alguma alteração no status da assinatura (como o usuário bloquear, deixar de ser amigo ou voltar a seguir o canal), o Braze receberá a atualização do LINE e atualizará o perfil do usuário com o endereço `native_line_id` de acordo.

##### O perfil de usuário existente bloqueou, deixou de ser amigo ou de seguir o canal LINE 

1. O perfil de usuário do Braze é atualizado com um atributo `native_line_id`. Seu status de assinatura padrão é `unsubscribed`.
2. A ferramenta de sincronização de assinatura não descobre que o usuário está seguindo o canal LINE e o status da assinatura do usuário permanece como `unsubscribed`.
3. Se o usuário seguir o canal posteriormente, o Braze receberá a atualização do LINE e atualizará o perfil do usuário com o status da assinatura `subscribed`.

##### A criação do perfil do usuário ocorre depois que a LINE segue

1. O canal recebe um novo seguidor do LINE.
2. O Braze cria um perfil de usuário anônimo com o atributo `native_line_id` definido como o LINE ID do seguidor e um alias de usuário `line_id` definido como o LINE ID do seguidor. O perfil tem um status de assinatura de `subscribed`.
3. O usuário é identificado como tendo o LINE ID por meio da [reconciliação do usuário](#user-id-reconciliation).
  - O perfil de usuário anônimo pode ser identificado usando o [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) ponto de extremidade. As atualizações subsequentes (por meio do [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) ponto de extremidade, [importação de CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) ou [ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/cloud_ingestion/)) para esse perfil de usuário podem direcionar o usuário por esse `external_id` conhecido.

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

  - Um novo perfil de usuário pode ser criado (por meio do [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)[importação de CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) ou [ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/cloud_ingestion/)) definindo o endereço `native_line_id`. Esse novo perfil herdará o estado do status da assinatura do perfil de usuário anônimo existente. Observe que isso resultará em vários perfis compartilhando o mesmo `native_line_id`. Eles podem ser mesclados a qualquer momento usando o ponto de extremidade `/users/merge` no processo descrito na [Etapa 5](#step-5-merge-profiles-optional).

##### A criação do perfil do usuário ocorre antes de o LINE seguir

1. Você adquire um novo usuário e envia as informações para o Braze. Um novo perfil de usuário é criado (perfil 1).
2. O usuário segue sua conta do LINE.
3. O Braze recebe um evento de seguir e cria um perfil de usuário anônimo (perfil 2).
4. O usuário é identificado como tendo o LINE ID por meio da [reconciliação do usuário](#user-id-reconciliation).
5. Você atualiza o perfil 1 para definir o atributo `native_line_id`. Esse perfil herda o estado do status da assinatura do perfil 2.
  - Agora há dois perfis de usuário com o mesmo `native_line_id`. Eles podem ser mesclados a qualquer momento usando o ponto de extremidade `/users/merge` no processo descrito na [Etapa 5](#step-5-merge-profiles-optional).

## Reconciliação de ID de usuário 

Os IDs de linha são recebidos automaticamente pelo Braze quando um usuário segue seu canal ou quando você usa o fluxo de trabalho único de "sincronização de seguidores". As IDs do LINE também são específicas do canal que os usuários seguem, portanto, é improvável que os usuários possam fornecer suas IDs do LINE.

Há duas maneiras de combinar um LINE ID com um perfil de usuário existente no Braze:

- [Login no LINE](#line-login)
- [Vinculação de contas de usuário](#user-account-linking)

### Login do LINE

Esse método usa logins de mídia social para reconciliação. Quando um usuário faz login no seu aplicativo, ele tem a opção de usar o [LINE Login](https://developers.line.biz/en/docs/line-login/overview/) para criar uma conta de usuário ou fazer login.

{% alert note %}
Para adquirir a ID LINE correta para cada usuário, configure o Login LINE com o mesmo provedor da sua conta ou canal oficial LINE integrado ao Brasil.
{% endalert %}

1. Acesse o LINE Developer Console e [solicite permissão para obter os endereços de e-mail dos usuários](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission) que fazem login no seu aplicativo por meio do LINE Login.

2. Siga as etapas apropriadas fornecidas pela LINE para implementar o LINE Login:<br><br>
  - [Direções de aplicativos da Web](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [Direções de aplicativos nativos](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>Certifique-se de incluir o site `email` no [escopo definido](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes) para as solicitações de verificação. 

{: start="3"}
3\. Use a [chamada do token Verify ID](https://developers.line.biz/en/reference/line-login/#verify-id-token) para obter o e-mail do usuário. 

4. Salve o LINE ID do usuário (`native_line_id`) no perfil do usuário com um e-mail correspondente em seu banco de dados ou crie um novo perfil de usuário com o e-mail e o LINE ID do usuário.

5. Envie as informações de usuário novas ou atualizadas para o Braze usando o [endpoint`/user/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users/), [a importação de CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) ou [a ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/cloud_ingestion/).

#### Fluxos de trabalho

##### O seguidor existente usa o login do LINE

**Cenário:** Um usuário anônimo foi criado durante a sincronização inicial do assinante ou após a integração por meio de um evento "follow".

1. O usuário faz login no seu aplicativo usando o LINE Login.
2. O LINE fornece o e-mail do usuário.
3. Você envia ao Braze o usuário atualizado (o perfil de usuário existente com esse e-mail para adicionar o LINE ID) ou atualiza o usuário anônimo com o e-mail.

##### Novo seguidor usa o login do LINE

**Cenário:** Não existe nenhum perfil de usuário no Braze com o ID da linha do usuário.

1. O usuário faz login no seu aplicativo usando o LINE Login.
2. O LINE fornece o e-mail do usuário.
3. Ou você:
  - Atualize um perfil de usuário existente com esse e-mail para que ele também tenha o ID da linha do usuário.
  - Crie um novo perfil de usuário com o e-mail e o LINE ID.
4. Quando o usuário segue sua conta oficial LINE, o Braze recebe um evento de seguir e atualiza o status da assinatura do usuário para `subscribed`.

### Vinculação de contas de usuário 

Esse método permite que os usuários vinculem suas contas LINE à conta de usuário do seu aplicativo. Em seguida, você pode usar o Liquid no Braze, como {% raw %}`{{line_id}}`{% endraw %}, para criar um URL personalizado para o usuário que passa o LINE ID do usuário de volta para o seu site ou aplicativo, que pode então ser associado a um usuário conhecido.

1. Crie um Canvas baseado em ação que se baseie em uma alteração de estado de assinatura e seja acionado quando um usuário se inscrever no seu canal LINE.<br>Canvas que é acionado quando um usuário se inscreve no canal LINE.]({% image_buster /assets/img/line/account_link_1.png %})
2. Crie uma mensagem incentivando os usuários a fazer login no seu site ou aplicativo, passando o LINE ID do usuário como um parâmetro de consulta (por meio do Liquid), como, por exemplo

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3\. Crie uma mensagem de acompanhamento que forneça o código do cupom.
4\. (Opcional) Crie uma campanha baseada em ação ou um Canvas que seja acionado quando o usuário do LINE for identificado para enviar ao usuário o código do cupom. <br>Campanha baseada em ação que é acionada quando o usuário do LINE é identificado.]({% image_buster /assets/img/line/account_link_2.png %})

#### Como funciona

Depois que o usuário faz login, é feita uma alteração em seu site ou aplicativo para que o ID do usuário seja enviado de volta ao Braze para associá-lo ao ID da linha que foi passado como parte do URL, com um código de exemplo como:

```json
const currentUrl = new URL(window.location.href)
const queryParams = new URLSearchParams(currentUrl.search);
const lineUserId = queryParams.get("line_user_id")

if (user && isLoggedIn && lineUserId) {
  post(
   "https://rest.iad-03.braze.com	/users/identify",
   {
     "aliases_to_identify": [
       {
   "external_id": user.getUserId(),
   "user_alias": {
     "alias_name": lineUserId,
     "alias_label": "line_id"
   }
 }
      ]
    }
  )
  braze.logCustomEvent("identified_line_user_for_promotion");
}
```

#### Fluxos de trabalho

##### O usuário existente segue seu canal LINE

**Cenário:** Um usuário existente no Braze segue seu canal no LINE.

1. O LINE envia ao Braze um evento de acompanhamento.
2. O Braze cria um perfil de usuário anônimo com o ID LINE, o alias de usuário `line_id` e o status de grupo de assinatura LINE de `subscribed`.
3. O usuário recebe uma mensagem LINE com um link para o seu site e aplicativo e faz o login. Seu perfil de usuário agora é conhecido.
4. O perfil de usuário anônimo que foi criado é identificado e mesclado por meio do [ ponto de extremidade /users/identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) no perfil de usuário conhecido do usuário. O perfil de usuário conhecido agora contém o ID da LINE e tem um status de assinatura de `subscribed`.
5. (Opcional) O usuário recebe uma mensagem LINE com o código do cupom e o Braze registra o envio no perfil do usuário Braze.

## Criação de usuários de teste LINE no Braze

Você pode testar seu canal LINE antes de configurar [a reconciliação do usuário](#user-id-reconciliation) criando um Canvas ou uma campanha "Who am I".

1. Configure um Canvas que retorne o ID de usuário Braze de um usuário em uma palavra de acionamento específica. <br><br>Exemplo de acionador <br><br>Acionador para enviar a campanha aos usuários que enviaram uma LINE de entrada para um grupo de assinatura específico.]({% image_buster /assets/img/line/trigger.png %}){: style="max-width:80%;"}<br><br>Exemplo de mensagem<br><br>Mensagem LINE informando o ID do usuário do Braze.]({% image_buster /assets/img/line/message.png %}){: style="max-width:40%;"}<br><br>

2. No Braze, você pode usar o Braze ID para pesquisar usuários específicos e modificá-los conforme necessário.

{% alert important %}
Certifique-se de que o Canvas não tenha controle global ou grupos de controle que impeçam os envios.
{% endalert %}


