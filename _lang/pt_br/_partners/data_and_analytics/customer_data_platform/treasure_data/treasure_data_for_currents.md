---
nav_title: Treasure Data para Currents
article_title: Treasure Data para Currents
description: "Esse artigo de referência descreve a parceria entre o Braze Currents e o Treasure Data, uma plataforma de dados do cliente corporativo que permite que você escreva os resultados do trabalho diretamente no Braze."
page_type: partner
tool: Currents
alias: /partners/treasure_data_for_currents/
search_tag: Partner
---


# Treasure Data para Currents

> [O Treasure Data](https://www.treasuredata.com/) é uma plataforma de dados do cliente (CDP) que coleta e encaminha informações de várias fontes para uma variedade de outros locais em sua pilha de marketing.

A integração entre a Braze e o Treasure Data permite que você controle perfeitamente o fluxo de informações entre os dois sistemas. Agora, com o Currents, você também pode conectar dados ao Treasure Data para transformá-los em ação em todo o stack de crescimento.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Treasure Data | É necessário ter uma [conta do Treasure Data](https://console.treasuredata.com/users/sign_in) para usar a parceria. |
| Currents | Para exportar dados de volta para o Treasure Data, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configurado em sua conta. |
| URL de dados do tesouro | Isso pode ser obtido navegando até o dashboard do Treasure Data e copiando o URL de ingestão.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
O Treasure Data registra cada evento em lotes. Para saber mais sobre como consultar o Treasure Data para obter contagens de eventos, consulte [Integração de importação do Braze Currents](https://docs.treasuredata.com/articles/#!int/braze-currents-import-integration).
{% endalert %}

## Integração

A abordagem recomendada para se conectar ao Treasure Data pela API de postback. Esse método não requer um conector padrão, e os dados podem ser recebidos por uma abordagem de push. Todos os eventos enviados em um lote de dados estão dentro de um campo de uma linha em uma matriz JSON, que precisa ser analisada para obter os dados necessários.

{% alert important %}
Atualmente, a ingestão no Treasure Data por meio do coletor de eventos não ocorre em tempo real e pode levar até cinco minutos.
{% endalert %}

### Etapa 1: configure a API de postback do Treasure Data com a Braze

As instruções para criar uma API de Postback podem ser encontradas no [site da Treasure Data](https://docs.treasuredata.com/display/public/PD/Postback+API). O Braze enviará diretamente os eventos atualizados para o Treasure Data em tempo real, com exceção da ingestão por meio do coletor de eventos. Quando concluído, o Treasure Data fornecerá um URL da fonte de dados a ser copiado para uso na próxima etapa.

### Etapa 2: crie um Current

Na Braze, navegue até **Currents** > **\+ Criar Current** > **Exportação do Treasure Data**. Forneça um nome de integração, e-mail de contato e o URL do Treasure Data. Em seguida, selecione o que deseja rastrear na lista de eventos disponíveis e clique em **Launch Current (Iniciar atual**).

Todos os eventos enviados ao Treasure Data incluirão o endereço `external_user_id` do usuário. No momento, a Braze não envia dados de eventos ao Treasure Data para usuários que não definiram o `external_user_id`.

{% alert important %}
Mantenha o URL do Treasure Data atualizada. Se o URL de seu conector estiver incorreto, o Braze não poderá enviar eventos. Se isso persistir por mais de 48 horas, os eventos do conector serão descartados, e os dados serão perdidos permanentemente.
{% endalert %}

#### Exemplo de valor de campo de evento
```json
{
    "events": [
        {
            "event_type": "users.message.email.Open",
            "id": "a1234567-89ab-cdef-0123-456789abcdef",
            "time": 1477502783,
            "user": {
                "user_id": "user_id",
                "timezone": "America/Chicago"
        },
            "properties": {
                "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
                "campaign_name": "Test Campaign",
                "dispatch_id": "12345qwert",
                "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
                "email_address": "test@example.com",
                "send_id": "f123456789abcdef01234567",
                "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
            }
        }
    ]
}
```

#### Exemplo de exibição ingerida

![4]{: style="max-width:70%;"}

## Detalhes da integração

O Braze oferece suporte à exportação de todos os dados listados nos [glossários de eventos Currents]({{site.baseurl}}/user_guide/data/braze_currents/) (incluindo todas as propriedades nos eventos de [engajamento com mensagens]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) e de [comportamento do cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)) para o Treasure Data.

A estrutura de carga útil para dados exportados é a mesma que a estrutura de carga útil para conectores HTTP personalizados, que pode ser visualizada no [repositório de exemplos para conectores HTTP personalizados](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).


[4]: {% image_buster /assets/img/treasure_data/treasure_data_ingested_view.png %}
