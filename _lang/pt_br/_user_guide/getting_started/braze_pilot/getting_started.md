---
nav_title: Começando
article_title: Introdução ao Braze Pilot
page_order: 2
page_type: reference
description: "Este artigo de referência cobre brevemente os passos de integração necessários de seus engenheiros ou desenvolvedores."
---

# Começando com o Braze Pilot

> Este artigo cobre como começar a usar o Braze Pilot. Aqui, vamos guiá-lo pelo download do aplicativo, inicializando a conexão com seu painel Braze e completando a configuração.

## Passo 1: Baixar o Braze Pilot

Para começar a usar o Braze Pilot, você precisará primeiro baixar o aplicativo na Apple App Store ou no Google Play Store. Você pode procurar o aplicativo na loja de aplicativos ou escanear os códigos QR abaixo para visitar a página do aplicativo para seu dispositivo.

## Passo 2: Aceitar os termos e condições

Em seguida, aceite os termos e condições e insira seu e-mail de trabalho no formulário. Seu e-mail será usado apenas para análises de uso do aplicativo e não será utilizado para fins de marketing.

\![Página de boas-vindas do Braze Pilot.]({% image_buster /assets/img/braze_pilot/pilot_welcome.png %}){:style="max-width:30%"} \![Opção para inserir seu endereço de e-mail de trabalho.]({% image_buster /assets/img/braze_pilot/pilot_signin.png %}){:style="max-width:30%"}

## Passo 3: Inicializar a conexão com o SDK do Braze

O Braze Pilot permite que você inicialize o SDK do Braze contra qualquer painel Braze. Uma vez que o SDK esteja inicializado, o Pilot começará a enviar dados de engajamento para o Braze e permitirá que você acione qualquer mensagem lançada a partir desse painel Braze.

Existem dois métodos para configurar a conexão do SDK no Pilot: Códigos QR de demonstração e o assistente de configuração.

{% tabs local %}
{% tab Demo QR codes %}

### Método 1: Códigos QR de demonstração

Escaneie um código QR que inclua todos os detalhes necessários para inicializar o SDK, criar seu perfil de usuário e direcioná-lo para uma simulação de aplicativo específica no Braze Pilot. Códigos QR de demonstração são exibidos na gaveta de companheiro para campanhas de demonstração específicas em sua avaliação gratuita.

| Pilot para Android | Pilot para iOS |
| --- | --- |
| \![Código QR para Android.]({% image_buster /assets/img/braze_pilot/android_qr_code.png %}){:style="max-width:60%"} | \![Código QR para iOS.]({% image_buster /assets/img/braze_pilot/ios_qr_code.png %}){:style="max-width:60%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Setup wizard %}

### Método 2: Assistente de configuração

Siga um guia passo a passo para inicializar a conexão com seu espaço de trabalho do painel a partir da página **Configurações do App** no seu painel Braze.

\![Passo 1 do assistente de configuração para Braze Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Essa conexão é específica para o espaço de trabalho. Isso significa que se você inicializar a conexão a partir do espaço de trabalho de demonstração e depois mudar para o espaço de trabalho ao vivo no seu painel de avaliação gratuita, você precisará re-inicializar o SDK a partir desse espaço de trabalho para receber quaisquer campanhas lançadas lá.

\![O menu suspenso de espaço de trabalho no painel Braze com "Demonstração - Braze" selecionado como o espaço de trabalho ativo.]({% image_buster /assets/img/braze_pilot/dashboard_workspace.png %}){:style="max-width:60%"}

{% endtab %}
{% endtabs %}

## Passo 4: Permitir permissões de push

Finalmente, é recomendável que você permita que o aplicativo envie permissões de push se quiser testar as capacidades de push através do aplicativo. Você pode dar ao aplicativo essas permissões das seguintes maneiras: atualizando as configurações do aplicativo nas configurações do seu dispositivo ou lançando uma mensagem de introdução de push do Braze para o aplicativo.

{% tabs local %}
{% tab Update the settings for the app %}

Abra as configurações do seu dispositivo e localize o Braze Pilot. Em seguida, atualize as configurações para permitir que as notificações apareçam na sua tela de bloqueio.

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/device_settings.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Launch a push primer message %}

Você pode usar uma mensagem in-app do Braze para solicitar permissões de push para o aplicativo, assim como faria para seus próprios consumidores. Para aprender como construir esse tipo de mensagem no Braze, veja [Mensagens in-app de introdução de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages#push-primer-in-app-messages).

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/push_primer1.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Passo 5: Experimente a mensagem do Braze no Pilot

Agora você está pronto para começar a receber campanhas e Canvases do seu painel do Braze como um usuário do Braze Pilot! Visite qualquer uma das campanhas lançadas em seu espaço de trabalho de demonstração para uma rápida demonstração dos casos de uso do Braze, depois vá para seu espaço de trabalho ao vivo para começar a enviar os seus.

Para mais informações sobre como configurar campanhas e Canvases no Braze, veja [Introdução: Campanhas e Canvases]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases).