---
nav_title: Suporte de brasagem
article_title: Suporte
description: "Esta página o ajudará a localizar o portal de suporte da Braze para enviar comentários sobre o produto Braze. Esta página só poderá ser acessada por clientes Braze."
alias: /braze_support/
page_type: reference
search_rank: 7
---

# [![Curso de aprendizado Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/the-braze-support-portal/){: style="float:right;width:120px;border:0;" class="noimgborder"} Suporte Braze

## Acesse o portal de suporte

Para entrar em contato com a equipe de suporte da Braze, navegue até o painel de controle da Braze. No painel, selecione **Suporte** > **Obter ajuda**.

\![O menu suspenso "Suporte" com a opção de obter ajuda.]({% image_buster /assets/img_archive/get_help.png %}){: style="max-width:60%;"}

Dependendo das suas permissões Braze e se você for um contato de suporte designado, você será direcionado para o portal de suporte Braze, onde poderá enviar e rastrear casos, ou para o nosso formulário de suporte padrão. Se não tiver certeza de que é um contato de suporte da Braze, entre em contato com o administrador da Braze, o gerente de sucesso da Braze ou o proprietário da conta da sua empresa.

## Adição de contatos de suporte designados

Os contatos de suporte designados podem acessar todos os casos de suporte da sua empresa, independentemente de quem os enviou. É possível definir usuários como contatos de suporte designados diretamente na página **Editar usuário**. 

1. Vá para **Configurações** > **Usuários da empresa** e, em seguida, procure o usuário pelo nome ou endereço de e-mail.
2. Selecione o nome do usuário ou passe o mouse sobre a linha do nome do usuário para exibir um menu. 
3. No menu, selecione **Editar** para ser redirecionado para a página **Editar usuário**.
4. Marque a caixa de seleção **Definir este usuário como um Contato de Suporte Designado para o Portal de Suporte Braze**.

A caixa de seleção para definir um usuário como um contato de suporte designado.]({% image_buster /assets/img_archive/designated_support_contact.png %}){: style="max-width:70%;"}

### Obtenção de acesso

Depois que um usuário for designado como um contato de suporte, o portal de suporte do Braze enviará a esse usuário um e-mail de boas-vindas com instruções para configurar seu acesso.

## Forneça capturas de tela do console do desenvolvedor

Ao se comunicar com o suporte, talvez seja necessário acessar o console do desenvolvedor para fornecer informações adicionais:
- Cromado
  1. Clique com o botão direito do mouse na página da Web e selecione **Inspecionar**.
  2. Selecione a guia **Console** na janela que se abre.
  3. Faça uma captura de tela da guia do console.<br><br>
- Firefox
  1. Clique com o botão direito do mouse na página da Web e selecione **Inspecionar elemento**.
  2. Selecione a guia **Console** na janela que se abre.
  3. Faça uma captura de tela da guia do console.<br><br>
- Safári
  1. Vá para o Safari na barra de menus na parte superior da tela e selecione **Preferências**.
  2. Selecione **Avançado** e marque a caixa de seleção ao lado de **Mostrar menu Desenvolver na barra de menus**. Em seguida, você pode sair da janela.
  3. Clique com o botão direito do mouse na página da Web e selecione **Inspecionar elemento**.
  4. Selecione a guia **Console** na janela que se abre.
  5. Faça uma captura de tela da guia do console.

## Práticas recomendadas para o envio de um caso de suporte

### Forneça o máximo de informações possível

Quanto mais insights você puder oferecer, melhor. Inclua detalhes específicos como o espaço de trabalho, o URL da campanha ou do segmento e quaisquer IDs externas relevantes. Isso pode nos ajudar a solucionar seu problema com mais eficiência.

### Forneça uma amostra de usuários

Compartilhe uma amostragem de usuários em vez de todo o segmento afetado. O fornecimento de um número menor de usuários nos ajuda a restringir nosso escopo e acelerar nossas investigações.

### Anexar registros de rede (registros HAR)

Se você entrar em contato com o suporte, será útil pedir ao usuário afetado que colete logs de rede (logs HAR) do navegador enquanto o problema ocorre. Isso exibirá as solicitações de rede entre o navegador e o servidor para os componentes individuais de uma página da Web, bem como o painel do Braze que o usuário está tentando abrir.

Peça para o usuário afetado fazer o seguinte:

1. Abra suas ferramentas de desenvolvedor. Se estiver usando o Chrome, isso pode ser feito usando o atalho de teclado `option` + `⌘` + `J` (no macOS). Se estiver usando o Windows ou o Linux, isso pode ser feito usando o atalho `shift` + `CTRL` + `J`.
2. Selecione **Rede** > **Fetch/XHR** ou **XHR**.
3. Faça uma gravação ou captura de tela mostrando o **nome**, o **status**, o **tamanho** e **a hora** dos elementos.<br><br>\![A guia "Fetch/XHR" em um navegador Chrome.]({% image_buster /assets/img/network_xhr.png %}){: style="max-width:60%;"}

Em seguida, anexe a gravação ou a captura de tela do usuário ao tíquete de suporte. Essas informações podem ajudar na investigação do Support.

### Esclarecer o comportamento esperado em relação ao real

Conte-nos o que você esperava e o que realmente aconteceu. Isso pode nos ajudar a restringir as possíveis causas do problema.

### Anexe imagens relevantes

Considere a possibilidade de anexar uma captura de tela para ilustrar o problema. O fornecimento dessas imagens pode ajudar significativamente a entender o problema e acelerar o processo de resolução.

### Avaliar o impacto

Selecione o nível de gravidade apropriado para nos ajudar a atribuir os recursos certos para resolver o problema. 

{% alert important %}
Marcar um problema como "Crítico" significa que sua instância de produção está inativa e todo o trabalho no Braze foi interrompido.
{% endalert %}

## Solução de problemas de acesso

Se você receber um erro ao fazer login no Portal de Suporte Braze, como `Check your entry`, certifique-se de ter seguido o link em seu e-mail de boas-vindas para definir uma senha para o portal. Se você já tiver feito isso ou se já tiver conseguido fazer login no portal, crie um tíquete de suporte.