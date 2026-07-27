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
		cls.templates[name] = template_func

	@classmethod
	def get_template(cls, name):
		return cls.templates.get(name)

	def __call__(self, template_name):
		template = self.get_template(template_name)
		if template is None:
			raise ValueError(f"Template '{template_name}' not found")
		return template(self)

	def __str__(self):
		return f"Report(title={self.title}, content={self.content})"
