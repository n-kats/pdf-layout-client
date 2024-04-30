from pathlib import Path
import requests

from pydantic import BaseModel, RootModel


class PDFLayout(BaseModel):
    page: int
    xmin: float
    ymin: float
    xmax: float
    ymax: float
    type: str


class PDFLayoutClient:
    def __init__(self, url: str):
        self.__url = url

    def get_pdf_layout(self, pdf_path: Path) -> list[PDFLayout]:
        with open(pdf_path, "rb") as f_in:
            response = requests.post(
                f"{self.__url}/pdf-layout",
                files={"file": (pdf_path.name, f_in, "application/pdf")},
            )
        return RootModel[list[PDFLayout]].model_validate(response.json()).root

    def annotation_request(self, pdf_path: Path) -> None:
        with open(pdf_path, "rb") as f_in:
            requests.post(
                f"{self.__url}/annotation_request",
                files={"file": (pdf_path.name, f_in, "application/pdf")},
            )
