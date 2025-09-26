---
nav_title: Configuração do LINE
article_title: Configuração do LINE
description: "Este artigo aborda como configurar o canal Braze LINE, incluindo os pré-requisitos e as próximas etapas sugeridas."
page_type: partner
search_tag: Partner
page_order: 0
channel:
 - LINE
alias: /line/line_setup/
---


# Configuração do LINE

> Este artigo aborda como configurar o canal LINE no Braze, incluindo como configurar usuários, reconciliar IDs de usuários e criar usuários de teste LINE no Braze.

## Pré-requisitos

Você precisará dos seguintes itens para integrar o LINE ao Braze:

- [Conta comercial LINE](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- Status de conta premium ou verificada (necessário para sincronizar os seguidores existentes)
   - Veja [as diretrizes de conta do LINE](https://terms2.line.me/official_account_guideline_oth)
- [Conta de desenvolvedor do LINE](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [Canal de envio de mensagens do LINE](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

O envio de mensagens LINE a partir do Braze será feito com os créditos de mensagens de sua conta.

## Tipos de contas LINE

| Tipo de conta | Descrição |
| --- | --- |
| Conta não verificada | Uma conta não revisada que pode ser obtida por qualquer pessoa (física ou jurídica). Essa conta é representada por um emblema cinza e não aparecerá nos resultados de pesquisa no app LINE. |
| Conta verificada | Uma conta que passou na triagem do LINE Yahoo. Essa conta é representada por um emblema azul e aparecerá nos resultados de pesquisa no app LINE.<br><br>Essa conta está disponível apenas para contas sediadas no Japão, Taiwan, Tailândia e Indonésia.  |
| Conta Premium | Uma conta que passou na triagem do LINE Yahoo. Essa conta é representada por um emblema verde e aparecerá nos resultados de pesquisa no app LINE. Esse tipo de conta é concedido automaticamente durante a triagem, a critério da LINE. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Tipo de conta necessário

Para sincronizar seguidores na Braze, sua conta LINE precisa ser verificada ou premium. Quando você cria uma conta, seu status padrão é não verificado. Você precisará solicitar a verificação da conta.

### Solicitação de uma conta LINE verificada

{% alert important %}
As contas verificadas estão disponíveis apenas para contas sediadas no Japão, Taiwan, Tailândia e Indonésia.
{% endalert %}

1. Na página da **conta oficial** do LINE, selecione **Configurações**.
2. Em **Status de verificação de divulgação de informações**, selecione **Solicitar verificação de conta**.
3. Insira as informações necessárias.
4. Aguarde uma notificação com os resultados da revisão.

## Integração do LINE

Para configurar atualizações consistentes de usuários, traga os IDs LINE dos usuários existentes e sincronize todos eles com os estados de inscrição do LINE:

1. [Importar ou atualizar usuários conhecidos existentes](#step-1-import-or-update-existing-line-users)
2. [Integrar o canal LINE](#step-2-integrate-line-channel)
3. [Reconciliar IDs de usuários](#step-3-reconcile-user-ids)
4. [Alterar os métodos de atualização do usuário](#step-4-change-your-user-update-methods)
5. [(Opcional) Mesclar perfis de usuário](#step-5-merge-profiles-optional)

## Etapa 1: Importação ou atualização de usuários existentes do LINE

Essa etapa é necessária se você tiver um usuário LINE existente e identificado, pois o Braze extrairá automaticamente o estado da inscrição e atualizará o perfil de usuário correto. Se não tiver reconciliado anteriormente os usuários com o respectivo LINE ID, pule esta etapa. 

Você pode importar ou atualizar usuários usando qualquer um dos métodos suportados pela Braze, incluindo o endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), [importação de CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) ou [ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/cloud_ingestion/). 

Independentemente do método utilizado, atualize o site `native_line_id` para fornecer o ID da LINE do usuário. Para saber mais sobre o `native_line_id`, consulte [Configuração do usuário](#user-setup).

{% alert note %}
O estado do grupo de inscrições não deve ser especificado e será ignorado. O LINE é a fonte da verdade para o status da inscrição do usuário, que será sincronizado com o Braze por meio da ferramenta de sincronização de inscrição ou por atualizações de eventos.
{% endalert %}

## Etapa 2: Integrar o canal LINE

Depois que o processo de integração for concluído, o Braze puxará automaticamente os seguidores do LINE desse canal para o Braze. Para quaisquer IDs LINE que já estejam associados a um perfil de usuário Braze, cada perfil será atualizado com o status "inscrito", e quaisquer IDs LINE restantes gerarão usuários anônimos. Além disso, os novos seguidores do seu canal LINE terão perfis de usuário não identificados criados quando seguirem o canal.

### Etapa 2.1: Editar configurações de webhook

1. No LINE, acesse a guia **Envio de mensagens API** e edite suas **configurações de webhook**:
   - Defina o **URL do webhook** como `https://anna.braze.com/line/events`.
      - A Braze mudará automaticamente para um URL diferente ao fazer a integração, com base no cluster de seu dashboard.
   - Ative **Usar webhook** e **Reentrega de webhook**. <br><br> ![Página de configurações do webhook para verificar ou editar o URL do webhook, ativar ou desativar "Use webhook", "Webhook redelivery" e "Error statistics aggregation".]({% image_buster /assets/img/line/webhook_settings.png %}){: style="max-width:70%;"}
2. Observe as seguintes informações na guia **Providers (Provedores** ):

| Tipo de informação | Local |
| --- | --- |
| ID do provedor | Selecione seu provedor e acesse **\*Configurações** > **Informações básicas** |
| ID do canal | Selecione seu provedor e, em seguida, acesse **Canais** > seu canal > **Configurações básicas** |
| Segredo do canal | Selecione seu provedor e acesse **Channels (Canais** ) > your channel (seu canal) > **Basic settings (Configurações básicas**). |
| Token de acesso ao canal | Selecione seu provedor e acesse **Canais** > seu canal > **API de envio de mensagens**. Se não houver um token de acesso ao canal, selecione **Problema**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="3"}
3\. Acesse a página **Configurações** > **Configurações de resposta** e faça o seguinte:
   - Desative **Mensagem de saudação**. Isso pode ser tratado na Braze por meio do disparo no follow.
   - Desative o **envio de mensagens de resposta automática**. Todos os envios de mensagens disparadas devem ser feitos por meio do Braze. Isso não impedirá você de enviar diretamente do console LINE.
   - Ativar **Webhooks**.

![Página de configurações de resposta com opções de como sua conta tratará os bate-papos.]({% image_buster /assets/img/line/response_settings.png %}){: style="max-width:80%;"}

### Etapa 2.2: Gerar grupos de inscrições LINE no Braze

1. Acesse a página Braze Technology Partners do LINE e insira as informações que você notou na guia LINE **Providers** (Provedores do LINE):
   - ID do provedor
   - ID do canal
   - Segredo do canal
   - Token de acesso ao canal

Se quiser adicionar a lista de permissões de IP em sua conta LINE, adicione todos os endereços IP listados para seu cluster na [lista de permissões de IP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-allowlisting) à sua lista de permissões.

{% alert important %}
Durante a integração, certifique-se de verificar se o segredo do canal está correto. Se estiver incorreto, pode haver inconsistências no status da inscrição.
{% endalert %}

![Página de integração de envio de mensagens do LINE com a seção de integração do LINE.]({% image_buster /assets/img/line/integration.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Após a conexão, o Braze gerará automaticamente um grupo de inscrições do Braze para cada integração LINE adicionada com sucesso ao seu espaço de trabalho. <br><br> Todas as alterações em sua lista de seguidores (como novos seguidores ou pessoas que deixaram de segui-lo) serão automaticamente pushadas para o Braze.

![Seção de grupos de inscrições LINE exibindo um grupo de inscrições para o canal "LINE".]({% image_buster /assets/img/line/line_subscription_groups.png %}){: style="max-width:80%;"}

## Etapa 3: Reconciliar IDs de usuários

Combine os IDs LINE de seus usuários com seus perfis de usuário Braze existentes seguindo as etapas em [Reconciliação de ID de usuário](#user-id-reconciliation).

## Etapa 4: Altere seus métodos de atualização de usuário 

Supondo que você já tenha um método para fornecer atualizações de usuários ao Braze, será necessário atualizá-lo para incluir o novo campo `native_line_id` para que as atualizações subsequentes de usuários enviadas ao Braze incluam esse campo.

Podem existir no Braze perfis de usuários não identificados com `native_line_id` que foram criados como parte do processo de sincronização do status da inscrição ou quando um novo seguidor seguiu seu canal. 

Quando um usuário LINE é identificado em seu aplicativo por meio da [reconciliação de usuários](#user-id-reconciliation) ou por outros meios, é possível direcionar um possível perfil de usuário não identificado no Braze usando o [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) endpoint. Cada perfil de usuário não identificado com um `native_line_id` também tem um alias de usuário `line_id` que pode ser usado para direcionar o perfil de usuário a ser identificado.

Aqui está um exemplo de carga útil para `/users/identify` que direciona um perfil de usuário não identificado pelo alias de usuário `line_id`: 

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

Se não houver nenhum perfil de usuário existente para o seu `external_id` fornecido, ele será adicionado ao perfil de usuário não identificado, tornando-o identificado. Se houver um perfil de usuário para o `external_id`, todas as atribuições que estiverem exclusivamente no perfil de usuário não identificado serão copiadas para o perfil de usuário conhecido, incluindo `native_line_id` e o status de inscrição do usuário.

É possível atualizar os usuários do LINE que são conhecidos em seu aplicativo por meio do endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) passando seus identificadores externos e `native_line_id`. Se já existir um perfil de usuário não identificado para um usuário e o mesmo `native_line_id` for adicionado a um perfil de usuário diferente por meio de `/users/track`, ele herdará todos os estados de inscrição do perfil de usuário não identificado. No entanto, haverá perfis de usuário duplicados com o mesmo `native_line_id`. Todas as atualizações de inscrição subsequentes de atualizações de eventos atualizarão todos os perfis de acordo. 

Aqui está um exemplo de carga útil para `/users/track` que atualiza um perfil de usuário pelo ID de usuário externo para adicionar um `native_line_id`: 

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

Aqui está um exemplo de carga útil para `/users/merge` que direciona um perfil de usuário não identificado pelo alias de usuário `line_id`:

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

O LINE é a fonte da verdade para os estados de inscrição do usuário. Mesmo que você tenha a ID do LINE para um usuário (`native_line_id`), se esse usuário não tiver seguido o canal do LINE do qual você está enviando, o LINE não entregará mensagens ao usuário.

Para ajudar a gerenciar isso, a Braze oferece ferramentas e lógica que suportam uma base de usuários bem integrada, incluindo sincronização de inscrições e atualizações de eventos para quem segue e deixa de seguir o LINE.

### Sincronização de inscrições e lógica de eventos

1. **Ferramenta de sincronização de inscrições:** Essa ferramenta é implantada automaticamente após uma integração bem-sucedida do canal LINE. Use-o para atualizar perfis existentes e criar novos perfis.<br><br>Todos os perfis de usuário do Braze que tenham um `native_line_id` que siga o canal LINE serão atualizados para ter um status de grupo de inscrições de `subscribed`. Qualquer seguidor do canal LINE que não tenha um perfil de usuário Braze com o `native_line_id` terá:<br><br>\- Um perfil de usuário anônimo criado com `native_line_id` definido como o ID LINE do usuário que segue o canal <br>\- Um alias de usuário `line_id` definido para o ID do LINE do usuário após o canal <br>\- Um status de grupo de inscrições de `subscribed`

{: start="2"}
2\. **Atualizações do evento:** São usados para atualizar o status da inscrição de um usuário. Quando o Braze receber atualizações de eventos do usuário para o canal LINE integrado e o evento for um follow, o perfil do usuário terá um status de grupo de inscrições de `subscribed`. Se o evento for um unfollow, o perfil do usuário terá um status de grupo de inscrições de `unsubscribed`.<br><br>\- Todos os perfis de usuário do Braze com um `native_line_id` correspondente serão atualizados automaticamente. <br>\- Se não houver um perfil de usuário correspondente para um evento, o Braze criará um [usuário anônimo]({{site.baseurl}}/line/user_management/).

## Casos de uso

Esses são casos de uso de como os usuários podem ser atualizados depois de seguir as etapas de configuração acima.

##### O perfil do usuário Braze existente já segue o canal LINE

1. O perfil de usuário do Braze é atualizado com uma atribuição `native_line_id`. Seu status de inscrição padrão é `unsubscribed`.
2. A ferramenta de sincronização de inscrição é executada, descobre que o usuário está seguindo o canal LINE e atualiza o perfil do usuário com o status da inscrição `subscribed`.
3. Se ocorrer alguma alteração no status da inscrição (como o usuário bloquear, deixar de ser amigo ou voltar a seguir o canal), o Braze receberá a atualização do LINE e atualizará o perfil do usuário com o endereço `native_line_id` de acordo.

##### O perfil de usuário existente bloqueou, deixou de ser amigo ou de seguir o canal LINE 

1. O perfil de usuário do Braze é atualizado com uma atribuição `native_line_id`. Seu status de inscrição padrão é `unsubscribed`.
2. A ferramenta de sincronização de inscrição não descobre que o usuário está seguindo o canal LINE e o status da inscrição do usuário permanece como `unsubscribed`.
3. Se o usuário seguir o canal posteriormente, o Braze receberá a atualização do LINE e atualizará o perfil do usuário com o status da inscrição `subscribed`.

##### A criação do perfil do usuário ocorre depois que a LINE segue

1. O canal recebe um novo seguidor do LINE.
2. O Braze cria um perfil de usuário anônimo com a atribuição `native_line_id` definida como o LINE ID do seguidor e um alias de usuário `line_id` definido como o LINE ID do seguidor. O perfil tem um status de inscrição de `subscribed`.
3. O usuário é identificado como tendo o LINE ID por meio da [reconciliação do usuário](#user-id-reconciliation).
  - O perfil de usuário anônimo pode ser identificado usando o endpoint [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). As atualizações subsequentes (por meio do endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), [importação de CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) ou [ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/cloud_ingestion/)) para esse perfil de usuário podem direcionar o usuário por esse `external_id` conhecido.

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

  - Um novo perfil de usuário pode ser criado (por meio do endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), [importação de CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) ou [ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/cloud_ingestion/)) definindo o endereço `native_line_id`. Esse novo perfil herdará o estado do status da inscrição do perfil de usuário anônimo existente. Note que isso resultará em vários perfis compartilhando o mesmo `native_line_id`. Eles podem ser mesclados a qualquer momento usando o endpoint `/users/merge` no processo descrito na [etapa 5](#step-5-merge-profiles-optional).

##### A criação do perfil do usuário ocorre antes de o LINE seguir

1. Você adquire um novo usuário e envia as informações para o Braze. Um novo perfil de usuário é criado (perfil 1).
2. O usuário segue sua conta do LINE.
3. O Braze recebe um evento de seguir e cria um perfil de usuário anônimo (perfil 2).
4. O usuário é identificado como tendo o LINE ID por meio da [reconciliação do usuário](#user-id-reconciliation).
5. Você atualiza o perfil 1 para definir a atribuição `native_line_id`. Esse perfil herda o estado do status da inscrição do perfil 2.
  - Agora há dois perfis de usuário com o mesmo `native_line_id`. Eles podem ser mesclados a qualquer momento usando o endpoint `/users/merge` no processo descrito na [etapa 5](#step-5-merge-profiles-optional).

## Reconciliação de ID de usuário 

Os LINE IDs são recebidos automaticamente pelo Braze quando um usuário segue seu canal ou quando você usa o fluxo de trabalho único de "sincronização de seguidores". As IDs do LINE também são específicas para o canal que os usuários seguem, portanto, é improvável que os usuários possam fornecer suas IDs do LINE.

Há duas maneiras de combinar um LINE ID com um perfil de usuário existente no Braze:

- [Login do LINE](#line-login)
- [Vinculação de contas de usuário](#user-account-linking)

### Login do LINE

Esse método usa logins de redes sociais para reconciliação. Quando um usuário se registra no seu app, ele tem a opção de usar o [LINE Login](https://developers.line.biz/en/docs/line-login/overview/) para criar uma conta de usuário ou fazer login.

{% alert note %}
Para adquirir a ID LINE correta para cada usuário, configure o Login LINE com o mesmo provedor da sua conta ou canal oficial LINE integrado ao Braze.
{% endalert %}

1. Acesse o console de desenvolvedor do LINE e [solicite permissão para obter os endereços de e-mail dos usuários](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission) que registram seu app por meio do LINE Login.

2. Siga as etapas apropriadas fornecidas pelo LINE para implementar o LINE Login:<br><br>
  - [Instruções do app da Web](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [Instruções do app nativo](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>Certifique-se de incluir o site `email` no [escopo definido](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes) para as solicitações de verificação. 

{: start="3"}
3\. Use a [chamada do token Verify ID](https://developers.line.biz/en/reference/line-login/#verify-id-token) para adquirir o e-mail do usuário. 

4. Salve o LINE ID do usuário (`native_line_id`) no perfil do usuário com um e-mail correspondente em seu banco de dados ou crie um novo perfil de usuário com o e-mail e o LINE ID do usuário.

5. Envie as informações novas ou atualizadas do usuário para o Braze usando o [endpoint `/user/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users/), a [importação de CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) ou a [ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/cloud_ingestion/).

#### Fluxos

##### O seguidor existente usa o LINE Login

**Cenário:** Um usuário anônimo foi criado durante a sincronização inicial do assinante ou após a integração por meio de um evento "follow".

1. O usuário registra-se no seu app usando o LINE Login.
2. O LINE fornece o e-mail do usuário.
3. Você envia ao Braze o usuário atualizado (o perfil de usuário existente com esse e-mail para adicionar o LINE ID) ou atualiza o usuário anônimo com o e-mail.

##### Novo seguidor usa o LINE Login

**Cenário:** Não existe nenhum perfil de usuário no Braze com o ID LINE do usuário.

1. O usuário registra-se no seu app usando o LINE Login.
2. O LINE lhe fornece o e-mail do usuário.
3. Ou você:
  - Atualize um perfil de usuário existente com esse e-mail para que ele também tenha o LINE ID do usuário.
  - Crie um novo perfil de usuário com o e-mail e o ID do LINE.
4. Quando o usuário segue sua conta oficial LINE, o Braze recebe um evento de seguir e atualiza o status da inscrição do usuário para `subscribed`.

### Vinculação de contas de usuário 

Esse método permite que os usuários vinculem suas contas LINE à conta de usuário do seu app. Em seguida, é possível usar o Liquid no Braze, como {% raw %}`{{line_id}}`{% endraw %}, para criar um URL personalizado para o usuário que passa o LINE ID do usuário de volta para o seu site ou app, que pode então ser associado a um usuário conhecido.

1. Crie um Canva baseado em ação que se baseie em uma alteração de estado de inscrição e dispare quando um usuário se inscrever no seu canal LINE.<br>![Canva que é disparada quando um usuário se inscreve no canal LINE.]({% image_buster /assets/img/line/account_link_1.png %})
2. Crie uma mensagem incentivando os usuários a registrar seu site ou app, passando o LINE ID do usuário como um parâmetro de consulta (por meio do Liquid), como, por exemplo:

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3\. Crie uma mensagem de acompanhamento que forneça o código do cupom.
4\. (Opcional) Crie uma campanha baseada em ação ou Canva que seja disparada quando o usuário do LINE for identificado para enviar ao usuário o código do cupom. <br>![Campanha baseada em ação que dispara quando o usuário do LINE é identificado.]({% image_buster /assets/img/line/account_link_2.png %})

#### Como funciona?

Depois que o usuário registra, é feita uma alteração em seu site ou app para que o ID do usuário seja enviado de volta ao Braze para associá-lo ao LINE ID que foi passado como parte do URL, com um código de exemplo como:

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

#### Fluxos

##### O usuário existente segue seu canal LINE

**Cenário:** Um usuário existente no Braze segue seu canal no LINE.

1. O LINE envia ao Braze um evento de acompanhamento.
2. O Braze cria um perfil de usuário anônimo com o ID LINE, o alias de usuário `line_id` e o status do grupo de inscrições LINE de `subscribed`.
3. O usuário recebe uma mensagem LINE com um link para seu site e app e faz o registro. Seu perfil de usuário agora é conhecido.
4. O perfil de usuário anônimo que foi criado é identificado e mesclado por meio do [endpoint /users/identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) no perfil de usuário conhecido do usuário. O perfil de usuário conhecido agora contém o ID da LINE e tem um status de inscrição de `subscribed`.
5. (Opcional) O usuário recebe uma mensagem LINE com o código do cupom e o Braze registra o envio no perfil do usuário Braze.

## Criação de usuários de teste LINE no Braze

É possível testar seu canal LINE antes de configurar a [reconciliação do usuário](#user-id-reconciliation) criando um Canva ou uma campanha "Who am I".

1. Configure uma tela que retorne o ID de usuário Braze de um usuário em uma palavra específica disparada. <br><br>Exemplo de disparo <br><br>![Disparar para enviar a campanha aos usuários que enviaram um LINE de entrada para um grupo de inscrições específico.]({% image_buster /assets/img/line/trigger.png %}){: style="max-width:80%;"}<br><br>Exemplo de mensagem<br><br>![Mensagem LINE informando a ID de usuário do Braze.]({% image_buster /assets/img/line/message.png %}){: style="max-width:40%;"}<br><br>

2. No Braze, você pode usar o Braze ID para pesquisar usuários específicos e modificá-los conforme necessário.

{% alert important %}
Certifique-se de que o canva não tenha controle global ou grupos de controle que impeçam os envios.
{% endalert %}


