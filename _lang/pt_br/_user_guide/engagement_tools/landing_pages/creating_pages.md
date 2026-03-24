---
nav_title: Criar landing pages
article_title: Criar Landing Pages
description: "Este artigo aborda como criar e personalizar as landing pages do Braze com o editor de arrastar e soltar."
page_order: 0
---

# Criar landing pages

> Aprenda a criar e personalizar uma landing page usando o editor de arrastar e soltar, para que você possa aumentar seu público e coletar preferências diretamente no Braze.

## Pré-requisitos

Para acessar o construtor de landing pages, você precisa de [certas permissões]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/#prerequisites). Se você não tiver acesso, peça ajuda ao seu administrador do Braze.

## Criando uma landing page

### Etapa 1: Criar um novo rascunho

Acessar **Envio de mensagens** > **Landing page**, então selecione **Criar landing page**. Você também pode selecionar o nome de uma landing page existente para duplicar ou fazer alterações.

![A seção de landing pages no painel do Braze.]({% image_buster /assets/img/landing_pages/landing-pages-homepage.png %})

### Etapa 2: Insira os detalhes da página

Adicione detalhes internos e públicos que ajudem a organizar, brandear e compartilhar sua landing page.

#### Detalhes gerais

Digite um nome e uma descrição para a landing page. Esses detalhes são usados para buscar a página em seu espaço de trabalho interno. Eles não serão visíveis para seus clientes.

#### Detalhes do site

Configure metatags para personalizar a forma como sua página aparece na guia do navegador e otimize-a para os resultados dos mecanismos de pesquisa. Elas ficarão visíveis para seus clientes.

Sugerimos seguir estas práticas recomendadas:

| Campo | Descrição | Recomendações |
| --- | --- |
| Título do site | O título que é exibido na guia do navegador. | Use até 60 caracteres. |
| Metadescrição | Um snippet de texto que é exibido nos resultados da pesquisa. | Use entre 140 e 160 caracteres.|
| Favicon | O ícone que aparece ao lado do título do site na guia do navegador. | Use uma proporção de 1:1 e um tipo de arquivo compatível com PNG, JPEG ou ICO. |
| URL da página | Este é o caminho da URL para sua landing page. Este valor também é referenciado ao usar [tags liquid de landing page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) que você pode incorporar em uma mensagem para identificar automaticamente quando eles enviam seu formulário.| Este valor deve ser único em seu espaço de trabalho. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Etapa 3: Personalize a página

Se você ainda não fez isso, selecione **Salvar como rascunho**. Para começar a personalizar sua página, selecione **Editar landing page**. O editor de arrastar e soltar será pré-carregado com um modelo padrão que você pode personalizar para se adequar ao seu caso de uso.

![Um exemplo de landing page sendo criada no editor de arrastar e soltar.]({% image_buster /assets/img/landing_pages/template.png %})

O editor usa dois tipos de componentes para a composição da landing page: blocos básicos e blocos de formulário. Todos os blocos devem ser colocados em uma fileira.

![A seção 'Construir' contendo 'Linhas' e 'Blocos de Formulário'.]({% image_buster /assets/img/landing_pages/dnd.png %}){: style="max-width:35%;"}

{% tabs %}
{% tab Basic blocks %}

Você pode usar esses blocos para adicionar conteúdo e personalizar o layout da sua landing page.

| Tipo de Bloco   | Descrição |
|-------------|-------------|
| Título       | Um bloco de texto para adicionar um cabeçalho ou título ao seu conteúdo. Útil para estruturar seções e melhorar a legibilidade. |
| Parágrafo   | Um bloco de texto para descrições mais longas ou contexto adicional. Suporta formatação de texto rico. |
| Botão      | Um elemento clicável que direciona os usuários para uma ação específica, como abrir um link ou enviar um formulário. |
| Botão de opção | Adiciona uma lista de opções das quais os usuários podem selecionar uma. Quando enviado, o perfil do usuário registra o atributo personalizado associado. |
| Imagem       | Um bloco para exibir imagens. Você pode fazer upload de uma imagem ou fornecer uma URL para referenciar uma fonte externa. |
| Link        | Um hyperlink que os usuários podem clicar para navegar até uma URL especificada. Pode ser incorporado dentro do texto ou ser independente. |
| Espaçador      | Um bloco invisível que adiciona espaçamento vertical entre elementos para melhorar o layout e a legibilidade. |
| Código personalizado | Um bloco que permite inserir e executar HTML, CSS ou JavaScript personalizados para personalização avançada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Texto em destaque

{% multi_lang_include span_text.md %}

{% endtab %}
{% tab Form blocks %}

Você pode usar esses blocos para criar um formulário que vincula os dados enviados pelo usuário ao seu perfil no Braze. Tenha em mente que, se você usar blocos de formulário, também precisará criar uma página de destino adicional para o estado de confirmação.

![Um bloco de formulário que registra um novo cliente e envia um código de desconto para o e-mail dele.]({% image_buster /assets/img/landing_pages/form.png %}){: style="max-width:70%;"}

| Tipo de Bloco     | Descrição |
|---------------|-------------|
| Captura de e-mail | Um campo de formulário para endereços de e-mail. Quando enviado, o endereço de e-mail é adicionado ao perfil desse usuário no Braze. |
| Captura de telefone | Um campo de formulário para números de telefone. Quando enviado, o usuário é inscrito no seu grupo de inscrições por SMS ou WhatsApp. |
| Campo de entrada   | Um campo de formulário que suporta atributos padrão (como nome e sobrenome) ou uma string de atributo personalizada de sua escolha. |
| Menu suspenso      | Os usuários podem selecionar um item de uma lista pré-definida. Você pode adicionar quaisquer strings de atributos personalizados à lista. |
| Caixa de seleção      | Se um usuário marcar a caixa, o atributo do bloco é definido como `true`. Se não for verificado, seu atributo é definido como `false`. |
| Grupo de caixas de seleção| Os usuários podem selecionar entre várias opções apresentadas. Os valores são definidos ou adicionados a um atributo personalizado de array definido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Após criar uma landing page com um formulário, certifique-se de incorporar seu [tag Liquid da landing page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) na sua mensagem. Com esta tag, a Braze pode identificar e atualizar automaticamente os perfis de usuários existentes quando eles enviam o formulário.
{% endalert %}

{% endtab %}
{% endtabs %}

#### Estilos de contêiner de página

Você pode definir estilos a serem aplicados em todos os blocos de componentes relevantes na sua landing page a partir da guia **Container da página**. Esses estilos serão usados em toda a página, exceto quando você os substituir por um bloco específico.

Recomendamos configurar os estilos no nível do contêiner da página antes de personalizar os estilos no nível do bloco. Você também pode adicionar uma imagem de fundo para a página inteira.

![A seção 'Container da página' com opções para personalizar imagens de fundo, cores, detalhes de borda e estilo de conteúdo.]({% image_buster /assets/img/landing_pages/page_container.png %}){: style="max-width:40%;"}

#### Responsivo a dispositivos de usuários

Você pode tornar sua landing page responsiva ao tamanho do dispositivo de um usuário empilhando colunas verticalmente em telas menores. Para ativar isso, adicione uma coluna na linha que você deseja tornar responsiva e, em seguida, ative **Empilhar verticalmente em telas menores** na seção **Personalizar colunas**.

Quando ativado, você também pode inverter a pilha de colunas para controlar a ordem vertical do conteúdo de várias colunas em telas menores. Isso faz com que as páginas pareçam e se sintam melhores em dispositivos móveis sem código personalizado.

![O botão "Empilhar verticalmente em telas menores" na seção "Personalizar colunas".]({% image_buster /assets/img/landing_pages/device_responsive_toggle.png %}){: style="max-width:50%;"}

#### Campos opcionais e obrigatórios

Você pode escolher se um campo de formulário é obrigatório ou opcional. Campos obrigatórios devem ser preenchidos antes que o formulário possa ser enviado. Campos opcionais podem ser deixados em branco ou não selecionados por um usuário.

Por exemplo, para impor a captura de consentimento antes do envio do formulário, você pode ativar **Campo de entrada obrigatório** para definir uma caixa de seleção como obrigatória com o texto de isenção apropriado.

![Um campo de formulário de caixa de seleção com o botão "Campo de entrada obrigatório" selecionado.]({% image_buster /assets/img/landing_pages/lp-optional-required.png %}){: style="max-width:50%;"}

### Etapa 4: Crie uma página de confirmação (opcional)

Se sua landing page não incluir um formulário, continue para a próxima etapa.

Se sua landing page incluir um [formulário](#form-blocks), crie uma segunda landing page para servir como a experiência de confirmação. Esta página deve agradecer aos usuários ou fornecer um próximo passo após o envio do formulário.

Para vincular a página de confirmação:
- Selecione o botão **Enviar** no seu formulário
- Use a ação **Abrir URL na web** para vincular à sua página de confirmação

Se você não incluir uma página de confirmação, os usuários podem não saber que seu formulário foi enviado com sucesso. Sempre inclua uma experiência de confirmação para completar a jornada.

{% alert note %}
Se sua página de confirmação abrir em uma nova guia, um usuário que retornar à landing page original e reenviar com informações atualizadas pode sobrescrever a submissão anterior, resultando em dados inconsistentes.
{% endalert %}

{% alert important %}
Se você configurar um botão com **Enviar formulário quando o botão for clicado** habilitado e usar **Comportamento ao clicar** para abrir uma URL na web em uma nova guia, o bloqueador de pop-ups embutido do iOS Safari pode impedir que a navegação funcione. Isso ocorre porque o envio do formulário seguido pela abertura de uma nova guia é tratado como um pop-up.<br><br>Para evitar esse problema, configure botões com envio de formulário para abrir a URL resultante na mesma guia (não em uma nova guia). Botões sem envio de formulário podem abrir URLs em novas guias sem problemas.
{% endalert %}

### Etapa 5: Prévia a página

Você pode fazer uma prévia de sua landing page na guia **Preview** (Pré-visualização) do editor. Depois de salvar sua landing page como rascunho, você pode visitar o URL acessando **Landing Pages** e selecionando **Copiar URL** ao lado de sua landing page. Você também pode compartilhar o URL com os colaboradores.

![Uma landing page com o menu aberto para mostrar a opção "Copiar URL".]({% image_buster /assets/img/landing_pages/copy-url.png %})

Antes de publicar, certifique-se:

- Você não excedeu o limite de landing pages publicadas do seu plano
- Cada página baseada em formulário vincula a uma [página de confirmação](#step-4-create-a-confirmation-page) usando a ação **Abrir URL na web**
- Todos os campos obrigatórios da página (como caminho da URL e título) estão completos

Quando estiver pronto, selecione **Publicar landing page**.

## Usando templates

Use templates de landing page para criar templates para suas próximas campanhas. Esses modelos podem ser acessados e gerenciados tanto no editor de landing page quanto na seção **Templates** do dashboard (**Templates** > **Landing Page Templates**). Modelos de landing page requerem um nome e opcionalmente requerem uma descrição. 

## Gerenciamento de modelos

Você pode prévia, arquivar, editar ou duplicar modelos de landing page. Ao editar uma landing page, você também pode salvar sua landing page como um modelo, fazer alterações no modelo ou excluir o conteúdo da landing page. 

![Um dropdown com opções para salvar, alterar e excluir uma landing page.]({% image_buster /assets/img/landing_pages/manage-lp-template.png %}){: style="max-width:60%;"}

## Visualização de análises de dados

Para analisar a eficácia da sua landing page, acesse **Envio de mensagens** > **Landing pages**, então selecione uma landing page que você publicou. Aqui, você pode acompanhar o número de visualizações de página, cliques na página, envios de página e as taxas de envio para sua landing page.

![A seção de análise de dados para uma landing page.]({% image_buster /assets/img/landing_pages/analytics.png %})

## Tratando erros de envio de formulário {#handling-form-submission-errors}

Se um usuário tentar enviar um formulário com entradas ausentes ou não suportadas, verá uma mensagem de erro genérica e não poderá enviar.

Causas comuns:

- Campos obrigatórios estão em branco
- Caracteres especiais são usados em entradas de texto
- Uma caixa de seleção obrigatória não está marcada

Mensagens de erro mostradas aos usuários não podem ser personalizadas. Prévia sua landing page para confirmar o comportamento dos campos antes de publicar. 
