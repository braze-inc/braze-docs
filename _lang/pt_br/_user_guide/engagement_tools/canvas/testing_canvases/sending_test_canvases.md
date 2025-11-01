---
nav_title: Envio de telas de teste
article_title: Envio de telas de teste
page_order: 1
description: "Este artigo de referência aborda como testar um Canvas antes do lançamento e as práticas recomendadas."
page_type: reference
tool: Canvas
---

# Envio de telas de teste

> Depois de [criar seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/), há várias verificações que você pode querer fazer antes de lançá-lo, dependendo de detalhes como o tamanho do público-alvo ou o número de filtros de segmentação.

Quando possível, o Braze recomenda testar um Canvas antes de lançá-lo. Normalmente, esse teste será realizado em seu ambiente Braze. Testar o Canvas pode envolver duplicá-lo, conduzir os usuários de teste pela jornada do usuário e verificar se o comportamento do usuário está alinhado com o que você delineou no Canvas.

## Etapa 1: Crie seu plano de teste

Criar um plano de teste é essencial antes de começar a testar o Canvas. Um plano de teste pode ajudar a identificar e rastrear áreas específicas da jornada do Canvas.

Ao criar seu plano de testes, considere as seguintes questões:
- Foi criado pelo menos um usuário para cada ramificação e caminho do Canvas?
- Algum segmento está sendo usado em seu Canvas? 
	- Se forem usados segmentos, pode haver pré-requisitos para que um usuário se enquadre no Canvas antes de se qualificar para uma jornada do usuário.
- As mensagens no Canvas de teste têm algum Líquido nos títulos das mensagens que levam à ID do usuário ou ao endereço de e-mail para garantir que sejam fáceis de identificar a mensagem e o usuário para fins de teste?

## Etapa 2: Identificar usuários de teste

Em seguida, identifique um conjunto de usuários de teste que passarão pelas etapas do Canvas sem realmente enviar mensagens aos usuários pretendidos. Os usuários de teste podem ser endereços de e-mail existentes que não são usados para serviços reais em seu painel do Braze ou novos endereços de e-mail usados exclusivamente para fins de teste. 

## Etapa 3: Configure seu Canvas

Em seguida, é hora de testar seu Canvas! Para manter as informações do Canvas original e do Canvas de teste organizadas, crie uma cópia do seu Canvas para fins de teste.

Há duas maneiras de testar seu Canvas. 

- **Método 1:** No Canvas duplicado, edite a parte **Entry Audience (Público de entrada)** do construtor do Canvas para que apenas os usuários de teste estejam qualificados para o Canvas. Você também pode inserir seu próprio endereço de e-mail como usuário de teste adicionando o filtro de teste **Email Address**. No exemplo abaixo, limitamos o Canvas a dois usuários de teste que usaram o aplicativo pela primeira vez há menos de três dias.

Um Canvas com um público de entrada de "First used these apps less than 3 days ago" e os endereços de e-mail de dois usuários de teste.]({% image_buster /assets/img_archive/canvas_test2.png %}){: style="max-width:90%;"}

- **Método 2:** [Visualize os caminhos do usuário]({{site.baseurl}}/preview_user_paths/) selecionando o botão **Test Canvas** no rodapé do construtor do Canvas.

## Etapa 4: Inicie seu teste

Inicie seu Canvas de teste para permitir que os usuários comecem a entrar. Conclua os comportamentos do usuário em seu aplicativo que enviariam os usuários pela respectiva jornada do Canvas.

Verifique se os usuários de teste estão recebendo as mensagens pretendidas nas etapas do Canvas. Observe que seus usuários de teste podem não receber uma mensagem por motivos não limitados a:

- Não elegível para o Grupo de Controle Global
- Limitações do limite de frequência
- Associação de segmento incompatível
- Mensagens abortadas
- Push tokens associados a diferentes usuários

Continue a iterar os testes do Canvas para garantir que o desempenho do Canvas seja o esperado.

## Dicas gerais

### Identifique suas etapas do Canvas

Em alguns casos, um usuário pode receber várias mensagens ao passar por um Canvas. Se o atraso entre as etapas tiver sido reduzido significativamente para testes, talvez nem sempre fique claro qual mensagem está sendo acionada durante o teste. Garantir que as mensagens de teste incluam o nome da etapa ou o ID do usuário (usando o Liquid) facilitará a identificação e a confirmação de que a mensagem correta foi enviada aos usuários corretos.

### Criar um grupo interno

Em vez de criar usuários de teste individuais, você pode criar um [Grupo de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), que é um grupo interno cuja finalidade é revisar o conteúdo da sua mensagem. Isso inclui um grupo de usuários que receberão mensagens de teste de campanhas e Canvases. Em seguida, você pode adicionar esse grupo de teste no campo **Add Content Test Groups (Adicionar grupos de teste de conteúdo** ) em **Test Recipients (Destinatários de teste**).

### Reduzir atrasos

Para ajudar a executar os testes com mais eficiência, sugerimos reduzir os atrasos de tempo para minutos ou segundos para fins de teste, para que você possa visualizar as mensagens em tempo hábil. Por exemplo, aguarde pelo menos 2 a 3 minutos entre os testes para poder isolar ações específicas para jornadas específicas do Canvas.

### Aproveite os blocos de conteúdo

Se algum conteúdo for repetido em sua estrutura de teste (por exemplo, um Liquid complexo para filtrar usuários em diferentes etapas do Canvas), tente salvar esse conteúdo repetido como um [Content Block]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks). Agora, você poderá incluir o Content Block em todas as etapas individuais do Canvas.

### Use o Postman e o ponto de extremidade do usuário Track

Você pode executar testes com o Postman e a [Braze Postman Collection]({{site.baseurl}}/api/postman_collection/). Use o [endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para registrar e rastrear eventos e compras personalizados para seus vários usuários de teste.

Observe que o envio de dados para a API de rastreamento de usuários só pode ser feito com uma ID externa. Portanto, os usuários de teste podem precisar ser adicionados como usuários de teste em um grupo interno no painel do Braze para que erros específicos possam ser investigados com mais detalhes. 

#### Teste de várias ramificações

Quando estiver testando um Canvas com várias ramificações que visam usuários com base em diferentes atributos e eventos, siga este plano de teste:

1. Para cada ramificação, identifique os atributos e eventos que o usuário deve ter para ser incluído na jornada do Canvas.
2. Crie-os em uma carga útil JSON a ser postada usando o ponto de extremidade `/users/track`.

