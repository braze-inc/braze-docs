---
nav_title: Começar
article_title: Comece com o Braze Pilot
page_order: 2
page_type: reference
description: "Este artigo de referência aborda brevemente as etapas de integração exigidas de seus engenheiros ou desenvolvedores."
---

# Comece com o Braze Pilot

> Este artigo cobre como começar a usar o Braze Pilot. Aqui, vamos guiá-lo pelo download do app, inicializando a conexão com seu dashboard do Braze e completando a configuração.

## Etapa 1: Baixar Braze Pilot

Para começar a usar o Braze Pilot, você primeiro precisará baixar o app da Apple App Store ou do Google Play Store. Você pode procurar o app na loja de apps ou escanear os códigos QR abaixo para visitar a página do app para seu dispositivo.

## Etapa 2: Aceite os termos e condições

Em seguida, aceite os termos e condições e insira seu e-mail de trabalho no formulário. Seu e-mail será usado apenas para análises de uso do app e não será utilizado para fins de marketing.

![Página de boas-vindas do Braze Pilot.]({% image_buster /assets/img/braze_pilot/pilot_welcome.png %}){:style="max-width:30%"} ![Opção para inserir seu endereço de e-mail de trabalho.]({% image_buster /assets/img/braze_pilot/pilot_signin.png %}){:style="max-width:30%"}

## Etapa 3: Inicialize a conexão com o SDK do Braze

O Braze Pilot permite que você inicialize o SDK do Braze contra qualquer dashboard do Braze. Uma vez que o SDK esteja inicializado, o Pilot começará a enviar dados de engajamento para o Braze e permitirá que você dispare qualquer mensagem lançada a partir desse dashboard do Braze.

Existem dois métodos para configurar a conexão do SDK no Pilot: Códigos QR de demonstração e o assistente de configuração.

{% tabs local %}
{% tab Demo QR codes %}

### Método 1: Códigos QR de demonstração

Escaneie um código QR que inclui todos os detalhes necessários para inicializar o SDK, criar seu perfil de usuário e fazer deep link para uma simulação de app específica no Braze Pilot. Códigos QR de demonstração são exibidos na gaveta de companheiro para campanhas de demonstração específicas em seu teste gratuito.

| Pilot para Android | Piloto para iOS |
| --- | --- |
| ![Código QR para Android.]({% image_buster /assets/img/braze_pilot/android_qr_code.png %}){:style="max-width:60%"} | ![Código QR para iOS.]({% image_buster /assets/img/braze_pilot/ios_qr_code.png %}){:style="max-width:60%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Setup wizard %}

### Método 2: Assistente de configuração

Siga um guia passo a passo para inicializar a conexão com seu espaço de trabalho no dashboard a partir da página **Configurações do App** no seu dashboard Braze.

![Passo 1 do assistente de configuração para o Piloto Braze.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Essa conexão é específica do espaço de trabalho. Isso significa que se você inicializar a conexão a partir do espaço de trabalho de demonstração e depois mudar para o espaço de trabalho ao vivo no seu dashboard de teste gratuito, você precisará re-inicializar o SDK a partir desse espaço de trabalho para receber quaisquer campanhas lançadas lá.

![O menu suspenso de espaços de trabalho no dashboard Braze com "Demo - Braze" selecionado como o espaço de trabalho ativo.]({% image_buster /assets/img/braze_pilot/dashboard_workspace.png %}){:style="max-width:60%"}

{% endtab %}
{% endtabs %}

## Etapa 4: Permitir permissões de push

Por fim, é recomendado que você permita que o app envie permissões de push se quiser testar as capacidades de push através do app. Você pode dar essas permissões ao app das seguintes maneiras: atualizando as configurações do app nas configurações do seu dispositivo ou lançando uma mensagem introdutória de push do Braze para o app.

{% tabs local %}
{% tab Update the settings for the app %}

Abra as configurações do seu dispositivo e localize o Braze Pilot. Em seguida, atualize as configurações para permitir que notificações apareçam na sua tela de bloqueio.

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

Você pode usar uma mensagem no app do Braze para solicitar permissões de push para o app, assim como faria para seus próprios consumidores. Para aprender como construir esse tipo de mensagem no Braze, veja [Mensagens introdutórias de push no app]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages#push-primer-in-app-messages).

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/push_primer1.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Etapa 5: Experimente o envio de mensagens do Braze no Piloto

Agora você está pronto para começar a receber campanhas e Canvases do seu dashboard Braze como um usuário do Braze Pilot! Visite qualquer uma das campanhas lançadas no seu espaço de trabalho de demonstração para uma rápida demonstração dos casos de uso do Braze, depois vá para o seu espaço de trabalho ao vivo para começar a enviar os seus próprios.

Para mais informações sobre como configurar campanhas e Canvases no Braze, veja [Introdução: Campanhas e telas]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases).