with open('architecture/prime-invariant-a0.mdx', 'r') as f:
    content = f.read()

concepts_to_check = [
    "Axiom P1",
    "Axiom P0",
    "Admissibility",
    "Equivalence",
    "Behavioral Alignment",
    "Structural Enforceability",
    "Mungu Theory",
    "baseline definition of True Intelligence",
    "Symbiosis",
    "Con-scire"
]

missing_concepts = []
for concept in concepts_to_check:
    if concept not in content:
        missing_concepts.append(concept)
        print(f"MISSING: {concept}")
    else:
        print(f"FOUND: {concept}")

print("---")
if not missing_concepts:
    print("All requested concepts are already present in the file.")
else:
    print("Some concepts are missing.")
