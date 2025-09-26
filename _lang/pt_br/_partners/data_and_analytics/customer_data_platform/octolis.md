---
nav_title: Octolis
article_title: Octolis
description: "Este artigo de referência descreve a parceria entre a Braze e a Octolis, uma plataforma de ativação de dados que permite integrar seus dados à Braze."
alias: /partners/octolis/
page_type: partner
search_tag: Octolis

---

# Octolis

> A [Octolis](http://octolis.com) é uma poderosa plataforma de ativação de dados (ou plataforma de dados do cliente headless). Sobreposto a um banco de dados de sua propriedade, o Octolis é uma maneira fácil de unificar, preparar, pontuar e sincronizar dados em suas ferramentas de negócios.

_Essa integração é mantida pela Octolis._

## Sobre a integração

A integração da Braze com a Octolis atua como middleware entre suas fontes de dados brutos e a Braze, permitindo recuperar e unificar dados de várias fontes, online e offline:
1. Unifique e combine dados de fontes como loja virtual, CRM, sistema de PDV etc.
2. Normalizar e pontuar
3. Sincronização em tempo real de campos computados e eventos para o Braze

![]({% image_buster /assets/img/Octolis/Braze_scheme.png %})

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Octolis | É necessário ter uma conta Octolis para usar esta parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões [**users.track**]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint dependerá do URL do Braze para sua instância. |
| Chave do app da Braze | A chave do identificador de seu app. Ela pode ser entrada em **Dashboard da Braze > Gerenciar configurações > Chave de API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

Antes de iniciar a integração, consulte as seções a seguir sobre conexões, fontes, públicos e sincronizações.

Para obter mais informações, consulte a seção [Como começar](https://help.octolis.com/) da Octolis.

### Etapa 1: Conecte o Octolis às suas fontes de dados

Para enviar dados para a Braze, confirme se você criou pelo menos um [público](https://help.octolis.com/audiences/create-a-no-code-audience). Um público combina várias fontes de dados, aplica-as às etapas de preparação e adiciona campos computados.

Esses públicos precisam ser criados com base em várias fontes de dados. Uma fonte pode ser qualquer uma das seguintes:
- Um objeto do Salesforce (contatos, contas, etc.)
- Um objeto do Zendesk (tickets)
- Um arquivo dentro de um SFTP (arquivo CSV contendo alguns contatos, arquivo JSON contendo eventos...)
- Uma tabela/visualização de um banco de dados.
- Um dos seus sistemas nos envia registros por meio de webhooks ou chamadas de API.

### Etapa 2: Adicionar Braze como um destino

Em seguida, para definir o Braze como um novo destino, selecione **\+ Adicionar mais** na parte superior do seu destino atual na tela principal e selecione **Braze** entre as ferramentas de negócios disponíveis.

![]({% image_buster /assets/img/Octolis/Braze_screen2.png %})

Depois de selecionado, forneça o seguinte:

- Sua chave de API do Braze: Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**.
- Período: O Octolis aplicará a limitação de taxa no período determinado.
- Volume da solicitação: Número de solicitações que você pode fazer dentro desse período de tempo.
- Atributos personalizados: Especifique aqui os novos campos que você enviará ao Braze, seu formato (string, integer, float) e marque a opção **Required for syncs** se quiser que um deles seja obrigatório para uma sincronização.

![]({% image_buster /assets/img/Octolis/Braze_screen3.png %})

Após a configuração, a Braze aparecerá como um novo destino na tela inicial.

### Etapa 3: Criar uma nova sincronização

No menu, clique em **Syncs (Sincronizações)** e selecione **Add sync (Adicionar sincronização** ) no canto superior direito. Selecione o público que deseja selecionar a partir do público que você criou antes.
Em seguida, selecione **Braze** como o destino e para qual entidade você enviará os dados.

![]({% image_buster /assets/img/Octolis/Braze_screen4.png %})

### Etapa 4: Definir configurações de saída

Por padrão, a Braze cria todos os atributos que você enviaria, mas é preciso documentar a lista de campos a serem sincronizados.

![]({% image_buster /assets/img/Octolis/Braze_screen5.png %}){: style="max-width:75%;"}

Aqui está uma definição específica dos campos de configuração.

| Campo | Descrição |
| --- | --- |
| Para onde você deseja sincronizar o público? | A entidade Braze onde você criará ou atualizará registros. |
| Qual campo é usado para identificar um registro? | O campo usará o Octolis para identificar um registro se ele já existir no Braze. |
| Com que frequência você deseja enviar cada registro? | Por padrão, a sincronização será incremental para todas as integrações (API, banco de dados, FTP). Isso significa que somente os novos valores desde a última atualização serão atualizados. Caso necessário, você também pode enviar tabelas inteiras em intervalos regulares. Ao iniciar, a Octolis enviará a tabela completa. |
| Quais campos devem ser sincronizados? | Mapeamento de campos de Octolis para Braze. A lista de todos os campos disponíveis aparece no menu suspenso. Para enviar um campo computado para o Braze, você deve primeiro garantir que criou a coluna correspondente em sua entidade Braze. |
| Quando você deseja sincronizar o público? | Como os dados serão enviados à Braze: manualmente, em tempo real ou em períodos programados.  |
| Sincronizar quando o registro é... | Criar: para aceitação, é importante que a tabela da Braze continue sendo a principal. Não é ideal que a Octolis dispare uma sincronização quando o campo for atualizado.<br><br>Atualizar: por outro lado, para um campo de nome, por exemplo, é recomendável atualizar o campo na tabela da Braze sempre que um cliente informar uma nova entrada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Desduplicação de várias chaves

A desduplicação é um grande desafio ao reconciliar dados de várias fontes, especialmente online e offline. Por meio do módulo avançado sem código do Octolis, você pode usar várias chaves para [deduplicação](https://help.octolis.com/resources/faq/what-is-deduplication-and-how-does-it-work). Esse módulo está disponível para cada tabela mestre, o que significa que você pode adaptar a lógica a cada entidade.


