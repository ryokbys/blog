#!/bin/bash

cwd=`pwd`
maindir=/Users/kobayashi/Dropbox/Public/pelican_blog
cd $maindir
rsync -avz ./output/* nitweb:httpdocs/contents/blog/
cd $cwd
