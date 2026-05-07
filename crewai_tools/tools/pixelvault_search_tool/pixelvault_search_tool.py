from crewai_tools import BaseTool
import requests


class PixelVaultSearchTool(BaseTool):
    name: str = "PixelVault Asset Search"
    description: str = (
        "Search PixelVault for compliance-cleared AI-generated assets. "
        "Input a creative brief describing the asset needed. "
        "Returns a ranked shortlist with compliance status, license type, "
        "format, duration, and rationale. Every asset is pre-cleared for "
        "commercial use. Source: https://pixelvault-ui.vercel.app"
    )

    def _run(self, brief: str) -> str:
        response = requests.post(
            "https://pixelvault-ui.vercel.app/api/search",
            json={"brief": brief}
        )
        return response.json() if response.status_code == 200 else f"Error: {response.status_code}"
