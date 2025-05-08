---
nav_title: Enviando Mensagens de Teste
article_title: Enviando Mensagens de Teste
page_order: 6
description: "Este artigo de referência cobre o envio de mensagens de teste para diferentes canais."

---

# Enviando mensagens de teste

> Antes de enviar uma campanha de mensagens para seus usuários, você pode querer testá-la para garantir que ela esteja correta e funcione da maneira pretendida. Criar e enviar mensagens de teste para selecionar dispositivos ou membros da sua equipe é muito simples usando as ferramentas no dashboard.

## Criando um segmento de teste designado <a class="margin-fix" name="test-segment"></a>

Depois de configurar um segmento de teste, você pode usá-lo para testar **qualquer** de nossos canais de envio de mensagens. Se for configurado corretamente, o processo precisará ser feito apenas uma vez.

Para configurar um segmento de teste, navegue até a página de **Segmentos** no dashboard e crie um novo segmento. Clique em **Adicionar Filtro** para escolher um dos filtros de teste encontrados na parte inferior do menu suspenso.

![Uma campanha de teste do Braze exibindo os filtros disponíveis na etapa de direcionamento.]({% image_buster /assets/img_archive/testmessages1.png %})

Dois desses filtros de teste permitem selecionar usuários com endereços de e-mail específicos ou [IDs de usuários]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#setting-user-ids) externos.

![Um menu suspenso que exibe vários filtros listados em um título que diz Testing]({% image_buster /assets/img_archive/testmessages2.png %})

Os filtros de endereço de e-mail e ID de usuário externo têm três opções:

  1) **"Igual"** \- Isso procurará uma correspondência exata do e-mail ou ID de usuário que você fornecer. Use isto se você deseja enviar as campanhas de teste apenas para dispositivos associados a um único e-mail ou ID de usuário.

  2) **Não é igual** \- Use isto se você quiser excluir um determinado e-mail ou ID de usuário das campanhas de teste.

  3) **"Correspondências"** \- Isso encontrará usuários que tenham endereços de e-mail ou IDs de usuário que correspondam a parte do termo de pesquisa que você fornecer. Você poderia usar isso para encontrar apenas os usuários que têm um endereço "@yourcompany.com", permitindo que você envie mensagens para todos em sua equipe.

Você pode selecionar vários e-mails específicos usando a opção "matches" e separando os endereços de e-mail com um caractere | (por exemplo, "matches" "email1@braze.com | email2@braze.com").

Esses filtros também podem ser usados em conjunto para restringir sua lista de usuários de teste. Por exemplo, o segmento de teste pode incluir um filtro de endereço de e-mail que "corresponde" a "@braze.com" e outro filtro que "não é igual" a "sales@braze.com". 

Depois de adicionar os filtros de teste ao seu segmento de teste, você pode verificar se selecionou apenas os usuários desejados clicando em **Prévia** no topo do editor de segmentos ou exportando os dados de usuários desse segmento para CSV clicando no ícone de engrenagem no canto superior direito do editor e selecionando **Exportar todos os dados de usuários para CSV** no menu suspenso.

![Uma seção de uma campanha do Braze intitulada Segment Details (Detalhes do segmento)]({% image_buster /assets/img_archive/testmessages3.png %})

>  Exportar os dados de usuários do segmento para CSV fornecerá a imagem mais precisa de quem se enquadra nesse segmento. A guia **prévia** é apenas uma amostra dos usuários no segmento e, portanto, pode parecer que não selecionou todos os membros pretendidos.

## Enviando uma notificação por push de teste ou mensagens no app <a class="margin-fix" name="push-inapp-test"></a>

Para enviar notificações por push de teste ou mensagens no app, você precisa direcionar seu segmento de teste criado anteriormente. Comece criando sua campanha e seguindo os passos habituais. Quando você chegar na etapa **Usuários Alvo**, selecione seu segmento de teste no menu suspenso.

![Uma campanha de teste do Braze exibindo os segmentos disponíveis na etapa de direcionamento.]({% image_buster /assets/img_archive/test_segment.png %})

Conclua a confirmação da sua campanha e lance-a para testar sua notificação por push e mensagens no app.

>  Certifique-se de selecionar **Permitir que os usuários se tornem re-elegíveis para receber a campanha** na parte **Agendar** do criador de campanhas se você pretende usar uma única campanha para enviar uma mensagem de teste para si mesmo mais de uma vez.

## Enviando uma mensagem de teste por e-mail

Se você estiver apenas testando mensagens de e-mail, não necessário configurar um segmento de teste. Na primeira etapa do criador de campanha onde você compõe a mensagem de e-mail da sua campanha, clique em **Enviar Teste** e insira o endereço de e-mail para o qual você deseja enviar um e-mail de teste. 

![Uma campanha do Braze com a guia Test Send (Envio de teste) selecionada]({% image_buster /assets/img_archive/testmessages45.png %})

{% alert tip %}
Você também pode ativar ou desativar [TESTE (ou SEED)]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines) sendo anexado às suas mensagens de teste.
{% endalert %}

## Testando a partir da linha de comando

Como alternativa, se você quiser testar notificações por push via a linha de comando, você pode seguir os seguintes exemplos para cada plataforma.

### Testando push com aplicativos iOS via cURL

Você pode enviar uma única notificação pelo terminal por meio do CURL e da [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/). Você precisará substituir os seguintes campos pelos valores corretos para o seu caso de teste:

- `YOUR_API_KEY` - disponível em **Configurações** > **Chaves de API**
- `YOUR_EXTERNAL_USER_ID` - disponível na página **Pesquisar Usuários**
- `YOUR_KEY1` (opcional)
- `YOUR_VALUE1` (opcional)

{% alert note %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), essas páginas estão em um local diferente: <br>- **Chaves de API** está localizado em **Console de desenvolvedor** > **Configurações de API** <br>**Pesquisar Usuários** está localizado em **Usuários** > **Pesquisa de Usuários**
{% endalert %}

>  Os seguintes exemplos demonstram os endpoints apropriados da API para clientes na instância `US-01`. Se você não estiver nessa instância, consulte nossa [documentação da API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) para ver em qual endpoint fazer solicitações.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert": "Test push",
      "extra": { 
        "YOUR_KEY1" :"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

### Testando push com aplicativos Android via cURL

Você pode enviar uma única notificação pelo terminal por meio do cURL e da [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/). Você precisará substituir os seguintes campos pelos valores corretos para o seu caso de teste:

- `YOUR_API_KEY` (Acessar **Configurações** > **API Keys**.)
- `YOUR_EXTERNAL_USER_ID` (Procure um perfil na página **Buscar Usuários**.)
- `YOUR_KEY1` (opcional)
- `YOUR_VALUE1` (opcional)

>  Os seguintes exemplos demonstram os endpoints apropriados da API para clientes na instância `US-01`. Se você não estiver nessa instância, consulte nossa [documentação da API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) para ver em qual endpoint fazer solicitações.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

### Testando push com aplicativos Kindle via cURL

Você pode enviar uma única notificação pelo terminal por meio do cURL e da [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/). Você precisará substituir os seguintes campos pelos valores corretos para o seu caso de teste:

- `YOUR_API_KEY` - disponível na página **console de desenvolvedor**
- `YOUR_EXTERNAL_USER_ID` - disponível na página **Pesquisa de usuários**
- `YOUR_KEY1` (opcional)
- `YOUR_VALUE1` (opcional)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "kindle_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

## Limitações de mensagens de teste

Existem algumas situações em que as mensagens de teste não têm paridade completa de recursos com o lançamento de uma campanha ou canva para um conjunto real de usuários. Nesses casos, para validar esse comportamento, você deve lançar a campanha ou canva para um conjunto limitado de usuários de teste.

- A exibição da [Central de Preferências]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) do Braze a partir das **Mensagens de Teste** fará com que o botão de envio fique acinzentado
- O cabeçalho de cancelar inscrição da lista não está incluído nos e-mails enviados pela funcionalidade de mensagem de teste
- Para mensagens no app e Cartões de Conteúdo, o usuário alvo deve ter um token por push para o dispositivo alvo

