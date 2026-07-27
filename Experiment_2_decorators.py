def bold_text(func):
	def wrapper(*args, **kwargs):
		return f"<b>{func(*args, **kwargs)}</b>"

	return wrapper


class Report:
	templates = {}

	def __init__(self, title, content):
		self.title = title
		self.content = content

	@classmethod
	def add_template(cls, name, template_func):
		pass

	@classmethod
	def get_template(cls, name):
		pass

	def __call__(self, template_name):
		pass

	def __str__(self):
		return f"Report(title={self.title}, content={self.content})"
