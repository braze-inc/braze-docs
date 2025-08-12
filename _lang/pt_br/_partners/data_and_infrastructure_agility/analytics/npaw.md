---
nav_title: NPAW
article_title: NPAW
alias: /partners/npaw/
description: "Este artigo de referência descreve a parceria entre a Braze e a NPAW, uma plataforma inteligente de análise de dados que fornece insights práticos para os principais profissionais de mídia online."
page_type: partner
search_tag: Partner
hidden: true

---

# NPAW

> A [NPAW](https://nicepeopleatwork.com/), também conhecida como _Nice People at Work_, é uma plataforma inteligente de análise de dados que fornece insights práticos para os principais profissionais de mídia online. Com a suíte de ferramentas YOUBORA da NPAW, os clientes da Braze agora podem aproveitar uma IA preditiva e robusta para entender melhor o comportamento do cliente e impulsionar o engajamento em todas as plataformas.

# Pré-requisitos

| Requisito   |Origin| Descrição |
| --------------|------|-------------|
| chave de API YOUBORA |[Configurações do YOUBORA](https://youbora.nicepeopleatwork.com/users/login)|Uma chave de API gerada no cadastro do usuário e pode ser localizada em **Configurações** |
| ID |[Configurações da Braze](https://dashboard.braze.com/sign_in) | YOUBORA oferece as opções de vincular o software ao Braze via um ***ID do Braze***, um ***ID de Usuário externo*** ou um ***ID de Usuário*** |
| Endpoint |[Configurações da Braze](https://dashboard.braze.com/sign_in)| Um endpoint de URL totalmente personalizável configurável através do seu dashboard do Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

# integração de análise de dados

## Acessando a página de integrações

Após o registro em sua conta do YOUBORA tool suite, navegue até a página Integrations selecionando a opção **Integrations** no menu suspenso da conta.

![Menu suspenso do NPAW]({% image_buster /assets/img/npaw_dropdown.png %})

## Configurando sua integração

Na página de integração, role para baixo até que você
veja a opção de integração **Braze**. Depois de clicar nela, você verá uma série de parâmetros necessários para preencher:

![Integração NPAW]({% image_buster /assets/img/npaw_integration.png %})

Preencha os campos com os dados coletados na seção de pré-requisitos, em que:
* **Nome do conector** é uma string **alfanumérica** que será usada para se referir a esta integração no futuro. Este valor pode ser definido para qualquer coisa que você goste, desde que contenha **apenas** letras e números.
* **ID de usuário** é o ID previamente escolhido para vincular seu software YOUBORA à sua conta Braze. Por exemplo, se você optar por realizar o link via seu **Braze ID**, selecione **Braze ID** no menu suspenso para atribuir o valor ao campo adequado.
* **chave de API** é a sua chave de API da suíte de ferramentas YOUBORA encontrada anteriormente na seção **API** em **Configurações**.
* **Endpoint** é o endpoint de URL personalizável configurado anteriormente no seu dashboard do Braze.

Depois que todos os campos forem preenchidos, basta clicar no botão **Conectar** para estabelecer uma conexão e salvar as alterações feitas.

## Usando sua integração NPAW

Depois de terminar de configurar sua integração com a Braze, navegue até o produto **Usuários** e selecione o **Gerenciador de Amostras** dentro do **Gerenciador de Seções**.

Depois de criar uma amostra no **Sample Manger**, você agora poderá clicar no ícone de três pontos no lado direito para enviar todos os usuários da sua amostra para a Braze.

![Gerenciador de amostras da NPAW]({% image_buster /assets/img/npaw_sample_manager.png %})

Agora, depois de enviar seus usuários para a Braze, você pode agir e focar campanhas em segmentos de usuários para reengajar usuários inativos, contatar seus usuários mais leais ou qualquer ação em qualquer segmento de usuário!
