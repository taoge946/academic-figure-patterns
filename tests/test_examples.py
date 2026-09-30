"""Every example script runs headless, writes its figure, and reproduces its committed data.

Scripts write to fixed relative paths, so each test runs them in a temporary copy of the repository.
Figures are only checked for existence (font availability changes pixels across machines); the arrays
behind the synthetic figures are compared numerically with the committed .npz files.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = sorted(p.name for p in (ROOT / "examples").glob("*.py"))
AFTER = [n for n in EXAMPLES if n[:3] in {"11a", "11b", "11c", "11d", "12a", "12b", "12c", "12d", "12e"}]


@pytest.fixture(scope="module")
def workdir(tmp_path_factory):
    d = tmp_path_factory.mktemp("repo")
    shutil.copytree(ROOT / "afp", d / "afp")
    shutil.copytree(ROOT / "examples", d / "examples")
    return d


def run(workdir, script):
    env = dict(os.environ, MPLBACKEND="Agg", PYTHONPATH=str(workdir))
    return subprocess.run([sys.executable, f"examples/{script}"], cwd=workdir, env=env,
                          capture_output=True, text=True, timeout=300)


@pytest.mark.parametrize("script", EXAMPLES)
def test_example_runs(workdir, script):
    res = run(workdir, script)
    assert res.returncode == 0, res.stderr[-2000:]
    assert not (workdir / "figures").exists(), "examples must write into examples/figures/"


@pytest.mark.parametrize("script", AFTER)
def test_example_data_reproducible(workdir, script):
    key = script[:3]
    committed = np.load(ROOT / "examples" / "data" / f"{key}.npz")
    res = run(workdir, script)
    assert res.returncode == 0, res.stderr[-2000:]
    regenerated = np.load(workdir / "examples" / "data" / f"{key}.npz")
    assert set(committed.files) == set(regenerated.files)
    for name in committed.files:
        np.testing.assert_allclose(regenerated[name], committed[name], rtol=1e-9, atol=1e-12,
                                   err_msg=f"{key}.npz:{name}")
    assert (workdir / "examples" / "figures" / f"{key}_after.png").exists()
