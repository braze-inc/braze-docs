---
nav_title: ViralSweep
article_title: ViralSweep
alias: /partners/viralsweep/
description: "Este artigo de referência descreve a parceria entre o Braze e o ViralSweep, um serviço de software que permite que as marcas criem, executem e gerenciem promoções de marketing digital, como sorteios, concursos, prêmios instantâneos, listas de espera, promoções por indicação e muito mais."
page_type: partner
search_tag: Partner

---

# ViralSweep

> [O ViralSweep](https://viralsweep.com) é um software como serviço que permite às marcas criar, executar e gerenciar promoções de marketing digital, como sorteios, concursos, prêmios instantâneos, listas de espera, promoções por indicação e muito mais. 

_Essa integração é mantida pela ViralSweep._

## Sobre a integração

A integração entre o Braze e o ViralSweep permite que você realize sorteios e concursos na plataforma ViralSweep (aumentando suas listas de e-mail e SMS) e, em seguida, envie as informações de inscrição em sorteios ou concursos para a Braze para serem usadas em campanhas ou canvas. 

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta ViralSweep | É necessário ter uma conta na ViralSweep que utilize o plano de negócios para aproveitar essa parceria. |
| chave da API REST Braze | Uma chave da API REST da Braze com todos os dados de usuários e permissões de e-mail. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
|Ponto de extremidade REST do Braze | Sua URL de endpoint REST. Seu endpoint dependerá do [URL da Braze para [sua instância]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1 : Conecte-se ao Braze no ViralSweep

No ViralSweep, navegue até **Integrações > Envio de e-mail e SMS > Adicionar serviço** e selecione **Braze**. 

![]({% image_buster /assets/img/viralsweep/connect.gif %})

### Etapa 2 : Adicionar credenciais do Braze

Na janela de configuração de integrações, forneça sua chave da API REST da Braze e o endpoint REST. Confirme se o endpoint fornecido não inclui `https://`. Ele deve seguir o formato `dashboard-03.braze.com`. 

![Página de integração do serviço ViralSweep solicitando ao usuário a chave de API do Braze e o URL do dashboard do Braze.]({% image_buster /assets/img/viralsweep/connect2.png %}){: style="max-width:40%;"}

Clique em **Connect (Conectar**).

### Etapa 3 : Adicionar credenciais do Braze
Você está conectado! A promoção agora está conectada à Braze, e todas as inscrições coletadas pelo ViralSweep serão enviadas automaticamente para a Braze.

## Perguntas frequentes

### Quais campos o ViralSweep passa para o Braze?
- Nome
- Sobrenome
- Endereço de e-mail
- Endereço
- Endereço 2
- Cidade
- Status
- Código postal
- País
- Data de nascimento
- Telefone
- ID da promoção
- Link de referência
- Nome da campanha de rastreamento

### O ViralSweep atualiza os assinantes?
Sim. Se você realizar uma promoção e o ViralSweep passar alguém para o Braze, e depois você realizar outra promoção no futuro e a mesma pessoa participar, as informações dessa pessoa serão automaticamente atualizadas no Braze (se alguma nova informação for fornecida). Principalmente, o URL de referência será atualizado com o URL mais recente de cada promoção em que ele entrar, e o campo ID da promoção conterá o ID de todas as promoções em que ele entrou.

## Solução de problemas

Se você se conectou ao Braze e os dados não estão sendo adicionados à sua conta, pode ser porque:

- **O e-mail já existe no Braze**<br>
O endereço de e-mail inserido na promoção pode já estar em sua conta Braze, portanto não será adicionado novamente; ele só será atualizado se novas informações forem fornecidas para esse contato.<br><br>
- **E-mail já inserido no ViralSweep**<br>
O endereço de e-mail inserido na promoção já foi inserido em outra ocasião, então não será passado para a Braze novamente. Isso pode acontecer se você configurar sua integração com o Braze depois de já ter entrado na promoção.


