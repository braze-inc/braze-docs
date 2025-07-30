---
nav_title: Localização
article_title: Localização
page_order: 7
description: "Este artigo de referência aborda os conceitos básicos de localização, lista os benefícios de diferentes abordagens de orquestração em campanhas e Canvas e lista as diferentes maneiras pelas quais os usuários podem lidar com a personalização em seus envios de mensagens."
tool:
    - Campaigns
    - Canvas
---

# Localização

> Para empresas com clientes em muitos países, lidar com a localização no início da sua jornada com a Braze pode economizar tempo e recursos para suas empresas.

## Como funciona?

Após a [integração do SDK do Braze]({{site.baseurl}}/developer_guide/sdk_integration/), as informações de localização dos dispositivos dos usuários são coletadas automaticamente. O local contém o idioma e um identificador de região. Esta informação está disponível na ferramenta de segmentação da Braze em **País** e **Idioma**.

{% alert tip %}
Para obter detalhes técnicos sobre como a localização é recebida, consulte a documentação oficial [do iOS](https://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html) e [do Android](http://developer.android.com/reference/java/util/Locale.html).
{% endalert %}

## Gerenciamento de traduções

Considere as seguintes abordagens para gerenciar suas traduções.

{% tabs local %}
{% tab campanha %}
### Um modelo para todos

Nessa abordagem, a localização é aplicada a um único modelo no Braze usando o [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid). Após o envio, o dashboard fornece análise de dados agregada da campanha. O engajamento no nível do usuário pode ser medido usando funis de segmento personalizados, por exemplo, combinando os filtros **País** e **Campanha Recebida**.

| Vantagens | Considerações |
| --- | --- |
| Abordagem centralizada<br>\- Tempo de construção de e-mail reduzido, sem necessidade de construir um e-mail várias vezes | Construção de relatórios manual<br>O relatório da campanha mostra métricas agregadas em vez de métricas por país<br>Precisa testar completamente o Liquid para garantir que ele preencha conforme o esperado<br>Dependendo de como você obtém o valor do país ou de quantos condados você configurou, pode ser complicado testar cada país<br>Mais difícil agendar envios para horários específicos em diferentes fusos horários<br>Mais difícil de usar se você quiser enviar conteúdo separado por país. |
| \--- | \--- | \--- |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Um modelo por país 

Essa abordagem separa os modelos em diferentes localidades de envio. Após o envio, o dashboard relata a análise de dados com base em cada país separadamente, e quaisquer eventos de nível de usuário [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) downstream também estarão vinculados a uma campanha específica.

- Os modelos se beneficiam da implementação de [tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags#tags) para fins de manutenção e rastreamento.
- As campanhas podem herdar as configurações do mesmo [Braze modelo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media#about-templates-and-media) e [Blocos de Conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) (como [modelos de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template) que contêm Liquid).
- Campanhas e modelos pré-existentes podem ser [duplicados]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating/) para permitir um tempo mais rápido para obter valor.

| Vantagens | Considerações |
| --- | --- |
| Escalável para vários locais<br>Relatórios sobre receita por país dentro da Braze (como por campanha)<br>Flexibilidade se houver conteúdo drasticamente diferente por país | \- Requer estruturação estratégica<br>Mais esforço de construção necessário (como campanhas separadas para cada país) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab canvas %}
### Uma viagem para todos

Nessa abordagem, a localização é tratada no [Canva Journeys]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/the_basics/#building-the-customer-journey) e no Liquid para definir o envio de mensagens para cada usuário. 

Depois que um canva é enviado, o dashboard fornece [análise de dados do canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) agregada, enquanto o engajamento ao nível do usuário pode ser medido através de [funis de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/) personalizados, como a combinação de [**país**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#country) e filtros de [**etapa do canva recebida**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#received-canvas-step).

| Vantagens | Considerações |
| --- | --- |
| Abordagem centralizada<br>\- Tempo de construção de e-mail reduzido - não há necessidade de construir um e-mail várias vezes. | Construção de relatórios manual<br>\- O relatório de canva mostra métricas agregadas em vez de métricas por país<br>Precisa testar completamente o Liquid para garantir que ele preencha conforme o esperado<br>Dependendo de como você obtém o valor do país ou de quantos condados você configurou, pode ser complicado testar cada país<br>Mais difícil agendar envios para horários específicos em diferentes fusos horários<br>Mais difícil de usar se você quiser enviar conteúdo separado por país. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Uma viagem por país

Nessa abordagem, o construtor de jornadas [do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) oferece a flexibilidade de criar jornadas de usuário por meio de vários [componentes do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/). Esses componentes podem ser [duplicados]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating) no nível do componente e da jornada geral.

A localização pode ser obtida com os seguintes métodos:

- Separe canvas por país, isso garante que as jornadas complexas do usuário sejam definidas no topo do funil usando filtros de público
- Jornadas de usuário sob medida por país, a implementação de [caminhos do público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) para segmentar intuitivamente os usuários em grande escala para cada jornada, criando threads de mensagens separadas para cada país em um único canva

Uma vez enviado, o dashboard fornece análise de dados dinâmica por país e dentro de eventos [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) no nível do usuário com base na localização atual do cliente.

| Vantagens | Considerações |
| --- | --- |
| \- Relatórios sobre receita por país dentro da Braze (como por canva, variante ou etapa)<br>Flexibilidade se houver conteúdo drasticamente diferente por país<br>Pode adicionar outros canais como parte da jornada no futuro | \- Requer estruturação estratégica<br>Mais esforço de construção necessário (como etapas de mensagem separadas para cada país)<br>\- O canva pode se tornar grande e difícil de ler se você tiver jornadas personalizadas e complexas para cada país em um único canva. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Envio de mensagens traduzidas

Para enviar mensagens personalizadas com base no idioma ou na localização de um usuário, use um dos seguintes métodos:

{% tabs local %}
{% tab Manualmente %}
Você pode colar manualmente seu conteúdo no corpo da mensagem e usar [o Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) para exibir [condicionalmente]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) o idioma correto para o destinatário. Para isso:

1. Crie sua mensagem e selecione **Idioma** para gerar a lógica condicional Liquid para cada um dos idiomas selecionados.
2. Você pode usar o modelo Liquid a seguir para ajudar a construir sua mensagem. Para cada campo com modelo, você deve inserir as variações após o segmento entre colchetes do modelo. A variação deve corresponder ao código de idioma referenciado entre colchetes antes dele.
    {% raw %}
    ```liquid
    {% if ${language} == 'en' %}
    This is a message in English from Braze!
    {% elsif ${language} == 'es' %}
    Este es un mensaje en español de Braze !
    {% elsif ${language} == 'zh' %}
    这是一条来自Braze的中文消息。
    {% else %}
    This is a message from Braze! This will go to anyone who does not match the other specified languages!
    {% endif %}
    ```
    {% endraw %}
3. Teste sua mensagem antes de enviá-la inserindo o ID de um usuário ou e-mail para verificar como uma mensagem apareceria para um indivíduo dependendo de seu idioma. 

{% alert tip %}
Sempre recomendamos incluir uma {% raw %}`{% else %}`{% endraw %} declaração no seu envio de mensagens. Embora a maioria dos usuários veja o envio de mensagens em seu idioma específico, o texto será visível para aqueles que:
- Não tem um idioma selecionado
- Tenha um idioma que a Braze não suporte
- Tenha um dispositivo onde o idioma é indetectável
{% endalert %}
{% endtab %}

{% tab Blocos de Conteúdo %}
Braze [Blocos de Conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks) são blocos de conteúdo reutilizáveis. Quando um bloco é alterado, todas as referências a esse bloco são alteradas. Por exemplo, atualizações em um cabeçalho ou rodapé de e-mail serão refletidas em todos os e-mails ou para abrigar traduções. Esses blocos também podem ser [criados]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/#create-content-block) e [atualizados]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) usando a API REST, e os usuários podem fazer upload de traduções programaticamente. 

Ao criar uma campanha no dashboard, os Blocos de Conteúdo podem ser referenciados usando a tag {% raw %}`{{content_blocks.${name_of_content_block}}}`{% endraw %}. Esses blocos podem conter todas as traduções dentro da lógica condicional para cada idioma, como mostrado na opção 1, ou um bloco separado para cada idioma pode ser usado.

Os blocos de conteúdo também podem ser utilizados como um processo de gerenciamento de tradução, onde o conteúdo que requer tradução é armazenado dentro de um bloco de conteúdo, buscado, traduzido e, em seguida, atualizado:
1. Crie manualmente um bloco de conteúdo no dashboard com a tag "Necessita tradução".
2. Seu serviço realiza uma busca noturna de todos os Blocos de Conteúdo usando o [`/content_blocks/list` endpoint]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/).
3. Seu serviço busca detalhes em cada bloco de conteúdo através do [`/content_blocks/info` endpoint]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) para ver quais blocos estão marcados para tradução.
4. Seu serviço de tradução traduz o corpo de todos os Blocos de Conteúdo "Necessita tradução".
5. Seu serviço atinge o [`/content_block/update` endpoint]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) para atualizar o conteúdo traduzido e atualizar a tag para "Tradução Completa".
{% endtab %}

{% tab Catálogos %}
[Catálogos]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/) permitem acessar dados de objetos JSON importados via API e arquivos CSV para enriquecer suas mensagens, semelhante a atributos personalizados ou propriedades de eventos personalizados através do Liquid. Por exemplo:

{% subtabs local %}
{% subtab API %}

Crie um catálogo através da seguinte chamada de API:
```json
curl --location --request POST 'https://your_api_endpoint/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "catalogs": [
   {
     "name": "translations",
     "description": "My localization samples",
     "fields": [
       {
         "name": "id",
         "type": "string"
       },
       {
         "name": "context",
         "type": "string"
       },
       {
         "name": "language",
         "type": "string"
       },
       {
         "name": "body",
         "type": "string"
       }
     ]
   }
 ]
}'
```

Adicione itens através da seguinte chamada de API:

```json
curl --location --request POST 'https://your_api_endpoint/catalogs/translations/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "items": [
   {
     "id": "1",
     "context": "1",
     "language": "en",
     "body": "Hey"
   },
   {
     "id": "2",
     "context": "1",
     "language": "es",
     "body": "Hola"
   },
   {
     "id": "3",
     "context": "1",
     "language": "pt",
     "body": "Oi"
   },
   {
     "id": "4",
     "context": "1",
     "language": "de",
     "body": "Hallo"
   }
 ]
}'
```
{% endsubtab%}
{% subtab CSV %}
Crie um CSV no seguinte formato:

| id | contexto | language | corpo |
| --- | --- | --- |
| 1 | 1 | en | Olá |
| 2 | 1 | es | Olá |
| 3 | 1 | pt | Oi |
| 4 | 1 | de | Olá |
| 5 | 2 | en | Olá |
| 6 | 2 | es | Olá |
| 7 | 2 | pt | Oi |
| 8 | 2 | de | Olá |
| 9 | 3 | en | Olá |
| 10 | 3 | es | Olá |
| 11 | 3 | pt | Oi |
| 12 | 3 | de | Olá |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}
{% endsubtab %}
{% endsubtabs %}

Esses itens de catálogo podem ser referenciados usando [personalização]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#using-catalogs-in-a-message), mostrado abaixo, ou [seleções]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections) que permitem criar grupos de dados. 

{% raw %}
```liquid
{% catalog_items translations 1 %}
{{items[0].body}} 
//returns “Hey”
```
{% endraw %}
{% endtab %}

{% tab Envio de mensagens de localização %}
Adicione e use localidades em sua mensagem para direcionar usuários em diferentes idiomas em uma única campanha ou Canvas para os canais de envio de mensagens ou e-mail. Para obter um passo a passo completo, consulte [Localidades em mensagens de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/) ou [Localidades em mensagens push]({{site.baseurl}}/user_guide/message_building_by_channel/push/using_locales/).

{% alert important %}
Este recurso está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}
{% endtab %}

{% tab Parceiros do Braze %}
Muitos parceiros da Braze oferecem soluções de localização, incluindo [Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex/#about-transifex) e [Crowdin](https://crowdin.com/). Normalmente, os usuários usam a plataforma junto com uma equipe interna e uma agência de tradução. Essas traduções são então carregadas lá e são então acessíveis via API REST. Esses serviços também costumam aproveitar [Conteúdo Conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), permitindo que os usuários obtenham as traduções via API.

Por exemplo, as seguintes chamadas de Conteúdo Conectado chamam Transifex e Crowdin para buscar uma tradução, aproveitando {% raw %}`{{${language}}}`{% endraw %} para identificar a tradução correta para um determinado usuário. Esta tradução é então salva no bloco JSON "strings" e referenciada.

{% subtabs local %}
{% subtab Transifex example %}
{% raw %}
```liquid
{% connected_content https://www.transifex.com/api/2/project/example/resource/example/translation/{{${language}}}/strings :basic_auth semc :save strings %}
{{strings[0].translation}}
```
{% endraw %}
{% endsubtab %}
{% subtab Crowdin example %}
{% raw %}
```liquid
{% connected_content https://api.crowdin.com/api/project/braze-test/export-file?key=you_api_key&language={{${language}}}&file=test.json&export_translated_only=1 :save response %}
{{response.value_1}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Planilhas eletrônicas %}
Hospede as traduções em uma planilha e, em seguida, use um dos seguintes métodos para enviar sua mensagem no idioma relevante.

{% subtabs local %}
{% subtab Connected Content %}
Você pode pedir a uma agência de tradução que armazene as traduções em uma planilha do Google e, em seguida, consultar esse conteúdo usando o [Braze Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content). Ao enviar uma mensagem, a tradução relevante para cada usuário será inserida no corpo da campanha com base no idioma selecionado. 

{% alert note %}
A API do Google Sheets tem um limite de 500 solicitações por 100 segundos por projeto. As chamadas de Conteúdo Conectado podem ser armazenadas em cache, mas essa solução não é escalável para uma campanha de alto tráfego.
{% endalert %}
{% endsubtab %}

{% subtab JSON API via SheetDB %}
Esta opção fornece um método alternativo de transformar Google Sheets em objetos JSON consultados via Connected Content. Ao transformar uma planilha em uma API JSON via SheetDB, você pode escolher entre [vários níveis de inscrição](https://sheetdb.io/pricing) dependendo da cadência das chamadas da API.

A estrutura da planilha segue as etapas da opção 4, mas o SheetDB também fornece [filtros adicionais](https://docs.sheetdb.io/#sheetdb-api) para consulta dos objetos.

Alguns usuários podem preferir implementar o SheetDB com menos dependências de Liquid e Connected Block, implementando o [método de busca](https://docs.sheetdb.io/#get-search-in-document) do SheetDB em chamadas de solicitação GET para filtrar os objetos JSON com base no {% raw %}`{{${language}}}`{% endraw %} Liquid tag para retornar automaticamente os resultados para um único idioma, em vez de construir grandes blocos condicionais.

#### Etapa 1: Formate a planilha do Google

Primeiro, construa a planilha do Google para que os idiomas sejam objetos diferentes:

| linguagem | título1 | corpo1 | título2 | corpo2 |
Ei | 1 | Ei2 | 5 |
| es | Olá | 2 | Olá2 | 6 |
| pt | Oi | 3 | Oi2 | 7 |
| de | Olá | 4 | Hallo2 | 8 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

#### Etapa 2: Use a linguagem Liquid tag em uma chamada de Conteúdo Conectado

Em seguida, implemente a {% raw %}`{{${language}}}`{% endraw %} Liquid tag dentro de uma chamada de Conteúdo Conectado. Observe que o SheetDB gerará automaticamente o `sheet_id` ao criar a planilha.

{% raw %}
```liquid
{% connected_content https://sheetdb.io/api/v1/[sheet_id]/search?language={{${language}}} :save result%}
```
{% endraw %}

#### Etapa 3: Modele suas mensagens

Por fim, use Liquid para modelar suas mensagens:

{% raw %}
```liquid
{{result[0].title1}} //returns “Hey”
{{result[0].title2}} //returns “Hey2”
```
{% endraw %}

##### Considerações

- O campo {% raw %}`{{${language}}}`{% endraw %} deve ser definido para todos os usuários; caso contrário, um bloco condicional Liquid deve ser apresentado como um manipulador de fallback para usuários sem um idioma.
- A modelagem de dados no Google Sheets deve seguir uma vertical orientada por linguagem diferente, em vez de ter objetos de mensagem.
- SheetDB oferece uma conta gratuita limitada e várias opções pagas que devem ser consideradas com base na sua estratégia de campanha. 
- Chamadas de Conteúdo Conectado podem ser armazenadas em cache. Recomendamos medir a cadência projetada das chamadas da API e investigar uma abordagem alternativa de chamar o endpoint principal do SheetDB em vez de usar o método de busca.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
