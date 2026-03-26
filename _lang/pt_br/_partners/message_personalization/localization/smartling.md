---
nav_title: Smartling
article_title: Smartling
description: "Este artigo de referência descreve a parceria entre a Braze e o Smartling, um software baseado em nuvem para localização. O Braze Connector oferece suporte à tradução de modelos de e-mail HTML, blocos de conteúdo, canvas e mensagens de e-mail de campanhas."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> O [Smartling](https://www.smartling.com/) é um software de gerenciamento de tradução em nuvem de ponta a ponta para clientes que buscam automatizar a tradução de sites, aplicativos e experiências do cliente.

_Essa integração é mantida pela Smartling._

## Sobre a integração

O Braze Connector oferece suporte a traduções para mensagens em campanhas e Canvas (e-mail, push, mensagens no app e banners), modelos de e-mail e blocos de conteúdo. Consulte a tabela a seguir para saber quais tipos de editor são compatíveis com cada canal ou recurso.

| Canal/Recurso | Editor tradicional (ex. HTML) | Editor de arrastar e soltar |
| --------------- | ----------------------------- | -------------------- |
| [E-mail]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email) | ✅ | ✅ |
| [Mensagens no app]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message) | ✅ | ✅ |
| [Push]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push) | ✅ | n/a |
| Modelo de e-mail | ✅ | ✅ |
| Banners | n/a | ✅ |
| Blocos de conteúdo |  ✅* |  ✅* |

*Consulte [Gerenciar traduções para blocos de conteúdo](#managing-translations-for-content-blocks) para mais informações.

### Fluxo de trabalho legado

Dependendo do seu caso de uso, gerencie traduções para blocos de conteúdo usando o fluxo de trabalho de tradução legado ou o fluxo de trabalho atualizado. 

No fluxo de trabalho atualizado, usando o suporte multilíngue da Braze e as localizações nas mensagens, as tags de tradução são adicionadas ao bloco de conteúdo. No entanto, o Smartling executa traduções no nível da mensagem. O conteúdo é traduzido somente quando é incluído em uma campanha ou canva e a localização de destino é definida. Para saber mais, consulte [Gerenciamento de traduções para blocos de conteúdo](#managing-translations-for-content-blocks).

Para saber mais sobre o fluxo de trabalho legado, consulte [Gerenciamento de traduções usando o fluxo de trabalho legado](#managing-translations-using-the-legacy-workflow).

## Pré-requisitos

| Requisito                   | Descrição                                                                                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Conta do Smartling             | É necessário ter uma [conta Smartling](https://dashboard.smartling.com/) para aproveitar essa parceria.                                                          |
| Projeto de tradução Smartling | Para conectar sua conta da Braze ao Smartling, primeiro você deve fazer login e [criar um projeto de tradução](https://help.smartling.com/hc/en-us/articles/115003074093). |
| Chave da API REST da Braze            | Uma chave da API REST da Braze com as seguintes permissões: <br>- campaigns.translations.get<br>- campaigns.translations.update<br>- campaigns.list<br>- campaigns.details<br>- canvas.translations.get<br>- canvas.translations.update<br>- campaigns.details<br>- templates.email.create<br>- templates.email.update<br>- templates.email.list<br>- templates.email.info<br>- templates.translations.get<br>- templates.translations.update<br>- content_blocks.info<br>- content_blocks.list<br>- content_blocks.create<br>- content_blocks.update<br><br> Isso pode ser criado no dashboard da Braze em **Configurações > Chaves de API**. |
| Endpoint REST da Braze           | [Sua URL de endpoint REST.]({{site.baseurl}}/api/basics/#endpoints) Seu endpoint depende da URL da Braze para sua instância.             |
| Configurações multilíngues da Braze | [Conclua as configurações multilíngues na Braze]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Definir as configurações multilíngues na Braze

Consulte [as instruções de configuração multilíngue da Braze]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) para configurar as localizações na Braze.

### Etapa 2: Configurar o projeto Braze no Smartling TMS

Consulte a [documentação do Smartling](https://help.smartling.com/hc/en-us/articles/13248549217435) para obter detalhes sobre a configuração do conector.

### Como conectar a Braze ao Smartling

1. Em sua [conta Smartling](https://dashboard.smartling.com/), crie um tipo de projeto [Braze Connector](https://help.smartling.com/hc/en-us/articles/115003074093).

![Conexão da Braze no Smartling.]({% image_buster /assets/img/smartling/image1_Connecting_Braze_to_Smartling.png %})

{: start="2"}
2. Nesse projeto, selecione **Configurações** > **Configurações da Braze** > **Conectar à Braze**.
3. Preencha os campos obrigatórios, como URL da API e chave de API. Se a conexão de teste for bem-sucedida, salve a conexão. Se o teste não for bem-sucedido, confirme se você inseriu a URL da API e a chave de API corretas.

![Conexão da Braze nas configurações de API do Smartling.]({% image_buster /assets/img/smartling/image2_API.png %})

{: start="4"}
4. Adicione outros idiomas ao projeto.

![Conexão da Braze em idiomas de projeto do Smartling.]({% image_buster /assets/img/smartling/image3_project_languages.png %})

{: start="5"}
5. Em Braze Settings, verifique se os valores na coluna **Target Language (Braze)** correspondem às localizações configuradas nas configurações multilíngues da Braze. A convenção de nomenclatura da localização deve corresponder exatamente.

![Conexão da Braze na confirmação de idiomas do Smartling.]({% image_buster /assets/img/smartling/image4_language_confirmation.png %})

### Etapa 3: Adicionar tags de tradução à sua mensagem da Braze

Consulte [as instruções da Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/?tab%3Dhtml%2520editor#prerequisites) sobre como adicionar tags de tradução às suas mensagens:

- [E-mail]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email)
- [Push]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push)
- [Mensagens no app]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message)

Aqui está um exemplo de uma campanha de e-mail em HTML com tags de tradução.

![E-mail da Braze com tags de tradução.]({% image_buster /assets/img/smartling/image5_translation_tags.png %})

Você deve salvar a mensagem como rascunho antes de selecionar as localizações.

### Etapa 4: Gerenciar traduções no Smartling

Depois de conectar e configurar o conector da Braze, encontre o conteúdo da Braze na guia Braze em seu projeto Smartling. Para saber mais, consulte a [documentação do Smartling](https://help.smartling.com/hc/en-us/articles/13248577069979).

O Smartling oferece recursos avançados para pesquisar e selecionar conteúdo por:
- Pesquisa por palavra-chave
- Tipo de conteúdo da Braze
- Tags da Braze

1. Neste exemplo, a campanha de e-mail de promoção de Ano Novo foi criada na [etapa 3](#step-3-add-translation-tags-to-your-braze-message).

![E-mail da Braze com tags de tradução.]({% image_buster /assets/img/smartling/image6_ny_promotion.png %})

{: start="2"}
2. Depois de localizar a campanha que deseja traduzir, selecione a pasta, escolha as variantes e selecione **Solicitar tradução**.

![Solicitar traduções.]({% image_buster /assets/img/smartling/image7_request_translation.png %})

{: start="3"}
3. Crie um novo trabalho para a tradução.

![Crie um novo trabalho para a tradução.]({% image_buster /assets/img/smartling/image8_request_translation.png %})

{: start="4"}
4. Depois que o trabalho for autorizado, edite cada tradução na ferramenta CAT.

![Ferramenta CAT de tradução.]({% image_buster /assets/img/smartling/image9_translation_job.png %})

{: start="5"}
5. Depois que as traduções forem concluídas, salve e envie sua tradução para a Braze.

![Enviar a tradução para a Braze.]({% image_buster /assets/img/smartling/image10_translations.png %})

### Etapa 5: Visualizar a mensagem como um usuário multilíngue na Braze

Na Braze, faça uma prévia da sua campanha como um usuário multilíngue para confirmar que as traduções foram aplicadas corretamente.

![Prévia do usuário multilíngue.]({% image_buster /assets/img/smartling/image11_preview.png %})

## Gerenciamento de traduções para blocos de conteúdo

Os blocos de conteúdo são gerenciados na seção **Modelos e Mídias** na Braze.

### Tradução armazenada como parte do componente da mensagem

As tags de tradução pertencem ao bloco de conteúdo. No entanto, o Smartling executa traduções no nível da mensagem; o conteúdo é traduzido somente quando é incluído em uma campanha ou canva e a localização de destino é definida.

### Considerações

- As tags de tradução devem ser adicionadas manualmente ao bloco de conteúdo tanto no editor HTML quanto no editor de arrastar e soltar do bloco de conteúdo.
- As localizações são selecionadas no nível da mensagem, não nos blocos de conteúdo em si.
- Para Canvas, recomendamos o uso de linhas para inserir blocos de conteúdo em sua mensagem em vez de adicioná-los manualmente com uma Liquid tag. Arrastar um bloco de conteúdo da prévia para um e-mail cria uma cópia local; quaisquer alterações no bloco de conteúdo "pai" não se propagam para outras campanhas que usam esse bloco.
- Se você usar uma Liquid tag de bloco de conteúdo, certifique-se de incluir pelo menos uma tag de tradução diretamente no corpo do e-mail. A adição manual da tag de tradução permite que você selecione as localizações no menu suspenso multilíngue. O Smartling captura as tags de tradução do bloco de conteúdo. É possível adicionar uma tag `comment` para que o texto não fique visível para o usuário.

## Gerenciamento de traduções usando o fluxo de trabalho legado

Se preferir gerenciar as traduções diretamente em um bloco de conteúdo, consulte as instruções legadas na [documentação do Smartling](https://help.smartling.com/hc/en-us/articles/13248577069979-Translating-with-the-Braze-Connector). Esse método usa um atributo de idioma e a lógica if/else do Liquid para exibir texto em diferentes idiomas.

## Perguntas frequentes

### Há suporte para tags de tradução no editor de arrastar e soltar?

Para o editor de arrastar e soltar (e-mail, bloco de conteúdo, mensagem no app), você deve adicionar manualmente as tags de tradução como Liquid tags.

### Como traduzir o texto dentro de uma Liquid tag?

O Smartling reconhece as Liquid tags e as torna variáveis não editáveis no criador. Qualquer outro texto dentro da Liquid tag, como texto padrão ou filtros como join, também se torna não editável no Smartling. No entanto, remova a Liquid tag no Smartling e recrie a Liquid tag com o texto padrão traduzido. Um aviso é exibido ao salvar a tradução.