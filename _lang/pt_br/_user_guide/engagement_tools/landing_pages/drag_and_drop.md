---
nav_title: Editor de arrastar e soltar
article_title: Criação de landing pages do tipo arrastar e soltar
description: "Este artigo aborda como criar e personalizar as landing pages do Braze com o editor de arrastar e soltar."
page_order: 0
alias: /landing_pages/drag_and_drop/
---

# Landing pages de arrastar e soltar

> Usando o editor de arrastar e soltar, você pode criar e personalizar uma landing page para aumentar seu público e coletar preferências diretamente no Braze.

{% alert important %}
As landing pages estão atualmente em acesso antecipado. Há um limite de cinco landing pages por empresa. As sessões de usuário final registradas nas landing pages contam para o cálculo de Usuários ativos mensais (MAU).
{% endalert %}

## Criação de uma landing page (arrastar e soltar)

### Etapa 1: Crie uma landing page

Acesse **Envio de mensagens** > **Landing Pages** e selecione **Criar landing page** ou selecione o nome de uma **landing page** existente para duplicá-la ou fazer alterações nela.

![A página inicial "Landing Pages".][2]{: style="max-width:90%;"}

### Etapa 2: Configure os detalhes de sua landing page

#### Detalhes gerais

O nome e a descrição da landing page são usados para pesquisar a página em seu espaço de trabalho interno. Eles não serão visíveis para seus clientes.

#### Detalhes do site

Configure metatags para personalizar a forma como sua página aparece na guia do navegador e otimize-a para os resultados dos mecanismos de pesquisa. Elas ficarão visíveis para seus clientes.

Sugerimos seguir estas práticas recomendadas:

| Detalhes | Descrição | Recomendações |
| --- | --- |
| Título do site | O título que é exibido na guia do navegador. | Use até 60 caracteres. |
| Descrição da tabela | Um snippet de texto que é exibido nos resultados da pesquisa. | Use entre 140 e 160 caracteres.|
| Favicon | O ícone que aparece ao lado do título do site na guia do navegador. | Use uma proporção de 1:1 e um tipo de arquivo compatível com PNG, JPEG ou ICO. |
| Identificador de URL | Esse é o link em que os usuários clicarão para navegar até sua landing page. | Isso deve ser exclusivo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Etapa 3: Personalize sua landing page

Selecione **Launch Editor** para começar a projetar sua landing page no editor de arrastar e soltar. O editor será pré-carregado com um modelo padrão que pode ser personalizado para se adequar ao seu caso de uso.

![Modelo de landing page com um formulário para inscrever-se como cliente.][8]{: style="max-width:90%;"}

#### Blocos de arrastar e soltar

O editor usa dois tipos de componentes para a composição da landing page: linhas e blocos. Todos os blocos devem ser colocados em uma fileira.

![A seção do editor "Compilação" que contém "Linhas" e "Blocos de formulário".][4]{: style="max-width:30%;"}

#### Bloco de formulários

Use vários componentes de bloco de formulário para registrar atributos personalizados e padrão do perfil e eventos personalizados. O bloco de formulário de campo de entrada pode registrar atributos padrão e personalizados para seus usuários, e os blocos de formulário de captura de telefone e captura de e-mail podem capturar os campos de telefone e e-mail para os envios de formulário dos seus usuários. As ações do botão podem ser registradas como atributos personalizados, eventos personalizados ou ambos no envio do formulário. 

Se você incluir um bloco de formulário, deverá incluir pelo menos um botão com o botão de alternância ativado para **Enviar formulário quando o botão for clicado**. Você também deve criar outra landing page para o [estado de confirmação](#confirmation-state).

![Um bloco de formulário que registra um novo cliente e envia um código de desconto para o e-mail dele.][5]{: style="max-width:70%;"}

#### Estilos de contêiner de página

É possível definir estilos a serem aplicados em todos os blocos de componentes relevantes em sua landing page na guia **Contêiner de página**. Esses estilos serão usados em toda a página, exceto quando você os substituir por um bloco específico.

Recomendamos configurar os estilos no nível do contêiner da página antes de personalizar os estilos no nível do bloco. Você também pode adicionar uma imagem de fundo para a página inteira.

![O contêiner de página com opções para personalizar imagens de fundo, cores, detalhes de borda e estilo de conteúdo.][6]{: style="max-width:30%;"}

### Etapa 4: Prévia de sua landing page

Você pode fazer uma prévia de sua landing page na guia **Preview** (Pré-visualização) do editor. Depois de salvar sua landing page como rascunho, você pode visitar o URL acessando **Landing Pages** e selecionando **Copiar URL** ao lado de sua landing page. Você também pode compartilhar o URL com os colaboradores.

![Uma landing page com o menu aberto para mostrar a opção "Copy URL" (Copiar URL).][7]{: style="max-width:90%;"}

Quando estiver satisfeito com a landing page, selecione **Publish Landing Page (Publicar landing page**).

{% alert important %}
O identificador de URL não pode ser editado após a publicação da landing page.
{% endalert %}

## Criação de uma landing page de confirmação {#confirmation-state}

Se você incluir um [formulário](#form-block) em sua landing page, não se esqueça de criar uma landing page de confirmação. Crie outra landing page para o estado de confirmação e, em seguida, adicione o link no campo **Abrir URL** da **Web** do botão que envia o formulário.

## Links para sua landing page

Você pode incluir um link para a landing page em qualquer canal, copiando e colando o link em uma mensagem do Braze ou em uma campanha de mensagens em redes sociais.

## Tratamento de erros de envio de formulários

Se um usuário inserir um valor de formulário inválido (como caracteres especiais não aceitos), ele verá um indicador de erro genérico que não pode ser personalizado e não poderá enviar o formulário. Você pode ver o comportamento do erro na landing page de prévia.

## Mesclar usuários criados a partir de sua landing page

Cada envio de formulário em uma landing page criará um novo perfil de usuário anônimo no Braze. Se já existir um usuário com o mesmo endereço de e-mail, é possível mesclar o novo perfil de usuário ao perfil existente usando o endpoint [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merging-unidentified-user). Para saber mais sobre as diferentes maneiras de desduplicar usuários no Braze, consulte [Duplicar usuários]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users).

A fusão de usuários será tratada automaticamente por meio de uma Liquid tag no futuro. 

## Considerações

O tamanho do corpo da landing page pode ser de até 1 MB.

## Permissões

Você precisa de permissões de administrador ou de todas as seguintes permissões para acessar, criar e publicar landing pages:

- Acessar landing page
- Criar rascunhos de landing page
- Publicar landing page

## Níveis de planos

O número de landing pages publicadas e domínios personalizados que você pode usar depende do seu tipo de plano: gratuito ou pago (incremental).

| Recurso                                                                                                   | Nível gratuito     | Nível pago (incremental)     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| Landing pages publicadas                                                                 | Cinco por empresa | 20 adicionais |
| Domínios personalizados          | Um por empresa | Cinco adicionais |

## Perguntas frequentes

### O que acontece quando um usuário envia suas informações na landing page?

Quando um usuário envia um formulário, um novo perfil de usuário do Braze é criado com os dados de usuários enviados.

### Há algum requisito técnico para publicar uma landing page?

Não, não há requisitos técnicos.

### Existe um editor de HTML para landing pages?

Você pode editar o HTML de uma landing page usando o bloco Custom Code.

### Há relatórios disponíveis para landing pages?

Não, isso não está disponível no momento.

### Posso criar um webhook dentro de uma landing page?

Não, isso não é suportado no momento.

### Quais recursos estão no roteiro das landing pages? {#roadmap}

Planejamos lançar recursos adicionais para landing pages, que estão em desenvolvimento. Isso pode incluir:

* Nova tag Liquid para vincular uma landing page em um canal de envio de mensagens do Braze
* Mesclagem automática de usuários quando uma landing page é enviada por meio de um canal Braze
* Página de relatórios básicos
* Blocos de formulário de arrastar e soltar para caixas de seleção e menus suspensos
* Evento padrão para rastreamento e redirecionamento com base em envios de formulários

Embora esses recursos façam parte de nosso roteiro, eles ainda estão em desenvolvimento, e o Braze não pode garantir que qualquer um ou todos esses recursos serão disponibilizados de forma geral. O acesso a alguns ou todos os recursos planejados para landing pages pode estar sujeito a taxas adicionais.

[1]: {% image_buster /assets/img/landing_pages/homepage.gif %}
[2]: {% image_buster /assets/img/landing_pages/create.png %}
[3]: {% image_buster /assets/img/landing_pages/details.png %}
[4]: {% image_buster /assets/img/landing_pages/dnd.png %}
[5]: {% image_buster /assets/img/landing_pages/form.png %}
[6]: {% image_buster /assets/img/landing_pages/page_container.png %}
[7]: {% image_buster /assets/img/landing_pages/url_handle.png %}
[8]: {% image_buster /assets/img/landing_pages/template.png %}
