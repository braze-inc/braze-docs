---
nav_title: Criação de páginas de destino
article_title: Criação de páginas de destino
description: "Este artigo aborda como criar e personalizar as páginas de destino do Braze com o editor de arrastar e soltar."
page_order: 0
---

# Criação de páginas de destino

> Saiba como criar e personalizar uma página de destino usando o editor de arrastar e soltar, para que você possa aumentar seu público e coletar preferências diretamente no Braze.

## Pré-requisitos

Para acessar o construtor de landing pages, você precisa de [determinadas permissões]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/#prerequisites). Se você não tiver acesso, peça ajuda ao administrador do Braze.

## Criação de uma página de destino

### Etapa 1: Criar um novo rascunho

Acesse **Messaging** > **Landing Pages (** **Mensagens** > **Páginas de destino**) e selecione **Create landing page (Criar página de destino**). Você também pode selecionar o nome de uma landing page existente para duplicá-la ou fazer alterações nela.

\![A seção de páginas de destino no painel do Braze.]({% image_buster /assets/img/landing_pages/landing-pages-homepage.png %})

### Etapa 2: Insira os detalhes da página

Adicione detalhes internos e voltados para o público que o ajudem a organizar, marcar e compartilhar sua página de destino.

#### Detalhes gerais

Digite um nome e uma descrição para a página de destino. Esses detalhes são usados para pesquisar a página em seu espaço de trabalho interno. Eles não ficarão visíveis para seus clientes.

#### Detalhes do site

Configure metatags para personalizar a forma como sua página aparece na guia do navegador e otimize-a para os resultados dos mecanismos de pesquisa. Elas ficarão visíveis para seus clientes.

Sugerimos seguir estas práticas recomendadas:

| Campo | Descrição | Recomendações |
| --- | --- |
| Título do site | O título que é exibido na guia do navegador. | Use até 60 caracteres. |
| Meta descrição | Um snippet de texto que é exibido nos resultados da pesquisa. | Use entre 140 e 160 caracteres.|
| Favicon | O ícone que aparece ao lado do título do site na guia do navegador. | Use uma proporção de 1:1 e um tipo de arquivo compatível com PNG, JPEG ou ICO. |
| URL da página | Esse é o caminho do URL para sua página de destino. Esse valor também é referenciado ao usar [tags líquidas da página de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) que você pode incorporar em uma mensagem para identificar automaticamente quando eles enviam o formulário.| Esse valor deve ser exclusivo em seu espaço de trabalho. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Etapa 3: Personalizar a página

Se ainda não o fez, selecione **Salvar como rascunho**. Para começar a personalizar sua página, selecione **Editar página de destino**. O editor de arrastar e soltar será pré-carregado com um modelo padrão que você pode personalizar para se adequar ao seu caso de uso.

\![Um exemplo de página de destino sendo criada no editor de arrastar e soltar.]({% image_buster /assets/img/landing_pages/template.png %})

O editor usa dois tipos de componentes para a composição da página de destino: blocos básicos e blocos de formulários. Todos os blocos devem ser colocados em uma fileira.

\![A seção "Build" que contém "Rows" e "Form Blocks".]({% image_buster /assets/img/landing_pages/dnd.png %}){: style="max-width:35%;"}

{% tabs %}
{% tab Basic blocks %}

Você pode usar esses blocos para adicionar conteúdo e personalizar o layout da sua página de destino.

| Tipo de bloco   | Descrição |
|-------------|-------------|
| Título       | Um bloco de texto para adicionar um cabeçalho ou título ao seu conteúdo. Útil para estruturar seções e melhorar a legibilidade. |
| Parágrafo   | Um bloco de texto para descrições mais longas ou contexto adicional. Oferece suporte à formatação de rich text. |
| Botão      | Um elemento clicável que direciona os usuários a uma ação específica, como abrir um link ou enviar um formulário. |
| Botão de rádio | Adiciona uma lista de opções das quais os usuários podem selecionar uma. Quando enviado, o perfil do usuário registra o atributo personalizado associado. |
| Imagem       | Um bloco para exibição de imagens. Você pode carregar uma imagem ou fornecer um URL para fazer referência a uma fonte externa. |
| Link        | Um hiperlink no qual os usuários podem clicar para navegar até um URL especificado. Pode ser incorporado ao texto ou autônomo. |
| Espaçador      | Um bloco invisível que adiciona espaçamento vertical entre os elementos para melhorar o layout e a legibilidade. |
| Código personalizado | Um bloco que permite que você insira e execute HTML, CSS ou JavaScript personalizados para personalização avançada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Texto do intervalo

{% multi_lang_include span_text.md %}

{% endtab %}
{% tab Form blocks %}

Você pode usar esses blocos para criar um formulário que vincule os dados enviados pelo usuário ao seu perfil no Braze. Lembre-se de que, se você usar blocos de formulários, também precisará criar uma página de destino adicional para o estado de confirmação.

\![Um bloco de formulário que registra um novo cliente e envia um código de desconto para o e-mail dele.]({% image_buster /assets/img/landing_pages/form.png %}){: style="max-width:70%;"}

| Tipo de bloco     | Descrição |
|---------------|-------------|
| Captura de e-mail | Um campo de formulário para endereços de e-mail. Quando enviado, o endereço de e-mail é adicionado ao perfil do usuário no Braze. |
| Captura de telefone | Um campo de formulário para números de telefone. Quando enviado, o usuário é inscrito no seu grupo de assinatura de SMS ou WhatsApp. |
| Campo de entrada   | Um campo de formulário que suporta atributos padrão (como nome e sobrenome) ou uma cadeia de atributos personalizada de sua escolha. |
| Menu suspenso      | Os usuários podem selecionar um item de uma lista predefinida. Você pode adicionar qualquer string de atributo personalizado à lista. |
| Caixa de seleção      | Se um usuário marcar a caixa, o atributo do bloco será definido como `true`. Se não estiver marcado, seu atributo será definido como `false`. |
| Grupo de caixas de seleção| Os usuários podem selecionar entre várias opções apresentadas. Os valores são definidos ou adicionados a um atributo personalizado de matriz definida. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Depois de criar uma página de destino com um formulário, certifique-se de incorporar [a tag Liquid da página de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) em sua mensagem. Com essa tag, o Braze pode identificar e atualizar automaticamente os perfis de usuários existentes quando eles enviam o formulário.
{% endalert %}

{% endtab %}
{% endtabs %}

#### Estilos de contêiner de página

Você pode definir estilos a serem aplicados em todos os blocos de componentes relevantes em sua landing page na guia **Contêiner de página**. Esses estilos serão usados em toda a página, exceto quando você os substituir por um bloco específico.

Recomendamos configurar os estilos no nível do contêiner da página antes de personalizar os estilos no nível do bloco. Você também pode adicionar uma imagem de fundo para a página inteira.

\![A seção "Contêiner de página" com opções para personalizar imagens de fundo, cores, detalhes de borda e estilo de conteúdo.]({% image_buster /assets/img/landing_pages/page_container.png %}){: style="max-width:40%;"}

#### Responsivo aos dispositivos do usuário

Você pode tornar sua página de destino responsiva ao tamanho do dispositivo do usuário empilhando colunas verticalmente em telas menores. Para ativar isso, adicione uma coluna à linha que deseja tornar responsiva e, em seguida, ative a opção **Empilhar verticalmente em telas menores** na seção **Personalizar colunas**.

Quando ativado, você também pode inverter as colunas de empilhamento para controlar a ordem vertical do conteúdo de várias colunas em telas menores. Isso faz com que as páginas tenham uma melhor aparência e comportamento em dispositivos móveis sem código personalizado.

A opção "Vertically stack on smaller screens" (Empilhar verticalmente em telas menores) na seção "Customize columns" (Personalizar colunas).]({% image_buster /assets/img/landing_pages/device_responsive_toggle.png %}){: style="max-width:50%;"}

#### Campos opcionais e obrigatórios

Você pode escolher se um campo de formulário é obrigatório ou opcional. Os campos obrigatórios devem ser preenchidos antes que o formulário possa ser enviado. Os campos opcionais podem ser deixados em branco ou não selecionados por um usuário.

Por exemplo, para impor a captura de consentimento antes do envio do formulário, você pode ativar **a entrada de campo obrigatória** para definir uma caixa de seleção como obrigatória com o texto de isenção de responsabilidade apropriado.

\![Um campo de formulário de caixa de seleção com a opção "Campo de entrada obrigatório" selecionada.]({% image_buster /assets/img/landing_pages/lp-optional-required.png %}){: style="max-width:50%;"}

### Etapa 4: Criar uma página de confirmação (opcional)

Se sua página de destino não incluir um formulário, passe para a próxima etapa.

Se sua página de destino incluir um [formulário](#form-blocks), crie uma segunda página de destino para servir como experiência de confirmação. Essa página deve agradecer aos usuários ou fornecer uma próxima etapa após o envio do formulário.

Para vincular a página de confirmação:
- Selecione o botão **Enviar** em seu formulário
- Use a ação **Abrir URL da Web** para criar um link para sua página de confirmação

Se você não incluir uma página de confirmação, os usuários podem não saber que o formulário foi enviado com êxito. Sempre inclua uma experiência de confirmação para concluir a jornada.

{% alert note %}
Se a sua página de confirmação abrir em uma nova guia, um usuário que retornar à página de destino original e reenviar com informações atualizadas poderá substituir o envio anterior, resultando em dados inconsistentes.
{% endalert %}

### Etapa 5: Visualizar a página

Você pode visualizar sua página de destino na guia **Preview (Visualização** ) do editor. Depois de salvar sua página de destino como rascunho, você pode visitar o URL acessando **Landing Pages** e selecionando **Copiar URL** ao lado da página de destino. Você também pode compartilhar o URL com os colaboradores.

\![Uma página de destino com o menu aberto para mostrar a opção "Copiar URL".]({% image_buster /assets/img/landing_pages/copy-url.png %})

Antes de publicar, certifique-se de que:

- Você não excedeu o limite de páginas de destino publicadas do seu plano
- Cada página baseada em formulário é vinculada a uma [página de confirmação](#step-4-create-a-confirmation-page) usando a ação **Abrir URL da Web** 
- Todos os campos obrigatórios da página (como caminho do URL e título) estão completos

Quando estiver pronto, selecione **Publish Landing Page (Publicar página de destino**).

## Uso de modelos

Use modelos de página de destino para criar modelos para suas próximas campanhas. Esses modelos podem ser acessados e gerenciados no editor de landing page e na seção **Modelos** do painel**(Modelos** > **Modelos de landing page**). Os modelos de página de destino exigem um nome e, opcionalmente, uma descrição. 

## Gerenciamento de modelos

Você pode visualizar, arquivar, editar ou duplicar modelos de landing page. Ao editar uma landing page, você também pode salvar sua landing page como modelo, fazer alterações no modelo ou excluir o conteúdo da landing page. 

\![Um menu suspenso com opções para salvar, alterar e excluir uma página de destino.]({% image_buster /assets/img/landing_pages/manage-lp-template.png %}){: style="max-width:60%;"}

## Visualização de análises

Para analisar a eficácia de sua página de destino, vá para **Mensagens** > **Páginas de destino** e selecione uma página de destino que você publicou. Aqui, você pode acompanhar o número de visualizações de página, cliques na página, envios de página e as taxas de envio da sua página de destino.

\![A seção de análise de uma página de destino.]({% image_buster /assets/img/landing_pages/analytics.png %})

## Tratamento de erros de envio de formulários {#handling-form-submission-errors}

Se um usuário tentar enviar um formulário com uma entrada ausente ou sem suporte, ele verá uma mensagem de erro genérica e não poderá enviar.

Causas comuns:

- Os campos obrigatórios são deixados em branco
- Caracteres especiais são usados em entradas de texto
- Uma caixa de seleção obrigatória não está selecionada

As mensagens de erro mostradas aos usuários não podem ser personalizadas. Visualize sua página de destino para confirmar o comportamento do campo antes da publicação. 
