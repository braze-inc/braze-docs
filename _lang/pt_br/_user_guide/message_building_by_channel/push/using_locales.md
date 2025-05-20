---
nav_title: Localidades no envio de mensagens
article_title: Localidades no envio de mensagens
page_order: 9
description: "Este artigo fornece etapas sobre como usar localidades em suas notificações por push."
---

# Localidades em mensagens

> Depois de adicionar localizações ao seu espaço de trabalho, é possível direcionar usuários em diferentes idiomas, tudo em uma única notificação por push.

## Pré-requisitos

Para editar e gerenciar [o suporte a vários idiomas]({{site.baseurl}}/multi_language_support/), é necessário ter a permissão de usuário "Manage Multi-Language Settings" (Gerenciar configurações de vários idiomas). Para adicionar a localização a uma mensagem, você precisará de permissões para editar campanhas.

## Uso de localidades

Para usar localidades em seu envio de mensagens, crie uma campanha de mensagens push ou um Canva e conclua o seguinte:

1. Adicione as tags de tradução {% raw %}`{% translation %}` e `{% endtranslation %}`{% endraw %} para envolver todos os URLs de texto e imagem ou link a serem traduzidos.<br><br>![Criador de notificações por push com tags de tradução adicionadas aos campos de título e mensagem.]({% image_buster /assets/img/multi-language_support/push_translation_tags.png %})<br><br>
2. Salve sua mensagem como um rascunho.
3. Selecione **Gerenciar idioma** e adicione suas localizações para a mensagem usando o menu suspenso.
4. Selecione **Baixar modelo** e, em seguida, preencha as traduções no modelo CSV. <br><br>![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})<br><br>
5. Para fazer upload do modelo CSV concluído, selecione **Upload translations (Fazer upload de traduções**). <br><br>![A janela "Mensagens em vários idiomas" com duas localizações selecionadas e botões para baixar um modelo ou fazer upload de traduções.]({% image_buster /assets/img/multi-language_support/upload_translation.png %})

Para atualizar as traduções, atualize o CSV e faça upload do arquivo novamente. Isso significa que qualquer alteração nas IDs ou localizações no CSV não será atualizada automaticamente em sua mensagem.

{% alert tip %}
Confira nossa [API de tradução]({{site.baseurl}}/api/endpoints/translations) para gerenciar e atualizar traduções em suas campanhas e canvas.
{% endalert %}

## Faça uma prévia de suas localidades

No menu suspenso **Visualizar mensagem como usuário** na guia **Teste**, selecione **Usuário personalizado** e insira idiomas diferentes para fazer a prévia da mensagem e verificar se a mensagem foi traduzida conforme o esperado.

{% multi_lang_include locales.md section="Frequently Asked Questions" %}
