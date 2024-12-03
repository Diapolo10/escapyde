# Escapyde Changelog

All notable changes to this project will be documented in this file.

The format is based on [CHANGELOG.md][Changelog]
and this project adheres to [Semantic Versioning][SemVer].

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

## [1.0.2] - 2024-12-03

Moved py.typed to the correct location.

### Fixed

- Fixed type annotation support when imported.

-->

_______________________________________________________________________________

## [1.0.2] - 2024-12-03

Moved py.typed to the correct location.

### Fixed

- Fixed type annotation support when imported.

_______________________________________________________________________________

## [1.0.1] - 2023-06-08

Fixed an issue with the Ruff workflow.

### Fixed

- Fixed Ruff running on tag releases

_______________________________________________________________________________

## [1.0.0] - 2023-06-08

Completely overhauled the `escapyde.ansi.AnsiEscape` class. This release breaks
backwards compatibility with manual use of the class, however use of the
provided colour shortcuts is not affected. `README.md` has also been updated.

### Added

- Added support for chaining formatting options
- Added new validators
- Added new examples to `README.md`, with screenshots
- New unit tests
- `SECURITY.md`

### Changed

- Updated dependencies
- Moved screenshots to an asset directory
- `escapyde.ansi.AnsiEscape` now works a lot differently

### Fixed

- Fixed chaining escape sequences

_______________________________________________________________________________

## [0.2.3] - 2023-06-07

Remembered to include `py.typed` in the package, and fixed a bug with the
`escape_format` function. Furthermore, identified a major bug with chained
escapes, which will be fixed in the next major update as it may require breaking
changes.

### Added

- Added `py.typed` - this time for real
- Added unit tests

### Changed

- Updated dependencies

### Fixed

- Fixed a bug where `escape_format` was forcing any replaced substrings to be
  lowercase. The casing in the output now matches the input.

_______________________________________________________________________________

## [0.2.2] - 2023-06-01

Updated dependencies, and added `py.typed` to show the package
is type-hinted.

### Added

- Added `py.typed`

### Changed

- Updated dependencies

_______________________________________________________________________________

## [0.2.1] - 2023-02-09

Updated metadata files, workflows, and dependencies.

### Added

- Added a whole bunch of new workflows
- Added Dependabot auto-updates
- Added a pull request template

### Changed

- Updated dependencies
- Updated some metadata

_______________________________________________________________________________

## [0.2.0] - 2022-01-16

This release adds a new function, `escapyde.escape_format`, which can be used
to format known substrings in a string with ANSI escape sequences. In addition
the codebase now uses type hints thorough.

The new feature was inspired by [this Reddit thread][Reddit escape format].

### Added

- Added `escapyde.escape_format`
- Added more type hints for better typing coverage

### Changed

- Updated the localisation files

_______________________________________________________________________________

## [0.1.2] - 2021-12-01

This release adds support for arbitrary types; previously `AnsiEscape` only
supported strings.

### Changed

- Changed `AnsiEscape` to support any type
- Updated the localisation files

_______________________________________________________________________________

## [0.1.1] - 2021-12-01

A hotfix release that fixes a problem in the README example code, and adds a
screenshot of the code running.

### Added

- Added a screenshot of the example code running in IPython

### Changed

- Updated the localisation files

### Fixed

- Fixed a mistake in the `README.md` example code related to string formatters
- Fixed the package name in `CHANGELOG.md`

_______________________________________________________________________________

## [0.1.0] - 2021-12-01

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

[Changelog]: http://changelog.md/
[Reddit escape format]: https://www.reddit.com/r/learnpython/comments/rvcg0l/print_colour_in_terminal/hr73v3f/
[SemVer]: http://semver.org/

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
