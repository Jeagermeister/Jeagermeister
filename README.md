## Hi, I'm Brian 📊⚙️✌️

I'm a **Data Engineer II**. I moved into software development from IT in 2022, and have
spent the years since building data pipelines and the orchestration around them.

Outside of that I build and maintain **Linux-native tooling**, mostly in the places where
good software got abandoned or never existed. Recovering desktop Linux from years on
Windows turned into a habit of fixing the gaps I hit along the way.

Currently working in **C/C++**, **C#/.NET** and **Rust** — but also have experience in working with Python, SQL, & Javascript.

<!-- Once the site is live, uncomment and fill in. This is the line that does the directing. -->
<!-- ### 🌐 &nbsp;[brian.example](https://brian.example) — projects, documentation, and what I'm working toward -->
<!-- The repos below are mirrors; the site is the fuller picture. -->

---

### What I'm building

**[Apocrypha](https://github.com/Jeagermeister/Apocrypha)** · C# / Avalonia
A Linux-first continuation of the archived NexusMods.App. Mod management that treats
Linux as the primary target rather than an afterthought — Proton-aware game detection,
native SMAPI support, and diagnostics for the engine limits that actually break modded
games. Ships as an AppImage.

**[Kirei](https://github.com/Jeagermeister/Kirei)** · Lua
An Aseprite extension that imports PNG/JPG/WebP images as clean, editable pixel sprites
— edge hardening and palette quantization, so imported art behaves like art you drew.

**[SIGIL](https://github.com/Jeagermeister/sigil)** · C
A minimal native client for AI chat providers — *Shell Interface for Generative Intelligence
Layers*. Links against the **system WebKitGTK** instead of bundling a browser engine, so the
binary is a few hundred kilobytes and starting it is a process spawn rather than a container
mount. Three providers out of the box.

**[Hermit](https://github.com/Jeagermeister/Hermes-Cpp)** · C/C++
A supervisor for local models doing real filesystem work. Small models (9–12B through Ollama)
can do the work but drift over a long session, so this keeps them on rails: every tool call
confined to one sandbox root, every write read back and hashed, anything overwritten backed up
somewhere the model cannot reach — and completion decided by inspecting the filesystem rather
than by the model saying it's done. Drives a model directly from the CLI, or runs as an MCP
server so a larger assistant can call it for hands. Inspired by NousResearch's Hermes Agent,
deliberately not a port.

Every guardrail traces to a measured failure rather than a hunch. The 259 recorded runs the
design is built on ship in the repo under [`bench/fsops/`](https://github.com/Jeagermeister/Hermes-Cpp/tree/main/bench/fsops)
— including the runs where models reported success on an untouched tree, and the ones that
overwrote real files with invented content. Sandbox, tools and verification are built and
tested; the model loop is next.

---

### How I work

Most day-to-day development happens on a **self-hosted Gitea** instance I run and
maintain — branches, pull requests, code review and CI all live there, with builds
running on my own hardware. What you see here is the published result.

That setup is its own small systems project: private networking, automated backups,
self-hosted CI runners, and a documented recovery path.

**On AI.** I use it, and I would rather say exactly how than leave it up to assumption.

The ideas, the design and the architecture are mine. I write the rough draft — including the
wrong version I have to think my way out of first. AI comes in after that, for four things:

- **Review** — a second pass over code I have already written
- **Revisions and touch-ups** — tightening what is there
- **Documentation** — describing the design, the code, and the individual components
- **Unit tests** — help covering the cases

Everything it produces, I read and understand before it lands. If I cannot explain a line, it
does not ship. I do not vibe-code.

---

### Interests

Linux game-modding tooling · game engines from first principles · data engineering and
pipelines · local-first and agentic AI on hardware I own · virtualization · developer
tools and CLIs

<!--
  Optional additions once they exist:
    - portfolio site link
    - a "currently reading / learning" line
    - GitHub stats cards (github-readme-stats) — note these will under-report while
      most work happens on Gitea
-->
