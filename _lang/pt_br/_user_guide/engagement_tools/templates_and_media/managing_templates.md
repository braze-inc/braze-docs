---
nav_title: Gerenciamento de modelos
article_title: Gerenciamento de modelos
page_order: 3

page_type: reference
description: "Este artigo de referência descreve como duplicar e arquivar modelos na seção Modelos e mídia do painel de controle do Braze."
tool:
  - Templates
  - Media

---

# Gerenciamento de modelos

> O arquivamento ou a duplicação de modelos pode ajudar a organizá-los e gerenciá-los melhor. Este artigo de referência aborda como arquivar e duplicar modelos na seção **Modelos** do painel de controle do Braze.

## Duplicação de modelos

### Modelo individual

\![Menu suspenso com opção duplicada.]({% image_buster /assets/img/template_duplicate_cog.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

Para duplicar um modelo individual, selecione o ícone de engrenagem <i class="fas fa-cog"></i> para o modelo individual e selecione **Duplicate (Duplicar** ) no menu suspenso.
<br><br>

{% alert note %}
Para modelos de [bloco de conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/), é criada uma cópia de rascunho. Para todos os outros modelos, uma nova cópia duplicada é criada automaticamente.
{% endalert %}

### Vários modelos

{% raw %}

A duplicação de vários modelos pode ser feita selecionando a caixa de seleção ao lado do nome do modelo. Primeiro, selecione os modelos e, em seguida, selecione **Duplicate (Duplicar**).

Os modelos duplicados podem ser encontrados classificando a coluna **Last Edited (Última edição** ). Por padrão, os novos modelos serão denominados `Copy of ORIGINAL_TEMPLATE_NAME`.

{% endraw %}

\![Três modelos classificados pela hora em que foram editados pela última vez, com um modelo copiado no topo da lista.]({% image_buster /assets/img/duplicate_multiple_template.gif %})

## Modelos de arquivamento

\![Menu suspenso de configurações expandido que mostra três opções: "Archive" (Arquivar), "Duplicate" (Duplicar) e "Copy to workspace" (Copiar para o espaço de trabalho) com a opção "Archive" (Arquivar) destacada.]({% image_buster /assets/img/template_archive_cog.png %}){: style="float:right;max-width:20%;margin-left:15px;"}

Para arquivar um modelo individual, selecione o ícone de configurações na tela da grade de modelos e selecione **Arquivar**. Quando um modelo for arquivado, observe os diferentes cenários a seguir:

- As campanhas ativas continuam a usar o modelo arquivado sem nenhuma interrupção.
- As campanhas de rascunho mantêm o conteúdo do modelo arquivado e podem ser editadas e lançadas.
- Para editar um modelo arquivado, você deve primeiro desarquivá-lo. Da mesma forma, para usar um modelo arquivado em uma campanha, você deve primeiro desarquivar o modelo.

Para arquivar vários modelos, marque a caixa de seleção ao lado de cada modelo que você deseja arquivar. Depois de selecionar vários modelos, selecione **Archive**. Você pode encontrar seus modelos arquivados selecionando **Archived** em **Show** na grade de modelos.

Drop Saved & Seção Drop Email Templates que mostra dois modelos selecionados e a barra de ferramentas com a opção de arquivamento.]({% image_buster /assets/img/archive_multiple_template.png %}){: style="max-width:60%;"}

{% alert important %}
O arquivamento não está disponível no momento para [modelos de links]({{site.baseurl}}/user_guide/message_building_by_channel/email/link_templates/#link-templates).
{% endalert %}

