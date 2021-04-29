# vim: ft=python fileencoding=utf-8 sw=4 et sts=4

from typing import Any, BinaryIO

from PyQt5.QtGui import QPixmap, QImageReader
from PyQt5.QtCore import QProcess

from vimiv import api
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


def load_frame(path) -> QPixmap:
    """Extract the first frame from the video and initialize QPixmap"""

    process = QProcess()
    process.start(f"ffmpeg -loglevel quiet -i {path} -vframes 1 -f singlejpeg pipe:1")
    process.waitForFinished()

    if process.exitStatus() != QProcess.NormalExit or process.exitCode() != 0:
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

    _logger.debug("Initialized RawPrev")
