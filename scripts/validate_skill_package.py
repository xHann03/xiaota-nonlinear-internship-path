#!/usr/bin/env python3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "VERSION",
    "CHANGELOG.md",
    "agents/openai.yaml",
    "references/voice-and-conversation.md",
    "references/onboarding-and-dialogue.md",
    "references/diagnosis-framework.md",
    "references/output-patterns.md",
    "references/creator-evidence.md",
    "references/source-notes.md",
    "references/human-handoff.md",
    "references/internal-review.md",
    "eval/real-user-queries.md",
    "eval/conversation-scenarios.md",
    "eval/expected-properties.md",
]

SKILL_MARKERS = [
    "每轮只问一个",
    "creator-evidence.md",
    "不要因为用户想要主线就强行包装",
    "这部分更适合继续问蛋挞本人",
]

SOURCE_IDS = [
    "6ab50491000000001500fb8b",
    "69d631ad000000001d01f897",
    "6a106711000000003502e678",
    "6a658586000000001101d1e7",
    "69c68e6e0000000023020a6e",
    "69ef65190000000035021390",
    "69d8e7b3000000001b001c15",
    "69d79fd0000000001d01d0e0",
    "69fdd631000000003503ac9b",
    "69e899f00000000023021371",
    "6a89f3a4000000003300edc8",
    "69cfd2670000000023022523",
    "69cd000500000000230139a8",
]


def main() -> None:
    errors = []

    for relative_path in REQUIRED_FILES:
        path = ROOT / relative_path
        if not path.is_file():
            errors.append(f"missing required file: {relative_path}")

    skill_path = ROOT / "SKILL.md"
    if skill_path.is_file():
        skill_text = skill_path.read_text(encoding="utf-8")
        for marker in SKILL_MARKERS:
            if marker not in skill_text:
                errors.append(f"SKILL.md missing marker: {marker}")

    evidence_path = ROOT / "references/creator-evidence.md"
    if evidence_path.is_file():
        evidence_text = evidence_path.read_text(encoding="utf-8")
        for source_id in SOURCE_IDS:
            if source_id not in evidence_text:
                errors.append(f"creator-evidence.md missing source id: {source_id}")

    if errors:
        raise SystemExit("\n".join(errors))

    print(f"OK: validated {len(REQUIRED_FILES)} required files and evidence markers")


if __name__ == "__main__":
    main()
