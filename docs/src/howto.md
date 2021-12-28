# Project Documentation

## Get Started
Documentation can be written as rst or md files in the `codershq/docs/src`.


To build and serve docs, use the commands:

    docker-compose -f local.yml up docs

Changes to files in `docs/src` will be picked up and reloaded automatically.

[MdBook](https://rust-lang.github.io/mdBook) is the tool used to build documentation.

## CI

Coders HQ has a CI workflow with github-pages in the `github-pages` branch which executes whenever a push happens to main like. 

An example workflow `.github/workflows/gh-pages.yml` with [GitHub Actions for GitHub Pages].
For the first deployment, we have to do this operation: [First Deployment with `GITHUB_TOKEN` - peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages#%EF%B8%8F-first-deployment-with-github_token)

[GitHub Actions for GitHub Pages]: https://github.com/peaceiris/actions-gh-pages

[![peaceiris/actions-gh-pages - GitHub](https://gh-card.dev/repos/peaceiris/actions-gh-pages.svg?fullname)](https://github.com/peaceiris/actions-gh-pages)

```yml
name: github pages

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  deploy:
    runs-on: ubuntu-20.04
    concurrency:
      group: ${{ github.workflow }}-${{ github.ref }}
    steps:
      - uses: actions/checkout@v2

      - name: Setup mdBook
        uses: peaceiris/actions-mdbook@v1
        with:
          mdbook-version: 'latest'
        
      - run: mdbook build
        working-directory: ./docs
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        if: ${{ github.ref == 'refs/heads/main'}}
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./docs/book
```

## Use a specific version of mdBook

Set `mdbook-version: '0.4.10'` to use version 0.4.10 of mdBook.

```yaml
- name: Setup mdBook
  uses: peaceiris/actions-mdbook@v1
  with:
    mdbook-version: '0.4.10'
```

This action fetches the latest version of mdBook by [mdbook — Homebrew Formulae](https://formulae.brew.sh/formula/mdbook)