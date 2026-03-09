## Usando blocos de editor de mensagem no app

Os blocos de editor estão localizados na seção **Construir** para mensagens no app. Para usá-los, arraste um bloco do editor para dentro de uma coluna. Ele se ajustará automaticamente à largura da coluna. Cada bloco do editor tem suas próprias configurações, como o controle granular do preenchimento. O painel do lado direito muda automaticamente para um painel de propriedades do elemento de conteúdo selecionado.

## Tipos

A tabela a seguir descreve como você pode usar cada tipo de bloco de editor.

| Nome | Descrição |
| --- | --- |
| Título | Insere um texto de título na mensagem. |
| Parágrafo | Insere um texto de parágrafo na mensagem. |
| Botão | Adiciona um botão padrão. As propriedades desse bloco permitem a edição, a configuração de links e a análise de dados de registro. |
| Botão de opção | Adiciona uma lista de opções das quais os usuários podem selecionar uma. Quando enviado, o perfil do usuário registra o atributo personalizado associado, que deve ser uma string para ser salvo. Atributos personalizados com outros tipos de dados não são salvos no perfil do usuário. |
| Imagem | Insere uma imagem da [biblioteca de mídia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). |
| Link | Insere um hyperlink que os usuários podem clicar para navegar para uma URL especificada. Pode ser incorporado dentro do texto ou de forma independente. |
| Espaçador | Adiciona espaço ou preenchimento entre outros blocos. |
| Código personalizado | Insere e executa HTML, CSS ou JavaScript personalizados para personalização avançada.  |
| Captura de telefone | Insere um campo de formulário para números de telefone. Quando enviado, o usuário é inscrito no grupo de [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) ou [inscrições do WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/). |
| Captura de e-mail | Insere um campo de formulário para endereços de e-mail. Quando enviado, o endereço de e-mail é adicionado ao perfil desse usuário no Braze. |
| Menu suspenso      | Insere um dropdown com uma lista pré-definida de itens dos quais os usuários podem selecionar um. Você pode adicionar quaisquer strings de atributos personalizados à lista. |
| Caixa de seleção      | Insere uma caixa de seleção. Se o usuário marcar a caixa, o atributo do bloco é definido como `true`. Se deixado desmarcado, seu atributo é definido como `false`. |
| Grupo de caixas de seleção| Os usuários podem selecionar entre várias opções apresentadas. Os valores são definidos ou adicionados a um atributo personalizado de array definido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Propriedades

Os detalhes das propriedades de cada bloco de editor são fornecidos nas tabelas a seguir.

### Título e parágrafo

| Propriedade | Descrição |
| --- | --- |
| Família da fonte | O estilo da fonte para o texto |
| Peso da fonte | Determina a espessura do texto |
| Tamanho da fonte | Determina o tamanho do texto |
| Altura da linha | Modifica a distância entre as linhas de texto |
| Espaçamento entre as letras | Modifica a distância entre cada caractere |
| Alinhamento de texto | Move o texto para ser alinhado à esquerda, ao centro, à direita ou justificado |
| Cor do texto | Modifica a cor do texto |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Botão

| Propriedade | Descrição |
| --- | --- |
| Largura do botão | Modifica a largura do botão para ser automática ou manual |
| Família da fonte | Este é o estilo da fonte para o texto |
| Peso da fonte | Determina a espessura do texto |
| Tamanho da fonte | Determina o tamanho do texto |
| Espaçamento entre as letras | Modifica a distância entre cada caractere |
| Alinhamento do botão | Move o botão para ser alinhado à esquerda, ao centro ou à direita |
| Cor do texto do botão | Modifica a cor do texto no botão |
| Cor de fundo | Modifica a cor do fundo do botão |
| Estilo da borda | Determina o estilo da borda do botão | 
| Raio da borda | Determina o quão arredondados você deseja que sejam os cantos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Imagem

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

| Propriedade | Descrição |
| --- | --- |
| URL | O endereço hospedado para a imagem |
| Alinhamento | Move a imagem para ser alinhada à esquerda, ao centro ou à direita |
| Cor de fundo | Modifica a cor do fundo da imagem |
| Estilo da borda | Determina o estilo da borda da imagem | 
| Raio da borda | Determina quão arredondados você gostaria que os cantos da imagem fossem |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link

| Propriedade | Descrição |
| --- | --- |
| Família da fonte | Este é o estilo da fonte para o texto |
| Peso da fonte | Determina a espessura do texto |
| Espaçamento entre as letras | Modifica a distância entre cada caractere |
| Cor do texto | Modifica a cor do texto |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Espaçador

| Propriedade | Descrição |
| --- | --- |
| Cor de fundo | Modifica a cor de fundo do espaçador |
| Altura | Modifica a altura do espaçador. Você também pode modificar isso usando as alças de redimensionamento no espaçador. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Código personalizado

| Propriedade | Descrição |
| --- | --- |
| Código personalizado | Permite adicionar, editar ou excluir HTML, CSS e JavaScript de uma mensagem no app. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Captura de telefone

| Propriedade | Descrição |
| --- | --- |
| Grupo de inscrições | O [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) ou [grupo de inscrições do WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/) ao qual o usuário será inscrito ao coletar seu número de telefone, com a opção de coletar números de todos os países |
| Alinhamento de texto | Move o texto para ser alinhado à esquerda, ao centro, à direita ou justificado |
| Texto do espaço reservado | Um número de telefone de exemplo para exibir |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Captura de e-mail

| Propriedade | Descrição |
| --- | --- |
| Família da fonte | O estilo da fonte para o texto |
| Peso da fonte | Determina a espessura do texto |
| Tamanho da fonte | Determina o tamanho do texto |
| Altura da linha | Modifica a distância entre as linhas de texto |
| Cor do texto | Modifica a cor do texto |
| Espaçamento entre as letras | Modifica a distância entre cada caractere |
| Alinhamento de texto | Move o texto para ser alinhado à esquerda, ao centro, à direita ou justificado |
| Texto do espaço reservado | Um endereço de e-mail de exemplo para exibir |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Ações

Você pode atribuir uma ação que ocorre quando um usuário toca em um botão, link ou imagem na mensagem. Você também pode usar [Liquid]({{site.baseurl}}/liquid/) para personalizar as ações. Detalhes para as ações de cada bloco de editor são fornecidos nas tabelas a seguir.

### Botão

| Ação | Descrição |
| --- | --- |
| Enviar formulário quando o botão for clicado | Envia o formulário e executa o comportamento ao clicar selecionado. Desative esta opção para executar apenas o comportamento ao clicar. |
| Defina comportamentos específicos para cada plataforma | Personaliza o comportamento do botão para cada plataforma separadamente. |
| Comportamento ao clicar | Determina a ação quando o usuário clica no botão, como fechar a mensagem, abrir a URL da web, fazer deeplinking em uma página específica do app, ir para outra página ou [requesting push permission]({{site.baseurl}}/push_primer/). |
| Registre atributos ou eventos personalizados | Determina se clicar no botão atualizará o perfil do usuário com dados personalizados. Você também pode selecionar o identificador para relatórios. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Imagem

Para especificações de imagem, consulte nossas [in-app message image specifications]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/image_specs/#in-app-messages).

| Ação | Descrição |
| --- | --- |
| Texto alternativo | A cópia escrita que aparece no lugar de uma imagem se a imagem não for carregada. Leitores de tela anunciam texto alternativo para explicar imagens, então use uma linguagem simples para fornecer informações-chave sobre uma imagem. |
| Enviar formulário quando a imagem for clicada | Envia o formulário e executa o comportamento ao clicar selecionado. Desative esta opção para executar apenas o comportamento ao clicar. |
| Defina comportamentos específicos para cada plataforma | Personaliza o comportamento da imagem para cada plataforma separadamente. |
| Comportamento ao clicar | Determina a ação quando o usuário clica na imagem, como fechar a mensagem, abrir a URL da web, fazer deeplinking em uma página específica do app, ir para outra página ou [requesting push permission]({{site.baseurl}}/push_primer/). |
| Registre atributos ou eventos personalizados | Determina se clicar na imagem atualizará o perfil do usuário com dados personalizados. Você também pode selecionar o identificador para relatórios. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link

| Ação | Descrição |
| --- | --- |
| URL | O hyperlink para navegar para |
| Identificador para relatório | Determina qual identificador é usado para relatórios |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

