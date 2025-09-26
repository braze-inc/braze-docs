---
nav_title: Survicate
article_title: Survicate
description: "Este artigo de referência descreve a parceria entre o Braze e a Survicate, uma plataforma de feedback do cliente que ajuda a coletar, analisar e agir com base nos insights do cliente em vários canais e durante toda a jornada do usuário."
alias: /partners/survicate/
page_type: partner
search_tag: Partner

---

# Survicate

![Um exemplo de como uma pesquisa HTML incorporada (primeira pergunta) poderia parecer em um e-mail Braze.]({% image_buster /assets/img/survicate/survicate_asset_1.png %}){: style="float:right;max-width:40%;border:0; margin-left:8px;"}

> A [Survicate](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter) é uma plataforma de feedback do cliente que ajuda a coletar, analisar e agir com base nos insights do cliente em vários canais e durante toda a jornada do usuário.  

_Esta integração é mantida pela Survicate._

## Sobre a integração

Com a integração Braze e Survicate, você pode incorporar pesquisas diretamente em seus e-mails Braze para aumentar as taxas de resposta. As respostas da pesquisa são sincronizadas automaticamente com os perfis de usuário do Braze como atributos ou eventos personalizados. Os insights em tempo real facilitam o rastreamento e a análise do feedback juntamente com os dados de clientes e a criação de acompanhamentos direcionados.

## Casos de uso

A Braze e a Survicate trabalham juntas para cobrir uma série de casos de uso de feedback, ajudando-o a coletar insights práticos sobre o usuário e a melhorar a experiência do cliente:

- Medir a satisfação do cliente (como CSAT, NPS ou CES)
- Coletar feedback sobre o produto
- Conduzir pesquisas de usuários ou de mercado
- Reúna insights em estágios críticos da jornada do cliente
- Disparar fluxos de trabalho personalizados e automatizar campanhas de acompanhamento com base no feedback do cliente

## Principais recursos da integração

A integração entre a Survicate e a Braze oferece sincronização de dados em tempo real, de modo que as informações mais atualizadas das pesquisas da Survicate ficam imediatamente disponíveis na Braze. Com base nas respostas da pesquisa, você pode usar esses dados para tomar medidas oportunas e personalizadas.

- **Envie as respostas da pesquisa para o Braze como atributos personalizados do usuário**: Enriqueça os perfis de usuários do Braze com dados de respostas de pesquisas.
- **Disparar eventos personalizados no Braze**: Use eventos baseados nas respostas da pesquisa para direcionar grupos específicos ou iniciar campanhas de acompanhamento.
- **Crie segmentos detalhados**: Crie segmentos Braze usando dados das pesquisas Survicate para personalizar ainda mais seu alcance.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Survicate | Você precisa de uma conta Survicate para ativar essa integração. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Crie sua pesquisa no Survicate

1. No painel do Survicate, selecione **Criar nova pesquisa**.
2. Escolha o canal da pesquisa - **pesquisas por e-mail, link, site, produto e app móvel** estão disponíveis. 
3. Elabore sua pesquisa do zero, use o criador de pesquisas IA ou selecione entre mais de 100 modelos prontos para uso.

![Quatro opções para criar uma pesquisa: começar do zero, usar um modelo, criação assistida por IA e importar perguntas.]({% image_buster /assets/img/survicate/survicate_asset_3.png %})

### Etapa 2: Identifique os entrevistados automaticamente com os e-mails do Braze

1. Depois que sua pesquisa estiver pronta, acesse a guia **Configure (Configurar)**.
2. Para *Identificar respondentes com*, selecione **Braze**. Isso vincula automaticamente as respostas aos perfis de seus clientes Braze, portanto, não há necessidade de solicitar detalhes de contato em sua pesquisa.

![Braze é selecionado como os respondentes.]({% image_buster /assets/img/survicate/survicate_asset_2.png %})

### Etapa 3: Conecte a integração

1. Em seguida, na **guia Connect (Conectar)**, encontre o Braze e selecione **Connect ** to integrate (Conectar para integrar). 
2. Insira a chave de API do espaço de trabalho de sua conta Braze e o URL das instâncias da Braze.

![Campos para inserir a chave de API do espaço de trabalho e a URL da instância Braze.]({% image_buster /assets/img/survicate/image1.png %})

### Etapa 4: Compartilhe sua pesquisa

1. Em seguida, na guia **Share (Compartilhar)**, escolha onde deseja colocar o questionário. As opções incluem:
- **Link direto**: Copie o link para usá-lo no Braze como um botão ou hiperlink.
- **Incorporar a primeira pergunta**: Copie o código HTML para incorporar a primeira pergunta da pesquisa diretamente no corpo de um e-mail do Braze.
- **Lançar uma pesquisa em seu site ou no produto**: Instale o código de rastreamento uma vez e defina as pesquisas ao vivo diretamente no painel do Survicate.

### Etapa 5: Adicione a pesquisa à sua campanha de e-mail do Braze

1. No Braze, cole o link da pesquisa ou o código HTML no conteúdo da sua campanha de e-mail.
2. Comece a coletar feedback e rastrear as respostas diretamente no Survicate.


