# Usage: 
# {% sdk_min_versions ios:3.2.3 android:8.0.0 web:1.2.3 %}
# Description:
# Renders a chip for each platform along with the changelog version as an href

module Jekyll
  module SdkMinVersions
    class SdkMinVersionsTag < Liquid::Tag

      def initialize(tag_name, text, tokens)
        super
        @original_ios = get_full_version(text, 'ios')
        @ios_changelog_ref = get_changelog_ref(@original_ios)

        @original_web = get_full_version(text, 'web')
        @web_changelog_ref = get_changelog_ref(@original_web)

        @original_android = get_full_version(text, 'android')
        @android_changelog_ref = get_changelog_ref(@original_android)
      end

      def render(context)
        site = context.registers[:site]
        converter = site.find_converter_instance(::Jekyll::Converters::Markdown)

        render_html = "<div id='sdk-versions'>"
        if !@original_web.nil?
          render_html += "<a href='/docs/developer_guide/platform_integration_guides/web/changelog/##{@web_changelog_ref}' class='sdk-versions--chip web-sdk' target='_blank'><i class='fa fa-desktop'></i> &nbsp; Web: #{@original_web} &nbsp;<i class='fa fa-external-link'></i></a>"
        end
        if !@original_ios.nil?
          render_html += "<a href='/docs/developer_guide/platform_integration_guides/ios/changelog/##{@ios_changelog_ref}' class='sdk-versions--chip ios-sdk' target='_blank'><i class='fa fa-apple'></i> &nbsp; iOS: #{@original_ios} &nbsp;<i class='fa fa-external-link'></i></a>"
        end
        if !@original_android.nil?
          render_html += "<a href='/docs/developer_guide/platform_integration_guides/android/changelog/##{@android_changelog_ref}' class='sdk-versions--chip android-sdk' target='_blank'><i class='fa fa-android'></i> &nbsp; Android: #{@original_android} &nbsp;<i class='fa fa-external-link'></i></a>"
        end

        render_html += "</div>"
        return render_html
      end

      private 

      def get_full_version(text, platform)
        query = /.*#{platform}:([\w\.]+) .*/
        match = text.match(query)
        if match.nil?
          return nil
        else 
          return match[1]
        end
      end

      def get_changelog_ref(text)
        if text.nil?
          return ""
        end
        return text.gsub(".", "")
      end
    end
  end
end

Liquid::Template.register_tag('sdk_min_versions', Jekyll::SdkMinVersions::SdkMinVersionsTag)
