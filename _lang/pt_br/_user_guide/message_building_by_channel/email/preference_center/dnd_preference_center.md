---
nav_title: Central de Preferências de e-mail do tipo arrastar e soltar
article_title: Central de Preferências de e-mail do tipo arrastar e soltar
alias: "/dnd_preference_center/"
description: "Esta página de referência aborda como criar uma Central de Preferências de e-mail com o editor de arrastar e soltar."
page_order: 2
---

# Crie uma Central de Preferências de e-mail com o recurso de arrastar e soltar

> Usando o editor de arrastar e soltar, é possível criar e personalizar uma Central de Preferências para ajudar a gerenciar quais usuários recebem determinados tipos de comunicação. Você pode ter até 50 centrais de preferências por espaço de trabalho.

{% multi_lang_include drag_and_drop_access.md variable_name='dnd editors' %}

## Etapa 1: Crie uma Central de Preferências de e-mail

Crie uma Central de  Preferências navegando até **Público** > **Inscrições** > **Central de Preferências de E-mail**.

Aqui, será exibida uma lista de centros de preferências personalizados. Selecione **Create New (Criar novo)** para criar um novo centro de preferências ou selecione o nome de um já existente para fazer alterações.

![Uma lista de Centrais de Preferências personalizadas com o nome, a descrição, o tipo, o status, a data da última edição e a criação pelo usuário.]({% image_buster /assets/img/preference_center/preference_center1.png %})

## Etapa 2: Nomear a Central de Preferências de e-mail

Os nomes das Centrais de Preferências só podem conter caracteres alfanuméricos, traços ou sublinhados. O nome que você fornecer determinará a sintaxe da tag Liquid gerada. 

Essa Liquid tag pode ser incluída em qualquer campanha de envio de e-mail ou etapa do Canva e direcionará os usuários para a central de preferências.

![Um exemplo de Liquid para um centro de preferências.]({% image_buster /assets/img/preference_center/preference_center2.png %})

## Etapa 3: Adicionar grupos de inscrições à Central de Preferências

Selecione **Launch Editor** para começar a projetar sua central de preferências no editor de arrastar e soltar.

### Definir os grupos de inscrições disponíveis

Para determinar quais grupos de inscrições devem ser mostrados na Central de Preferências, selecione o botão **\+ Adicionar grupos de inscrições** para abrir um modal em que os grupos de inscrições desejados podem ser selecionados. Após a seleção, selecione o botão **Add Subscription Groups (Adicionar grupos de inscrições** ) para adicioná-los à Central de Preferências.

Você pode configurar ainda mais os grupos de inscrições selecionados selecionando o bloco inteligente e ajustando as propriedades do bloco.
- Ajuste a ordem dos grupos de inscrições
- Adicionar ou remover grupos de inscrições adicionais
- Inclua descrições
- Adicione ou remova a caixa de seleção **Assinar tudo**, que inscreverá o usuário em todos os grupos de inscrições mostrados nesse bloco
- Adicione ou remova uma caixa de seleção **Cancelar inscrição de todos** que cancelará a inscrição do usuário em todos os grupos de inscrições mostrados nesse bloco

![Um exemplo de uma Central de Preferências com as opções de assinar todas as mensagens, marketing, boletins informativos e e-mails semanais, ou cancelar a inscrição de todos.]({% image_buster /assets/img/preference_center/preference_center3.png %}){: style="max-width:38%;"} ![]({% image_buster /assets/img/preference_center/preference_center4.png %}){: style="max-width:45%;"}

O botão **Cancelar inscrição de todos** na parte inferior do modelo não é removível e cancelará [globalmente a inscrição]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) do usuário no recebimento de qualquer mensagem de e-mail.

## Etapa 4: Personalize a Central de Preferências usando o editor de arrastar e soltar

### Definir estilos comuns

É possível definir determinados estilos a serem aplicados em todos os blocos relevantes em seu centro de preferências na guia **Common Styles (Estilos comuns** ). Os estilos definidos nesta seção são usados em toda a mensagem, exceto quando são substituídos por um bloco específico. Para facilitar a experiência de design, recomendamos configurar os estilos no nível da página antes de personalizar os estilos no nível do bloco.

![Um exemplo de configurações de estilo comuns para texto, botões e links.]({% image_buster /assets/img/preference_center/preference_center5.png %}){: style="max-width:45%;"}

{% alert tip %}
Para retornar aos estilos comuns, selecione o botão "X" nas propriedades de blocos individuais. Em seguida, selecione o contêiner da mensagem, o botão "X" da mensagem ou o plano de fundo do editor.
{% endalert %}

## Componentes da Central de Preferências do tipo arrastar e soltar

O editor de arrastar e soltar usa dois componentes principais para tornar a composição do centro de preferências rápida e fácil: linhas e blocos. Todos os blocos devem ser colocados em uma fileira.

{% tabs %}
{% tab Rows %}

As linhas são unidades estruturais que definem a composição horizontal de uma seção da mensagem usando células.

![Opção para selecionar o tipo de linha em sua mensagem.]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

Quando uma linha é selecionada, é possível adicionar ou remover o número de colunas necessárias na seção Personalização de colunas para colocar diferentes elementos de conteúdo lado a lado. Você também pode deslizar para ajustar o tamanho das colunas existentes.

![Opções para personalizar as propriedades da coluna, incluindo cor de fundo, estilo da borda, raio da borda e preenchimento.]({% image_buster /assets/img/preference_center/preference_center7.png %}){: style="max-width:45%;"}

Como prática recomendada, formate suas propriedades de linha e coluna antes de formatar os blocos dentro das linhas. Você pode ajustar o espaçamento e o alinhamento em muitos lugares, portanto, começar pela base facilita a edição à medida que você acessa.

{% endtab %}
{% tab Blocos %}

Os blocos representam diferentes tipos de conteúdo que podem ser usados em sua mensagem. Arraste uma dentro de um segmento de linha existente, que se ajustará automaticamente à largura da célula.

![Opção para selecionar blocos, incluindo título, parágrafo, botão, imagem e espaçador.]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

Cada bloco tem suas próprias configurações, como o controle granular do preenchimento. O painel do lado direito muda automaticamente para um painel de estilo para o elemento de conteúdo selecionado. Para saber mais, consulte [Propriedades do bloco do editor]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/).

Se estiver usando o bloco Código personalizado na Central de Preferências, os quadros embutidos podem não ser gerados no código personalizado quando entregues aos usuários.

{% endtab %}
{% endtabs %}

## Etapa 5: Personalize sua página de confirmação

Não se esqueça de personalizar a página de confirmação! Você pode editar essa página selecionando **Confirmation Page (Página de confirmação** ) na parte superior da janela do editor de arrastar e soltar. Essa página será exibida aos usuários depois de atualizarem suas preferências usando a Central de Preferências. Os mesmos recursos de estilo acima também se aplicam a essa página.

![Um exemplo de página de confirmação para comunicar que as preferências do usuário foram atualizadas.]({% image_buster /assets/img/preference_center/preference_center9.png %}){: style="max-width:65%;"}

## Etapa 6: Pré-visualize e inicie sua Central de Preferências

Você pode fazer a prévia da Central de Preferências selecionando a guia **Preview (Pré-visualização** ) no editor. No entanto, a funcionalidade de teste está desativada. Depois de editar a Central de Preferências, você pode fechar o editor selecionando o botão **Concluído**.

Você verá uma prévia do centro de preferências e da página de confirmação. Selecione **Salvar como rascunho** para retornar a essa Central de Preferências mais tarde ou, se estiver satisfeito, selecione **Launch Central de Preferências (Iniciar Central de Preferências**).

Ao iniciar a Central de Preferências, você será solicitado a confirmar o nome, pois ele não poderá ser editado após o lançamento. Depois que você confirmar o nome, a Central de Preferências será iniciada e estará pronta para uso.

## Usando a Central de Preferências

{% multi_lang_include preference_center_warning.md %}

Para colocar um link para o centro de preferências em seus e-mails, copie a Liquid tag do centro de preferências desejado selecionando o ícone **Copy Liquid**.

![A opção Copy Liquid na linha de um centro de preferências.]({% image_buster /assets/img/preference_center/preference_center10.png %}){: style="max-width:75%;"}

Adicione a tag Liquid ao local desejado em seu e-mail, da mesma forma que as [URLs de cancelamento de inscrição]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#adding-a-custom-unsubscribe-link) são inseridas.

## Tratamento de erros

Se ocorrer um erro quando o usuário selecionar **Salvar** em uma Central de Preferências, será apresentada a seguinte mensagem de erro padrão, que não pode ser personalizada ou estilizada no editor. No entanto, a localização das mensagens de erro ainda é possível nessas páginas. 

![Um erro de "Houve um problema ao salvar suas preferências. Tente novamente."]({% image_buster /assets/img/preference_center/preference_center11.png %}){: style="max-width:55%;"}

