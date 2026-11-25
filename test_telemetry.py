from telemetry import depth_status

tests = [
    (None, "NO DATA"),
    (1.9, "LIVE"),
    (2.0, "STALE"),
    (3.0, "STALE")
]

failed = 0

for age, expected in tests:
    actual = depth_status(age)

    if actual == expected:
        print(f"PASS: {age} -> {actual}")
    else:
        print(f"FAIL: {age} -> Expected {expected}, got {actual}")
        failed += 1

print(f"\nFailed tests: {failed}")
