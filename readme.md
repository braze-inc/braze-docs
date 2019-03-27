# Success!!

This repository houses the content on Braze's [Docs](https://braze.com/docs/), the [User Guide](https://braze.com/docs/user_guide/), and the [Developer Guide](https://braze.com/docs/developer_guide/).

## Initial Setup
For friends in Success, Product, and Marketing, please find the necessary steps [here](https://github.com/Appboy/success/wiki/Setting-up-your-local-environment).

For friends in Engineering (or anyone using rbenv) - if you are having problems related to ruby versions (i.e. `ruby -v`  tells you that you are not on 2.2.4), try adding the following to your .bash_profile:
```
if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi
```

## SITE UPDATE
Documentation is currently being updated and redesigned.  If you're having trouble with the new site, and getting build error, try the following steps:

* Assume basic Jekyll local installed already done, otherwise follow [Wiki instructions](https://github.com/Appboy/success/wiki/Setting-up-your-local-environment).
* Optional: Upgrade rvm
  * `rvm get stable`
* Upgrade Ruby
  * `rvm install ruby-2.5.1`
* Have rvm using new Ruby
  * `rvm use ruby-2.5.1`
* Update Jekyll and Gems
  * `gem install bundler`
  * `bundle install`

Afterwards, you should be able to do the normal Jekyll build or rake process.

## Wiki
For more information on this repository and making changes to the [User Guide](https://braze.com/docs/user_guide/) and the [Developer Guide](https://braze.com/docs/developer_guide/), please visit the wiki [here](https://github.com/Appboy/success/wiki).

## Heroku Setup (ignore unless your name is Sal)
#### Git Config
```
git remote add staging https://git.heroku.com/ab-success.git
git remote add production https://git.heroku.com/ab-success-production.git
git remote add -t master -m master -f secure git@github.com:AppboySecure/success.git
git checkout -b master -t secure/master
git checkout develop
```
#### Ruby
```
brew update && brew upgrade ruby-build && brew upgrade rbenv-gemset;
eval "$(rbenv init -)"
rbenv install 2.2.4
rbenv local 2.2.4
gem install bundler -v 1.11.2
rbenv rehash
bundle install
```
### Heroku
#### Logs
##### Staging
`heroku logs --remote staging`
##### Production
`heroku logs --remote production`
#### Deploy
##### Staging
`git push staging develop:master`
##### Production
`git push production master:master`

## Herokou Troubleshooting Pull Request
To view logs for Heroku pull request, get access to ab-success on heroku, and follow heroku documentation to get the [CLI install](https://devcenter.heroku.com/articles/heroku-cli)

### Custom git Pull Request Remote
Add Custom Pull Request to remote (Replace testpr with desire remote name)
```
git remote add testpr https://git.heroku.com/ab-success-pr-[pullrequestnumber].git
```
Or rename existing remote with the Pull Request
```
git remote set-url testpr https://git.heroku.com/ab-success-pr-[pullrequestnumber].git
```

### View Pull Request Log
To pull the request log (or replace testpr with previous remote name)
```
heroku logs --remote testpr
```
