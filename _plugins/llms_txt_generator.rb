require 'jekyll'

module Jekyll
  class LlmsTxtGenerator
    def self.init
      # This will be called by the markdown copy plugin after it completes
    end

    def self.generate_llms_txt(site)
      return unless should_generate_llms_txt?(site)
      
      # Get all markdown files from the site
      markdown_files = get_markdown_files(site)
      
      # Generate the llms.txt content
      content = generate_llms_content(site, markdown_files)
      
      # Write the llms.txt file directly to _site
      site_dir = site.dest || File.join(site.source, '_site')
      llms_path = File.join(site_dir, 'llms.txt')
      File.write(llms_path, content)
      
      Jekyll.logger.info "LlmsTxtGenerator:", "Generated llms.txt with #{markdown_files.length} markdown files"
    end

    def self.should_generate_llms_txt?(site)
      site.config['llms_txt'] != false && 
      (ENV['JEKYLL_ENV'] == 'production' || site.config['llms_txt'] == true)
    end

    def self.get_markdown_files(site)
      markdown_files = []
      site_dir = site.dest || File.join(site.source, '_site')
      
      # Define the main collections we want to include
      target_collections = ['user_guide', 'developer_guide', 'api']
      
      # Crawl _site directory for index.md files in target collections only
      if Dir.exist?(site_dir)
        target_collections.each do |collection|
          collection_dir = File.join(site_dir, collection)
          next unless Dir.exist?(collection_dir)
          
          Dir.glob(File.join(collection_dir, '**', 'index.md')).each do |file_path|
            relative_path = file_path.sub(site_dir, '').sub(/^\//, '')
            url_path = relative_path.sub(/\/index\.md$/, '/')
            
            # Skip files with minimal content (layout-driven navigation pages)
            content = File.read(file_path)
            content_stripped = content.strip
            
            # Skip if content is too short or just contains HTML breaks
            next if content_stripped.length < 50
            next if content_stripped.match?(/^(<br\s*\/?>|\s)+$/i)
            
            # Extract title from the markdown file
            title = extract_title_from_file(file_path)
            
            markdown_files << {
              title: title,
              url: "/#{url_path}",
              collection: collection,
              content: content
            }
          end
        end
      end
      
      markdown_files
    end


    def self.extract_title_from_file(file_path)
      return "Untitled" unless File.exist?(file_path)
      
      content = File.read(file_path)
      return "Untitled" if content.nil? || content.empty?
      
      # Try to extract title from first heading
      lines = content.split("\n")
      lines.each do |line|
        if line.match(/^#+\s+(.+)/)
          return line.gsub(/^#+\s+/, '').strip.to_s
        end
      end
      
      # Fallback: use first non-empty line (truncated)
      first_line = lines.find { |line| !line.strip.empty? }
      if first_line
        title = first_line.strip.to_s
        return title.length > 50 ? "#{title[0..47]}..." : title
      end
      
      "Untitled"
    end


    def self.group_files_by_section(files)
      sections = Hash.new { |h, k| h[k] = [] }
      
      files.each do |file|
        url_parts = file[:url].split('/').reject(&:empty?)
        
        # Get the first section after the collection name (1 level deep)
        # For URLs like /developer_guide/banners/... we want "Banners"
        # For URLs like /user_guide/message_building_by_channel/... we want "Message Building By Channel"
        if url_parts.length >= 2
          # Take the first part after the collection (index 1)
          section_name = url_parts[1].split('_').map(&:capitalize).join(' ')
        else
          # If no subdirectory, use "General"
          section_name = 'General'
        end
        
        sections[section_name] << file
      end
      
      sections
    end


    def self.generate_llms_content(site, markdown_files)
      base_url = site.config['homeurl'] || "https://www.braze.com"
      base_path = site.config['baseurl'] || ""
      
      content = <<~LLMS
        # Braze Documentation

        Braze is a comprehensive customer engagement platform that helps businesses build meaningful relationships with their customers through personalized messaging, automation, and analytics.

        ## Core Documentation Sections

      LLMS

      # Group files by collection
      collections = markdown_files.group_by { |file| file[:collection] }
      
      # Define collection descriptions
      collection_descriptions = {
        'user_guide' => 'The User Guide provides comprehensive information for marketers, product managers, and business users on how to use Braze\'s features and capabilities.',
        'developer_guide' => 'The Developer Guide provides technical documentation for developers integrating Braze SDKs.',
        'api' => 'Complete API documentation for programmatic access to Braze\'s features.'
      }

      collections.each do |collection_name, files|
        next if files.empty?
        
        collection_title = collection_name.split('_').map(&:capitalize).join(' ')
        description = collection_descriptions[collection_name] || "Documentation for #{collection_title.downcase}."
        
        content << "## #{collection_title}\n"
        content << "#{description}\n\n"
        
        # Group files by section (2 levels deep)
        sections = group_files_by_section(files)
        
        sections.each do |section_name, section_files|
          next if section_files.empty?
          
          content << "### #{section_name}\n"
          
          # Sort files by title
          sorted_files = section_files.sort_by { |file| (file[:title] || "Untitled").to_s }
          
          sorted_files.each do |file|
            # Add index.md to the end of the URL
            url_path = file[:url].end_with?('/') ? file[:url] + 'index.md' : file[:url] + '/index.md'
            full_url = "#{base_url}#{base_path}#{url_path}"
            title = file[:title] || "Untitled"
            content << "- [#{title}](#{full_url})\n"
          end
          
          content << "\n"
        end
      end

      content
    end
  end

end

# Initialize the plugin
Jekyll::LlmsTxtGenerator.init
