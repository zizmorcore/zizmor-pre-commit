# zizmor-pre-commit

[![image](https://img.shields.io/pypi/v/zizmor/1.17.0.svg)](https://pypi.python.org/pypi/zizmor)
[![image](https://img.shields.io/pypi/l/zizmor/1.17.0.svg)](https://pypi.python.org/pypi/zizmor)
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
  rev: v1.17.0
  hooks:
    # Run the linter.
    - id: zizmor
```

> [!IMPORTANT]
> Starting with v1.17.0, the default behavior of the hook changed from collecting
> a specific set of YAML inputs (within pre-commit itself) to allowing `zizmor` to
> discover inputs internally. This is both faster and more consistent with how
> `zizmor` expects to be invoked, but it may be a breaking change for some users
> who have explicitly configured inputs.
> 
> See [zizmor-pre-commit#22] for additional information.

[zizmor-pre-commit#22]: https://github.com/zizmorcore/zizmor-pre-commit/issues/22

## License

zizmor-pre-commit is licensed under:

- MIT license ([LICENSE](LICENSE) or <https://opensource.org/licenses/MIT>)
