import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	description="Python Tool for accessing online data from KOBO TOOLBOX.",
	name="kobodata",
	version="0.0.9",
	author = "Brightius Kalokola",
	author_email = "brightiuskalokola@gmail.com",
	long_description = long_description,
	long_description_content_type="text/markdown",
	url = "",
	packages=setuptools.find_packages(),
	summary = None,
	home_page = None,
	install_requires=["requests"],
	license="MIT",
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)