---
nav_title: Locais em mensagens
article_title: Locais em mensagens
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "Este artigo fornece etapas sobre como usar localidades em suas mensagens."
---

# Locais em mensagens

> Depois de adicionar localidades ao seu espaço de trabalho, você pode segmentar usuários em diferentes idiomas em uma única mensagem push, de e-mail ou no aplicativo.

{% multi_lang_include locales.md section="Prerequisites" %}

{% alert important %}
O suporte a vários idiomas e as localidades nas mensagens estão atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar desse acesso antecipado.
{% endalert %}

## Uso de localidades

{% tabs %}
{% tab In-app message %}

Para usar as localidades em suas mensagens, crie uma campanha de mensagens no aplicativo ou no Canvas. Selecione o editor de arrastar e soltar ou o editor tradicional e siga as etapas de acordo com seu editor.

{% subtabs %}
{% subtab traditional editor %}

1. Adicione as tags de tradução {% raw %}`{% translation %}` e `{% endtranslation %}`{% endraw %} para envolver todos os URLs de texto e imagem ou link a serem traduzidos. 
2. Adicione uma tag de ID a cada tag de tradução. Um exemplo é: {% raw %}`{% translation id_1 %}`{% endraw %}

\![Editor tradicional com IDs de tradução.]({% image_buster /assets/img/multi-language_support/html_iam_editor_translation_tags.png %}){: style="max-width:60%;"}

{: start="3"}
3\. Depois de adicionar as tags, salve sua mensagem como rascunho.
4\. Selecione **Gerenciar idiomas** e adicione suas localidades para a mensagem usando o menu suspenso.

\!["Gerenciar idiomas" modal com uma localidade selecionada.]({% image_buster /assets/img/multi-language_support/manage_languages_modal.png %})

{: start="5"}
5\. Selecione **Baixar modelo** para baixar o modelo de tradução como um arquivo CSV. Em seguida, preencha as traduções no arquivo CSV.

\![Um exemplo de um arquivo CSV de tradução.]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})

{: start="6"}
6\. Selecione **Carregar traduções** para carregar o arquivo CSV com as traduções concluídas.

{% endsubtab %}
{% subtab Drag-and-drop editor %}

1. Adicione as tags de tradução {% raw %}`{% translation %}` e `{% endtranslation %}`{% endraw %} para envolver todos os URLs de texto e imagem ou link a serem traduzidos. 
2. Adicione uma tag de ID a cada tag de tradução. Um exemplo é: {% raw %}`{% translation id_1 %}`{% endraw %} 

\![Editor de arrastar e soltar com duas IDs de tradução.]({% image_buster /assets/img/multi-language_support/dnd_iam_editor_translation_tags.png %}){: style="max-width:70%;"}

{: start="3"}
3\. Depois de adicionar as tags, salve sua mensagem como rascunho e abra o editor novamente.
4\. No painel **Build**, selecione **Multi-language** e adicione suas localidades para a mensagem usando o menu suspenso.
5\. Selecione **Baixar modelo** para baixar o modelo de tradução como um arquivo CSV. 

\!["Painel multilíngue" com botão para fazer download do modelo.]({% image_buster /assets/img/multi-language_support/dnd_iam_download_template.png %}){: style="max-width:40%;"}

{: start="6"}
6\. Preencha as traduções no arquivo CSV. Se você copiou e colou as tags de tradução diretamente da Etapa 1, talvez seja necessário remover `<code>` da coluna **Translation tags** do arquivo CSV.
7\. Selecione **Carregar traduções** para carregar o arquivo CSV com as traduções concluídas.

\!["Painel multilíngue" com botões para fazer download do modelo e carregar traduções.]({% image_buster /assets/img/multi-language_support/dnd_iam_upload_translations.png %}){: style="max-width:40%;"}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Email %}

Para usar as localidades em suas mensagens, crie uma campanha de e-mail ou Canvas. Selecione o editor HTML ou o editor de arrastar e soltar e, em seguida, siga as etapas de acordo com seu editor.

{% subtabs %}
{% subtab HTML editor %}

1. Destaque o texto que você deseja traduzir. Selecione **Inserir tag de tradução**. Isso envolverá seu texto com tags de tradução. <br>\![Editor HTML com uma localidade selecionada.]({% image_buster /assets/img/multi-language_support/html_editor_translation_tag_example.png %})
2. Salve a mensagem como um rascunho.
3. Selecione **Multi-language (Vários idiomas** ) e adicione suas localidades para a mensagem usando o menu suspenso.
4. Selecione **Baixar modelo** para baixar o modelo de tradução como um arquivo CSV. Em seguida, preencha as traduções no arquivo CSV. <br>\![Um exemplo de um arquivo CSV de tradução.]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})
5. Selecione **Carregar traduções** para carregar o arquivo CSV com as traduções concluídas.

{% endsubtab %}
{% subtab Drag-and-drop editor %}

1. Adicione as tags de tradução {% raw %}`{% translation %}` e `{% endtranslation %}`{% endraw %} para envolver todos os URLs de texto e imagem ou link a serem traduzidos. 
2. Adicione uma tag de ID a cada tag de tradução. Um exemplo é: {% raw %}`{% translation id_1 %}`{% endraw %} <br>\![Editor de arrastar e soltar com duas IDs de tradução.]({% image_buster /assets/img/multi-language_support/dnd_editor_translation_example.png %})
3. Depois de adicionar as tags, salve sua mensagem como rascunho.
4. Selecione **Multi-language (Vários idiomas** ) e adicione suas localidades para a mensagem usando o menu suspenso.
5. Selecione **Baixar modelo** para baixar o modelo de tradução como um arquivo CSV. 
6. Preencha as traduções no arquivo CSV. Se você copiou e colou as tags de tradução diretamente da Etapa 1, talvez seja necessário remover `<code>` da coluna **Translation tags** do arquivo CSV.
7. Selecione **Carregar traduções** para carregar o arquivo CSV com as traduções concluídas.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Push %}

Para usar as localidades em suas mensagens, crie uma campanha push ou um Canvas e conclua o seguinte:

1. Adicione tags de tradução {% raw %}`{% translation id1%}` e `{% endtranslation %}`{% endraw %} para envolver todos os URLs de texto, imagem ou link a serem traduzidos. Cada ID de tradução (`id1`) deve ser exclusiva.

Compositor de notificações push com tags de tradução adicionadas aos campos de título e mensagem.]({% image_buster /assets/img/multi-language_support/push_translation_tags.png %})

{: start="2"}
2\. Salve sua mensagem como um rascunho.
3\. Selecione **Gerenciar idioma** e adicione suas localidades para a mensagem usando o menu suspenso.
4\. Selecione **Baixar modelo** e, em seguida, preencha as traduções no modelo CSV.

\![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})

{: start="5"}
5\. Para carregar o modelo CSV preenchido, selecione **Upload translations (Carregar traduções**). 

A janela "Multi-language messages" (Mensagens em vários idiomas) com duas localidades selecionadas e botões para fazer download de um modelo ou carregar traduções.]({% image_buster /assets/img/multi-language_support/upload_translation.png %})

{% endtab %}
{% endtabs %}

Quaisquer alterações nas IDs ou localidades no arquivo CSV não serão atualizadas automaticamente em sua mensagem. Para atualizar as traduções, atualize o arquivo CSV e faça o upload do arquivo novamente.

{% alert tip %}
Confira nossa [API de tradução]({{site.baseurl}}/api/endpoints/translations) para gerenciar e atualizar traduções em suas campanhas e Canvases.
{% endalert %}

## Visualize suas localidades

{% tabs %}
{% tab In-app message %}

No menu suspenso **Preview message as user (Visualizar mensagem como usuário** ) na guia **Test (Teste** ), selecione **Custom user (Usuário personalizado** ) e insira idiomas diferentes para visualizar a mensagem e verificar se a mensagem foi traduzida conforme o esperado.


{% endtab %}
{% tab Email %}

Na seção **Preview & Test (Teste de visualização** ), selecione **Multi-language User (Usuário multilíngue** ) para verificar se a mensagem foi traduzida conforme o esperado.

{% endtab %}
{% tab Push %}

No menu suspenso **Preview message as user (Visualizar mensagem como usuário** ) na guia **Test (Teste** ), selecione **Custom user (Usuário personalizado** ) e insira idiomas diferentes para visualizar a mensagem e verificar se a mensagem foi traduzida conforme o esperado.

{% endtab %}
{% endtabs %}

## Gerenciamento de traduções

### Edição de traduções para campanhas lançadas e Canvases

Depois que uma campanha ou tela for lançada, você ainda poderá modificar as traduções quando estiver no modo de rascunho. Isso se aplica se você estiver editando traduções diretamente no compositor, por upload de CSV ou por meio da API. 

Antes de fazer qualquer atualização de tradução, a campanha ou o Canvas deve primeiro ser salvo como rascunho.

1. Selecione **Edit campaign/Canvas** e, em seguida, faça suas edições no compositor.
2. Selecione **Salvar como rascunho** e, em seguida, selecione **Sim** na janela modal.
3. Vá para a etapa **Review Summary (Resumo da revisão** ) e selecione **Update campaign/Canvas (Atualizar campanha/Canvas**).
4. Selecione **Atualizar campanha/Canvas** na janela modal.

Para obter mais detalhes sobre o gerenciamento de campanhas e Canvases após o lançamento, consulte [Edição de campanhas lançadas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/) e [rascunhos do Canvas e edição pós-lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_drafts/).

### Duplicação de etapas ou campanhas do Canvas e traduções

Ao duplicar uma etapa do Canvas ou uma campanha, seja no modo de rascunho após o lançamento ou durante a criação inicial, as traduções associadas a essa etapa não serão transferidas. Todas as traduções necessárias precisam ser adicionadas à nova etapa ou campanha. Certifique-se de revisar e atualizar as traduções adequadamente ao fazer modificações em seu Canvas ou campanha.

### Usando a API multilíngue com o Canvases

Para usar a [API multilíngue com o Canvases]({{site.baseurl}}/api/endpoints/translations/), você deve incluir `workflow_id`, `step_id` e `message_variation_id` na lista de parâmetros.

#### Etapas do Canvas adicionadas aos rascunhos pós-lançamento

Ao usar a API multilíngue com etapas do Canvas que foram criadas após o lançamento do Canvas, o `message_variation_id` que você passar para a API estará vazio ou em branco.

## Perguntas frequentes

#### Posso fazer uma alteração na cópia traduzida em uma de minhas localidades?
Sim. Primeiro, faça a edição no CSV e, em seguida, carregue o arquivo novamente para fazer uma alteração na cópia traduzida.

#### Posso aninhar tags de tradução?
Não.

#### Posso adicionar estilo HTML nas tags de tradução?
Sim, mas não se esqueça de verificar se o estilo HTML não está traduzido com o conteúdo.

#### Que validações ou verificações extras o Braze faz?

| Cenário                                                                                                                                                 | Validação em brasagem                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Um arquivo de tradução não possui localidades associadas à mensagem atual.                                                                               | Esse arquivo de tradução não será carregado.                                                                       |
| Um arquivo de tradução está faltando blocos de texto, como um texto dentro das tags de tradução Liquid, da mensagem de e-mail atual.                                | Esse arquivo de tradução não será carregado.                                                                       |
| O arquivo de tradução inclui o texto padrão que não corresponde aos blocos de texto da mensagem de e-mail atual.                                          | Esse arquivo de tradução não será carregado. Corrija isso em seu CSV antes de tentar fazer o upload novamente.               |
| O arquivo de tradução inclui localidades que não existem nas configurações **do Suporte multilíngue**.                                                           | Essas localidades não serão salvas no Braze.                                                                      |
| O arquivo de tradução inclui blocos de texto que não existem na mensagem atual (como o rascunho atual no momento em que as traduções são carregadas). | Os blocos de texto que não existirem em sua mensagem atual não serão salvos do arquivo de tradução para o Braze. |
| Remoção de uma localidade da mensagem depois que essa localidade já tiver sido carregada na mensagem como parte do arquivo de tradução.                           | A remoção da localidade removerá todas as traduções associadas à localidade em sua mensagem.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }