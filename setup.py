from setuptools import setup, Extension
import platform

# Define the extension module
module = Extension('embed_python', sources=['embed_python.c'])

# Define the setup
setup(
    name='AI-Music-Generator-Offline',
    version='1.0',
    description='Offline AI music generator app for macOS with embedded Python and Apple M1 support',
    ext_modules=[module],
    install_requires=[
        'pyinstaller',
        'tensorflow-macos; platform_machine=="arm64"',
        'tensorflow-metal; platform_machine=="arm64"',
    ],
    entry_points={
        'console_scripts': [
            'ai-music-generator=main:main',
        ],
    },
)
