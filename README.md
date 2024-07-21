# VSCode Extensions Info

This script fetches information about specified VSCode extensions from the Visual Studio Marketplace and generates a Markdown table with the details.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/vscode-extensions-info.git
   cd vscode-extensions-info
   ```

2. Add your VSCode extension IDs in the `generate_vscode_extensions_table.py` script.

3. Run the script:

   ```bash
   python generate_vscode_extensions_table.py
   ```

4. The generated Markdown table will be saved in `extensions_table.md`.

## Example

```markdown
| Unique Identifier       | Marketplace Link                                                                           | VSCode Install Link                                    | Short Description                                                            |
| ----------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------ | ---------------------------------------------------------------------------- |
| eamodio.gitlens         | [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)             | [gitlens](vscode:extension/eamodio.gitlens)            | Supercharge the Git capabilities built into Visual Studio Code.              |
| donjayamanne.githistory | [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory) | [githistory](vscode:extension/donjayamanne.githistory) | View and search git log along with the graph and details.                    |
| mhutchie.git-graph      | [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)        | [git-graph](vscode:extension/mhutchie.git-graph)       | View a Git Graph of your repository, and perform Git actions from the graph. |
```
