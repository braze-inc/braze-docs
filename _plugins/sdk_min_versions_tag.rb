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

        @original_ios2 = get_full_version(text, 'swift')
        @ios_changelog_ref2 = get_changelog_ref(@original_ios2)

        @original_ios3 = get_full_version(text, 'objc')
        @ios_changelog_ref3 = get_changelog_ref(@original_ios3)

        @original_web = get_full_version(text, 'web')
        @web_changelog_ref = get_changelog_ref(@original_web)

        @original_android = get_full_version(text, 'android')
        @android_changelog_ref = get_changelog_ref(@original_android)

        @original_roku = get_full_version(text, 'roku')
        @roku_changelog_ref = get_changelog_ref(@original_roku)

        @flutter = get_full_version(text, 'flutter')
        @flutter_changelog_ref = get_changelog_ref(@flutter)

        @reactnative = get_full_version(text, 'reactnative')
        @reactnative_changelog_ref = get_changelog_ref(@reactnative)

        @unity = get_full_version(text, 'unity')
        @unity_changelog_ref = get_changelog_ref(@unity)

        @cordova = get_full_version(text, 'cordova')
        @cordova_changelog_ref = get_changelog_ref(@cordova)

        @xamarin = get_full_version(text, 'xamarin')
        @xamarin_changelog_ref = get_changelog_ref(@xamarin)

      end

      def render(context)
        site = context.registers[:site]
        converter = site.find_converter_instance(::Jekyll::Converters::Markdown)

        render_html = "<div id='sdk-versions'>"
        if !@original_web.nil?
          render_html += "<a href='/docs/developer_guide/platform_integration_guides/web/changelog/##{@web_changelog_ref}' class='sdk-versions--chip web-sdk' target='_blank'><i class='fa-solid fa-desktop'></i> &nbsp; Web: #{@original_web}+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        if !@original_ios.nil?
          render_html += "<a href='/docs/developer_guide/platform_integration_guides/ios/changelog/swift_changelog/##{@ios_changelog_ref}' class='sdk-versions--chip ios-sdk' target='_blank'><i class='fa-brands fa-apple'></i> &nbsp; iOS: #{@original_ios}+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        if !@original_ios2.nil?
          render_html += "<a href='/docs/developer_guide/platform_integration_guides/ios/changelog/swift_changelog/##{@ios_changelog_ref2}' class='sdk-versions--chip ios-sdk' target='_blank'><i class='fa-brands fa-apple'></i> &nbsp; iOS Swift: #{@original_ios2}+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        if !@original_ios3.nil?
          render_html += "<a href='/docs/developer_guide/platform_integration_guides/ios/changelog/objc_changelog/##{@ios_changelog_ref3}' class='sdk-versions--chip ios-sdk' target='_blank'><i class='fa-brands fa-apple'></i> &nbsp; iOS Objective-C: #{@original_ios3} &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        if !@original_android.nil?
          render_html += "<a href='/docs/developer_guide/platform_integration_guides/android/changelog/##{@android_changelog_ref}' class='sdk-versions--chip android-sdk' target='_blank'><i class='fa-brands fa-android'></i> &nbsp; Android: #{@original_android}+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        if !@original_roku.nil?
          render_html += "<a href='/docs/developer_guide/platform_integration_guides/roku/changelog/##{@roku_changelog_ref}' class='sdk-versions--chip roku-sdk' target='_blank'><i class='fa-solid fa-tv'></i> &nbsp; Roku: #{@original_roku}+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        if !@flutter.nil?
          render_html += "<a href='/docs/developer_guide/platform_integration_guides/flutter/changelog/##{@flutter_changelog_ref}' class='sdk-versions--chip flutter-sdk' target='_blank'>Flutter: #{@flutter}+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        if !@unity.nil?
          render_html += "<a href='/docs/developer_guide/platform_integration_guides/unity/changelog/##{@unity_changelog_ref}' class='sdk-versions--chip unity-sdk' target='_blank'>Unity: #{@unity}+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        if !@reactnative.nil?
          render_html += "<a href='/docs/developer_guide/platform_integration_guides/react_native/changelog/##{@reactnative_changelog_ref}' class='sdk-versions--chip reactnative-sdk' target='_blank'>React Native: #{@reactnative}+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        if !@cordova.nil?
          render_html += "<a href='/docs/developer_guide/platform_integration_guides/cordova/changelog/##{@cordova_changelog_ref}' class='sdk-versions--chip cordova-sdk' target='_blank'>Cordova: #{@cordova}+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        if !@xamarin.nil?
          render_html += "<a href='/docs/developer_guide/platform_integration_guides/xamarin/changelog/##{@xamarin_changelog_ref}' class='sdk-versions--chip xamarin-sdk' target='_blank'>Xamarin: #{@xamarin}+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        render_html += "</div>"
        return render_html
      end

      private

      def get_full_version(text, platform)
        query = /.*#{platform}:([\w\.\-]+) .*/
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
