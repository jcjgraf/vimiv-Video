# vim: ft=python fileencoding=utf-8 sw=4 et sts=4

from typing import Any, BinaryIO

from vimiv import api
from vimiv.qt.core import QProcess
from vimiv.qt.gui import QPixmap, QImageReader
from vimiv.utils import log

_logger = log.module_logger(__name__)


def test_mov(header: bytes, _f: BinaryIO) -> bool:
    return header[4:8] == b"ftyp" and header[8:10] == b"qt"


def test_mp4(header: bytes, _f: BinaryIO) -> bool:
    return header[4:8] == b"ftyp" and header[8:12].decode() in (
        "avc1",
        "iso2",
        "isom",
        "mmp4",
        "mp41",
        "mp42",
        "mp71",
        "msnv",
        "ndas",
        "ndsc",
        "ndsh",
        "ndsm",
        "ndsp",
        "ndss",
        "ndxc",
        "ndxh",
        "ndxm",
        "ndxp",
        "ndxs",
    )


def test_avi(header: bytes, _f: BinaryIO) -> bool:
    return header[0:4] == b"RIFF" and header[8:11] == b"AVI"


def load_frame(path) -> QPixmap:
    """Extract the first frame from the video and initialize QPixmap"""

    process = QProcess()
    process.start(
        "ffmpeg",
        ["-loglevel", "quiet", "-i", path, "-vframes", "1", "-f", "image2", "pipe:1"],
    )
    if not process.waitForFinished():
        _logger.error(f"Process exited with code {process.exitCode()}")
        raise OSError("Error waiting for process")

    if (
        process.exitStatus() != QProcess.ExitStatus.NormalExit
        or process.exitCode() != 0
    ):
        _logger.error(f"Process exited with code {process.exitCode()}")
        stderr = process.readAllStandardError()
        raise ValueError(f"Error calling ffmpeg: '{stderr.data().decode()}'")

    handler = QImageReader(process, "jpeg".encode())
    handler.setAutoTransform(True)

    process.closeWriteChannel()
    process.terminate()

    # Extract QImage from QImageReader and convert to QPixmap
    pixmap = QPixmap()
    pixmap.convertFromImage(handler.read())

    return pixmap


def init(info: str, *_args: Any, **_kwargs: Any) -> None:
    """Setup RawPrev plugin by adding the raw handler"""
    api.add_external_format("mov", test_mov, load_frame)
    api.add_external_format("mp4", test_mp4, load_frame)
    api.add_external_format("avi", test_avi, load_frame)

    _logger.debug("Initialized RawPrev")
