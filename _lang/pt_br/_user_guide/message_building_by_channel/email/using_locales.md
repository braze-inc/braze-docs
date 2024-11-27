---
nav_title: Localidades no envio de mensagens
article_title: Localidades no envio de mensagens
page_order: 6.3
description: "Este artigo fornece etapas sobre como usar localidades em seu envio de mensagens."
---

# Localidades no envio de mensagens

> Depois de adicionar localidades ao seu espaço de trabalho, é possível direcionar usuários em diferentes idiomas em uma única mensagem de e-mail.

## Pré-requisitos

Para editar e gerenciar [o suporte a vários idiomas]({{site.baseurl}}/multi_language_support/), é necessário ter a permissão de usuário "Manage Multi-Language Settings" (Gerenciar configurações de vários idiomas). Para adicionar a localização a uma mensagem, você precisará de permissões para editar campanhas.

## Uso de localidades

Para usar localidades em seu envio de mensagens, crie uma campanha de e-mail ou canva. Selecione o editor de HTML ou o editor de arrastar e soltar e siga as etapas de acordo com seu editor.

{% tabs %}
{% tab editor de HTML %}

1. Destaque o texto que você deseja traduzir. Selecione **Inserir tag de tradução**. Isso envolverá seu texto com tags de tradução. <br>![]({% image_buster /assets/img/multi-language_support/html_editor_translation_tag_example.png %})
2. Salve a mensagem como um rascunho.
3. Selecione **Vários idiomas** e adicione suas localizações para a mensagem usando o menu suspenso.
4. Selecione **Baixar modelo** para baixar o modelo de tradução como um CSV. Em seguida, preencha as traduções no CSV. <br>![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})
5. Selecione **Upload translations** para fazer upload do arquivo CSV com as traduções concluídas.

{% endtab %}
{% tab Editor de arrastar e soltar %}

1. Adicione as tags de tradução {% raw %}`{% translation %}` e `{% endtranslation %}`{% endraw %} para envolver todos os URLs de texto e imagem ou link a serem traduzidos.<br>![]({% image_buster /assets/img/multi-language_support/dnd_editor_translation_example.png %})
2. Depois de adicionar as tags, salve sua mensagem como rascunho.
3. Selecione **Vários idiomas** e adicione suas localizações para a mensagem usando o menu suspenso.
4. Selecione **Baixar modelo** para baixar o modelo de tradução como um CSV. Em seguida, preencha as traduções no CSV. <br>![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})
5. Selecione **Upload translations** para fazer upload do arquivo CSV com as traduções concluídas.

{% endtab %}
{% endtabs %}

Para atualizar as traduções, atualize o CSV e faça upload do arquivo novamente. Isso significa que qualquer alteração nas IDs ou localizações no CSV não será atualizada automaticamente em sua mensagem.

{% alert tip %}
Confira nossa [API de tradução]({{site.baseurl}}/api/endpoints/translations) para gerenciar e atualizar traduções em suas campanhas e canvas.
{% endalert %}

## Faça uma prévia de suas localidades

Na seção **Preview & Test (Pré-visualização e teste** ), selecione **Multi-language User (Usuário multilíngue** ) para pré-visualizar a mensagem e verificar se a mensagem foi traduzida conforme o esperado.

## Perguntas frequentes

#### Quero fazer uma alteração no texto traduzido em uma de minhas localizações. Como posso fazer isso?
Faça a edição no arquivo CSV e, em seguida, faça upload do arquivo novamente para fazer uma alteração no texto traduzida.

#### Posso aninhar tags de tradução?
Não.

#### Posso adicionar estilo HTML nas tags de tradução?
Sim. No entanto, confira se o estilo HTML não está traduzido com o conteúdo.

#### Que validações ou verificações extras o Braze faz?

| Cenário                                                                                                                                                 | Validação em Braze                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Um arquivo de tradução não tem localidades associadas à mensagem atual.                                                                               | Esse arquivo de tradução não será carregado.                                                                       |
| Um arquivo de tradução está sem alguns blocos de texto, como um texto dentro de tags de tradução Liquid, da mensagem de e-mail atual.                                | Esse arquivo de tradução não será carregado.                                                                       |
| O arquivo de tradução inclui o texto padrão que não corresponde aos blocos de texto da mensagem de e-mail atual.                                          | Esse arquivo de tradução não será carregado. Corrija isso em seu CSV antes de tentar fazer upload novamente.               |
| O arquivo de tradução inclui localizações que não existem nas configurações **do Suporte multilíngue**.                                                           | Essas localizações não serão salvas no Braze.                                                                      |
| O arquivo de tradução inclui blocos de texto que não existem na mensagem atual (como o rascunho atual no momento em que as traduções são feitas upload). | Os blocos de texto que não existirem em sua mensagem atual não serão salvos do arquivo de tradução para o Braze. |
| Remoção de uma localização da mensagem depois que essa localização já tiver sido carregada para a mensagem como parte do arquivo de tradução.                           | A remoção da localidade removerá todas as traduções associadas à localidade em sua mensagem.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }