---
nav_title: ActionIQ
article_title: ActionIQ
description: "Este artigo de referência aborda a integração entre a Braze e a ActionIQ. ActionIQ é uma plataforma de dados do cliente empresarial para profissionais de marketing, analistas e tecnólogos. Esta integração permite que as marcas sincronizem e mapeiem seus dados ActionIQ diretamente para a Braze."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ
---

# ActionIQ

> A [ActionIQ][2] traz ordem ao caos da experiência do cliente. O ActionIQ Customer Experience (CX) Hub dá a todas as equipes acesso direto e controlado de autoatendimento aos dados de cliente para descobrir públicos e orquestrar experiências em escala.

A integração Braze e ActionIQ permite que as marcas sincronizem e mapeiem seus dados ActionIQ diretamente para o Braze, capacitando a entrega de experiências extraordinárias ao cliente com base em toda a amplitude de seus dados de cliente. A integração permite aos usuários:
- Mapeie segmentos de público ou atributos personalizados para o Braze diretamente do ActionIQ
- Encaminhe os eventos rastreados pelo ActionIQ para a Braze em tempo real para disparar campanhas personalizadas e direcionadas

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta ActionIQ | Uma conta ActionIQ é necessária para aproveitar esta integração. |
| chave da API REST Braze | Uma chave da API REST da Braze com as permissões `users.track` e `user.export.ids`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Seu URL do ponto de extremidade REST][1]. Seu endpoint dependerá do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Participação do público

Esta integração é usada para sincronizar a associação de público do ActionIQ com o Braze, criando atributos personalizados que indicam se um perfil do Braze faz parte de um segmento. Cada público do ActionIQ corresponde a um atributo personalizado booleano único.

A convenção de nomenclatura padrão para o atributo personalizado criado é: `AIQ_<Audience ID>_<Split ID>`.

Para criar um segmento desses usuários, no Braze, navegue até **Segmentos**, crie um novo segmento e selecione **Atributos Personalizados** como seu filtro. A partir daqui, você pode escolher o atributo personalizado do ActionIQ. Depois que o segmento é criado, você pode selecioná-lo como um filtro de público ao criar uma campanha ou canva.

#### Solicitações

No ActionIQ, configure uma conexão da Braze fornecendo sua chave da API REST e o endpoint REST da Braze. 

Para corresponder aos consumidores na plataforma Braze, os seguintes identificadores devem ser incluídos na sua configuração de ativação:
- `braze_id`
- `external_id`

Depois que sua integração estiver conectada, as informações começarão a ser enviadas para a Braze.

### Eventos

A plataforma ActionIQ pode ser configurada para receber informações de eventos através de seu serviço de ingestão de streaming. Esta outra opção de integração encaminha esses Eventos para a Braze, para que os profissionais de marketing os usem para orquestração ou acionamento de campanhas de marketing.

A integração de eventos é capaz de enviar atributos adicionais do ActionIQ como parte das propriedades dentro da carga útil do evento.

#### Solicitações

A integração de eventos envia as seguintes informações para a Braze:
- Nome do evento
- Identificador do consumidor (ou `braze_id` ou `external_id`)
- Data e hora
- Propriedades do evento, que são preenchidas por quaisquer atributos adicionais na configuração de exportação


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.actioniq.com/