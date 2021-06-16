FROM ruby:2.6.5
RUN apt-get update && apt-get install -y build-essential gcc wget git locales locales-all openjdk-11-jre-headless
RUN apt-get clean
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
WORKDIR /app
COPY . .
RUN gem install bundler 
RUN bundle install 
EXPOSE 4000
CMD rake