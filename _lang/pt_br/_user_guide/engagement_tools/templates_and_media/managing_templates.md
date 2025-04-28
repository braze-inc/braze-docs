---
nav_title: Gerenciamento de modelos
article_title: Gerenciamento de modelos
page_order: 3

page_type: reference
description: "Este artigo de referência descreve como duplicar e arquivar modelos na seção de modelos e mídias do dashboard da Braze."
tool:
  - Templates
  - Media

---

# Gerenciamento de modelos

> Arquivar ou duplicar modelos pode ajudar a organizá-los e gerenciá-los melhor. Este artigo de referência cobre como arquivar e duplicar modelos na seção **Templates** do dashboard da Braze.

## Duplicação de modelos

### Modelo individual

![][8]{: style="float:right;max-width:15%;margin-left:15px;"}

Para duplicar um modelo individual, selecione o ícone de engrenagem <i class="fas fa-cog"></i> para o modelo individual e selecione **Duplicar** no menu suspenso.
<br><br>

{% alert note %}
Para modelos de [blocos de conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/), uma cópia de rascunho é criada. Para todos os outros modelos, uma nova cópia duplicada é criada automaticamente.
{% endalert %}

### Múltiplos modelos

{% raw %}

Para duplicar vários modelos, selecione a caixa de seleção ao lado do nome de cada modelo. Primeiro, selecione os modelos e depois selecione o botão **Duplicar** que aparece.

Modelos duplicados podem ser encontrados classificando a coluna **Última Edição**. Por padrão, novos modelos serão nomeados `Copy of ORIGINAL_TEMPLATE_NAME`.

{% endraw %}

![GIF que mostra um usuário selecionando dois modelos e clicando em "Duplicar", o que resulta em um total de quatro modelos, classificados pelo tempo em que os modelos foram editados pela última vez.][9]

## Arquivando modelos

![Menu suspenso de configurações expandido mostrando três opções: Editar, Arquivar e Duplicar, com a opção Arquivar destacada.][10]{: style="float:right;max-width:20%;margin-left:15px;"}

Para arquivar um modelo individual, selecione o ícone de configurações na tela de grade do modelo e selecione **Arquivar**. Quando um modelo é arquivado, note os seguintes cenários diferentes:

- Campanhas ativas continuam a usar o modelo arquivado sem qualquer interrupção.
- Rascunhos de campanhas mantêm o conteúdo do modelo arquivado e podem ser editados e lançados.
- Para editar um modelo arquivado, é preciso desarquivá-lo primeiro. Da mesma forma, para usar um modelo arquivado para uma campanha, você deve desarquivar o modelo primeiro.

Para arquivar vários modelos, selecione a caixa de seleção ao lado de cada modelo que você deseja arquivar. Depois de selecionar vários modelos, selecione **Arquivar selecionados**. Você pode encontrar seus **modelos** arquivados selecionando **Arquivados** em **Mostrar** na grade de **modelos**.

![Seção de Modelos de E-mail Salvos Drop & Drop que mostra dois modelos selecionados: Experimente o modelo Premium e Bem-vindo modelo. O botão "Arquivar selecionados" está destacado pelo usuário.][11]

{% alert important %}
O arquivamento não está disponível atualmente para [modelos de link]({{site.baseurl}}/user_guide/message_building_by_channel/email/link_templates/#link-templates).
{% endalert %}

[10]: {% image_buster /assets/img/template_archive_cog.png %}
[11]: {% image_buster /assets/img/archive_multiple_template.png %}
[8]: {% image_buster /assets/img/template_duplicate_cog.png %}
[9]: {% image_buster /assets/img/duplicate_multiple_template.gif %}