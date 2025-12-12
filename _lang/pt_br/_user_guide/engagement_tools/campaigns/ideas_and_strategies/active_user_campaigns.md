---
nav_title: Campanhas de usuários ativos
article_title: Campanhas de Usuários Ativos
page_order: 0.5
page_type: tutorial
description: "Este artigo de como fazer descreve os benefícios das campanhas de usuários ativos dentro do painel da Braze e os passos para criar e configurar uma."
tool: 
  - Campaigns

---

# Campanhas de usuários ativos

> Identifique seus usuários ativos para ajudá-lo a criar campanhas personalizadas e recompensar aqueles que frequentam sua plataforma. 

Entrar em contato com usuários já ativos do seu aplicativo pode ser uma ferramenta poderosa para ajudar a construir um público dedicado de usuários consistentes do aplicativo. Um pouco de reconhecimento personalizado de seus usuários mais ativos pode transformá-los em evangelistas do seu aplicativo.

Você também pode conferir nosso [Braze Learning course](https://learning.braze.com/quick-overview-segment-and-campaign-setup) sobre estratégia de marketing para campanhas de email e ciclo de vida recomendadas!

## Entendendo usuários ativos

A Braze define um "usuário ativo" para um determinado período de tempo como qualquer usuário que tenha uma sessão nesse período.

Se um usuário perder a conectividade, armazenaremos os dados da sessão localmente e os enviaremos quando o usuário recuperar a conexão com a rede. Essas sessões também serão aplicadas à contagem de usuários ativos. Além disso, se seu aplicativo tiver um processo de registro, a Braze contará todos os usuários como ativos—registrados ou não registrados.

Se você definir IDs de Usuário para identificar usuários quando um novo usuário fizer login, ele será contado como um usuário ativo separado. Usuários que são atualizados via API também serão contados como um usuário ativo no período em que forem atualizados.

## Passo 1: Identificando seus principais usuários

Usando nossa seleção de filtros, crie um segmento de usuários que você acha que abrange sua base de usuários mais leal e consistente. O seguinte segmento de amostra define os principais usuários.

\![]({% image_buster /assets/img_archive/define_top_users.png %} "Define your top users")

Além disso, você não precisará continuar atualizando este segmento, pois os usuários que entrarem ou saírem das restrições da campanha serão correspondentemente alvo ou dispensados.

{% alert note %}
O exemplo anterior segmenta os usuários com base no uso geral do aplicativo. Na maioria dos casos, a coleção total de filtros necessários para definir seu segmento de usuários principais será amplamente definida pelas especificidades do seu aplicativo.
{% endalert %}

## Passo 2: Entre em contato com seus principais usuários

### Faça seus usuários se sentirem apreciados

Faça seus usuários se sentirem apreciados agradecendo-lhes pela lealdade e dedicação ao seu aplicativo. Dê aos seus usuários mais razões para continuar voltando ao seu aplicativo para incentivar mais atividades. Isso pode assumir a forma de ofertas especiais ou bônus exclusivamente para seus principais usuários. 

Recompensas inesperadas podem ser mais eficazes para incentivar ações contínuas dos usuários do que se você tivesse prometido desde o início!

\![Uma campanha na etapa de Composição com uma notificação rica do iOS que diz: "Obrigado novamente por comprar conosco! Para mostrar nossa apreciação, estamos oferecendo frete grátis na sua próxima compra".]({% image_buster /assets/img/congratulations_push.jpg %})

### Acompanhe seus resultados

Acompanhe as aberturas para garantir que você está direcionando a coleção adequada de usuários com o tipo de mensagem ideal. Além disso, acompanhe quaisquer cancelamentos de notificações push e tenha cuidado para não perder esses usuários cruciais.

