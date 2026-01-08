---
nav_title: Criando um webhook
article_title: Criando um Webhook
page_order: 1
channel:
  - webhooks
description: "Este artigo de referência cobre como criar e configurar uma campanha de webhook."
search_rank: 2
---

# Criando uma campanha de webhook

> Criar uma campanha de webhook ou incluir um webhook em uma campanha multicanal permite que você acione ações fora do aplicativo, fornecendo a outros sistemas e aplicativos informações em tempo real. 

Você pode usar webhooks para enviar informações para sistemas, como Salesforce ou Marketo, ou para seus sistemas de backend. Por exemplo, você pode querer creditar as contas de seus clientes com uma promoção depois que eles realizarem um evento personalizado um certo número de vezes.

{% alert tip %}
Para saber mais sobre o que são webhooks e como você pode usá-los no Braze, confira [Sobre webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) antes de prosseguir.
{% endalert %}

## Passo 1: Escolha onde construir sua mensagem

Não tem certeza se sua mensagem deve ser enviada usando uma campanha ou um Canvas? Campanhas são melhores para campanhas de mensagens únicas e simples, enquanto Canvases são melhores para jornadas de usuários em várias etapas.

{% tabs %}
{% tab Campaign %}

**Passos:**

1. Vá para **Mensagens** > **Campanhas** e selecione **Criar Campanha**.
2. Selecione **Webhook**, ou, para campanhas que visam múltiplos canais, selecione **Multicanal**.
3. Nomeie sua campanha de forma clara e significativa.
4. (Opcional) Adicione uma descrição para descrever como esta campanha será usada.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário.
   * As tags facilitam a localização de suas campanhas e a construção de relatórios. Por exemplo, ao usar o [Construtor de Relatórios]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), você pode filtrar por tags específicas.
5. Adicione e nomeie quantas variantes precisar para sua campanha. Você pode escolher diferentes modelos de webhook para cada uma de suas variantes adicionadas. Para mais informações sobre este tópico, consulte [Testes Multivariados e A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Se todas as mensagens em sua campanha forem semelhantes ou tiverem o mesmo conteúdo, componha sua mensagem antes de adicionar variantes adicionais. Você pode então escolher **Copiar da Variante** no menu suspenso **Adicionar Variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Passos:**

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o compositor de Canvas.
2. Depois de configurar seu Canvas, adicione uma etapa no construtor de Canvas. Nomeie sua etapa de forma clara e significativa.
3. Escolha um [cronograma de etapas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) e especifique um atraso conforme necessário.
4. Filtre seu público para esta etapa conforme necessário. Você pode refinar ainda mais os destinatários desta etapa especificando segmentos e adicionando filtros adicionais. As opções de público serão verificadas após o atraso no momento em que as mensagens forem enviadas.
5. Escolha seu [comportamento de avanço]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Escolha quaisquer outros canais de mensagens que você gostaria de emparelhar com sua mensagem.

{% endtab %}
{% endtabs %}

## Etapa 2: Construa seu webhook

Você pode escolher criar um webhook do zero, usar um modelo existente ou usar um de nossos modelos existentes. Em seguida, construa seu webhook na aba **Compor** do editor.

A aba **Compor** consiste nos seguintes campos:

- Idioma
- URL do Webhook
- Método HTTP
- Corpo da solicitação

\![A aba "Compor" com um exemplo de modelo de webhook.]({% image_buster /assets/img_archive/webhook_compose.png %})

#### Idioma {#internationalization}

[Internacionalização]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) é suportada na URL e no corpo da solicitação. Para internacionalizar sua mensagem, selecione **Adicionar idiomas** e preencha os campos obrigatórios. 

Recomendamos selecionar seus idiomas antes de escrever seu conteúdo para que você possa preencher seu texto onde ele pertence no Liquid. Para nossa lista completa de idiomas disponíveis que você pode usar, consulte [Idiomas suportados]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

Se você estiver adicionando texto em um idioma que é escrito da direita para a esquerda, observe que a aparência final das mensagens da direita para a esquerda depende em grande parte de como os provedores de serviços as renderizam. Para melhores práticas na elaboração de mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criando mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

#### URL do Webhook

A URL do webhook, ou URL HTTP, especifica seu endpoint. O endpoint é o local onde você enviará as informações que está capturando no webhook. 

Se você deseja enviar informações para um fornecedor, o fornecedor deve fornecer esta URL em sua documentação de API. Se você estiver enviando informações para seus próprios sistemas, verifique com sua equipe de desenvolvimento ou engenharia para confirmar se está usando a URL correta. 

A Braze permite apenas URLs que se comunicam por meio de portas padrão `80` (HTTP) e `443` (HTTPS).

##### Usando Liquid

Você pode personalizar suas URLs de webhook usando [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/). Às vezes, certos endpoints podem exigir que você identifique um usuário ou forneça informações específicas do usuário como parte da sua URL. Ao usar Liquid, certifique-se de incluir um [valor padrão]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web) para cada informação específica do usuário que você usar em sua URL.

#### Método HTTP

O [Método HTTP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#methods) que você deve usar varia dependendo do endpoint para o qual está enviando informações. Na maioria dos casos, você usará POST.

#### Corpo da solicitação

O corpo da solicitação é a informação que será enviada para a URL que você especificou. Você pode criar o corpo da sua solicitação de webhook com pares chave-valor JSON ou texto bruto.

##### Pares chave-valor JSON

Pares chave-valor JSON permitem que você escreva facilmente uma solicitação para um endpoint que espera um formato JSON. Você só pode usar isso com um endpoint que espera uma solicitação JSON. Por exemplo, se sua chave for `message_body`, o valor correspondente pode ser `Your order just arrived!`. Depois de inserir seu par chave-valor, o compositor configurará sua solicitação na sintaxe JSON, e uma prévia da sua solicitação JSON será preenchida automaticamente.

\![Corpo da solicitação definido para pares chave-valor JSON.]({% image_buster /assets/img/webhook_json_1.png %})

Você pode personalizar seus pares chave-valor usando Liquid, como incluir qualquer atributo de usuário, [atributo personalizado]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#additional-notes-and-best-practices), ou [propriedade de evento]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) em sua solicitação. Por exemplo, você pode incluir o primeiro nome e o e-mail de um cliente em sua solicitação. Certifique-se de incluir um [valor padrão]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web) para cada atributo.

##### Texto bruto

A opção de texto bruto oferece a flexibilidade de escrever uma solicitação para um endpoint que espera um corpo de qualquer formato. Por exemplo, você pode usar isso para escrever uma solicitação para um endpoint que espera que sua solicitação esteja no formato XML. 

Tanto a [personalização]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) quanto a [internacionalização]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) usando Liquid são suportadas em texto bruto.

\![Um exemplo de um corpo de solicitação com texto bruto usando Liquid.]({% image_buster /assets/img_archive/webhook_rawtext.png %})

Se você definir o `Content-Type` [cabeçalho de solicitação](#request-headers-optional) para `application/x-www-form-url-encoded`, o corpo da solicitação deve ser formatado como uma string codificada em URL. Por exemplo:

{% raw %}
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived
```
{% endraw %}

\![Corpo da solicitação com string codificada em URL.]({% image_buster /assets/img_archive/webhook_rawtext_URL-encoded.png %})

## Passo 3: Configurar configurações adicionais

#### Cabeçalhos de solicitação (opcional)

Certos endpoints podem exigir que você inclua cabeçalhos em sua solicitação. Na seção **Compor** do compositor, você pode adicionar quantos cabeçalhos forem necessários.

\![Exemplos de cabeçalhos de solicitação para a chave "Authorization" e a chave "Content-type".]({% image_buster /assets/img_archive/webhook_request_headers_example.png %})

Os cabeçalhos de solicitação comuns são `Content-Type` especificações (que descrevem que tipo de dados esperar no corpo, como XML ou JSON) e cabeçalhos de autorização que contêm suas credenciais com seu fornecedor ou sistema. 

As especificações do tipo de conteúdo devem usar a chave `Content-Type`. Os valores comuns são `application/json` ou `application/x-www-form-urlencoded`.

Os cabeçalhos de autorização devem usar a chave `Authorization`. Os valores comuns são {% raw %} `Bearer {{YOUR_TOKEN}}` ou `Basic {{YOUR_TOKEN}}` {% endraw %} onde `YOUR_TOKEN` são as credenciais fornecidas pelo seu fornecedor ou sistema.

## Passo 4: Teste o envio da sua mensagem

Antes de ativar sua campanha, a Braze recomenda que você teste o webhook para garantir que a solicitação esteja formatada corretamente.

Para fazer isso, mude para a aba **Teste** e envie um webhook de teste. Você pode testar o webhook como um usuário aleatório, um usuário específico (inserindo seu endereço de e-mail ou ID de usuário externo) ou um usuário personalizado com atributos de sua escolha.  

Após enviar o webhook de teste, um diálogo aparecerá com a mensagem de resposta. Se a solicitação do webhook não for bem-sucedida, consulte a mensagem de erro para obter assistência na solução de problemas do seu webhook. O seguinte exemplo detalha a resposta de um webhook com uma URL de webhook inválida.

```json
404 Not Found

{
  "error": {
    "message": "Unrecognized request URL. Please see https://lob.com/docs or email us at support@lob.com.",
    "status_code": 404
  }
}

```

## Passo 5: Construa o restante da sua campanha ou Canvas

{% tabs %}
{% tab Campaign %}

Em seguida, construa o restante da sua campanha. Veja as seções a seguir para mais detalhes sobre como usar melhor nossas ferramentas para construir webhooks.

#### Escolha o cronograma de entrega ou gatilho

Os webhooks podem ser entregues com base em um horário agendado, uma ação ou com base em um gatilho de API. Para mais informações, consulte [Agendando sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para entrega baseada em ação, você também pode definir a duração da campanha e [Horários de Silêncio]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

Esta etapa também é onde você pode especificar controles de entrega, como permitir que os usuários se tornem [re-eligíveis]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para receber a campanha, ou habilitar regras de [limitação de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Escolha os usuários para segmentar

Em seguida, você precisa [segmentar usuários]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) escolhendo segmentos ou filtros para restringir seu público. Nesta etapa, você selecionará o público maior de seus segmentos e restringirá ainda mais esse segmento com nossos filtros, se desejar. Você receberá automaticamente uma prévia de como essa população de segmento aproximada se parece agora. Tenha em mente que a associação exata ao segmento é sempre calculada pouco antes da mensagem ser enviada.

{% multi_lang_include target_audiences.md %}

#### Escolha eventos de conversão

Braze permite que você acompanhe com que frequência os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), após receber uma campanha. Você tem a opção de permitir uma janela de até 30 dias durante a qual uma conversão será contabilizada se o usuário realizar a ação especificada.

{% endtab %}

{% tab Canvas %}

Se você ainda não fez isso, complete as seções restantes do seu passo no Canvas. Para mais detalhes sobre como construir o restante do seu Canvas, implementar testes multivariados e Seleção Inteligente, e mais, consulte o passo [Construa seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) da nossa documentação do Canvas.

{% endtab %}
{% endtabs %}

## Passo 6: Revisar e implantar

Depois de terminar de construir a última parte da sua campanha ou Canvas, revise seus detalhes, teste-o e, em seguida, envie-o!

## Coisas a saber

### Erros, lógica de repetição e timeouts

Webhooks dependem de servidores Braze fazendo solicitações a um endpoint externo, e erros podem ocorrer ocasionalmente. Os erros mais comuns incluem erros de sintaxe, chaves de API expiradas, limites de taxa e problemas inesperados do lado do servidor. Antes de enviar uma campanha de webhook:

- Teste seu webhook para erros de sintaxe
- Certifique-se de que as variáveis personalizadas tenham valores padrão

Se o seu webhook falhar ao enviar, uma mensagem de erro será registrada no [Registro de Atividade de Mensagem]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/), e incluirá detalhes como o timestamp do erro, nome do aplicativo e detalhes sobre o erro.

\![Erro de webhook com a mensagem "Um token de acesso ativo deve ser usado para consultar informações sobre o usuário atual".]({% image_buster /assets/img_archive/webhook-error.png %})

Se a mensagem de erro não for clara o suficiente em relação à origem do erro, você deve verificar a documentação do endpoint da API que está usando. Esses geralmente fornecem uma explicação dos códigos de erro que o endpoint usa, bem como o que normalmente os causa.

#### Códigos de resposta e lógica de repetição

Quando a solicitação de webhook é enviada, o servidor receptor retornará um código de resposta indicando o que aconteceu com a solicitação. A tabela a seguir resume as diferentes respostas que o servidor pode enviar, como elas impactam a análise da campanha e se, no caso de erros, a Braze tentará reenviar a campanha:

| Código de resposta | Marcado como recebido? | Tentativas? |
|---------------|-----------|----------|
| `20x` (sucesso)  | Sim |   N/A  |
| `30x` (redirecionamento)  | Não | Não |
| `408` (tempo de espera da solicitação)  | Não | Sim |
| `429` (limite de taxa)  | Não | Sim |
| `Other 4XX` (erro do cliente)  | Não | Não |
| `5XX` (erro do servidor)   | Não | Sim |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
A Braze tenta os códigos de status acima até cinco vezes em 30 minutos usando retrocesso exponencial. Se não conseguirmos acessar seu endpoint, as tentativas podem ser distribuídas ao longo de um período de 24 horas.<br><br>Cada webhook tem 90 segundos antes de expirar.
{% endalert %}

#### Solução de problemas e detalhes adicionais de erro

Para explicações detalhadas, etapas de solução de problemas e orientações sobre como resolver erros específicos de webhook, consulte [Troubleshooting webhook and Connected Content requests]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors/). Você também encontrará mais explicações sobre como nosso sistema de detecção de hosts não saudáveis funciona e como a Braze fornece notificações de erro por meio de e-mails automatizados e registro adicional no Braze Currents.

### Lista de permissões de IP {#ip-allowlisting}

Quando um webhook é enviado da Braze, os servidores da Braze fazem solicitações de rede para nossos clientes ou servidores de terceiros. Com a lista de permissão de IP, você pode verificar se as solicitações de webhook estão vindo da Braze, adicionando uma camada de segurança.

A Braze enviará webhooks dos seguintes IPs. Os IPs listados são adicionados automaticamente e dinamicamente a qualquer chave de API que tenha sido optada para a lista de permissão.

{% alert important %}
Se você estiver fazendo um webhook de Braze para Braze e usando a lista de permissão, deve permitir todos os seguintes IPs, incluindo `127.0.0.1`.
{% endalert %}

{% multi_lang_include data_centers.md datacenters='ips' %}

### Usando webhooks com parceiros da Braze {#utilizing-webhooks}

Existem muitas maneiras de usar webhooks, e com nossos parceiros de tecnologia (Alloys), você pode usar webhooks para aprimorar sua comunicação diretamente com seus clientes e usuários.

Confira:
* [Messenger]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/instant_chat/messenger/)
* [Remerge]({{site.baseurl}}/partners/remerge/)
* [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/)
* E muitos mais de nossos [parceiros de tecnologia]({{site.baseurl}}/partners/home/)!


