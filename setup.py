from setuptools import setup, find_packages

    name="house_price_prediction",
    version="1.0.0",
    description="A machine learning project for predicting California housing prices.",
    author="Sana Ullah",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "seaborn",
        "jupyter"
    ],
)
