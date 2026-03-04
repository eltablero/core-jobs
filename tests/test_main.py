import sys

import pytest

import src.main as main_mod


def test_runs_media_scraping(monkeypatch: pytest.MonkeyPatch) -> None:
    called = {"ok": False}

    def fake_run() -> None:
        called["ok"] = True

    monkeypatch.setattr(main_mod, "run_media_scraping", fake_run)
    monkeypatch.setattr(sys, "argv", ["main.py", "media-scraping"])

    main_mod.main()

    assert called["ok"] is True


def test_unrecognized_job_prints_message(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(sys, "argv", ["main.py"])  # no args -> default

    # Ensure any real job won't run if accidentally called
    def fail_if_called() -> None:
        raise AssertionError("run_media_scraping should not be called for default")

    monkeypatch.setattr(main_mod, "run_media_scraping", fail_if_called)

    main_mod.main()

    captured = capsys.readouterr()
    assert "Job default no reconocido" in captured.out
