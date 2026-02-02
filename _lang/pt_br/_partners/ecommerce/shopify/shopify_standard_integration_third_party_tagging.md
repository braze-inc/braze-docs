---
nav_title: Integração do Shopify Standard com tag de terceiros
article_title: "Integração do Shopify Standard com tag de terceiros"
description: "Este artigo de referência descreve como configurar a integração padrão da Shopify com uma ferramenta de tag de terceiros."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration_third_party_tagging/
page_order: 2
---

# Integração padrão do Shopify com ferramenta de tag de terceiros

> Esta página o orienta no uso de ferramentas de terceiros, como o Google Tag Manager, com a [integração padrão do Shopify]({{site.baseurl}}/shopify_standard_integration/) para inicializar e carregar o Braze Web SDK.

Para lojas on-line da Shopify, recomendamos usar o método de integração padrão da Braze para oferecer suporte aos SDKs da Braze em seu site. No entanto, entendemos que você pode preferir usar uma ferramenta de terceiros, como o Google Tag Manager. Se você optar por usar uma ferramenta de terceiros com o conector Shopify do Braze, lembre-se de que a integração do Braze e a incorporação do app gerenciarão o SDK durante o processo de checkout.

## Solicitações

- **Chave de API consistente entre sua ferramenta de terceiros e o conector da Shopify:** A chave de API deve ser consistente tanto no Braze quanto em sua ferramenta de terceiros. Isso evita a criação de usuários duplicados e mantém a compatibilidade entre os SDKs. 
  - **Local da chave de API:** Depois de integrar a jornada de integração padrão, a integração criará automaticamente um aplicativo da Web do Braze chamado "Shopify". Recupere a chave de API dentro da integração que é usada com a configuração da ferramenta de terceiros. 
- **Versões consistentes do SDK entre sua ferramenta de terceiros e o conector da Shopify:** A versão do SDK deve ser `5.4` em sua ferramenta de terceiros. O uso de um número de versão incorreto pode causar problemas de incompatibilidade, pois alguns métodos do SDK podem não existir em versões mais antigas.
- **Tempo de inicialização consistente do SDK:** Nas configurações de integração padrão do Shopify, você pode selecionar os SDKs a serem inicializados no início da sessão ou quando ocorrer um login na conta. Essa configuração deve ser consistente entre sua ferramenta de terceiros e o Braze. As inconsistências podem levar a problemas de downstream para o usuário e a sincronização de dados. 

{% alert note %}
Recomendamos usar exclusivamente o método de integração padrão em vez de usá-lo em conjunto com gerenciadores de tags de terceiros, o que pode causar conflitos entre o Braze SDK e as ferramentas de terceiros. Se você usar uma ferramenta de terceiros, faça um teste para confirmar que tudo funciona conforme o esperado.
{% endalert %}

## Configuração da integração com uma ferramenta de terceiros

Desviar-se das etapas fornecidas pode levar a problemas inesperados, portanto, certifique-se de segui-las à risca.

1. Siga as etapas fornecidas na [configuração da integração padrão do Shopify]({{site.baseurl}}/shopify_standard_integration/). Ao [ativar os SDKs do Braze Web]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-2-enable-braze-web-sdks), marque a caixa que indica que você está usando uma ferramenta de terceiros para adicionar o SDK do Braze Web ao seu site da Shopify.

![Seção "Braze SDK settings" (Configurações do Braze SDK) com uma caixa de seleção para indicar que você usará uma ferramenta de terceiros para adicionar o Braze Web SDK.]({% image_buster /assets/img/Shopify/third_party_enable.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Acesse **Configurações** > **Configurações do app**, selecione o app da Web **da Shopify** e copie a **chave de API do Shopify on Web**.
3\. Cole a chave da API na configuração do SDK da Web de sua ferramenta de terceiros e defina a versão do SDK como `5.4`.

## Captura de dados do Shopify e sincronização de usuários

Desde que o Web SDK esteja acessível no front-end do seu site da Shopify por meio de uma ferramenta de terceiros, a integração padrão capturará os dados da Shopify e sincronizará os usuários conforme esperado.

## Considerações e isenções de responsabilidade

- **Configurações de inicialização:** Se você modificar as configurações de inicialização por meio da ferramenta de terceiros, a sincronização de usuários e dados poderá ser afetada. Por exemplo, se você optar por inicializar o SDK quando um formulário de consentimento de cookie for aceito, o Braze não receberá rastreamento de usuários anônimos ou dados de usuários até que o usuário consinta. 
- **Não há suporte para a definição de atribuições diretamente pelo site `dataLayer`:** Use `window.braze` em vez de `dataLayer` para definir atribuições.
- **Usuários duplicados em potencial:** Se a chave de API não corresponder ao Braze e à sua ferramenta de terceiros, poderão ser criados usuários duplicados.
- **Incompatibilidade de SDK:** O uso de um número de versão incorreto pode causar problemas com os métodos do SDK.