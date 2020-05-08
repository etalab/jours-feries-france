from setuptools import setup

setup(
    name="jours_feries_france",
    license="MIT",
    packages=["jours_feries_france"],
    version="0.6.0",
    description="Jours fériés en France, en métropole et en outre-mer.",
    author="Etalab",
    author_email="info@data.gouv.fr",
    url="https://github.com/etalab/jours-feries-france",
    keywords=["bank-holidays", "jours-feries", "france"],
    extras_require={"dev": ["nose"]},
    python_requires=">=2.7,<4",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
