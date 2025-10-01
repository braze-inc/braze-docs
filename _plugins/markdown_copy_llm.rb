# _plugins/markdown_copy_llm.rb
require 'jekyll'
require 'liquid'

module MarkdownExport
  # No-op blocks: keep inner Markdown (strip HTML wrappers)
  class MdexpSdkTabs < Liquid::Block
    def render(context); super; end
  end

  class MdexpSdkTab < Liquid::Block
    def render(context); super; end
  end

  class MdexpTab < Liquid::Block
    def render(context); super; end
  end

  class MdexpSubtabs < Liquid::Block
    def render(context); super; end
  end

  class MdexpSubtab < Liquid::Block
    def render(context); super; end
  end

  class MdexpSdkSubtabs < Liquid::Block
    def render(context); super; end
  end

  class MdexpSdkSubtab < Liquid::Block
    def render(context); super; end
  end

  class MdexpTabs < Liquid::Block
    def render(context); super; end
  end

  # Inline raw Markdown includes. Be lenient with args.
  class MdexpMultiLangInclude < Liquid::Tag
    def initialize(tag_name, markup, tokens)
      super
      @markup = markup.to_s.strip # allow empty/variables/filters
    end

    def render(context)
      # Resolve expression (string literal, variable, or empty)
      path = resolve_path(@markup, context).to_s.strip
      return "<!-- export: empty multi_lang_include -->" if path.empty?

      site = context.registers[:site]
      src  = site.source

      # Try absolute under source; also respect _includes lookup
      candidates = []
      candidates << File.expand_path(path, src)
      Array(site.config['includes_dir'] || '_includes').each do |inc|
        candidates << File.expand_path(path, File.join(src, inc))
      end

      full = candidates.find { |p| File.file?(p) }
      return "<!-- export: not found #{path} -->" unless full

      File.read(full)
    rescue => e
      Jekyll.logger.error "MarkdownCopyLLM:", "Failed to inline #{@markup}: #{e.class}: #{e.message}"
      "<!-- export: failed to inline #{@markup}: #{e.class}: #{e.message} -->"
    end

    private

    def resolve_path(markup, context)
      return "" if markup.nil? || markup.empty?
      
      # Extract just the file path, ignoring parameters like page="testing"
      # e.g. "banners/testing.md page=\"testing\"" -> "banners/testing.md"
      path = markup.split(/\s+/).first
      
      # Accept quoted strings, bare words, or full Liquid expressions
      # e.g. "a/b.md", a/b.md, {{ var | downcase }}
      if path.start_with?('"', "'")
        path.gsub(/\A["']|["']\z/, '')
      elsif path.include?('{{')
        Liquid::Template.parse(path).render(context)
      else
        path
      end
    end
  end
end

# Register export-only tag names (do NOT override your real tags)
Liquid::Template.register_tag('mdexp_sdktabs', MarkdownExport::MdexpSdkTabs)
Liquid::Template.register_tag('mdexp_sdktab',  MarkdownExport::MdexpSdkTab)
Liquid::Template.register_tag('mdexp_tab',     MarkdownExport::MdexpTab)
Liquid::Template.register_tag('mdexp_tabs',    MarkdownExport::MdexpTabs)
Liquid::Template.register_tag('mdexp_subtabs', MarkdownExport::MdexpSubtabs)
Liquid::Template.register_tag('mdexp_subtab',  MarkdownExport::MdexpSubtab)
Liquid::Template.register_tag('mdexp_sdksubtabs', MarkdownExport::MdexpSdkSubtabs)
Liquid::Template.register_tag('mdexp_sdksubtab',  MarkdownExport::MdexpSdkSubtab)
Liquid::Template.register_tag('mdexp_multi_lang_include', MarkdownExport::MdexpMultiLangInclude)

module Jekyll
  class MarkdownCopyLLM
    RAW_KEY = "__export_merged_md"

    def self.init
      # Capture export Markdown just before normal rendering
      Jekyll::Hooks.register [:pages, :documents], :pre_render do |item, payload|
        next unless should_capture?(item, item.site)
        item.data[RAW_KEY] = render_liquid_markdown_friendly(item, payload, item.site)
      end

      # Emit files after normal site write
      Jekyll::Hooks.register :site, :post_write do |site|
        copy_markdown_files(site)
      end
    end

    # ---------- helpers ----------

    def self.should_capture?(item, site)
      markdown?(item, site) &&
        !item.path.include?('_site/') &&
        !item.path.start_with?('_') &&
        %w[_includes _layouts _data _plugins].none? { |d| item.path.start_with?(d) }
    end

    def self.markdown?(item, site)
      ext = item.respond_to?(:extname) ? item.extname : File.extname(item.path)
      return true if %w[.md .markdown].include?(ext)
      # Or detect via active Markdown converter if you use custom extensions:
      # site.find_converter_instance(Jekyll::Converters::Markdown).matches(ext)
      false
    end

    # Rewrites certain tag names to export-only aliases, then renders Liquid.
    # This expands variables and inlines raw Markdown, while stripping tab HTML wrappers.
    def self.render_liquid_markdown_friendly(item, payload, site)
      content = item.content.dup

      # Map real tags -> export tags (open/close)
      replacements = {
        /\{%\s*sdktabs\b/           => '{% mdexp_sdktabs',
        /\{%\s*endsdktabs\s*%}/     => '{% endmdexp_sdktabs %}',
        /\{%\s*sdktab\b/            => '{% mdexp_sdktab',
        /\{%\s*endsdktab\s*%}/      => '{% endmdexp_sdktab %}',
        /\{%\s*sdksubtabs\b/            => '{% mdexp_sdksubtabs',
        /\{%\s*endsdksubtabs\s*%}/      => '{% endmdexp_sdksubtabs %}',
        /\{%\s*sdksubtab\b/            => '{% mdexp_sdksubtab',
        /\{%\s*endsdksubtab\s*%}/      => '{% endmdexp_sdksubtab %}',
        /\{%\s*tab\b/            => '{% mdexp_tab',
        /\{%\s*endtab\s*%}/      => '{% endmdexp_tab %}',
        /\{%\s*tabs\b/            => '{% mdexp_tabs',
        /\{%\s*endtabs\s*%}/      => '{% endmdexp_tabs %}',
        /\{%\s*subtabs\b/            => '{% mdexp_subtabs',
        /\{%\s*endsubtabs\s*%}/      => '{% endmdexp_subtabs %}',
        /\{%\s*subtab\b/            => '{% mdexp_subtab',
        /\{%\s*endsubtab\s*%}/      => '{% endmdexp_subtab %}',
        /\{%\s*multi_lang_include\b/ => '{% mdexp_multi_lang_include'
      }
      replacements.each { |re, sub| content.gsub!(re, sub) }

      page_drop = item.to_liquid
      liquid_payload = site.site_payload.merge({ 'page' => page_drop })
      registers = { site: site, page: page_drop }

      site.liquid_renderer
          .file(item.relative_path)
          .parse(content)
          .render!(liquid_payload, registers: registers)
    end

    def self.copy_markdown_files(site)
      return unless should_copy?(site)
      all = site.pages + site.collections.flat_map { |_, c| c.docs }
      copied = 0

      all.each do |item|
        next unless should_capture?(item, site)
        merged = item.data[RAW_KEY].to_s
        next if merged.empty?

        dest = File.join(site.dest, output_path_for(item))
        FileUtils.mkdir_p(File.dirname(dest))
        File.write(dest, merged)
        copied += 1
      end

      Jekyll.logger.info "MarkdownCopyLLM:", "Exported #{copied} merged Markdown files"
      
      # Generate llms.txt after markdown files are created
      if defined?(Jekyll::LlmsTxtGenerator)
        Jekyll::LlmsTxtGenerator.generate_llms_txt(site)
      end
    end

    def self.output_path_for(item)
      url_path = item.url.sub(%r{^/}, '').sub(%r{/$}, '')
      url_path.empty? ? 'index.md' : File.join(url_path, 'index.md')
    end

    def self.should_copy?(site)
      site.config['markdown_copies'] != false &&
        (ENV['JEKYLL_ENV'] == 'production' || site.config['markdown_copies'] == true)
    end
  end
end

Jekyll::MarkdownCopyLLM.init
