---
nav_title: Smartling
article_title: Smartling
description: "Este artigo de referência descreve a parceria entre a Braze e o Smartling, um software baseado em nuvem para localização. O Braze Connector oferece suporte à tradução de modelos de e-mail HTML, blocos de conteúdo, canvas e mensagens de campanha de e-mail."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> o [Smartling](https://www.smartling.com/) é um software de gerenciamento de tradução em nuvem de ponta a ponta para clientes que buscam automatizar a tradução de sites, aplicativos e experiências do cliente.

_Essa integração é mantida pela Smartling._

## Sobre a integração

O Braze Connector oferece suporte a traduções para mensagens em campanhas e Canvas (mensagens de e-mail, push e mensagens no app), modelos de e-mail e blocos de conteúdo. Consulte a tabela a seguir para saber mais sobre os canais e recursos suportados ao determinar o uso do novo conector com suporte a vários idiomas ou fluxo de trabalho legado.

| Canal/Função | Editor tradicional (ex. HTML) | Editor de arrastar e soltar |
| --------------- | ----------------------------- | -------------------- |
| [E-mail]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email) | ✅ | ✅ |
| [Mensagens no app]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message) | ✅ | ✅ |
| [Push]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push) | ✅ | n/a |
| Modelo de e-mail | Fluxo de trabalho legado | Fluxo de trabalho legado|
| Blocos de conteúdo |  ✅* |  ✅* |

\*Consulte [Gerenciar traduções para blocos de conteúdo](#managing-translations-for-content-blocks) para obter mais informações.

### Fluxo de trabalho legado

Dependendo de seu caso de uso, gerencie traduções para blocos de conteúdo usando o fluxo de trabalho de tradução legado ou o fluxo de trabalho atualizado. 

No fluxo de trabalho atualizado, usando o suporte multilíngue da Braze e as localizações nas mensagens, as tags de tradução são adicionadas ao bloco de conteúdo. No entanto, o Smartling executa traduções no nível da mensagem. O conteúdo é traduzido somente quando o conteúdo é incluído em uma campanha ou canva e o direcionamento é definido. Para saber mais, consulte [Gerenciamento de traduções para blocos de conteúdo](#managing-translations-for-content-blocks).

Para modelos de e-mail, somente o fluxo de trabalho legado é suportado. Para saber mais, consulte [Gerenciamento de traduções usando o fluxo de trabalho herdado](#managing-translations-using-the-legacy-workflow).

## Pré-requisitos

| Requisito                   | Descrição                                                                                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Conta do Smartling             | É necessário ter uma [conta Smartling](https://dashboard.smartling.com/) para aproveitar essa parceria.                                                          |
| Projeto de tradução Smartling | Para conectar sua conta da Braze com o Smartling, primeiro você deve se inscrever [criar um projeto de tradução](https://help.smartling.com/hc/en-us/articles/115003074093). |
| Chave da API REST do Braze            | Uma chave da API REST do Braze com as seguintes permissões: <br>- campaigns.translations.get<br>- campaigns.translations.update<br>- campaigns.list<br>- campaigns.details<br>- canvas.translations.get<br>- canvas.translations.update<br>- campaigns.details<br>- templates.email.create<br>- templates.email.update<br>- templates.email.list<br>- templates.email.info<br>- templates.translations.get<br>- templates.translations.update<br>- content_blocks.info<br>- content_blocks.list<br>- content_blocks.create<br>- content_blocks.update<br><br> Isso pode ser criado no dashboard do Braze em **Configurações > Chaves de API**. |
| Endpoint REST  do Braze           | [Sua URL de endpoint REST.]({{site.baseurl}}/api/basics/#endpoints) Seu endpoint depende do URL do Braze para sua instância.             |
| Configurações multilíngues do Braze | [Configurações completas de vários idiomas no Braze]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Definir as configurações de vários idiomas no Braze

Consulte [as instruções de configuração multilíngue do Braze]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) para configurar as localizações no Braze.

### Etapa 2: Configurar o projeto Braze no Smartling TMS

Consulte a [documentação da Smartling](https://help.smartling.com/hc/en-us/articles/13248549217435) para obter detalhes sobre a configuração do conector.

### Como conectar a Braze ao Smartling

1. Em sua [conta Smartling](https://dashboard.smartling.com/), crie um tipo de projeto [Braze Connector](https://help.smartling.com/hc/en-us/articles/115003074093).

![Conexão Braze em Smartling.]({% image_buster /assets/img/smartling/image1_Connecting_Braze_to_Smartling.png %})

{: start="2"}
2\. Nesse projeto, selecione **Configurações** > **Configurações do Braze** > **Conectar ao Braze**.
3\. Preencha os campos obrigatórios, como URL da API e chave da API. Se o teste de conexão for bem-sucedido, salve a conexão. Se o teste não for bem-sucedido, confirme se você inseriu o URL da API e a chave de API corretos.

![Conexão Braze nas configurações da API Smartling.]({% image_buster /assets/img/smartling/image2_API.png %})

{: start="4"}
4\. Adicionar outros idiomas de projeto.

![Conexão Braze em idiomas de projeto Smartling.]({% image_buster /assets/img/smartling/image3_project_languages.png %})

{: start="5"}
5\. Em Braze Settings, verifique se os valores na coluna **Target Language (Braze)** correspondem às localizações configuradas nas configurações multilíngues do Braze. A convenção de nomenclatura da localização deve corresponder exatamente.

![Conexão Braze em Smartling Language Confirmation.]({% image_buster /assets/img/smartling/image4_language_confirmation.png %})

### Etapa 3: Adicione tags de tradução à sua mensagem do Braze

Consulte [as instruções do Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/?tab%3Dhtml%2520editor#prerequisites) sobre como adicionar tags de tradução às suas mensagens:

- [E-mail]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email)
- [Push]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push)
- [Mensagem no app]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message)

Aqui está um exemplo de uma campanha de e-mail em HTML com tags de tradução.

![Envio de e-mail para o Braze com tags de tradução.]({% image_buster /assets/img/smartling/image5_translation_tags.png %})

Você deve salvar a mensagem como rascunho antes de selecionar as localizações.

### Etapa 4: Gerenciar traduções no Smartling

Depois de conectar e configurar o conector Braze, encontre o conteúdo do Braze na guia Braze em seu projeto Smartling. Para saber mais, consulte a [documentação do Smartling](https://help.smartling.com/hc/en-us/articles/13248577069979).

O Smartling oferece recursos avançados para pesquisar e selecionar conteúdo por:
- Pesquisa de palavras-chave
- Tipo de conteúdo de Braze
- Tags da Braze

1. Neste exemplo, a campanha de e-mail de promoção de Ano Novo foi criada na [etapa 3](#step-3-add-translation-tags-to-your-braze-message).

![Envio de e-mail para o Braze com tags de tradução.]({% image_buster /assets/img/smartling/image6_ny_promotion.png %})

{: start="2"}
2\. Depois de localizar a campanha que deseja traduzir, selecione a pasta, escolha as variantes e selecione **Solicitar tradução**.

![Solicitar traduções.]({% image_buster /assets/img/smartling/image7_request_translation.png %})

{: start="3"}
3\. Crie um novo trabalho para a tradução.

![Crie um novo trabalho para a tradução.]({% image_buster /assets/img/smartling/image8_request_translation.png %})

{: start="4"}
4\. Depois que o trabalho for autorizado, edite cada tradução na ferramenta CAT.

![Ferramenta CAT de tradução.]({% image_buster /assets/img/smartling/image9_translation_job.png %})

{: start="5"}
5\. Depois que as traduções forem concluídas, salve e envie sua tradução para o Braze.

![Enviar a tradução para o Braze.]({% image_buster /assets/img/smartling/image10_translations.png %})

### Etapa 5: Pré-visualize a mensagem como um usuário multilíngue no Braze

No Braze, faça uma prévia de sua campanha como um usuário multilíngue para confirmar que as traduções foram aplicadas corretamente.

![Prévia do usuário em vários idiomas.]({% image_buster /assets/img/smartling/image11_preview.png %})

## Gerenciamento de traduções para blocos de conteúdo

Os blocos de conteúdo são gerenciados na seção **Modelos & Media** no Braze.

### Tradução armazenada como parte do componente da mensagem

As tags de tradução pertencem ao bloco de conteúdo. No entanto, o Smartling executa traduções no nível da mensagem; o conteúdo é traduzido somente quando é incluído em uma campanha ou Canva e a localização de destino é definida.

### Considerações

- As tags de tradução devem ser adicionadas manualmente ao bloco de conteúdo para os editores de HTML e de arrastar e soltar o bloco de conteúdo.
- As localizações são selecionadas no nível da mensagem, não nos blocos de conteúdo em si.
- Para o Canva, recomendamos o uso de linhas para inserir blocos de conteúdo em sua mensagem em vez de adicioná-los manualmente com uma tag Liquid. Arrastar um bloco de conteúdo da prévia para um e-mail faz uma cópia local; quaisquer alterações no bloco de conteúdo "pai" não se propagam para outras campanhas que usam esse bloco.
- Se você usar uma tag Liquid do bloco de conteúdo, certifique-se de incluir pelo menos uma tag de tradução diretamente no corpo do e-mail. A adição manual da tag de tradução permite que você selecione as localizações no menu suspenso de vários idiomas. O Smartling pega as tags de tradução para o bloco de conteúdo. É possível adicionar uma tag `comment` para que o texto não fique visível para o usuário.

## Gerenciamento de traduções usando o fluxo de trabalho legado

Se preferir gerenciar as traduções diretamente em um bloco de conteúdo ou modelo de e-mail, consulte as instruções herdadas na [documentação da Smartling](https://help.smartling.com/hc/en-us/articles/13248577069979-Translating-with-the-Braze-Connector). Esse método usa uma atribuição de idioma e a lógica if/else do Liquid para exibir o texto em diferentes idiomas.

## Perguntas frequentes

### Há suporte para tags de tradução no editor de arrastar e soltar?

Para o editor de arrastar e soltar (e-mail, bloco de conteúdo, mensagem no app), você deve adicionar manualmente as tags de tradução como Liquid tags.

### Como traduzir o texto em uma tag Liquid?

O Smartling reconhece as tags Liquid e as torna variáveis não editáveis no criador. Qualquer outro texto dentro da tag Liquid, como texto padrão ou filtros como join, também se torna não editável no Smartling. No entanto, remova a tag Liquid no Smartling e recrie a tag Liquid com o texto padrão traduzido. Um aviso é exibido ao salvar a tradução.
