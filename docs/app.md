# GitHub Actions Automation Bot

This is a Python script that uses OpenAI's GPT-35-TURBO API to generate a README.md file that explains the code in a repository. The README.md file will have a project description, instructions on how to install the dependencies and how to execute the code, how to contribute, and any references to external sources of information if available.

## Dependencies

This script requires the following dependencies:

- `openai`
- `dotenv`

You can install them by running:

```
pip install openai dotenv
```

## How to Use

1. Clone this repository.
2. Create an OpenAI API key and set it as an environment variable named `OPENAI_API_KEY`.
3. (Optional) Set the OpenAI API base URL as an environment variable named `OPENAI_API_BASE`.
4. (Optional) Set the directory to scan for Python files as an environment variable named `DIRECTORY`. If not set, the current directory will be used.
5. Run the script by executing `python main.py`.
6. The script will generate a `README.md` file in the root directory of the repository.

## How to Contribute

1. Fork this repository.
2. Create a new branch: `git checkout -b my-new-branch`
3. Make your changes and commit them: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-branch`
5. Submit a pull request.

## References

- [OpenAI API Documentation](https://beta.openai.com/docs/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)