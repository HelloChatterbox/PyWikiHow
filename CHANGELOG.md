# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.5.0]  - 2019-12-12

Breaking Changes, api is backward incompatible

### Changed

- Refactor into individual classes
    - WikiHow
    - HowTo
    - HowToStep
- Refactor search
    - WikiHow.search is now a generator
    - search now returns HowTo objects instead of urls
- split examples in several files

### Added

- search_wikihow function
- ParseError exception

### Fixed

- handle parse errors

## [0.3.1]  - 2019-12-12

### Changed

- Transfered ownership to [OpenJarbas](https://github.com/OpenJarbas)
- Made a changelog

[unreleased]: https://github.com/OpenJarbas/PyWikiHow/tree/dev
[0.5.0]: https://github.com/OpenJarbas/PyWikiHow/tree/0.5.0
[0.3.1]: https://github.com/OpenJarbas/PyWikiHow/tree/0.3.1
