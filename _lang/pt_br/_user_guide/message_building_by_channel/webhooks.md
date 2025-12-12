---
nav_title: Webhooks
article_title: Webhooks
page_order: 4
layout: dev_guide
alias: /about_webhooks/
guide_top_header: "Webhooks"
guide_top_text: "Webhooks são uma maneira comum de as aplicações se comunicarem - para compartilhar dados em tempo real. Nos dias de hoje, raramente temos um aplicativo autônomo que possa fazer tudo. Na maioria das vezes, você está trabalhando em muitos aplicativos ou sistemas diferentes que são especializados para realizar certas tarefas, e esses aplicativos precisam ser capazes de se comunicar entre si. É aí que os webhooks entram. <br><br> Um webhook é uma mensagem automatizada de um sistema para outro após um determinado critério ter sido atendido. No Braze, esse critério geralmente é a ativação de um evento personalizado. <br><br>Em sua essência, um webhook é um método baseado em eventos para que dois sistemas separados tomem ações eficazes com base em dados transmitidos em tempo real. Essa mensagem contém instruções que dizem ao sistema receptor quando e como realizar uma tarefa específica. Por causa disso, os webhooks podem fornecer acesso mais dinâmico e flexível a dados e funcionalidades programáticas, e capacitar você a configurar jornadas do cliente que otimizam processos. <br><br>**A disponibilidade de webhooks depende do seu pacote Braze. Entre em contato com seu gerente de conta ou gerente de sucesso do cliente para começar.**"
description: "Esta página de destino é o lar dos webhooks. Aqui, você pode encontrar artigos sobre como criar webhooks, criar modelos de webhook e webhooks Braze-to-Braze."
channel:
  - webhooks
search_rank: 3
guide_featured_title: "Artigos da seção"
guide_featured_list:
- name: Criando um Webhook
  link: /docs/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Criando um Modelo de Webhook
  link: /docs/user_guide/message_building_by_channel/webhooks/webhook_template/
  image: /assets/img/braze_icons/table.svg
- name: Webhooks Braze-to-Braze
  link: /docs/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/
  image: /assets/img/braze_icons/switch-horizontal-01.svg
- name: Relatórios
  link: /docs/user_guide/message_building_by_channel/webhooks/reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Resolvendo Problemas de Solicitações de Webhook 
  link: /docs/help/help_articles/api/webhook_connected_content_errors/
  image: /assets/img/braze_icons/check-square-broken.svg
---

## [![Curso de Aprendizado Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/understanding-webhooks){: style="float:right;width:120px;border:0;" class="noimgborder"}Casos de uso

Webhooks são uma excelente maneira de conectar seus sistemas—afinal, webhooks são como os aplicativos se comunicam. Aqui estão alguns cenários gerais onde webhooks podem ser particularmente úteis:

- Enviando dados para e de Braze
- Enviando mensagens para seus clientes através de canais não diretamente suportados pelo Braze
- Postando para as APIs do Braze

Alguns casos de uso mais específicos incluem o seguinte:

- Se um usuário cancelar a inscrição do e-mail, você pode ter um webhook atualizando seu banco de dados de análises ou CRM com essa mesma informação, garantindo uma visão holística do comportamento desse usuário.
- Envie [mensagens transacionais]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/) para usuários dentro do Facebook Messenger ou Line.
- Envie correspondência direta para clientes em resposta à sua atividade no aplicativo e na web usando webhooks para se comunicar com serviços de terceiros como [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/).
- Se um jogador atingir um certo nível ou acumular um certo número de pontos, use webhooks e sua configuração de API existente para enviar uma atualização de personagem ou moedas diretamente para a conta dele. Se você enviar o webhook como parte de uma campanha de mensagens multicanal, pode enviar um push ou outra mensagem para avisar o jogador sobre a recompensa ao mesmo tempo.
- Se você é uma companhia aérea, pode usar webhooks e sua configuração de API existente para creditar a conta de um cliente com um desconto após ele ter reservado um certo número de voos.
- Receitas infinitas "Se Isso Então Aquilo" ([IFTTT](https://ifttt.com/about))—por exemplo, se um cliente fizer login no aplicativo via e-mail, então esse endereço pode ser automaticamente configurado no Salesforce.

## Anatomia de um webhook

Um webhook consiste nas seguintes partes.

| Parte do Webhook | Descrição |
| --- | --- |
| [Método HTTP](#methods) | Assim como APIs, webhooks precisam de métodos de solicitação. Esses são dados para a URL que o webhook atinge e informam ao endpoint o que fazer com as informações fornecidas. Existem quatro métodos HTTP que você pode especificar: POST, GET, PUT e DELETE. |
| URL HTTP | O endereço URL do seu endpoint de webhook. O endpoint é o local onde você enviará as informações que está capturando no webhook. |
| Corpo da solicitação | Esta parte do webhook contém as informações que você está comunicando ao endpoint. O corpo da solicitação pode ser pares de chave-valor JSON ou texto bruto. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

\![Exemplo de webhook com um método HTTP, URL HTTP e corpo da solicitação.]({% image_buster /assets/img_archive/webhook_anatomy.png %})

### Métodos HTTP {#methods}

A tabela a seguir descreve os quatro diferentes métodos HTTP que você pode especificar em seu webhook.

| Método HTTP | Descrição |
| ----------- | ----------- |
| POST | Este método grava novas informações no servidor receptor. Um exemplo comum do método POST em uma aplicação do mundo real é um [formulário de contato](https://www.braze.com/company/contact) em um site. Quaisquer informações que você colocar no formulário se tornam parte de um corpo de solicitação e são enviadas a um receptor. Este é o método mais comum usado ao enviar dados.
| GET | Este método recupera informações existentes, em vez de escrever novas informações. Por definição, uma solicitação GET não suporta um corpo de solicitação. Este é o método mais comum usado ao solicitar dados de um servidor. Por exemplo, considere o endpoint [`/segments/list` endpoint]({{site.baseurl}}/api/endpoints/export/segments/get_segment/). Se você fizer uma solicitação GET, ela retornará uma lista de seus segmentos.
| PUT | Este método atualiza informações no endpoint, substituindo qualquer informação existente pelo que está no corpo da solicitação. 
| DELETE | Este método exclui o recurso na URL HTTP. 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Webhooks no Braze

No Braze, você pode criar um webhook como uma campanha de webhook, campanha de API ou componente de Canvas.

{% tabs %}
{% tab Webhook Campaign %}

1. No painel do Braze, vá para **Campanhas**.
2. Clique em **Criar Campanha** e selecione **Webhook**.

Consulte [Criando um webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) para mais informações.

{% endtab %}
{% tab API Campaign %}

1. No painel do Braze, vá para **Campanhas**.
2. Clique em **Criar Campanha** e selecione **Campanha de API**.
3. Clique em **Adicionar Mensagens** e selecione **Webhook**.
4. Formate sua chamada de API para incluir um [objeto webhook]({{site.baseurl}}/api/objects_filters/messaging/webhook_object/).

Consulte [Criando um webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) para mais informações.

{% endtab %}
{% tab Canvas Component %}

1. No seu Canvas, crie um novo componente.
2. Na seção **Mensagem** do seu componente, selecione **Webhook**.

Consulte [Criando um webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) para mais informações.

{% endtab %}
{% endtabs %}

## Tratamento de erros de webhook e limitação de taxa

Quando a Braze recebe uma resposta de erro de uma chamada de webhook, ajustamos automaticamente o comportamento de envio desse webhook com base nesses cabeçalhos de resposta:

- `Retry-After`
- `X-Rate-Limit-Limit`
- `X-Rate-Limit-Remaining`
- `X-Rate-Limit-Reset`

Esses cabeçalhos nos ajudam a interpretar limites de taxa e ajustar a velocidade de envio de acordo para evitar mais erros. Também implementamos uma estratégia de retrocesso exponencial para novas tentativas, o que ajuda a reduzir o risco de sobrecarregar seus servidores, espaçando as tentativas de nova tentativa ao longo do tempo.

Se detectarmos que a maioria das solicitações de webhook para um host específico está falhando, adiamos temporariamente todas as tentativas de envio para esse host. Em seguida, retomaremos o envio após um período de resfriamento definido, permitindo que seu sistema se recupere.


