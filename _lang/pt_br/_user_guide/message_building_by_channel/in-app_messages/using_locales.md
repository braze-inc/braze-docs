---
nav_title: Localidades no envio de mensagens
article_title: Localidades no envio de mensagens
page_order: 4
alias: /iam_locales/
description: "Este artigo fornece etapas sobre como usar localidades em suas mensagens no app."
---

# Localidades em mensagens

> Depois de adicionar localidades ao seu espaço de trabalho, é possível direcionar usuários em diferentes idiomas em uma única mensagem no app.

{% multi_lang_include locales.md section="Prerequisites" %}

## Uso de localidades

Para usar localidades em seu envio de mensagens, crie uma campanha de mensagens no app ou no Canva. Selecione o editor de arrastar e soltar ou o editor tradicional e, em seguida, siga as etapas de acordo com seu editor.

{% tabs %}
{% tab editor tradicional %}

1. Adicione as tags de tradução {% raw %}`{% translation %}` e `{% endtranslation %}`{% endraw %} para envolver todos os URLs de texto e imagem ou link a serem traduzidos. 
2. Adicione uma tag de ID a cada tag de tradução. Um exemplo é: {% raw %}`{% translation id_1 %}`{% endraw %}

![Editor tradicional com IDs de tradução.]({% image_buster /assets/img/multi-language_support/html_iam_editor_translation_tags.png %}){: style="max-width:60%;"}

{: start="3"}
3\. Depois de adicionar as tags, salve sua mensagem como rascunho.
4\. Selecione **Gerenciar idiomas** e adicione suas localizações para a mensagem usando o menu suspenso.

![Modal "Gerenciar idiomas" com uma localização selecionada.]({% image_buster /assets/img/multi-language_support/manage_languages_modal.png %})

{: start="5"}
5\. Selecione **Baixar modelo** para baixar o modelo de tradução como um arquivo CSV. Em seguida, preencha as traduções no arquivo CSV.

![Um exemplo de um arquivo CSV de tradução.]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})

{: start="6"}
6\. Selecione **Upload translations** para fazer upload do arquivo CSV com as traduções concluídas.

{% endtab %}
{% tab Editor de arrastar e soltar %}

1. Adicione as tags de tradução {% raw %}`{% translation %}` e `{% endtranslation %}`{% endraw %} para envolver todos os URLs de texto e imagem ou link a serem traduzidos. 
2. Adicione uma tag de ID a cada tag de tradução. Um exemplo é: {% raw %}`{% translation id_1 %}`{% endraw %} 

![Editor de arrastar e soltar com dois IDs de tradução.]({% image_buster /assets/img/multi-language_support/dnd_iam_editor_translation_tags.png %}){: style="max-width:70%;"}

{: start="3"}
3\. Depois de adicionar as tags, salve sua mensagem como rascunho e abra o editor novamente.
4\. No painel **Build**, selecione **Multi-language** e adicione suas localizações para a mensagem usando o menu suspenso.
5\. Selecione **Baixar modelo** para baixar o modelo de tradução como um arquivo CSV. 

![Painel "multilíngue" com botão para baixar o modelo.]({% image_buster /assets/img/multi-language_support/dnd_iam_download_template.png %}){: style="max-width:40%;"}

{: start="6"}
6\. Preencha as traduções no arquivo CSV. Se tiver copiado e colado as tags de tradução diretamente da etapa 1, talvez seja necessário remover `<code>` da coluna **Translation tags** do arquivo CSV.
7\. Selecione **Upload translations** para fazer upload do arquivo CSV com as traduções concluídas.

![Painel "multilíngue" com botões para baixar o modelo e fazer upload das traduções.]({% image_buster /assets/img/multi-language_support/dnd_iam_upload_translations.png %}){: style="max-width:40%;"}

{% endtab %}
{% endtabs %}

Quaisquer alterações nas IDs ou localizações no arquivo CSV não serão atualizadas automaticamente em sua mensagem. Para atualizar as traduções, atualize o arquivo CSV e faça upload do arquivo novamente.

{% alert tip %}
Confira nossa [API de tradução]({{site.baseurl}}/api/endpoints/translations) para gerenciar e atualizar traduções em suas campanhas e canvas.
{% endalert %}

{% multi_lang_include locales.md section="Preview" %}

{% multi_lang_include locales.md section="Frequently Asked Questions" %}
