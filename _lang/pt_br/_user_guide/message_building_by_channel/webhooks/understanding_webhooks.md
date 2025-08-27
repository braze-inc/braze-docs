---
nav_title: Sobre Webhooks
article_title: Sobre Webhooks
page_order: 0
channel:
  - webhooks
description: "Este artigo de referência cobre o básico dos webhooks, incluindo casos de uso comuns, anatomia do webhook e como usá-los na Braze."

---

# [![curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/understanding-webhooks){: style="float:right;width:120px;border:0;" class="noimgborder"}Sobre Webhooks

> Este artigo de referência cobre o básico dos webhooks para fornecer os blocos de construção necessários para criar o seu próprio. Procurando etapas sobre como criar um webhook na Braze? Consulte [Creating a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).

Webhooks são uma maneira comum para aplicativos se comunicarem—para compartilhar dados em tempo real. Nos dias de hoje, raramente temos um aplicativo independente que possa fazer tudo. Na maioria das vezes, você está trabalhando em muitos aplicativos ou sistemas diferentes que são especializados para realizar certas tarefas, e esses aplicativos precisam ser capazes de se comunicar uns com os outros. É aí que os webhooks entram.

Um webhook é uma mensagem automatizada de um sistema para outro após certos critérios serem atendidos. Na Braze, esse critério é geralmente o acionamento de um evento personalizado.

No seu núcleo, um webhook é um método baseado em eventos para que dois sistemas separados tomem ações eficazes com base nos dados transmitidos em tempo real. Essa mensagem contém instruções que informam ao sistema receptor quando e como realizar uma tarefa específica. Por causa disso, os webhooks podem fornecer a você um acesso mais dinâmico e flexível aos dados e à funcionalidade programática, e capacitar você a configurar jornadas de clientes que otimizam processos.

## Casos de uso

Webhooks são uma excelente maneira de conectar seus sistemas — afinal, webhooks são como os aplicativos se comunicam. Aqui estão alguns cenários gerais onde webhooks podem ser particularmente úteis:

- Enviando dados para e de Braze
- Enviar mensagens para seus clientes por meio de canais não diretamente suportados pelo Braze
- Publicando nas APIs da Braze

Alguns casos de uso mais específicos incluem o seguinte:

- Se um usuário cancelar a inscrição do e-mail, você pode ter um webhook atualizando seu banco de dados de análise de dados ou CRM com essa mesma informação, garantindo uma visão holística do comportamento desse usuário.
- Envie [mensagens transacionais]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/) para usuários no Facebook Messenger ou LINE.
- Envie mala direta para os clientes em resposta à atividade deles no app e na web, usando webhooks para se comunicar com serviços de terceiros como [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/).
- Se um jogador atingir um certo nível ou acumular um certo número de pontos, use webhooks e sua configuração de API existente para enviar um upgrade de personagem ou moedas diretamente para sua conta. Se você enviar o webhook como parte de uma campanha de mensagens em vários canais, você pode enviar um push ou outra mensagem para informar o jogador sobre a recompensa ao mesmo tempo.
- Se você é uma companhia aérea, pode usar webhooks e sua configuração de API existente para creditar a conta de um cliente com um desconto após ele ter reservado um certo número de voos.
- Receitas infinitas do "If This Then That" ([IFTTT](https://ifttt.com/about)) — por exemplo, se um cliente entrar no app via e-mail, esse endereço pode ser configurado automaticamente no Salesforce.

## Anatomia de um webhook

Um webhook consiste nas seguintes partes.

| Parte do Webhook | Descrição |
| --- | --- |
| [Método HTTP](#methods) | Como APIs, webhooks precisam de métodos de solicitação. Estes são dados para a URL que o webhook aciona e informam ao endpoint o que fazer com as informações fornecidas. Existem quatro métodos HTTP que você pode especificar: POST, GET, PUT e DELETE. |
| URL HTTP | O endereço URL do seu endpoint de webhook. O endpoint é o local onde você enviará as informações que está capturando no webhook. |
| Corpo da solicitação | Essa parte do webhook contém as informações que você está comunicando ao endpoint. O corpo da solicitação pode ser pares de chave-valor JSON ou texto bruto. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Exemplo de webhook com um método HTTP, URL HTTP e corpo da solicitação.]({% image_buster /assets/img_archive/webhook_anatomy.png %})

### Métodos HTTP {#methods}

A tabela a seguir descreve os quatro métodos HTTP diferentes que você pode especificar no seu webhook.

| Método HTTP | Descrição |
| ----------- | ----------- |
| POST | Este método grava novas informações no servidor de recebimento. Um exemplo comum do método POST em uma aplicação do mundo real é um [formulário de contato](https://www.braze.com/company/contact) em um site. Qualquer informação que você colocar no formulário se torna parte de um corpo de solicitação e é enviada a um receptor. Este é o método mais comum usado ao enviar dados.
| OBTER | Este método recupera informações existentes, em vez de escrever novas informações. Por definição, uma solicitação GET não é compatível com um corpo de solicitação. Este é o método mais comum usado ao solicitar dados de um servidor. Por exemplo, considere o [endpoint `/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/). Se você fizesse uma solicitação GET, ela retornaria uma lista de seus segmentos.
| PUT | Este método atualiza as informações no endpoint, substituindo qualquer informação existente pelo que está no corpo da solicitação. 
| EXCLUIR | Este método exclui o recurso no URL HTTP. 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Webhooks no Braze

Na Braze, você pode criar um webhook como uma campanha de webhook, campanha de API ou componente de canva.

{% tabs %}
{% tab Campanha de Webhook %}

1. No dashboard da Braze, acesse **Campanhas**.
2. Clique em **Criar Campanha** e selecione **Webhook**.

Consulte [Criando um webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) para saber mais.

{% endtab %}
{% tab Campanha da API %}

1. No dashboard da Braze, acesse **Campanhas**.
2. Clique em **Criar Campanha** e selecione **Campanha de API**.
3. Clique em **Adicionar Mensagens** e selecione **Webhook**.
4. Formate sua chamada de API para incluir um [objeto webhook]({{site.baseurl}}/api/objects_filters/messaging/webhook_object/).

Consulte [Criando um webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) para saber mais.

{% endtab %}
{% tab Componente de canva %}

1. Em sua canva, crie um novo componente.
2. Na seção **Mensagem** do seu componente, selecione **Webhook**.

Consulte [Criando um webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) para saber mais.

{% endtab %}
{% endtabs %}

## Tratamento de erros e limite de frequência de webhooks

Quando o Braze recebe uma resposta de erro de uma chamada de webhook, ajustamos automaticamente o comportamento de envio desse webhook com base nesses cabeçalhos de resposta:

- `Retry-After`
- `X-Rate-Limit-Limit`
- `X-Rate-Limit-Remaining`
- `X-Rate-Limit-Reset`

Esses cabeçalhos nos ajudam a interpretar os limites de frequência e a ajustar a velocidade de envio de acordo para evitar mais erros. Também implementamos uma estratégia de backoff exponencial para novas tentativas, o que ajuda a reduzir o risco de sobrecarga dos servidores, espaçando as tentativas de nova tentativa ao longo do tempo.

Se detectarmos que a maioria das solicitações de webhook para um host específico está falhando, adiaremos temporariamente todas as tentativas de envio para esse host. Em seguida, retomaremos o envio após um período de resfriamento definido, permitindo que seu sistema se recupere.


