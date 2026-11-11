import os
import re
import shutil
import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent


@pytest.fixture(scope="module")
def files_pattern() -> re.Pattern[str]:
    hooks = yaml.safe_load((ROOT / ".pre-commit-hooks.yaml").read_text())
    matching_hooks = [hook for hook in hooks if hook.get("id") == "zizmor"]
    assert len(matching_hooks) == 1, (
        f"expected exactly one zizmor hook, found {len(matching_hooks)}"
    )
    return re.compile(matching_hooks[0]["files"])


@pytest.mark.parametrize(
    ("path", "should_match"),
    [
        (".github/workflows/ci.yml", True),
        (".github/workflows/ci.yaml", True),
        (".github/workflows/dependabot.yml", True),
        ("vendored/repo/.github/workflows/ci.yml", True),
        (".github/workflows/nested/ci.yml", False),
        (".github/workflows/.yml", False),
        (".github/workflows/ci.json", False),
        (".github/workflows/ci.yml.bak", False),
        ("foo.github/workflows/ci.yml", False),
        (".github/dependabot.yml", True),
        (".github/dependabot.yaml", True),
        ("vendored/repo/.github/dependabot.yml", True),
        (".github/dependabotXyml", False),
        (".github/dependabot-yml.yaml", False),
        ("action.yml", True),
        ("action.yaml", True),
        ("some/nested/action.yml", True),
        ("faction.yml", False),
        ("transaction.yaml", False),
        ("my-action.yml", False),
        ("action.yml.bak", False),
        (".pre-commit-config.yml", True),
        (".pre-commit-config.yaml", True),
        ("subproject/.pre-commit-config.yaml", True),
        ("pre-commit-config.yaml", False),
        (".pre-commit-config.yaml.bak", False),
        (".pre-commit-hooks.yml", True),
        (".pre-commit-hooks.yaml", True),
        ("subproject/.pre-commit-hooks.yaml", True),
        ("ci.yml", False),
        ("workflows/ci.yml", False),
    ],
)
def test_files_pattern(
    files_pattern: re.Pattern[str], path: str, should_match: bool
) -> None:
    matched = files_pattern.search(path) is not None
    assert matched == should_match


def test_hook_audits_supported_inputs(tmp_path: Path) -> None:
    repository = tmp_path / "repository"
    shutil.copytree(ROOT / "tests" / "fixtures", repository)
    inputs = sorted(
        str(path.relative_to(repository))
        for path in repository.rglob("*")
        if path.is_file()
    )
    assert inputs, "no fixture inputs found"

    subprocess.run(["git", "init", "--quiet"], cwd=repository, check=True)
    subprocess.run(["git", "add", "--all"], cwd=repository, check=True)

    env = os.environ | {
        "PRE_COMMIT_HOME": str(tmp_path / "pre-commit-cache"),
        "ZIZMOR_OFFLINE": "true",
    }
    result = subprocess.run(
        [
            "pre-commit",
            "try-repo",
            str(ROOT),
            "zizmor",
            "--all-files",
            "--verbose",
        ],
        cwd=repository,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout
    for path in inputs:
        assert f"completed {path}" in result.stdout
