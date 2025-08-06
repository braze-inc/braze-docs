---
nav_title: API de Personalização Hightouch
article_title: API de Personalização Hightouch
description: "Este artigo de referência descreve a integração entre a Braze e a API de Personalização da Hightouch, um serviço gerenciado para hospedar uma API de dados de baixa latência baseada em qualquer conjunto de dados dentro do seu data warehouse na nuvem. Este artigo de referência aborda os casos de uso que a API de personalização da Hightouch resolve, os dados com os quais ela trabalha, como configurá-la e como integrá-la com a Braze."
page_type: partner
search_tag: Partner
---

# API de Personalização Hightouch

> A [API de Personalização](https://hightouch.com/docs/destinations/personalization-api) do Hightouch é um serviço gerenciado que permite hospedar uma API de dados de baixa latência baseada em qualquer conjunto de dados no seu data warehouse na nuvem.

![]({% image_buster /assets/img/hightouch/cohort7.png %})

A integração da Braze e da Hightouch permite que você use a API com [conteúdo conectado da Braze]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) para obter dados atualizados de clientes ou objetos em suas campanhas ou canvas no momento do envio.

A API de Personalização da Hightouch fornece um endpoint REST para usar na sua configuração do Braze. Especificamente, você pode usar a oferta de Conteúdo Conectado do Braze para fazer uma solicitação GET à API de Personalização para recuperar todas as informações relacionadas a um identificador específico. Os dados expostos pela API podem representar dados de clientes, produtos ou qualquer outro objeto. 

![]({% image_buster /assets/img/hightouch/cohort6.png %})

## Pré-requisitos

| Requisito| Descrição|
| ---| ---| 
| [Conta Hightouch](https://app.hightouch.com/login) com API de Personalização ativada | É necessária uma conta [Business Tier](https://hightouch.com/pricing) da Hightouch para usar a parceria.|
| Casos de uso definidos | Antes de configurar a API, determine seu caso de uso para a integração. Consulte a lista a seguir para ver os casos de uso comuns. |
| Dados armazenados em um data warehouse na nuvem ou outra fonte | A Hightouch tem integração com [mais de 25 fontes de dados](https://hightouch.com/integrations) |
| chave de API Hightouch | Pode ser criada em **Hightouch > Settings > API keys > Add API key** (Hightouch > Configurações > Chaves de API > Adicionar chave de API). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs %}
{% tab Casos de uso %}

### Casos de uso

Antes de começar, é útil planejar exatamente como você deseja usar a API de personalização.

Casos de uso comuns incluem:
- **Recomendações de produtos** para simplificar a incorporação de recomendações de produtos personalizadas em templates de e-mail, campanhas ou experiências no app
- **Impulsionando campanhas de marketing personalizadas** ao enriquecer os pontos de contato de marketing com recomendações de produtos dinâmicas
- **Oferecendo personalização no app ou na web**, por exemplo, resultados de pesquisa personalizados, preços baseados em coorte e envio de mensagens, recomendações de artigos ou localizações de lojas mais próximas
- **Recomendações baseadas em dados financeiros ou médicos**—dados financeiros têm requisitos rigorosos que a Hightouch atende por meio de suas [políticas rigorosas de segurança de dados](https://hightouch.com/docs/security/overview#compliance). Com a Hightouch, você pode criar segmentos de clientes com base em dados financeiros ou médicos sem expor os atributos subjacentes usados em seus critérios de segmentação.

{% endtab %}
{% tab Conjuntos de dados %}

### Conjuntos de dados

A API de Personalização atua como um cache para os dados selecionados em seu armazém, então você já deve ter os dados de recomendação armazenados lá. Você pode usar Hightouch para transformá-lo de acordo com um modelo, se necessário. Este tipo de dados inclui:
- Metadados do usuário, como região geográfica, idade ou outras informações demográficas
- Ações ou eventos do usuário, incluindo compras anteriores, visualizações de páginas, cliques, etc.

{% endtab %}
{% endtabs %}

## Integração

### Etapa 1: Conectar a fonte de dados ao Hightouch

As [fontes](https://hightouch.com/docs/getting-started/concepts#sources) da Hightouch são onde os dados comerciais da sua organização residem. Neste caso, é onde seus dados de usuários são armazenados.
1. Na Hightouch, acesse **Sources Overview > Add Source** (Visão geral das fontes > Adicionar fonte). Selecione seu data warehouse como a fonte.<br><br>
2. Insira as credenciais relevantes; estas variarão dependendo da fonte. 

Para mais detalhes, consulte a [documentação](https://hightouch.com/docs) relevante.

### Etapa 2: Dados do modelo

Os modelos Hightouch definem quais dados extrair da sua fonte. Para configurar um novo modelo, siga estas etapas:

1. No Hightouch, Acessar [**Visão geral dos modelos**](https://app.hightouch.com/models) > **Adicionar modelo**, e selecione a fonte que você acabou de conectar. <br><br>
2. Em seguida, escolha um [método de modelagem](https://hightouch.com/docs/models/creating-models). Como todas as suas informações devem ser unidas em uma tabela, você pode usar o seletor de tabela visual para defini-la. Alternativamente, você pode escrever SQL para incluir apenas as colunas que deseja ou confiar em seus modelos dbt existentes, Looker Looks ou workbooks da Sigma.<br><br>
3. Antes de continuar, veja uma prévia do seu modelo para confirmar se ele está consultando seus dados de interesse. Por padrão, a Braze limita a prévia aos primeiros 100 registros. Depois de validar seus dados, clique em **Continue** (Continuar).<br><br>
4. Dê um nome ao seu modelo, por exemplo, "Recomendações do usuário."<br><br>
5. Por fim, selecione uma chave primária e clique em **Finish** (Concluir). Uma chave primária deve ser uma coluna com identificadores únicos. Este é também o campo que você usará para chamar a API de personalização para recuperar as recomendações de um usuário específico.

### Etapa 3: Configurar API de personalização

A preparação da API para receber solicitações tem duas etapas:
- Habilitando a API de personalização nas regiões mais próximas da sua infraestrutura
- Criando sincronizações para definir quais modelos devem ser materializados no cache gerenciado pelo Hightouch

Siga estas instruções para completar ambos:

1. Na Hightouch, acesse [**Destinations**](https://app.hightouch.com/destinations) (Destinos) e selecione a API de personalização da Hightouch criada para você. Se você não tiver esse destino habilitado, entre em contato com o suporte da [Hightouch](mailto:friends@hightouch.com).<br><br>
2. Em seguida, selecione a região apropriada. Selecionar a região mais próxima da sua infraestrutura reduzirá seus tempos de resposta. Se você não vir uma região próxima à sua infraestrutura, entre em contato com o [suporte da Hightouch](mailto:friends@hightouch.com).<br><br>
3. Acessar a [**Visão geral de sincronizações** página de visão geral](https://app.hightouch.com/syncs) e clicar no botão **Adicionar sincronização**. Em seguida, selecione o modelo relevante e o destino que você configurou anteriormente.<br><br> 
4. Digite um nome de coleção alfanumérico. Coleções são conceitualmente semelhantes a tabelas de banco de dados. Cada um deve representar um tipo de dado específico, como clientes ou faturas. Os nomes das coleções devem ser alfanuméricos e farão parte do seu endpoint da API de Personalização.<br><br>
5. Em seguida, especifique qual coluna do seu modelo deve servir como índice principal para consultas de registros. Este campo deve identificar exclusivamente cada registro na coleção e muitas vezes é o mesmo que a chave primária do seu modelo. A API de personalização suporta pesquisas em vários índices. Por exemplo, pode ser do seu interesse recuperar perfis de clientes usando `user_id`, `anonymous_id` ou `email_address`. Para ativar vários índices, entre em contato com o [suporte da Hightouch](mailto:friends@hightouch.com).<br><br>
6. Use o mapeador de campo para especificar quais colunas do seu modelo devem ser incluídas na carga útil da resposta da API. Você pode renomear esses campos e usar o mapeador avançado para aplicar transformações usando a linguagem de modelo Liquid.<br><br>
7. Selecione o [comportamento de exclusão](https://www.hightouch.com/docs/destinations/personalization-api#delete-behavior) apropriado para o seu caso de uso.<br><br>
8. Por fim, clique em **Continue** (Continuar) e depois selecione um [cronograma de sincronização](https://hightouch.com/docs/syncs/schedule-sync-ui).

Hightouch agora sincronizará os dados em seu armazém para um banco de dados gerenciado e os exporá através da API de Personalização.

### Etapa 4: Chame a API de personalização através do Braze Connected Content

Depois de configurar sua instância de API de personalização, você pode usá-la como um endpoint de Conteúdo Conectado do Braze. 

A API está acessível em `https://personalization.{region}.hightouch.com`, por exemplo, `https://personalization.us-west-2.hightouch.com`. 

A informação está disponível usando este endpoint `/v1/collections/:collection_name/records/:index_key/:index_value`.

Por exemplo, você poderia incluir este trecho em uma campanha ou canva:

{% raw %}

```liquid
{% connected_content
     https://personalization.us-west-2.hightouch.com/v1/collections/customer/records/id/12345
     :method get
     :headers {
       "Authorization": "Bearer {{YOUR-API-KEY}}"
  }
     :content_type application/json
     :save customer
%}
```
{% endraw %}

Você pode usar a modelagem Liquid para referenciar as propriedades retornadas na carga útil JSON e usá-las no seu envio de mensagens.

Para a carga útil de exemplo abaixo:

```json
{
    "user_id": 12345,
    "full_name": "Jane Doe",
    "lifetime_value": 1492.18,
    "churn_risk": 0.04,
    "90_day_summary": {
        "num_songs_listened": 813,
        "top_genres": [
            "house",
            "techno",
            "ambient"
        ],
        "top_artists": [
            "deadmau5",
            "Marsh",
            "Enamour"
        ],
    },
    "recommendations": {
        "concerts": [
            {
                "artist": "Aphex Twin",
                "location": "San Francisco, CA",
                "event_date": "2023-01-31"
            },
            {
                "artist": "Sultan + Shepard",
                "location": "San Francisco, CA",
                "event_date": "2023-02-25"
            }
        ],
        "upcoming_album_release": {
            "title": "Universal Language",
            "artist": "Simon Doty",
            "label": "Anjunadeep",
            "release_date": "2023-04-28"
        }
    },
}
```

As seguintes referências do Liquid retornariam este exemplo de dados:

| Liquid modelo | Exemplo devolvido |
| --- | --- |
| {% raw %}`{{artists.recommendations.concerts[0].artist}}`{% endraw %}| Aphex Twin |
| {% raw %}`{{artists.recommendations.concerts[0].location}}`{% endraw %}| San Francisco, CA |
| {% raw %}`{{artists.recommendations.upcoming_album_release.title}}`{% endraw %}| Língua Universal |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Solução de problemas

Se você tiver dúvidas, entre em contato com o suporte da [Hightouch](mailto:friends@hightouch.com) para obter assistência.

