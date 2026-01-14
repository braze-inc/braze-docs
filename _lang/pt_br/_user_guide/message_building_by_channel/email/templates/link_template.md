---
nav_title: Modelos de links
article_title: Modelos de links
page_order: 4
description: "Este artigo aborda como criar diferentes tipos de modelos de links em seus e-mails."
tool:
  - Templates
channel:
  - email

---

# Modelos de links

> Com os modelos de links, você pode criar links dinâmicos e reutilizáveis para suas campanhas de e-mail anexando parâmetros ou URLs. Isso pode criar consistência nos URLs em suas campanhas e mensagens. 

{% alert note %}
Os modelos de links são um recurso opcional. Se **o Email Link Templates** não estiver presente na seção **Templates**, entre em contato com o gerente da sua conta para ativar o recurso.
{% endalert %}

## Como funciona

Os modelos de links são usados com mais frequência nos seguintes casos de uso:

- Anexar parâmetros de consulta do Google Analytics a todos os links em uma determinada mensagem de e-mail
- Anexar um URL a todos os links em uma determinada mensagem de e-mail

Digamos que você esteja executando uma campanha promocional por e-mail para o lançamento de um novo produto. Você pode usar um modelo de link que direciona os usuários para a página do produto e personalizar o link para incluir o nome do usuário ou um código promocional específico. Isso permite que você acompanhe quantos usuários clicaram no link e fizeram uma compra. Dessa forma, você pode criar consistência entre seus links e monitorar melhor suas análises.

## Criação de um modelo de link

Você pode criar um número ilimitado de modelos de links para atender às suas diversas necessidades. Para criar um modelo de link, faça o seguinte:

1. Vá para **Templates** > **Email Link Templates**. 
2. Selecione **Criar modelo de link de e-mail**.
3. Dê um nome ao seu modelo de link.
4. (Opcional) Adicione uma descrição, equipe ou tag para acrescentar detalhes sobre o modelo de link.
5. (Opcional) Selecione o botão de alternância para adicionar automaticamente o modelo de link a links em campanhas de e-mail e Canvases. Isso se aplica ao adicionar um novo link a qualquer e-mail novo ou existente.

Há dois tipos de modelos de links que você pode criar:

- [Modelo de link que é inserido antes de um URL](#prepend-link-template)
- [Modelo de link que é inserido após uma URL](#append-link-template)

Ao usar modelos de link e [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), o Liquid só deve ser adicionado dentro da tag body para garantir uma renderização consistente.

### Anexar: Criar um modelo de link que seja inserido antes de um URL {#prepend-link-template}

Para adicionar uma cadeia de caracteres ou URL antes dos links em sua mensagem de e-mail, faça o seguinte:

1. Crie um novo modelo de link.
2. Defina a **posição do modelo** como **Before URL (Antes da URL)**. 
3. Insira uma cadeia de caracteres que sempre será anexada ao seu URL. 

A **visualização do modelo** é fornecida para lhe dar um exemplo de como o modelo de link será inserido antes de um URL.

Campos Template Position (Posição do modelo), Prepend URL (Anexar URL) e Template Preview (Visualização do modelo) para o processo de inserção do modelo de link antes de um URL.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### Anexar: Criar um modelo de link que seja inserido após um URL {#append-link-template}

Se você quiser adicionar parâmetros de consulta após um URL em sua mensagem de e-mail:

1. Crie um novo modelo de link.
2. Defina a **posição do modelo** como **After URL**. 
3. Insira os parâmetros de consulta (`value=example`) no final de cada URL. Você pode ter vários parâmetros anexados ao final de um URL.

Campos Template Position (Posição do modelo), Query Parameters (Parâmetros de consulta) e Template Preview (Visualização do modelo) para o processo de inserção do modelo de link após um URL.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## Uso de modelos de links em campanhas de e-mail

Após a configuração dos modelos de link, você pode selecionar o modelo a ser usado em seu e-mail.

- **Editor de HTML:** Vá para a guia **Link Management (Gerenciamento de links** ) na seção **Content (Conteúdo** ). Selecione **Add a Link Template (Adicionar um modelo de link**), escolha seu modelo de link e selecione **Add (Adicionar**).

{% alert important %}
Para acessar a guia **Gerenciamento de links** no editor de e-mail HTML atualizado, é necessário ativar o alias de links. Para ativar o aliasing de links, entre em contato com o gerente da sua conta.
{% endalert %}

- **Editor de arrastar e soltar:** Selecione a guia **Conteúdo** > **Gerenciamento de links**. Em seguida, selecione **Add a Link Template (Adicionar um modelo de link**). Para acessar os modelos de link no editor de arrastar e soltar, você deve ter [o aliasing de link]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/) ativado.

Aba Link Management no editor de arrastar e soltar com um exemplo de lista de modelos de links.]({% image_buster /assets/img_archive/link_template_messagecomposer2.png %})

{% alert note %}
Os modelos de link não são aplicados a texto simples. Isso significa que o Currents pode mostrar cliques que não incluem os parâmetros dos modelos de link, pois esses cliques podem vir da versão de texto simples do e-mail.
{% endalert %}

Ao adicionar modelos de links na guia **Gerenciamento de links**, role para a direita para ver os modelos que você adicionou. Se os links existentes em um e-mail já tiverem um modelo de link adicionado, os links recém-adicionados também terão o modelo de link adicionado por padrão.

## Gerenciamento de modelos de links

Você também pode [duplicar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) modelos de links. Saiba mais sobre como criar e gerenciar modelos e conteúdo criativo em [Templates & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

{% alert important %}
O arquivamento de modelos não está disponível no momento para modelos de links.
{% endalert %}

## Perguntas frequentes

Para obter respostas às perguntas mais frequentes sobre modelos de links, consulte nossa página de [perguntas frequentes sobre modelos]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/).

