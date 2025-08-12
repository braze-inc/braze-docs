---
nav_title: Snowplow
article_title: Snowplow
description: "Este artigo de referência descreve a parceria entre o Braze e a Snowplow, uma plataforma de coleta de dados de código aberto, que permite encaminhar eventos da Snowplow para o Braze por meio da tag do lado do servidor do Google Tag Manager."
alias: /partners/snowplow/
page_type: partner
search_tag: Partner

---

# Snowplow

> A [Snowplow](https://snowplowanalytics.com) é uma plataforma de código aberto dimensionável para coleta de dados avançados, de alta qualidade e de baixa latência. Ela foi projetada para coletar dados comportamentais completos e de alta qualidade para empresas.

_Essa integração é mantida pela Snowplow._

## Sobre a integração

A integração lado a lado entre o Braze e o Snowplow ativa a capacitação dos usuários para encaminhar eventos do Snowplow para o Braze por meio da tag do lado do servidor do Google Tag Manager. A tag Braze da Snowplow permite que você envie eventos para a Braze enquanto oferece flexibilidade e controle adicionais:
- Visibilidade total de todas as transformações nos dados
- Capacidade de desenvolver a sofisticação ao longo do tempo
- Todos os dados permanecem em sua nuvem privada até que você escolha encaminhá-los
- Facilidade de configuração devido às ricas bibliotecas de tags e à interface de usuário familiar do Google Tag Manager

Aproveite os ricos dados de comportamento da Snowplow para promover interações poderosas centradas no cliente no Braze e enviar mensagens personalizadas em tempo real.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Pipeline da Snowplow | Um pipeline de Snowplow precisa estar em funcionamento. |
| No lado do servidor do Google Tag Manager | O GTM-SS precisa ser implantado, e é preciso configurar o [cliente da Snowplow para o GTM-SS](https://docs.snowplowanalytics.com/docs/forwarding-events-to-destinations/forwarding-events/google-tag-manager-server-side/snowplow-client-for-gtm-ss/). |
| chave da API REST Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint dependerá do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

### Entrega personalizada e baseada em ação
Use qualquer um dos inúmeros eventos avançados que a Snowplow coleta por padrão ou defina seus eventos personalizados para moldar jornadas de clientes ainda mais granulares que façam sentido para sua empresa. Aproveite os ricos dados de comportamento da Snowplow para projetar funis de clientes e liberar valor para suas equipes de marketing e de produtos, ajudando-as a maximizar a conversão e o uso do produto por meio do Braze.

### Segmentação dinâmica
Crie públicos dinâmicos no Braze com base nos dados comportamentais de alta qualidade da Snowplow: À medida que os usuários realizam ações em seu produto, app ou site, é possível aproveitar os dados de comportamento em tempo real coletados pela Snowplow para adicionar ou remover automaticamente usuários de segmentos relevantes no Braze.

## Integração

### Etapa 1: Instalação do modelo

#### Instalação manual

1. Baixe o arquivo de modelo [`template.tpl`](https://github.com/snowplow/snowplow-gtm-server-side-braze-tag/blob/main/template.tpl).
2. Crie uma nova tag na seção **Modelos** de um contêiner de servidor do Google Tag Manager.
3. Clique no menu **More Actions (Mais ações** ) no canto superior direito e selecione **Import (Importar**).
4. Importe o arquivo de modelo baixado e salve-o.

#### Galeria do Tag Manager

Em breve! Essa tag está aguardando aprovação para ser incluída na galeria do GTM.

### Etapa 2: configuração da tag da Braze

Com o modelo instalado, adicione a tag da Braze ao seu contêiner GTM-SS.

1. Na guia **Tag**, selecione **New (Novo**) e, em seguida, selecione **Braze Tag (Tag do Braze** ) como sua configuração de tag.
2. Selecione o gatilho desejado para os eventos que deseja encaminhar para a Braze.
3. Insira os parâmetros necessários e configure sua tag (mais detalhes podem ser encontrados na seção Personalização a seguir).
4. Clique em **Salvar**.

## Personalização

### Parâmetros de tag necessários

A tabela a seguir lista os parâmetros de tag necessários que devem ser incluídos na configuração de sua tag Braze.

| Parâmetro | Descrição |
| --------- | ----------- |
| Ponto de extremidade da API do Braze REST | Defina como o URL do seu [endpoint]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) REST da Braze. |
| Chave de API do Braze | Defina isso como sua [chave de API]({{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys) do Braze que será incluída em cada solicitação. |
| Braze `external_id` | Defina essa chave como a propriedade do evento do cliente que corresponde ao `external_id` dos seus usuários e que será usada como o [identificador de usuário do Braze]({{site.baseurl}}/developer_guide/rest_api/basics/#external-user-id-explanation). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Mapeamento de eventos

A tabela a seguir lista as opções de mapeamento de eventos referentes ao evento Snowplow, conforme reivindicado pelo [cliente Snowplow](https://docs.snowplowanalytics.com/docs/forwarding-events-to-destinations/forwarding-events/google-tag-manager-server-side/snowplow-client-for-gtm-ss/).

| Opção de mapeamento | Descrição |
| --------- | ----------- |
| Incluir a autodescrição do evento | Ativado por padrão. Indica se os dados do evento de autodescrição do Snowplow serão incluídos nos objetos de propriedades do evento enviados ao Braze. |
| Regras de contexto do evento Snowplow | Descreve como a tag Braze usará as entidades de contexto anexadas a um evento Snowplow. |
| Extrair entidade da matriz se for um único elemento | As entidades de limpa-neve estão sempre em matrizes, pois várias da mesma entidade podem ser anexadas a um evento. Essa opção escolherá o único elemento da matriz se a matriz contiver apenas um único elemento. |
| Incluir todas as entidades no objeto de evento | Ativado por padrão. Inclui todas as entidades em um evento dentro do objeto de propriedades do evento Braze. Desative essa opção para selecionar entidades individuais para inclusão. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Mapeamento avançado de eventos

#### Regras de propriedade de eventos

Se você quiser incluir outras propriedades do evento do cliente e mapeá-las para o evento do Braze, consulte as regras na tabela a seguir: 

| Regras de propriedade de eventos | Descrição |
| --------- | ----------- |
| Incluir propriedades de eventos comuns | Ativada por padrão, essa opção define se as propriedades do evento da [definição de evento comum](https://developers.google.com/tag-platform/tag-manager/server-side/common-event-data) serão incluídas automaticamente nas propriedades do evento Braze. |
| Regras adicionais de mapeamento de propriedades de usuário e de eventos | Especifique a chave da propriedade do evento do cliente e a chave do objeto das propriedades que você gostaria de mapear (ou deixe a chave mapeada em branco para manter o mesmo nome). Você pode usar a notação de jornada de chave aqui (por exemplo, `x-sp-tp2.p` para uma plataforma de eventos Snowplow ou `x-sp-contexts.com_snowplowanalytics_snowplow_web_page_1.0.id` para um ID de exibição de página de eventos Snowplow (no índice 0 da matriz) ou escolher propriedades não Snowplow se estiver usando um cliente alternativo.<br><br>As regras de mapeamento de propriedades de eventos preenchem o objeto de propriedades de eventos do Braze.|
| Incluir propriedades comuns do usuário| Ativada por padrão, essa opção define se as propriedades `user_data` da definição de evento comum devem ser incluídas no objeto de atribuições do usuário do Braze.|
| Propriedade de tempo do evento | Essa opção permite especificar a propriedade de evento do cliente para preencher a hora do evento (no formato ISO-8601) ou deixá-la vazia para usar a hora atual (comportamento padrão). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Mapeamento de entidades

Usando a tabela de mapeamento de entidades do Snowplow, as entidades podem ser remapeadas para terem nomes diferentes no Braze e incluídas em propriedades de eventos ou objetos de atribuições de usuários. 

A entidade pode ser especificada em dois formatos diferentes:
- Correspondência da versão principal: `x-sp-contexts_com_snowplowanalytics_snowplow_web_page_1`, em que `com_snowplowanalytics_snowplow` é o fornecedor do evento, `web_page` é o nome do esquema, e `1` é o número da versão principal. `x-sp-` também pode ser omitido, se desejado.
- Correspondência total do esquema: `iglu:com.snowplowanalytics.snowplow/webPage/jsonschema/1-0-0`
<br><br>

| Opção de mapeamento de entidade | Descrição |
| --------- | ----------- |
| Incluir entidades não mapeadas no evento | Ao remapear ou mover algumas entidades para atributos de usuário com a personalização anterior, essa opção ativa a garantia de que todas as entidades não mapeadas (como quaisquer entidades não encontradas nas [regras de propriedade do evento](#event-property-rules)) serão incluídas no objeto de propriedades do evento Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


