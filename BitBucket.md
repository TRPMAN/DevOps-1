# Bitbucket Config and Command

## bitbucket.org config file
Host bitbucket.org

 PreferredAuthentications publickey

 IdentityFile (private key pair)

## Good to Know command in this step
514  ssh -T git@bitbucket.org

517  git clone (bitbucket ssh url)

521  cat cicd-app/.git/config

524  mkdir cicd

525  cd cicd

526  git clone (target source code)

528  cat .git/config

529  git checkout aws-ci

530  git branch -a

532  git remote rm origin

534  git remote add origin (bitbucket ssh url)

535  cat .git/config

536  git push origin --all