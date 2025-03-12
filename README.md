# zizmor-pre-commit

[![image](https://img.shields.io/pypi/v/zizmor/1.5.1.svg)](https://pypi.python.org/pypi/zizmor)
[![image](https://img.shields.io/pypi/l/zizmor/1.5.1.svg)](https://pypi.python.org/pypi/zizmor)
[![image](https://img.shields.io/pypi/pyversions/zizmor/1.5.1.svg)](https://pypi.python.org/pypi/zizmor)
[![Actions status](https://github.com/woodruffw/zizmor-pre-commit/workflows/main/badge.svg)](https://github.com/woodruffw/zizmor-pre-commit/actions)

A [pre-commit](https://pre-commit.com/) hook for [Zizmor](https://github.com/woodruffw/zizmor).

Distributed as a standalone repository to enable installing Zizmor via prebuilt wheels from
[PyPI](https://pypi.org/project/zizmor/).

### Using Zizmor with pre-commit

To run zizmor via pre-commit, add the following to your `.pre-commit-config.yaml`:

```yaml
repos:
- repo: https://github.com/woodruffw/zizmor-pre-commit
  # Zizmor version.
  rev: v1.5.1
  hooks:
    # Run the linter.
    - id: zizmor
```

## License

zizmor-pre-commit is licensed under:

- MIT license ([LICENSE](LICENSE) or <https://opensource.org/licenses/MIT>)
