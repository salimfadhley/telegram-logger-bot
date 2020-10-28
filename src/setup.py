import setuptools

with open("README.md", "r") as fh:
      long_description = fh.read()

try:
      REQUIREMENTS = list(open("requirements.txt").read().splitlines())
except IOError:
      REQUIREMENTS = []

setuptools.setup(
      name="example-pkg-YOUR-USERNAME-HERE", # Replace with your own username
      version="0.0.1",
      author="Example Author",
      author_email="author@example.com",
      description="A small example package",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/pypa/sampleproject",
      packages=["bot", "test_bot"],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      python_requires='>=3.9',
      install_requires=REQUIREMENTS,
)
