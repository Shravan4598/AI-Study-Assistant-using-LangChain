"""
Custom exception module for the AI Study Assistant.

This module defines a custom exception class that provides
detailed error information, including the filename and
line number where the exception occurred.
"""

import sys
from typing import Any


class AIStudyAssistantException(Exception):
    """
    Custom exception for the AI Study Assistant.

    This exception captures the original exception along with
    the file name and line number for easier debugging.
    """

    def __init__(self, error_message: Any, error_detail: sys) -> None:
        """
        Initialize the custom exception.

        Parameters
        ----------
        error_message : Any
            Original exception message.

        error_detail : sys
            sys module used to extract traceback information.
        """
        super().__init__(str(error_message))
        self.error_message = self._get_detailed_error(
            error_message,
            error_detail,
        )

    @staticmethod
    def _get_detailed_error(
        error_message: Any,
        error_detail: sys,
    ) -> str:
        """
        Generate a detailed error message.

        Parameters
        ----------
        error_message : Any
            Original exception.

        error_detail : sys
            Python sys module.

        Returns
        -------
        str
            Formatted exception message.
        """
        _, _, exc_tb = error_detail.exc_info()

        if exc_tb is None:
            return str(error_message)

        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

        return (
            "\n"
            "================ Exception Occurred ================\n"
            f"File      : {file_name}\n"
            f"Line      : {line_number}\n"
            f"Error     : {error_message}\n"
            "===================================================="
        )

    def __str__(self) -> str:
        """
        Return the formatted error message.
        """
        return self.error_message