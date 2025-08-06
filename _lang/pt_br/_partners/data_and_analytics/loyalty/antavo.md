---
nav_title: Antavo
article_title: Antavo Loyalty Cloud
description: "Este artigo de referência descreve a parceria entre o Braze e a Antavo, um programa de fidelidade de última geração que vai além de recompensas por compras."
alias: /partners/antavo/
page_type: partner
search_tag: Partner
---

# Antavo Loyalty Cloud

> [A Antavo](https://antavo.com/) é um provedor de tecnologia de fidelidade SaaS de nível empresarial que cria programas de fidelidade abrangentes para promover o amor à marca e mudar o comportamento do cliente.

_Essa integração é mantida pela Antavo._

## Sobre a integração

A integração entre a Antavo e a Braze permite que você use dados relacionados ao programa de fidelidade para criar campanhas personalizadas e aprimorar a experiência do cliente. O Antavo oferece suporte à sincronização de dados de fidelidade entre as duas plataformas - essa é uma sincronização de dados unidirecional apenas, do Antavo para o Braze. A integração oferece suporte ao campo `external_id` Braze, que o Antavo usa para sincronizar o ID do membro de fidelidade.

## Pré-requisitos

| Requisito          | Descrição                                                                                                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------  |
| Conta Antavo       | Para aproveitar essa parceria, é necessário ter uma conta [Antavo](https://antavo.com/) com a integração Braze ativada.                                                |
| Chave da API REST do Braze   | Uma chave da API REST do Braze com as seguintes permissões: `users.track`, `events.list`, `events.data_series`, e `events.get`.<br><br>Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**.  |
| Endpoint REST do Braze  | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint dependerá do URL do Braze para sua instância.                |
| Identificador do app Braze | A chave do identificador de seu app. <br><br>Para localizar essa chave no dashboard do Braze, vá para **Configurações** > **Chaves de API** e encontre a seção **Identificação**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Conectar o Braze em Antavo

No Antavo, acesse **Modules** > **Braze** e clique em **Configure**. Ao navegar pela primeira vez para a página de configuração de integração do Braze no Antavo, a interface solicitará que você conecte os dois sistemas.

Forneça as seguintes credenciais:

- **URL da instância:** O endpoint Braze REST da instância para a qual você está provisionado.
- **Token (identificador) da API:** A chave da API REST do Braze que o Antavo deve usar ao enviar solicitações ao Braze.
- **Identificador do app:** O identificador do app Braze.

Depois de inserir as credenciais, clique em **Connect (Conectar**).

![Conecte a tela do Braze no Antavo com o URL da instância, o token da API e o identificador do app.]({% image_buster /assets/img/antavo/connect_braze.png %})

### Etapa 2: Configurar o mapeamento de campos

Depois que a conexão for estabelecida, você será redirecionado automaticamente para a página **Sync Fields (Sincronizar campos** ) no Antavo para configurar a sincronização de campos entre os dois sistemas.   Você pode acessar essa página a qualquer momento em **Módulos** > **Braze**.

Para configurar o mapeamento de campo no Antavo:

1. Clique em **Adicionar novo campo** <i class="fas fa-plus" alt=""></i>.
2. Use o campo suspenso para selecionar o **campo de fidelidade** da Antavo que você deseja sincronizar com a Braze.
3. Informe o **campo Remoto** que representa o atributo personalizado equivalente na Braze no qual os dados serão preenchidos.  

{% alert note %}
Você pode encontrar sua lista de atributos personalizados no Braze em **Data Settings** > **Custom Attributes** ( Configurações de dados > Atributos personalizados). Se o campo que você inserir não estiver definido no Braze, um novo campo será gerado automaticamente com a primeira sincronização.
{% endalert %}

{:start="4"}
4\. Para adicionar outros pares de campos, repita as etapas 1 a 3.
5\. Para remover um campo da lista de dados sincronizados, clique em <i class="fa-solid fa-rectangle-xmark" title="Excluir"></i> no final da linha.
6\. Clique em **Salvar**.

Quando qualquer valor dos campos configurados é alterado no Antavo, não apenas a sincronização desse valor único é disparada, mas todos os campos adicionados ao mapeamento de campos são incluídos na solicitação.

![Página Sync Fields no Antavo.]({% image_buster /assets/img/antavo/data_field_mapping.png %})

{% alert important %}
Para minimizar o consumo de pontos de dados, recomendamos mapear apenas os campos que serão acionados na Braze.
{% endalert %}

#### Tipos de dados suportados

A integração suporta todos os [tipos de dados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage) de atributos personalizados da Braze, a saber: número (inteiro, flutuante), string, array, booleano, objeto, vetor de objetos e data.

![Perfil do Braze mostrando diferentes atributos personalizados.]({% image_buster /assets/img/antavo/braze_profile.png %})

Os campos de dados são preenchidos com base no mapeamento de campo configurado.

## Gatilhos

Além de configurar o mapeamento de campo, a integração oferece recursos adicionais por meio da ferramenta [Workflows](https://antavo.atlassian.net/wiki/spaces/AUM/pages/581402629) da Antavo. Todos os [tipos de dados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage) de atributos personalizados da Braze e os [tipos de dados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#expected-format) de propriedades de eventos personalizados também podem ser sincronizados com fluxos de trabalho.

### Sincronizar dados de fidelidade ocasionalmente

Use essa opção se os dados não estiverem armazenados em campos de fidelidade no Antavo ou se os dados não forem adicionados à lista de campos mapeados. A sincronização dos dados solicitados é disparada quando os critérios de fluxo de trabalho configurados são atendidos.

Visite o guia passo a passo para saber como configurar a sincronização dos [dados de fidelidade relacionados à última compra](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Sync-data-related-to-the-customer%E2%80%99s-last-purchase).

### Sincronização de eventos do programa de fidelidade

Use eventos sincronizados do Antavo para inserir membros de fidelidade em telas Braze baseadas em ações. A integração pode sincronizar qualquer evento do Antavo (incluindo eventos de compra) que apareça no Braze como eventos personalizados.

Visite o guia passo a passo para saber como configurar a sincronização do [evento de registro do programa de fidelidade](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!) e a sincronização do [evento de ganho de benefícios do programa de fidelidade](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!).


