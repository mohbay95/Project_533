from setuptools import setup, find_packages

setup(
    name="snakes-and-ladders",  # Replace with your package name
    version="0.1.0",  # Update version as needed
    author="Mohammed and Vidal",
    author_email="",
    description="A snakes and ladders game package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mohbay95/Project_533",  # Update with your GitHub repo URL
    packages=find_packages(),  # Automatically finds all packages in your project
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "snakes-and-ladders=main:main",  # Replace `main` with the module containing your main function
        ]
    },
    include_package_data=True,
    install_requires=[
        # Add any required packages here
    ],
)






