---
nav_title: Oficina
article_title: Workshop do Amazon Personalize
alias: /partners/amazon_personalize_workshop/
description: "Este artigo de referência descreve o processo de configuração do Amazon Personalize e sua integração em seu ambiente Braze usando o Connected Content."
page_type: partner
search_tag: Partner
---

# Workshop do Amazon Personalize

> Este artigo de referência o guiará pelo processo de configuração do Amazon Personalize e sua integração ao seu ambiente Braze usando o Connected Content. Isso é feito por meio de um workshop prático que o guiará por todas as etapas necessárias para implantar e treinar as soluções do Amazon Personalize e integrá-las a uma campanha de e-mail do Braze.

_Essa integração é mantida pela Amazon Personalize._

## Sobre a integração

Os exemplos a seguir foram implementados em um site de comércio eletrônico de exemplo totalmente funcional chamado Retail Demo Store. Os recursos e o código para este tutorial estão publicados no [AWS Samples Retail Demo Store](https://github.com/aws-samples/retail-demo-store/). Você pode usar essa implementação de arquitetura de referência como um esboço para implementar o Amazon Personalize em seu próprio ambiente.

## Solicitações

Você precisará clonar o [repositório do Retail Demo Store](https://github.com/aws-samples/retail-demo-store/) e seguir as etapas descritas para implantar o ambiente do workshop em sua conta da AWS. É necessário ter uma conta do AWS para concluir o workshop e executar o código de integração.

## Arquitetura de integração

Antes de configurar o Braze para enviar mensagens personalizadas aos usuários, revise os componentes relevantes necessários para um site de comércio eletrônico típico, usando a arquitetura da Retail Demo Store como exemplo.

![Uma imagem que detalha a arquitetura de personalização do Braze, notando como os diferentes componentes interagem uns com os outros.]({% image_buster /assets/img/amazon_personalize/braze-personalize-arch.png %}){: style="max-width:70%" }

1. A interface de usuário da Web da Retail Demo Store usa a biblioteca JavaScript do AWS Amplify para enviar eventos de treinamento para o Amazon Personalize.
2. Os registros de usuários de campanha da Braze são atualizados a partir do serviço Global Store User.
3. Quando uma campanha do Braze é executada, um modelo de Connected Content é usado para buscar recomendações do Personalize e preencher um modelo de e-mail para um usuário direcionado.
4. As informações do catálogo de produtos também podem ser usadas para treinar modelos de recomendação.

O Braze enviará e-mails aos seus usuários com base no comportamento deles ou nas atribuições de seus perfis de usuário. Esses dados podem ajudar a identificar usuários e criar perfis de usuários para ajudar a determinar quando enviar uma mensagem ou e-mail.

Esse fluxo de dados de eventos ocorrerá em paralelo aos dados de eventos comportamentais que estão sendo enviados ao Amazon Personalize. Neste workshop, a loja de demonstração usa a Amplify para enviar eventos para o Personalize. Esses dados são usados para treinar um modelo de recomendações que pode ser usado nas chamadas do Braze Connected Content para personalizar o conteúdo para os usuários quando a campanha do Braze for executada.

O Braze Connected Content poderá obter essas recomendações por meio de um serviço de recomendação executado na AWS. O workshop Retail Demo Store mostra um exemplo de implantação de serviço de recomendação. Em um cenário de implementação em sua própria infraestrutura, você precisará implementar um serviço semelhante para obter itens de seu próprio serviço de catálogo.

## Preparação do workshop de arquitetura de referência

### Etapa 1: implante a Retail Demo Store na sua conta do AWS

![Uma imagem das regiões da AWS disponíveis.]({% image_buster /assets/img/amazon_personalize/region.png %}){: style="float:right;max-width:40%;margin-top:15px;margin-bottom:10px;"}

Na tabela a seguir, escolha uma **região do AWS** e selecione **Iniciar stack** (Launch Stack). Essa lista não representa todas as regiões possíveis onde você pode implantar o projeto, apenas as regiões atualmente configuradas para implantação com a Retail Demo Store.

Aceitar todos os valores de parâmetros padrão do modelo. A implementação de todos os recursos do projeto deve levar de 25 a 30 minutos.

### Etapa 2: Criar campanhas do Amazon Personalize

Antes de poder fornecer recomendações personalizadas de produtos, primeiro é necessário treinar os modelos de machine learning e fornecer pontos de extremidade de inferência que permitirão obter recomendações do Amazon Personalize. O modelo CloudFormation implantado na etapa 1 inclui uma instância do notebook Amazon SageMaker, que fornece um notebook Jupyter com instruções detalhadas passo a passo.

1. Faça login na conta do AWS em que você implantou o modelo do AWS CloudFormation na etapa 1.
2. No console do Amazon SageMaker, escolha **Notebook instances** (Instâncias de notebook).
3. Se você não vir a instância do notebook **RetailDemoStore**, verifique se está na mesma região em que implantou o projeto na etapa 1.
4. Para acessar a instância do notebook, escolha **Open Jupyter** (Abrir Jupyter) ou **Open JupyterLab** (Abrir JupyterLab).
5. Quando a interface da Web do Jupyter tiver sido carregada para a instância do notebook, escolha o notebook `workshop/1-Personalization/1.1-Personalize.ipynb`. Talvez seja necessário selecionar a pasta `workshop` para ver os subdiretórios do notebook.
6. Quando estiver com o notebook `1.1-Personalize` aberto, faça uma etapa do workshop executando cada célula. Você pode selecionar **Run** (Executar) na barra de ferramentas do Jupyter para executar sequencialmente o código nas células. O notebook leva aproximadamente duas horas para concluir.

### Etapa 3: Enviar e-mails personalizados do Braze

Com as soluções e campanhas do Amazon Personalize implementadas, sua instância do Retail Demo Store está pronta para fornecer recomendações para suas campanhas de e-mail. Na etapa 1, você implantou o aplicativo da Web de demonstração e todos os serviços associados, incluindo o serviço de recomendação necessário para integrar suas campanhas de e-mail ao Braze por meio do Connected Content, que usa as campanhas do Amazon Personalize implantadas na etapa 2.

Semelhante ao workshop de personalização na etapa 2, o workshop de envio de mensagens do Braze a seguir o orienta na configuração da integração entre o Braze e o Amazon Personalize.

1. Faça login na conta do AWS em que você implantou o modelo do AWS CloudFormation na etapa 1.
2. No console do Amazon SageMaker, escolha **Notebook Instances** (Instâncias de notebook).
3. Se você não vir a instância do notebook **RetailDemoStore**, verifique se está na mesma região da AWS em que implantou o projeto.
4. Para acessar a instância do notebook, escolha **Open Jupyter** (Abrir Jupyter) ou **Open JupyterLab** (Abrir JupyterLab).
5. Quando a interface da Web do Jupyter tiver sido carregada para a instância do notebook, escolha o notebook `workshop/4-Messaging/4.2-Braze.ipynb`. Talvez seja necessário selecionar a pasta `workshop` para ver os subdiretórios do notebook.
6. Quando estiver com o notebook `4.2-Braze` aberto, faça uma etapa do workshop executando cada célula. Você pode selecionar **Run** (Executar) na barra de ferramentas do Jupyter para executar sequencialmente o código nas células. O notebook leva aproximadamente uma hora para concluir.

### Etapa 4: Recursos de limpeza

Para evitar cobranças futuras, exclua os recursos da AWS que o projeto Retail Demo Store removendo a pilha do AWS CloudFormation que você criou na etapa 1.


