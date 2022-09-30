import subprocess
import typing
from pathlib import Path
from ._constants import STUBS


RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
END = '\033[0m'

MARKER = 'py.typed'
TEMPLATE = '{name:30} {status}'
ROOT = Path(__file__).parent


class Module(typing.NamedTuple):
    path: Path
    exe: str
    dry: bool

    @property
    def patched(self) -> bool:
        return (self.path / MARKER).exists()

    @property
    def stubbed(self) -> bool:
        if self.path.name.endswith('-stubs'):
            return True
        new_name = self.path.name + '-stubs'
        return (self.path.parent / new_name).exists()

    @property
    def annotated(self) -> bool:
        script_path = ROOT / '_script_inspect.py'
        script = script_path.read_text()
        script = script.replace('MODULE_NAME', self.path.name)
        result = subprocess.run([self.exe, '-c', script])
        assert result.returncode in (21, 22)
        return result.returncode == 21

    def process(self) -> str:
        if self.patched:
            return GREEN + 'already annotated' + END
        if self.stubbed:
            return GREEN + 'already has stubs' + END

        stub = STUBS.get(self.path.name.lower())
        if stub:
            if not self.dry:
                cmd = [self.exe, '-m', 'pip', 'install', stub]
                result = subprocess.run(cmd, stdout=subprocess.DEVNULL)
                if result.returncode != 0:
                    return RED + 'cannot install stubs' + END
            return YELLOW + 'stubs installed' + END

        if self.annotated:
            if not self.dry:
                (self.path / MARKER).write_bytes(b'')
            return YELLOW + 'patched' + END
        return RED + 'has no annotations' + END


class Explorer(typing.NamedTuple):
    exe: str
    dry: bool

    @property
    def root(self) -> Path:
        script_path = ROOT / '_script_sites.py'
        cmd = [self.exe, str(script_path)]
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE)
        sites = result.stdout.decode().strip().splitlines()
        print(sites)
        for site in sites:
            path = Path(site)
            if path.exists():
                print(path)
                return path
        raise LookupError('cannot find site packages directory')

    @property
    def modules(self) -> typing.Iterable[Module]:
        for mpath in sorted(self.root.iterdir()):
            if '.' in mpath.name:
                continue
            if not mpath.is_dir():
                continue
            yield Module(path=mpath, exe=self.exe, dry=self.dry)

    def run(self) -> typing.Iterable[str]:
        for module in self.modules:
            status = module.process()
            yield TEMPLATE.format(
                name=BLUE + module.path.name + END,
                status=status,
            )
