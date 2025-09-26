---
nav_title: Rendimento dinâmico
article_title: Rendimento dinâmico
description: "Esse artigo de referência descreve a parceria entre a Braze e a Dynamic Yield. Essa parceria permite que você aproveite o mecanismo de recomendação e segmentação da Dynamic Yield para criar blocos de experiência que podem ser incorporados às mensagens do Braze."
alias: /partners/dynamic_yield/
page_type: partner
search_tag: Partner

---

# Rendimento dinâmico

> [A Dynamic Yield](https://www.dynamicyield.com/), uma empresa da Mastercard, ajuda empresas de todos os setores a oferecer experiências digitais aos clientes que são personalizadas, otimizadas e sincronizadas. Com o [Experience OS](http://www.dynamicyield.com/experience-os) da Dynamic Yield, profissionais de marketing, gerentes de produtos, desenvolvedores e equipes digitais podem combinar algoritmicamente conteúdo, produtos e ofertas com cada cliente para acelerar a receita e a fidelidade do cliente.

_Essa integração é mantida pela Dynamic Yield._

## Sobre a integração

A parceria entre o Braze e a Dynamic Yield permite que você aproveite o mecanismo de recomendação e segmentação da Dynamic Yield para criar blocos de experiência que podem ser incorporados às mensagens do Braze. Os blocos de experiência podem ser compostos por:
- **Blocos de recomendações**: Defina algoritmos e filtros para obter o conteúdo personalizado dos usuários que se propaga quando o e-mail é aberto. 
- **Blocos de conteúdo dinâmico**: Direcione diferentes promoções e mensagens para diferentes usuários. O direcionamento pode se basear em afinidade ou público. O Dynamic Yield determina qual experiência personalizada será oferecida quando o e-mail for aberto. 

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da Dynamic Yield | É necessário ter uma conta [Dynamic Yield](https://adm.dynamicyield.com/users/sign_in#/r/dashboard) para aproveitar essa parceria. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Criar um bloco de experiência

Para criar um bloco de experiência na Dynamic Yield, navegue até **Email > Experience Emails > Create New** (E-mail > E-mails de experiência > Criar novo).

Em seguida, selecione **Create Experience Block (Criar bloco de experiência)** para criar um bloco de conteúdo dinâmico ou de recomendações a ser incorporado em um modelo de e-mail do Braze.<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield7.png %})

### Etapa 2: elabore seu envio de mensagens

A imagem a seguir mostra um e-mail do zero no construtor.<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield5.png %})

1. Digite um nome de campanha, nota e rótulos para a campanha na área de título.<br><br>
2. Inserir um bloco de experiência. Esses blocos incluem:
  - [Recomendações](#configure-a-recommendations-block): Um widget que oferece aos usuários recomendações totalmente personalizadas.
  - [Conteúdo dinâmico](#configure-a-dynamic-content-block): direcionamento de promoções e mensagens diferentes para diversos públicos.<br><br>
3. Atualizar configurações:
  - Use os parâmetros de URL para rastrear os cliques em seu software de análise de dados (opcional). Adicione parâmetros às exibições padrão conforme necessário.
  - Selecione um período de atributo, que pode ser de sete dias (padrão) ou um dia.<br><br>
4. Salvar e sair. Você pode voltar a editar todos os elementos do seu e-mail a qualquer momento antes de o código ser gerado. Após a geração do código, você poderá editar qualquer elemento que [não afete o código](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZPXB6MH094J1MWS5N86FXH).

### Configurar um bloco de recomendações

O bloco de recomendações ativa a definição de algoritmos e filtragem para originar o conteúdo personalizado dos usuários que se propaga quando o e-mail é aberto. 

1. Arraste um bloco de recomendações do painel de edição para o corpo do e-mail.<br><br>
2. Selecione o algoritmo desejado (popularidade, afinidade do usuário, similaridade e outros). Dependendo do algoritmo selecionado, são exibidas opções adicionais: 
  - Se sua recomendação for baseada na popularidade, você poderá embaralhar os resultados para evitar o envio da mesma recomendação de diferentes e-mails que o usuário abrir.
  - Outros algoritmos, como o de similaridade, dependem do contexto para fornecer recomendações que exigem que você selecione os itens a serem incluídos. Esses itens podem ser adicionados no construtor ou [adicionar uma tag de mesclagem ao código incorporado](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#advanced) para torná-lo dinâmico, por exemplo, para adicionar itens semelhantes aos e-mails de confirmação de envio. <br><br>
3. É possível excluir produtos que o usuário já tenha comprado para evitar a recomendação desses produtos.<br><br>
4. Você pode adicionar uma [regra de arquivamento personalizada](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZP4ZWZX1JJ2SH61MB3HVXD) para fixar produtos específicos em slots ou incluir e excluir produtos por propriedades do produto. Por exemplo, não mostre produtos com código inferior a US$ 5 ou apenas produtos da categoria de shorts.<br><br>
5. Por fim, configure o design do bloco de recomendação. Para fazer isso, selecione um modelo de item, defina o número de itens a serem exibidos e em quantas linhas. 

### Configurar um bloco de conteúdo dinâmico
Use o Dynamic Content para direcionar promoções e mensagens diferentes para usuários diferentes. O direcionamento pode se basear em afinidade ou público. O Dynamic Yield determina qual experiência personalizada será oferecida quando o e-mail for aberto. 

1. Arraste um bloco de conteúdo dinâmico do painel de edição para o corpo do e-mail.<br><br> 
2. Selecione um modelo para a primeira variação. Agora você pode definir variáveis de design e conteúdo. Salve a variação quando terminar. <br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield3.png %})<br><br> 
3. Defina o público no painel Conteúdo dinâmico.<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield4.png %})<br><br> 
4. Adicione outra variação para direcionamento a outro público específico ou a todos os usuários. Repita conforme necessário.<br><br> 
5. Defina as prioridades de suas variações usando as setas para cima e para baixo. <br><br> 
6. As prioridades determinam qual variação é atendida quando um usuário é elegível para mais de uma experiência.

### Etapa 3: integre seu e-mail com a Braze

Essa integração permite adicionar widgets de recomendação personalizados e conteúdo dinâmico com a tecnologia Dynamic Yield em suas campanhas de e-mail do Braze. A incorporação dessas campanhas nas campanhas do Braze é feita com um código de incorporação simples que você cola no editor de e-mail do Braze.

1. Clique no ícone de integração do ESP na página da lista "Experience Email" (E-mail da experiência).<br><br> 
2. Digite o token relevante da Braze que insere o CUID e o ID de e-mail do usuário.<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield2_new.png %})
  
Quando o e-mail ficar pronto, a próxima etapa será a geração do código para incorporar na Braze.
1. Em **Experience Emails**, clique em **Generate Code (Gerar código**).<br><br> 
2. Em seguida, clique em **Copiar para a área de transferência**.<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield.png %})<br><br> 
3. Cole o código em sua campanha de e-mail do Braze e, em seguida, continue a projetar, testar e publicar sua campanha de e-mail.


