require 'jekyll'

module Jekyll
  class LlmsTxtGenerator
    RAW_MARKDOWN_KEY = "__export_merged_md"
    PUBLIC_MARKDOWN_KEY = "llm_markdown_content"

    def self.init
      # Generation is triggered by markdown_copy_llm.rb after markdown export completes.
    end

    def self.generate_llms_txt(site)
      return unless should_generate_llms_txt?(site)

      documents = developer_guide_documents(site)
      llms_content = generate_llms_content(site, documents)
      llms_full_content = generate_llms_full_content(site, documents)

      site_dir = site.dest || File.join(site.source, '_site')
      developer_guide_dir = File.join(site_dir, 'developer_guide')
      Dir.mkdir(developer_guide_dir) unless Dir.exist?(developer_guide_dir)
      llms_path = File.join(developer_guide_dir, 'llms.txt')
      llms_full_path = File.join(developer_guide_dir, 'llms-full.txt')

      File.write(llms_path, llms_content)
      File.write(llms_full_path, llms_full_content)

      Jekyll.logger.info(
        "LlmsTxtGenerator:",
        "Generated llms.txt and llms-full.txt with #{documents.length} developer guide pages"
      )
    end

    def self.should_generate_llms_txt?(site)
      site.config['llms_txt'] != false &&
      (ENV['JEKYLL_ENV'] == 'production' || site.config['llms_txt'] == true)
    end

    def self.developer_guide_documents(site)
      collection = site.collections['developer_guide']
      return [] unless collection

      docs = collection.docs.select { |doc| doc.output != false }
      ordered = sort_documents_like_nav_tree(docs)

      # Safety fallback: if any docs were not represented in the tree, append them.
      seen = {}
      ordered.each { |doc| seen[doc.url.to_s] = true }
      docs.each do |doc|
        ordered << doc unless seen[doc.url.to_s]
      end

      ordered
    end

    def self.sort_documents_like_nav_tree(documents)
      tree = build_nav_tree(documents)
      ordered = []
      flatten_nav_tree(tree, ordered)
      ordered
    end

    def self.build_nav_tree(documents)
      root = {}

      documents.each do |doc|
        path_parts = doc.url.to_s.split('/')
        path_parts.shift # leading empty value
        path_parts.shift # collection segment (developer_guide)

        current = root
        max_index = path_parts.length - 1

        path_parts.each_with_index do |segment, idx|
          next if segment.to_s.empty?

          key = segment.downcase
          current[:nav_list] ||= {}
          current[:children] ||= {}

          if idx < max_index
            unless current[:nav_list].key?(key)
              current[:nav_list][key] = {
                key: key,
                title: decode_slug_title(segment),
                weight: nil
              }
            end
            current[:children][key] ||= {}
            current = current[:children][key]
            next
          end

          current[:nav_list][key] = {
            key: key,
            title: page_title_for(doc, ""),
            weight: parse_weight(doc.data['page_order'])
          }
          current[:nav_pages] ||= {}
          current[:nav_pages][key] = doc unless doc.data['config_only']
        end
      end

      root
    end

    def self.flatten_nav_tree(node, output)
      nav_list = node[:nav_list] || {}
      return if nav_list.empty?

      sorted_entries = nav_list.values.sort_by do |entry|
        [entry[:weight].nil? ? 1 : 0, entry[:weight]]
      end

      sorted_entries.each do |entry|
        key = entry[:key]
        page = (node[:nav_pages] || {})[key]
        output << page if page

        child = (node[:children] || {})[key]
        flatten_nav_tree(child, output) if child
      end
    end

    def self.parse_weight(value)
      return nil if value.nil?

      Float(value)
    rescue
      nil
    end

    def self.decode_slug_title(text)
      text.to_s
          .gsub("%20", ' ')
          .gsub("+", ' ')
          .gsub('_', ' ')
          .gsub("%26", '&')
          .gsub("%2F", '/')
          .gsub("%3A", ':')
          .gsub("%3F", '?')
          .gsub("%2C", ',')
          .gsub("%2B", '+')
    end

    def self.page_title_for(doc, markdown)
      explicit_title = doc.data['article_title'] || doc.data['nav_title'] || doc.data['title']
      explicit = decode_slug_title(explicit_title.to_s).strip
      return explicit unless explicit.empty?

      extract_markdown_headings(markdown).each do |heading|
        return heading[:text] if heading[:level] == 1
      end

      "Untitled"
    end

    def self.page_markdown_for(doc)
      merged = doc.data[RAW_MARKDOWN_KEY] || doc.data[PUBLIC_MARKDOWN_KEY]
      content = merged.to_s.strip
      content = doc.content.to_s if content.empty?
      content.to_s
    end

    def self.path_for_llms(doc, site)
      base_path = site.config['baseurl'].to_s
      doc_path = doc.url.to_s
      suffix = doc_path.end_with?('/') ? 'index.md' : '/index.md'
      "#{base_path}#{doc_path}#{suffix}"
    end

    def self.extract_markdown_headings(markdown)
      headings = []
      in_code_block = false

      markdown.to_s.each_line do |line|
        stripped = line.strip

        if stripped.start_with?("```")
          in_code_block = !in_code_block
          next
        end
        next if in_code_block

        match = line.match(/^(#+)\s+(.+?)\s*#*\s*$/)
        next unless match

        heading_text = cleanup_inline_markdown(match[2])
        next if heading_text.empty?

        headings << {
          level: match[1].length,
          text: heading_text
        }
      end

      headings
    end

    def self.cleanup_inline_markdown(text)
      clean = text.to_s.dup
      clean.gsub!(/`([^`]+)`/, '\1')
      clean.gsub!(/\[([^\]]+)\]\([^)]+\)/, '\1')
      clean.gsub!(/\*\*([^*]+)\*\*/, '\1')
      clean.gsub!(/\*([^*]+)\*/, '\1')
      clean.gsub!(/_{1,2}([^_]+)_{1,2}/, '\1')
      clean.gsub!(/\{%\s*.*?\s*%\}/, '')
      clean.gsub!(/\{\{\s*.*?\s*\}\}/, '')
      clean.gsub!(/\s+/, ' ')
      clean.strip
    end

    def self.extract_summary(markdown)
      in_code_block = false
      markdown.to_s.each_line do |line|
        stripped = line.strip
        if stripped.start_with?("```")
          in_code_block = !in_code_block
          next
        end
        next if in_code_block
        next if stripped.empty?
        next if stripped.match?(/\A<\/?[\w:-]+[^>]*>\z/)
        next if stripped.start_with?('#', '>', '-', '*', '|', '{%', '{{')

        summary = cleanup_inline_markdown(stripped)
        return summary unless summary.empty?
      end

      ""
    end

    def self.strip_frontmatter(markdown)
      text = markdown.to_s
      return text unless text.start_with?("---\n")

      parts = text.split(/^---\s*$\n?/, 3)
      return text if parts.length < 3

      parts[2].to_s
    end

    def self.normalize_full_text(markdown)
      clean = strip_frontmatter(markdown)
      clean = clean.gsub(/\r\n?/, "\n")
      clean = clean.gsub(/\t/, "  ")
      clean = clean.gsub(/\{%\s*.*?\s*%\}/m, '')
      clean = clean.gsub(/\{\{\s*.*?\s*\}\}/m, '')
      clean = clean.gsub(/\n{3,}/, "\n\n")
      clean.strip
    end

    def self.strip_html(text)
      text.to_s.gsub(/<[^>]*>/, ' ').gsub(/\s+/, ' ').strip
    end

    def self.full_text_fallback_from_frontmatter(doc)
      lines = []
      top = strip_html(doc.data['guide_top_text'])
      desc = strip_html(doc.data['description'])

      guide_header = strip_html(doc.data['guide_top_header'])
      lines << guide_header unless guide_header.empty?
      lines << top unless top.empty?
      lines << desc unless desc.empty?

      featured = doc.data['guide_featured_list']
      if featured.is_a?(Array) && !featured.empty?
        lines << "Featured:"
        featured.each do |item|
          next unless item.is_a?(Hash)
          name = strip_html(item['name'])
          lines << "- #{name}" unless name.empty?
        end
      end

      lines.join("\n").strip
    end

    def self.full_text_for_doc(doc, markdown)
      normalized = normalize_full_text(markdown)
      return normalized unless normalized.empty?

      full_text_fallback_from_frontmatter(doc)
    end

    def self.generate_llms_content(site, documents)
      content = <<~LLMS
        # Braze Documentation

        Index of all Developer Guide pages and their headings.

        ## Developer Guide

      LLMS

      documents.each do |doc|
        markdown = page_markdown_for(doc)
        title = page_title_for(doc, markdown)
        path = path_for_llms(doc, site)
        summary = extract_summary(markdown)
        headings = extract_markdown_headings(markdown)

        if summary.empty?
          content << "- [#{title}](#{path})\n"
        else
          content << "- [#{title}](#{path}): #{summary}\n"
        end

        headings.each do |heading|
          indent = '  ' * heading[:level]
          content << "#{indent}- #{'#' * heading[:level]} #{heading[:text]}\n"
        end

        content << "\n"
      end

      content
    end

    def self.generate_llms_full_content(site, documents)
      content = <<~LLMS
        # Braze Developer Guide Full Text

        Consolidated full markdown text for all pages in the Developer Guide collection.

      LLMS

      documents.each do |doc|
        markdown = page_markdown_for(doc)
        title = page_title_for(doc, markdown)
        path = path_for_llms(doc, site)
        normalized = full_text_for_doc(doc, markdown)
        next if normalized.empty?

        content << "# #{title}\n\n"
        content << "Source: #{path}\n\n"
        content << "#{normalized}\n\n"
      end

      content
    end
  end

end

# Initialize the plugin
Jekyll::LlmsTxtGenerator.init
