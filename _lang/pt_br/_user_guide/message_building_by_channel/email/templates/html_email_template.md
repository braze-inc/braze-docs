---
nav_title: Carregando um Modelo de E-mail HTML
article_title: Carregando um Modelo de E-mail HTML
page_order: 2
description: "Este artigo de referência explica como criar, gerenciar e solucionar problemas de um modelo de e-mail HTML usando o dashboard da Braze."
tool:
  - Templates
channel:
  - email

---

# Carregando um modelo de e-mail HTML

> O dashboard da Braze permite que você faça upload de seus próprios modelos de e-mail em HTML e os salve para uso posterior em campanhas. Você também pode [criar um modelo de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) usando nosso editor.

## Pré-requisitos {#upload-requirements}

Primeiro, você precisará criar seu modelo de e-mail HTML. Este deve ser um arquivo ZIP que contém o seguinte:

* Um único arquivo HTML—o corpo do seu e-mail
* Uma pasta de imagens que são referenciadas no arquivo HTML
* Menos de 50 arquivos de imagem
* Seja menor que 5 MB

## Carregando seu modelo

### Etapa 1: Navegue para o editor de modelo de e-mail

Acessar os **Templates** > **e-mail Templates**.

### Etapa 2: Abrir o carregador

Na seção **Tipo de Modelo**, selecione **editor de HTML** e role para baixo até a seção **Comece a partir de um Modelo HTML Básico**. Selecione **De Arquivo**.

### Etapa 3: Faça o upload do seu modelo

Selecione **fazer upload de arquivo** e selecione seu modelo do seu computador. Consulte a seção [Pré-requisitos](#upload-requirements) para garantir que seu modelo atenda aos requisitos de fazer upload.

#### Solucionar problemas de erros de upload de modelo

Há várias mensagens de erro de e-mail que você pode receber ao enviar um arquivo de modelo HTML. Se você vir uma mensagem de erro, consulte a tabela a seguir para problemas comuns e suas correções recomendadas:

| Erro | Consertar |
|------|---|
|.zip acima de 5 MB| Reduza o tamanho do seu arquivo e tente fazer o upload novamente.|
|.zip corrompido| Inspecione seu arquivo e tente fazer o upload novamente. |
|HTML não encontrado| Adicione o arquivo HTML ao seu arquivo ZIP e tente fazer o upload novamente.|
|Múltiplos HTML| Remova um dos arquivos HTML e tente fazer o upload novamente.|
|Imagens acima de 5 MB| Reduza o número de imagens e tente fazer o upload novamente. |
|Imagens Extras| Pode haver imagens adicionais no seu arquivo que não são referenciadas no seu arquivo HTML. Isso não causará um erro de falha, mas as imagens extras serão descartadas. Se essas imagens deveriam ser referenciadas no arquivo HTML, então verifique o conteúdo, corrija quaisquer erros e tente fazer o upload novamente.|
|Imagens ausentes| Se houver imagens referenciadas no seu arquivo HTML, mas essas imagens não estiverem incluídas na pasta de imagens do arquivo ZIP, você receberá um erro de arquivo. Inspecione seu arquivo e corrija quaisquer erros (como erros de ortografia), ou adicione as imagens ausentes ao seu arquivo ZIP e tente fazer o upload novamente.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapa 4: Conclua e salve seu modelo

Certifique-se de salvar seu modelo selecionando **Save Template (Salvar modelo)**. Agora você está pronto para usar este modelo em qualquer campanha ou canva que escolher!

{% alert note %}
Se você fizer qualquer edição em um modelo existente, essas alterações não serão refletidas em campanhas que foram criadas usando versões anteriores desse modelo.
{% endalert %}

## Usando seus modelos em campanhas de API {#api_for_upload_email_templates}

Para usar seu e-mail em uma campanha de API, você precisa do `email_template_id`, que pode ser encontrado na parte inferior de qualquer modelo de e-mail criado no Braze.

Seção ![Identificador da API de um modelo de e-mail HTML.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:50%;"}

## Gerenciando templates de e-mail

Você pode [duplicar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) e [arquivar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) modelos de e-mail! Saiba mais sobre como criar e gerenciar modelos e conteúdo criativo em [Templates]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## Perguntas frequentes

Para respostas a perguntas frequentes sobre modelos de e-mail, confira nossa página [FAQ sobre e-mail e modelos de link]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/).


