

from io import StringIO
from pathlib import Path
import subprocess
import sys
from typeforce._cli import main


def test_smoke(tmp_path: Path):
    # create venv
    venv_path = tmp_path / '.venv'
    cmd = [sys.executable, '-m', 'venv', str(venv_path)]
    subprocess.run(cmd, check=True)

    # install deps
    exe_path = venv_path / 'bin' / 'python'
    cmd = [str(exe_path), '-m', 'pip', 'install', 'astroid']
    subprocess.run(cmd, check=True)

    # run typeforce
    stdout = StringIO()
    code = main(['--exe', str(exe_path)], stdout)
    assert code == 0

    stdout.seek(0)
    output = stdout.read()
    assert 'astroid' in output
    assert 'patched' in output
