# CarsonDavis.github.io

Personal blog built with Jekyll and the Chirpy theme. Images are hosted on S3 with an automated Lambda pipeline that generates WebPs and LQIP thumbnails.

## Getting Started

### Prerequisites

Follow the [Jekyll installation docs](https://jekyllrb.com/docs/installation/) and install [Git](https://git-scm.com/).

### Installation

```bash
bundle install
```

See the [Chirpy theme docs](https://github.com/cotes2020/jekyll-theme-chirpy#documentation) for theme-specific details.

## Running Locally

```bash
bundle exec jekyll serve --unpublished
```

If the build is acting up, burn the cache and rebuild:

```bash
rm -rf .jekyll-cache _site
bundle exec jekyll build --trace
```

Replicate the GitHub Actions HTML validation:

```bash
bundle exec htmlproofer ./_site --disable-external
```

## Documentation

| Doc | Contents |
|-----|----------|
| [Writing Posts](docs/writing-posts.md) | Frontmatter, image tags, grid layouts, upload workflow |
| [Image Pipeline](docs/image-pipeline.md) | S3 folder structure, Lambda architecture, LQIP specs |
| [Infrastructure](docs/infrastructure.md) | AWS resources, SAM template, CI/CD, monitoring |
| [Migration](docs/migration.md) | Migrating old posts to the new image system |
