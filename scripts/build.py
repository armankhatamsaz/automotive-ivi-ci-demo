import argparse
import subprocess
import sys


def run_step(command, step_name):
    print(f"\n=== [STEP] {step_name} ===")
    print(f"Running: {' '.join(command)}")
    try:
        subprocess.run(command, check=True, text=True)
        print(f"[SUCCESS] {step_name} passed.")
    except FileNotFoundError:
        print(f"[ENV ERROR] Tool not found: {command[0]}")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"[FAILED] {step_name} failed with exit code {e.returncode}")
        sys.exit(e.returncode)


def main():
    parser = argparse.ArgumentParser(description="Automotive IVI CI Build & Test Script")
    parser.add_argument("--cc", default="gcc", help="C compiler (gcc or clang)")
    parser.add_argument("--cxx", default="g++", help="C++ compiler (g++ or clang++)")
    parser.add_argument("--build-dir", default="build", help="CMake build directory")
    args = parser.parse_args()

    # ۱. آماده‌سازی CMake و خروجی گرفتن از compile_commands.json
    run_step(
        [
            "cmake",
            "-B",
            args.build_dir,
            "-S",
            ".",
            f"-DCMAKE_C_COMPILER={args.cc}",
            f"-DCMAKE_CXX_COMPILER={args.cxx}",
            "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        ],
        "CMake Configure",
    )

    # ۲. کامپایل کتابخانه و تست‌ها
    run_step(
        ["cmake", "--build", args.build_dir],
        "CMake Build",
    )

    # ۳. اجرای تست‌های واحد با CTest
    run_step(
        ["ctest", "--test-dir", args.build_dir, "--output-on-failure"],
        "CTest Execution",
    )


if __name__ == "__main__":
    main()