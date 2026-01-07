import typer
import sys
from dotenv import load_dotenv
from .executor import CommandExecutor
from .ai_helper import AIHelper

# Загрузка переменных окружения
load_dotenv()


def confirm_action(message: str) -> bool:
    try:
        response = input(f"{message} [Y/n]: ").strip().lower()
        return response in ['', 'y', 'yes']
    except EOFError:
        return False


def main_logic(
        command: str = typer.Argument(..., help="The shell command to execute"),
        auto_fix: bool = typer.Option(False, "--auto", "-a", help="Automatically apply fix"),
        max_retries: int = typer.Option(1, "--retries", "-r", help="Max retries")
):
    """
    TerminAI: Run a command and fix it with AI if it fails.
    """
    executor = CommandExecutor()

    try:
        ai = AIHelper()
    except ValueError as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        print("💡 Ensure OPENAI_API_KEY is set (start with gsk_... for Groq)")
        sys.exit(1)

    attempt = 0
    current_command = command

    while attempt <= max_retries:
        if attempt > 0:
            print(f"\n🔄 Retry attempt {attempt}/{max_retries}")

        # 1. Выполняем команду
        exit_code, stdout, stderr = executor.execute(current_command)

        # Если успех — выходим
        if exit_code == 0:
            print(f"\n✅ Command succeeded!")
            sys.exit(0)

        # 2. Если ошибка — зовем AI
        print(f"\n❌ Command failed (code {exit_code})")
        print("🤖 Analyzing error with AI...\n")

        context = executor.get_context()
        analysis = ai.analyze_error(
            current_command,
            context["exit_code"],
            context["stdout_tail"],
            context["stderr"]
        )

        # 3. Показываем решение
        print("─" * 60)
        print(f"🔴 Problem: {analysis.get('explanation', 'Unknown error')}")

        fix_cmd = analysis.get('fix_command')
        if not fix_cmd:
            print("🟡 No fix available.")
            sys.exit(exit_code)

        print(f"🟢 Suggested Fix:\n   {fix_cmd}")
        print("─" * 60)

        # 4. Спрашиваем разрешение
        should_apply = auto_fix or confirm_action("\nApply this fix?")

        if not should_apply:
            print("❌ Fix declined.")
            sys.exit(exit_code)

        # 5. Применяем фикс
        current_command = fix_cmd
        attempt += 1

    print(f"\n⚠️  Max retries reached.")
    sys.exit(1)


# Функция-точка входа для setup.py
def entry_point():
    typer.run(main_logic)


if __name__ == "__main__":
    entry_point()