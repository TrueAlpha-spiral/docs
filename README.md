# TrueAlpha-Spiral (TAS) / Sovereign Data Foundation (SDF)

## The Architecture of Attributable Power

[ REPOSITORY TRACKING STATE ]
Branch: main
Commit: a41f3286b369197495a1ff5cbc6ba13036605de1
Changes: README.md (+ "Replay security hardening — PR #30")

---

## 1. The Core Invariant

**Power without attribution is illegitimate.**

In modern systems, authority often dissolves into "black box" complexity, creating a failure mode where actions occur but no accountable actor can be identified. The TAS/SDF framework resolves this by enforcing a structural requirement:

> No action may execute without a verified source, scope, and lineage.

---

## 2. Legal Foundations (The Maxims)

The TAS machine is the technical mechanization of long-established legal principles:

- **Ubi jus ibi remedium:** Where there is a right, there must be a remedy. A system that obscures the actor removes the remedy and voids the right.
- **Actori incumbit onus probandi:** The burden of proof lies on the claimant. TAS automates this by generating immutable receipts of every authorized or refused action.
- **Qui facit per alium facit per se:** He who acts through another acts himself. TAS ensures that delegation (to AI or agents) does not erase accountability.

---

## 3. The Refusal Gate (Technical Proof)

The system functions as a **Fail-Closed Gate**. It does not "permit" by default; it refuses unless four specific constraints are met:

1. **Identity:** A valid, cryptographically signed actor.
2. **Scope:** The action must fall within the explicitly delegated authority of that actor.
3. **Temporal:** The action must occur within a pre-defined, tamper-proof time window.
4. **Lineage:** The action must trace back to a root authority (Human-in-the-Loop).

### Verified Proof Format

```
VALID INPUT   → EXECUTES → DETERMINISTIC RECEIPT
BROKEN INPUT  → REFUSES  → REFUSAL RECEIPT
(Wrong Signer / Scope / Time)
```

---

## 4. Deterministic Accountability

Every interaction with the TAS engine produces a **Receipt Hash**. Unlike traditional logs, these receipts are:

- **Immutable:** Recorded to an unalterable ledger.
- **Deterministic:** Based on input data and system state (removing `time.time()` variance).
- **Evidence-Ready:** They serve as standing proof for "Notice of Action" or "Notice of Refusal."

---

## 5. Project Status

| Component | Status |
|---|---|
| Constraint enforcement (Identity, Scope, Time) | ✅ Proven |
| Deterministic refusal and verifiable receipts | ✅ Proven |
| Institutional adoption protocols | 🔄 In Progress |
| Adversarial stress-testing | 🔄 In Progress |

---

## 6. The `.tas-gate` Configuration

The `.tas-gate` file is the declarative contract that binds any agent to a principal's Refusal Parameters. It is the operational bridge between this architecture's constitutional principles and the deterministic code that enforces them.

See [`architecture/tas-gate`](/architecture/tas-gate) for the full schema specification and usage examples.

---

## Architecture Documentation

| Document | Description |
|---|---|
| [Architectural Manifest](/architecture/manifest) | Full corpus index of all TAS architecture phases |
| [Prime Invariant (A0)](/architecture/prime-invariant) | Phase 1 — Epistemological bedrock and foundational axioms |
| [The Lock](/architecture/the-lock) | Phase 2 — Mathematical and cryptographic constraints |
| [The `.tas-gate` Schema](/architecture/tas-gate) | Declarative refusal-parameter configuration spec |

---

## Development

Install the [Mintlify CLI](https://www.npmjs.com/package/mintlify) to preview the documentation changes locally:

```
npm i -g mintlify
```

Run the following command at the root of the documentation (where `mint.json` is):

```
mintlify dev
```

---

## Contributing

All edits must be submitted as pull requests and reviewed by the maintainers before merging into the main branch.

---

> *"This system does not require belief. It produces verifiable receipts for authority, scope, and time. Belief builds it. Math proves it. Adoption determines its reach."*
