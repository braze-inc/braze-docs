---
nav_title: ActionIQ
article_title: ActionIQ
description: "Este artigo de referência aborda a integração entre a Braze e a ActionIQ. A ActionIQ é uma plataforma de dados do cliente para profissionais de marketing, analistas e tecnólogos. Esta integração permite que as marcas sincronizem e mapeiem seus dados ActionIQ diretamente para a Braze."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ
---

# ActionIQ

> [A ActionIQ](https://www.actioniq.com/) é uma plataforma de dados do cliente para marcas corporativas que oferece aos profissionais de marketing maneiras fáceis e seguras de ativar dados em qualquer lugar da experiência do cliente. A arquitetura exclusiva e criadora do ActionIQ significa que os dados podem permanecer em segurança onde estão, e as equipes de marketing usam apenas as ferramentas de que precisam.

_Essa integração é mantida pela ActionIQ._

## Sobre a integração

A integração entre o Braze e o ActionIQ permite que as marcas sincronizem e mapeiem seus dados do ActionIQ diretamente no Braze, possibilitando o fornecimento de experiências extraordinárias aos clientes com base em toda a amplitude de seus dados de clientes. As integrações disponíveis permitem que os usuários:

- Atualize os perfis de usuário no Braze com informações de associação do público e quaisquer atribuições diretamente do ActionIQ
- Encaminhe os eventos rastreados pelo ActionIQ para a Braze em tempo real para disparar campanhas personalizadas e direcionadas
- Entregue campanhas disparadas por API no Braze diretamente dos pontos de contato em uma jornada do ActionIQ

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta ActionIQ | Uma conta ActionIQ é necessária para aproveitar esta integração. |
| Chave da API REST do Braze | Uma chave da API REST do Braze com as permissões necessárias para a respectiva integração. Consulte a respectiva seção Requisitos para obter mais detalhes. <br><br>Essa chave pode ser criada no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST  do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint dependerá do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integrações

### Participação do público

Esta integração é usada para sincronizar a associação de público do ActionIQ com o Braze, criando atributos personalizados que indicam se um perfil do Braze faz parte de um segmento. Cada público do ActionIQ corresponde a um atributo personalizado booleano único.

A convenção de nomenclatura padrão para o atributo personalizado criado é: `AIQ_<Audience ID>_<Split ID>`.

Para criar um segmento desses usuários, faça o seguinte:
1. No Braze, navegue até **Segments (Segmentos**).
2. Crie um novo segmento.
3. Selecione **Atributos personalizados** como seu filtro.
4. A partir daqui, escolha o atributo personalizado ActionIQ. 
5. Depois que o segmento é criado, você pode selecioná-lo como um filtro de público ao criar uma campanha ou canva.

Além disso, essa integração atualizará qualquer atributo personalizado ou padrão em um perfil de usuário do Braze com seus valores de atributo do ActionIQ.

#### Solicitações

É necessária uma chave da API REST do Braze com as permissões `users.track` e `user.export.ids`. Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. 

No ActionIQ, configure uma conexão da Braze fornecendo sua chave da API REST e o endpoint REST da Braze. 

Para corresponder aos consumidores na plataforma Braze, os seguintes identificadores devem ser incluídos na sua configuração de ativação:
- `braze_id`
- `external_id`

### Eventos

Você pode configurar a plataforma ActionIQ para receber informações de eventos por meio de seu serviço de ingestão de streaming. Essa opção de integração encaminha esses eventos ao Braze para que os profissionais de marketing os utilizem para orquestração ou para disparar campanhas de marketing. A integração de eventos é capaz de enviar atribuições adicionais do ActionIQ como parte das propriedades na carga útil do evento.

#### Solicitações

É necessária uma chave da API REST do Braze com as permissões `users.track` e `user.export.ids`. Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. 

A integração de eventos envia as seguintes informações para a Braze:
- Nome do evento
- Identificador do consumidor (ou `braze_id` ou `external_id`)
- Data e hora
- Propriedades do evento, que são preenchidas por quaisquer atributos adicionais na configuração de exportação

### Campanhas disparadas

Essa integração disparará uma campanha no Braze para todos os usuários em um segmento do ActionIQ. Depois de configurar o texto, os testes multivariantes e as regras de reelegibilidade de sua campanha, você poderá dispará-la a partir de qualquer ponto de contato da jornada do ActionIQ adicionando o ID da campanha do Braze à sua configuração de exportação.

Opcionalmente, você pode incluir quaisquer outras atribuições do ActionIQ em sua exportação para preencher a cópia de sua campanha. Eles são enviados com o objeto `trigger_properties`.

#### Solicitações

É necessária uma chave da API REST do Braze com as permissões `campaigns.trigger.send` e `campaigns.list`. Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**.

Os seguintes valores devem ser enviados em sua exportação do ActionIQ para o Braze:
- Identificador do consumidor (ou `braze_id` ou `external_id`)
- ID da campanha


