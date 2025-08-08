---
nav_title: Localidades no envio de mensagens
article_title: Localidades no envio de mensagens
page_order: 9
description: "Este artigo fornece etapas sobre como usar localidades em suas notificações por push."
---

# Localidades em mensagens

> Depois de adicionar localizações ao seu espaço de trabalho, é possível direcionar usuários em diferentes idiomas, tudo em uma única notificação por push.

{% multi_lang_include locales.md section="Prerequisites" %}

{% alert important %}
O suporte a vários idiomas e as localizações nas mensagens estão atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar desse acesso antecipado.
{% endalert %}

## Uso de localidades

Para usar localidades em seu envio de mensagens, crie uma campanha de mensagens push ou um Canva e conclua o seguinte:

1. Adicione as tags de tradução {% raw %}`{% translation %}` e `{% endtranslation %}`{% endraw %} para envolver todos os URLs de texto e imagem ou link a serem traduzidos.

![Criador de notificações por push com tags de tradução adicionadas aos campos de título e mensagem.]({% image_buster /assets/img/multi-language_support/push_translation_tags.png %})

{: start="2"}
2\. Salve sua mensagem como um rascunho.
3\. Selecione **Gerenciar idioma** e adicione suas localizações para a mensagem usando o menu suspenso.
4\. Selecione **Baixar modelo** e, em seguida, preencha as traduções no modelo CSV.

![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})

{: start="5"}
5\. Para fazer upload do modelo CSV concluído, selecione **Upload translations (Fazer upload de traduções**). 

![A janela "Mensagens em vários idiomas" com duas localizações selecionadas e botões para baixar um modelo ou fazer upload de traduções.]({% image_buster /assets/img/multi-language_support/upload_translation.png %})

Quaisquer alterações nas IDs ou localizações no arquivo CSV não serão atualizadas automaticamente em sua mensagem. Para atualizar as traduções, atualize o arquivo CSV e faça upload do arquivo novamente.

{% alert tip %}
Confira nossa [API de tradução]({{site.baseurl}}/api/endpoints/translations) para gerenciar e atualizar traduções em suas campanhas e canvas.
{% endalert %}

{% multi_lang_include locales.md section="Preview" %}

{% multi_lang_include locales.md section="Frequently Asked Questions" %}
