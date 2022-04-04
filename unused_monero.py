from typing import Any, Dict, Set, List
import json
import subprocess

MAPPING_FILE = "monero_func_mapping.json"


def load_all_function_aliases() -> None:

    file = "core/mocks/generated/trezorcrypto/monero.pyi"

    functions: Set[str] = set()
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("def"):
                f_name = line.split("(")[0].split(" ")[1]
                functions.add(f_name)

    for f_name in functions:
        print(f_name)

    print(len(functions))

    alias_file = "core/src/apps/monero/xmr/crypto/__init__.py"

    function_aliases: Dict[str, List[str]] = {}

    with open(alias_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            for func_name in functions:
                if f"tcry.{func_name}" in line:
                    alias = line.split("=")[0].strip()
                    if func_name not in function_aliases:
                        function_aliases[func_name] = []
                    function_aliases[func_name].append(alias)

    print(function_aliases)

    # It was needed to modify something manually
    # with open(MAPPING_FILE, "w") as f:
    #     f.write(json.dumps(function_aliases, indent=4))


def check_definitions() -> None:
    with open(MAPPING_FILE, "r") as f:
        mapping = json.loads(f.read())

    is_used_mappings: Dict[str, Dict[str, Any]] = {}
    for func_name, aliases in mapping.items():
        is_used_mappings[func_name] = {
            "aliases": aliases,
            "is_used": False
        }

    for func_name in is_used_mappings:
        aliases = is_used_mappings[func_name]["aliases"]
        for alias in aliases:
            is_there = is_used(alias)
            if is_there:
                is_used_mappings[func_name]["is_used"] = True
                break

    # for mapp in is_used_mappings:
    #     print(f"{mapp}: {is_used_mappings[mapp]['is_used']}")

    unused_functions = {fc: val for fc, val in is_used_mappings.items() if not val["is_used"]}
    print("Unused functions:")
    for func, values in unused_functions.items():
        print(func, values)
        # print(f"{func}: {values['aliases']}")


def is_used(func_name: str) -> bool:
    cmd = f'grep -r "crypto.{func_name}" core/src/apps/monero'
    grep_result = subprocess.run(
        cmd, stdout=subprocess.PIPE, text=True, shell=True
    )
    # print(grep_result.stdout)

    return grep_result.returncode == 0


if "__main__" == __name__:
    # load_all_function_aliases()
    check_definitions()
