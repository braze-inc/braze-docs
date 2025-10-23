---
nav_title: Criação de landing pages
article_title: Criação de landing pages
description: "Este artigo aborda como criar e personalizar as landing pages do Braze com o editor de arrastar e soltar."
page_order: 0
---

# Criando páginas de destino

> Aprenda a criar e personalizar uma landing page usando o editor de arrastar e soltar, para que você possa aumentar seu público e coletar preferências diretamente no Braze.

## Criando uma landing page

### Etapa 1: Criar um novo rascunho

Acessar **Envio de mensagens** > **Landing page**, então selecione **Criar landing page**. Você também pode clicar no nome de uma landing page existente para duplicá-la ou fazer alterações.

![A seção de landing pages no dashboard do Braze.]({% image_buster /assets/img/landing_pages/landing-pages-homepage.png %})

### Etapa 2: Insira os detalhes da página

#### Detalhes gerais

O nome e a descrição da landing page são usados para pesquisar a página em seu espaço de trabalho interno. Eles não serão visíveis para seus clientes.

#### Detalhes do site

Configure metatags para personalizar a forma como sua página aparece na guia do navegador e otimize-a para os resultados dos mecanismos de pesquisa. Elas ficarão visíveis para seus clientes.

Sugerimos seguir estas práticas recomendadas:

| Detalhes | Descrição | Recomendações |
| --- | --- |
| Título do site | O título que é exibido na guia do navegador. | Use até 60 caracteres. |
| Metadescrição | Um snippet de texto que é exibido nos resultados da pesquisa. | Use entre 140 e 160 caracteres.|
| Favicon | O ícone que aparece ao lado do título do site na guia do navegador. | Use uma proporção de 1:1 e um tipo de arquivo compatível com PNG, JPEG ou ICO. |
| URL da página | Essa é a jornada do URL para sua landing page. Esse valor também é referenciado ao usar [as tags Liquid da landing page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) que podem ser incorporadas em uma mensagem para identificar automaticamente quando o formulário é enviado.| Esse valor deve ser exclusivo em seu espaço de trabalho. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Etapa 3: Personalize a página

Se você ainda não fez isso, selecione **Salvar como rascunho**. Para começar a personalizar sua página, selecione **Editar landing page**. O editor de arrastar e soltar será pré-carregado com um modelo padrão que você pode personalizar para se adequar ao seu caso de uso.

![Um exemplo de landing page sendo criada no editor de arrastar e soltar.]({% image_buster /assets/img/landing_pages/template.png %})

O editor usa dois tipos de componentes para a composição da landing page: [blocos básicos](#basic-blocks) e [blocos de formulário](#form-blocks). Todos os blocos devem ser colocados em uma fileira.

![A seção 'Build' contendo 'Rows' e 'Form Blocks'.]({% image_buster /assets/img/landing_pages/dnd.png %}){: style="max-width:35%;"}

#### Blocos básicos

Você pode usar esses blocos para adicionar conteúdo e personalizar o layout da sua landing page.

| Tipo de bloco   | Descrição |
|-------------|-------------|
| Título       | Um bloco de texto para adicionar um cabeçalho ou título ao seu conteúdo. Útil para estruturar seções e melhorar a legibilidade. |
| Parágrafo   | Um bloco de texto para descrições mais longas ou contexto adicional. Oferece suporte à formatação de rich text. |
| Botão      | Um elemento clicável que direciona os usuários a uma ação específica, como abrir um link ou enviar um formulário. |
| Imagem       | Um bloco para exibição de imagens. Você pode fazer upload de uma imagem ou fornecer um URL para fazer referência a uma fonte externa. |
| Link        | Um hiperlink no qual os usuários podem clicar para navegar até um URL especificado. Pode ser incorporado ao texto ou autônomo. |
| Espaçador      | Um bloco invisível que adiciona espaçamento vertical entre os elementos para melhorar o layout e a legibilidade. |
| Código personalizado | Um bloco que permite que você insira e execute HTML, CSS ou JavaScript personalizados para personalização avançada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Blocos de formulário

Você pode usar esses blocos para criar um formulário que vincula os dados enviados pelo usuário ao seu perfil no Braze. Tenha em mente que, se você usar blocos de formulário, também precisará criar uma página de destino adicional para o estado de confirmação.

![Um bloco de formulário que registra um novo cliente e envia um código de desconto para o e-mail dele.]({% image_buster /assets/img/landing_pages/form.png %}){: style="max-width:70%;"}

| Tipo de bloco     | Descrição |
|---------------|-------------|
| Captura de e-mail | Um campo de formulário para endereços de e-mail. Quando enviado, o endereço de e-mail é adicionado ao perfil do usuário no Braze. |
| Captura de telefone | Um campo de formulário para números de telefone. Quando enviado, o usuário é inscrito no seu grupo de inscrições de SMS ou Whatsapp. |
| Campo de entrada   | Um campo de formulário compatível com atributos padrão (como nome e sobrenome) ou uma string de atributo personalizado de sua escolha. |
| Menu suspenso      | Os usuários podem selecionar um item de uma lista predefinida. Você pode adicionar quaisquer strings de atributos personalizados à lista. |
| Caixa de seleção      | Se um usuário marcar a caixa, a atribuição do bloco será definida como `true`. Se não estiver marcado, sua atribuição será definida como `false`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Depois de criar uma landing page com um formulário, não se esqueça de incorporar [a Liquid tag da landing page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) em sua mensagem. Com essa tag, o Braze pode identificar e atualizar automaticamente os perfis de usuários existentes quando eles enviam o formulário.
{% endalert %}

#### Estilos de contêiner de página

É possível definir estilos a serem aplicados em todos os blocos de componentes relevantes em sua landing page na guia **Contêiner de página**. Esses estilos serão usados em toda a página, exceto quando você os substituir por um bloco específico.

Recomendamos configurar os estilos no nível do contêiner da página antes de personalizar os estilos no nível do bloco. Você também pode adicionar uma imagem de fundo para a página inteira.

![A seção "Contêiner de página" com opções para personalizar imagens de fundo, cores, detalhes de borda e estilo de conteúdo.]({% image_buster /assets/img/landing_pages/page_container.png %}){: style="max-width:30%;"}

### Etapa 4: Crie uma página de confirmação

Se você adicionou um [formulário](#form-block) à sua landing page na etapa anterior, crie uma landing page adicional para o estado de confirmação e, em seguida, adicione o link **Abrir URL** ao botão que envia o formulário. Caso contrário, continue para a próxima etapa.

### Etapa 5: Prévia a página

Você pode fazer uma prévia de sua landing page na guia **Preview** (Pré-visualização) do editor. Depois de salvar sua landing page como rascunho, você pode visitar o URL acessando **Landing Pages** e selecionando **Copiar URL** ao lado de sua landing page. Você também pode compartilhar o URL com os colaboradores.

![Uma landing page com o menu aberto para mostrar a opção "Copy URL" (Copiar URL).]({% image_buster /assets/img/landing_pages/copy-url.png %})

Quando estiver pronto, selecione **Publicar landing page**.

## Tratamento de erros de envio de formulários

Se um usuário inserir um valor de formulário inválido (como caracteres especiais não aceitos), ele verá um indicador de erro genérico que não pode ser personalizado e não poderá enviar o formulário. Você pode ver o comportamento de erro na prévia da landing page.

## Visualização de análises de dados

Para analisar a eficácia da sua landing page, acesse **Envio de mensagens** > **Landing pages**, então selecione uma landing page que você publicou. Aqui, você pode acompanhar o número de visualizações de página, cliques na página, envios de página e as taxas de envio para sua landing page.

![A seção de análise de dados de uma landing page.]({% image_buster /assets/img/landing_pages/analytics.png %})
