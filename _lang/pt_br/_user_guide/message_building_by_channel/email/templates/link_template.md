---
nav_title: Modelos de links
article_title: Modelos de links
page_order: 4
description: "Este artigo aborda como criar diferentes tipos de modelos de link em seus e-mails."
tool:
  - Templates
channel:
  - email

---

# Modelos de links

> Os modelos de link permitem adicionar parâmetros e prefixar URLs a todos os links em uma mensagem de e-mail.

Modelos de link são mais frequentemente usados nos seguintes casos:

1. Anexando parâmetros de consulta do Google análise de dados a todos os links em uma determinada mensagem de e-mail
2. Adicionar um URL a todos os links em uma determinada mensagem de e-mail

{% alert note %}
Os modelos de link são um recurso opcional. Se **Modelos de Link de E-mail** estiver ausente na seção **Modelos**, entre em contato com o gerente da sua conta para ativar o recurso.
{% endalert %}

## Criar um modelo de link

![][11]{: style="float:right;max-width:20%;"}

Você pode criar um número ilimitado de modelos de link para suportar suas várias necessidades. Para criar um modelo de link:

1. Acessar **Modelos** > **Enviar modelo de link por e-mail**. 
2. Clique em **Criar Modelo de Link**.

{% alert note %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), esta página está localizada em **engajamento** > **modelos e mídias** > **Modelos de Link**.
{% endalert %}

Existem dois tipos de modelos de link que você pode criar:

- [Modelo de link que é inserido  antes de um URL](#prepend-link-template)
- [Modelo de link que insere após um URL](#append-link-template)

Ao usar modelos de link e [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), Liquid deve ser adicionado apenas dentro da tag body para garantir uma renderização consistente.

### Prepend: Crie um modelo de link para inserir antes de um URL {#prepend-link-template}

Se você quiser adicionar uma string ou URL antes dos links na sua mensagem de e-mail, crie um novo modelo de link e defina a **Posição do Modelo** para **Antes da URL**. Em seguida, insira uma string que sempre será adicionada ao início do seu URL. 

Uma seção de prévia é fornecida com um exemplo do processo de inserção.

![Os campos Posição do modelo, URL de prepend e Prévia do Modelo para o processo de inserção de modelo de link antes de um URL.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### Anexar: Crie um modelo de link para inserir após um URL {#append-link-template}

Se você quiser adicionar parâmetros de consulta após um URL na sua mensagem de e-mail, crie um novo modelo de link e defina a **Posição do Modelo** para **Após URL**. Em seguida, insira os parâmetros de consulta (`value=something`) no final de cada URL.

Você pode ter vários parâmetros anexados ao final de um URL.

![Posição do Modelo, Parâmetros de Consulta e campos de Prévia do Modelo para o processo de inserção de modelo de link após um URL.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## Usando modelos de link em campanhas de e-mail

Depois que seus modelos de link estiverem configurados, você pode selecionar o modelo a ser usado em seu e-mail.

- **editor de HTML:** Acessar a guia **Gerenciamento de link** na seção **Conteúdo**. Selecione **Add a Link Template (Adicionar um modelo de** link), escolha seu modelo de link e selecione **Add (Adicionar**).

{% alert important %}
Para acessar a guia **Gerenciamento de Links** no editor de e-mail HTML atualizado, você deve ter a aliasing de links ativada. Para ativar a vinculação de links, entre em contato com o gerente da sua conta.
{% endalert %}

- **Editor de arrastar e soltar:** Selecione **Conteúdo** > **Gerenciamento de Links**. Em seguida, selecione **Add a Link Template (Adicionar um modelo de link**). Para acessar os modelos de link no editor de arrastar e soltar, você deve ter [aliasing de link]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/) ativado.

![Guia de gerenciamento de links no editor de arrastar e soltar com uma lista de exemplo de modelos de links.][1]

{% alert note %}
Os modelos de link não são aplicados a texto simples. Isso significa que o Currents pode mostrar cliques que não incluem os parâmetros dos modelos de link, pois esses cliques podem vir da versão de texto simples do e-mail.
{% endalert %}

À medida que você adiciona modelos de link na guia **Gerenciamento de Links**, role para a direita para ver os modelos que você adicionou.

## Gerenciamento de modelos de links

Você também pode [duplicar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) modelos de link. Saiba mais sobre como criar e gerenciar modelos e conteúdos criativos em [modelos e mídias]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

{% alert important %}
O recurso de arquivar modelos não está disponível atualmente para modelos de link.
{% endalert %}

## Perguntas frequentes

Para respostas a perguntas frequentes sobre modelos de links, confira nossa [página de Perguntas Frequentes sobre Modelos][10].

[1]:{% image_buster /assets/img_archive/link_template_messagecomposer2.png %}
[2]:{% image_buster /assets/img_archive/link_template_postappend.png %}
[3]:{% image_buster /assets/img_archive/link_template_preappend.png %}
[4]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/
[11]: {% image_buster /assets/img_archive/create_link_template.png %}
