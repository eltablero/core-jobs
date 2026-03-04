import sys

from src.jobs.media_scraping import run_media_scraping


def main() -> None:
    job_name = sys.argv[1] if len(sys.argv) > 1 else "default"

    if job_name == "media-scraping":
        run_media_scraping()
    else:
        print(f"Job {job_name} no reconocido")


if __name__ == "__main__":
    main()
