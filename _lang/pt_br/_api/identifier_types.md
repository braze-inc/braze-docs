---
nav_title: "Tipos de identificadores de API"
article_title: Tipos de identificadores de API
page_order: 2.2
toc_headers: h2
description: "Este artigo de referência aborda os diferentes tipos de identificadores de API que existem no dashboard do Braze, onde você pode encontrá-los e para que são usados." 
page_type: reference

---

# Tipos de identificadores da API

> Este guia de referência aborda os diferentes tipos de identificadores de API que podem ser encontrados no dashboard da Braze, sua finalidade, onde você pode encontrá-los e como eles são normalmente usados. Para obter informações sobre as chaves da API REST ou as chaves da API do espaço de trabalho, consulte a [visão geral da API]({{site.baseurl}}/api/api_key/).

Os seguintes identificadores podem ser usados para acessar seu modelo, tela, campanha, segmento, envio ou cartão da API externa do Braze. Todas as mensagens devem seguir a codificação [UTF-8](https://en.wikipedia.org/wiki/UTF-8).

## Identificador do app

O identificador de aplicativo ou `app_id` é um parâmetro que associa a atividade a um app específico em seu espaço de trabalho. Ele designa com qual app dentro do espaço de trabalho você está interagindo. Por exemplo, você verá que terá um `app_id` para seu app para iOS, um `app_id` para seu app para Android e um `app_id` para sua integração na Web. No Braze, você pode descobrir que tem vários apps para a mesma plataforma nos vários tipos de plataforma suportados pelo Braze.

### Onde posso encontrá-lo?

Há duas maneiras de localizar seu `app_id`:

{% tabs local %}
{% tab Identificadores de app %}
Acesse **Settings** > **APIs and Identifiers** > **App Identifiers**. Sua chave de API para cada app está listada na coluna **Identificador**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), **o App Identifiers** está localizado em **Developer Console** > **API Settings**.
{% endalert %}
{% endtab %}

{% tab Configurações do app %}
Acessar **Configurações** > **Configurações do app**. Sua chave de API está listada ao lado do campo **Chave de API** na seção de configurações.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), **as App Settings** estão localizadas em **Manage Settings** > **Settings**.
{% endalert %}
{% endtab %}
{% endtabs %}

### Para que ele pode ser usado?

Os identificadores de aplicativos no Braze são usados na integração do SDK e também são usados para fazer referência a um aplicativo específico nas chamadas da API REST. Com o `app_id`, é possível fazer muitas coisas, como extrair dados de um evento personalizado que ocorreu em um determinado app, recuperar estatísticas de desinstalação, estatísticas de novos usuários, estatísticas de DAU e estatísticas de início de sessão de um determinado app.

{% alert tip %}
Às vezes, pode ser que seja solicitado um `app_id`, mas você não está trabalhando com um app, porque é um campo legado específico para uma plataforma específica. Você pode omitir esse campo incluindo qualquer string de caracteres como espaço reservado para esse parâmetro obrigatório.
{% endalert %}

### Vários identificadores de app

Durante a configuração do SDK, o caso de uso mais comum para vários identificadores de app é separar esses identificadores para variantes de compilação de depuração e lançamento.

Para alternar facilmente entre vários identificadores de app em suas compilações, recomendamos a criação de um arquivo `braze.xml` separado para cada [variante de compilação](https://developer.android.com/studio/build/build-variants.html) relevante. Uma variante de compilação é uma combinação de tipo de compilação e sabor do produto. Por padrão, um novo projeto Android é configurado com os tipos de compilação `debug` e `release` e nenhum tipo de produto.

Para cada variante de compilação relevante, crie um novo `braze.xml` para ela em `src/<build variant name>/res/values/`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">{YOUR_BUILD_VARIANT_API_KEY}</string>
</resources>
```
Quando a variante de compilação for compilada, ela usará o novo identificador.

## Identificador do modelo

Um identificador de [modelo]({{site.baseurl}}/api/endpoints/templates/) ou ID de modelo é uma chave aleatória gerada pelo Braze para um determinado modelo dentro do dashboard. Os IDs de modelo são exclusivos para cada modelo e podem ser usados para fazer referência a modelos por meio da API. 

Os modelos são ótimos para quando sua empresa contrata seus designs de HTML para campanhas. Depois que os modelos forem criados, você terá um modelo que não é específico para uma campanha, mas que pode ser aplicado a uma série de campanhas, como um boletim informativo.

### Onde posso encontrá-lo?

Você pode encontrar o ID do modelo de duas maneiras:

{% tabs local %}
{% tab Modelos %}
Acesse **Modelos**, selecione uma página de modelo e, em seguida, selecione um modelo pré-existente. Se o modelo que você deseja ainda não existir, crie um e salve-o. Na parte inferior da página do modelo individual, você poderá encontrar o identificador do modelo.
{% endtab %}

{% tab Chaves de API %}
Acesse **Configurações** > **APIs e identificadores**. Aqui, o Braze oferece uma pesquisa de **identificadores adicionais de API**, onde você pode procurar identificadores específicos.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar identificadores de API no **console do desenvolvedor** > **Configurações de API**.
{% endalert %}
{% endtab %}
{% endtabs %}

### Para que ele pode ser usado?

- Atualizar modelos pela API
- Obter informações sobre um modelo específico

## Identificador de tela

Um identificador de [tela]({{site.baseurl}}/user_guide/engagement_tools/canvas/) ou ID de tela é uma chave aleatória gerada pelo Braze para uma determinada tela dentro do dashboard. As IDs do Canvas são exclusivas para cada Canvas e podem ser usadas para fazer referência a Canvases por meio da API. 

Lembre-se de que, se você tiver um Canvas com variantes, haverá um ID geral do Canvas, bem como IDs de Canvas de variantes individuais aninhados sob o Canvas principal. 

### Onde posso encontrá-lo?

Você pode encontrar seu ID do canva no dashboard. Acesse **Envio de mensagens** > **Canvas** e selecione um Canvas pré-existente. Se o canva que você deseja ainda não existir, crie um e salve-o. Na parte inferior de uma página individual do Canvas, clique em **Analyze Variants (Analisar variantes**). Uma janela é exibida com o identificador da API do Canva localizado na parte inferior.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), **o Canva** está localizado em **Engajamento**.
{% endalert %}

### Para que ele pode ser usado?

- Rastreamento da análise de dados em uma mensagem específica
- Obtenha estatísticas agregadas de alto nível sobre a performance do Canva
- Obter detalhes sobre um Canva específico
- Com o Currents para trazer dados de nível de usuário para uma abordagem "mais ampla" do Canvas
- Com o envio de mensagens disparadas pela API para coletar estatísticas de mensagens transacionais

## Identificador de campanha

Um identificador [de campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) ou ID de campanha é uma chave aleatória gerada pelo Braze para uma determinada campanha dentro do dashboard. Os IDs de campanha são exclusivos para cada campanha e podem ser usados para fazer referência a campanhas por meio da API. 

Lembre-se de que, se você tiver uma campanha com variantes, haverá um ID de campanha geral e IDs de campanha variantes individuais aninhados sob a campanha principal. 

### Onde posso encontrá-lo?

Você pode encontrar seu ID de campanha de duas maneiras:

{% tabs local %}
{% tab Campanhas %}
Acesse **Envio de mensagens** > **Campanhas** e selecione uma campanha pré-existente. Se a campanha que você deseja ainda não existir, crie uma e salve-a. Na parte inferior da página da campanha individual, você poderá encontrar seu **Campaign API Identifier**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), **Campaigns** está em **Engagement (Engajamento**).
{% endalert %}
{% endtab %}

{% tab Chaves de API %}
Acesse **Configurações** > **APIs e identificadores**. Aqui, o Braze oferece uma pesquisa de **identificadores adicionais de API**, onde você pode procurar identificadores específicos.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), **as chaves de API** estão localizadas em **Console do desenvolvedor** > **Configurações de API**.
{% endalert %}
{% endtab %}
{% endtabs %}

### Para que ele pode ser usado?

- Rastreamento da análise de dados em uma mensagem específica
- Obtenha estatísticas agregadas de alto nível sobre a performance da campanha
- Obter detalhes sobre uma campanha específica
- Com o Currents para trazer dados de usuários para uma abordagem "mais ampla" das campanhas
- Com entrega disparada pela API para coletar estatísticas de mensagens transacionais
- Para [pesquisar uma campanha específica]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/#search-syntax) na página **Campaigns** usando o filtro `api_id:YOUR_API_ID`

## Identificador de segmento

Um identificador de [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/) ou ID de segmento é uma chave aleatória gerada pelo Braze para um determinado segmento dentro do dashboard. As IDs de segmento são exclusivas para cada segmento e podem ser usadas para fazer referência a segmentos por meio da API. 

### Onde posso encontrá-lo?

Você pode encontrar sua ID de segmento de duas maneiras:

{% tabs local %}
{% tab Segmentos %}
Acesse **Público** > **Segmentos** e selecione um segmento pré-existente. Se o segmento que você deseja ainda não existir, crie um e salve-o. Na parte inferior da página de segmento individual, você poderá encontrar seu identificador de segmento.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), **Segments** está em **Engagement (Engajamento**).
{% endalert %}
{% endtab %}

{% tab Chaves de API %}
Acesse **Configurações** > \*\*APIs**e identificadores**. Aqui, o Braze oferece uma pesquisa de **identificadores adicionais de API**, onde você pode procurar identificadores específicos.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), **as chaves de API** estão localizadas em **Console do desenvolvedor** > **Configurações de API**.
{% endalert %}
{% endtab %}
{% endtabs %}

### Para que ele pode ser usado?
- Obter detalhes sobre um segmento específico
- Recuperar análises de dados de um segmento específico
- Puxe quantas vezes um evento personalizado foi registrado para um segmento específico
- Especifique e envie uma campanha para os membros de um segmento a partir da API

## Identificador do cartão

Um identificador de cartão ou ID de cartão é uma chave aleatória gerada pelo Braze para um determinado cartão de feed de notícias dentro do dashboard. Os IDs de cartão são exclusivos para cada cartão [do Feed de notícias]({{site.baseurl}}/user_guide/engagement_tools/news_feed/) e podem ser usados para fazer referência a cartões por meio da API. 

{% alert note %}
O feed de notícias será descontinuado. A Braze recomenda que os clientes que usam nossa ferramenta de feed de notícias migrem para o canal de envio de mensagens Content Cards - é mais flexível, personalizável e confiável. Confira o [guia de migração]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) para saber mais.
{% endalert %}

### Onde posso encontrá-lo?

Você pode encontrar o ID do cartão de duas maneiras:

{% tabs local %}
{% tab Feed de notícias %}
Acesse **Envio de** **mensagens** > **Feed de notícias** e selecione um feed de notícias pré-existente. Se o Feed de notícias que você deseja ainda não existir, crie um e salve-o. Na parte inferior da página individual do Feed de notícias, você poderá encontrar o identificador exclusivo do seu cartão.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), **o Feed de notícias** está em **Engajamento**.
{% endalert %}
{% endtab %}

{% tab Chaves de API %}
Acesse **Configurações** > **APIs e identificadores**. Aqui, o Braze oferece uma pesquisa de **identificadores adicionais de API**, onde você pode procurar identificadores específicos.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), **as chaves de API** estão localizadas em **Console do desenvolvedor** > **Configurações de API**.
{% endalert %}
{% endtab %}
{% endtabs %}

### Para que ele pode ser usado?

- Recuperar informações relevantes em um cartão
- Rastreamento de eventos relacionados aos cartões de conteúdo e ao engajamento

## Enviar identificador

Um identificador de envio, ou ID de envio, é uma chave gerada pelo Braze ou criada por você para um determinado envio de mensagens sob a qual a análise de dados deve ser rastreada. O identificador de envio permite que você obtenha análises de dados para uma instância específica de uma campanha enviada por meio do [endpoint`/sends/data_series` ]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/).

### Onde posso encontrá-lo?

As campanhas disparadas por API e API que são enviadas como um broadcast gerarão automaticamente um identificador de envio se um identificador de envio não for fornecido. Se você quiser especificar seu próprio identificador de envio, primeiro terá de criar um por meio do [endpoint`/sends/id/create` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/). O identificador precisa conter todos os caracteres ASCII e ter no máximo 64 caracteres. Você pode reutilizar um identificador de envio em vários envios da mesma campanha se quiser agrupar a análise desses envios.

### Para que ele pode ser usado?
Envie e rastreie a performance das mensagens de forma programática, sem a criação de campanhas para cada envio.

## Identificador do grupo de inscrições

Um identificador de grupo de inscrições, ou ID de grupo de inscrições, é uma chave gerada pelo Braze para um determinado grupo de inscrições. Os IDs são exclusivos para cada grupo de inscrições e podem ser usados para fazer referência a grupos de inscrições por meio da API.

### Onde posso encontrá-lo?

Acesse **Público** > **Inscrições** e copie a ID ao lado do respectivo grupo de inscrições.

### Para que ele pode ser usado?

- Listar os grupos de inscrições de um usuário
- Obter o status do grupo de inscrições de um usuário
- Atualizar o status do grupo de inscrições de um usuário
