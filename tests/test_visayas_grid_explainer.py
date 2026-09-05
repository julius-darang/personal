import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "how-i-built-the-visayas-grid.html"


class VisayasGridExplainerTests(unittest.TestCase):
    def test_article_is_complete_and_registered(self):
        article = ROOT / "blogs" / SLUG
        self.assertTrue(article.exists(), "The explainer article must exist")

        content = article.read_text(encoding="utf-8")
        for expected in (
            "How I Built an Interactive Model of the Visayas Power Grid",
            "https://visayasgrid.vercel.app",
            "https://github.com/julius-darang/visayasgrid",
            "54 buses",
            "60 lines",
            "115 generator units",
            "What the model cannot tell you",
            "What comes next",
        ):
            self.assertIn(expected, content)

        registrations = {
            "build.py": f'"blogs/{SLUG}"',
            "sync.py": f'"blogs/{SLUG}"',
            "pages/writings.html": f'../blogs/{SLUG}',
            "sitemap.xml": f'https://juliusdarang.com/blogs/{SLUG}',
            "feed.xml": f'https://juliusdarang.com/blogs/{SLUG}',
            "proj/visayasgrid.html": f'../blogs/{SLUG}',
            "blogs/modelling-the-philippine-grid.html": SLUG,
        }
        for relative_path, expected in registrations.items():
            content = (ROOT / relative_path).read_text(encoding="utf-8")
            self.assertIn(expected, content, f"Missing registration in {relative_path}")


if __name__ == "__main__":
    unittest.main()
