---
nav_title: Segmentar Engajar
article_title: Segmentar Engajar
page_order: 3
alias: /partners/segment_personas/
alias: /partners/segment_engage/
alias: /partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/

description: "Este artigo de referência descreve a parceria entre o Braze e a Segment, uma plataforma de dados do cliente que coleta e encaminha informações entre fontes em sua pilha de marketing."
page_type: partner
search_tag: Partner

---

# Segmentar Engajar

> A [Segment](https://segment.com) é uma plataforma de dados do cliente que ajuda você a coletar, limpar e ativar os dados de seus clientes. Este artigo de referência fornece uma visão geral da conexão entre [Braze e Segment Engage](https://segment.com/docs/destinations/braze/#Engage) e descreve os requisitos e processos para a implementação e uso adequados.

A integração Braze e Segment permite que você use [Engage](https://segment.com/docs/engage/), o construtor de público integrado do Segment, para criar segmentos de usuários com base nos dados que você já coletou de várias fontes. Esses públicos serão então sincronizados com a Braze como uma coorte, ou denotados no perfil do usuário através de [atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) ou [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) que podem ser usados para criar segmentos da Braze para usar em campanhas e redirecionamento de canva.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do segmento | É necessário ter uma [conta da Segment](https://app.segment.com/login) para aproveitar essa parceria. |
| Destino na nuvem da Braze | Você já deve ter [configurado o Braze como um destino]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) na sua integração com o Segment.<br><br>Isso inclui fornecer o data center correto da Braze e a chave da API REST nas suas [configurações de conexão]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings). |
| Chave de importação de dados do Braze | Para sincronizar os públicos do Engage com o Braze como coortes, você deve gerar uma chave de importação de dados.<br><br>A importação de coorte está em acesso antecipado, entre em contato com seu gerente de sucesso do cliente da Braze para obter acesso a este recurso. |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração de Destino de Coortes

### Etapa 1: Crie um público Engage
1. No Segment, navegue até a guia **Audiences** (Públicos) no Engage e clique em **New** (Novo).
2. Crie seu público. Um raio no canto superior da página indicará se o público é atualizado em tempo real.
3. Em seguida, selecione Braze como seu destino.
4. Prévia seu público clicando em **Revisar e Criar**. Por padrão, o Segment consulta todos os dados históricos para definir o valor atual do traço calculado e do público. Para omitir esses dados, desmarque **Preenchimento Histórico**.

### Etapa 2: Capture sua chave de importação de dados da coorte

No Braze, navegue para **Integrações de Parceiros** > **Parceiros de Tecnologia** e selecione **Segmento**.

Aqui você encontra o endpoint REST e gera sua chave de importação de dados da Braze. Depois que a chave é gerada, você pode criar outra ou invalidar uma existente.

### Etapa 3: conecte o destino de coortes da Braze
Siga [as instruções da Segment](https://segment.com/docs/connections/destinations/catalog/actions-braze-cohorts/#getting-started) sobre como configurar o Destino de Cohortes para sincronizar seus públicos do Engage como coortes para a Braze.

### Etapa 4: Crie um segmento Braze a partir do público Engage
No Braze, navegue até **Segmentos**, crie um novo segmento e selecione **Cohortes de Segmento** como seu filtro. Aqui você pode escolher qual coorte do Segment deseja incluir. Depois que o segmento de coorte do Segment for criado, você pode selecioná-lo como um filtro de público ao criar uma campanha ou canva.

![]({% image_buster /assets/img/segment/segment3.png %})

## integração do Modo Nuvem

### Etapa 1: Crie um traço computado de Segment ou público

1. No Segment, navegue até a **Características Computadas** ou **Públicos** guia em **Engajar**, e clique em **Novo**.
2. Crie seu traço computado ou público. Um raio no canto superior da página indica se a computação está sendo atualizada em tempo real.
3. Em seguida, selecione **Braze** como seu destino. 
4. Obtenha uma prévia do seu público clicando em **Revisar e criar**. Por padrão, o Segment consulta todos os dados históricos para definir o valor atual do traço calculado e do público. Para omitir esses dados, desmarque **Preenchimento Histórico**.
5. Nas configurações de traço ou público calculado, ajuste as configurações de conexão com base em como você gostaria que seus dados fossem enviados para a Braze.

#### Traços e públicos calculados

[Traços computados](https://segment.com/docs/engage/audiences/computed-traits/) e [públicos](https://segment.com/docs/Engage/audiences/) podem ser enviados para Braze como atributos personalizados ou eventos personalizados.
- Características e públicos enviados usando a chamada `identify` aparecerão no Braze como atributos personalizados.
- Características e públicos enviados usando a chamada `track` aparecerão no Braze como eventos personalizados.

Você pode escolher qual método usar (ou escolher usar ambos) quando conectar o traço calculado ao destino Braze.

{% tabs %}
{% tab Identificar %}

Você pode enviar características e públicos calculados para a Braze como `identify` chamadas para criar atributos personalizados na Braze. 

Por exemplo, se você tiver uma característica computada do Engage para "Último item visualizado", `last_product_viewed_item` será exibido no perfil do usuário na Braze em **Atributos personalizados**. Se este fosse um público do Engage, você encontraria seu público listado em **Atributos personalizados** definidos como `true`.

| Traço Computado | Públicos |
| -------------- | --------- |
| ![A seção de atributos personalizados em um perfil de usuário lista "last_product_viewed_item" como "Sweater" (Suéter).]({% image_buster /assets/img/segment/last_viewed-id-braze.png %}) | ![A seção de atributos personalizados em um perfil de usuário lista "dormant_shopper" como "true".]({% image_buster /assets/img/segment/dormant-identify-braze.png %}) |

{% endtab %}
{% tab Rastrear %}

Você pode enviar características e públicos calculados para a Braze como `track` chamadas para criar eventos personalizados na Braze. 

Continuando o exemplo anterior, se um usuário tiver uma característica calculada para "Último Produto Visualizado", ela aparecerá nos perfis dos usuários na Braze como `Trait Computed` com a contagem correspondente e o carimbo de data/hora mais recente em **Eventos Personalizados**. Se este fosse um público do Engage, você encontraria seu público, contagem e o carimbo de data/hora mais recente listados em **Atributos Personalizados** definidos como `true`.

| Traço Computado | Públicos |
| -------------- | --------- |
| ![A seção de eventos personalizados em um perfil de usuário lista "Característica computada" "1" vez, sendo a última vez "20 horas atrás".]({% image_buster /assets/img/segment/last_viewed-track-braze.png %}) | ![A seção de atributos personalizados em um perfil de usuário lista "Público entrou" "1" vez, sendo a última vez "9 de março, às 1h45".]({% image_buster /assets/img/segment/dormant-track-braze.png %}) |

{% endtab %}
{% endtabs %}

### Etapa 2: Segmentar usuários no Braze

No Braze, para criar um segmento desses usuários, navegue até **Segmentos** em **engajamento**, crie um novo segmento e nomeie seu segmento. Em seguida, com base na chamada que você usou:
- **Identificar**: Selecione **atributo personalizado** como o filtro e localize seu atributo personalizado. Em seguida, use a opção "corresponde a uma expressão regular" (característica) ou a opção "igual a" (público) e insira a variável apropriada.
- **Rastrear**: Selecione **evento personalizado** como o filtro e localize seu evento personalizado. Em seguida, use a opção "mais de", "menos de" ou "exatamente" e insira o valor desejado. Isso dependerá de como você deseja definir seu segmento.

Depois de salvo, você pode referenciar este segmento durante a criação da canva ou campanha na etapa de direcionamento de usuários.

## Sincronizar tempo

Embora a configuração padrão para a conexão Braze com Segment Engage seja `Realtime`, existem alguns filtros que desqualificarão a persona de sincronizar em tempo real, incluindo alguns filtros baseados em tempo que restringem o tamanho do seu público no momento do envio da mensagem.

## Teste de depuração de segmento

O dashboard do Segment fornece um recurso "Debugger" que permite aos clientes testar se os dados de uma "Fonte" estão sendo transferidos para um "Destino" conforme esperado.

Este recurso se conecta ao endpoint Braze [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), o que significa que só pode ser usado para usuários identificados (usuários que já possuem um ID de usuário para seu perfil de usuário Braze).

Isso não funcionará para uma integração Braze lado a lado. Nenhum dado do servidor será transmitido se você não tiver inserido as informações corretas da API REST da Braze.

