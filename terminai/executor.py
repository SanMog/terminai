import subprocess
import sys
from typing import Tuple, Optional


class CommandExecutor:
    """Executes shell commands with real-time output streaming"""

    def __init__(self):
        self.last_stdout = []
        self.last_stderr = []
        self.last_exit_code = 0

    def execute(self, command: str) -> Tuple[int, str, str]:
        """
        Execute command with real-time streaming
        Returns: (exit_code, stdout, stderr)
        """
        print(f"🔵 Executing: {command}\n")

        # Reset storage
        self.last_stdout = []
        self.last_stderr = []

        try:
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1
            )

            # Stream stdout in real-time
            for line in process.stdout:
                print(line, end='')
                sys.stdout.flush()
                self.last_stdout.append(line)

            # Wait for completion and get stderr
            _, stderr = process.communicate()
            self.last_stderr = stderr.splitlines()
            self.last_exit_code = process.returncode

            # Print stderr if exists
            if stderr:
                print(stderr, file=sys.stderr)
                sys.stderr.flush()

            stdout_text = ''.join(self.last_stdout)

            return self.last_exit_code, stdout_text, stderr

        except Exception as e:
            error_msg = f"Failed to execute command: {str(e)}"
            print(f"❌ {error_msg}", file=sys.stderr)
            return 1, "", error_msg

    def get_context(self, max_lines: int = 20) -> dict:
        """Get execution context for AI analysis"""
        return {
            "exit_code": self.last_exit_code,
            "stdout_tail": '\n'.join(self.last_stdout[-max_lines:]),
            "stderr": '\n'.join(self.last_stderr),
        }