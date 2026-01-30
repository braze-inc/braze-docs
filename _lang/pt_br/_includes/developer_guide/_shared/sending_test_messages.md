# Envio de mensagens de teste

> Antes de enviar uma campanha de mensagens para seus usuários, você pode querer testá-la para garantir que ela esteja correta e funcione da maneira pretendida. Você pode usar o dashboard para criar e enviar mensagens de teste com notificações por push, mensagens no app (IAM) ou envio de e-mail.

## Envio de mensagens de teste

### Etapa 1: Criar um segmento de teste designado <a class="margin-fix" name="test-segment"></a>

Depois de configurar um segmento de teste, você poderá usá-lo para testar qualquer um de seus canais de envio de mensagens do Braze. Quando configurado corretamente, isso só precisa ser feito uma única vez.

Para configurar um segmento de teste, acesse **Segments (Segmentos** ) e crie um novo segmento. Selecione **Add Filter (Adicionar filtro**) e escolha um dos filtros de teste.

![Uma campanha de teste da Braze exibindo os filtros disponíveis na etapa de direcionamento.]({% image_buster /assets/img_archive/testmessages1.png %})

Com os filtros de teste, é possível garantir que apenas os usuários com um endereço de e-mail específico ou [ID de usuário externo]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#setting-user-ids) recebam a mensagem de teste.

![Um menu suspenso exibindo vários filtros listados sob um título que diz Testando]({% image_buster /assets/img_archive/testmessages2.png %})

Os filtros de endereço de e-mail e de ID de usuário externo oferecem as seguintes opções:

| Operador          | Descrição |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `equals`      | Isso procurará uma correspondência exata do e-mail ou da ID de usuário que você fornecer. Use essa opção se quiser enviar as campanhas de teste apenas para dispositivos associados a um único e-mail ou ID de usuário. |
| `does not equal` | Use essa opção se quiser excluir um e-mail ou ID de usuário específico das campanhas de teste. |
| `matches`     | Isso encontrará usuários que tenham endereços de e-mail ou IDs de usuário que correspondam a parte do termo de pesquisa fornecido. Isso pode ser usado para encontrar apenas os usuários que têm um endereço `@yourcompany.com`, permitindo o envio de mensagens a todos da sua equipe. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Você pode selecionar vários e-mails específicos usando a opção "`matches`" e separando os endereços de e-mail com um caractere |. Por exemplo: "`matches`" "`email1@braze.com` | `email2@braze.com`". Você também pode combinar vários operadores. Por exemplo, o segmento de teste pode incluir um filtro de endereço de e-mail que "`matches`" "`@braze.com`" e outro filtro que "`does not equal`" "`sales@braze.com`". 

Depois de adicionar os filtros de teste ao seu segmento de teste, é possível verificar se ele está funcionando selecionando **Prévia** ou **Configurações** > **Exportar todos os dados do usuário em CSV** para exportar os dados de usuários desse segmento para um arquivo CSV.

![Uma seção de uma campanha do Braze intitulada Detalhes do Segmento]({% image_buster /assets/img_archive/testmessages3.png %})

{% alert note %}
Exportar os dados de usuários do segmento para um arquivo CSV é o método de verificação mais preciso, pois a prévia mostrará apenas uma amostra dos seus usuários e poderá não incluir todos os usuários.
{% endalert %}

### Etapa 2: Envio de mensagens

Você pode enviar uma mensagem usando o dashboard do Braze ou a linha de comando.

{% tabs local %}
{% tab Using the dashboard %}
{% subtabs %}
{% subtab push or in-app message %}
Para enviar notificações por push de teste ou mensagens no app, você precisa direcionar seu segmento de teste criado anteriormente. Comece criando sua campanha e seguindo os passos habituais. Quando chegar à etapa de direcionamento **de público**, selecione seu segmento de teste no menu suspenso.

![Uma campanha de teste da Braze exibindo os segmentos disponíveis na etapa de direcionamento.]({% image_buster /assets/img_archive/test_segment.png %})

Confirme sua campanha e lance-a para testar a notificação por push e as mensagens no app.

{% alert note %}
Certifique-se de selecionar **Permitir que os usuários se tornem re-elegíveis para receber a campanha** na parte **Agendar** do criador de campanhas se você pretende usar uma única campanha para enviar uma mensagem de teste para si mesmo mais de uma vez.
{% endalert %}
{% endsubtab %}

{% subtab email message %}
Se você estiver apenas testando mensagens de e-mail, não necessário configurar um segmento de teste. Na primeira etapa do criador de campanha onde você compõe a mensagem de e-mail da sua campanha, clique em **Enviar Teste** e insira o endereço de e-mail para o qual você deseja enviar um e-mail de teste. 

![Uma campanha da Braze com a guia Enviar Teste selecionada]({% image_buster /assets/img_archive/testmessages45.png %})

{% alert tip %}
Você também pode ativar ou desativar [TESTE (ou SEED)]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines) sendo anexado às suas mensagens de teste.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Using the command line %}
Como alternativa, você pode enviar uma única notificação usando cURL e a [API de envio de mensagens do Braze]({{site.baseurl}}/api/endpoints/messaging/). Note que esses exemplos fazem uma solicitação usando a instância `US-01`. Para descobrir o seu, consulte [os pontos de extremidade da API]({{site.baseurl}}/api/basics/#endpoints).

{% subtabs local %}
{% subtab android %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "CUSTOM_KEY":"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}

{% subtab swift %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert": "Test push",
      "extra": { 
        "CUSTOM_KEY" :"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}

{% subtab kindle %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "kindle_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "CUSTOM_KEY":"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}
{% endsubtabs %}

Substitua o seguinte:

| Espaço reservado         | Descrição                                               |
|---------------------|-----------------------------------------------------------|
| `BRAZE_API_KEY`      | Sua chave de API do Braze usada para autenticação. No Braze, vá para **Settings** > **API Keys** ( **Configurações** > **Chaves de API** ) para localizar sua chave. |
| `EXTERNAL_USER_ID` | O ID de usuário externo usado para enviar sua mensagem a um usuário específico. No Braze, acesse **Público** > **Pesquisar usuários** e, em seguida, pesquise um usuário. |
| `CUSTOM_KEY`         | (Opcional) Uma chave personalizada para dados adicionais.              |
| `CUSTOM_VALUE`       | (Opcional) Um valor personalizado atribuído à sua chave personalizada.    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

## Limitações do teste

Existem algumas situações em que as mensagens de teste não têm paridade completa de recursos com o lançamento de uma campanha ou canva para um conjunto real de usuários. Nesses casos, para validar esse comportamento, você deve lançar a campanha ou canva para um conjunto limitado de usuários de teste.

- A visualização da [Central de Preferências]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) do Braze a partir das **Mensagens de Teste** fará com que o botão de envio fique acinzentado.
- O cabeçalho list-unsubscribe não está incluído nos e-mails enviados pela funcionalidade de mensagem de teste.
- Para mensagens no app e cartões de conteúdo, o usuário de destino deve ter um token por push para o dispositivo de destino.
