import unicodedata
import difflib

# List of real domains to compare
whitelist = ['google.com', 'facebook.com', 'apple.com', 'amazon.com', 'microsoft.com']

# Basic homoglyph map
homoglyphs = {
    'а': 'a', 'е': 'e', 'і': 'i', 'о': 'o', 'р': 'p',
    'ѕ': 's', 'ɡ': 'g', 'ӏ': 'l', 'һ': 'h', 'ʏ': 'y'
}

# Fixes Unicode & replaces suspicious characters
def clean(domain):
    norm = unicodedata.normalize('NFKC', domain)
    fixed = ''.join(homoglyphs.get(c, c) for c in norm)
    return norm, fixed

# Compares with known domains
def check(domain):
    norm, clean_domain = clean(domain)
    if any(ord(c) > 127 for c in norm):
        print(f"\n⚠️ Suspicious Unicode in: {domain}")
        print(f"🔹 Normalized: {norm}")
        print(f"🔹 Replaced:   {clean_domain}")
        for legit in whitelist:
            sim = difflib.SequenceMatcher(None, clean_domain, legit).ratio()
            if sim > 0.8:
                print(f"❗ Looks like: {legit} (Similarity: {round(sim, 2)})")
    else:
        print("✅ Domain looks clean.")

# Run
if __name__ == "__main__":
    domain = input("Enter domain to check: ")
    check(domain)
