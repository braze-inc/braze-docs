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

{% alert important %}
O suporte a vários idiomas e as localizações nas mensagens estão atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar desse acesso antecipado.
{% endalert %}

## Uso de localidades

Para usar localidades em seu envio de mensagens, crie uma campanha de e-mail ou canva. Selecione o editor de HTML ou o editor de arrastar e soltar e siga as etapas de acordo com seu editor.

{% tabs %}
{% tab editor de HTML %}

1. Destaque o texto que você deseja traduzir. Selecione **Inserir tag de tradução**. Isso envolverá seu texto com tags de tradução. <br>![Editor de HTML com uma localização selecionada.]({% image_buster /assets/img/multi-language_support/html_editor_translation_tag_example.png %})
2. Salve a mensagem como um rascunho.
3. Selecione **Vários idiomas** e adicione suas localizações para a mensagem usando o menu suspenso.
4. Selecione **Baixar modelo** para baixar o modelo de tradução como um arquivo CSV. Em seguida, preencha as traduções no arquivo CSV. <br>![Um exemplo de um arquivo CSV de tradução.]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})
5. Selecione **Upload translations** para fazer upload do arquivo CSV com as traduções concluídas.

{% endtab %}
{% tab Editor de arrastar e soltar %}

1. Adicione as tags de tradução {% raw %}`{% translation %}` e `{% endtranslation %}`{% endraw %} para envolver todos os URLs de texto e imagem ou link a serem traduzidos. 
2. Adicione uma tag de ID a cada tag de tradução. Um exemplo é: {% raw %}`{% translation id_1 %}`{% endraw %} <br>![Editor de arrastar e soltar com dois IDs de tradução.]({% image_buster /assets/img/multi-language_support/dnd_editor_translation_example.png %})
3. Depois de adicionar as tags, salve sua mensagem como rascunho.
4. Selecione **Vários idiomas** e adicione suas localizações para a mensagem usando o menu suspenso.
5. Selecione **Baixar modelo** para baixar o modelo de tradução como um arquivo CSV. 
6. Preencha as traduções no arquivo CSV. Se tiver copiado e colado as tags de tradução diretamente da etapa 1, talvez seja necessário remover `<code>` da coluna **Translation tags** do arquivo CSV.
7. Selecione **Upload translations** para fazer upload do arquivo CSV com as traduções concluídas.

{% endtab %}
{% endtabs %}

Quaisquer alterações nas IDs ou localizações no arquivo CSV não serão atualizadas automaticamente em sua mensagem. Para atualizar as traduções, atualize o arquivo CSV e faça upload do arquivo novamente.

## Faça uma prévia de suas localidades

Na seção **Prévia e teste**, selecione **Usuário multilíngue** para verificar se a mensagem foi traduzida conforme o esperado.

## Gerenciamento de traduções

### Edição de traduções para campanhas e telas lançadas

Depois que uma campanha ou uma tela for lançada, você ainda poderá modificar as traduções quando estiver no modo de rascunho. Isso se aplica se estiver editando traduções diretamente no criador, fazendo upload de CSV ou por meio da API. 

Antes de fazer qualquer atualização de tradução, a campanha ou o Canva deve primeiro ser salvo como rascunho.

1. Selecione **Edit campaign/Canva (Editar campanha/Canvas** ) e, em seguida, faça suas edições no criador.
2. Selecione **Salvar como rascunho** e, em seguida, selecione **Sim** na janela modal.
3. Acesse a etapa **Review Summary (Resumo da revisão** ) e selecione **Update campaign/Canva (Atualizar campanha/Canva**).
4. Selecione **Atualizar campanha/Canva** no modal.

Para obter mais detalhes sobre o gerenciamento de campanhas e Canvas após o lançamento, consulte [Edição de campanhas lançadas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/) e [rascunhos do Canvas e edição pós-lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_drafts/).

### Duplicação de etapas ou campanhas do Canva e traduções

Ao duplicar uma etapa do Canva ou uma campanha, seja no modo de rascunho após o lançamento ou durante a criação inicial, as traduções associadas a essa etapa não serão transferidas. Todas as traduções necessárias precisam ser adicionadas à nova etapa ou campanha. Certifique-se de revisar e atualizar as traduções adequadamente ao fazer modificações em seu Canva ou campanha.

### Usando a API multilíngue com o Canvas

Para usar a [API multilíngue com o Canvas]({{site.baseurl}}/api/endpoints/translations/), você deve incluir `workflow_id`, `step_id` e `message_variation_id` na lista de parâmetros.

#### Etapas do canva adicionadas aos rascunhos pós-lançamento

Ao usar a API multilíngue com etapas do Canva que foram criadas após o lançamento do Canva, o endereço `message_variation_id` que você passar para a API estará vazio ou em branco.

{% multi_lang_include locales.md section="Frequently Asked Questions" %}