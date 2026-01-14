---
nav_title: Redpoint
article_title: Redpoint 
description: "A integração da Redpoint à Braze permite a integração e o enriquecimento dos perfis de usuários da Braze com seus dados primários."
alias: /partners/redpoint/
page_type: partner
search_tag: Redpoint
---

# Redpoint

> [A Redpoint](https://www.redpointglobal.com) é uma plataforma de tecnologia que fornece aos profissionais de marketing uma plataforma de orquestração de campanhas totalmente integrada. Aproveite os recursos de segmentação, programação e automação do Redpoint para controlar como e quando os dados do CDP são importados para o Braze.

_Essa integração é mantida pela Redpoint._

## Sobre a integração

A integração entre a Braze e a Redpoint permite criar segmentos da Braze com base nos dados da Redpoint CDP. A Redpoint fornece dois modos de transmissão de dados para a Braze: 

1. Modo **Integração e upsert na Braze**: faz "upserts" um perfil de usuário da Redpoint para a Braze. É usado na integração ou atualização de registros de usuários quando os dados são alterados. 
2. Modo **Acréscimo à Braze**: Atualiza um perfil de usuário se esse usuário já existir no Braze. 

Você configurará um modelo de exportação e um canal de saída para cada modo.

{% alert note %}
"Upsert" é uma combinação das palavras "update" (atualização) e "insert" (inserção). É usado quando se deseja inserir um novo registro em uma tabela do banco de dados, se ele ainda não existir, ou atualizar o registro, se ele já existir. Essencialmente, o upsert verifica se um determinado registro está presente no banco de dados. Se o registro estiver presente, ele será atualizado e, se não estiver presente, um novo registro será inserido.
{% endalert %}

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| chave da API REST Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br>Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint dependerá da URL do Braze para sua instância. |
| Artefatos de gerenciamento de dados do Redpoint | A integração da Braze é suportada por um conjunto de artefatos do Redpoint Data Management. Entre em contato com o [suporte da Redpoint](https://support.redpointglobal.com/hc/en-us/restricted?return_to=https%3A%2F%2Fsupport.redpointglobal.com%2Fhc%2Fen-us) para solicitar os artefatos para a sua versão do Redpoint Data Management. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Atributos personalizados do Redpoint CDP

Os seguintes atributos personalizados do Redpoint podem ser adicionados a um perfil de usuário do Braze.

| Campo               | Descrição                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `rpi_cdp_attributes` | O objeto de atribuição de perfil Redpoint CDP                                                                                  |
| `rpi_audience_outputs`| Matriz de tags de saída do público para o qual o usuário é direcionado em uma execução do canal Redpoint Outbound Delivery Braze         |
| `rpi_offers`         | Conjunto de tags de oferta em que o usuário é direcionado em uma execução do canal Redpoint Outbound Delivery Braze                   |
| `rpi_contact_ids`    | Matriz de IDs de contato do histórico de ofertas em que o usuário é direcionado em uma execução de canal do Redpoint Outbound Delivery Braze     |
| `rpi_channel_exec_ids`| Matriz de IDs de execução de canal em que o usuário é direcionado em uma execução de canal do Redpoint Outbound Delivery Braze       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/redpoint/rpi_to_braze_custom_attributes.png %}){: style="max-width:75%;"}

## Integração

### Etapa 1: Configurar modelos

#### Etapa 1a: criar o modelo de integração e upsert da Braze

No Redpoint Interaction (RPI), crie um novo modelo de exportação e dê a ele o nome **Integração e upsert da Braze**. Esse modelo define os mapeamentos principais entre o Redpoint CDP e o perfil de usuário do Braze, juntamente com quaisquer atributos personalizados adicionais que você queira adicionar aos seus perfis de usuário no Braze.

Arraste as atribuições do Redpoint CDP para a coluna **Attribute (Atributo** ). Defina cada **valor de linha do cabeçalho** como a [atribuição de usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) Braze correspondente. 

A tabela a seguir lista as atribuições da Redpoint CDP e seus atributos correspondentes na Braze:

| Atribuição do Redpoint | Valor da linha do cabeçalho |
|--------------------|------------------|
| PID                | `external_id`    |
| Nome          | `first_name`     |
| Sobrenome          | `last_name`      |
| E-mail principal      | `email`          |
| País principal    | `country`        |
| DATA DE NASCIMENTO                | `dob`            |
| Gênero             | `gender`         |
| Cidade principal       | `home_city`      |
| Telefone principal      | `phone`          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Adicione a atribuição **Output Name** da tabela **Offer History (Histórico de ofertas** ). Por fim, adicione quaisquer atributos personalizados adicionais da Redpoint que você queira mesclar na Braze. Por exemplo, o modelo a seguir faz integração e atualização com educação, renda e estado civil como atributos adicionais.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_upsert_export_format.png %}){: style="max-width:75%;"}

#### Etapa 1b: Criar o modelo Braze Append

Crie um segundo modelo de exportação para operações somente de acréscimo, denominado **Acréscimo à Braze**.

Você definirá apenas duas atribuições para esse modelo. Para o **PID**, defina o **valor da linha do cabeçalho** como `external_id`. Em **Output Name**, defina o **Header Row** como `output_name`.

![Um modelo de exportação de amostra com os atributos `external_id` e nome de saída.]({% image_buster /assets/img/redpoint/rpi_to_braze_append_export_format.png %}){: style="max-width:75%;"}

#### Etapa 1c: Definir formato de data

Para ambos os modelos de exportação, navegue até a guia **Opções** e defina o **Formato de data** como o valor de **Formato personalizado**. Defina o formato como **aaaa-MM-dd**.

![A guia de opções mostra o formato de data definido como aaaa-MM-dd.]({% image_buster /assets/img/redpoint/rpi_to_braze_export_format_config.png %}){: style="max-width:75%;"}

### Etapa 2: Criar canais de saída

No RPI, crie dois novos canais. Defina ambos os canais como **Entrega de saída**. Nomeie um canal como **Braze Onboarding e Upsert** e o outro como **Braze Append**.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_general.png %}){: style="max-width:75%;"}

{% alert note %}
Após a integração inicial dos registros da CDP à Braze, verifique se os fluxos de trabalho subsequentes do Redpoint Interaction que usam o canal de integração e upsert da Braze foram projetados para selecionar apenas os registros alterados desde a sincronização inicial de integração.
{% endalert %}

### Etapa 3: Configurar os canais

#### Etapa 3a: defina o modelo e o formato do caminho de exportação

Navegue até a guia **General (Geral** ) na tela de **configuração de** canais. Defina o modelo de exportação para cada canal respectivo. 

Em seguida, defina um **formato de caminho de exportação** em ambos os canais que aponte para uma rede compartilhada, protocolo de transferência de arquivos ou local de provedor de conteúdo externo que seja acessível ao Redpoint Interaction e ao Redpoint Data Management. 

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_specific.png %}){: style="max-width:75%;"}

O formato do diretório de exportação em ambos os canais será idêntico e deverá terminar com `\\[Channel]\\[Offer]\\[Workflow ID]`.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_export_directory_setup.png %}){: style="max-width:50%;"}

#### Etapa 3b: Configurar a pós-execução

Navegue até a guia **Post Execution** (Pós-execução) na tela **Channels Configuration** (Configuração de canais). 

Marque a caixa de seleção **Pós-execução** para chamar um URL de serviço após a execução do canal. Digite o URL do serviço da Web do Redpoint Data Management. Essa entrada será idêntica tanto no seu canal de integração quanto no de acréscimo.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_post_execution.png %}){: style="max-width:75%;"}

### Etapa 4: Configurar os componentes do Braze no Redpoint Data Management 

O arquivo que contém os artefatos do Redpoint Data Management (RPDM) para suportar a integração do Braze contém um README com instruções detalhadas para configurar os componentes necessários. Tenha em mente os seguintes detalhes ao configurar sua integração. 

#### Etapa 4a: atualize a automação RPI para Braze com seu endpoint REST da Braze e o diretório de saída RPI de base 

Depois de importar os artefatos relacionados à Braze para o Redpoint Data Management, abra a automação denominada **AUTO_Process_RPI_to_Braze** e atualize as duas variáveis de automação a seguir com os valores de seu ambiente:

* **BRAZE_API_URL**: O ponto de extremidade Braze REST
* **BASE_OUTPUT_DIRECTORY**: o diretório de saída compartilhado entre o Redpoint Interaction e o Redpoint Data Management

![]({% image_buster /assets/img/redpoint/rpi_to_braze_auto_variables.png %}){: style="max-width:40%;"}

#### Etapa 4b: Atualizar o projeto de anexação do RPI ao Braze 

O projeto de gerenciamento de dados do Redpoint chamado **PROJ_RPI_to_Braze_Append** contém o esquema de arquivo de exportação de entrega e mapeamentos para o objeto de atributo personalizado `rpi_cdp_attributes` na Braze. 

Atualize o esquema de entrada de arquivos e a ferramenta de injeção de documentos denominada **RPI para Braze Document Injector** com quaisquer atributos personalizados adicionais de CDP definidos em seu modelo de arquivo de exportação. Esse exemplo mostra o mapeamento adicional de educação, renda e estado civil:

![]({% image_buster /assets/img/redpoint/rpi_to_braze_doc_injector_mappings.png %}){: style="max-width:40%;"}

## Usando a integração

O canal Outbound Delivery Braze agora pode ser usado nos fluxos de trabalho do Redpoint Interaction. Siga as práticas padrão para criar regras de seleção e públicos no RPI e criar programações e disparos de fluxo de trabalho associados. 

Para ativar a sincronização de uma saída do público RPI para o Braze, crie uma oferta de entrega e associe-a ao canal **Braze Onboarding and Upsert** ou **Braze Append**. Isso depende se a intenção é criar ou mesclar novos registros no Braze ou apenas anexar dados de campanha se o registro já existir no Braze.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_rpi_canvas.png %}){: style="max-width:80%;"}

Após a execução bem-sucedida do fluxo de trabalho no RPI, os dados de orquestração e CDP provenientes do RPI agora podem ser usados para criar segmentos no Braze.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_build_braze_segment.png %}){: style="max-width:80%;"}

Você pode visualizar as propriedades associadas ao Redpoint no perfil do usuário.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_record_example.png %}){: style="max-width:80%;"}


