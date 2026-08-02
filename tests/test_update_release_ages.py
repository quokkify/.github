import unittest
from datetime import datetime, timezone

from scripts.update_release_ages import update_release_ages


NOW = datetime(2026, 8, 2, 18, 0, tzinfo=timezone.utc)


class UpdateReleaseAgesTests(unittest.TestCase):
    def test_replaces_release_date_badge_with_exact_day_count(self):
        markdown = (
            "| [example](https://github.com/quokkify/example) | "
            "[![Release](https://img.shields.io/github/v/release/quokkify/example)]"
            "(https://github.com/quokkify/example/releases) | "
            "[![Release age](https://img.shields.io/github/release-date/quokkify/example"
            "?label=release%20age)](https://github.com/quokkify/example/releases) | Description |\n"
        )
        published_at = {"example": datetime(2026, 7, 30, 17, 0, tzinfo=timezone.utc)}

        updated = update_release_ages(markdown, published_at, now=NOW)

        self.assertIn(
            "https://img.shields.io/badge/release%20age-3%20days-blue", updated
        )
        self.assertNotIn("github/release-date", updated)

    def test_uses_singular_for_one_full_day(self):
        markdown = (
            "| repo | https://img.shields.io/github/v/release/quokkify/example | "
            "https://img.shields.io/date/1600000000?label=release%20age | description |\n"
        )
        published_at = {"example": datetime(2026, 8, 1, 17, 0, tzinfo=timezone.utc)}

        updated = update_release_ages(markdown, published_at, now=NOW)

        self.assertIn("release%20age-1%20day-blue", updated)

    def test_updates_existing_count_idempotently(self):
        markdown = (
            "| repo | https://img.shields.io/github/v/release/quokkify/example | "
            "https://img.shields.io/badge/release%20age-9%20days-blue | description |\n"
        )
        published_at = {"example": datetime(2026, 8, 2, 17, 30, tzinfo=timezone.utc)}

        updated = update_release_ages(markdown, published_at, now=NOW)
        repeated = update_release_ages(updated, published_at, now=NOW)

        self.assertIn("release%20age-0%20days-blue", updated)
        self.assertEqual(updated, repeated)

    def test_fails_closed_when_age_badge_is_missing(self):
        markdown = (
            "| repo | https://img.shields.io/github/v/release/quokkify/example | description |\n"
        )
        published_at = {"example": datetime(2026, 8, 1, tzinfo=timezone.utc)}

        with self.assertRaisesRegex(ValueError, "exactly one release-age badge"):
            update_release_ages(markdown, published_at, now=NOW)


if __name__ == "__main__":
    unittest.main()
