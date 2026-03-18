module Jekyll
  module Alerts
    ALERT_LABELS = {
      'es' => { 'note' => 'Nota', 'important' => 'Importante', 'tip' => 'Consejo',
                'warning' => 'Advertencia', 'update' => 'Actualización', 'checkpoint' => 'Punto de control' },
      'fr' => { 'note' => 'Remarque', 'important' => 'Important', 'tip' => 'Conseil',
                'warning' => 'Avertissement', 'update' => 'Mise à jour', 'checkpoint' => 'Point de contrôle' },
      'de' => { 'note' => 'Hinweis', 'important' => 'Wichtig', 'tip' => 'Tipp',
                'warning' => 'Warnung', 'update' => 'Aktualisierung', 'checkpoint' => 'Kontrollpunkt' },
      'ja' => { 'note' => '注', 'important' => '重要', 'tip' => 'ヒント',
                'warning' => '警告', 'update' => '更新', 'checkpoint' => 'チェックポイント' },
      'ko' => { 'note' => '참고', 'important' => '중요', 'tip' => '팁',
                'warning' => '경고', 'update' => '업데이트', 'checkpoint' => '체크포인트' },
      'pt-br' => { 'note' => 'Nota', 'important' => 'Importante', 'tip' => 'Dica',
                   'warning' => 'Aviso', 'update' => 'Atualização', 'checkpoint' => 'Ponto de verificação' },
    }.each_value { |v| v.freeze }.freeze

    class AlertTag < Liquid::Block

      def initialize(tag_name, markup, tokens)
        super
        @caption = markup
      end

      def render(context)
        site = context.registers[:site]
        converter = site.find_converter_instance(::Jekyll::Converters::Markdown)
        type = converter.convert(@caption).gsub(/<\/?p[^>]*>/, '').chomp.strip
        lang = (site.config['language'] || 'en').downcase
        label = (ALERT_LABELS.dig(lang, type.downcase) || type).gsub('-', ' ')
        body = converter.convert(super(context))
        "<div class='alert alert-#{type}' role='alert'><div class='alert-msg'> <b>#{label}: </b><br />#{body}</div></div>"
      end

    end
  end
end

Liquid::Template.register_tag('alert', Jekyll::Alerts::AlertTag)
