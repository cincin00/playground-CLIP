"""CLIP adapter."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ClipModelConfig:
    model_name: str
    pretrained: str
    device: str = "cpu"


class OpenClipAdapter:
    def __init__(self, config: ClipModelConfig) -> None:
        self._config = config

    @property
    def config(self) -> ClipModelConfig:
        return self._config

    def embed_image_bytes(self, image_bytes: bytes) -> list[float]:
        if not image_bytes:
            msg = "image_bytes must not be empty"
            raise ValueError(msg)
        msg = "OpenCLIP runtime is not wired yet"
        raise NotImplementedError(msg)
