
# IPlib3 Change Log

All notable changes to this project will be documented in this file.

The format is based on [CHANGELOG.md](http://changelog.md/)
and this project adheres to [Semantic Versioning](http://semver.org/).

<!-- 
TEMPLATE

## [major.minor.patch] - yyyy-mm-dd

A message that notes the main changes in the update.

### Added

### Changed

### Deprecated

### Fixed

### Removed

### Security

_______________________________________________________________________________
 
 -->

<!--
EXAMPLE

## [0.2.0] - 2021-06-02

Lorem Ipsum dolor sit amet.

### Added

- Cat pictures hidden in the library
- Added beeswax to the gears

### Changed

- Updated localisation files

-->

<!--
_______________________________________________________________________________

## [0.2.3] - YYYY-MM-DD

First official documentation.

### Added

- Documentation
- Now using specific versions for the dependencies

### Changed

- Changed the filename of `deploy.yml` to `pypi_deploy.yml` to get rid of a YAML validator complaint
- Updated dependencies

-->

_______________________________________________________________________________

## [0.1.0] - 2021-05-01

This is the beginning of the changelog. Previously made commits have not been
tracked, and there are no plans to distinguish them. You may consider this
the initial commit.

### Added

- Added Poetry files and build system
- Added a Lorem Ipsum example text snippet
- Added GitHub Actions
- Added autonatic PyPI releases
- Added 'clear' as a built-in formatting option
- Added a `Makefile`
- Added docstrings thorought the package

### Changed

- The releases are now built on the latest version of Ubuntu, using Python 3.9
- `README.md` now has more content, including example usage
- Default colours are now available from the top level of the package
  (eg. `escapyde.FRED` instead of `escapyde.colours.FRED`)
- Updated the localisation files

### Fixed

- Fixed an oversight related to chaining ANSI escape sequences
- Fixed linter issues

<!-- markdownlint-configure-file {
    "MD022": false,
    "MD024": false,
    "MD030": false,
    "MD032": false
} -->
<!--
    MD022: Blanks around headings
    MD024: No duplicate headings
    MD030: Spaces after list markers
    MD032: Blanks around lists
-->
