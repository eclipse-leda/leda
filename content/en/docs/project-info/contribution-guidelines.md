---
title: "Contribution Guidelines"
date: 2022-05-09T14:24:56+05:30
weight: 5
---

Thanks for considering to contribute to Eclipse Leda. We really appreciate the time and effort you want to spend helping to improve the project.

In order to get you started as fast as possible we need to go through some organizational issues first, though.

## Eclipse Development Process

This Eclipse Foundation open project is governed by the Eclipse Foundation
Development Process and operates under the terms of the Eclipse IP Policy.

* https://eclipse.org/projects/dev_process
* https://www.eclipse.org/org/documents/Eclipse_IP_Policy.pdf

## Eclipse Contributor Agreement

Before your contribution can be accepted by the project team contributors must
electronically sign the Eclipse Contributor Agreement (ECA).

- [http://www.eclipse.org/legal/ECA.php](http://www.eclipse.org/legal/ECA.php)

Commits that are provided by non-committers must have a Signed-off-by field in
the footer indicating that the author is aware of the terms by which the
contribution has been provided to the project. The non-committer must
additionally have an Eclipse Foundation account and must have a signed Eclipse
Contributor Agreement (ECA) on file.

For more information, please see the Eclipse Committer Handbook:
[https://www.eclipse.org/projects/handbook/#resources-commit](https://www.eclipse.org/projects/handbook/#resources-commit)

## Making Your Changes

- Fork the repository on GitHub.
- Create a new branch for your changes.
  - *Note: When forking multiple repositories (eg most of the time, you also need to make modifications to meta-leda), please use the same branch name of each repository.*
- Make your changes following the code style guide for the respective type of content:
  - BitBake Recipes: https://www.openembedded.org/wiki/Styleguide
  - Documentation: https://www.docsy.dev/docs/best-practices/
  - Shell Scripts (Example Style Guide): https://google.github.io/styleguide/shellguide.html
- When you create new files make sure you include a proper license header at the top of the file (see License Header section below).
- Make sure you include test cases for non-trivial features.
- Make sure the test suite passes after your changes.
- Commit your changes into that branch.
- Use descriptive and meaningful commit messages. Start the first line of the commit message with the a GitHub Issue number if available and a title e.g. `[#9865] Add token based authentication`.
- Squash multiple commits that are related to each other semantically into a single one.
- Make sure you use the `-s` flag when committing as explained above.
- Push your changes to your branch in your forked repository.
- Once you're satisfied with your contribution, open a Pull Request and Eclipse Leda Committers will start with the review of your changes.
  - *Note: When working with multiple repositories, you need to open separate Pull Requests for each repository.*

## Adding Documentation to Hugo

- Add the markdown document to the appropriate folder in the path `leda/content/en`.
- Add the front-matter

```yaml
---
title: "title of the file"
date: 2022-05-09T13:43:25+05:30
---
```

- Additional front matter that can be added –
  - url : &quot;specifying a definite url to the file&quot;
  - weight : 10 (used for ordering your content in lists. Lower weight gets higher precedence.)
- The images need to be put in path `leda/static/assets`. The image reference should be `/assets/image.jpg` in the markdown file.
  (Note: Do not use relative paths or url)
- In case you are creating a new folder, create \_index.md file with the front matter only.

## Running Locally

- Install hugo version 0.98.0 extended [Release v0.98.0 · gohugoio/hugo (github.com)](https://github.com/gohugoio/hugo/releases/tag/v0.98.0)
- Install Docsy theme in the path leda/themes/docsy –

```bash
#Run this command from root directory of velocitas-docs
git clone https://github.com/google/docsy.git themes/docsy
```

- Install pre-requisites

```bash
cd themes/docsy/userguide/
npm install
npm install --save-dev postcss
```

- From the leda directory run the command **hugo server** visit localhost:1313 to see the rendered static site.

## Submitting the Changes

Submit a pull request via the normal GitHub UI.

## After Submitting

- Do not use your branch for any other development, otherwise further changes that you make will be visible in the PR.

## License Header

Please make sure any file you newly create contains a proper license header like this:

```bash
# /********************************************************************************
# * Copyright (c) 2022 Contributors to the Eclipse Foundation
# *
# * See the NOTICE file(s) distributed with this work for additional
# * information regarding copyright ownership.
# *
# * This program and the accompanying materials are made available under the
# * terms of the Apache License 2.0 which is available at
# * https://www.apache.org/licenses/LICENSE-2.0
# *
# * SPDX-License-Identifier: Apache-2.0
# ********************************************************************************/
```

You should, of course, adapt this header to use the specific mechanism for comments pertaining to the type of file you create.

**Important**

Please do not forget to add your name/organization to the `LICENSE` file's _Copyright Holders_ section. If this is not the first contribution you make, then simply update the time period contained in the copyright entry to use the year of your first contribution as the lower boundary and the current year as the upper boundary, e.g.

`Copyright 2017, 2018 ACME Corporation`

## Build

- On every PR merge a pipeline run will be triggered. This run will trigger the hugo docs build
- Hugo v0.98.0 extended is set up for the runner
- Docsy theme is setup for beautification of static site
- Then dependencies are installed for the theme
- Static site is generated and stored in a folder &quot;public&quot;
- The contents of public are committed to gh_pages branch which is exposed to host the github pages
