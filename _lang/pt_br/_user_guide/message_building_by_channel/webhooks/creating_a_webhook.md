---
nav_title: Criação de um webhook
article_title: Criação de um webhook
page_order: 1
channel:
  - webhooks
description: "Este artigo de referência aborda como criar e configurar uma campanha de webhook."
search_rank: 2
---

# Criação de uma campanha de webhook

> A criação de uma campanha de webhook ou a inclusão de um webhook em uma campanha multicanal permite disparar ações não relacionadas a aplicativos, fornecendo a outros sistemas e aplicativos informações em tempo real. 

Você pode usar webhooks para enviar informações para sistemas, como Salesforce ou Marketo, ou para seus sistemas back-end. Por exemplo, talvez você queira creditar uma promoção nas contas de seus clientes depois que eles realizarem um evento personalizado um determinado número de vezes.

{% alert tip %}
Para saber mais sobre o que são webhooks e como você pode usá-los no Braze, consulte [Sobre webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) antes de continuar.
{% endalert %}

## Etapa 1: Escolha onde construir sua mensagem

Não tem certeza se sua mensagem deve ser enviada por meio de uma campanha ou de um Canva? As campanhas são melhores para campanhas de mensagens únicas e simples, enquanto as canvas são melhores para jornadas de usuários em várias etapas.

{% tabs %}
{% tab Campanha %}

**Etapas:**

1. Acesse **Envio de mensagens** > **Campanhas** e selecione **Criar campanha**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar **Campaigns** em **Engagement (Engajamento**).
{% endalert %}

{:start="2"}
2\. Selecione **Webhook** ou, para campanhas com direcionamento para vários canais, selecione **Multicanal**.
3\. Dê à sua campanha um nome claro e significativo.
4\. (Opcional) Adicione uma descrição para descrever como essa campanha será usada.
4\. Adicione [equipes]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) conforme necessário.
   * As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/), você pode filtrar por tags específicas.
5. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Você pode escolher modelos diferentes de webhook para cada uma de suas variantes adicionadas. Para saber mais sobre esse tópico, consulte [Testes multivariantes e testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Se todas as mensagens em sua campanha forem semelhantes ou tiverem o mesmo conteúdo, crie sua mensagem antes de adicionar variantes adicionais. Em seguida, você pode selecionar **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Etapas:**

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o criador do Canvas.
2. Depois de configurar seu canvas, adicione uma etapa no construtor do canva. Dê um nome claro e significativo à sua etapa.
3. Escolha uma [programação de etapas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) e especifique uma postergação, conforme necessário.
4. Filtre seu público para esta etapa, conforme necessário. Você pode refinar ainda mais os destinatários dessa etapa especificando segmentos e adicionando filtros adicionais. As opções de público serão verificadas após a postergação no momento em que as mensagens forem enviadas.
5. Escolha seu [comportamento para avançar]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Escolha quaisquer outros canais de envio de mensagens que gostaria de associar à sua mensagem.

{% endtab %}
{% endtabs %}

## Etapa 2: Crie seu webhook

Você pode optar por criar um webhook do zero, usar um modelo existente ou usar um de nossos modelos existentes. Em seguida, crie seu webhook na guia **Compose (Criar** ) do editor.

A guia **Criador** consiste nos seguintes campos:

- Idioma
- URL do webhook
- Método HTTP
- Corpo da solicitação

![A guia "Compose" com um exemplo de modelo de webhook do Facebook Messenger.]({% image_buster /assets/img_archive/webhook_compose.png %})

#### Idioma {#internationalization}

[A internacionalização][16] é compatível com o URL e o corpo da solicitação. Para internacionalizar sua mensagem, selecione **Adicionar idiomas** e preencha os campos obrigatórios. 

Recomendamos selecionar seus idiomas antes de escrever seu conteúdo para que possa preencher o texto onde ele pertence no Liquid. Para ver a lista completa de idiomas disponíveis que você pode usar, consulte [Idiomas suportados]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

#### URL do webhook

O URL do webhook, ou URL HTTP, especifica seu endpoint. O endpoint é o local para o qual você enviará as informações que está capturando no webhook. 

Se quiser enviar informações a um fornecedor, ele deverá fornecer esse URL em sua documentação da API. Se estiver enviando informações para seus próprios sistemas, verifique com sua equipe de desenvolvimento ou engenharia para confirmar se está usando o URL correto. 

A Braze só permite URLs que se comunicam pelas portas padrão `80` (HTTP) e `443` (HTTPS).

##### Usando Liquid

Você pode personalizar seus URLs de webhook usando o [Liquid][15]. Às vezes, determinados pontos de extremidade podem exigir que você identifique um usuário ou forneça informações específicas do usuário como parte do seu URL. Ao usar o Liquid, inclua um [valor padrão][19] para cada informação específica do usuário usada no URL.

#### Método HTTP

O [método HTTP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#methods) que você deve usar varia de acordo com o endpoint para o qual você está enviando informações. Na maioria dos casos, você usará o POST.

#### Corpo da solicitação

O corpo da solicitação é a informação que será enviada para o URL que você especificou. Você pode criar o corpo da sua solicitação de webhook com pares de valores-chave JSON ou texto bruto.

##### Pares de valores-chave JSON

Os pares de valores-chave JSON permitem que você escreva facilmente uma solicitação para um endpoint que espera um formato JSON. Você só pode usar isso com um ponto de extremidade que espera uma solicitação JSON. Por exemplo, se sua chave for `message_body`, o valor correspondente poderá ser `Your order just arrived!`. Depois de inserir seu par chave/valor, o criador configurará sua solicitação na sintaxe JSON, e uma prévia de sua solicitação JSON será preenchida automaticamente.

![Corpo da solicitação definido como pares de valores-chave JSON.]({% image_buster /assets/img/webhook_json_1.png %})

É possível personalizar seus pares de valores-chave usando o Liquid, como incluir qualquer atributo de usuário, [atributo personalizado][17] ou [propriedade de evento][18] em sua solicitação. Por exemplo, você pode incluir o nome e o e-mail de um cliente em sua solicitação. Não se esqueça de incluir um [valor padrão][19] para cada atribuição.

##### Texto bruto

A opção de texto bruto lhe dá a flexibilidade de escrever uma solicitação para um ponto de extremidade que espera um corpo de qualquer formato. Por exemplo, você pode usar isso para escrever uma solicitação para um ponto de extremidade que espera que sua solicitação esteja no formato XML. 

Tanto [a personalização][15] quanto [a internacionalização][16] usando Liquid são suportadas em texto bruto.

![Um exemplo de um corpo de solicitação com texto bruto usando Liquid.]({% image_buster /assets/img_archive/webhook_rawtext.png %})

Se você definir o [cabeçalho da solicitação](#request-headers-optional) `Content-Type` como `application/x-www-form-url-encoded`, o corpo da solicitação deverá ser formatado como uma string codificada por URL. Por exemplo:

{% raw %}
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived
```
{% endraw %}

![Corpo da solicitação com string codificada por URL.]({% image_buster /assets/img_archive/webhook_rawtext_URL-encoded.png %})

## Etapa 3: Configurar definições adicionais

#### Cabeçalhos de solicitação (opcional)

Alguns endpoints podem exigir que você inclua cabeçalhos em sua solicitação. Na seção **Compose** do criador, é possível adicionar quantos cabeçalhos forem necessários.

![Exemplos de cabeçalho de solicitação para a chave "Authorization" e a chave "Content-type".]({% image_buster /assets/img_archive/webhook_request_headers_example.png %})

Os cabeçalhos de solicitação comuns são as especificações `Content-Type` (que descrevem o tipo de dados a serem esperados no corpo, como XML ou JSON) e os cabeçalhos de autorização que contêm suas credenciais com seu fornecedor ou sistema. 

As especificações de tipo de conteúdo devem usar a chave `Content-Type`. Os valores comuns são `application/json` ou `application/x-www-form-urlencoded`.

Os cabeçalhos de autorização devem usar a chave `Authorization`. Os valores comuns são {% raw %} `Bearer {{YOUR_TOKEN}}` ou `Basic {{YOUR_TOKEN}}` {% endraw %}, em que `YOUR_TOKEN` são as credenciais fornecidas por seu fornecedor ou sistema.

## Etapa 4: Teste o envio de suas mensagens

Antes de colocar sua campanha ativa, o Braze recomenda que você teste o webhook para garantir que a solicitação esteja formatada corretamente.

Para isso, vá para a guia **Teste** e envie um webhook de teste. É possível testar o webhook como um usuário aleatório, um usuário específico (inserindo seu endereço de e-mail ou ID de usuário externo) ou um usuário personalizado com atributos de sua escolha.  

Depois de enviar o webhook de teste, será exibida uma caixa de diálogo com a mensagem de resposta. Se a solicitação do webhook não for bem-sucedida, consulte a mensagem de erro para obter ajuda na solução de problemas do webhook. O exemplo a seguir detalha a resposta de um webhook com um URL de webhook inválido.

```json
404 Not Found

{
  "error": {
    "message": "Unrecognized request URL. Please see https://lob.com/docs or email us at support@lob.com.",
    "status_code": 404
  }
}

```

## Etapa 5: Crie o restante de sua campanha ou Canva

{% tabs %}
{% tab Campanha %}

Em seguida, crie o restante de sua campanha. Consulte as seções a seguir para obter mais detalhes sobre a melhor forma de usar nossas ferramentas para criar webhooks.

#### Escolha a programação ou o disparo da entrega

Os webhooks podem ser entregues com base em um horário programado, em uma ação ou em um disparo de API. Para saber mais, consulte [Agendamento de sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para entrega baseada em ação, você também pode definir a duração da campanha e o [Horário de silêncio]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

Nessa etapa, também é possível especificar controles de entrega, como permitir que os usuários se tornem [reelegíveis]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para receber a campanha ou ativar regras [de limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Escolha os usuários a serem direcionados

Em seguida, é necessário direcionar os [usuários]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) escolhendo segmentos ou filtros para restringir seu público. Nessa etapa, você selecionará o público maior de seus segmentos e restringirá ainda mais esse segmento com nossos filtros, se desejar. Você receberá automaticamente um instantâneo de como é a população desse segmento aproximado no momento. Lembre-se de que a associação exata ao segmento de mensagens é sempre calculada imediatamente antes do envio da mensagem.

#### Selecionar eventos de conversão

O Braze permite rastrear a frequência com que os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), após receberem uma campanha. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão será contada se o usuário realizar a ação especificada.

{% endtab %}

{% tab Canvas %}

Se ainda não tiver feito isso, conclua as seções restantes da etapa do canva. Para obter mais detalhes sobre como criar o restante de seu Canvas, implementar testes multivariantes e Intelligent Selection e muito mais, consulte a etapa [Construir seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de nossa documentação do Canvas.

{% endtab %}
{% endtabs %}

## Etapa 6: Revisão e implementação

Depois de terminar de criar a última parte de sua campanha ou Canva, revise seus detalhes, teste-a e envie-a!

## Coisas para saber

### Erros, lógica de nova tentativa e tempos limite

Os webhooks dependem de servidores Braze que fazem solicitações a um endpoint externo, e podem ocorrer erros de sintaxe e outros. A primeira etapa para evitar erros de webhook é testar sua campanha de webhook quanto a erros de sintaxe e certificar-se de que as variáveis personalizadas tenham um valor padrão. No entanto, os webhooks ainda podem falhar devido a problemas como chaves de API expiradas, limites de frequência ou erros inesperados do servidor. Se o seu webhook não conseguir enviar, uma mensagem de erro será registrada no [Message Activity Log][42].

Essa descrição contém a hora em que o erro ocorreu, o nome do app e a mensagem de erro:

![Erro de webhook com a mensagem "Um token de acesso ativo deve ser usado para consultar informações sobre o usuário atual".]({% image_buster /assets/img_archive/webhook-error.png %})

Se o corpo da mensagem não for suficientemente claro em relação à origem do erro, verifique a documentação do endpoint da API que está usando. Normalmente, eles fornecem uma explicação dos códigos de erro que o endpoint usa, bem como a causa típica desses erros.

Como em outras campanhas, o Braze rastreia a entrega de suas campanhas de webhook e as conversões resultantes delas. Quando a solicitação do webhook for enviada, o servidor receptor retornará um código de resposta indicando o que aconteceu com a solicitação. 

A tabela a seguir resume as diferentes respostas que o servidor pode enviar, como elas afetam a análise de dados da campanha e se, no caso de erros, o Braze tentará reenviar a campanha:

| Código da resposta | Marcado como recebido? | Novas tentativas? |
|---------------|-----------|----------|
| `20x` (sucesso)  | Sim |   N/D  |
| `30x` (redirecionamento)  | Não | Não |
| `408` (tempo limite da solicitação)  | Não | Sim |
| `429` (limite de frequência)  | Não | Sim |
| `Other 4XX` (erro do cliente)  | Não | Não |
| `5XX` (erro do servidor)   | Não | Sim |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Para erros de `5XX`, o Braze tentará enviar novamente o webhook até 5 vezes em 30 minutos usando o backoff exponencial. Para todos os outros erros, o Braze continuará tentando novamente por até 24 horas.<br><br>Cada webhook tem 90 segundos antes de atingir o tempo limite.
{% endalert %}

### Lista de permissões de IP {#ip-allowlisting}

Quando um webhook é enviado pelo Braze, os servidores do Braze fazem solicitações de rede aos nossos clientes ou a servidores de terceiros. Com a lista de permissões de IP, você pode verificar se as solicitações de webhook são provenientes da Braze, adicionando uma camada de segurança.

O Braze enviará webhooks dos seguintes IPs. Os IPs listados são automática e dinamicamente adicionados a quaisquer chaves de API que tenham sido aceitas para a listagem de permissões.

{% alert important %}
Se estiver criando um webhook Braze-para-Braze e usando a lista de permissões, deverá colocar na lista de permissões todos os seguintes IPs, incluindo `127.0.0.1`.
{% endalert %}

| Para as instâncias `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, e `US-07`: |
|---|
| `127.0.0.1`
| `23.21.118.191`
| `34.206.23.173`
| `50.16.249.9`
| `52.4.160.214`
| `54.87.8.34`
| `54.156.35.251`
| `52.54.89.238`
| `18.205.178.15`

| Para as instâncias `EU-01` e `EU-02`: |
|---|
| `127.0.0.1`
| `52.58.142.242`
| `52.29.193.121`
| `35.158.29.228`
| `18.157.135.97`
| `3.123.166.46`
| `3.64.27.36`
| `3.65.88.25`
| `3.68.144.188`
| `3.70.107.88` 

| Por exemplo, `US-08`: |
|---|
| `52.151.246.51`
| `52.170.163.182`
| `40.76.166.157`
| `40.76.166.170`
| `40.76.166.167`
| `40.76.166.161`
| `40.76.166.156`
| `40.76.166.166`
| `40.76.166.160`
| `40.88.51.74`
| `52.154.67.17`
| `40.76.166.80`
| `40.76.166.84`
| `40.76.166.85`
| `40.76.166.81`
| `40.76.166.71`
| `40.76.166.144`
| `40.76.166.145`

### Uso de webhooks com parceiros do Braze {#utilizing-webhooks}

Há muitas maneiras de usar webhooks e, com nossos parceiros de tecnologia (Alloys), é possível usar webhooks para elevar o nível da comunicação diretamente com seus clientes e usuários.

Confira:
* [Messenger]({{site.baseurl}}/partners/message_orchestration/additional_channels/instant_chat/messenger/)
* [Remerge]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/remerge)
* [Lob.com]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/lob)
* E muitos outros de nossos [parceiros de tecnologia]({{site.baseurl}}/partners/home/)!


[15]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[16]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#additional-notes-and-best-practices
[18]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/
[42]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/message_activity_log_tab/
