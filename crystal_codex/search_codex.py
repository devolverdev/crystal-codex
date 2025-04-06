from crystal_codex.file_writer import load_codex

def search_by_attribute(codex, keyword, field=None):
    results = {}

    for name, info in codex.items():
        target_fields = info.values() if not field else [info.get(field, "")]
        if field == "name":
            target_fields = [name]

        if any(keyword in str(value).lower() for value in target_fields):
            results[name] = info

    return results

def list_all(codex):
    print("\n📜 All crystals in your codex:")
    for name in codex:
        print("💠", name.title())

def pretty_print(name, info):
    print(f"\033[1;35m\n🔮 {name.title()}\033[0m")
    for key, val in info.items():
        print(f"   \033[1;36m{key.title()}\033[0m: {val}")

if __name__ == "__main__":
    codex = load_codex()

    print("🔍 Welcome to the Codex Searcher 🔮")

    if input("🪄 List all crystals first? (y/n): ").lower() == "y":
        list_all(codex)

    field = input("Limit search to (name/chakra/color/effect/element or leave blank for all): ").lower().strip()
    if field == "": field = None

    keyword = input("🔍 Search for keyword: ").lower()

    results = search_by_attribute(codex, keyword, field)

    if results:
        print(f"\n✨ Found {len(results)} match(es):")
        for name, data in results.items():
            pretty_print(name, data)
    else:
        print("🫥 No matching crystals found.")
