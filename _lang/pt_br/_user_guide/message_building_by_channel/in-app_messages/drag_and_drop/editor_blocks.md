---
nav_title: Blocos do editor
article_title: "Blocos do editor de mensagens no app"
description: "Este artigo de referência descreve os blocos do editor disponíveis no editor de arrastar e soltar para mensagens no app."
alias: "/editor_blocks_dnd_iam/"
page_order: 5
---

# Bloqueios do editor de mensagens no app

> Os blocos do editor são os vários blocos disponíveis no **editor de arrastar e soltar** na seção **Construção**. Esta seção inclui uma série de blocos que representam os diferentes tipos de conteúdo que podem ser usados na sua mensagem.

## Como usar os blocos do editor

Para usá-los, arraste um bloco do editor para dentro de uma coluna. Ele se ajustará automaticamente à largura da coluna. Cada bloco do editor tem suas próprias configurações, como o controle granular do preenchimento. O painel do lado direito muda automaticamente para um painel de propriedades do elemento de conteúdo selecionado.

### Tipos

A tabela a seguir descreve como você pode usar cada tipo de bloco de editor.

| Nome | Descrição |
| --- | --- |
| Título | Insere um texto de título na mensagem. |
| Parágrafo | Insere um texto de parágrafo na mensagem. |
| Botão | Adiciona um botão padrão. As propriedades desse bloco permitem a edição, a configuração de links e a análise de dados de registro. |
| Botão de opção | Adiciona uma lista de opções das quais os usuários podem selecionar uma. Quando enviado, o perfil do usuário registra o atributo personalizado associado. |
| Imagem | Insere uma imagem da biblioteca de mídia. |
| Link | Insere um hiperlink no qual os usuários podem clicar para navegar até um URL especificado. Pode ser incorporado ao texto ou autônomo. |
| Espaçador | Adiciona espaço ou preenchimento entre outros blocos. |
| Código personalizado | Insere e executa HTML, CSS ou JavaScript personalizados para personalização avançada.  |
| Captura de telefone | Insere um campo de formulário para números de telefone. Quando enviado, o usuário é inscrito no grupo de inscrições do SMS ou do WhatsApp. |
| Captura de e-mail | Insere um campo de formulário para endereços de e-mail. Quando enviado, o endereço de e-mail é adicionado ao perfil do usuário no Braze. |
| Menu suspenso      | Insere um menu suspenso com uma lista predefinida de itens dos quais os usuários podem selecionar um. Você pode adicionar quaisquer strings de atributos personalizados à lista. |
| Caixa de seleção      | Insere uma caixa de seleção. Se o usuário marcar a caixa, a atribuição do bloco será definida como `true`. Se não estiver marcado, sua atribuição será definida como `false`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Ações

Os detalhes das ações de cada bloco do editor são fornecidos nas tabelas a seguir.

### Botão

| Ação | Descrição |
| --- | --- |
| Enviar formulário quando o botão for clicado | Submete o formulário e executa o comportamento ao clicar selecionado. Desative esta opção para executar apenas o comportamento ao clicar. |
| Defina comportamentos específicos para cada plataforma | Personaliza o comportamento do botão para cada plataforma separadamente. |
| Comportamento ao clicar | Determina a ação quando o usuário clica no botão, como fechar a mensagem, abrir o URL da Internet, fazer um link profundo em uma página específica do app, acessar outra página ou solicitar permissão por push. |
| Registre atributos ou eventos personalizados | Determina se, ao clicar no botão, o perfil do usuário será atualizado com dados personalizados. Você também pode selecionar o identificador para o relatório. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Imagem

| Ação | Descrição |
| --- | --- |
| Texto alternativo | A cópia escrita que aparece no lugar de uma imagem se a imagem não for carregada. Os leitores de tela anunciam o texto alternativo para explicar as imagens, portanto, use uma linguagem simples para fornecer informações importantes sobre uma imagem. |
| Enviar formulário quando a imagem for clicada | Submete o formulário e executa o comportamento ao clicar selecionado. Desative esta opção para executar apenas o comportamento ao clicar. |
| Defina comportamentos específicos para cada plataforma | Personaliza o comportamento da imagem para cada plataforma separadamente. |
| Comportamento ao clicar | Determina a ação quando o usuário clica na imagem, como fechar a mensagem, abrir a URL da Internet, fazer um link profundo em uma página específica do app, acessar outra página ou solicitar permissão push. |
| Registre atributos ou eventos personalizados | Determina se clicar na imagem atualizará o perfil do usuário com dados personalizados. Você também pode selecionar o identificador para o relatório. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link

| Ação | Descrição |
| --- | --- |
| URL | O hiperlink para o qual navegar
| Identificador para relatório | Determina qual identificador é usado para o relatório. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Propriedades

Os detalhes das propriedades de cada bloco de editor são fornecidos nas tabelas a seguir.

### Título e parágrafo

| Propriedade | Descrição |
| --- | --- |
| Família da fonte | O estilo da fonte do texto |
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
| Largura do botão | Modifica a largura do botão para que seja automático ou manual |
| Família da fonte | Esse é o estilo da fonte do texto |
| Peso da fonte | Determina a espessura do texto |
| Tamanho da fonte | Determina o tamanho do texto |
| Espaçamento entre as letras | Modifica a distância entre cada caractere |
| Alinhamento do botão | Move o botão para a esquerda, para o centro ou para a direita |
| Cor do texto do botão | Modifica a cor do texto no botão |
| Cor de fundo | Modifica a cor do plano de fundo do botão |
| Estilo da borda | Determina o estilo da borda do botão do botão | 
| Raio da borda | Determina o quão arredondados você deseja que sejam os cantos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Imagem

| Propriedade | Descrição |
| --- | --- |
| URL | O endereço hospedado da imagem |
| Alinhamento | Move a imagem para a esquerda, para o centro ou para a direita |
| Cor de fundo | Modifica a cor do plano de fundo da imagem |
| Estilo da borda | Determina o estilo da borda da imagem | 
| Raio da borda | Determina o quão arredondados você gostaria que fossem os cantos da imagem |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link

| Propriedade | Descrição |
| --- | --- |
| Família da fonte | Esse é o estilo da fonte do texto |
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

### Captura telefônica

| Propriedade | Descrição |
| --- | --- |
| Grupo de inscrições | O grupo de inscrições de SMS ou WhatsApp no qual o usuário será inscrito ao coletar seu número de telefone, com uma opção para coletar números de todos os países |
| Alinhamento de texto | Move o texto para ser alinhado à esquerda, ao centro, à direita ou justificado |
| Texto do espaço reservado | Um número de telefone de espaço reservado a ser exibido |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Captura de e-mail

| Propriedade | Descrição |
| --- | --- |
| Família da fonte | O estilo da fonte do texto |
| Peso da fonte | Determina a espessura do texto |
| Tamanho da fonte | Determina o tamanho do texto |
| Altura da linha | Modifica a distância entre as linhas de texto |
| Cor do texto | Modifica a cor do texto |
| Espaçamento entre as letras | Modifica a distância entre cada caractere |
| Alinhamento de texto | Move o texto para ser alinhado à esquerda, ao centro, à direita ou justificado |
| Texto do espaço reservado | Um endereço de e-mail de espaço reservado a ser exibido |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
