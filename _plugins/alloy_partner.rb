# https://github.com/dimitri-koenig/jekyll-plugins
# modified to allow variable url
require 'net/http'
require 'uri'

module Jekyll

  class AlloyPartner < Liquid::Tag
    PARTNER_URL = "https://b7pblshe.api.sanity.io/vX/data/query/marketing-prod?query=*%5B_type+%3D%3D+%22technologyPartner%22+%26%26+language+%3D%3D+%24locale%5D%7B%0A++%22slug%22%3A+seo.slug.current%2C%0A++%22integration_partner_id%22%3A+integrationPartnerId%2C%0A++%22alloysId%22%3A+integrationPartnerId%2C%0A++%22partner_name%22%3A+title%2C%0A++%22partner_logo_url%22%3A+company-%3Elogotype.default.asset-%3Eurl%2C%0A++%22partner_description%22%3A+pt%3A%3Atext%28whatIsIt%29%2C%0A++%22partner_featured%22%3A+isFeaturedPartner%2C%0A++%22partner_featured_short_description%22%3A+featuredPartnerShortDescription%2C%0A++%22partner_and_braze_description%22%3A+pt%3A%3Atext%28howWeWorkTogether%29%2C%0A++%22partner_website_url%22%3A+company-%3Eurl%2C%0A++%22partner_specialties%22%3A+partnerSpecialty-%3Ename%5B_key+%3D%3D+%24locale%5D.value%2C%0A++%22partner_categories%22%3A+partnerCategories%5B%5D-%3Ename%5B_key+%3D%3D+%24locale%5D.value%2C%0A++%22partner_integration_methods%22%3A+partnerIntegrationMethods%2C%0A++%22dashboard_integration_methods%22%3A+dashboardIntegrationMethods%5B%5D%7B%0A++++%22integration_method_id%22%3A+methodId%2C%0A++++%22method_title%22%3A+title%2C%0A++++%22documentation%22%3A+%7B%0A++++++%22braze_documentation_url%22%3A+brazeDocumentationUrl%2C+%0A++++++%22partner_documentation_url%22%3A+partnerDocumentationUrl%0A++++%7D%0A++%7D%2C%0A++%22jsonUrl%22%3A+%22https%3A%2F%2Fb7pblshe.api.sanity.io%2Fv2022-03-07%2Fdata%2Fquery%2Fmarketing-prod%3Fquery%3D*%255B_type%2B%253D%253D%2B%2522technologyPartner%2522%2B%2526%2526%2Blanguage%2B%253D%253D%2B%2524locale%2B%2526%2526%2BintegrationPartnerId%2B%253D%253D%2B%2524id%255D%255B0%255D%257B%250A%2B%2B%2522slug%2522%253A%2Bseo.slug.current%252C%250A%2B%2B%2522integration_partner_id%2522%253A%2BintegrationPartnerId%252C%250A%2B%2B%2522alloysId%2522%253A%2BintegrationPartnerId%252C%250A%2B%2B%2522partner_name%2522%253A%2Btitle%252C%250A%2B%2B%2522partner_logo_url%2522%253A%2Bcompany-%253Elogotype.default.asset-%253Eurl%252C%250A%2B%2B%2522partner_description%2522%253A%2Bpt%253A%253Atext%2528whatIsIt%2529%252C%250A%2B%2B%2522partner_featured%2522%253A%2BisFeaturedPartner%252C%250A%2B%2B%2522partner_featured_short_description%2522%253A%2BfeaturedPartnerShortDescription%252C%250A%2B%2B%2522partner_and_braze_description%2522%253A%2Bpt%253A%253Atext%2528howWeWorkTogether%2529%252C%250A%2B%2B%2522partner_website_url%2522%253A%2Bcompany-%253Eurl%252C%250A%2B%2B%2522partner_specialties%2522%253A%2BpartnerSpecialty-%253Ename%255B_key%2B%253D%253D%2B%2524locale%255D.value%252C%250A%2B%2B%2522partner_categories%2522%253A%2BpartnerCategories%255B%255D-%253Ename%255B_key%2B%253D%253D%2B%2524locale%255D.value%252C%250A%2B%2B%2522partner_integration_methods%2522%253A%2BpartnerIntegrationMethods%252C%250A%2B%2B%2522dashboard_integration_methods%2522%253A%2BdashboardIntegrationMethods%255B%255D%257B%250A%2B%2B%2B%2B%2522integration_method_id%2522%253A%2BmethodId%252C%250A%2B%2B%2B%2B%2522method_title%2522%253A%2Btitle%252C%250A%2B%2B%2B%2B%2522documentation%2522%253A%2B%257B%250A%2B%2B%2B%2B%2B%2B%2522braze_documentation_url%2522%253A%2BbrazeDocumentationUrl%252C%2B%250A%2B%2B%2B%2B%2B%2B%2522partner_documentation_url%2522%253A%2BpartnerDocumentationUrl%250A%2B%2B%2B%2B%257D%250A%2B%2B%257D%252C%250A%257D%26%2524id%3D%2522%22+%2B+integrationPartnerId+%2B+%22%2522%26%2524locale%3D%2522en-us%2522%22%0A%7D&%24locale=%22en-us%22"

    def initialize(tag_name, markup, tokens)
      super
    end

    def render(context)
      site = context.registers[:site]
      # partnerembed = context.config['partner_api']
      partnerembed = site.config['partner_api']
      if ENV["PARTNER_API"].to_s.downcase != 'true'
        partnerembed = false
      end

      if partnerembed
        lang = site.config['language'] || 'en'
        url = PARTNER_URL
        case lang
        when 'ja'
          url.gsub!('locale=%22en-us%22', 'locale=%22ja%22')
        end

        if context['site']['data'].include?(url)
          puts 'Using cache for: ' + url.split('?')[0]
          return context['site']['data'][url]
        else
          puts 'Fetching content of url: ' + url.split('?')[0]
          if url =~ URI::regexp
            @results = fetchContent(url)
          else
            puts 'Error fetching: ' + url
          end

          if @results.code != '200'
            puts 'Error returning results: ' + url
            context['site']['data'][url] = '{}'
            return '{}'
          else
            if @results.body
              results_hash = JSON.parse(@results.body.force_encoding('UTF-8'))
              results_hash.delete("query")
              if (results_hash.key?("result"))
                results_hash["result"].each { |rw|
                  rw.delete("jsonUrl")
                }
              end
              context['site']['data'][url] = results_hash.to_json
              return context['site']['data'][url]
            else
              puts 'Empty content from : ' + url
              return '{}'
            end
          end
        end
      else
        return '{}'
      end
    end

    def fetchContent(url)
      link = URI.parse(url.strip)
      http = Net::HTTP.new(link.host, link.port)
      http.open_timeout = 60
      http.read_timeout = 120
      res = Net::HTTP.get_response(link)
      return res
    end
  end
end

Liquid::Template.register_tag('alloy_partner', Jekyll::AlloyPartner)
