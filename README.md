# zizmor-pre-commit

[![image](https://img.shields.io/pypi/v/zizmor/1.25.2.svg)](https://pypi.python.org/pypi/zizmor)
[![image](https://img.shields.io/pypi/l/zizmor/1.25.2.svg)](https://pypi.python.org/pypi/zizmor)
[![Actions status](https://github.com/zizmorcore/zizmor-pre-commit/workflows/main/badge.svg)](https://github.com/zizmorcore/zizmor-pre-commit/actions)

A [pre-commit](https://pre-commit.com/) hook for [zizmor](https://github.com/zizmorcore/zizmor).

Distributed as a standalone repository to enable installing `zizmor` via prebuilt wheels from
[PyPI](https://pypi.org/project/zizmor/).

### Using zizmor with pre-commit

To run zizmor via pre-commit, add the following to your `.pre-commit-config.yaml`:

```yaml
repos:
- repo: https://github.com/zizmorcore/zizmor-pre-commit
  # Zizmor version.
  rev: v1.25.2
  hooks:
    # Run the linter.
    - id: zizmor
```

To autofix issues, set the following args:

```yaml
repos:
- repo: https://github.com/zizmorcore/zizmor-pre-commit
  # Zizmor version.
  rev: v1.24.1
  hooks:
    # Run the linter.
    - id: zizmor
      args: [--no-progress, --fix]
```

(`--no-progress` must be specified since that arg exists in the repo's hook configuration, and `args` overrides all existing args)

[zizmor-pre-commit#22]: https://github.com/zizmorcore/zizmor-pre-commit/issues/22

## License

zizmor-pre-commit is licensed under:

- MIT license ([LICENSE](LICENSE) or <https://opensource.org/licenses/MIT>)
