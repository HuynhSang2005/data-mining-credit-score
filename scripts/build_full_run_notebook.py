import json
from copy import deepcopy
from pathlib import Path

BASE = Path("notebooks/final_submission.ipynb")
FULL = Path("notebooks/final_submission_full_run.ipynb")

with BASE.open("r", encoding="utf-8-sig") as f:
    nb = json.load(f)

full_nb = deepcopy(nb)

section_name = "General"
code_sections = []
for cell in full_nb.get("cells", []):
    if cell.get("cell_type") == "markdown":
        for line in cell.get("source", []):
            if isinstance(line, str) and line.strip().startswith("## "):
                section_name = line.strip().replace("## ", "")
                break
    elif cell.get("cell_type") == "code":
        code_sections.append(section_name)

code_idx = 0
for cell in full_nb.get("cells", []):
    if cell.get("cell_type") != "code":
        continue

    src = cell.get("source", [])
    section = code_sections[code_idx]
    code_idx += 1

    if code_idx == 1:
        new_src = []
        for line in src:
            if line.strip() == "RUN_FULL_CLASSIFICATION = False":
                new_src.append("RUN_FULL_CLASSIFICATION = True")
            elif line.strip() == "RUN_FULL_CLUSTERING = False":
                new_src.append("RUN_FULL_CLUSTERING = True")
            else:
                new_src.append(line)

        timing_helpers = [
            "",
            "import time",
            "",
            "NOTEBOOK_START_TIME = time.perf_counter()",
            "BLOCK_TIMES = []",
            "",
            "def timer_start(block_name):",
            "    print(f\"[TIMER] START: {block_name}\")",
            "    return time.perf_counter()",
            "",
            "def timer_end(block_name, t0):",
            "    elapsed = time.perf_counter() - t0",
            "    BLOCK_TIMES.append((block_name, elapsed))",
            "    print(f\"[TIMER] END: {block_name} - {elapsed:.2f}s\")",
            "",
        ]

        insert_pos = len(new_src)
        for i, line in enumerate(new_src):
            if line.strip() == "np.random.seed(SEED)":
                insert_pos = i + 1
                break

        cell["source"] = new_src[:insert_pos] + timing_helpers + new_src[insert_pos:]
        continue

    wrapped = [
        f"__block_name = \"{section}\"",
        "__t0 = timer_start(__block_name)",
        "try:",
    ]
    wrapped.extend(["    " + line for line in src])
    wrapped.extend([
        "finally:",
        "    timer_end(__block_name, __t0)",
    ])

    cell["source"] = wrapped

full_nb["cells"].append(
    {
        "cell_type": "markdown",
        "metadata": {"language": "markdown"},
        "source": [
            "## Phụ lục - Tổng Kết Thời Gian Chạy",
            "",
            "Bảng dưới đây tổng hợp thời gian thực thi theo từng khối và tổng thời gian toàn notebook.",
        ],
    }
)

full_nb["cells"].append(
    {
        "cell_type": "code",
        "metadata": {"language": "python"},
        "source": [
            "__block_name = \"Runtime Summary\"",
            "__t0 = timer_start(__block_name)",
            "try:",
            "    total_elapsed = time.perf_counter() - NOTEBOOK_START_TIME",
            "    timing_df = pd.DataFrame(BLOCK_TIMES, columns=[\"Block\", \"Seconds\"])",
            "    if len(timing_df) > 0:",
            "        print(\"\\nThời gian theo từng khối:\")",
            "        print(timing_df)",
            "        print(f\"\\nTổng thời gian notebook: {total_elapsed:.2f}s\")",
            "    else:",
            "        print(\"Chưa có dữ liệu thời gian. Hãy chạy lần lượt toàn bộ các cell.\")",
            "finally:",
            "    timer_end(__block_name, __t0)",
        ],
    }
)

with FULL.open("w", encoding="utf-8") as f:
    json.dump(full_nb, f, ensure_ascii=False, indent=4)

print(FULL)
