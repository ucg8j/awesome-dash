# Simple link validator for the README.md file

import asyncio
import re

import httpx


async def validate_link(client: httpx.AsyncClient, url: str) -> tuple[str, bool]:
    url = url.rstrip(")")
    try:
        response = await client.head(url, follow_redirects=True, timeout=5.0)
        is_valid = 200 <= response.status_code < 400
        print(f"URL: {url}, Status Code: {response.status_code}")
        return url, is_valid
    except Exception as e:
        print(f"URL: {url}, Exception: {e}")
        return url, False


def extract_markdown_links(content: str) -> list[str]:
    # Match markdown links [text](url) and direct URLs
    markdown_pattern = r"\[(?:[^\]]*)\]\((https?://[^\s\)]+)\)"
    direct_url_pattern = r"(?<!\])\b(https?://[^\s\)]+)"

    # Find all markdown format links
    markdown_links = re.findall(markdown_pattern, content)
    # Find all direct URLs (not part of markdown syntax)
    direct_urls = re.findall(direct_url_pattern, content)

    return markdown_links + direct_urls


async def check_readme_links(readme_path: str, only_invalid: bool = False) -> None:
    with open(readme_path, "r") as file:
        content = file.read()

    links = extract_markdown_links(content)

    async with httpx.AsyncClient() as client:
        tasks = [validate_link(client, link) for link in links]
        results = await asyncio.gather(*tasks)

        print("Results:")
        for url, is_valid in results:
            if not only_invalid or not is_valid:
                print(f"{url}: {'Valid' if is_valid else 'Invalid'}")


asyncio.run(check_readme_links("README.md", only_invalid=True))
