---
nav_title: Localização
article_title: Localização
page_order: 7
description: "Este artigo de referência aborda os conceitos básicos de localização, lista os benefícios de diferentes abordagens de orquestração em campanhas e Canvases e lista diferentes maneiras pelas quais os usuários podem lidar com a personalização em suas mensagens."
tool:
    - Campaigns
    - Canvas
---

# Localização

> Para empresas com clientes em muitos países, lidar com a localização no início de sua jornada no Braze pode economizar tempo e recursos.

## Como funciona

Depois de [integrar o SDK do Braze]({{site.baseurl}}/developer_guide/sdk_integration/), as informações de localidade dos dispositivos do usuário são coletadas automaticamente. O locale contém o idioma e um identificador de região. Essas informações estão disponíveis na ferramenta de segmentação do Braze em **País** e **Idioma**.

{% alert tip %}
Para obter detalhes técnicos sobre como a localidade é recebida, consulte a documentação oficial [do iOS](https://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html) e [do Android](http://developer.android.com/reference/java/util/Locale.html).
{% endalert %}

## Gerenciamento de traduções

Considere as seguintes abordagens para gerenciar suas traduções.

{% tabs local %}
{% tab campaign %}
### Um modelo para todos

Nessa abordagem, a localização é aplicada a um único modelo no Braze usando [o Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid). Após o envio, o painel fornece análises agregadas da campanha. O envolvimento no nível do usuário pode ser medido usando funis de segmentos personalizados, por exemplo, combinando filtros de **país** e **de campanha recebida**.

| Vantagens | Considerações |
| --- | --- |
| \- Abordagem centralizada<br>\- Redução do tempo de criação de e-mails, sem necessidade de criar um e-mail várias vezes | \- Criação manual de relatórios<br>\- O relatório da campanha mostra métricas agregadas em vez de métricas por país<br>\- É necessário testar exaustivamente o Liquid para garantir que ele seja preenchido conforme o esperado<br>\- Dependendo de como você extrai o valor do país ou de quantos países você configurou, pode ser complicado testar cada país<br>\- É mais difícil programar envios para horários específicos em diferentes fusos horários<br>\- Mais difícil de usar se você quiser enviar conteúdo separado por país. |
| \--- | \--- | \--- |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Um modelo por país 

Essa abordagem separa o modelo em diferentes locais de envio. Após o envio, o painel informa o envio de análises com base em cada país separadamente, e todos os eventos do [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) no nível do usuário posterior também serão vinculados a uma campanha específica.

- Os modelos se beneficiam da implementação de [tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags#tags) para fins de manutenção e rastreamento.
- As campanhas podem herdar as configurações do mesmo [modelo Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media#about-templates-and-media) e dos [blocos de conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) (como [os modelos de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template) que contêm Liquid).
- Campanhas e modelos pré-existentes podem ser [duplicados]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating/) para permitir um time-to-value mais rápido.

| Vantagens | Considerações |
| --- | --- |
| \- Escalável para vários locais<br>\- Relatórios sobre a receita por país no Braze (por exemplo, por campanha)<br>\- Flexibilidade se houver um conteúdo drasticamente diferente por país | \- Requer estruturação estratégica<br>\- Mais esforço de construção necessário (como campanhas separadas para cada país) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab canvas %}
### Uma viagem para todos

Nessa abordagem, a localização é tratada no [Canvas Journeys]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/the_basics/#building-the-customer-journey) e no Liquid para definir as mensagens para cada usuário. 

Depois que um Canvas é enviado, o painel fornece [o Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) agregado, enquanto o envolvimento no nível do usuário pode ser medido por meio de [funis de segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/) personalizados, como a combinação de [**País**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#country) e [**Etapa do Canvas recebido**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#received-canvas-step) filtros.

| Vantagens | Considerações |
| --- | --- |
| \- Abordagem centralizada<br>\- Redução do tempo de criação de e-mails - não há necessidade de criar um e-mail várias vezes. | \- Criação manual de relatórios<br>\- O relatório do Canvas mostra métricas agregadas em vez de métricas por país<br>\- É necessário testar exaustivamente o Liquid para garantir que ele seja preenchido conforme o esperado<br>\- Dependendo de como você extrai o valor do país ou de quantos países você configurou, pode ser complicado testar cada país<br>\- É mais difícil programar envios para horários específicos em diferentes fusos horários<br>\- Mais difícil de usar se você quiser enviar conteúdo separado por país. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Uma viagem por país

Nessa abordagem, o construtor de jornadas [do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) oferece a flexibilidade de criar jornadas de usuário por meio de vários [componentes do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/). Esses componentes podem ser [duplicados]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating) no nível do componente e da jornada geral.

A localização pode ser obtida com os seguintes métodos:

- Canvases separados por país, o que garante que as jornadas complexas do usuário sejam definidas no topo do funil usando filtros de público-alvo
- Jornadas de usuário personalizadas por país, a implementação de [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) para segmentar intuitivamente os usuários em grande escala para cada jornada, criando tópicos de mensagens separados para cada país em um único Canvas

Depois de enviado, o painel fornece análises dinâmicas por país e em eventos [do Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) no nível do usuário com base na localização atual do cliente.

| Vantagens | Considerações |
| --- | --- |
| \- Relatórios sobre a receita por país no Braze (como por tela, variante ou etapa)<br>\- Flexibilidade se houver um conteúdo drasticamente diferente por país<br>\- Pode adicionar outros canais como parte da jornada no futuro | \- Requer estruturação estratégica<br>\- Mais esforço de construção necessário (como etapas de mensagens separadas para cada país)<br>\- O Canvas pode ficar grande e difícil de ler se você tiver jornadas personalizadas e complexas para cada país em um único Canvas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Envio de mensagens traduzidas

Para enviar mensagens personalizadas com base no idioma ou na localidade de um usuário, use um dos métodos a seguir:

{% tabs local %}
{% tab Manually %}
Você pode colar manualmente o conteúdo no corpo da mensagem e usar [o Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) para exibir [condicionalmente]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) o idioma correto para o destinatário. Para fazer isso:

1. Escreva sua mensagem e selecione **Idioma** para gerar a lógica condicional Liquid para cada um dos idiomas selecionados.
2. Você pode usar o modelo Liquid a seguir para ajudar a elaborar sua mensagem. Para cada campo com modelo, você deve inserir as variações após o segmento entre colchetes do modelo. A variação deve corresponder ao código de idioma referenciado nos colchetes antes dela.
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
3. Teste sua mensagem antes de enviá-la inserindo o ID ou o e-mail de um usuário para verificar como uma mensagem apareceria para uma pessoa, dependendo do idioma dela. 

{% alert tip %}
Sempre recomendamos incluir uma declaração {% raw %}`{% else %}`{% endraw %} em suas mensagens. Embora a maioria dos usuários veja as mensagens em seu idioma específico, o texto ficará visível para aqueles que não têm acesso a ele:
- Não tem um idioma selecionado
- Ter um idioma que não seja compatível com o Braze
- Ter um dispositivo em que o idioma não seja detectável
{% endalert %}
{% endtab %}

{% tab Content Blocks %}
[Os blocos de conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks) Braze são blocos reutilizáveis de conteúdo. Quando um bloco é alterado, todas as referências a esse bloco são alteradas. Por exemplo, as atualizações em um cabeçalho ou rodapé de e-mail serão refletidas em todos os e-mails ou nas traduções internas. Esses blocos também podem ser [criados]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/#create-content-block) e [atualizados]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) usando a API REST, e os usuários podem fazer upload de traduções de forma programática. 

Ao criar uma campanha no painel, os blocos de conteúdo podem ser referenciados usando a tag {% raw %}`{{content_blocks.${name_of_content_block}}}`{% endraw %}. Esses blocos podem conter todas as traduções alojadas na lógica condicional para cada idioma, conforme mostrado na opção 1, ou pode ser usado um bloco separado para cada idioma.

Os blocos de conteúdo também podem ser utilizados como um processo de gerenciamento de tradução, em que o conteúdo que requer tradução é armazenado em um bloco de conteúdo, buscado, traduzido e depois atualizado:
1. Crie manualmente um bloco de conteúdo no painel com a tag "Needs Translation" (Precisa de tradução).
2. Seu serviço realiza uma busca noturna de todos os blocos de conteúdo usando o [ponto de extremidade`/content_blocks/list` ]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/).
3. Seu serviço obtém detalhes sobre cada Content Block por meio do [endpoint`/content_blocks/info` ]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) para ver quais blocos estão marcados para tradução.
4. Seu serviço de tradução traduz o corpo de todos os blocos de conteúdo "Precisa de tradução".
5. Seu serviço acessa o [endpoint`/content_block/update` ]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) para atualizar o conteúdo traduzido e atualizar a tag para "Translation Complete".
{% endtab %}

{% tab Catalogs %}
[Os catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/) permitem que você acesse dados de objetos JSON importados via API e arquivos CSV para enriquecer suas mensagens, de forma semelhante aos atributos personalizados ou às propriedades de eventos personalizados do Liquid. Por exemplo:

{% subtabs local %}
{% subtab API %}

Crie um catálogo por meio da seguinte chamada de API:
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

Adicione itens por meio da seguinte chamada de API:

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

| id | contexto | idioma | corpo |
| --- | --- | --- |
| 1 | 1 | en | Ei |
| 2 | 1 | es | Olá |
| 3 | 1 | pt | Oi |
| 4 | 1 | de | Olá |
| 5 | 2 | en | Ei |
| 6 | 2 | es | Olá |
| 7 | 2 | pt | Oi |
| 8 | 2 | de | Olá |
| 9 | 3 | en | Ei |
| 10 | 3 | es | Olá |
| 11 | 3 | pt | Oi |
| 12 | 3 | de | Olá |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}
{% endsubtab %}
{% endsubtabs %}

Esses itens de catálogo podem ser referenciados usando [a personalização]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#using-catalogs-in-a-message), mostrada abaixo, ou [seleções]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) que permitem criar grupos de dados. 

{% raw %}
```liquid
{% catalog_items translations 1 %}
{{items[0].body}} 
//returns “Hey”
```
{% endraw %}
{% endtab %}

{% tab Locale messages %}
Adicione e use localidades em sua mensagem para atingir usuários em diferentes idiomas em uma única campanha ou Canvas para os canais de e-mail ou push. Para obter um passo a passo completo, consulte [Locales in email messages (Locais em mensagens de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/) ) ou [Locales in push messages (Locais em mensagens push]({{site.baseurl}}/user_guide/message_building_by_channel/push/using_locales/)).

{% alert important %}
Esse recurso está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}
{% endtab %}

{% tab Braze partners %}
Muitos parceiros do Braze oferecem soluções de localização, incluindo [a Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex/#about-transifex) e [a Crowdin](https://crowdin.com/). Normalmente, os usuários usam a plataforma juntamente com uma equipe interna e uma agência de tradução. Essas traduções são carregadas lá e podem ser acessadas por meio da API REST. Esses serviços também costumam aproveitar o [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), permitindo que os usuários obtenham as traduções por meio da API.

Por exemplo, as seguintes chamadas do Connected Content chamam o Transifex e o Crowdin para buscar uma tradução, aproveitando o {% raw %}`{{${language}}}`{% endraw %} para identificar a tradução correta para um determinado usuário. Essa tradução é então salva no bloco JSON "strings" e referenciada.

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

{% tab Spreadsheets %}
Hospede as traduções em uma planilha e, em seguida, use um dos métodos a seguir para enviar sua mensagem no idioma relevante.

{% subtabs local %}
{% subtab Connected Content %}
Você pode pedir a uma agência de tradução que armazene as traduções em uma planilha do Google e, em seguida, consultar esse conteúdo usando o [Braze Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content). Quando você enviar uma mensagem, a tradução relevante para cada usuário será inserida no corpo da campanha com base no idioma selecionado. 

{% alert note %}
A API do Google Sheets tem um limite de 500 solicitações por 100 segundos por projeto. As chamadas do Connected Content podem ser armazenadas em cache, mas essa solução não é dimensionável para uma campanha de alto tráfego.
{% endalert %}
{% endsubtab %}

{% subtab JSON API via SheetDB %}
Essa opção oferece um método alternativo de transformar o Google Sheets em objetos JSON consultados via Connected Content. Ao transformar uma planilha em uma API JSON por meio do SheetDB, você pode escolher entre [vários níveis de assinatura](https://sheetdb.io/pricing), dependendo da cadência das chamadas à API.

A estrutura da planilha segue as etapas da opção 4, mas o SheetDB também fornece [filtros adicionais](https://docs.sheetdb.io/#sheetdb-api) para consultar os objetos.

Alguns usuários podem preferir implementar o SheetDB com menos dependências do Liquid e do Connected Block, implementando o [método de pesquisa](https://docs.sheetdb.io/#get-search-in-document) do SheetDB em chamadas de solicitação GET para filtrar os objetos JSON com base na tag {% raw %}`{{${language}}}`{% endraw %} Liquid para retornar automaticamente os resultados de um único idioma, em vez de criar grandes blocos condicionais.

#### Etapa 1: Formatar a planilha do Google

Primeiro, crie a planilha do Google de modo que os idiomas sejam objetos diferentes:

| idioma | título1 | corpo1 | título2 | corpo2 |
| en | Hey | 1 | Hey2 | 5 |
| es | Hola | 2 | Hola2 | 6 |
| pt | Oi | 3 | Oi2 | 7 |
| de | Hallo | 4 | Hallo2 | 8 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

#### Etapa 2: Use a tag language Liquid em uma chamada de Connected Content

Em seguida, implemente a tag {% raw %}`{{${language}}}`{% endraw %} Liquid em uma chamada Connected Content. Observe que o SheetDB gerará automaticamente o endereço `sheet_id` ao criar a planilha.

{% raw %}
```liquid
{% connected_content https://sheetdb.io/api/v1/[sheet_id]/search?language={{${language}}} :save result%}
```
{% endraw %}

#### Etapa 3: Modelo de suas mensagens

Por fim, use o Liquid para criar modelos para suas mensagens:

{% raw %}
```liquid
{{result[0].title1}} //returns “Hey”
{{result[0].title2}} //returns “Hey2”
```
{% endraw %}

##### Considerações

- O campo {% raw %}`{{${language}}}`{% endraw %} deve ser definido para todos os usuários; caso contrário, um bloco condicional Liquid deve ser apresentado como um manipulador de fallback para usuários sem um idioma.
- A modelagem de dados no Planilhas Google precisa seguir uma vertical diferente, orientada pela linguagem, em vez de ter objetos de mensagem.
- O SheetDB oferece uma conta gratuita limitada e várias opções de pagamento que devem ser consideradas com base em sua estratégia de campanha. 
- As chamadas do Connected Content podem ser armazenadas em cache. Recomendamos medir a cadência projetada das chamadas de API e investigar uma abordagem alternativa de chamar o endpoint principal do SheetDB em vez de usar o método de pesquisa.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
