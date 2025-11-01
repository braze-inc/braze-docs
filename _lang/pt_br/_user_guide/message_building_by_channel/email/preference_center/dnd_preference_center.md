---
nav_title: Centro de preferências de e-mail do tipo arrastar e soltar
article_title: Centro de preferências de e-mail do tipo arrastar e soltar
alias: "/dnd_preference_center/"
description: "Esta página de referência aborda como criar um centro de preferências de e-mail com o editor de arrastar e soltar."
page_order: 2
---

# Crie um centro de preferências de e-mail com o recurso de arrastar e soltar

> Usando o editor de arrastar e soltar, é possível criar e personalizar um centro de preferências para ajudar a gerenciar quais usuários recebem determinados tipos de comunicação. Você pode ter até 100 centros de preferência por espaço de trabalho.

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Etapa 1: Criar um centro de preferências de e-mail

Crie um centro de preferências navegando até **Audience** > **Email Preference Centers**.

Aqui, será exibida uma lista de centros de preferências personalizados. Selecione **Criar novo** para criar um novo centro de preferências ou selecione o nome de um centro existente para fazer alterações.

Uma lista de centros de preferências personalizados com o nome, a descrição, o tipo, o status, a data da última edição e a criação pelo usuário.]({% image_buster /assets/img/preference_center/preference_center1.png %})

## Etapa 2: Nomear o centro de preferências de e-mail

Os nomes dos centros de preferência só podem conter caracteres alfanuméricos, traços ou sublinhados. O nome que você fornecer determinará a sintaxe da tag Liquid gerada. 

Essa Liquid tag pode ser incluída em qualquer campanha de e-mail de saída ou nas etapas do Canvas e direcionará os usuários para o centro de preferências.

\![Um exemplo de Liquid para um centro de preferências.]({% image_buster /assets/img/preference_center/preference_center2.png %})

## Etapa 3: Adicionar grupos de assinaturas ao centro de preferências

Selecione **Launch Editor** para começar a projetar seu centro de preferências no editor de arrastar e soltar.

### Definir grupos de assinaturas disponíveis

Para determinar quais grupos de assinatura devem ser exibidos no centro de preferências, selecione o botão **\+ Adicionar grupos de assinatura** para abrir um modal em que os grupos de assinatura desejados podem ser selecionados. Após a seleção, selecione o botão **Add Subscription Groups (Adicionar grupos de assinatura** ) para adicioná-los ao centro de preferências.

Você pode configurar ainda mais os grupos de assinatura selecionados selecionando o bloco inteligente e ajustando as propriedades do bloco.
- Ajustar a ordem dos grupos de assinatura
- Adicionar ou remover grupos de assinatura adicionais
- Incluir descrições
- Adicione ou remova a caixa de seleção **Subscribe to all (Assinar para todos** ), que inscreverá o usuário em todos os grupos de assinatura mostrados nesse bloco
- Adicione ou remova uma caixa de seleção **Unsubscribe from all (Cancelar assinatura de todos** ) que cancelará a assinatura do usuário de todos os grupos de assinatura mostrados nesse bloco

Exemplo de uma central de preferências com as opções de assinar todas as mensagens, marketing, boletins informativos e e-mails semanais, ou cancelar a assinatura de todos.]({% image_buster /assets/img/preference_center/preference_center3.png %}){: style="max-width:38%;"}\![]({% image_buster /assets/img/preference_center/preference_center4.png %}){: style="max-width:45%;"}

O botão **Cancelar inscrição de todos** na parte inferior do modelo não é removível e cancelará [globalmente a inscrição]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) do usuário no recebimento de mensagens de e-mail.

## Etapa 4: Personalize o centro de preferências usando o editor de arrastar e soltar

### Definir estilos comuns

Você pode definir determinados estilos a serem aplicados em todos os blocos relevantes em seu centro de preferências na guia **Common Styles (Estilos comuns** ). Os estilos definidos nesta seção são usados em toda a sua mensagem, exceto quando você os substitui em um bloco específico. Para facilitar a experiência de design, recomendamos configurar os estilos no nível da página antes de personalizar os estilos no nível do bloco.

\![Um exemplo de configurações de estilo comuns para texto, botões e links.]({% image_buster /assets/img/preference_center/preference_center5.png %}){: style="max-width:45%;"}

{% alert tip %}
Para retornar aos estilos comuns, selecione o botão "X" nas propriedades de blocos individuais. Em seguida, selecione o contêiner da mensagem, o botão "X" da mensagem ou o plano de fundo do editor.
{% endalert %}

## Componentes do centro de preferências do tipo arrastar e soltar

O editor de arrastar e soltar usa dois componentes principais para tornar a composição do centro de preferências rápida e fácil: linhas e blocos. Todos os blocos devem ser colocados em uma fileira.

{% tabs %}
{% tab Rows %}

As linhas são unidades estruturais que definem a composição horizontal de uma seção da mensagem usando células.

Opção para selecionar o tipo de linha em sua mensagem.]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

Quando uma linha é selecionada, é possível adicionar ou remover o número de colunas necessárias na seção Personalização de colunas para colocar diferentes elementos de conteúdo lado a lado. Você também pode deslizar para ajustar o tamanho das colunas existentes.

Opções para personalizar as propriedades da coluna, incluindo a cor do plano de fundo, o estilo da borda, o raio da borda e o preenchimento.]({% image_buster /assets/img/preference_center/preference_center7.png %}){: style="max-width:45%;"}

Como prática recomendada, formate suas propriedades de linha e coluna antes de formatar os blocos dentro das linhas. Você pode ajustar o espaçamento e o alinhamento em muitos lugares, portanto, começar da base facilita a edição à medida que você avança.

{% endtab %}
{% tab Blocks %}

Os blocos representam diferentes tipos de conteúdo que você pode usar em sua mensagem. Arraste uma dentro de um segmento de linha existente, que se ajustará automaticamente à largura da célula.

Opção para selecionar blocos, incluindo título, parágrafo, botão, imagem e espaçador.]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

Cada bloco tem suas próprias configurações, como o controle granular do preenchimento. O painel do lado direito muda automaticamente para um painel de estilo para o elemento de conteúdo selecionado. Para obter mais informações, consulte [Propriedades do bloco do editor]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/).

Se estiver usando o bloco Código personalizado no seu centro de preferências, os quadros embutidos podem não ser gerados no código personalizado quando entregues aos usuários.

{% endtab %}
{% endtabs %}

## Etapa 5: Personalize sua página de confirmação

Não se esqueça de personalizar a página de confirmação! Você pode editar essa página selecionando **Confirmation Page (Página de confirmação** ) na parte superior da janela do editor de arrastar e soltar. Essa página será exibida aos usuários depois de atualizarem suas preferências usando o centro de preferências. Os mesmos recursos de estilo acima também se aplicam a essa página.

\![Um exemplo de página de confirmação para comunicar que as preferências do usuário foram atualizadas.]({% image_buster /assets/img/preference_center/preference_center9.png %}){: style="max-width:65%;"}

## Etapa 6: Visualize e inicie seu centro de preferências

Você pode visualizar o centro de preferências selecionando a guia **Preview (Visualizar** ) no editor. No entanto, a funcionalidade de teste está desativada. Depois de editar o centro de preferências, você pode fechar o editor selecionando o botão **Done (Concluído** ).

Você verá uma visualização do centro de preferências e da página de confirmação. Selecione **Save as Draft (Salvar como rascunho** ) para retornar a esse centro de preferências mais tarde ou, se estiver satisfeito, selecione **Launch Preference Center (Iniciar centro de preferências**).

Ao iniciar o centro de preferências, você será solicitado a confirmar o nome, pois ele não poderá ser editado após o lançamento. Depois que você confirmar o nome, o centro de preferências será iniciado e estará pronto para uso.

## Usando o centro de preferências

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

Para colocar um link para o centro de preferências em seus e-mails, copie a tag Liquid do centro de preferências desejado selecionando o ícone **Copy Liquid**.

\![A opção Copiar líquido na linha de um centro de preferências.]({% image_buster /assets/img/preference_center/preference_center10.png %}){: style="max-width:75%;"}

Adicione a tag Liquid ao local desejado em seu e-mail, da mesma forma que [os URLs de cancelamento de assinatura]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#adding-a-custom-unsubscribe-link) são inseridos.

## Tratamento de erros

Se ocorrer um erro quando o usuário selecionar **Salvar** em um centro de preferências, será apresentada a seguinte mensagem de erro padrão, que não pode ser personalizada ou estilizada no editor. No entanto, a localização das mensagens de erro ainda é compatível com essas páginas. 

\![Um erro informando "Houve um problema ao salvar suas preferências. Por favor, tente novamente".]({% image_buster /assets/img/preference_center/preference_center11.png %}){: style="max-width:55%;"}

