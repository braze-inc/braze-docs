---
nav_title: Carregamento de um modelo de e-mail em HTML
article_title: Carregamento de um modelo de e-mail HTML
page_order: 2
description: "Este artigo de referência aborda como criar, gerenciar e solucionar problemas de um modelo de e-mail HTML usando o painel de controle do Braze."
tool:
  - Templates
channel:
  - email

---

# Carregamento de um modelo de e-mail em HTML

> O painel de controle do Braze permite que você carregue seus próprios modelos de e-mail em HTML e os salve para uso posterior em campanhas. Você também pode [criar um modelo de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) usando nosso editor.

## Pré-requisitos {#upload-requirements}

Primeiro, você precisará criar seu modelo de e-mail em HTML. Esse deve ser um arquivo ZIP que contenha o seguinte:

* Um único arquivo HTML - o corpo do seu e-mail
* Uma pasta de imagens que são referenciadas no arquivo HTML
* Menos de 50 arquivos de imagem
* Ter menos de 5 MB

## Carregamento de seu modelo

### Etapa 1: Navegue até o editor de modelos de e-mail

Vá para **Templates** > **Email Templates**.

### Etapa 2: Abra o carregador

Na seção **Tipo de modelo**, selecione **Editor HTML** e role para baixo até a seção **Iniciar a partir de um modelo HTML básico**. Selecione **From File**.

### Etapa 3: Faça upload de seu modelo

Selecione **Upload From File** e selecione o modelo em seu computador. Consulte a seção [Pré-requisitos](#upload-requirements) para garantir que seu modelo atenda aos requisitos de upload.

#### Solucionar problemas de erros de upload de modelos

Há várias mensagens de erro de e-mail que você pode receber ao fazer upload de um arquivo de modelo HTML. Se você receber um erro, consulte a tabela a seguir para ver os problemas comuns e as correções recomendadas:

| Erro | Consertar |
|------|---|
|.zip com mais de 5 MB| Reduza o tamanho do arquivo e tente fazer o upload novamente.|
|.zip corrompido| Inspecione seu arquivo e tente fazer o upload novamente. |
|HTML ausente| Adicione o arquivo HTML ao seu arquivo ZIP e tente fazer o upload novamente.|
|Vários HTML| Remova um dos arquivos HTML e tente fazer o upload novamente.|
|Imagens com mais de 5 MB| Reduza o número de imagens e tente fazer o upload novamente. |
|Imagens extras| Pode haver imagens adicionais em seu arquivo que não estejam referenciadas em seu arquivo HTML. Isso não causará um erro de falha, mas as imagens extras serão descartadas. Se essas imagens deveriam ser referenciadas no arquivo HTML, verifique o conteúdo, corrija os erros e tente fazer o upload novamente.|
|Imagens ausentes| Se houver imagens referenciadas em seu arquivo HTML, mas essas imagens não estiverem incluídas na pasta de imagens do arquivo ZIP, você receberá um erro de arquivo. Inspecione seu arquivo e corrija os erros (como erros de ortografia) ou adicione as imagens que faltam ao seu arquivo ZIP e tente fazer o upload novamente.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapa 4: Conclua e salve seu modelo

Certifique-se de salvar seu modelo selecionando **Save Template (Salvar modelo**). Agora você está pronto para usar esse modelo em qualquer campanha ou Canvas que escolher!

{% alert note %}
Se você fizer qualquer edição em um modelo existente, essas alterações não serão refletidas nas campanhas que foram criadas usando versões anteriores desse modelo.
{% endalert %}

## Uso de seus modelos em campanhas de API {#api_for_upload_email_templates}

Para usar seu e-mail para uma campanha de API, você precisa do endereço `email_template_id`, que pode ser encontrado na parte inferior de qualquer modelo de e-mail criado no Braze.

Seção API Identifier de um modelo de e-mail em HTML.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:50%;"}

## Gerenciamento de modelos de e-mail

Você pode [duplicar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) e [arquivar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) modelos de e-mail! Saiba mais sobre como criar e gerenciar modelos e conteúdo criativo em [Modelos]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## Perguntas frequentes

Para obter respostas às perguntas mais frequentes sobre modelos de e-mail, consulte nossa página de [perguntas frequentes sobre modelos de e-mail e links]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/).


