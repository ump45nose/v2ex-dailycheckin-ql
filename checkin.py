"""Run only the V2EX task from Sitoi/dailycheckin with a Qinglong environment variable."""
import json
import os
import sys
import tempfile

from dailycheckin.main import checkin


def main():
    raw = os.getenv("V2EX")
    if not raw and os.getenv("V2EX_COOKIE"):
        raw = json.dumps([{"cookie": os.environ["V2EX_COOKIE"]}])
    if not raw:
        raise SystemExit("Set V2EX or V2EX_COOKIE in the Qinglong environment")
    accounts = json.loads(raw)
    if not isinstance(accounts, list) or not accounts:
        raise SystemExit("V2EX must be a non-empty account list")
    with tempfile.TemporaryDirectory(prefix="v2ex-checkin-") as directory:
        os.chdir(directory)
        with open("config.json", "w", encoding="utf-8") as output:
            json.dump({"V2EX": accounts}, output)
        os.chmod("config.json", 0o600)
        sys.argv = [sys.argv[0], "--include", "V2EX"]
        checkin()


if __name__ == "__main__":
    main()
