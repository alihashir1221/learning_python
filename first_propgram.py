print("21-08-2026")
print("o-----")
print(" |||||")
print("*" * 10)


class print:
	"""A simple line printer with optional prefix and output stream."""

	def __init__(self, prefix="", stream=None):
		import sys

		self.prefix = prefix
		self.stream = stream if stream is not None else sys.stdout

	def write(self, message=""):
		"""Write a message followed by a newline and return the text."""
		text = f"{self.prefix}{message}"
		self.stream.write(text + "\n")
		return text

	def flush(self):
		"""Flush the configured output stream."""
		self.stream.flush()