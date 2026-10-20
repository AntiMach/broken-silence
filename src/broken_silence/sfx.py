import ffmpeg


from typing import Any, NamedTuple


class SFX(NamedTuple):
    file: str
    dur: float
    stream: Any

    @classmethod
    def from_path(cls, file: str):
        sfx_probe = ffmpeg.probe(file)
        return cls(
            file=file,
            dur=float(sfx_probe["streams"][0]["duration"]),
            stream=ffmpeg.input(file),
        )
