import os
import yaml
import frontmatter
from pathlib import Path

content_dir = Path("content")
nlu_file = Path("data/nlu.yml")
stories_file = Path("data/stories.yml")
domain_file = Path("domain.yml")
log_file = Path("rasa_markdown_log.txt")

def generate_intent(slug):
    return "intent_" + slug.strip("/").replace("/", "_").replace("-", "_")

# Load existing files safely
def load_yaml_file(path):
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    return {}

# Load current data
nlu_data = load_yaml_file(nlu_file).get("nlu", [])
stories_data = load_yaml_file(stories_file).get("stories", [])
domain_data = load_yaml_file(domain_file)
domain_data.setdefault("version", "3.1")
domain_data.setdefault("responses", {})

# Track existing
existing_intents = {entry["intent"] for entry in nlu_data}
log_entries = []

# Process Markdown
for md_file in content_dir.rglob("*.md"):
    post = frontmatter.load(md_file)

    title = post.get("title")
    slug = post.get("url")
    body = post.content.strip().split("\n\n")[0]

    if not (title and slug and body):
        continue

    intent = generate_intent(slug)
    action = f"utter_{intent}"

    if intent in existing_intents:
        continue  # Skip duplicates

    # Add NLU
    nlu_data.append({
        "intent": intent,
        "examples": f"- {title.strip()}\n- {title.strip().lower()}"
    })

    # Add story
    stories_data.append({
        "story": f"story_{intent}",
        "steps": [
            {"intent": intent},
            {"action": action}
        ]
    })

    # Add domain response
    domain_data["responses"][action] = [{"text": body.strip()}]

    # Log it
    log_entries.append(f"✔️ Added intent: {intent} from '{title}'")

# Write outputs
nlu_out = {"version": "3.1", "nlu": nlu_data}
with open(nlu_file, "w", encoding="utf-8") as f:
    yaml.dump(nlu_out, f, allow_unicode=True)

stories_out = {"version": "3.1", "stories": stories_data}
with open(stories_file, "w", encoding="utf-8") as f:
    yaml.dump(stories_out, f, allow_unicode=True)

with open(domain_file, "w", encoding="utf-8") as f:
    yaml.dump(domain_data, f, allow_unicode=True)

with open(log_file, "w", encoding="utf-8") as f:
    f.write("\n".join(log_entries))

print("✅ Mafaili yameboreshwa. Angalia `rasa_markdown_log.txt` kwa orodha ya intents mpya.")
